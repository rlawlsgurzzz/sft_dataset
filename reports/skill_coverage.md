# Skill Coverage

enemy_single_target_attack [21.1%(18%) / 4]
  enemy_alive [75.0%(80%) / 3]
    null [66.7%(55%) / 2]
      "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0043
      "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260512_032346.jsonl_seed_master_0058
    text_ally_target_but_enemy_skill [33.3%(25%) / 1]
      "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_031947.jsonl_seed_master_0050
  enemy_dead [25.0%(20%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 1]
      "A_03, 죽은 E_02한테 공격 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_031947.jsonl_seed_master_0047

self_buff [15.8%(14%) / 3]
  self [100.0%(100%) / 3]
    null [66.7%(45%) / 2]
      "A_03, 지금 스킬 써." @ 2 @ self_skill_without_explicit_target @ accepted_20260512_005252.jsonl_seed_master_0006, accepted_20260512_032346.jsonl_seed_master_0054
    text_enemy_target_but_self_skill [33.3%(35%) / 1]
      "A_03, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260512_031947.jsonl_seed_master_0044

ally_shield [15.8%(13%) / 3]
  ally_alive [66.7%(85%) / 2]
    null [100.0%(50%) / 2]
      "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260512_005252.jsonl_seed_master_0007, accepted_20260512_031947.jsonl_seed_master_0049
  ally_dead [33.3%(15%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 1]
      "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_032346.jsonl_seed_master_0053

ally_heal [10.5%(11%) / 2]
  ally_alive [100.0%(85%) / 2]
    null [50.0%(55%) / 1]
      "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260512_032346.jsonl_seed_master_0059
    text_enemy_target_but_ally_skill [50.0%(25%) / 1]
      "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_031947.jsonl_seed_master_0045
  ally_dead [0.0%(15%) / 0]

ally_resurrection [10.5%(13%) / 2]
  ally_dead [50.0%(70%) / 1]
    null [100.0%(65%) / 1]
      "A_04, 쓰러진 A_02한테 스킬 써." @ 1 @ dead_ally_skill_target_allowed @ accepted_20260512_032346.jsonl_seed_master_0051
  ally_alive [50.0%(30%) / 1]
    text_living_target_but_resurrection_skill [100.0%(35%) / 1]
      "A_04, 살아있는 A_02한테 부활 스킬 써." @ 1 @ text_living_target_but_resurrection_skill @ accepted_20260512_032346.jsonl_seed_master_0052

enemy_aoe_attack [10.5%(12%) / 2]
  enemy_alive [100.0%(100%) / 2]
    null [100.0%(75%) / 2]
      "A_06, 적들이 뭉친 쪽에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260512_005252.jsonl_seed_master_0008, accepted_20260512_032346.jsonl_seed_master_0055

enemy_debuff [5.3%(8%) / 1]
  enemy_alive [100.0%(85%) / 1]
    null [100.0%(60%) / 1]
      "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0048
  enemy_dead [0.0%(15%) / 0]

mobility_skill [0.0%(5%) / 0]
  self [0.0%(50%) / 0]
  enemy_alive [0.0%(50%) / 0]

no_skill [10.5%(6%) / 2]
  none [100.0%(100%) / 2]
    skill_actor_has_no_skill [100.0%(100%) / 2]
      "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260512_031947.jsonl_seed_master_0046
      "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260512_032346.jsonl_seed_master_0060
