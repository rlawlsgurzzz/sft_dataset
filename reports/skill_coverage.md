# Skill Coverage

enemy_single_target_attack [25.8%(18%) / 16]
  enemy_alive [81.2%(80%) / 13]
    null [84.6%(55%) / 11]
      "A_03, E_02한테 공격 스킬 써." @ 1 @ [] @ accepted_20260513_012220.jsonl_seed_master_0103
      "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260513_012219.jsonl_seed_master_0043
      "A_03, 가장 가까운 적에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260513_012221.jsonl_seed_master_0167
      "A_03, 적 후열에게 접근해서 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260513_012221.jsonl_seed_master_0172
      "A_03, 체력이 제일 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260513_012221.jsonl_seed_master_0165
      "A_03과 A_06은 E_02에게 스킬을 써." @ 1 @ [] @ accepted_20260513_012222.jsonl_seed_master_0177
      "A_03은 E_01에게, A_06은 E_03에게 스킬을 써." @ 1 @ [] @ accepted_20260513_012222.jsonl_seed_master_0179
      "A_03은 적 전열에, A_06은 적 후열에 스킬을 써." @ 1 @ target_role_backline_enemy @ accepted_20260513_012222.jsonl_seed_master_0182
      "스킬 쓸 수 있는 아군은 체력 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260513_012222.jsonl_seed_master_0185
      "스킬을 쓰기 안전한 아군은 E_02에게 스킬 써." @ 1 @ healthy_actor_selection @ accepted_20260513_012222.jsonl_seed_master_0187
      "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260513_012219.jsonl_seed_master_0058
    text_ally_target_but_enemy_skill [15.4%(25%) / 2]
      "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260513_012219.jsonl_seed_master_0050
      "A_03, A_02한테 공격 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260513_012220.jsonl_seed_master_0104
  enemy_dead [18.8%(20%) / 3]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 3]
      "A_03, 죽은 E_02한테 공격 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012219.jsonl_seed_master_0047
      "A_03, 죽은 E_02한테 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012222.jsonl_seed_master_0174
      "A_03, 죽은 E_02한테 스킬 써." @ 1 @ named_target_dead, no_valid_skill_target @ accepted_20260513_012222.jsonl_seed_master_0175

self_buff [4.8%(14%) / 3]
  self [100.0%(100%) / 3]
    null [33.3%(45%) / 1]
      "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260513_012220.jsonl_seed_master_0074
    text_enemy_target_but_self_skill [33.3%(35%) / 1]
      "A_03, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260513_012219.jsonl_seed_master_0044
    text_ally_target_but_self_skill [33.3%(20%) / 1]
      "A_03, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260513_012220.jsonl_seed_master_0094

ally_shield [9.7%(13%) / 6]
  ally_alive [66.7%(85%) / 4]
    null [75.0%(50%) / 3]
      "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260513_012219.jsonl_seed_master_0049, accepted_20260513_012220.jsonl_seed_master_0095
      "A_04는 A_01에게, A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260513_012222.jsonl_seed_master_0181
    text_enemy_target_but_ally_skill [25.0%(30%) / 1]
      "A_04, E_02한테 보호 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260513_012220.jsonl_seed_master_0096
  ally_dead [33.3%(15%) / 2]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 2]
      "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012220.jsonl_seed_master_0084
      "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012219.jsonl_seed_master_0053

