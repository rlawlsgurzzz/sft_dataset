# Synthetic SFT Dataset 현재 상태 요약

## 1. 이 데이터셋이 필요한 이유

현재 프로젝트의 목표는 전장 상태와 한국어 자연어 명령을 받아, 학생 모델이 다음 JSON을 안정적으로 출력하도록 학습시키는 것이다.

```text
전장 상태 + 한국어 명령
→ thinking / dialog / action JSON
```

기존 프롬프트 기반 방식만으로는 아래 문제가 반복될 수 있다.

```text
- actor / target 해석 오류
- skill target side 판단 오류
- self skill, ally skill, enemy skill 충돌 처리 불안정
- wait / skillControl 남발
- dialog와 action actor 불일치
- schema extra field 또는 JSON 파싱 실패
- 현재 상태에서 불가능한 명령을 억지로 실행
```

따라서 목표는 단순한 명령 paraphrase 데이터셋이 아니라, **전장 상태와 명령 의미가 결합된 coverage-driven SFT dataset**을 만드는 것이다.

우선순위는 다음이다.

```text
raw output semantic correctness
> schema correctness
> runtime validity
> policy validity
> dialog 품질
> 표현 다양성
```

---

## 2. 현재 런타임 입력/출력 전제

현재 학생 모델이 배워야 하는 출력은 다음 세 top-level key로 고정된다.

```json
{
  "thinking": "짧은 판단 요약",
  "dialog": [],
  "action": []
}
```

허용 action type은 다음이다.

```text
move
attack
skill
wait
skillControl
```

주요 runtime input은 다음 구조를 따른다.

```json
{
  "input": {
    "area_situation": {
      "allies": [],
      "enemies": []
    },
    "command": "한국어 명령"
  },
  "commandAnalysis": {
    "analysisMode": "runtime_constraint_summary",
    "allowedActors": [],
    "allowedAttackTargets": [],
    "validMoveToUnits": [],
    "invalidUnits": [],
    "actionPolicy": {}
  }
}
```

중요한 전제:

```text
commandAnalysis는 명령 의도 파서가 아니다.
commandAnalysis는 런타임상 가능한 actor / attack target / move.to 범위를 요약한다.
actor, target, action 의미 해석은 LLM이 한다.
```

---

## 3. 현재 작성된 6개 파일

### 3.1 `sft_dataset/config/taxonomy_sot.json`

역할:

```text
분류 기준, 목표 비율, valid matrix, skill valid matrix, edge_flags enum, 각 항목 설명을 담는 machine-readable SOT.
```

담고 있는 내용:

```text
- command_style 5종
- topic 비율
- actor_selection 비율
- target_selection 비율
- action_pattern 비율
- general valid matrix
- skill_family 비율
- skill_target_kind 비율
- conflict_type 비율
- skill valid matrix
- edge_flags enum
- 각 분류 기준 설명
```

이 파일이 실제 기준이다. Markdown report는 이 파일에서 파생되는 보기용 문서다.

---

### 3.2 `sft_dataset/scripts/sft_taxonomy.py`

역할:

```text
taxonomy_sot.json을 로드하고, 숫자 path를 stable path로 변환하며, 요청이 valid matrix에 맞는지 LLM 호출 전에 검사한다.
```

주요 기능:

```text
- taxonomy_sot.json shape 검사
- c1-2-1-3-1-10.4 형태의 요청 파싱
- general path 검증
- skill override path 검증
- edge_flags / command_style / skill_case taxonomy 검증
- selected_bucket에 필요한 설명 추출
```

숫자 path는 사람 입력용이고, 내부에서는 stable path로 변환한다.

---

### 3.3 `sft_dataset/scripts/sft_coverage_report.py`

역할:

```text
accepted/*.jsonl을 읽어 현재 coverage를 집계하고 general_coverage.md, skill_coverage.md, coverage_summary.md, taxonomy_sot.md를 재생성한다.
```

생성되는 report:

```text
reports/taxonomy_sot.md
reports/general_coverage.md
reports/skill_coverage.md
reports/coverage_summary.md
```

