# teacher가 생성한 master sample 후보를 검증해 accepted/rejected JSONL로 분류한다.
# parse/schema/runtime/policy/semantic/taxonomy 검사를 한 번에 수행한다.
# sanitizer repair를 전제로 한 label은 accepted에 넣지 않는다.
# 현재 런타임 입력 구조: input + commandAnalysis -> thinking/dialog/action을 기준으로 한다.

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
import hashlib

try:
    from sft_taxonomy import DEFAULT_TAXONOMY_PATH, load_taxonomy, validate_metadata_against_taxonomy
except ImportError:
    import sys

    sys.path.append(str(Path(__file__).resolve().parent))
    from sft_taxonomy import DEFAULT_TAXONOMY_PATH, load_taxonomy, validate_metadata_against_taxonomy

DEFAULT_DATASET_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ACCEPTED_DIR = DEFAULT_DATASET_ROOT / "accepted"
DEFAULT_REJECTED_DIR = DEFAULT_DATASET_ROOT / "rejected"
VALIDATION_INDEX_FILENAME = ".validated_inputs.json"

MIN_WAIT_SECONDS = 1.0
MAX_WAIT_SECONDS = 10.0
MAX_ACTIONS_PER_ACTOR = 3
ALLOWED_MOVE_SUBTYPES = {"approachOpponent", "escape", "help", "holdFront"}
ALLOWED_MOVEMENT_TYPES = {"direct", "flank"}
ALLOWED_ACTION_TYPES = {"move", "attack", "skill", "wait", "skillControl"}
EXPECTED_OUTPUT_KEYS = {"thinking", "dialog", "action"}


class ValidationContext:
    def __init__(self, sample: dict[str, Any], taxonomy: dict[str, Any]) -> None:
        self.sample = sample
        self.taxonomy = taxonomy
        self.errors: list[str] = []

    def add(self, code: str, detail: str = "") -> None:
        self.errors.append(code if not detail else f"{code}: {detail}")


