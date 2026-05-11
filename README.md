# Synthetic SFT Dataset 설계 요약

## 1. 목적

이 데이터셋은 전장 상태와 한국어 자연어 명령을 입력받아, 학생 SLM이 전투 명령 결과를 안정적인 JSON으로 출력하도록 학습시키기 위한 Synthetic SFT dataset이다.

```text
전장 상태 + 한국어 명령 + commandAnalysis
→ thinking / dialog / action JSON
```

학습 대상은 단순한 문장 paraphrase가 아니다. 명령 의미, actor/target/action 판단, skill target side, 현재 전장 상태, 런타임 유효성, dialog/action 일치까지 포함한 전투 명령 파서 동작 전체다.

품질 우선순위는 다음이다.

```text
raw output semantic correctness
> schema correctness
> runtime validity
> policy validity
> dialog 품질
> 표현 다양성
```

SFT label은 처음부터 유효한 assistant output이어야 한다. sanitizer가 보정한 결과는 label로 사용하지 않는다.

---

## 2. 전체 역할 분리

### 2.1 teacher LLM

teacher LLM은 master sample 후보를 생성한다.

teacher가 생성하는 항목은 다음이다.

```text
id
split
command_spec
metadata
skill_case
gold
input.input.command
input.input.area_situation
output
```

teacher는 전장 상태를 완전하게 창작하고, 그 전장 상태와 명령에 맞는 정답 `thinking / dialog / action`을 만든다.

teacher는 `commandAnalysis`를 생성하지 않는다.

### 2.2 validator

validator는 teacher가 생성한 raw sample을 검증한다.

검증 범위는 다음이다.

```text
JSON parse
master sample schema
metadata taxonomy
skill_case taxonomy
area_situation schema
unit runtime validity
output schema
action runtime validity
skill target validity
dialog/action actor consistency
gold semantic consistency
```

검증을 통과한 sample은 accepted에 저장된다. 이때 validator가 `area_situation`을 읽어 `input.commandAnalysis`를 계산해 추가한다.

### 2.3 student SLM

student SLM은 accepted sample에서 만들어진 최종 입력을 학습한다.

학생 모델의 입력은 다음 구조를 가진다.

```json
{
  "input": {
    "command": "한국어 명령",
    "area_situation": {
      "allies": [],
      "enemies": []
    }
  },
  "commandAnalysis": {
    "analysisMode": "runtime_constraint_summary",
    "allowedActors": [],
    "allowedAttackTargets": [],
    "validMoveToUnits": [],
    "deadAllies": [],
    "invalidUnits": [],
    "actionPolicy": {}
  }
}
```

학생 모델의 출력은 다음 세 top-level key로 고정된다.

```json
{
  "thinking": "짧은 판단 요약",
  "dialog": [],
  "action": []
}
```

---

## 3. raw sample 구조

teacher가 생성하는 raw sample은 다음 구조를 따른다.

```json
{
  "id": "sample id",
  "split": "train",
  "command_spec": {},
  "metadata": {},
  "skill_case": null,
  "gold": {},
  "input": {
    "input": {
      "command": "한국어 명령",
      "area_situation": {
        "allies": [],
        "enemies": []
      }
    }
  },
  "output": {
    "thinking": "짧은 판단 요약",
    "dialog": [],
    "action": []
  }
}
```

raw sample에는 다음 항목이 들어가면 안 된다.

```text
input.commandAnalysis
commandAnalysis
allowedActors
allowedAttackTargets
validMoveToUnits
deadAllies
invalidUnits
actionPolicy
validator_result
source_ref
```

---

## 4. accepted sample 구조

accepted sample은 raw sample에 validator 산출물이 추가된 형태다.

```json
{
  "input": {
    "input": {
      "command": "한국어 명령",
      "area_situation": {
        "allies": [],
        "enemies": []
      }
    },
    "commandAnalysis": {
      "analysisMode": "runtime_constraint_summary",
      "allowedActors": [],
      "allowedAttackTargets": [],
      "validMoveToUnits": [],
      "deadAllies": [],
      "invalidUnits": [],
      "actionPolicy": {}
    }
  },
  "validator_result": {
    "passed": true,
    "failure_reasons": []
  }
}
```

accepted 폴더가 학습 데이터와 coverage 집계의 source of truth다.

---

## 5. 전장 상태 스키마

`area_situation`은 항상 두 배열을 가진다.

```json
{
  "allies": [],
  "enemies": []
}
```

### 5.1 allies

`allies`에는 정확히 6명의 아군이 들어간다.

```text
A_01
A_02
A_03
A_04
A_05
A_06
```

아군 유닛 필수 필드는 다음이다.