중요한 점:

```text
accepted 폴더가 source of truth다.
report markdown은 수동으로 고치는 문서가 아니라, 매번 재생성되는 derived report다.
```

---

### 3.4 `sft_dataset/scripts/sft_generation_request.py`

역할:

```text
사용자의 생성 요청을 파싱하고, 기존 accepted paraphrase sample을 찾아 teacher LLM에 보낼 selected_bucket payload를 만든다.
```

주요 기능:

```text
- 숫자 path 요청 파싱
- taxonomy valid matrix 검사
- selected command slot 찾기
- accepted sample에서 기존 validation 통과 paraphrase command_text 추출
- command_style 함께 추출
- selected_bucket 구성
- selected_bucket에 선택된 기준 설명 포함
- source_ref는 LLM 입력에서 제외
```

LLM에게 보내는 핵심 구조:

```json
{
  "selected_bucket": {},
  "existing_valid_paraphrase_samples": [
    {
      "command_text": "A_03, E_02한테 스킬 써",
      "command_style": "direct_korean"
    }
  ],
  "count_to_generate": 4
}
```

중요한 원칙:

```text
selected_bucket이 의미/상황/edge_flags를 가진다.
existing_valid_paraphrase_samples는 표현 예시와 command_style만 가진다.
```

---

### 3.5 `sft_dataset/scripts/sft_validator.py`

역할:

```text
teacher가 만든 sample을 parse/schema/runtime/policy/semantic/taxonomy 기준으로 검증하고 accepted 또는 rejected로 분류한다.
```

현재 검증 범위:

```text
- master sample 필드 존재 여부
- metadata taxonomy 검증
- skill_case taxonomy 검증
- output top-level key 검증
- action schema 검증
- actor runtime validity 검증
- attack target runtime validity 검증
- move.to runtime validity 검증
- skill description exact match 검증
- skill target side/runtime validity 검증
- wait after attack/skill 금지
- dialog/action actor 일치 검증
- gold 기준 semantic 검증
```

accepted에 들어가는 sample은 `validator_result.passed = true`로 기록된다.

---

### 3.6 `sft_dataset/scripts/sft_cli.py`

역할:

```text
report 생성, generation request payload 생성, validator 실행을 명령어 하나로 묶는 진입점.
```

현재 subcommand:

```text
report
request
validate
```

---

## 4. 주요 명령어

### 4.1 report 재생성

```powershell
python scripts/sft_cli.py report
```

실행 결과:

```text
reports/taxonomy_sot.md
reports/general_coverage.md
reports/skill_coverage.md
reports/coverage_summary.md
```

---

### 4.2 teacher LLM에 보낼 생성 요청 payload 생성

```powershell
python scripts/sft_cli.py request c1-2-1-3-1-10.4 --print-json
```

의미:

```text
일반 coverage table의 특정 command slot에 대해 새 paraphrase/sample 후보 4개 생성을 요청하는 payload를 만든다.
```

skill override 포함 예:

```powershell
python scripts/sft_cli.py request c3-1-1-4-4-1/2-3-2.4 --print-json
```

주의:

```text
request는 selected command slot에 연결된 accepted sample이 있어야 작동한다.
초기 accepted sample이 없으면 기존 valid paraphrase를 읽을 수 없으므로 실패하는 것이 정상이다.
```

---

### 4.3 teacher 결과 검증

```powershell
python scripts/sft_cli.py validate --input raw_generations/batch_0001_raw.jsonl --refresh-report
```

검증만 하고 저장하지 않기:

```powershell
python scripts/sft_cli.py validate --input raw_generations/batch_0001_raw.jsonl --dry-run
```

---

## 5. 현재 파일들만으로는 아직 알 수 없거나 미완성인 부분

### 5.1 실제 teacher LLM API 호출부

현재 6개 파일에는 실제 Together AI 호출 코드가 없다.

현재 흐름은 여기까지다.

```text
request payload 생성
→ 외부 코드가 teacher LLM 호출
→ raw generation jsonl 저장
→ validator 실행
```

