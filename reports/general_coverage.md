# General Coverage

attack [17.8%(24%) / 19]
  explicit_actor [63.2%(35%) / 12]
    explicit_enemy_target [33.3%(30%) / 4]
      attack_only [75.0%(45%) / 3]
        simple_clear_target [33.3%(18%) / 1]
          "A_01, E_02를 공격해." @ 1 @ [] @ accepted_20260512_005252.jsonl_seed_master_0001
        dead_named_target [33.3%(6%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260512_023750.jsonl_seed_master_0011
        untargetable_named_target [33.3%(5%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260512_023750.jsonl_seed_master_0012
      move_then_attack [25.0%(25%) / 1]
        flank_attack_requested [100.0%(6%) / 1]
          "A_01, E_02의 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260512_023750.jsonl_seed_master_0014
    nearest_enemy [16.7%(15%) / 2]
      attack_only [50.0%(45%) / 1]
        nearest_target_clear [100.0%(8%) / 1]
          "A_02, 가장 가까운 적을 공격해." @ 1 @ [] @ accepted_20260512_005252.jsonl_seed_master_0002
      move_then_attack [50.0%(25%) / 1]
        nearest_target_clear [100.0%(8%) / 1]
          "A_02, 제일 가까운 적한테 붙어서 공격해." @ 1 @ [] @ accepted_20260512_023750.jsonl_seed_master_0015
    lowest_hp_enemy [8.3%(15%) / 1]
      attack_only [100.0%(45%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "A_03, 체력이 제일 낮은 적을 노려." @ 1 @ [] @ accepted_20260512_023750.jsonl_seed_master_0016
    highest_threat_enemy [8.3%(12%) / 1]
      attack_only [100.0%(45%) / 1]
        highest_threat_target_clear [100.0%(7%) / 1]
          "A_01, 제일 위험한 적부터 공격해." @ 1 @ [] @ accepted_20260512_023750.jsonl_seed_master_0017
    role_based_enemy [16.7%(12%) / 2]
      attack_only [100.0%(45%) / 2]
        role_based_target_clear [100.0%(8%) / 2]
          "A_02, 적 원거리 유닛을 먼저 끊어." @ 1 @ target_role_ranged_enemy @ accepted_20260512_023750.jsonl_seed_master_0018
          "A_02, 후방에 있는 적부터 노려." @ 1 @ target_role_backline_enemy @ accepted_20260512_023750.jsonl_seed_master_0019
    pressure_source_enemy [16.7%(10%) / 2]
      attack_only [100.0%(45%) / 2]
        pressure_source_target_clear [100.0%(8%) / 2]
          "A_03, A_02를 때리는 적을 떼어내." @ 2 @ pressure_source_target_clear @ accepted_20260512_023750.jsonl_seed_master_0020, accepted_20260512_025139.jsonl_seed_master_0021
    invalid_explicit_target [0.0%(6%) / 0]
  explicit_multi_actor [10.5%(15%) / 2]
    explicit_enemy_target [100.0%(30%) / 2]
      multi_actor_same_target [50.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "A_01과 A_02는 E_01을 같이 공격해." @ 1 @ [] @ accepted_20260512_025139.jsonl_seed_master_0022
      multi_actor_different_targets [50.0%(7%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "A_01은 E_01을, A_02는 E_03을 공격해." @ 1 @ [] @ accepted_20260512_025139.jsonl_seed_master_0023
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [0.0%(15%) / 0]
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]
  global_condition [10.5%(20%) / 2]
    explicit_enemy_target [50.0%(30%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "손이 비는 아군은 전부 E_01을 집중 공격해." @ 1 @ free_actor_selection @ accepted_20260512_005252.jsonl_seed_master_0003
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [50.0%(15%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        lowest_hp_target_clear [100.0%(8%) / 1]
          "공격 가능한 아군은 체력이 제일 낮은 적을 같이 공격해." @ 1 @ [] @ accepted_20260512_025139.jsonl_seed_master_0024
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]
  global_role_based [10.5%(15%) / 2]
    explicit_enemy_target [50.0%(30%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        focus_fire_clear [100.0%(8%) / 1]
          "근접 아군은 E_01을 묶어." @ 1 @ actor_role_melee @ accepted_20260512_025139.jsonl_seed_master_0026
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [0.0%(15%) / 0]
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [50.0%(12%) / 1]
      multi_actor_different_targets [100.0%(7%) / 1]
        role_based_target_clear [100.0%(8%) / 1]
          "원거리 아군은 적 후열을 먼저 공격해." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260512_025139.jsonl_seed_master_0025
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]
  global_state_based [5.3%(15%) / 1]
    explicit_enemy_target [0.0%(30%) / 0]
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [0.0%(15%) / 0]
    highest_threat_enemy [100.0%(12%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        highest_threat_target_clear [100.0%(7%) / 1]
          "체력이 여유 있는 아군은 제일 위험한 적을 압박해." @ 1 @ healthy_actor_selection @ accepted_20260512_025139.jsonl_seed_master_0027
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]

move [15.9%(22%) / 17]
  explicit_actor [64.7%(45%) / 11]
    explicit_ally_target [45.5%(22%) / 5]
      move_only [80.0%(55%) / 4]
        move_to_alive_ally [25.0%(10%) / 1]
          "A_02, A_04에게 이동해." @ 1 @ [] @ accepted_20260512_005252.jsonl_seed_master_0004
        move_to_dead_ally [25.0%(5%) / 1]
          "A_02, A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260512_025139.jsonl_seed_master_0028
        help_ally [25.0%(10%) / 1]
          "A_02, A_04 근처로 가." @ 1 @ [] @ accepted_20260512_025139.jsonl_seed_master_0030
        move_to_self_attempt [25.0%(5%) / 1]
          "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260512_025139.jsonl_seed_master_0029
      move_then_attack [20.0%(20%) / 1]
        help_ally [100.0%(10%) / 1]
          "A_02, A_04 근처로 가서 주변 적을 공격해." @ 1 @ help_ally_then_attack @ accepted_20260512_025611.jsonl_seed_master_0031
    explicit_enemy_target [27.3%(18%) / 3]
      move_only [33.3%(55%) / 1]
        approach_enemy_only [100.0%(10%) / 1]
          "A_01, E_02에게 접근해." @ 1 @ [] @ accepted_20260512_025611.jsonl_seed_master_0032
      move_then_attack [66.7%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          "A_01, E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260512_025611.jsonl_seed_master_0033
        flank_enemy_then_attack [50.0%(8%) / 1]
          "A_01, E_02 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260512_025611.jsonl_seed_master_0034
    safe_ally [9.1%(16%) / 1]
      move_only [100.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          "A_01, 아군 뒤쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260512_025611.jsonl_seed_master_0035
    low_hp_ally [9.1%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "A_01, 체력이 낮은 아군에게 붙어." @ 1 @ low_hp_ally_target @ accepted_20260512_025611.jsonl_seed_master_0036
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [9.1%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          "A_01, 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260512_025611.jsonl_seed_master_0037
  explicit_multi_actor [11.8%(10%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [100.0%(16%) / 2]
      move_only [100.0%(55%) / 2]
        retreat_to_backline_ally [100.0%(12%) / 2]
          "A_01, A_02는 뒤로 빠져." @ 2 @ retreat_to_safe_ally @ accepted_20260512_005252.jsonl_seed_master_0005, accepted_20260512_025611.jsonl_seed_master_0038
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  global_condition [5.9%(15%) / 1]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [100.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        low_hp_actor_escape [100.0%(10%) / 1]
          "체력이 낮은 아군은 전부 뒤로 빠져." @ 1 @ low_hp_actor_selection @ accepted_20260512_025611.jsonl_seed_master_0039
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  global_role_based [5.9%(15%) / 1]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [0.0%(16%) / 0]
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [100.0%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          "전열 아군은 앞에서 버텨." @ 1 @ frontline_actor_selection, hold_front_requested @ accepted_20260512_025611.jsonl_seed_master_0040
  global_state_based [5.9%(10%) / 1]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [0.0%(16%) / 0]
    low_hp_ally [100.0%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 1 @ free_actor_selection, low_hp_ally_target @ accepted_20260512_031947.jsonl_seed_master_0041
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  no_valid_actor [5.9%(5%) / 1]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [100.0%(16%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260512_031947.jsonl_seed_master_0042
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]

skill [39.3%(26%) / 42]
  explicit_actor [90.5%(55%) / 38]
    explicit_enemy_target [39.5%(26%) / 15]
      skill_only [93.3%(70%) / 14]
        enemy_skill_valid_target [28.6%(10%) / 4]
          "A_01, E_02에게 도약기로 붙어." @ 1 @ mobility_skill_enemy_approach @ accepted_20260512_035448.jsonl_seed_master_0112
          "A_03, E_02한테 공격 스킬 써." @ 1 @ [] @ accepted_20260512_035448.jsonl_seed_master_0103
          "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0043
          "A_03, E_02한테 약화 스킬 써." @ 1 @ [] @ accepted_20260512_035448.jsonl_seed_master_0106
        self_skill_enemy_target_conflict [14.3%(8%) / 2]
          "A_03, E_02한테 스킬 써." @ 2 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260512_031947.jsonl_seed_master_0044, accepted_20260512_035444.jsonl_seed_master_0093
        ally_skill_enemy_target_conflict [21.4%(8%) / 3]
          "A_04, E_02한테 보호 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_035444.jsonl_seed_master_0096
          "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_031947.jsonl_seed_master_0045
          "A_04, E_02한테 회복 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260512_035444.jsonl_seed_master_0099
        dead_target_forbidden [21.4%(6%) / 3]
          "A_03, 죽은 E_02한테 공격 스킬 써." @ 2 @ skill_target_dead_not_allowed @ accepted_20260512_031947.jsonl_seed_master_0047, accepted_20260512_035448.jsonl_seed_master_0105
          "A_03, 죽은 E_02한테 약화 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035448.jsonl_seed_master_0108
        actor_has_no_skill [14.3%(8%) / 2]
          "A_03, E_02한테 스킬 써." @ 2 @ actor_has_no_skill @ accepted_20260512_031947.jsonl_seed_master_0046, accepted_20260512_035448.jsonl_seed_master_0113
      move_then_skill [6.7%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260512_031947.jsonl_seed_master_0048
    explicit_ally_target [42.1%(22%) / 16]
      skill_only [100.0%(70%) / 16]
        ally_skill_valid_target [25.0%(10%) / 4]
          "A_04, A_02한테 보호 스킬 써." @ 1 @ [] @ accepted_20260512_035444.jsonl_seed_master_0095
          "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260512_005252.jsonl_seed_master_0007, accepted_20260512_031947.jsonl_seed_master_0049
          "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260512_035444.jsonl_seed_master_0098
        self_skill_enemy_target_conflict [6.2%(8%) / 1]
          "A_03, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260512_035444.jsonl_seed_master_0094
        enemy_skill_ally_target_conflict [25.0%(8%) / 4]
          "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_031947.jsonl_seed_master_0050
          "A_03, A_02한테 공격 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0104
          "A_03, A_02한테 약화 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0107
          "A_06, A_02 주변에 광역 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260512_035448.jsonl_seed_master_0110
        resurrection_dead_ally_valid [12.5%(8%) / 2]
          "A_04, 쓰러진 A_02한테 부활 스킬 써." @ 1 @ dead_ally_skill_target_allowed @ accepted_20260512_035448.jsonl_seed_master_0101
          "A_04, 쓰러진 A_02한테 스킬 써." @ 1 @ dead_ally_skill_target_allowed @ accepted_20260512_032346.jsonl_seed_master_0051
        resurrection_living_ally_conflict [12.5%(6%) / 2]
          "A_04, 살아있는 A_02한테 부활 스킬 써." @ 2 @ text_living_target_but_resurrection_skill @ accepted_20260512_032346.jsonl_seed_master_0052, accepted_20260512_035448.jsonl_seed_master_0102
        dead_target_forbidden [18.8%(6%) / 3]
          "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 2 @ skill_target_dead_not_allowed @ accepted_20260512_032346.jsonl_seed_master_0053, accepted_20260512_035444.jsonl_seed_master_0097
          "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035444.jsonl_seed_master_0100
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [2.6%(8%) / 1]
      skill_only [100.0%(70%) / 1]
        aoe_skill_center_selection [100.0%(8%) / 1]
          "A_06, 적들이 뭉친 쪽에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260512_005252.jsonl_seed_master_0008
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [15.8%(8%) / 6]
      skill_only [100.0%(70%) / 6]
        self_skill_no_target [66.7%(8%) / 4]
          "A_01, 도약기로 빠져." @ 1 @ mobility_skill_self_escape @ accepted_20260512_035448.jsonl_seed_master_0111
          "A_03, 지금 스킬 써." @ 3 @ self_skill_without_explicit_target @ accepted_20260512_005252.jsonl_seed_master_0006, accepted_20260512_032346.jsonl_seed_master_0054, accepted_20260512_035444.jsonl_seed_master_0092
        aoe_skill_center_selection [33.3%(8%) / 2]
          "A_06, 적들이 뭉친 쪽에 광역 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260512_035448.jsonl_seed_master_0109
          "A_06, 적들이 뭉친 쪽에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260512_032346.jsonl_seed_master_0055
  explicit_multi_actor [0.0%(10%) / 0]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_condition [0.0%(10%) / 0]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_role_based [2.4%(10%) / 1]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [100.0%(8%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260512_032346.jsonl_seed_master_0058
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_state_based [2.4%(10%) / 1]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [100.0%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260512_032346.jsonl_seed_master_0059
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  no_valid_actor [4.8%(5%) / 2]
    explicit_enemy_target [50.0%(26%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260512_032346.jsonl_seed_master_0060
    explicit_ally_target [50.0%(22%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_target [100.0%(4%) / 1]
          "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ no_valid_skill_target @ accepted_20260512_035433.jsonl_seed_master_0061
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]

skillControl [8.4%(8%) / 9]
  explicit_actor [66.7%(70%) / 6]
    none [100.0%(100%) / 6]
      skillControl_defer [50.0%(55%) / 3]
        explicit_defer_skill [66.7%(25%) / 2]
          "A_03, 스킬은 아직 쓰지 말고 5초 후로 미뤄." @ 2 @ [] @ accepted_20260512_005252.jsonl_seed_master_0009, accepted_20260512_035433.jsonl_seed_master_0062
        defer_without_duration [33.3%(15%) / 1]
          "A_03, 스킬은 좀 아껴." @ 1 @ skillControl_duration_unspecified @ accepted_20260512_035433.jsonl_seed_master_0063
      skillControl_forbid [50.0%(35%) / 3]
        explicit_forbid_skill [33.3%(25%) / 1]
          "A_03, 지금은 스킬 쓰지 마." @ 1 @ [] @ accepted_20260512_035433.jsonl_seed_master_0064
        forbid_without_duration [33.3%(10%) / 1]
          "A_03, 스킬 쓰지 말고 있어." @ 1 @ [] @ accepted_20260512_035433.jsonl_seed_master_0065
        actor_has_no_skill [33.3%(5%) / 1]
          "A_03, 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260512_035433.jsonl_seed_master_0066
  explicit_multi_actor [22.2%(20%) / 2]
    none [100.0%(100%) / 2]
      skillControl_defer [50.0%(55%) / 1]
        multi_actor_defer_skill [100.0%(10%) / 1]
          "A_03과 A_04는 스킬을 아껴." @ 1 @ multi_actor_skillControl @ accepted_20260512_035433.jsonl_seed_master_0067
      skillControl_forbid [50.0%(35%) / 1]
        multi_actor_forbid_skill [100.0%(5%) / 1]
          "A_03과 A_04는 지금 스킬 쓰지 마." @ 1 @ multi_actor_skillControl @ accepted_20260512_035433.jsonl_seed_master_0068
  no_valid_actor [11.1%(10%) / 1]
    none [100.0%(100%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        selected_actor_dead [100.0%(5%) / 1]
          "A_03, 스킬 쓰지 마." @ 1 @ named_actor_dead @ accepted_20260512_035433.jsonl_seed_master_0069

wait [7.5%(8%) / 8]
  explicit_actor [75.0%(60%) / 6]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 6]
      wait_only [66.7%(65%) / 4]
        explicit_wait [25.0%(25%) / 1]
          "A_04, 지금 자리에서 대기해." @ 1 @ [] @ accepted_20260512_035433.jsonl_seed_master_0070
        explicit_wait_duration [50.0%(20%) / 2]
          "A_04, 5초만 기다려." @ 2 @ explicit_wait_duration @ accepted_20260512_005252.jsonl_seed_master_0010, accepted_20260512_035437.jsonl_seed_master_0071
        hold_position_wait [25.0%(10%) / 1]
          "A_04, 위치 유지하면서 잠깐 버텨." @ 1 @ hold_front_requested @ accepted_20260512_035437.jsonl_seed_master_0072
      wait_then_attack [16.7%(20%) / 1]
        wait_then_attack_valid [100.0%(15%) / 1]
          "A_04, 3초 기다렸다가 E_02를 공격해." @ 1 @ wait_then_attack @ accepted_20260512_035437.jsonl_seed_master_0073
      wait_then_skill [16.7%(10%) / 1]
        wait_then_skill_valid [100.0%(10%) / 1]
          "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260512_035437.jsonl_seed_master_0074
  explicit_multi_actor [0.0%(15%) / 0]
    explicit_enemy_target [0.0%(10%) / 0]
    none [0.0%(90%) / 0]
  global_condition [0.0%(15%) / 0]
    explicit_enemy_target [0.0%(10%) / 0]
    none [0.0%(90%) / 0]
  no_valid_actor [25.0%(10%) / 2]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 2]
      empty_action_expected [100.0%(5%) / 2]
        no_matching_wait_actor [50.0%(6%) / 1]
          "체력이 낮은 아군은 잠깐 대기해." @ 1 @ no_matching_actor @ accepted_20260512_035437.jsonl_seed_master_0077
        selected_actor_dead [50.0%(6%) / 1]
          "A_04, 지금 자리에서 대기해." @ 1 @ named_actor_dead @ accepted_20260512_035437.jsonl_seed_master_0078

empty [11.2%(12%) / 12]
  explicit_actor [58.3%(30%) / 7]
    explicit_enemy_target [57.1%(20%) / 4]
      empty_action_expected [100.0%(100%) / 4]
        named_target_dead [25.0%(10%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260512_035440.jsonl_seed_master_0081
        named_target_untargetable [25.0%(10%) / 1]
          "A_01, E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260512_035440.jsonl_seed_master_0082
        actor_outside_allowedActors [25.0%(8%) / 1]
          "A_01, E_02를 공격해." @ 1 @ actor_outside_allowedActors @ accepted_20260512_035437.jsonl_seed_master_0080
        attack_target_outside_allowedTargets [25.0%(8%) / 1]
          "A_01, E_02를 공격해." @ 1 @ attack_target_outside_allowedTargets @ accepted_20260512_035440.jsonl_seed_master_0083
    explicit_ally_target [14.3%(15%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_target_dead_not_allowed [100.0%(8%) / 1]
          "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260512_035440.jsonl_seed_master_0084
    invalid_explicit_target [28.6%(30%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        move_to_self_attempt [50.0%(6%) / 1]
          "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260512_035440.jsonl_seed_master_0085
        skill_actor_has_no_skill [50.0%(8%) / 1]
          "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260512_035440.jsonl_seed_master_0086
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [0.0%(20%) / 0]
  explicit_multi_actor [8.3%(10%) / 1]
    explicit_enemy_target [100.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        all_named_actors_dead [100.0%(6%) / 1]
          "A_01과 A_02는 E_02를 공격해." @ 1 @ all_named_actors_dead @ accepted_20260512_035440.jsonl_seed_master_0087
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [0.0%(20%) / 0]
  global_condition [8.3%(25%) / 1]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [100.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260512_035440.jsonl_seed_master_0088
  global_role_based [8.3%(15%) / 1]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [100.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_role_actor [100.0%(6%) / 1]
          "원거리 아군은 적 후열을 공격해." @ 1 @ no_matching_role_actor @ accepted_20260512_035440.jsonl_seed_master_0089
    lowest_hp_enemy [0.0%(5%) / 0]
    none [0.0%(20%) / 0]
  global_state_based [8.3%(10%) / 1]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [100.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_valid_target [100.0%(8%) / 1]
          "공격 가능한 아군은 체력이 제일 낮은 적을 공격해." @ 1 @ no_valid_target @ accepted_20260512_035440.jsonl_seed_master_0090
    none [0.0%(20%) / 0]
  no_valid_actor [8.3%(10%) / 1]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [100.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          "살아있는 아군은 전부 후퇴해." @ 1 @ no_valid_actor @ accepted_20260512_035444.jsonl_seed_master_0091
