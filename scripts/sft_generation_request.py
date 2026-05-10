# accepted 샘플에서 기존 paraphrase들을 읽어 teacher LLM 생성 요청 payload를 만든다.
# 숫자 path는 sft_taxonomy.py로 검증하고, 내부 처리는 stable path 기준으로 수행한다.
# selected_bucket에는 선택된 분류와 설명만 넣고, source_ref는 LLM 입력에서 제외한다.
# command_style은 accepted sample의 metadata에서 command_text와 함께 추출한다.

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

try:
    from sft_taxonomy import (
        DEFAULT_TAXONOMY_PATH,
        GeneralPath,
        SkillPath,
        conflict_type_to_key,
        get_selected_bucket_descriptions,
        load_taxonomy,
        parse_generation_request,
    )
    from sft_coverage_report import (
        DEFAULT_ACCEPTED_DIR,
        DEFAULT_DATASET_ROOT,
        get_base_command_text,
        get_edge_flags,
        get_general_path,
        get_metadata,
        get_skill_path,
        load_accepted_samples,
    )
except ImportError:
    import sys

    sys.path.append(str(Path(__file__).resolve().parent))
    from sft_taxonomy import (
        DEFAULT_TAXONOMY_PATH,
        GeneralPath,
        SkillPath,
        conflict_type_to_key,
        get_selected_bucket_descriptions,
        load_taxonomy,
        parse_generation_request,
    )
    from sft_coverage_report import (
        DEFAULT_ACCEPTED_DIR,
        DEFAULT_DATASET_ROOT,
        get_base_command_text,
        get_edge_flags,
        get_general_path,
        get_metadata,
        get_skill_path,
        load_accepted_samples,
    )

DEFAULT_REQUEST_OUTPUT_DIR = DEFAULT_DATASET_ROOT / "raw_generations"

DEFAULT_SKILL_FLAGS: dict[str, dict[str, bool]] = {
    "enemy_single_target_attack": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "self_buff": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "ally_shield": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "ally_heal": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "ally_resurrection": {"is_skill_aoe": False, "can_skill_target_dead": True},
    "enemy_aoe_attack": {"is_skill_aoe": True, "can_skill_target_dead": False},
    "enemy_debuff": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "mobility_skill": {"is_skill_aoe": False, "can_skill_target_dead": False},
    "no_skill": {"is_skill_aoe": False, "can_skill_target_dead": False},
}


def sample_command_text(sample: dict[str, Any]) -> str:
    command_spec = sample.get("command_spec")
    if isinstance(command_spec, dict):
        command_text = command_spec.get("command_text")
        if isinstance(command_text, str) and command_text:
            return command_text

    input_obj = sample.get("input")
    if isinstance(input_obj, dict):
        nested = input_obj.get("input")
        if isinstance(nested, dict):
            command = nested.get("command")
            if isinstance(command, str) and command:
                return command

    return get_base_command_text(sample)


def sample_command_style(sample: dict[str, Any]) -> str:
    metadata = get_metadata(sample)
    value = metadata.get("command_style")
    if isinstance(value, str) and value:
        return value
    return "direct_korean"


def general_path_matches(sample: dict[str, Any], path: GeneralPath) -> bool:
    return get_general_path(sample) == (
        path.topic,
        path.actor_selection,
        path.target_selection,
        path.action_pattern,
        path.scenario_family,
    )