추가가 필요한 파일:

```text
sft_dataset/scripts/sft_teacher_client.py
```

예상 역할:

```text
Together AI API를 호출해 Gemma 4 31B IT teacher response를 받고 raw_generations/*.jsonl에 저장한다.
```

---

### 5.2 teacher system prompt 전문

현재 생성 request payload 구조는 있지만, teacher LLM에게 줄 최종 system prompt 전문은 아직 고정되지 않았다.

필요한 내용:

```text
- selected_bucket만 따른다.
- taxonomy 밖 값을 만들지 않는다.
- existing_valid_paraphrase_samples는 같은 의미의 표현 예시다.
- edge_flags는 selected_bucket에 있는 값만 유지한다.
- source_ref는 만들지 않는다.
- output은 sanitizer-repaired label이 아니라 raw valid label이어야 한다.
```

---

### 5.3 seed accepted sample

현재 request 방식은 기존 accepted paraphrase들을 보고 확장하는 방식이다.

따라서 최초에는 각 command slot마다 최소 1개 seed accepted sample이 필요하다.

seed가 없으면:

```text
request payload 생성 불가
```

가능한 해결:

```text
- 사람이 직접 seed master sample을 작성
- 기존 battle_eval_cases*.json을 master sample 형식으로 변환
- teacher에게 최초 seed만 별도 생성시키고 사람이 검수
```

---

### 5.4 validator의 actor-target 문맥 검증 보강

현재 validator는 runtime/schema/gold 검증은 하지만, 아래처럼 한국어 문장 구조 기반의 actor-target 문맥 검증은 아직 충분하지 않다.

추가해야 할 사항:

```text
비슷한 콤마 구조라도 문맥에 따라 actor-target, actor-actor, target-target을 구분해야 한다.
```

---

## 6. teacher LLM에게 반드시 알려야 하는 actor/target 문맥 규칙

현재의 워크플로우로 만든 데이터셋은 온디바이스 gemma4 E4b 모델을 sft 튜닝하는 데에 쓰일 예정인데, battle_eval_cases16.json 과 gemma_ollama_test16.py가 실제 작동하는 프롬프트와 코드를 담고 있다. 앞으로 이 시스템을 유지/보수 하는데에 있어, 이 파일들을 참고하는 것이 권장됨.

---

## 7. validator에 추가하는 것이 좋은 문맥 검증

validator에 아래 검증을 추가하는 것이 좋다.

### 7.1 command_spec slot 검증

목표:

```text
metadata의 actor_selection / target_selection / scenario_family와 command_spec.slots가 논리적으로 맞는지 검사한다.
```

예시:

```text
metadata.actor_selection = explicit_actor
metadata.target_selection = explicit_ally_target
command_text = "A_02, A_04에게 이동해"

기대:
slots.actor = "A_02"
slots.target = "A_04"
mentioned_units = ["A_02", "A_04"]
```

반대로 아래처럼 나오면 rejected가 맞다.

```json
{
  "slots": {
    "actor": ["A_02", "A_04"],
    "target": null
  }
}
```

---

### 7.2 explicit_multi_actor 검증

예시:

```text
metadata.actor_selection = explicit_multi_actor
command_text = "A_01, A_02는 뒤로 빠져"
```

기대:

```json
{
  "slots": {
    "actors": ["A_01", "A_02"],
    "target": null
  }
}
```

아래처럼 target으로 처리하면 rejected가 맞다.

```json
{
  "slots": {
    "actor": "A_01",
    "target": "A_02"
  }
}
```

---

### 7.3 target_selection 기반 검증

권장 규칙:

```text
explicit_ally_target이면 target은 ally unitId여야 한다.
explicit_enemy_target이면 target은 enemy unitId여야 한다.
none이면 명시 target slot이 없어야 한다.
invalid_explicit_target이면 명시 target은 있을 수 있지만, edge_flags 또는 scenario_family가 invalid 이유를 설명해야 한다.
```

---

### 7.4 action actor와 command_spec actor 일치 검증

권장 규칙:

```text
explicit_actor이면 output.action actor는 command_spec.slots.actor와 일치해야 한다.
explicit_multi_actor이면 output.action actor set은 command_spec.slots.actors의 부분집합 또는 gold.required_actors와 일치해야 한다.
explicit_ally_target인 경우 target이 actor로 잘못 들어가면 rejected한다.
```

---

## 8. 현재 전체 흐름

```text
1. taxonomy_sot.json으로 분류 기준과 목표 비율 정의
2. report 명령으로 현재 accepted coverage 확인
3. 부족한 bucket을 숫자 path로 request
4. sft_generation_request.py가 selected_bucket payload 생성
5. teacher LLM이 새 master sample 후보 생성
6. sft_validator.py가 parse/schema/runtime/policy/semantic/taxonomy 검증
7. 통과 sample은 accepted에 저장
8. 실패 sample은 rejected에 저장
9. report를 다시 생성해 coverage 갱신
```

---

## 9. 현재 설계의 핵심 원칙

```text
- accepted 폴더가 source of truth다.
- markdown report는 수동 수정하지 않는다.
- taxonomy_sot.json이 분류 기준의 source of truth다.
- 숫자 path는 사람 입력용이다.
- 내부 처리는 stable path 기준이다.
- skill sample은 general coverage와 skill coverage 양쪽에 모두 반영된다.
- command_style은 coverage row에 쓰지 않고 accepted sample에서 직접 읽는다.
- edge_flags는 selected_bucket에 속한다.
- individual paraphrase sample에 edge_flags를 따로 보내지 않는다.
- source_ref는 LLM에게 보내지 않는다.
- validator 통과 실패 sample은 학습 데이터에 넣지 않는다.
- sanitizer가 고친 output은 SFT label로 쓰지 않는다.
```





Synthetic SFT Coverage 생성 계획
1. 목표

목표는 “명령을 많이 만드는 것”이 아니라, 필요한 상황 bucket을 먼저 정의하고, 각 bucket을 validation 통과 샘플로 채우는 것이다.

학습 태스크는 고정한다.

전장 상태 + 한국어 명령
→ thinking / dialog / action JSON

중요도는 다음 순서다.

raw output semantic correctness
> schema correctness
> runtime validity
> policy validity
> dialog 품질
> 표현 다양성

학생 모델 런타임 구조는 현재 코드의 input + commandAnalysis → thinking/dialog/action 구조를 기준으로 유지한다.

2. source of truth

실제 기준 데이터는 markdown이 아니다.

기준은 다음이다.

validation을 통과한 accepted dataset 폴더
또는
master jsonl

markdown은 사람이 보기 위한 derived report다.

accepted/
  accepted_0001.jsonl
  accepted_0002.jsonl

reports/
  general_coverage.md
  skill_coverage.md

Python을 한 번 돌리면:

accepted 폴더 읽기
→ master sample 취합
→ general_coverage.md 재생성
→ skill_coverage.md 재생성

수동으로 markdown을 고치는 방식은 쓰지 않는다.

3. 일반 coverage table

일반 coverage table은 모든 샘플을 포함한다.

skill 관련 샘플도 여기에 반드시 들어간다.

계층 구조:

대주제
└── actor_selection
    └── target_selection
        └── action_pattern
            └── scenario_family
                └── 기준 명령 row

대주제 예:

attack
skill
skillControl
move
wait
empty

각 분류 노드는 자기 아래에 포함된 총량을 표시한다.

총 기준 명령 슬롯 수
총 accepted scenario/sample 수

최하위 기준 명령 row는 이런 형태다.

"기준 명령" @ paraphrase_sample_count @ edge_flags @ {문서풀네임_id 목록}

예:

"A_03, E_05에게 스킬을 써" @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_0003.jsonl_sample_000421
"A_03야, A_05에게 스킬을 써" @ 2 @ explicit_ally_target_conflicts_with_self_skill @ accepted_0004.jsonl_sample_000812, accepted_0005.jsonl_sample_000933

중요한 점:

