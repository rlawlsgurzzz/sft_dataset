# General Coverage

attack [21.8%(24%) / 41]
  explicit_actor [56.1%(35%) / 23]
    explicit_enemy_target [21.7%(30%) / 5]
      attack_only [40.0%(45%) / 2]
        simple_clear_target [50.0%(18%) / 1]
          "A_01, E_02를 공격해." @ 1 @ [] @ accepted_20260514_002649.jsonl_seed_master_0001
        multiple_valid_targets [50.0%(10%) / 1]
          "A_01, 지금 가장 처리하기 좋은 적을 골라 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0114
      move_then_attack [60.0%(25%) / 3]
        simple_clear_target [33.3%(18%) / 1]
          "A_01, E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0115
        pressure_source_target_clear [33.3%(8%) / 1]
          "A_01, E_02에게 붙어서 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0116
        flank_attack_requested [33.3%(6%) / 1]
          "A_01, E_02의 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260514_002740.jsonl_seed_master_0014
    nearest_enemy [13.0%(15%) / 3]
      attack_only [66.7%(45%) / 2]
        multiple_valid_targets [50.0%(10%) / 1]
          "A_01, 가장 가까운 적을 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0117
        nearest_target_clear [50.0%(8%) / 1]
          "A_02, 가장 가까운 적을 공격해." @ 1 @ [] @ accepted_20260514_002649.jsonl_seed_master_0002
      move_then_attack [33.3%(25%) / 1]
        nearest_target_clear [100.0%(8%) / 1]
          "A_02, 제일 가까운 적한테 붙어서 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0015
    lowest_hp_enemy [13.0%(15%) / 3]
      attack_only [66.7%(45%) / 2]
        multiple_valid_targets [50.0%(10%) / 1]
          "A_01, 체력이 제일 낮은 적을 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0118
        lowest_hp_target_clear [50.0%(8%) / 1]
          "A_03, 체력이 제일 낮은 적을 노려." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0016
      move_then_attack [33.3%(25%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "A_01, 체력이 제일 낮은 적에게 붙어서 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0119
    highest_threat_enemy [13.0%(12%) / 3]
      attack_only [66.7%(45%) / 2]
        multiple_valid_targets [50.0%(10%) / 1]
          "A_01, 가장 위협적인 적을 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0120
        highest_threat_target_clear [50.0%(7%) / 1]
          "A_01, 제일 위험한 적부터 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0017
      move_then_attack [33.3%(25%) / 1]
        highest_threat_target_clear [100.0%(7%) / 1]
          "A_01, 제일 위험한 적에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0121
    role_based_enemy [17.4%(12%) / 4]
      attack_only [75.0%(45%) / 3]
        multiple_valid_targets [33.3%(10%) / 1]
          "A_01, 후열 적을 먼저 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0122
        role_based_target_clear [66.7%(8%) / 2]
          "A_02, 적 원거리 유닛을 먼저 끊어." @ 1 @ target_role_ranged_enemy @ accepted_20260514_002740.jsonl_seed_master_0018
          "A_02, 후방에 있는 적부터 노려." @ 1 @ target_role_backline_enemy @ accepted_20260514_002740.jsonl_seed_master_0019
      move_then_attack [25.0%(25%) / 1]
        role_based_target_clear [100.0%(8%) / 1]
          "A_01, 적 후열 쪽으로 붙어서 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0123
    pressure_source_enemy [13.0%(10%) / 3]
      attack_only [66.7%(45%) / 2]
        pressure_source_target_clear [100.0%(8%) / 2]
          "A_01, A_02를 때리는 적을 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0124
          "A_03, A_02를 때리는 적을 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002740.jsonl_seed_master_0021
      move_then_attack [33.3%(25%) / 1]
        pressure_source_target_clear [100.0%(8%) / 1]
          "A_01, A_02를 압박하는 적에게 붙어서 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0125
    invalid_explicit_target [8.7%(6%) / 2]
      empty_action_expected [100.0%(5%) / 2]
        dead_named_target [50.0%(6%) / 1]
          "A_01, 죽은 E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260514_002742.jsonl_seed_master_0126
        untargetable_named_target [50.0%(5%) / 1]
          "A_01, 숨어 있는 E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260514_002742.jsonl_seed_master_0127
  explicit_multi_actor [22.0%(15%) / 9]
    explicit_enemy_target [22.2%(30%) / 2]
      multi_actor_same_target [50.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "A_01과 A_02는 E_01을 같이 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0022
      multi_actor_different_targets [50.0%(7%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "A_01은 E_01을, A_02는 E_03을 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0023
    nearest_enemy [11.1%(15%) / 1]
      multi_actor_different_targets [100.0%(7%) / 1]
        nearest_target_clear [100.0%(8%) / 1]
          "A_01과 A_02는 각자 가장 가까운 적을 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0128
    lowest_hp_enemy [22.2%(15%) / 2]
      multi_actor_same_target [50.0%(18%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "A_01과 A_02는 체력이 제일 낮은 적을 같이 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0129
      multi_actor_different_targets [50.0%(7%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "A_01과 A_02는 각자 체력이 제일 낮은 적을 노려." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0130
    highest_threat_enemy [11.1%(12%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        highest_threat_target_clear [100.0%(7%) / 1]
          "A_01과 A_02는 제일 위험한 적을 같이 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0131
    role_based_enemy [22.2%(12%) / 2]
      multi_actor_same_target [50.0%(18%) / 1]
        role_based_target_clear [100.0%(8%) / 1]
          "A_01과 A_02는 적 후열을 같이 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0133
      multi_actor_different_targets [50.0%(7%) / 1]
        role_based_target_clear [100.0%(8%) / 1]
          "A_01은 적 전열을 묶고, A_02는 적 후열을 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0132
    pressure_source_enemy [11.1%(10%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        pressure_source_target_clear [100.0%(8%) / 1]
          "A_01과 A_02는 아군을 압박하는 적을 같이 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0134
    invalid_explicit_target [0.0%(6%) / 0]
  global_condition [7.3%(20%) / 3]
    explicit_enemy_target [33.3%(30%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "손이 비는 아군은 전부 E_01을 집중 공격해." @ 1 @ free_actor_selection @ accepted_20260514_002649.jsonl_seed_master_0003
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [33.3%(15%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "공격 가능한 아군은 체력이 제일 낮은 적을 같이 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0024
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [33.3%(10%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        pressure_source_target_clear [100.0%(8%) / 1]
          "손이 비는 아군은 압박받는 아군을 때리는 적을 같이 공격해." @ 1 @ free_actor_selection, pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0136
    invalid_explicit_target [0.0%(6%) / 0]
  global_role_based [7.3%(15%) / 3]
    explicit_enemy_target [33.3%(30%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "근접 아군은 E_01을 묶어." @ 1 @ actor_role_melee @ accepted_20260514_002740.jsonl_seed_master_0026
    nearest_enemy [33.3%(15%) / 1]
      move_then_attack [100.0%(25%) / 1]
        nearest_target_clear [100.0%(8%) / 1]
          "근접 아군은 가장 가까운 적에게 붙어서 공격해." @ 1 @ actor_role_melee @ accepted_20260514_002742.jsonl_seed_master_0137
    lowest_hp_enemy [0.0%(15%) / 0]
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [33.3%(12%) / 1]
      multi_actor_different_targets [100.0%(7%) / 1]
        role_based_target_clear [100.0%(8%) / 1]
          "원거리 아군은 적 후열을 먼저 공격해." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260514_002740.jsonl_seed_master_0025
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]
  global_state_based [7.3%(15%) / 3]
    explicit_enemy_target [0.0%(30%) / 0]
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [33.3%(15%) / 1]
      attack_only [100.0%(45%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "지금 공격 여유가 있는 아군은 체력이 제일 낮은 적을 공격해." @ 1 @ healthy_actor_selection @ accepted_20260514_002742.jsonl_seed_master_0138
    highest_threat_enemy [33.3%(12%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        highest_threat_target_clear [100.0%(7%) / 1]
          "체력이 여유 있는 아군은 제일 위험한 적을 압박해." @ 1 @ healthy_actor_selection @ accepted_20260514_002740.jsonl_seed_master_0027
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [33.3%(10%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        pressure_source_target_clear [100.0%(8%) / 1]
          "지원 가능한 아군은 아군을 압박하는 적을 같이 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0139
    invalid_explicit_target [0.0%(6%) / 0]

move [20.2%(22%) / 38]
  explicit_actor [57.9%(45%) / 22]
    explicit_ally_target [27.3%(22%) / 6]
      move_only [66.7%(55%) / 4]
        move_to_alive_ally [25.0%(10%) / 1]
          "A_02, A_04에게 이동해." @ 1 @ [] @ accepted_20260514_002649.jsonl_seed_master_0004
        move_to_dead_ally [25.0%(5%) / 1]
          "A_02, A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260514_002740.jsonl_seed_master_0028
        help_ally [25.0%(10%) / 1]
          "A_02, A_04 근처로 가." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0030
        move_to_self_attempt [25.0%(5%) / 1]
          "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002740.jsonl_seed_master_0029
      move_then_attack [16.7%(20%) / 1]
        help_ally [100.0%(10%) / 1]
          "A_02, A_04 근처로 가서 주변 적을 공격해." @ 1 @ help_ally_then_attack @ accepted_20260514_002740.jsonl_seed_master_0031
      empty_action_expected [16.7%(10%) / 1]
        move_to_self_attempt [100.0%(5%) / 1]
          "A_02, A_02에게 이동해." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0141
    explicit_enemy_target [13.6%(18%) / 3]
      move_only [33.3%(55%) / 1]
        approach_enemy_only [100.0%(10%) / 1]
          "A_01, E_02에게 접근해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0032
      move_then_attack [66.7%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          "A_01, E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0033
        flank_enemy_then_attack [50.0%(8%) / 1]
          "A_01, E_02 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260514_002740.jsonl_seed_master_0034
    safe_ally [13.6%(16%) / 3]
      move_only [66.7%(55%) / 2]
        retreat_to_backline_ally [50.0%(12%) / 1]
          "A_01, 아군 뒤쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0035
        low_hp_actor_escape [50.0%(10%) / 1]
          "A_01, 체력이 낮으니 안전한 아군 쪽으로 빠져." @ 1 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0142
      empty_action_expected [33.3%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          "A_01, 안전한 아군 쪽으로 빠져." @ 1 @ no_matching_actor, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0143
    low_hp_ally [9.1%(12%) / 2]
      move_only [50.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "A_01, 체력이 낮은 아군에게 붙어." @ 1 @ low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0036
      move_then_attack [50.0%(20%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "A_01, 체력이 낮은 아군에게 붙어서 주변 적을 공격해." @ 1 @ low_hp_ally_target, help_ally_then_attack @ accepted_20260514_002742.jsonl_seed_master_0144
    backline_ally [9.1%(10%) / 2]
      move_only [100.0%(55%) / 2]
        retreat_to_backline_ally [50.0%(12%) / 1]
          "A_01, 후열 아군 쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0145
        low_hp_actor_escape [50.0%(10%) / 1]
          "A_01, 체력이 낮으니까 후열 아군 쪽으로 빠져." @ 1 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0146
    role_based_enemy [13.6%(5%) / 3]
      move_only [33.3%(55%) / 1]
        approach_enemy_only [100.0%(10%) / 1]
          "A_01, 적 후열 쪽으로 이동해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0149
      move_then_attack [66.7%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          "A_01, 적 후열에 접근해서 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0148
        flank_enemy_then_attack [50.0%(8%) / 1]
          "A_01, 적 후열 쪽으로 돌아가서 공격해." @ 1 @ flank_requested, target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0147
    invalid_explicit_target [9.1%(7%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        move_to_dead_ally [50.0%(5%) / 1]
          "A_02, 쓰러진 A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260514_002742.jsonl_seed_master_0150
        move_to_self_attempt [50.0%(5%) / 1]
          "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0151
    none [4.5%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          "A_01, 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0037
  explicit_multi_actor [21.1%(10%) / 8]
    explicit_ally_target [12.5%(22%) / 1]
      move_only [100.0%(55%) / 1]
        help_ally [100.0%(10%) / 1]
          "A_01과 A_02는 A_04 근처로 이동해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0152
    explicit_enemy_target [25.0%(18%) / 2]
      move_then_attack [100.0%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          "A_01과 A_02는 E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0153
        flank_enemy_then_attack [50.0%(8%) / 1]
          "A_01과 A_02는 E_02 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260514_002742.jsonl_seed_master_0154
    safe_ally [25.0%(16%) / 2]
      move_only [50.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          "A_01, A_02는 뒤로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0038
      move_then_attack [50.0%(20%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          "A_01과 A_02는 뒤로 빠졌다가 가까운 적을 공격해." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0155
    low_hp_ally [12.5%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "A_01과 A_02는 체력이 낮은 아군에게 붙어." @ 1 @ low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0156
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [12.5%(7%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        move_to_self_attempt [100.0%(5%) / 1]
          "A_01과 A_02는 각자 자기 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0157
    none [12.5%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          "A_01과 A_02는 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260514_002742.jsonl_seed_master_0158
  global_condition [5.3%(15%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        low_hp_actor_escape [100.0%(10%) / 1]
          "체력이 낮은 아군은 전부 뒤로 빠져." @ 1 @ low_hp_actor_selection @ accepted_20260514_002740.jsonl_seed_master_0039
    low_hp_ally [50.0%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 1 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0159
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  global_role_based [5.3%(15%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          "전열 아군은 안전한 아군 쪽으로 빠져." @ 1 @ frontline_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0160
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [50.0%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          "전열 아군은 앞에서 버텨." @ 1 @ frontline_actor_selection, hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0040
  global_state_based [5.3%(10%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          "압박받는 아군은 안전한 아군 뒤쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0161
    low_hp_ally [50.0%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 1 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0041
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  no_valid_actor [5.3%(5%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260514_002740.jsonl_seed_master_0042
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [50.0%(10%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          "움직일 수 있는 아군은 전부 후퇴해." @ 1 @ no_matching_actor @ accepted_20260514_002742.jsonl_seed_master_0162

skill [30.9%(26%) / 58]
  explicit_actor [72.4%(55%) / 42]
    explicit_enemy_target [31.0%(26%) / 13]
      skill_only [92.3%(70%) / 12]
        enemy_skill_valid_target [33.3%(10%) / 4]
          "A_01, E_02에게 도약기로 붙어." @ 1 @ mobility_skill_enemy_approach @ accepted_20260514_002741.jsonl_seed_master_0112
          "A_03, E_02한테 공격 스킬 써." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0103
          "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0043
          "A_03, E_02한테 약화 스킬 써." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0106
        self_skill_enemy_target_conflict [8.3%(8%) / 1]
          "A_03, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260514_002740.jsonl_seed_master_0044
        ally_skill_enemy_target_conflict [25.0%(8%) / 3]
          "A_04, E_02한테 보호 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0096
          "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002740.jsonl_seed_master_0045
          "A_04, E_02한테 회복 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0099
        dead_target_forbidden [16.7%(6%) / 2]
          "A_03, 죽은 E_02한테 공격 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002740.jsonl_seed_master_0047
          "A_03, 죽은 E_02한테 약화 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0108
        aoe_skill_center_selection [8.3%(8%) / 1]
          "A_05, E_03 주변에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0164
        actor_has_no_skill [8.3%(8%) / 1]
          "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002740.jsonl_seed_master_0046
      move_then_skill [7.7%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0048
    explicit_ally_target [31.0%(22%) / 13]
      skill_only [100.0%(70%) / 13]
        ally_skill_valid_target [23.1%(10%) / 3]
          "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0049, accepted_20260514_002741.jsonl_seed_master_0095
          "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002741.jsonl_seed_master_0098
        self_skill_enemy_target_conflict [7.7%(8%) / 1]
          "A_03, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260514_002741.jsonl_seed_master_0094
        enemy_skill_ally_target_conflict [30.8%(8%) / 4]
          "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002740.jsonl_seed_master_0050
          "A_03, A_02한테 공격 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0104
          "A_03, A_02한테 약화 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0107
          "A_06, A_02 주변에 광역 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0110
        resurrection_dead_ally_valid [15.4%(8%) / 2]
          "A_04, 쓰러진 A_02한테 스킬 써." @ 2 @ dead_ally_skill_target_allowed @ accepted_20260514_002741.jsonl_seed_master_0051, accepted_20260514_002741.jsonl_seed_master_0101
        resurrection_living_ally_conflict [7.7%(6%) / 1]
          "A_04, 살아있는 A_02한테 부활 스킬 써." @ 1 @ text_living_target_but_resurrection_skill @ accepted_20260514_002741.jsonl_seed_master_0052
        dead_target_forbidden [15.4%(6%) / 2]
          "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0053
          "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0100
    lowest_hp_enemy [4.8%(8%) / 2]
      skill_only [100.0%(70%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          "A_03, 체력이 제일 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0165
        aoe_skill_center_selection [50.0%(8%) / 1]
          "A_06, 체력이 제일 낮은 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0166
    nearest_enemy [7.1%(5%) / 3]
      skill_only [66.7%(70%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          "A_03, 가장 가까운 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0168
        aoe_skill_center_selection [50.0%(8%) / 1]
          "A_06, 가장 가까운 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0169
      move_then_skill [33.3%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          "A_03, 가장 가까운 적에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0167
    role_based_enemy [9.5%(8%) / 4]
      skill_only [75.0%(70%) / 3]
        enemy_skill_valid_target [33.3%(10%) / 1]
          "A_03, 적 후열에게 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0171
        aoe_skill_center_selection [66.7%(8%) / 2]
          "A_06, 적 후열이 뭉친 곳에 스킬 써." @ 1 @ target_role_backline_enemy, aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0170
          "A_06, 적들이 뭉친 쪽에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002649.jsonl_seed_master_0008
      move_then_skill [25.0%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          "A_03, 적 후열에게 접근해서 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0172
    low_hp_ally [2.4%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "A_04, 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0173
    invalid_explicit_target [4.8%(13%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        dead_target_forbidden [50.0%(6%) / 1]
          "A_03, 죽은 E_02한테 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002743.jsonl_seed_master_0174
        no_valid_skill_target [50.0%(4%) / 1]
          "A_03, 죽은 E_02한테 스킬 써." @ 1 @ named_target_dead, no_valid_skill_target @ accepted_20260514_002743.jsonl_seed_master_0175
    none [9.5%(8%) / 4]
      skill_only [75.0%(70%) / 3]
        self_skill_no_target [33.3%(8%) / 1]
          "A_01, 도약기로 빠져." @ 1 @ mobility_skill_self_escape @ accepted_20260514_002741.jsonl_seed_master_0111
        aoe_skill_center_selection [66.7%(8%) / 2]
          "A_06, 적들이 뭉친 쪽에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260514_002741.jsonl_seed_master_0055, accepted_20260514_002741.jsonl_seed_master_0109
      empty_action_expected [25.0%(10%) / 1]
        actor_has_no_skill [100.0%(8%) / 1]
          "A_03, 지금 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0176
  explicit_multi_actor [13.8%(10%) / 8]
    explicit_enemy_target [37.5%(26%) / 3]
      multi_actor_same_target [66.7%(7%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          "A_03과 A_06은 E_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0177
        aoe_skill_center_selection [50.0%(8%) / 1]
          "A_03과 A_06은 E_02 주변에 스킬을 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0178
      multi_actor_different_targets [33.3%(3%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "A_03은 E_01에게, A_06은 E_03에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0179
    explicit_ally_target [25.0%(22%) / 2]
      multi_actor_same_target [50.0%(7%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "A_04와 A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0180
      multi_actor_different_targets [50.0%(3%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "A_04는 A_01에게, A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0181
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [12.5%(8%) / 1]
      multi_actor_different_targets [100.0%(3%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "A_03은 적 전열에, A_06은 적 후열에 스킬을 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0182
    low_hp_ally [12.5%(10%) / 1]
      multi_actor_same_target [100.0%(7%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "A_04와 A_05는 체력이 제일 낮은 아군에게 스킬을 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0183
    invalid_explicit_target [0.0%(13%) / 0]
    none [12.5%(8%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          "A_03과 A_04는 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002743.jsonl_seed_master_0184
  global_condition [3.4%(10%) / 2]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [50.0%(8%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "스킬 쓸 수 있는 아군은 체력 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0185
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [50.0%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "회복 가능한 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0186
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_role_based [1.7%(10%) / 1]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [100.0%(8%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260514_002741.jsonl_seed_master_0058
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_state_based [3.4%(10%) / 2]
    explicit_enemy_target [50.0%(26%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "스킬을 쓰기 안전한 아군은 E_02에게 스킬 써." @ 1 @ healthy_actor_selection @ accepted_20260514_002743.jsonl_seed_master_0187
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [50.0%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002741.jsonl_seed_master_0059
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  no_valid_actor [5.2%(5%) / 3]
    explicit_enemy_target [33.3%(26%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002741.jsonl_seed_master_0060
    explicit_ally_target [33.3%(22%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_target [100.0%(4%) / 1]
          "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ no_valid_skill_target @ accepted_20260514_002741.jsonl_seed_master_0061
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [33.3%(8%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          "스킬 가능한 아군은 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002743.jsonl_seed_master_0188

skillControl [6.9%(8%) / 13]
  explicit_actor [46.2%(70%) / 6]
    none [100.0%(100%) / 6]
      skillControl_defer [33.3%(55%) / 2]
        explicit_defer_skill [50.0%(25%) / 1]
          "A_03, 스킬은 아직 쓰지 말고 5초 후로 미뤄." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0062
        defer_without_duration [50.0%(15%) / 1]
          "A_03, 스킬은 좀 아껴." @ 1 @ skillControl_duration_unspecified @ accepted_20260514_002741.jsonl_seed_master_0063
      skillControl_forbid [50.0%(35%) / 3]
        explicit_forbid_skill [33.3%(25%) / 1]
          "A_03, 지금은 스킬 쓰지 마." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0064
        forbid_without_duration [33.3%(10%) / 1]
          "A_03, 스킬 쓰지 말고 있어." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0065
        actor_has_no_skill [33.3%(5%) / 1]
          "A_03, 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002741.jsonl_seed_master_0066
      empty_action_expected [16.7%(10%) / 1]
        selected_actor_dead [100.0%(5%) / 1]
          "A_03, 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0189
  explicit_multi_actor [30.8%(20%) / 4]
    none [100.0%(100%) / 4]
      skillControl_defer [25.0%(55%) / 1]
        multi_actor_defer_skill [100.0%(10%) / 1]
          "A_03과 A_04는 스킬을 아껴." @ 1 @ multi_actor_skillControl @ accepted_20260514_002741.jsonl_seed_master_0067
      skillControl_forbid [25.0%(35%) / 1]
        multi_actor_forbid_skill [100.0%(5%) / 1]
          "A_03과 A_04는 지금 스킬 쓰지 마." @ 1 @ multi_actor_skillControl @ accepted_20260514_002741.jsonl_seed_master_0068
      empty_action_expected [50.0%(10%) / 2]
        actor_has_no_skill [50.0%(5%) / 1]
          "A_03과 A_04는 지금 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0191
        selected_actor_dead [50.0%(5%) / 1]
          "A_03과 A_04는 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0190
  no_valid_actor [23.1%(10%) / 3]
    none [100.0%(100%) / 3]
      empty_action_expected [100.0%(10%) / 3]
        actor_has_no_skill [33.3%(5%) / 1]
          "스킬이 없는 A_03은 지금 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0193
        selected_actor_dead [66.7%(5%) / 2]
          "A_03, 스킬 쓰지 마." @ 1 @ named_actor_dead @ accepted_20260514_002741.jsonl_seed_master_0069
          "A_03, 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0192

wait [8.0%(8%) / 15]
  explicit_actor [60.0%(60%) / 9]
    explicit_enemy_target [33.3%(10%) / 3]
      wait_only [33.3%(65%) / 1]
        explicit_wait [100.0%(25%) / 1]
          "A_04, E_02를 보면서 잠깐 대기해." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0196
      wait_then_attack [66.7%(20%) / 2]
        wait_then_attack_valid [100.0%(15%) / 2]
          "A_04, 3초 뒤에 E_02를 공격해." @ 2 @ explicit_wait_duration, wait_then_attack @ accepted_20260514_002743.jsonl_seed_master_0194, accepted_20260514_002743.jsonl_seed_master_0195
    none [66.7%(90%) / 6]
      wait_only [50.0%(65%) / 3]
        explicit_wait [33.3%(25%) / 1]
          "A_04, 지금 자리에서 대기해." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0070
        explicit_wait_duration [33.3%(20%) / 1]
          "A_04, 5초만 기다려." @ 1 @ explicit_wait_duration @ accepted_20260514_002741.jsonl_seed_master_0071
        hold_position_wait [33.3%(10%) / 1]
          "A_04, 위치 유지하면서 잠깐 버텨." @ 1 @ hold_front_requested @ accepted_20260514_002741.jsonl_seed_master_0072
      wait_then_attack [16.7%(20%) / 1]
        wait_then_attack_valid [100.0%(15%) / 1]
          "A_04, 3초 기다렸다가 E_02를 공격해." @ 1 @ wait_then_attack @ accepted_20260514_002741.jsonl_seed_master_0073
      wait_then_skill [16.7%(10%) / 1]
        wait_then_skill_valid [100.0%(10%) / 1]
          "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260514_002741.jsonl_seed_master_0074
      empty_action_expected [16.7%(5%) / 1]
        selected_actor_dead [100.0%(6%) / 1]
          "A_04, 지금 자리에서 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0198
  explicit_multi_actor [20.0%(15%) / 3]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 3]
      wait_only [33.3%(65%) / 1]
        multi_actor_wait [100.0%(8%) / 1]
          "A_03과 A_04는 잠깐 대기해." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0199
      wait_then_attack [33.3%(20%) / 1]
        wait_then_attack_valid [100.0%(15%) / 1]
          "A_03과 A_04는 잠깐 기다렸다가 공격해." @ 1 @ wait_then_attack @ accepted_20260514_002743.jsonl_seed_master_0200
      empty_action_expected [33.3%(5%) / 1]
        selected_actor_dead [100.0%(6%) / 1]
          "A_03과 A_04는 잠깐 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0202
  global_condition [6.7%(15%) / 1]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 1]
      wait_only [100.0%(65%) / 1]
        hold_position_wait [100.0%(10%) / 1]
          "위험한 아군은 잠깐 대기하면서 버텨." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0203
  no_valid_actor [13.3%(10%) / 2]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 2]
      empty_action_expected [100.0%(5%) / 2]
        no_matching_wait_actor [50.0%(6%) / 1]
          "체력이 낮은 아군은 잠깐 대기해." @ 1 @ no_matching_actor @ accepted_20260514_002741.jsonl_seed_master_0077
        selected_actor_dead [50.0%(6%) / 1]
          "A_04, 지금 자리에서 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002741.jsonl_seed_master_0078

empty [12.2%(12%) / 23]
  explicit_actor [43.5%(30%) / 10]
    explicit_enemy_target [50.0%(20%) / 5]
      empty_action_expected [100.0%(100%) / 5]
        named_actor_dead [20.0%(12%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0205
        named_target_dead [20.0%(10%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260514_002741.jsonl_seed_master_0081
        named_target_untargetable [20.0%(10%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260514_002741.jsonl_seed_master_0082
        actor_outside_allowedActors [20.0%(8%) / 1]
          "A_01, E_02를 공격해." @ 1 @ actor_outside_allowedActors @ accepted_20260514_002741.jsonl_seed_master_0080
        attack_target_outside_allowedTargets [20.0%(8%) / 1]
          "A_01, E_02를 공격해." @ 1 @ attack_target_outside_allowedTargets @ accepted_20260514_002741.jsonl_seed_master_0083
    explicit_ally_target [10.0%(15%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_target_dead_not_allowed [100.0%(8%) / 1]
          "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0084
    invalid_explicit_target [20.0%(30%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        move_to_self_attempt [50.0%(6%) / 1]
          "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002741.jsonl_seed_master_0085
        skill_actor_has_no_skill [50.0%(8%) / 1]
          "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002741.jsonl_seed_master_0086
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [20.0%(20%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        named_actor_dead [50.0%(12%) / 1]
          "A_01, 지금 공격할 수 있는 적을 찾아 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0206
        no_valid_target [50.0%(8%) / 1]
          "A_01, 지금 공격할 수 있는 적을 공격해." @ 1 @ no_valid_target @ accepted_20260514_002745.jsonl_seed_master_0207
  explicit_multi_actor [21.7%(10%) / 5]
    explicit_enemy_target [80.0%(20%) / 4]
      empty_action_expected [100.0%(100%) / 4]
        all_named_actors_dead [25.0%(6%) / 1]
          "A_01과 A_02는 E_02를 공격해." @ 1 @ all_named_actors_dead @ accepted_20260514_002741.jsonl_seed_master_0087
        named_target_dead [25.0%(10%) / 1]
          "A_01과 A_02는 E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260514_002745.jsonl_seed_master_0209
        named_target_untargetable [25.0%(10%) / 1]
          "A_01과 A_02는 E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260514_002745.jsonl_seed_master_0210
        attack_target_outside_allowedTargets [25.0%(8%) / 1]
          "A_01과 A_02는 E_02를 공격해." @ 1 @ attack_target_outside_allowedTargets @ accepted_20260514_002745.jsonl_seed_master_0208
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [20.0%(30%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_actor_has_no_skill [100.0%(8%) / 1]
          "A_03과 A_04는 죽은 E_02한테 스킬 써." @ 1 @ actor_has_no_skill, named_target_dead @ accepted_20260514_002745.jsonl_seed_master_0211
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [0.0%(20%) / 0]
  global_condition [8.7%(25%) / 2]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          "체력이 낮은 아군을 도울 수 있는 아군은 붙어." @ 1 @ no_matching_actor, low_hp_ally_target @ accepted_20260514_002745.jsonl_seed_master_0212
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260514_002741.jsonl_seed_master_0088
  global_role_based [8.7%(15%) / 2]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_role_actor [100.0%(6%) / 1]
          "원거리 아군은 적 후열을 공격해." @ 1 @ no_matching_role_actor @ accepted_20260514_002741.jsonl_seed_master_0089
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_role_actor [100.0%(6%) / 1]
          "전열 아군은 앞으로 버텨." @ 1 @ no_matching_role_actor @ accepted_20260514_002745.jsonl_seed_master_0213
  global_state_based [8.7%(10%) / 2]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_valid_target [100.0%(8%) / 1]
          "공격 가능한 아군은 적 후열을 공격해." @ 1 @ no_valid_target, target_role_backline_enemy @ accepted_20260514_002745.jsonl_seed_master_0214
    lowest_hp_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_valid_target [100.0%(8%) / 1]
          "공격 가능한 아군은 체력이 제일 낮은 적을 공격해." @ 1 @ no_valid_target @ accepted_20260514_002741.jsonl_seed_master_0090
    none [0.0%(20%) / 0]
  no_valid_actor [8.7%(10%) / 2]
    explicit_enemy_target [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        named_actor_dead [100.0%(12%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0215
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          "살아있는 아군은 전부 후퇴해." @ 1 @ no_valid_actor @ accepted_20260514_002741.jsonl_seed_master_0091