```json
{
  "unitId": "A_01",
  "isAlive": true,
  "canBeTargeted": true,
  "isRanged": false,
  "hpRatio": 0.78,
  "attackRatioToAvg": 1.08,
  "engagedByOpponentCount": 1,
  "teamFormationRole": "frontline",
  "skillDescription": "스킬 설명 문자열",
  "IsSkillOnSelf": false,
  "IsSkillOnOtherAlly": false,
  "isSkillAoe": false,
  "canSkillTargetDead": false,
  "closestTargetableOpponent": "E_02",
  "farthestTargetableOpponent": "E_06",
  "closestAliveAlly": "A_02",
  "farthestAliveAlly": "A_05"
}
```

### 5.2 enemies

`enemies`에는 정확히 6명의 적이 들어간다.

```text
E_01
E_02
E_03
E_04
E_05
E_06
```

적 유닛 필수 필드는 다음이다.

```json
{
  "unitId": "E_01",
  "isAlive": true,
  "canBeTargeted": true,
  "isRanged": false,
  "hpRatio": 0.82,
  "attackRatioToAvg": 1.12,
  "engagedByOpponentCount": 1,
  "teamFormationRole": "frontline"
}
```

### 5.3 단일 거리 신호 필드

아군 유닛에는 네 개의 단일 거리 신호 필드가 있다.

```text
closestTargetableOpponent
farthestTargetableOpponent
closestAliveAlly
farthestAliveAlly
```

규칙은 다음이다.

```text
- 네 필드는 배열이 아니다.
- 값은 unitId string 또는 null이다.
- unitId는 최대 하나만 들어간다.
- closestTargetableOpponent와 farthestTargetableOpponent에는 살아있고 canBeTargeted=true인 enemy만 들어간다.
- closestAliveAlly와 farthestAliveAlly에는 자기 자신을 제외한 살아있는 ally만 들어간다.
- 후보가 없으면 null이다.
- 후보가 1명뿐이면 closest와 farthest가 같은 unitId다.
- 후보가 2명 이상이면 closest와 farthest는 서로 다른 unitId다.
```

실제 거리 계산은 런타임 엔진에서 수행한다. Synthetic dataset에서는 teacher가 전술 상황에 맞는 논리적 거리 관계를 만든다.

---

## 6. 죽은 유닛 규칙

이 게임에서는 죽은 유닛도 보통 `canBeTargeted=true`일 수 있다.

죽은 유닛 규칙은 다음이다.

```text
- 죽은 ally는 actor가 될 수 없다.
- 죽은 enemy는 attack target이 될 수 없다.
- 죽은 unit은 move.to가 될 수 없다.
- 죽은 unit은 단일 거리 신호 필드에 들어갈 수 없다.
- 죽었지만 canBeTargeted=true인 ally는 validator가 commandAnalysis.deadAllies에 포함한다.
- canSkillTargetDead=true인 skill만 죽은 targetable ally를 skill target으로 사용할 수 있다.
```

---

## 7. commandAnalysis

`commandAnalysis`는 명령 의도 파서가 아니다.

역할은 현재 전장 상태에서 런타임상 가능한 범위를 요약하는 것이다.

```json
{
  "analysisMode": "runtime_constraint_summary",
  "allowedActors": [],
  "allowedAttackTargets": [],
  "validMoveToUnits": [],
  "deadAllies": [],
  "invalidUnits": [],
  "actionPolicy": {}
}
```

계산 기준은 다음이다.

```text
allowedActors: 살아있는 ally
allowedAttackTargets: 살아있고 canBeTargeted=true인 enemy
validMoveToUnits: 살아있는 ally + 살아있고 canBeTargeted=true인 enemy
deadAllies: 죽었지만 canBeTargeted=true인 ally
invalidUnits: 죽은 ally, 죽은 enemy, untargetable enemy 등
actionPolicy: action 관련 고정 정책
```

학생 SLM은 `commandAnalysis`를 참고하지만, actor/target/action 의미 해석은 직접 수행한다.

---

## 8. 출력 action 스키마

허용 action type은 다음이다.

```text
move
attack
skill
wait
skillControl
```

### 8.1 move

```json
{
  "type": "move",
  "subtype": "approachOpponent",
  "movementType": "direct",
  "to": "E_01"
}
```

규칙은 다음이다.

```text
subtype: approachOpponent | escape | help | holdFront
movementType: direct | flank
to: validMoveToUnits 안의 unitId
to에는 actor 자신의 unitId를 쓰지 않는다.
```

### 8.2 attack

```json
{
  "type": "attack",
  "target": "E_01"
}
```

규칙은 다음이다.

```text
target은 allowedAttackTargets 안의 enemy unitId다.
죽은 enemy나 untargetable enemy는 attack target이 될 수 없다.
```

### 8.3 skill

```json
{
  "type": "skill",
  "description": "actor의 정확한 skillDescription 문자열",
  "target": "unitId"
}
```

규칙은 다음이다.

