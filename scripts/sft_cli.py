# SFT dataset 관리 작업의 단일 진입점이다.
# report 생성, generation request payload 생성, teacher 호출, validator 실행을 묶는다.
# request/generate 출력 파일명은 raw_generations의 다음 순번을 사용한다.
# generate는 payload 생성 후 사용자 확인을 받고 teacher를 호출한다.
# 세부 검증 기준은 taxonomy_sot.json과 validator에 위임한다.

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    from sft_file_sequence import next_numbered_index, numbered_path
    from sft_generation_request import build_generation_payload, make_default_output_path, write_json
    from sft_teacher_client import MODEL_NAME, run_teacher_generation
    from sft_validator import validate_file
except ImportError:
    sys.path.append(str(Path(__file__).resolve().parent))
    from sft_file_sequence import next_numbered_index, numbered_path
    from sft_generation_request import build_generation_payload, make_default_output_path, write_json
    from sft_teacher_client import MODEL_NAME, run_teacher_generation
    from sft_validator import validate_file


DEFAULT_DATASET_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAXONOMY_PATH = DEFAULT_DATASET_ROOT / "config" / "taxonomy_sot.json"


def run_report(dataset_root: Path, taxonomy_path: Path) -> None:
    script_path = Path(__file__).resolve().parent / "sft_coverage_report.py"
    subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--dataset-root",
            str(dataset_root),
            "--taxonomy",
            str(taxonomy_path),
        ],
        check=True,
    )


def build_payload_or_print_error(args: argparse.Namespace) -> dict[str, Any] | None:
    try:
        return build_generation_payload(
            raw_request=args.request,
            dataset_root=Path(args.dataset_root),
            taxonomy_path=Path(args.taxonomy),
        )
    except Exception as error:
        print(f"request failed: {error}")
        return None


def run_request(args: argparse.Namespace) -> None:
    dataset_root = Path(args.dataset_root)

    payload = build_payload_or_print_error(args)
    if payload is None:
        return

    output_path = (
        Path(args.output)
        if args.output
        else make_default_output_path(dataset_root / "raw_generations", args.request)
    )

    write_json(output_path, payload)
    print(f"generation_request: {output_path}")

    if args.print_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


def print_generation_plan(
    payload: dict[str, Any],
    request_path: Path,
    raw_output_path: Path,
    trace_output_path: Path,
) -> None:
    request_info = payload.get("request", {})
    selected_bucket = payload.get("selected_bucket", {})

    stable_path = request_info.get("stable_path")
    skill_stable_path = request_info.get("skill_stable_path")
    count_to_generate = payload.get("count_to_generate")
    base_command_text = request_info.get("base_command_text")

    print("request ok")
    print(f"stable_path: {stable_path}")
    if skill_stable_path:
        print(f"skill_stable_path: {skill_stable_path}")
    print(f"base_command_text: {base_command_text}")
    print(f"count_to_generate: {count_to_generate}")

    edge_flags = selected_bucket.get("edge_flags")
    if edge_flags:
        print(f"edge_flags: {edge_flags}")

    skill_case = selected_bucket.get("skill_case")
    if skill_case:
        print(f"skill_case: {skill_case}")

    print(f"request_file: {request_path}")
    print(f"raw_generation_file: {raw_output_path}")
    print(f"trace_file: {trace_output_path}")


def run_generate(args: argparse.Namespace) -> None:
    dataset_root = Path(args.dataset_root)
    raw_dir = dataset_root / "raw_generations"

    payload = build_payload_or_print_error(args)
    if payload is None:
        return

    request_path = (
        Path(args.output)
        if args.output
        else make_default_output_path(raw_dir, args.request)
    )

    batch_index = next_numbered_index(raw_dir, "batch", "_raw.jsonl")
    raw_output_path = numbered_path(raw_dir, "batch", batch_index, "_raw.jsonl")
    trace_output_path = numbered_path(raw_dir, "batch", batch_index, "_trace.jsonl")

    print_generation_plan(
        payload=payload,
        request_path=request_path,
        raw_output_path=raw_output_path,
        trace_output_path=trace_output_path,
    )

    if args.print_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))

    answer = input("type y to continue, n to cancel: ").strip().lower()
    if answer != "y":
        print("cancelled")
        return

    write_json(request_path, payload)

    result = run_teacher_generation(
        input_path=request_path,
        output_path=raw_output_path,
        trace_path=trace_output_path,
        model_name=args.model,
        max_tokens=args.max_tokens,
        print_json=args.print_json,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


def run_validate(args: argparse.Namespace) -> None:
    result = validate_file(
        input_path=Path(args.input),
        dataset_root=Path(args.dataset_root),
        taxonomy_path=Path(args.taxonomy),
        write_outputs=not args.dry_run,
    )

    if result.get("skipped"):
        print("validate skipped: input already validated")
        return

    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.refresh_report and not args.dry_run:
        run_report(Path(args.dataset_root), Path(args.taxonomy))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Synthetic SFT dataset management CLI")
    parser.add_argument("--dataset-root", default=str(DEFAULT_DATASET_ROOT))
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY_PATH))

    subparsers = parser.add_subparsers(dest="command", required=True)

    report_parser = subparsers.add_parser("report", help="Regenerate coverage reports.")
    report_parser.set_defaults(
        func=lambda args: run_report(Path(args.dataset_root), Path(args.taxonomy))
    )

    request_parser = subparsers.add_parser("request", help="Build teacher LLM generation request payload.")
    request_parser.add_argument("request", help="Generation request path, e.g. c1-2-1-3-1-10.4")
    request_parser.add_argument("--output", default="")
    request_parser.add_argument("--print-json", action="store_true")
    request_parser.set_defaults(func=run_request)

    generate_parser = subparsers.add_parser("generate", help="Build request payload and call teacher after confirmation.")
    generate_parser.add_argument("request", help="Generation request path, e.g. c1-2-1-3-1-10.4")
    generate_parser.add_argument("--output", default="", help="Optional request payload path.")
    generate_parser.add_argument("--model", default=MODEL_NAME)
    generate_parser.add_argument("--max-tokens", type=int, default=12000)
    generate_parser.add_argument("--print-json", action="store_true")
    generate_parser.set_defaults(func=run_generate)

    validate_parser = subparsers.add_parser("validate", help="Validate teacher output and split accepted/rejected.")
    validate_parser.add_argument("--input", required=True, help="Teacher output JSON/JSONL path.")
    validate_parser.add_argument("--dry-run", action="store_true")
    validate_parser.add_argument("--refresh-report", action="store_true")
    validate_parser.set_defaults(func=run_validate)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()