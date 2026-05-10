# SFT dataset 관리 작업의 단일 진입점이다.
# report 생성, generation request payload 생성, validator 실행을 subcommand로 묶는다.
# 실제 기준은 taxonomy_sot.json과 accepted/rejected/raw_generations 폴더다.
# 각 세부 로직은 전용 스크립트에 위임한다.

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    from sft_generation_request import build_generation_payload, write_json, make_default_output_path
    from sft_validator import validate_file
except ImportError:
    sys.path.append(str(Path(__file__).resolve().parent))
    from sft_generation_request import build_generation_payload, write_json, make_default_output_path
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


def run_request(args: argparse.Namespace) -> None:
    dataset_root = Path(args.dataset_root)
    payload = build_generation_payload(
        raw_request=args.request,
        dataset_root=dataset_root,
        taxonomy_path=Path(args.taxonomy),
    )

    output_path = Path(args.output) if args.output else make_default_output_path(
        dataset_root / "raw_generations",
        args.request,
    )
    write_json(output_path, payload)
    print(f"generation_request: {output_path}")

    if args.print_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


def run_validate(args: argparse.Namespace) -> None:
    result = validate_file(
        input_path=Path(args.input),
        dataset_root=Path(args.dataset_root),
        taxonomy_path=Path(args.taxonomy),
        write_outputs=not args.dry_run,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.refresh_report and not args.dry_run:
        run_report(Path(args.dataset_root), Path(args.taxonomy))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Synthetic SFT dataset management CLI")
    parser.add_argument("--dataset-root", default=str(DEFAULT_DATASET_ROOT))
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY_PATH))

    subparsers = parser.add_subparsers(dest="command", required=True)

    report_parser = subparsers.add_parser("report", help="Regenerate coverage reports.")
    report_parser.set_defaults(func=lambda args: run_report(Path(args.dataset_root), Path(args.taxonomy)))

    request_parser = subparsers.add_parser("request", help="Build teacher LLM generation request payload.")
    request_parser.add_argument("request", help="Generation request path, e.g. c1-2-1-3-1-10.4")
    request_parser.add_argument("--output", default="")
    request_parser.add_argument("--print-json", action="store_true")
    request_parser.set_defaults(func=run_request)

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