def group_command_slots(
    samples: list[dict[str, Any]],
    path: GeneralPath,
) -> list[tuple[str, tuple[str, ...], list[dict[str, Any]]]]:
    groups: dict[tuple[str, tuple[str, ...]], list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        if not general_path_matches(sample, path):
            continue
        key = (get_base_command_text(sample), get_edge_flags(sample))
        groups[key].append(sample)

    rows: list[tuple[str, tuple[str, ...], list[dict[str, Any]]]] = []
    for (base_command_text, edge_flags), grouped_samples in groups.items():
        rows.append((base_command_text, edge_flags, grouped_samples))

    return sorted(rows, key=lambda item: item[0])


def get_command_slot_samples(
    samples: list[dict[str, Any]],
    path: GeneralPath,
) -> tuple[str, tuple[str, ...], list[dict[str, Any]]]:
    rows = group_command_slots(samples, path)
    index = path.command_slot_index
    if not rows:
        raise ValueError(f"No accepted command slots found for general path: {path.stable_path}")
    if index < 1 or index > len(rows):
        raise ValueError(
            f"command_slot_index out of range for {path.stable_path}: {index}. Available rows: {len(rows)}"
        )
    return rows[index - 1]


def infer_skill_path_from_samples(samples: list[dict[str, Any]]) -> Optional[SkillPath]:
    skill_paths = {get_skill_path(sample) for sample in samples}
    skill_paths.discard(None)
    if not skill_paths:
        return None
    if len(skill_paths) > 1:
        raise ValueError(
            "Selected command slot contains multiple skill paths. Use an explicit skill override."
        )

    family, target_kind, conflict_key = next(iter(skill_paths))
    return SkillPath(
        skill_family=family,
        skill_target_kind=target_kind,
        conflict_type=None if conflict_key == "null" else conflict_key,
    )


def infer_skill_flags_from_samples(
    samples: list[dict[str, Any]],
    skill_path: SkillPath,
) -> dict[str, bool]:
    for sample in samples:
        skill_case = sample.get("skill_case")
        if not isinstance(skill_case, dict):
            continue
        if skill_case.get("skill_family") != skill_path.skill_family:
            continue
        if skill_case.get("skill_target_kind") != skill_path.skill_target_kind:
            continue
        conflict = skill_case.get("conflict_type")
        if conflict != skill_path.conflict_type:
            continue

        is_aoe = skill_case.get("is_skill_aoe")
        can_dead = skill_case.get("can_skill_target_dead")
        if isinstance(is_aoe, bool) and isinstance(can_dead, bool):
            return {
                "is_skill_aoe": is_aoe,
                "can_skill_target_dead": can_dead,
            }

    return dict(DEFAULT_SKILL_FLAGS.get(skill_path.skill_family, {"is_skill_aoe": False, "can_skill_target_dead": False}))


def attach_skill_case_fields(
    selected_bucket: dict[str, Any],
    skill_path: Optional[SkillPath],
    samples: list[dict[str, Any]],
) -> dict[str, Any]:
    selected_bucket = dict(selected_bucket)
    if skill_path is None:
        selected_bucket["skill_case"] = None
        return selected_bucket

    skill_case = selected_bucket.get("skill_case")
    if not isinstance(skill_case, dict):
        skill_case = {}

    flags = infer_skill_flags_from_samples(samples, skill_path)
    skill_case["skill_family"] = skill_path.skill_family
    skill_case["skill_target_kind"] = skill_path.skill_target_kind
    skill_case["is_skill_aoe"] = flags["is_skill_aoe"]
    skill_case["can_skill_target_dead"] = flags["can_skill_target_dead"]
    skill_case["conflict_type"] = skill_path.conflict_type
    selected_bucket["skill_case"] = skill_case
    return selected_bucket


def build_existing_paraphrase_samples(samples: list[dict[str, Any]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    result: list[dict[str, str]] = []

    for sample in samples:
        command_text = sample_command_text(sample)
        command_style = sample_command_style(sample)
        key = (command_text, command_style)
        if key in seen:
            continue
        seen.add(key)
        result.append(
            {
                "command_text": command_text,
                "command_style": command_style,
            }
        )

    return result


def build_generation_payload(
    raw_request: str,
    dataset_root: Path = DEFAULT_DATASET_ROOT,
    taxonomy_path: Path = DEFAULT_TAXONOMY_PATH,
) -> dict[str, Any]:
    taxonomy = load_taxonomy(taxonomy_path)
    parsed = parse_generation_request(raw_request, taxonomy)
    samples = load_accepted_samples(dataset_root / "accepted")
    base_command_text, edge_flags, command_slot_samples = get_command_slot_samples(
        samples=samples,
        path=parsed.general_path,
    )

    skill_path = parsed.skill_path
    if skill_path is None and parsed.general_path.topic == "skill":
        skill_path = infer_skill_path_from_samples(command_slot_samples)
        if skill_path is None:
            raise ValueError("Skill topic request requires skill_path or accepted samples with skill_case.")

    selected_bucket = get_selected_bucket_descriptions(
        taxonomy=taxonomy,
        general_path=parsed.general_path,
        skill_path=skill_path,
        edge_flags=list(edge_flags),
    )
    selected_bucket = attach_skill_case_fields(
        selected_bucket=selected_bucket,
        skill_path=skill_path,
        samples=command_slot_samples,
    )

    return {
        "request": {
            "raw_request": parsed.raw_request,
            "count_to_generate": parsed.count,
            "display_path": parsed.raw_request.split(".")[0].removeprefix("c"),
            "stable_path": parsed.general_path.stable_path,
            "skill_stable_path": None if skill_path is None else skill_path.stable_path,
            "command_slot_index": parsed.general_path.command_slot_index,
            "base_command_text": base_command_text,
        },
        "selected_bucket": selected_bucket,
        "existing_valid_paraphrase_samples": build_existing_paraphrase_samples(command_slot_samples),
        "count_to_generate": parsed.count,
        "generation_constraints": [
            "Create new paraphrased commands and matching dataset samples for the selected_bucket only.",
            "Preserve the same scenario meaning and edge_flags as selected_bucket.",
            "Do not include source_ref in generated samples.",
            "Do not invent taxonomy values outside selected_bucket.",
            "Generated output labels must be raw valid assistant outputs, not sanitizer-repaired outputs.",
        ],
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def make_default_output_path(output_dir: Path, raw_request: str) -> Path:
    safe = raw_request.replace("/", "_").replace(".", "_").replace("-", "-")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return output_dir / f"generation_request_{timestamp}_{safe}.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", help="Generation request, e.g. c1-2-1-3-1-10.4")
    parser.add_argument("--dataset-root", default=str(DEFAULT_DATASET_ROOT))
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY_PATH))
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    dataset_root = Path(args.dataset_root)
    payload = build_generation_payload(
        raw_request=args.request,
        dataset_root=dataset_root,
        taxonomy_path=Path(args.taxonomy),
    )

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = make_default_output_path(dataset_root / "raw_generations", args.request)

    write_json(output_path, payload)
    print(f"generation_request: {output_path}")


if __name__ == "__main__":
    main()