최하위 row는 샘플 하나가 아니다.
같은 scenario/edge 의미를 가진 기준 명령 슬롯이다.
그 슬롯 아래에 validation 통과한 실제 paraphrase sample들의 문서/id 목록이 연결된다.
4. command_style 처리

command_style은 유지한다.

다만 coverage markdown 최하위 row에는 command_style 집계를 넣지 않는다.

이유:

LLM에게 생성 요청을 보낼 때
accepted sample 원문에서 command_text와 command_style을 직접 뽑아주면 충분하다.

즉 command_style은 master sample에는 남긴다.

예:

{
  "metadata": {
    "command_style": "direct_korean"
  }
}

하지만 coverage markdown row에는 굳이 이렇게 적지 않는다.

direct_korean: 3, casual_korean: 2

이건 불필요하다.

LLM 입력에서는 이렇게 보낸다.

{
  "command_text": "A_03, E_05에게 스킬을 써",
  "command_style": "direct_korean"
}

나중에 command_style 비율을 맞출 때도 accepted sample에서 직접 집계하면 된다.

5. skill coverage table

skill 관련 샘플은 두 곳에 모두 들어간다.

general_coverage.md
skill_coverage.md

skill coverage table은 skill 전용 분포를 보기 위한 derived report다.

계층 구조:

skill_family
└── skill_target_kind
    └── conflict_type
        └── 기준 명령 row

예:

self_buff
└── self
    └── text_enemy_target_but_self_skill
        └── "A_03, E_05에게 스킬을 써" @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_0003.jsonl_sample_000421

skill_case.conflict_type은 유지한다.
edge_flags와 겹치는 부분이 있어도, skill 전용 집계 축으로 유효하다.

skill과 무관한 샘플:

"skill_case": null

skill 관련 샘플:

"skill_case": {
  "skill_family": "self_buff",
  "skill_target_kind": "self",
  "is_skill_aoe": false,
  "can_skill_target_dead": false,
  "conflict_type": "text_enemy_target_but_self_skill"
}
6. edge_flags 위치

edge_flags는 paraphrase sample 각각에 붙여서 LLM에게 보내는 정보가 아니다.

같은 기준 명령 슬롯에서 파생된 paraphrase들은 완전히 같은 의미 / 같은 edge case를 유지해야 한다.

따라서 LLM 생성 입력에서는 edge_flags를 selected_bucket에 둔다.

맞는 구조:

{
  "selected_bucket": {
    "intent_family": "skill",
    "actor_selection": "explicit_actor",
    "target_selection": "explicit_enemy_target",
    "action_pattern": "skill_only",
    "scenario_family": "skill_self_target_conflict",
    "edge_flags": [
      "explicit_enemy_target_conflicts_with_self_skill"
    ],
    "skill_case": {
      "skill_family": "self_buff",
      "skill_target_kind": "self",
      "is_skill_aoe": false,
      "can_skill_target_dead": false,
      "conflict_type": "text_enemy_target_but_self_skill"
    }
  },
  "existing_valid_paraphrase_samples": [
    {
      "command_text": "A_03, E_05에게 스킬을 써",
      "command_style": "direct_korean"
    }
  ],
  "count_to_generate": 4
}

틀린 구조:

{
  "existing_valid_paraphrase_samples": [
    {
      "command_text": "A_03, E_05에게 스킬을 써",
      "command_style": "direct_korean",
      "edge_flags": [
        "explicit_enemy_target_conflicts_with_self_skill"
      ]
    }
  ]
}

이렇게 하면 edge case가 sample별로 다른 것처럼 보인다.
현재 설계에서는 틀린 표현이다.

7. source_ref 처리

source_ref는 LLM 입력에 넣지 않는다.

LLM은 생성에 필요한 의미 정보만 보면 된다.

LLM에게 필요한 것:

selected_bucket
existing command_text들
각 command_text의 command_style
count_to_generate

Python 내부 추적에는 {문서풀네임_id}를 유지한다.

coverage markdown row에는 문서/id 목록이 남는다.

accepted_0003.jsonl_sample_000421

하지만 LLM에게는 보내지 않는다.