def read_json_records_with_errors(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8").strip()

    if not text:
        return [], []

    valid: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []

    def add_json_value(value: Any, source_label: str) -> None:
        if isinstance(value, list):
            for index, item in enumerate(value, start=1):
                if isinstance(item, dict):
                    valid.append(item)
                else:
                    invalid.append(
                        {
                            "raw": item,
                            "failure_reasons": [f"SAMPLE_NOT_OBJECT at {source_label}[{index}]"],
                        }
                    )
            return

        if isinstance(value, dict) and isinstance(value.get("samples"), list):
            for index, item in enumerate(value["samples"], start=1):
                if isinstance(item, dict):
                    valid.append(item)
                else:
                    invalid.append(
                        {
                            "raw": item,
                            "failure_reasons": [f"SAMPLE_NOT_OBJECT at {source_label}.samples[{index}]"],
                        }
                    )
            return

        if isinstance(value, dict):
            valid.append(value)
            return

        invalid.append(
            {
                "raw": value,
                "failure_reasons": [f"ROOT_NOT_SAMPLE_OR_SAMPLE_LIST at {source_label}"],
            }
        )

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = None

    if parsed is not None:
        add_json_value(parsed, "root")
        return valid, invalid

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if not stripped:
            continue

        try:
            item = json.loads(stripped)
        except json.JSONDecodeError as error:
            invalid.append(
                {
                    "raw": stripped,
                    "failure_reasons": [f"JSON_PARSE_FAILED at line {line_number}: {error}"],
                }
            )
            continue

        add_json_value(item, f"line {line_number}")

    return valid, invalid


def get_input_payload(sample: dict[str, Any]) -> dict[str, Any]:
    value = sample.get("input")
    return value if isinstance(value, dict) else {}


def get_battle_input(sample: dict[str, Any]) -> dict[str, Any]:
    input_payload = get_input_payload(sample)
    value = input_payload.get("input")
    return value if isinstance(value, dict) else {}


def get_command_analysis(sample: dict[str, Any]) -> dict[str, Any]:
    input_payload = get_input_payload(sample)
    value = input_payload.get("commandAnalysis")
    return value if isinstance(value, dict) else {}


def get_area(sample: dict[str, Any]) -> dict[str, Any]:
    battle_input = get_battle_input(sample)
    value = battle_input.get("area_situation")
    return value if isinstance(value, dict) else {}


def get_units(sample: dict[str, Any], side: str) -> list[dict[str, Any]]:
    area = get_area(sample)
    value = area.get(side)
    return [unit for unit in value if isinstance(unit, dict)] if isinstance(value, list) else []


def get_unit_by_id(sample: dict[str, Any], unit_id: str) -> Optional[dict[str, Any]]:
    for side in ("allies", "enemies"):
        for unit in get_units(sample, side):
            if unit.get("unitId") == unit_id:
                return unit
    return None


def get_unit_side(sample: dict[str, Any], unit_id: str) -> Optional[str]:
    for unit in get_units(sample, "allies"):
        if unit.get("unitId") == unit_id:
            return "ally"
    for unit in get_units(sample, "enemies"):
        if unit.get("unitId") == unit_id:
            return "enemy"
    return None


def unit_id_set(sample: dict[str, Any], side: str) -> set[str]:
    return {unit.get("unitId") for unit in get_units(sample, side) if isinstance(unit.get("unitId"), str)}


def all_unit_ids(sample: dict[str, Any]) -> set[str]:
    return unit_id_set(sample, "allies") | unit_id_set(sample, "enemies")


def is_alive(unit: Optional[dict[str, Any]]) -> bool:
    return bool(unit and unit.get("isAlive") is True)


def is_targetable(unit: Optional[dict[str, Any]]) -> bool:
    return bool(unit and unit.get("canBeTargeted") is True)


def actor_has_skill(sample: dict[str, Any], actor_id: str) -> bool:
    unit = get_unit_by_id(sample, actor_id)
    return bool(unit and isinstance(unit.get("skillDescription"), str) and unit.get("skillDescription"))


def actor_skill_description(sample: dict[str, Any], actor_id: str) -> Optional[str]:
    unit = get_unit_by_id(sample, actor_id)
    if not unit:
        return None
    value = unit.get("skillDescription")
    return value if isinstance(value, str) and value else None


def can_actor_skill_target_dead(sample: dict[str, Any], actor_id: str) -> bool:
    unit = get_unit_by_id(sample, actor_id)
    return bool(unit and unit.get("canSkillTargetDead") is True)


def is_valid_skill_target(sample: dict[str, Any], actor_id: str, target_id: str) -> bool:
    actor = get_unit_by_id(sample, actor_id)
    target = get_unit_by_id(sample, target_id)
    if actor is None or target is None:
        return False

    target_side = get_unit_side(sample, target_id)
    is_self_skill = actor.get("IsSkillOnSelf") is True
    is_ally_skill = actor.get("IsSkillOnAlly") is True

    if is_self_skill:
        if target_id != actor_id:
            return False
    else:
        if target_id == actor_id:
            return False
        if is_ally_skill:
            if target_side != "ally":
                return False
        elif target_side != "enemy":
            return False

    if not is_targetable(target):
        return False
    if is_alive(target):
        return True
    return can_actor_skill_target_dead(sample, actor_id)


def list_from_command_analysis(sample: dict[str, Any], key: str) -> set[str]:
    command_analysis = get_command_analysis(sample)
    value = command_analysis.get(key)
    return {item for item in value if isinstance(item, str)} if isinstance(value, list) else set()


def output_action_entries(sample: dict[str, Any]) -> list[dict[str, Any]]:
    output = sample.get("output")
    if not isinstance(output, dict):
        return []
    action = output.get("action")
    return [entry for entry in action if isinstance(entry, dict)] if isinstance(action, list) else []


def iter_sequence_items(sample: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    items: list[tuple[str, dict[str, Any]]] = []
    for action_entry in output_action_entries(sample):
        actor_id = action_entry.get("unitId")
        sequence = action_entry.get("sequence")
        if not isinstance(actor_id, str) or not isinstance(sequence, list):
            continue
        for seq_item in sequence:
            if isinstance(seq_item, dict):
                items.append((actor_id, seq_item))
    return items


def validate_master_shape(ctx: ValidationContext) -> None:
    sample = ctx.sample
    for key in ["id", "split", "command_spec", "metadata", "skill_case", "gold", "input", "output"]:
        if key not in sample:
            ctx.add("MISSING_MASTER_FIELD", key)

    if not isinstance(sample.get("id"), str) or not sample.get("id"):
        ctx.add("INVALID_SAMPLE_ID")
    if sample.get("split") not in {"train", "validation", "test"}:
        ctx.add("INVALID_SPLIT")
    if not isinstance(sample.get("command_spec"), dict):
        ctx.add("COMMAND_SPEC_NOT_OBJECT")
    if not isinstance(sample.get("gold"), dict):
        ctx.add("GOLD_NOT_OBJECT")
    if not isinstance(get_input_payload(sample), dict):
        ctx.add("INPUT_NOT_OBJECT")

    command_spec = sample.get("command_spec")
    if isinstance(command_spec, dict):
        command_text = command_spec.get("command_text")
        if not isinstance(command_text, str) or not command_text:
            ctx.add("COMMAND_TEXT_MISSING")

    battle_input = get_battle_input(sample)
    if not battle_input:
        ctx.add("RUNTIME_INPUT_MISSING")
    elif not isinstance(battle_input.get("command"), str):
        ctx.add("INPUT_COMMAND_MISSING")

    if not get_units(sample, "allies"):
        ctx.add("ALLIES_MISSING_OR_EMPTY")
    if not isinstance(get_area(sample).get("enemies"), list):
        ctx.add("ENEMIES_MISSING")

    command_analysis = get_command_analysis(sample)
    if not command_analysis:
        ctx.add("COMMAND_ANALYSIS_MISSING")
    else:
        for key in ["allowedActors", "allowedAttackTargets", "validMoveToUnits", "invalidUnits", "actionPolicy"]:
            if key not in command_analysis:
                ctx.add("COMMAND_ANALYSIS_FIELD_MISSING", key)


def validate_taxonomy(ctx: ValidationContext) -> None:
    for error in validate_metadata_against_taxonomy(ctx.sample, ctx.taxonomy):
        ctx.add("TAXONOMY_INVALID", error)

    skill_case = ctx.sample.get("skill_case")
    if isinstance(skill_case, dict):
        if not isinstance(skill_case.get("is_skill_aoe"), bool):
            ctx.add("SKILL_CASE_AOE_NOT_BOOL")
        if not isinstance(skill_case.get("can_skill_target_dead"), bool):
            ctx.add("SKILL_CASE_CAN_TARGET_DEAD_NOT_BOOL")


def validate_output_schema(ctx: ValidationContext) -> None:
    sample = ctx.sample
    output = sample.get("output")
    if not isinstance(output, dict):
        ctx.add("OUTPUT_NOT_OBJECT")
        return

    if set(output.keys()) != EXPECTED_OUTPUT_KEYS:
        ctx.add("TOP_LEVEL_OUTPUT_KEYS_INVALID", str(sorted(output.keys())))

    if not isinstance(output.get("thinking"), str):
        ctx.add("THINKING_NOT_STRING")

    dialog = output.get("dialog")
    if not isinstance(dialog, list):
        ctx.add("DIALOG_NOT_ARRAY")
        dialog = []

    action = output.get("action")
    if not isinstance(action, list):
        ctx.add("ACTION_NOT_ARRAY")
        action = []

    seen_action_actors: set[str] = set()
    for action_entry in action:
        if not isinstance(action_entry, dict):
            ctx.add("ACTION_ITEM_NOT_OBJECT")
            continue
        if set(action_entry.keys()) != {"unitId", "sequence"}:
            ctx.add("INVALID_ACTION_KEYS", str(sorted(action_entry.keys())))

        actor_id = action_entry.get("unitId")
        sequence = action_entry.get("sequence")
        if not isinstance(actor_id, str):
            ctx.add("ACTION_UNIT_ID_NOT_STRING")
        else:
            if actor_id in seen_action_actors:
                ctx.add("ACTION_DUPLICATED_ACTOR", actor_id)
            seen_action_actors.add(actor_id)

        if not isinstance(sequence, list):
            ctx.add("SEQUENCE_NOT_ARRAY", str(actor_id))
            continue
        if len(sequence) > MAX_ACTIONS_PER_ACTOR:
            ctx.add("SEQUENCE_TOO_LONG", str(actor_id))

        for seq_item in sequence:
            if not isinstance(seq_item, dict):
                ctx.add("SEQUENCE_ITEM_NOT_OBJECT", str(actor_id))
                continue
            validate_sequence_schema(ctx, actor_id if isinstance(actor_id, str) else "", seq_item)

    for dialog_entry in dialog:
        if not isinstance(dialog_entry, dict):
            ctx.add("DIALOG_ITEM_NOT_OBJECT")
            continue
        if set(dialog_entry.keys()) != {"unitId", "text"}:
            ctx.add("INVALID_DIALOG_KEYS", str(sorted(dialog_entry.keys())))
        if not isinstance(dialog_entry.get("unitId"), str):
            ctx.add("DIALOG_UNIT_ID_NOT_STRING")
        if not isinstance(dialog_entry.get("text"), str):
            ctx.add("DIALOG_TEXT_NOT_STRING")


def validate_sequence_schema(ctx: ValidationContext, actor_id: str, seq_item: dict[str, Any]) -> None:
    action_type = seq_item.get("type")
    if action_type not in ALLOWED_ACTION_TYPES:
        ctx.add("UNKNOWN_ACTION_TYPE", str(action_type))
        return

    if action_type == "move":
        if set(seq_item.keys()) != {"type", "subtype", "movementType", "to"}:
            ctx.add("INVALID_MOVE_KEYS", str(sorted(seq_item.keys())))
        if seq_item.get("subtype") not in ALLOWED_MOVE_SUBTYPES:
            ctx.add("INVALID_MOVE_SUBTYPE", str(seq_item.get("subtype")))
        if seq_item.get("movementType") not in ALLOWED_MOVEMENT_TYPES:
            ctx.add("INVALID_MOVEMENT_TYPE", str(seq_item.get("movementType")))
        if not isinstance(seq_item.get("to"), str):
            ctx.add("MOVE_TO_NOT_STRING", actor_id)
        return

    if action_type == "attack":
        if set(seq_item.keys()) != {"type", "target"}:
            ctx.add("INVALID_ATTACK_KEYS", str(sorted(seq_item.keys())))
        if not isinstance(seq_item.get("target"), str):
            ctx.add("ATTACK_TARGET_NOT_STRING", actor_id)
        return

    if action_type == "skill":
        if set(seq_item.keys()) != {"type", "description", "target"}:
            ctx.add("INVALID_SKILL_KEYS", str(sorted(seq_item.keys())))
        if not isinstance(seq_item.get("description"), str):
            ctx.add("SKILL_DESCRIPTION_NOT_STRING", actor_id)
        if not isinstance(seq_item.get("target"), str):
            ctx.add("SKILL_TARGET_NOT_STRING", actor_id)
        return

    if action_type == "wait":
        if set(seq_item.keys()) != {"type", "durationSec"}:
            ctx.add("INVALID_WAIT_KEYS", str(sorted(seq_item.keys())))
        duration = seq_item.get("durationSec")
        if isinstance(duration, bool) or not isinstance(duration, (int, float)):
            ctx.add("WAIT_DURATION_NOT_NUMBER", actor_id)
        elif duration < MIN_WAIT_SECONDS or duration > MAX_WAIT_SECONDS:
            ctx.add("WAIT_DURATION_OUT_OF_RANGE", str(duration))
        return

    if action_type == "skillControl":
        mode = seq_item.get("mode")
        if mode == "defer":
            if set(seq_item.keys()) != {"type", "mode", "durationSec"}:
                ctx.add("INVALID_SKILL_CONTROL_DEFER_KEYS", str(sorted(seq_item.keys())))
            duration = seq_item.get("durationSec")
            if isinstance(duration, bool) or not isinstance(duration, (int, float)):
                ctx.add("SKILL_CONTROL_DURATION_NOT_NUMBER", actor_id)
            elif duration < MIN_WAIT_SECONDS or duration > MAX_WAIT_SECONDS:
                ctx.add("SKILL_CONTROL_DURATION_OUT_OF_RANGE", str(duration))
        elif mode == "forbid":
            if set(seq_item.keys()) != {"type", "mode"}:
                ctx.add("INVALID_SKILL_CONTROL_FORBID_KEYS", str(sorted(seq_item.keys())))
        else:
            ctx.add("INVALID_SKILL_CONTROL_MODE", str(mode))


def validate_runtime(ctx: ValidationContext) -> None:
    sample = ctx.sample
    ally_ids = unit_id_set(sample, "allies")
    enemy_ids = unit_id_set(sample, "enemies")
    all_ids = all_unit_ids(sample)
    allowed_actors = list_from_command_analysis(sample, "allowedActors")
    allowed_attack_targets = list_from_command_analysis(sample, "allowedAttackTargets")
    valid_move_to_units = list_from_command_analysis(sample, "validMoveToUnits")

    for action_entry in output_action_entries(sample):
        actor_id = action_entry.get("unitId")
        if not isinstance(actor_id, str):
            continue

        actor_unit = get_unit_by_id(sample, actor_id)
        if actor_id not in ally_ids:
            ctx.add("ACTOR_NOT_ALLY", actor_id)
        if not is_alive(actor_unit):
            ctx.add("ACTOR_DEAD", actor_id)
        if actor_id not in allowed_actors:
            ctx.add("ACTOR_OUTSIDE_ALLOWED_ACTORS", actor_id)

        sequence = action_entry.get("sequence")
        if not isinstance(sequence, list):
            continue

        for seq_item in sequence:
            if not isinstance(seq_item, dict):
                continue
            action_type = seq_item.get("type")

            if action_type == "move":
                to_id = seq_item.get("to")
                if not isinstance(to_id, str):
                    continue
                if to_id == actor_id:
                    ctx.add("MOVE_TO_SELF", actor_id)
                if to_id not in all_ids:
                    ctx.add("MOVE_TO_NOT_FOUND", to_id)
                if to_id not in valid_move_to_units:
                    ctx.add("MOVE_TO_OUTSIDE_VALID_MOVE_TO_UNITS", to_id)
                target_unit = get_unit_by_id(sample, to_id)
                if get_unit_side(sample, to_id) == "enemy" and (not is_alive(target_unit) or not is_targetable(target_unit)):
                    ctx.add("MOVE_TO_INVALID_ENEMY", to_id)
                if get_unit_side(sample, to_id) == "ally" and not is_alive(target_unit):
                    ctx.add("MOVE_TO_DEAD_ALLY", to_id)

            elif action_type == "attack":
                target = seq_item.get("target")
                if not isinstance(target, str):
                    continue
                target_unit = get_unit_by_id(sample, target)
                if target not in enemy_ids:
                    ctx.add("ATTACK_TARGET_NOT_ENEMY", target)
                if not is_alive(target_unit):
                    ctx.add("ATTACK_TARGET_DEAD", target)
                if not is_targetable(target_unit):
                    ctx.add("ATTACK_TARGET_UNTARGETABLE", target)
                if target not in allowed_attack_targets:
                    ctx.add("ATTACK_TARGET_OUTSIDE_ALLOWED_TARGETS", target)

            elif action_type == "skill":
                target = seq_item.get("target")
                description = seq_item.get("description")
                if not actor_has_skill(sample, actor_id):
                    ctx.add("SKILL_ACTOR_HAS_NO_SKILL", actor_id)
                    continue
                expected_description = actor_skill_description(sample, actor_id)
                if description != expected_description:
                    ctx.add("SKILL_DESCRIPTION_MISMATCH", actor_id)
                if not isinstance(target, str) or target not in all_ids:
                    ctx.add("SKILL_TARGET_NOT_FOUND", str(target))
                elif not is_valid_skill_target(sample, actor_id, target):
                    ctx.add("SKILL_TARGET_INVALID", f"{actor_id}->{target}")

            elif action_type == "skillControl":
                if not actor_has_skill(sample, actor_id):
                    ctx.add("SKILL_CONTROL_ACTOR_HAS_NO_SKILL", actor_id)


def validate_policy(ctx: ValidationContext) -> None:
    sample = ctx.sample
    action_actor_ids: list[str] = []
    for action_entry in output_action_entries(sample):
        actor_id = action_entry.get("unitId")
        if isinstance(actor_id, str):
            action_actor_ids.append(actor_id)
        sequence = action_entry.get("sequence")
        if not isinstance(sequence, list):
            continue
        for index, seq_item in enumerate(sequence):
            if not isinstance(seq_item, dict):
                continue
            if seq_item.get("type") == "wait" and index > 0:
                previous = sequence[index - 1]
                if isinstance(previous, dict) and previous.get("type") == "attack":
                    ctx.add("WAIT_AFTER_ATTACK", str(actor_id))
                if isinstance(previous, dict) and previous.get("type") == "skill":
                    ctx.add("WAIT_AFTER_SKILL", str(actor_id))

    output = sample.get("output")
    if not isinstance(output, dict):
        return
    dialog = output.get("dialog")
    if not isinstance(dialog, list):
        return

    action_actor_set = set(action_actor_ids)
    dialog_ids: list[str] = []
    for dialog_entry in dialog:
        if not isinstance(dialog_entry, dict):
            continue
        unit_id = dialog_entry.get("unitId")
        if isinstance(unit_id, str):
            dialog_ids.append(unit_id)
            if unit_id not in action_actor_set:
                ctx.add("DIALOG_UNIT_MISMATCH", unit_id)

    if not action_actor_ids and dialog:
        ctx.add("EMPTY_ACTION_DIALOG_NOT_EMPTY")

    for actor_id in action_actor_set:
        if dialog_ids.count(actor_id) != 1:
            ctx.add("DIALOG_MISSING_OR_DUPLICATED_FOR_ACTOR", actor_id)

    for dialog_id in set(dialog_ids):
        if dialog_ids.count(dialog_id) > 1:
            ctx.add("DIALOG_DUPLICATED_UNIT", dialog_id)


def sequence_action_types(sample: dict[str, Any]) -> list[str]:
    return [seq_item.get("type") for _, seq_item in iter_sequence_items(sample) if isinstance(seq_item.get("type"), str)]


def used_targets(sample: dict[str, Any]) -> set[str]:
    targets: set[str] = set()
    for _, seq_item in iter_sequence_items(sample):
        for key in ["target", "to"]:
            value = seq_item.get(key)
            if isinstance(value, str):
                targets.add(value)
    return targets


def validate_semantic_gold(ctx: ValidationContext) -> None:
    sample = ctx.sample
    gold = sample.get("gold")
    if not isinstance(gold, dict):
        return

    action_actors = [entry.get("unitId") for entry in output_action_entries(sample) if isinstance(entry.get("unitId"), str)]
    action_actor_set = set(action_actors)
    action_types = sequence_action_types(sample)
    action_type_set = set(action_types)
    target_set = used_targets(sample)

    required_actors = set(gold.get("required_actors", [])) if isinstance(gold.get("required_actors"), list) else set()
    allowed_actors = set(gold.get("allowed_actors", [])) if isinstance(gold.get("allowed_actors"), list) else set()
    forbidden_actors = set(gold.get("forbidden_actors", [])) if isinstance(gold.get("forbidden_actors"), list) else set()

    if required_actors and not required_actors.issubset(action_actor_set):
        ctx.add("SEMANTIC_ACTOR_MISMATCH", f"missing={sorted(required_actors - action_actor_set)}")
    if allowed_actors and not action_actor_set.issubset(allowed_actors):
        ctx.add("SEMANTIC_ACTOR_OUTSIDE_ALLOWED", f"extra={sorted(action_actor_set - allowed_actors)}")
    if forbidden_actors & action_actor_set:
        ctx.add("SEMANTIC_FORBIDDEN_ACTOR_USED", f"used={sorted(forbidden_actors & action_actor_set)}")

    required_types = set(gold.get("required_action_types", [])) if isinstance(gold.get("required_action_types"), list) else set()
    allowed_types = set(gold.get("allowed_action_types", [])) if isinstance(gold.get("allowed_action_types"), list) else set()
    forbidden_types = set(gold.get("forbidden_action_types", [])) if isinstance(gold.get("forbidden_action_types"), list) else set()

    if required_types and not required_types.issubset(action_type_set):
        ctx.add("SEMANTIC_ACTION_TYPE_MISMATCH", f"missing={sorted(required_types - action_type_set)}")
    if allowed_types and not action_type_set.issubset(allowed_types):
        ctx.add("SEMANTIC_ACTION_TYPE_OUTSIDE_ALLOWED", f"extra={sorted(action_type_set - allowed_types)}")
    if forbidden_types & action_type_set:
        ctx.add("SEMANTIC_FORBIDDEN_ACTION_TYPE_USED", f"used={sorted(forbidden_types & action_type_set)}")

    empty_action_allowed = gold.get("empty_action_allowed")
    if empty_action_allowed is False and not action_actors:
        ctx.add("SEMANTIC_UNEXPECTED_EMPTY_ACTION")
    if empty_action_allowed is True and action_actors and gold.get("expected_action_pattern") == "empty_action_expected":
        ctx.add("SEMANTIC_EMPTY_ACTION_MISMATCH")

    targets = gold.get("targets")
    if isinstance(targets, dict):
        required_targets = set(targets.get("required", [])) if isinstance(targets.get("required"), list) else set()
        allowed_targets = set(targets.get("allowed", [])) if isinstance(targets.get("allowed"), list) else set()
        forbidden_targets = set(targets.get("forbidden", [])) if isinstance(targets.get("forbidden"), list) else set()
        if required_targets and not required_targets.issubset(target_set):
            ctx.add("SEMANTIC_TARGET_MISMATCH", f"missing={sorted(required_targets - target_set)}")
        if allowed_targets and not target_set.issubset(allowed_targets):
            ctx.add("SEMANTIC_TARGET_OUTSIDE_ALLOWED", f"extra={sorted(target_set - allowed_targets)}")
        if forbidden_targets & target_set:
            ctx.add("SEMANTIC_FORBIDDEN_TARGET_USED", f"used={sorted(forbidden_targets & target_set)}")

    validate_gold_action_details(ctx, gold)


def validate_gold_action_details(ctx: ValidationContext, gold: dict[str, Any]) -> None:
    for actor_id, seq_item in iter_sequence_items(ctx.sample):
        action_type = seq_item.get("type")
        if action_type == "move" and isinstance(gold.get("move"), dict):
            move_gold = gold["move"]
            if move_gold.get("actor") and actor_id != move_gold.get("actor"):
                continue
            if move_gold.get("required_subtype") and seq_item.get("subtype") != move_gold.get("required_subtype"):
                ctx.add("SEMANTIC_MOVE_SUBTYPE_MISMATCH", actor_id)
            if move_gold.get("required_to") and seq_item.get("to") != move_gold.get("required_to"):
                ctx.add("SEMANTIC_MOVE_TO_MISMATCH", actor_id)

        if action_type == "attack" and isinstance(gold.get("attack"), dict):
            attack_gold = gold["attack"]
            if attack_gold.get("actor") and actor_id != attack_gold.get("actor"):
                continue
            if attack_gold.get("required_target") and seq_item.get("target") != attack_gold.get("required_target"):
                ctx.add("SEMANTIC_ATTACK_TARGET_MISMATCH", actor_id)

        if action_type == "skill" and isinstance(gold.get("skill"), dict):
            skill_gold = gold["skill"]
            if skill_gold.get("actor") and actor_id != skill_gold.get("actor"):
                continue
            if skill_gold.get("required_target") and seq_item.get("target") != skill_gold.get("required_target"):
                ctx.add("SEMANTIC_SKILL_TARGET_MISMATCH", actor_id)
            if skill_gold.get("description_exact") and seq_item.get("description") != skill_gold.get("description_exact"):
                ctx.add("SEMANTIC_SKILL_DESCRIPTION_MISMATCH", actor_id)

        if action_type == "skillControl" and isinstance(gold.get("skillControl"), dict):
            control_gold = gold["skillControl"]
            if control_gold.get("actor") and actor_id != control_gold.get("actor"):
                continue
            if control_gold.get("required_mode") and seq_item.get("mode") != control_gold.get("required_mode"):
                ctx.add("SEMANTIC_SKILL_CONTROL_MODE_MISMATCH", actor_id)


def validate_sample(sample: dict[str, Any], taxonomy: dict[str, Any]) -> list[str]:
    ctx = ValidationContext(sample, taxonomy)
    validate_master_shape(ctx)
    validate_taxonomy(ctx)
    validate_output_schema(ctx)
    validate_runtime(ctx)
    validate_policy(ctx)
    validate_semantic_gold(ctx)
    return ctx.errors


def normalize_sample_with_result(sample: dict[str, Any], passed: bool, errors: list[str]) -> dict[str, Any]:
    result = dict(sample)
    result["validator_result"] = {
        "passed": passed,
        "failure_reasons": errors,
    }
    return result


def append_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    if not records:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def load_validation_index(dataset_root: Path) -> dict[str, Any]:
    path = dataset_root / VALIDATION_INDEX_FILENAME
    if not path.exists():
        return {"validated_inputs": {}}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"validated_inputs": {}}

    if not isinstance(data, dict):
        return {"validated_inputs": {}}

    if not isinstance(data.get("validated_inputs"), dict):
        data["validated_inputs"] = {}

    return data


def save_validation_index(dataset_root: Path, index: dict[str, Any]) -> None:
    path = dataset_root / VALIDATION_INDEX_FILENAME
    path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

def validate_file(
    input_path: Path,
    dataset_root: Path = DEFAULT_DATASET_ROOT,
    taxonomy_path: Path = DEFAULT_TAXONOMY_PATH,
    write_outputs: bool = True,
) -> dict[str, Any]:
    input_hash = file_sha256(input_path)

    if write_outputs:
        validation_index = load_validation_index(dataset_root)
        validated_inputs = validation_index["validated_inputs"]

        if input_hash in validated_inputs:
            return {
                "input_path": str(input_path),
                "input_hash": input_hash,
                "skipped": True,
                "reason": "INPUT_ALREADY_VALIDATED",
                "previous_result": validated_inputs[input_hash],
            }
    else:
        validation_index = {"validated_inputs": {}}

    taxonomy = load_taxonomy(taxonomy_path)
    samples, parse_failures = read_json_records_with_errors(input_path)

    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    for failure in parse_failures:
        rejected.append(
            {
                "id": "parse_failed",
                "raw": failure.get("raw"),
                "validator_result": {
                    "passed": False,
                    "failure_reasons": failure.get("failure_reasons", ["JSON_PARSE_FAILED"]),
                },
            }
        )

    for sample in samples:
        errors = validate_sample(sample, taxonomy)
        if errors:
            rejected.append(normalize_sample_with_result(sample, False, errors))
        else:
            accepted.append(normalize_sample_with_result(sample, True, []))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    accepted_path = dataset_root / "accepted" / f"accepted_{timestamp}.jsonl"
    rejected_path = dataset_root / "rejected" / f"rejected_{timestamp}.jsonl"

    result = {
        "input_path": str(input_path),
        "input_hash": input_hash,
        "skipped": False,
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
        "accepted_path": str(accepted_path) if accepted else None,
        "rejected_path": str(rejected_path) if rejected else None,
    }

    if write_outputs:
        append_jsonl(accepted_path, accepted)
        append_jsonl(rejected_path, rejected)

        validation_index["validated_inputs"][input_hash] = result
        save_validation_index(dataset_root, validation_index)

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Teacher output JSON/JSONL file path.")
    parser.add_argument("--dataset-root", default=str(DEFAULT_DATASET_ROOT))
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY_PATH))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = validate_file(
        input_path=Path(args.input),
        dataset_root=Path(args.dataset_root),
        taxonomy_path=Path(args.taxonomy),
        write_outputs=not args.dry_run,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