ally_heal [16.1%(11%) / 10]
  ally_alive [90.0%(85%) / 9]
    null [77.8%(55%) / 7]
      "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260513_012220.jsonl_seed_master_0098
      "A_04, 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260513_012221.jsonl_seed_master_0173
      "A_04와 A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260513_012222.jsonl_seed_master_0180
      "A_04와 A_05는 체력이 제일 낮은 아군에게 스킬을 써." @ 1 @ low_hp_ally_target @ accepted_20260513_012222.jsonl_seed_master_0183
      "회복 가능한 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260513_012222.jsonl_seed_master_0186
      "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260513_012219.jsonl_seed_master_0059
      "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ no_valid_skill_target @ accepted_20260513_012220.jsonl_seed_master_0061
    text_enemy_target_but_ally_skill [22.2%(25%) / 2]
      "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260513_012219.jsonl_seed_master_0045
      "A_04, E_02한테 회복 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260513_012220.jsonl_seed_master_0099
  ally_dead [10.0%(15%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(20%) / 1]
      "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012220.jsonl_seed_master_0100

ally_resurrection [4.8%(13%) / 3]
  ally_dead [66.7%(70%) / 2]
    null [100.0%(65%) / 2]
      "A_04, 쓰러진 A_02한테 스킬 써." @ 2 @ dead_ally_skill_target_allowed @ accepted_20260513_012219.jsonl_seed_master_0051, accepted_20260513_012220.jsonl_seed_master_0101
  ally_alive [33.3%(30%) / 1]
    text_living_target_but_resurrection_skill [100.0%(35%) / 1]
      "A_04, 살아있는 A_02한테 부활 스킬 써." @ 1 @ text_living_target_but_resurrection_skill @ accepted_20260513_012219.jsonl_seed_master_0052

enemy_aoe_attack [14.5%(12%) / 9]
  enemy_alive [100.0%(100%) / 9]
    null [88.9%(75%) / 8]
      "A_03과 A_06은 E_02 주변에 스킬을 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260513_012222.jsonl_seed_master_0178
      "A_05, E_03 주변에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260513_012221.jsonl_seed_master_0164
      "A_06, 가장 가까운 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260513_012221.jsonl_seed_master_0169
      "A_06, 적 후열이 뭉친 곳에 스킬 써." @ 1 @ target_role_backline_enemy, aoe_skill_requires_single_center_target @ accepted_20260513_012221.jsonl_seed_master_0170
      "A_06, 적들이 뭉친 쪽에 스킬 써." @ 3 @ aoe_skill_requires_single_center_target @ accepted_20260513_012218.jsonl_seed_master_0008, accepted_20260513_012219.jsonl_seed_master_0055, accepted_20260513_012220.jsonl_seed_master_0109
      "A_06, 체력이 제일 낮은 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260513_012221.jsonl_seed_master_0166
    text_ally_target_but_enemy_skill [11.1%(25%) / 1]
      "A_06, A_02 주변에 광역 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260513_012220.jsonl_seed_master_0110

enemy_debuff [9.7%(8%) / 6]
  enemy_alive [83.3%(85%) / 5]
    null [80.0%(60%) / 4]
      "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260513_012219.jsonl_seed_master_0048
      "A_03, E_02한테 약화 스킬 써." @ 1 @ [] @ accepted_20260513_012220.jsonl_seed_master_0106
      "A_03, 가장 가까운 적에게 스킬 써." @ 1 @ [] @ accepted_20260513_012221.jsonl_seed_master_0168
      "A_03, 적 후열에게 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260513_012221.jsonl_seed_master_0171
    text_ally_target_but_enemy_skill [20.0%(25%) / 1]
      "A_03, A_02한테 약화 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260513_012220.jsonl_seed_master_0107
  enemy_dead [16.7%(15%) / 1]
    text_dead_target_but_skill_cannot_target_dead [100.0%(15%) / 1]
      "A_03, 죽은 E_02한테 약화 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260513_012220.jsonl_seed_master_0108

mobility_skill [3.2%(5%) / 2]
  self [50.0%(50%) / 1]
    null [100.0%(100%) / 1]
      "A_01, 도약기로 빠져." @ 1 @ mobility_skill_self_escape @ accepted_20260513_012220.jsonl_seed_master_0111
  enemy_alive [50.0%(50%) / 1]
    null [100.0%(100%) / 1]
      "A_01, E_02에게 도약기로 붙어." @ 1 @ mobility_skill_enemy_approach @ accepted_20260513_012220.jsonl_seed_master_0112

no_skill [11.3%(6%) / 7]
  none [100.0%(100%) / 7]
    skill_actor_has_no_skill [100.0%(100%) / 7]
      "A_03, E_02한테 스킬 써." @ 2 @ actor_has_no_skill @ accepted_20260513_012219.jsonl_seed_master_0046, accepted_20260513_012220.jsonl_seed_master_0086
      "A_03, 지금 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260513_012222.jsonl_seed_master_0176
      "A_03과 A_04는 죽은 E_02한테 스킬 써." @ 1 @ actor_has_no_skill, named_target_dead @ accepted_20260513_012223.jsonl_seed_master_0211
      "A_03과 A_04는 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260513_012222.jsonl_seed_master_0184
      "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260513_012219.jsonl_seed_master_0060
      "스킬 가능한 아군은 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260513_012222.jsonl_seed_master_0188
