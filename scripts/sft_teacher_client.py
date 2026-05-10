# Together AI로 teacher LLM을 호출하고 raw generation JSONL을 저장한다.
# 입력 payload는 sft_generation_request.py가 만든 selected_bucket 구조를 사용한다.
# 모델 출력은 JSON object 하나여야 하며, 검증은 sft_validator.py에서 수행한다.
# 이 파일은 accepted/rejected 판정을 하지 않는다.

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
출력은 반드시 JSON object 하나만 한다.
마크다운, 코드블록, 주석, 설명문, JSON 밖 텍스트를 출력하지 않는다.
사용자가 제공한 selected_bucket, existing_valid_paraphrase_samples, count_to_generate를 따른다.
selected_bucket의 edge_flags와 skill_case 의미를 유지한다.
existing_valid_paraphrase_samples는 같은 의미의 표현 예시다.
새 command_text는 같은 의미를 유지하되 말만 다르게 만든다.
각 sample은 validation을 통과할 수 있는 master sample 구조여야 한다.

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
    client = Together(api_key=os.environ["TOGETHER_API_KEY"])

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

    return extract_stream_text(stream)


def append_raw_generation(
    output_path: Path,
    request_payload: dict[str, Any],
    raw_response: str,
    model_name: str,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "model": model_name,
        "request_payload": request_payload,
        "raw_response": raw_response,
    }

    with output_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        required=True,
        help="Path to request payload JSON produced by sft_generation_request.py.",
    )
    parser.add_argument(
        "--output",
        default="sft_dataset/raw_generations/batch_raw.jsonl",
        help="Path to append raw teacher generations.",
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help="Together model name.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=320,
        help="Maximum output tokens.",
    )
    args = parser.parse_args()

    payload = load_json(Path(args.input))
    raw_response = call_together(
        user_payload=payload,
        model_name=args.model,
        max_tokens=args.max_tokens,
    )

    append_raw_generation(
        output_path=Path(args.output),
        request_payload=payload,
        raw_response=raw_response,
        model_name=args.model,
    )

    print(raw_response)


if __name__ == "__main__":
    main()