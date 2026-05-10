# accepted JSONL 샘플을 읽어 general/skill coverage markdown을 재생성한다.
# taxonomy_sot.json의 목표 비율과 현재 비율/개수를 함께 표시한다.
# taxonomy_sot.md와 coverage_summary.md도 같은 SOT 기준으로 생성한다.
# command_style은 coverage row에 쓰지 않고, accepted sample 내부 metadata로만 집계한다.

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Optional

try:
    from sft_taxonomy import DEFAULT_TAXONOMY_PATH, load_taxonomy, validate_metadata_against_taxonomy
except ImportError:
    import sys

    sys.path.append(str(Path(__file__).resolve().parent))
    from sft_taxonomy import DEFAULT_TAXONOMY_PATH, load_taxonomy, validate_metadata_against_taxonomy

DEFAULT_DATASET_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ACCEPTED_DIR = DEFAULT_DATASET_ROOT / "accepted"
DEFAULT_REPORTS_DIR = DEFAULT_DATASET_ROOT / "reports"

GENERAL_LEVELS = [
    "intent_family",
    "actor_selection",
    "target_selection",
    "action_pattern",
    "scenario_family",
]
SKILL_LEVELS = ["skill_family", "skill_target_kind", "conflict_type"]


def read_json_records(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []

    records: list[dict[str, Any]] = []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError(f"JSON array file must contain objects: {path}")
        for item in data:
            if isinstance(item, dict):
                records.append(item)
        return records

    if text.startswith("{") and "\n" not in text:
        data = json.loads(text)
        if isinstance(data, dict) and isinstance(data.get("samples"), list):
            return [item for item in data["samples"] if isinstance(item, dict)]
        if isinstance(data, dict):
            return [data]

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            item = json.loads(stripped)
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSONL at {path}:{line_number}") from error
        if isinstance(item, dict):
            records.append(item)

    return records


def load_accepted_samples(accepted_dir: Path) -> list[dict[str, Any]]:
    samples: list[dict[str, Any]] = []
    for path in sorted(accepted_dir.glob("*.jsonl")):
        for sample in read_json_records(path):
            sample = dict(sample)
            sample["__source_file"] = path.name
            samples.append(sample)
    return samples


def get_metadata(sample: dict[str, Any]) -> dict[str, Any]:
    metadata = sample.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def get_skill_case(sample: dict[str, Any]) -> Optional[dict[str, Any]]:
    skill_case = sample.get("skill_case")
    return skill_case if isinstance(skill_case, dict) else None


def get_sample_id(sample: dict[str, Any], fallback_index: int = 0) -> str:
    value = sample.get("id")
    if isinstance(value, str) and value:
        return value
    return f"sample_missing_id_{fallback_index:06d}"


def get_source_ref(sample: dict[str, Any], fallback_index: int = 0) -> str:
    source_file = sample.get("__source_file")
    if not isinstance(source_file, str) or not source_file:
        source_file = "unknown.jsonl"
    return f"{source_file}_{get_sample_id(sample, fallback_index)}"


def get_base_command_text(sample: dict[str, Any]) -> str:
    command_spec = sample.get("command_spec")
    if isinstance(command_spec, dict):
        base_command = command_spec.get("base_command_text")
        if isinstance(base_command, str) and base_command:
            return base_command
        command_text = command_spec.get("command_text")
        if isinstance(command_text, str) and command_text:
            return command_text

    input_obj = sample.get("input")
    if isinstance(input_obj, dict):
        nested_input = input_obj.get("input")
        if isinstance(nested_input, dict):
            command = nested_input.get("command")
            if isinstance(command, str) and command:
                return command

    return "<missing command>"


def get_edge_flags(sample: dict[str, Any]) -> tuple[str, ...]:
    metadata = get_metadata(sample)
    edge_flags = metadata.get("edge_flags", [])
    if not isinstance(edge_flags, list):
        return tuple()
    return tuple(flag for flag in edge_flags if isinstance(flag, str))


def get_general_path(sample: dict[str, Any]) -> tuple[str, str, str, str, str]:
    metadata = get_metadata(sample)
    return (
        str(metadata.get("intent_family", "unknown")),
        str(metadata.get("actor_selection", "unknown")),
        str(metadata.get("target_selection", "unknown")),
        str(metadata.get("action_pattern", "unknown")),
        str(metadata.get("scenario_family", "unknown")),
    )


def get_skill_path(sample: dict[str, Any]) -> Optional[tuple[str, str, str]]:
    skill_case = get_skill_case(sample)
    if skill_case is None:
        return None
    conflict_type = skill_case.get("conflict_type")
    return (
        str(skill_case.get("skill_family", "unknown")),
        str(skill_case.get("skill_target_kind", "unknown")),
        "null" if conflict_type is None else str(conflict_type),
    )


def percent(part: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return part * 100.0 / total


def format_ratio(current_count: int, total_count: int, target: Optional[float]) -> str:
    current_ratio = percent(current_count, total_count)
    if target is None:
        return f"{current_ratio:.1f}%(-) / {current_count}"
    return f"{current_ratio:.1f}%({target:g}%) / {current_count}"


def get_topic_target(taxonomy: dict[str, Any], topic: str) -> Optional[float]:
    value = taxonomy.get("global_targets", {}).get("topic", {}).get(topic)
    return float(value) if isinstance(value, (int, float)) else None


def get_matrix_target(
    taxonomy: dict[str, Any],
    topic: str,
    matrix_key: str,
    value: str,
) -> Optional[float]:
    topic_matrix = taxonomy.get("general_valid_matrix", {}).get(topic, {})
    if not isinstance(topic_matrix, dict):
        return None
    target_map = topic_matrix.get(matrix_key, {})
    if not isinstance(target_map, dict):
        return None
    target = target_map.get(value)
    return float(target) if isinstance(target, (int, float)) else None


def get_skill_family_target(taxonomy: dict[str, Any], value: str) -> Optional[float]:
    target = taxonomy.get("skill_targets", {}).get("skill_family", {}).get(value)
    return float(target) if isinstance(target, (int, float)) else None


def get_skill_matrix_target(
    taxonomy: dict[str, Any],
    skill_family: str,
    matrix_key: str,
    value: str,
) -> Optional[float]:
    family_matrix = taxonomy.get("skill_valid_matrix", {}).get(skill_family, {})
    if not isinstance(family_matrix, dict):
        return None
    target_map = family_matrix.get(matrix_key, {})
    if not isinstance(target_map, dict):
        return None
    target = target_map.get(value)
    return float(target) if isinstance(target, (int, float)) else None


def group_rows(samples: list[dict[str, Any]], skill_only: bool = False) -> dict[tuple[Any, ...], list[dict[str, Any]]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        if skill_only:
            skill_path = get_skill_path(sample)
            if skill_path is None:
                continue
            key = (*skill_path, get_base_command_text(sample), get_edge_flags(sample))
        else:
            key = (*get_general_path(sample), get_base_command_text(sample), get_edge_flags(sample))
        groups[key].append(sample)
    return groups


def render_row(
    command_text: str,
    edge_flags: tuple[str, ...],
    grouped_samples: list[dict[str, Any]],
) -> str:
    refs = [get_source_ref(sample, index) for index, sample in enumerate(grouped_samples, start=1)]
    edge_text = ", ".join(edge_flags) if edge_flags else "[]"
    ref_text = ", ".join(refs) if refs else "{}"
    return f'          "{command_text}" @ {len(grouped_samples)} @ {edge_text} @ {ref_text}'


def count_by(samples: Iterable[dict[str, Any]], extractor) -> Counter[str]:
    counter: Counter[str] = Counter()
    for sample in samples:
        value = extractor(sample)
        if isinstance(value, str):
            counter[value] += 1
    return counter


def render_general_coverage(samples: list[dict[str, Any]], taxonomy: dict[str, Any]) -> str:
    lines: list[str] = ["# General Coverage", ""]
    total = len(samples)
    groups = group_rows(samples, skill_only=False)

    topic_counts = count_by(samples, lambda sample: get_general_path(sample)[0])

    for topic in taxonomy.get("orders", {}).get("topic", []):
        topic_samples = [sample for sample in samples if get_general_path(sample)[0] == topic]
        topic_count = topic_counts.get(topic, 0)
        lines.append(f"{topic} [{format_ratio(topic_count, total, get_topic_target(taxonomy, topic))}]")

        actor_counts = count_by(topic_samples, lambda sample: get_general_path(sample)[1])
        for actor in taxonomy.get("general_valid_matrix", {}).get(topic, {}).get("allowed_actor_selection", {}).keys():
            actor_samples = [sample for sample in topic_samples if get_general_path(sample)[1] == actor]
            actor_count = actor_counts.get(actor, 0)
            lines.append(f"  {actor} [{format_ratio(actor_count, topic_count, get_matrix_target(taxonomy, topic, 'allowed_actor_selection', actor))}]")

            target_counts = count_by(actor_samples, lambda sample: get_general_path(sample)[2])
            for target in taxonomy.get("general_valid_matrix", {}).get(topic, {}).get("allowed_target_selection", {}).keys():
                target_samples = [sample for sample in actor_samples if get_general_path(sample)[2] == target]
                target_count = target_counts.get(target, 0)
                if target_count == 0:
                    lines.append(f"    {target} [{format_ratio(0, actor_count, get_matrix_target(taxonomy, topic, 'allowed_target_selection', target))}]")
                    continue
                lines.append(f"    {target} [{format_ratio(target_count, actor_count, get_matrix_target(taxonomy, topic, 'allowed_target_selection', target))}]")

                action_counts = count_by(target_samples, lambda sample: get_general_path(sample)[3])
                for action in taxonomy.get("general_valid_matrix", {}).get(topic, {}).get("allowed_action_pattern", {}).keys():
                    action_samples = [sample for sample in target_samples if get_general_path(sample)[3] == action]
                    action_count = action_counts.get(action, 0)
                    if action_count == 0:
                        continue
                    lines.append(f"      {action} [{format_ratio(action_count, target_count, get_matrix_target(taxonomy, topic, 'allowed_action_pattern', action))}]")

                    scenario_counts = count_by(action_samples, lambda sample: get_general_path(sample)[4])
                    for scenario in taxonomy.get("general_valid_matrix", {}).get(topic, {}).get("allowed_scenario_family", {}).keys():
                        scenario_samples = [sample for sample in action_samples if get_general_path(sample)[4] == scenario]
                        scenario_count = scenario_counts.get(scenario, 0)
                        if scenario_count == 0:
                            continue
                        lines.append(f"        {scenario} [{format_ratio(scenario_count, action_count, get_matrix_target(taxonomy, topic, 'allowed_scenario_family', scenario))}]")

                        matching_rows = []
                        for key, grouped_samples in groups.items():
                            key_topic, key_actor, key_target, key_action, key_scenario, command_text, edge_flags = key
                            if (
                                key_topic == topic
                                and key_actor == actor
                                and key_target == target
                                and key_action == action
                                and key_scenario == scenario
                            ):
                                matching_rows.append((command_text, edge_flags, grouped_samples))

                        for command_text, edge_flags, grouped_samples in sorted(matching_rows, key=lambda item: item[0]):
                            lines.append(render_row(command_text, edge_flags, grouped_samples))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_skill_coverage(samples: list[dict[str, Any]], taxonomy: dict[str, Any]) -> str:
    skill_samples = [sample for sample in samples if get_skill_path(sample) is not None]
    total = len(skill_samples)
    groups = group_rows(skill_samples, skill_only=True)
    lines: list[str] = ["# Skill Coverage", ""]

    family_counts = count_by(skill_samples, lambda sample: get_skill_path(sample)[0] if get_skill_path(sample) else "")

    for family in taxonomy.get("orders", {}).get("skill_family", []):
        family_samples = [sample for sample in skill_samples if get_skill_path(sample) and get_skill_path(sample)[0] == family]
        family_count = family_counts.get(family, 0)
        lines.append(f"{family} [{format_ratio(family_count, total, get_skill_family_target(taxonomy, family))}]")

        target_counts = count_by(family_samples, lambda sample: get_skill_path(sample)[1] if get_skill_path(sample) else "")
        target_map = taxonomy.get("skill_valid_matrix", {}).get(family, {}).get("allowed_skill_target_kind", {})
        for target_kind in target_map.keys():
            target_samples = [sample for sample in family_samples if get_skill_path(sample) and get_skill_path(sample)[1] == target_kind]
            target_count = target_counts.get(target_kind, 0)
            lines.append(f"  {target_kind} [{format_ratio(target_count, family_count, get_skill_matrix_target(taxonomy, family, 'allowed_skill_target_kind', target_kind))}]")

            conflict_counts = count_by(target_samples, lambda sample: get_skill_path(sample)[2] if get_skill_path(sample) else "")
            conflict_map = taxonomy.get("skill_valid_matrix", {}).get(family, {}).get("allowed_conflict_type", {})
            for conflict in conflict_map.keys():
                conflict_samples = [sample for sample in target_samples if get_skill_path(sample) and get_skill_path(sample)[2] == conflict]
                conflict_count = conflict_counts.get(conflict, 0)
                if conflict_count == 0:
                    continue
                lines.append(f"    {conflict} [{format_ratio(conflict_count, target_count, get_skill_matrix_target(taxonomy, family, 'allowed_conflict_type', conflict))}]")

                matching_rows = []
                for key, grouped_samples in groups.items():
                    key_family, key_target_kind, key_conflict, command_text, edge_flags = key
                    if key_family == family and key_target_kind == target_kind and key_conflict == conflict:
                        matching_rows.append((command_text, edge_flags, grouped_samples))

                for command_text, edge_flags, grouped_samples in sorted(matching_rows, key=lambda item: item[0]):
                    lines.append(render_row(command_text, edge_flags, grouped_samples))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_summary(samples: list[dict[str, Any]], taxonomy: dict[str, Any]) -> str:
    lines = ["# Coverage Summary", ""]
    total = len(samples)
    skill_samples = [sample for sample in samples if get_skill_path(sample) is not None]

    def table(title: str, counter: Counter[str], target_map: dict[str, Any], total_count: int) -> None:
        lines.extend([f"## {title}", "", "| key | current_ratio | target_ratio | count |", "|---|---:|---:|---:|"])
        for key, target in target_map.items():
            count = counter.get(key, 0)
            lines.append(f"| {key} | {percent(count, total_count):.1f}% | {target:g}% | {count} |")
        lines.append("")

    global_targets = taxonomy.get("global_targets", {})
    table("Topic", count_by(samples, lambda sample: get_general_path(sample)[0]), global_targets.get("topic", {}), total)
    table("Actor Selection", count_by(samples, lambda sample: get_general_path(sample)[1]), global_targets.get("actor_selection", {}), total)
    table("Target Selection", count_by(samples, lambda sample: get_general_path(sample)[2]), global_targets.get("target_selection", {}), total)
    table("Action Pattern", count_by(samples, lambda sample: get_general_path(sample)[3]), global_targets.get("action_pattern", {}), total)
    table("Command Style", count_by(samples, lambda sample: get_metadata(sample).get("command_style", "unknown")), global_targets.get("command_style", {}), total)

    skill_total = len(skill_samples)
    skill_targets = taxonomy.get("skill_targets", {})
    table("Skill Family", count_by(skill_samples, lambda sample: get_skill_path(sample)[0] if get_skill_path(sample) else ""), skill_targets.get("skill_family", {}), skill_total)
    table("Skill Target Kind", count_by(skill_samples, lambda sample: get_skill_path(sample)[1] if get_skill_path(sample) else ""), skill_targets.get("skill_target_kind", {}), skill_total)
    table("Conflict Type", count_by(skill_samples, lambda sample: get_skill_path(sample)[2] if get_skill_path(sample) else ""), skill_targets.get("conflict_type", {}), skill_total)

    taxonomy_errors = collect_taxonomy_errors(samples, taxonomy)
    lines.extend(["## Taxonomy Errors", ""])
    if not taxonomy_errors:
        lines.append("No taxonomy errors found.")
    else:
        for source_ref, errors in taxonomy_errors:
            lines.append(f"- {source_ref}: {'; '.join(errors)}")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def collect_taxonomy_errors(samples: list[dict[str, Any]], taxonomy: dict[str, Any]) -> list[tuple[str, list[str]]]:
    errors: list[tuple[str, list[str]]] = []
    for index, sample in enumerate(samples, start=1):
        sample_errors = validate_metadata_against_taxonomy(sample, taxonomy)
        if sample_errors:
            errors.append((get_source_ref(sample, index), sample_errors))
    return errors


def render_taxonomy_sot(taxonomy: dict[str, Any]) -> str:
    lines = ["# Taxonomy SOT", "", str(taxonomy.get("description", "")), ""]

    lines.extend(["## Global Targets", ""])
    for group_name, target_map in taxonomy.get("global_targets", {}).items():
        lines.append(f"### {group_name}")
        lines.append("")
        lines.append("| key | target | description |")
        lines.append("|---|---:|---|")
        for key, target in target_map.items():
            description = taxonomy.get("descriptions", {}).get(group_name, {}).get(key, "")
            lines.append(f"| {key} | {target:g}% | {description} |")
        lines.append("")

    lines.extend(["## General Valid Matrix", ""])
    for topic, matrix in taxonomy.get("general_valid_matrix", {}).items():
        lines.append(f"### {topic}")
        lines.append("")
        for key in ["allowed_actor_selection", "allowed_target_selection", "allowed_action_pattern", "allowed_scenario_family"]:
            lines.append(f"- {key}")
            for item, target in matrix.get(key, {}).items():
                lines.append(f"  - {item}: {target:g}%")
        lines.append("")

    lines.extend(["## Skill Valid Matrix", ""])
    for family, matrix in taxonomy.get("skill_valid_matrix", {}).items():
        lines.append(f"### {family}")
        lines.append("")
        for key in ["allowed_skill_target_kind", "allowed_conflict_type"]:
            lines.append(f"- {key}")
            for item, target in matrix.get(key, {}).items():
                lines.append(f"  - {item}: {target:g}%")
        required_edge_flags = matrix.get("required_edge_flags")
        if required_edge_flags:
            lines.append("- required_edge_flags")
            for flag in required_edge_flags:
                lines.append(f"  - {flag}")
        lines.append("")

    lines.extend(["## Edge Flags", "", "| edge_flag | description |", "|---|---|"])
    edge_descriptions = taxonomy.get("descriptions", {}).get("edge_flags", {})
    for flag in taxonomy.get("edge_flags", []):
        lines.append(f"| {flag} | {edge_descriptions.get(flag, '')} |")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", default=str(DEFAULT_DATASET_ROOT))
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY_PATH))
    args = parser.parse_args()

    dataset_root = Path(args.dataset_root)
    accepted_dir = dataset_root / "accepted"
    reports_dir = dataset_root / "reports"
    taxonomy = load_taxonomy(Path(args.taxonomy))
    samples = load_accepted_samples(accepted_dir)

    write_text(reports_dir / "general_coverage.md", render_general_coverage(samples, taxonomy))
    write_text(reports_dir / "skill_coverage.md", render_skill_coverage(samples, taxonomy))
    write_text(reports_dir / "coverage_summary.md", render_summary(samples, taxonomy))
    write_text(reports_dir / "taxonomy_sot.md", render_taxonomy_sot(taxonomy))

    print(f"accepted_samples: {len(samples)}")
    print(f"reports_dir: {reports_dir}")


if __name__ == "__main__":
    main()