8. 숫자 path와 stable path 분리

사람이 CLI에 입력할 때는 숫자 path를 쓴다.

예:

c1-2-1-3-1-10.4

의미:

일반 테이블의
1번째 대주제
2번째 actor_selection
1번째 target_selection
3번째 action_pattern
1번째 scenario_family
10번째 기준 명령 슬롯에 대해
새 paraphrase sample 4개 생성

skill override는 이렇게 쓴다.

c1-2-1-3-1-10/2-3-1.7

의미:

일반 테이블의 해당 기준 명령 슬롯을 기반으로,
skill table의
2번째 skill_family
3번째 skill_target_kind
1번째 conflict_type 조건으로
7개 생성

하지만 내부 저장과 핸들링은 숫자 path를 쓰지 않는다.

내부에서는 stable string path로 변환한다.

예:

{
  "display_path": "1-2-1-3-1-10",
  "stable_path": "skill.explicit_actor.explicit_enemy_target.skill_only.skill_self_target_conflict",
  "skill_stable_path": "self_buff.self.text_enemy_target_but_self_skill",
  "command_slot_id": "cmd_slot_skill_explicit_enemy_self_conflict_010"
}

숫자 path는 사람 입력용이다.
영구 ID나 내부 참조에는 쓰지 않는다.

9. valid matrix

모든 조합을 허용하지 않는다.

대주제별로 가능한 하위 축을 미리 제한한다.

예:

{
  "skillControl": {
    "allowed_actor_selection": [
      "explicit_actor",
      "explicit_multi_actor"
    ],
    "allowed_target_selection": [
      "none"
    ],
    "allowed_action_pattern": [
      "skillControl_defer",
      "skillControl_forbid"
    ],
    "allowed_scenario_family": [
      "explicit_defer_skill",
      "explicit_forbid_skill",
      "actor_has_no_skill"
    ]
  }
}

이게 없으면 coverage matrix가 불필요하게 폭발한다.

따라서 먼저 해야 할 일은:

대주제별 valid matrix 정의
→ 그 안에서 scenario_family 정의
→ 각 scenario_family 아래 기준 명령 슬롯 구성
10. 실제 생성 루프

전체 루프:

1. accepted dataset 폴더를 읽는다.
2. master sample들을 취합한다.
3. general_coverage.md와 skill_coverage.md를 재생성한다.
4. 사람이 부족한 bucket을 보고 숫자 path로 생성 요청을 입력한다.
5. Python이 숫자 path를 stable path로 변환한다.
6. 해당 기준 명령 슬롯에 연결된 문서풀네임_id 목록을 찾는다.
7. accepted DB에서 해당 sample들의 command_text와 command_style을 가져온다.
8. selected_bucket을 구성한다.
9. teacher LLM에게 selected_bucket + existing_valid_paraphrase_samples + count_to_generate를 보낸다.
10. teacher LLM이 새 paraphrase/sample 후보를 생성한다.
11. Python이 commandAnalysis를 재계산한다.
12. validator를 실행한다.
13. 통과한 sample만 accepted에 저장한다.
14. 실패한 sample은 rejected에 저장한다.
15. coverage report를 다시 생성한다.
11. LLM 입력 구조

일반 paraphrase 생성 요청의 핵심 구조:

{
  "selected_bucket": {
    "intent_family": "skill",
    "actor_selection": "explicit_actor",
    "target_selection": "explicit_enemy_target",
    "action_pattern": "skill_only",
    "scenario_family": "skill_self_target_conflict",
    "edge_flags": [
      "explicit_enemy_target_conflicts_with_self_skill"
    ],
    "skill_case": {
      "skill_family": "self_buff",
      "skill_target_kind": "self",
      "is_skill_aoe": false,
      "can_skill_target_dead": false,
      "conflict_type": "text_enemy_target_but_self_skill"
    }
  },
  "existing_valid_paraphrase_samples": [
    {
      "command_text": "A_03, E_05에게 스킬을 써",
      "command_style": "direct_korean"
    },
    {
      "command_text": "A_03, E_05한테 스킬 사용해",
      "command_style": "direct_korean"
    }
  ],
  "count_to_generate": 4
}