```text
description은 actor.skillDescription과 정확히 같아야 한다.
IsSkillOnSelf=true이면 target은 actor 자신이다.
IsSkillOnOtherAlly=true이면 target은 actor 자신이 아닌 ally다.
IsSkillOnSelf=false이고 IsSkillOnOtherAlly=false이면 target은 enemy다.
canSkillTargetDead=false이면 죽은 unit을 target으로 쓰지 않는다.
canSkillTargetDead=true이면 죽은 targetable ally를 target으로 쓸 수 있다.
isSkillAoe=true여도 output target은 중심 unitId 하나만 쓴다.
```

### 8.4 wait

```json
{
  "type": "wait",
  "durationSec": 2
}
```

규칙은 다음이다.

```text
wait은 명령에 대기, 지연, 타이밍 조절, 위치 유지 의미가 직접 있을 때만 사용한다.
durationSec는 1 이상 10 이하 number다.
attack 또는 skill 뒤에는 wait을 붙이지 않는다.
```

### 8.5 skillControl

```json
{
  "type": "skillControl",
  "mode": "defer",
  "durationSec": 5
}
```

또는:

```json
{
  "type": "skillControl",
  "mode": "forbid"
}
```

규칙은 다음이다.

```text
skillControl은 스킬 지연 또는 금지 의도가 명령에 명시될 때만 사용한다.
mode=defer이면 durationSec는 1 이상 10 이하 number다.
mode=forbid이면 durationSec를 쓰지 않는다.
```

---

## 9. dialog 규칙

```text
- dialog는 action actor당 정확히 하나만 만든다.
- action에 없는 unitId는 dialog에 넣지 않는다.
- 같은 unitId의 dialog를 여러 개 만들지 않는다.
- 여러 actor에게 완전히 같은 text를 반복하지 않는다.
- text는 actor의 전체 sequence를 짧은 한국어 한 문장으로 요약한다.
```

---

## 10. command_spec

`command_spec`은 명령문과 명령문 내부 slot을 설명한다.

```json
{
  "command_text": "A_02, A_04에게 이동해",
  "base_command_text": "A_01, A_02에게 이동해",
  "slots": {
    "actors": ["A_02"],
    "target": "A_04",
    "target_side_in_text": "ally",
    "mentioned_units": ["A_02", "A_04"]
  }
}
```

규칙은 다음이다.

```text
command_spec.command_text는 input.input.command와 정확히 같아야 한다.
actors는 명령문에서 행동 주체로 지정된 ally unitId 목록이다.
target은 명령문에서 대상 역할을 하는 unitId 또는 null이다.
target_side_in_text는 ally | enemy | self | none 중 하나다.
mentioned_units는 명령문에 직접 등장한 모든 unitId 목록이다.
```

한국어 명령은 조사, 동사, 문맥으로 actor와 target을 구분한다.

```text
"A_02, A_04에게 이동해" → A_02 actor, A_04 target
"A_04, A_02한테 스킬 써" → A_04 actor, A_02 target
"A_01, A_02는 뒤로 빠져" → A_01과 A_02 모두 actor
```

---

## 11. metadata와 taxonomy

`taxonomy_sot.json`이 분류 기준의 source of truth다.

`metadata`는 다음 필드를 가진다.

```json
{
  "intent_family": "skill",
  "command_style": "direct_korean",
  "actor_selection": "explicit_actor",
  "target_selection": "explicit_enemy_target",
  "action_pattern": "skill_only",
  "scenario_family": "skill_self_target_conflict",
  "edge_flags": []
}
```

모든 값은 taxonomy 안에 존재해야 한다.

`skill_case`는 skill 관련 sample에서만 object이며, 그 외에는 `null`이다.

```json
{
  "skill_family": "self_buff",
  "skill_target_kind": "self",
  "is_skill_aoe": false,
  "can_skill_target_dead": false,
  "conflict_type": "text_enemy_target_but_self_skill"
}
```

---

## 12. gold

`gold`는 validator가 output의 의미 일치를 검사하기 위한 정답 기준이다.

주요 필드는 다음이다.

```json
{
  "required_actors": [],
  "allowed_actors": [],
  "forbidden_actors": [],
  "required_action_types": [],
  "allowed_action_types": [],
  "forbidden_action_types": [],
  "empty_action_allowed": false,
  "expected_action_pattern": "attack_only",
  "targets": {
    "required": [],
    "allowed": [],
    "forbidden": []
  }
}
```

필요한 경우 action별 세부 기준도 포함할 수 있다.

```json
{
  "attack": {
    "actor": "A_01",
    "required_target": "E_02"
  },
  "skill": {
    "actor": "A_04",
    "required_target": "A_02",
    "description_exact": "죽은 아군 하나를 전투 가능한 상태로 되살린다."
  },
  "move": {
    "actor": "A_02",
    "required_subtype": "help",
    "required_to": "A_04"
  },
  "skillControl": {
    "actor": "A_03",
    "required_mode": "defer"
  }
}
```

