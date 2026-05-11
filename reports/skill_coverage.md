# Skill Coverage

enemy_single_target_attack [15.6%(18%) / 7]
  enemy_alive [71.4%(80%) / 5]
    null [60.0%(55%) / 3]
      "A_03, E_02한테 공격 스킬 써." @ 1 @ [] @ accepted_20260512_035448.jsonl_seed_master_0103
      "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0043
      "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260512_032346.jsonl_seed_master_0058
    text_ally_target_but_enemy_skill [40.0%(25%) / 2]
      "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_031947.jsonl_seed_master_0050
      "A_03, A_02한테 공격 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0104
  enemy_dead [28.6%(20%) / 2]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 2]
      "A_03, 죽은 E_02한테 공격 스킬 써." @ 2 @ skill_target_dead_not_allowed @ accepted_20260512_031947.jsonl_seed_master_0047, accepted_20260512_035448.jsonl_seed_master_0105

self_buff [15.6%(14%) / 7]
  self [100.0%(100%) / 7]
    null [57.1%(45%) / 4]
      "A_03, 지금 스킬 써." @ 3 @ self_skill_without_explicit_target @ accepted_20260512_005252.jsonl_seed_master_0006, accepted_20260512_032346.jsonl_seed_master_0054, accepted_20260512_035444.jsonl_seed_master_0092
      "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260512_035437.jsonl_seed_master_0074
    text_enemy_target_but_self_skill [28.6%(35%) / 2]
      "A_03, E_02한테 스킬 써." @ 2 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260512_031947.jsonl_seed_master_0044, accepted_20260512_035444.jsonl_seed_master_0093
    text_ally_target_but_self_skill [14.3%(20%) / 1]
      "A_03, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260512_035444.jsonl_seed_master_0094

ally_shield [15.6%(13%) / 7]
  ally_alive [57.1%(85%) / 4]
    null [75.0%(50%) / 3]
      "A_04, A_02한테 보호 스킬 써." @ 1 @ [] @ accepted_20260512_035444.jsonl_seed_master_0095
      "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260512_005252.jsonl_seed_master_0007, accepted_20260512_031947.jsonl_seed_master_0049
    text_enemy_target_but_ally_skill [25.0%(30%) / 1]
      "A_04, E_02한테 보호 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_035444.jsonl_seed_master_0096
  ally_dead [42.9%(15%) / 3]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 3]
      "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035440.jsonl_seed_master_0084
      "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 2 @ skill_target_dead_not_allowed @ accepted_20260512_032346.jsonl_seed_master_0053, accepted_20260512_035444.jsonl_seed_master_0097

ally_heal [13.3%(11%) / 6]
  ally_alive [83.3%(85%) / 5]
    null [60.0%(55%) / 3]
      "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260512_035444.jsonl_seed_master_0098
      "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260512_032346.jsonl_seed_master_0059
      "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ no_valid_skill_target @ accepted_20260512_035433.jsonl_seed_master_0061
    text_enemy_target_but_ally_skill [40.0%(25%) / 2]
      "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_031947.jsonl_seed_master_0045
      "A_04, E_02한테 회복 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_035444.jsonl_seed_master_0099
  ally_dead [16.7%(15%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 1]
      "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035444.jsonl_seed_master_0100

ally_resurrection [8.9%(13%) / 4]
  ally_dead [50.0%(70%) / 2]
    null [100.0%(65%) / 2]
      "A_04, 쓰러진 A_02한테 부활 스킬 써." @ 1 @ dead_ally_skill_target_allowed @ accepted_20260512_035448.jsonl_seed_master_0101
      "A_04, 쓰러진 A_02한테 스킬 써." @ 1 @ dead_ally_skill_target_allowed @ accepted_20260512_032346.jsonl_seed_master_0051
  ally_alive [50.0%(30%) / 2]
    text_living_target_but_resurrection_skill [100.0%(35%) / 2]
      "A_04, 살아있는 A_02한테 부활 스킬 써." @ 2 @ text_living_target_but_resurrection_skill @ accepted_20260512_032346.jsonl_seed_master_0052, accepted_20260512_035448.jsonl_seed_master_0102

enemy_aoe_attack [8.9%(12%) / 4]
  enemy_alive [100.0%(100%) / 4]
    null [75.0%(75%) / 3]
      "A_06, 적들이 뭉친 쪽에 광역 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260512_035448.jsonl_seed_master_0109
      "A_06, 적들이 뭉친 쪽에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260512_005252.jsonl_seed_master_0008, accepted_20260512_032346.jsonl_seed_master_0055
    text_ally_target_but_enemy_skill [25.0%(25%) / 1]
      "A_06, A_02 주변에 광역 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0110

enemy_debuff [8.9%(8%) / 4]
  enemy_alive [75.0%(85%) / 3]
    null [66.7%(60%) / 2]
      "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0048
      "A_03, E_02한테 약화 스킬 써." @ 1 @ [] @ accepted_20260512_035448.jsonl_seed_master_0106
    text_ally_target_but_enemy_skill [33.3%(25%) / 1]
      "A_03, A_02한테 약화 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0107
  enemy_dead [25.0%(15%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(15%) / 1]
      "A_03, 죽은 E_02한테 약화 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035448.jsonl_seed_master_0108

mobility_skill [4.4%(5%) / 2]
  self [50.0%(50%) / 1]
    null [100.0%(100%) / 1]
      "A_01, 도약기로 빠져." @ 1 @ mobility_skill_self_escape @ accepted_20260512_035448.jsonl_seed_master_0111
  enemy_alive [50.0%(50%) / 1]
    null [100.0%(100%) / 1]
      "A_01, E_02에게 도약기로 붙어." @ 1 @ mobility_skill_enemy_approach @ accepted_20260512_035448.jsonl_seed_master_0112

no_skill [8.9%(6%) / 4]
  none [100.0%(100%) / 4]
    skill_actor_has_no_skill [100.0%(100%) / 4]
      "A_03, E_02한테 스킬 써." @ 3 @ actor_has_no_skill @ accepted_20260512_031947.jsonl_seed_master_0046, accepted_20260512_035440.jsonl_seed_master_0086, accepted_20260512_035448.jsonl_seed_master_0113
      "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260512_032346.jsonl_seed_master_0060