여기서 핵심은:

selected_bucket이 의미/상황/edge를 가진다.
existing_valid_paraphrase_samples는 표현 예시와 command_style만 가진다.
12. master sample 구조

master에는 관리용 정보를 모두 둔다.

{
  "id": "sample_000421",
  "split": "train",

  "command_spec": {
    "command_id": "cmd_skill_explicit_target_001",
    "command_text": "A_03, E_02한테 스킬 써",
    "template_group": "explicit_actor_explicit_target_skill_v1",
    "paraphrase_group": "explicit_target_skill_korean_01",
    "base_command_text": "A_01, E_02한테 스킬 써",
    "slots": {
      "actor": "A_03",
      "target": "E_02",
      "target_side_in_text": "enemy",
      "mentioned_units": ["A_03", "E_02"]
    }
  },

  "metadata": {
    "intent_family": "skill",
    "command_style": "direct_korean",
    "actor_selection": "explicit_actor",
    "target_selection": "explicit_enemy_target",
    "action_pattern": "skill_only",
    "scenario_family": "skill_self_target_conflict",
    "edge_flags": [
      "explicit_enemy_target_conflicts_with_self_skill"
    ],
    "difficulty": "medium"
  },

  "skill_case": {
    "skill_family": "self_buff",
    "skill_target_kind": "self",
    "is_skill_aoe": false,
    "can_skill_target_dead": false,
    "conflict_type": "text_enemy_target_but_self_skill"
  },

  "gold": {},
  "input": {},
  "output": {},

  "validator_result": {
    "passed": true,
    "failure_reasons": []
  }
}

폐기하는 field:

battlefield_seed
source
reviewed
13. SFT 학습 파일 구조

학습용 JSONL에는 관리 정보를 넣지 않는다.

넣지 않는 것:

metadata
skill_case
gold
validator_result
source_ref
coverage path

학습용에는 실제 런타임에서 모델이 보는 것만 넣는다.

{
  "messages": [
    {
      "role": "system",
      "content": "<SYSTEM_PROMPT>"
    },
    {
      "role": "user",
      "content": "{\"input\":...,\"commandAnalysis\":...}"
    },
    {
      "role": "assistant",
      "content": "{\"thinking\":\"...\",\"dialog\":[],\"action\":[]}"
    }
  ]
}
14. validator 통과 조건

accepted에 들어가려면 반드시 통과해야 한다.

JSON parse 가능
schema valid
runtime valid
policy valid
semantic gold pass
skillDescription exact match
skill target side valid
dialog/action actor 일치
extra field 없음
unknown action type 없음
sanitizer repair 필요 없음

특히 중요한 원칙:

SFT label은 raw output 기준이다.
sanitizer가 고친 output은 학습 label로 쓰지 않는다.
15. 최종 합의점 요약

현재 합의된 핵심은 이거다.

1. command_style은 유지한다.
2. command_style은 coverage markdown 최하위 row에 넣지 않는다.
3. command_style은 LLM 입력 시 기존 accepted sample에서 command_text와 함께 뽑아준다.
4. general coverage table은 모든 샘플을 포함한다.
5. skill sample은 general coverage와 skill coverage 양쪽에 모두 반영한다.
6. skill_case.conflict_type은 유지한다.
7. edge_flags는 selected_bucket에 둔다.
8. paraphrase sample 개별 항목에는 edge_flags를 넣지 않는다.
9. source_ref는 LLM에게 보내지 않는다.
10. coverage markdown은 accepted DB에서 재생성되는 derived report다.
11. 숫자 path는 사람 입력용이다.
12. 내부 ID와 참조는 stable string path를 쓴다.
13. 새 paraphrase 생성은 기준 명령 하나가 아니라, 기존 validation 통과 paraphrase sample들을 보고 확장한다.
14. valid matrix로 대주제별 가능한 하위 조합을 제한한다.
15. validator 통과 실패 sample은 dataset에 넣지 않는다.