---

## 13. 주요 파일

### 13.1 `config/taxonomy_sot.json`

역할:

```text
분류 기준, 목표 비율, valid matrix, skill valid matrix, edge_flags enum, 설명을 담는 machine-readable SOT.
```

### 13.2 `scripts/sft_taxonomy.py`

역할:

```text
taxonomy_sot.json 로드
숫자 path 파싱
stable path 변환
general path 검증
skill override path 검증
selected_bucket 설명 추출
metadata와 skill_case taxonomy 검증
```

### 13.3 `scripts/sft_coverage_report.py`

역할:

```text
accepted/*.jsonl을 읽어 coverage를 집계하고 reports/*.md를 재생성한다.
```

생성되는 report:

```text
reports/taxonomy_sot.md
reports/general_coverage.md
reports/skill_coverage.md
reports/coverage_summary.md
```

### 13.4 `scripts/sft_generation_request.py`

역할:

```text
숫자 path 요청을 파싱하고, accepted sample에서 같은 command slot의 표현 예시를 추출해 teacher LLM 요청 payload를 만든다.
```

payload 핵심 구조:

```json
{
  "request": {},
  "selected_bucket": {},
  "existing_valid_paraphrase_samples": [],
  "count_to_generate": 4,
  "runtime_generation_contract": {},
  "area_situation_contract": {},
  "assistant_output_contract": {},
  "generation_constraints": []
}
```

### 13.5 `scripts/sft_teacher_client.py`

역할:

```text
teacher LLM을 호출하고 raw generation JSONL을 저장한다.
```

teacher 시스템 프롬프트에는 다음이 포함된다.

```text
teacher 생성 계약
학생 SLM runtime system prompt 전문
area_situation 생성 규칙
commandAnalysis 생성 금지 규칙
output 생성 규칙
schema skeleton
```

### 13.6 `scripts/sft_validator.py`

역할:

```text
teacher raw sample을 검증하고 accepted 또는 rejected로 분류한다.
accepted 저장 시 commandAnalysis를 계산해 추가한다.
```

### 13.7 `scripts/sft_cli.py`

역할:

```text
report 생성, request 생성, validate 실행을 하나의 CLI로 묶는다.
```

---

## 14. 주요 명령어

### 14.1 coverage report 생성

```powershell
python scripts/sft_cli.py report
```

### 14.2 teacher LLM 요청 payload 생성

```powershell
python scripts/sft_cli.py request c1-2-1-3-1-10.4 --print-json
```

skill override 포함 예:

```powershell
python scripts/sft_cli.py request c3-1-1-4-4-1/2-3-2.4 --print-json
```

### 14.3 teacher LLM 호출

```powershell
python scripts/sft_teacher_client.py --input raw_generations/request_0001.json --output raw_generations/raw_0001.jsonl --trace-output raw_generations/trace_0001.jsonl --stream-output
```

### 14.4 teacher 결과 검증

```powershell
python scripts/sft_cli.py validate --input raw_generations/raw_0001.jsonl --refresh-report
```

검증만 실행:

```powershell
python scripts/sft_cli.py validate --input raw_generations/raw_0001.jsonl --dry-run
```

---

## 15. 전체 루프

```text
1. taxonomy_sot.json으로 분류 기준과 valid matrix를 정의한다.
2. accepted 폴더를 기준으로 coverage report를 생성한다.
3. 부족한 command slot을 숫자 path로 선택한다.
4. sft_generation_request.py가 teacher payload를 만든다.
5. sft_teacher_client.py가 teacher LLM을 호출해 raw sample 후보를 저장한다.
6. sft_validator.py가 raw sample을 검증한다.
7. 통과 sample은 commandAnalysis가 추가되어 accepted에 저장된다.
8. 실패 sample은 rejected에 저장된다.
9. coverage report를 다시 생성한다.
10. accepted sample을 SFT 학습 데이터로 변환한다.
```

---

## 16. 설계 원칙

```text
- accepted 폴더가 source of truth다.
- reports/*.md는 derived report다.
- taxonomy_sot.json이 분류 기준의 source of truth다.
- 숫자 path는 사람 입력용이다.
- 내부 처리는 stable path 기준이다.
- teacher raw output에는 commandAnalysis가 없다.
- commandAnalysis는 validator 산출물이다.
- selected_bucket이 의미/상황/edge를 가진다.
- existing_valid_paraphrase_samples는 표현 예시와 command_style만 가진다.
- source_ref는 teacher 입력과 output에 넣지 않는다.
- validator 통과 실패 sample은 학습 데이터에 넣지 않는다.
- sanitizer가 고친 output은 SFT label로 쓰지 않는다.
```
