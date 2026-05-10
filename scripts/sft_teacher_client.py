# Together AI teacher를 호출하고 validator 입력용 JSONL을 저장한다.
# 입력은 sft_cli.py request/generate가 만든 generation request JSON이다.
# 출력 JSONL에는 master sample dict만 저장한다.
# 원본 응답은 trace JSONL에 별도로 저장한다.
# accepted/rejected 판정은 sft_validator.py가 수행한다.

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from together import Together

MODEL_NAME = "google/gemma-4-31B-it"

SYSTEM_PROMPT = """
너는 Unity 전투 명령 파서용 Synthetic SFT dataset sample을 생성하는 데이터 생성기다.

출력은 반드시 JSON object 하나 또는 JSON array 하나만 한다.
마크다운, 코드블록, 주석, 설명문, JSON 밖 텍스트를 출력하지 않는다.

사용자가 제공한 selected_bucket, existing_valid_paraphrase_samples, count_to_generate를 따른다.
selected_bucket의 intent_family, actor_selection, target_selection, action_pattern, scenario_family를 유지한다.
selected_bucket의 edge_flags와 skill_case 의미를 유지한다.
existing_valid_paraphrase_samples는 같은 의미의 표현 예시다.
새 command_text는 같은 의미를 유지하되 말만 다르게 만든다.

반드시 validation을 통과할 수 있는 master sample 구조로 생성한다.
각 sample에는 다음 top-level field를 포함한다:
id, split, command_spec, metadata, skill_case, gold, input, output

metadata에는 반드시 다음 필드를 포함한다:
intent_family, command_style, actor_selection, target_selection, action_pattern, scenario_family, edge_flags

skill_case가 null이 아닌 모든 sample은 반드시 다음 5개 필드를 가진다:
skill_family, skill_target_kind, is_skill_aoe, can_skill_target_dead, conflict_type

is_skill_aoe와 can_skill_target_dead는 반드시 boolean이다.
conflict_type은 null 또는 taxonomy에 존재하는 string이다.

source_ref는 만들지 않는다.
validator_result는 만들지 않는다.
taxonomy 밖 값을 만들지 않는다.
output은 sanitizer가 고친 결과가 아니라, 처음부터 raw valid label이어야 한다.

가능하면 다음 구조로 출력한다:
{
  "samples": [
    {
      "id": "...",
      "split": "train",
      "command_spec": {},
      "metadata": {},
      "skill_case": null,
      "gold": {},
      "input": {},
      "output": {}
    }
  ]
}

한국어 명령에서 콤마와 unitId 나열만 보고 actor/target을 기계적으로 판단하지 않는다.
문맥, 조사, 동사, 분류 기준을 함께 보고 actor와 target을 등록한다.

예시 1:
"A_02, A_04에게 이동해"
- explicit_ally_target / move_to_alive_ally 명령이다.
- A_02가 actor다.
- A_04가 target 또는 move.to다.
- 두 unitId가 모두 actor인 명령이 아니다.

예시 2:
"A_04, A_02한테 스킬 써"
- ally_skill_valid_target 명령이다.
- A_04가 actor다.
- A_02가 skill target이다.
- 두 unitId가 모두 actor인 명령이 아니다.

예시 3:
"A_01, A_02는 뒤로 빠져"
- explicit_multi_actor / safe_ally / move_only / multi_actor_retreat 명령이다.
- A_01과 A_02가 모두 actor다.
- 뒤로 빠지는 목적지는 전장 상태에서 안전한 ally 또는 backline ally를 기준으로 정한다.

따라서 콤마로 unitId가 나뉜 비슷한 문장 형식이라도,
분류 기준과 문맥에 따라 actor-target, actor-actor, target-target 관계를 논리적으로 구분해야 한다.
""".strip()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Input payload root must be a JSON object.")

    return data


def extract_stream_text(stream: Any) -> str:
    chunks: list[str] = []

    for event in stream:
        choices = getattr(event, "choices", None)
        if not choices:
            continue

        delta = getattr(choices[0], "delta", None)
        if delta is None:
            continue

        content = getattr(delta, "content", None)
        if content:
            chunks.append(content)

    return "".join(chunks)


def call_together(user_payload: dict[str, Any], model_name: str, max_tokens: int) -> str:
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        raise RuntimeError("TOGETHER_API_KEY environment variable is not set.")

    client = Together(api_key=api_key)

    stream = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": json.dumps(user_payload, ensure_ascii=False),
            },
        ],
        temperature=0.0,
        top_p=0.8,
        max_tokens=max_tokens,
        stream=True,
    )

    text = extract_stream_text(stream).strip()
    if not text:
        raise RuntimeError("Teacher response is empty.")

    return text


def strip_code_fence(text: str) -> str:
    stripped = text.strip()

    if not stripped.startswith("```"):
        return stripped

    lines = stripped.splitlines()
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip()

    return stripped


def parse_teacher_json(raw_text: str) -> Any:
    text = strip_code_fence(raw_text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    first_object = text.find("{")
    first_array = text.find("[")
    candidates = [index for index in [first_object, first_array] if index >= 0]

    if not candidates:
        raise ValueError("Teacher response does not contain JSON.")

    start = min(candidates)
    end = max(text.rfind("}"), text.rfind("]"))

    if end < start:
        raise ValueError("Teacher response JSON boundary is invalid.")

    return json.loads(text[start : end + 1])


def normalize_samples(parsed: Any) -> list[dict[str, Any]]:
    if isinstance(parsed, list):
        samples = parsed
    elif isinstance(parsed, dict) and isinstance(parsed.get("samples"), list):
        samples = parsed["samples"]
    elif isinstance(parsed, dict):
        samples = [parsed]
    else:
        raise ValueError("Teacher JSON root must be object, array, or object with samples.")

    normalized: list[dict[str, Any]] = []
    for index, sample in enumerate(samples, start=1):
        if not isinstance(sample, dict):
            raise ValueError(f"Sample #{index} is not an object.")
        normalized.append(sample)

    return normalized


def append_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    if not records:
        return

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def run_teacher_generation(
    input_path: Path,
    output_path: Path,
    trace_path: Path,
    model_name: str = MODEL_NAME,
    max_tokens: int = 12000,
    print_json: bool = False,
) -> dict[str, Any]:
    payload = load_json(input_path)

    raw_response = call_together(
        user_payload=payload,
        model_name=model_name,
        max_tokens=max_tokens,
    )

    parsed = parse_teacher_json(raw_response)
    samples = normalize_samples(parsed)

    append_jsonl(output_path, samples)

    trace_record = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "model": model_name,
        "input_path": str(input_path),
        "output_path": str(output_path),
        "sample_count": len(samples),
        "raw_response": raw_response,
    }
    append_jsonl(trace_path, [trace_record])

    if print_json:
        print(json.dumps(samples, ensure_ascii=False, indent=2))

    return {
        "input_path": str(input_path),
        "output_path": str(output_path),
        "trace_path": str(trace_path),
        "sample_count": len(samples),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        required=True,
        help="Path to request payload JSON produced by sft_cli.py request.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to append validator-ready raw generation JSONL.",
    )
    parser.add_argument(
        "--trace-output",
        required=True,
        help="Path to append raw teacher response trace JSONL.",
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help="Together model name.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=12000,
        help="Maximum output tokens.",
    )
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Print parsed samples.",
    )

    args = parser.parse_args()

    result = run_teacher_generation(
        input_path=Path(args.input),
        output_path=Path(args.output),
        trace_path=Path(args.trace_output),
        model_name=args.model,
        max_tokens=args.max_tokens,
        print_json=args.print_json,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()