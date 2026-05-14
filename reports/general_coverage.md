# General Coverage

attack [66.8%(24%) / 408]
  explicit_actor [51.5%(35%) / 210]
    explicit_enemy_target [39.5%(30%) / 83]
      attack_only [49.4%(45%) / 41]
        simple_clear_target [95.1%(18%) / 39]
          1-1-1-1-1-1 @ "A_01, E_02를 공격해." @ 39 @ [] @ accepted_20260514_002649.jsonl_seed_master_0001, accepted_20260514_005848.jsonl_batch_0001_001, accepted_20260514_015203.jsonl_batch_0002_001, accepted_20260514_015203.jsonl_batch_0002_002, accepted_20260514_015203.jsonl_batch_0002_003, accepted_20260514_015203.jsonl_batch_0002_004, accepted_20260514_015203.jsonl_batch_0002_005, accepted_20260514_015203.jsonl_batch_0002_006, accepted_20260514_015203.jsonl_batch_0002_007, accepted_20260514_021615.jsonl_batch_0003_001, accepted_20260514_021615.jsonl_batch_0003_002, accepted_20260514_021615.jsonl_batch_0003_003, accepted_20260514_021615.jsonl_batch_0003_004, accepted_20260514_021615.jsonl_batch_0003_005, accepted_20260514_021615.jsonl_batch_0003_006, accepted_20260514_021615.jsonl_batch_0003_007, accepted_20260514_021615.jsonl_batch_0003_008, accepted_20260514_021615.jsonl_batch_0003_009, accepted_20260514_021615.jsonl_batch_0003_010, accepted_20260514_022817.jsonl_batch_0004_001, accepted_20260514_022817.jsonl_batch_0004_002, accepted_20260514_022817.jsonl_batch_0004_003, accepted_20260514_022817.jsonl_batch_0004_004, accepted_20260514_022817.jsonl_batch_0004_005, accepted_20260514_022817.jsonl_batch_0004_006, accepted_20260514_022817.jsonl_batch_0004_007, accepted_20260514_022817.jsonl_batch_0004_008, accepted_20260514_022817.jsonl_batch_0004_009, accepted_20260514_022817.jsonl_batch_0004_010, accepted_20260514_024019.jsonl_batch_0005_001, accepted_20260514_024019.jsonl_batch_0005_002, accepted_20260514_024019.jsonl_batch_0005_003, accepted_20260514_024019.jsonl_batch_0005_004, accepted_20260514_024019.jsonl_batch_0005_005, accepted_20260514_024019.jsonl_batch_0005_006, accepted_20260514_024019.jsonl_batch_0005_007, accepted_20260514_024019.jsonl_batch_0005_008, accepted_20260514_024019.jsonl_batch_0005_009, accepted_20260514_024019.jsonl_batch_0005_010
        multiple_valid_targets [4.9%(10%) / 2]
          1-1-1-1-2-1 @ "A_01, 지금 가장 처리하기 좋은 적을 골라 공격해." @ 2 @ [] @ accepted_20260514_002742.jsonl_seed_master_0114, accepted_20260514_024137.jsonl_batch_0006_001
      move_then_attack [50.6%(25%) / 42]
        simple_clear_target [7.1%(18%) / 3]
          1-1-1-3-1-1 @ "A_01, E_02에게 접근해서 공격해." @ 3 @ [] @ accepted_20260514_002742.jsonl_seed_master_0115, accepted_20260514_024903.jsonl_batch_0007_002, accepted_20260514_024903.jsonl_batch_0007_004
        pressure_source_target_clear [19.0%(8%) / 8]
          1-1-1-3-7-1 @ "A_01, E_02에게 붙어서 공격해." @ 8 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0116, accepted_20260514_025740.jsonl_batch_0008_001, accepted_20260514_025740.jsonl_batch_0008_002, accepted_20260514_025740.jsonl_batch_0008_003, accepted_20260514_025740.jsonl_batch_0008_004, accepted_20260514_025740.jsonl_batch_0008_005, accepted_20260514_025740.jsonl_batch_0008_006, accepted_20260514_025740.jsonl_batch_0008_007
        flank_attack_requested [73.8%(6%) / 31]
          1-1-1-3-9-1 @ "A_01, E_02의 뒤쪽으로 돌아가서 공격해." @ 31 @ flank_requested @ accepted_20260514_002740.jsonl_seed_master_0014, accepted_20260514_031435.jsonl_batch_0009_001, accepted_20260514_031435.jsonl_batch_0009_002, accepted_20260514_031435.jsonl_batch_0009_003, accepted_20260514_031435.jsonl_batch_0009_004, accepted_20260514_031435.jsonl_batch_0009_005, accepted_20260514_031435.jsonl_batch_0009_006, accepted_20260514_031435.jsonl_batch_0009_007, accepted_20260514_031435.jsonl_batch_0009_008, accepted_20260514_031435.jsonl_batch_0009_009, accepted_20260514_031435.jsonl_batch_0009_010, accepted_20260514_032651.jsonl_batch_0010_001, accepted_20260514_032651.jsonl_batch_0010_002, accepted_20260514_032651.jsonl_batch_0010_003, accepted_20260514_032651.jsonl_batch_0010_004, accepted_20260514_032651.jsonl_batch_0010_005, accepted_20260514_032651.jsonl_batch_0010_006, accepted_20260514_032651.jsonl_batch_0010_007, accepted_20260514_032651.jsonl_batch_0010_008, accepted_20260514_032651.jsonl_batch_0010_009, accepted_20260514_032651.jsonl_batch_0010_010, accepted_20260514_033859.jsonl_batch_0011_001, accepted_20260514_033859.jsonl_batch_0011_002, accepted_20260514_033859.jsonl_batch_0011_003, accepted_20260514_033859.jsonl_batch_0011_004, accepted_20260514_033859.jsonl_batch_0011_005, accepted_20260514_033859.jsonl_batch_0011_006, accepted_20260514_033859.jsonl_batch_0011_007, accepted_20260514_033859.jsonl_batch_0011_008, accepted_20260514_033859.jsonl_batch_0011_009, accepted_20260514_033859.jsonl_batch_0011_010
    nearest_enemy [9.5%(15%) / 20]
      attack_only [90.0%(45%) / 18]
        multiple_valid_targets [94.4%(10%) / 17]
          1-1-3-1-2-1 @ "A_01, 가장 가까운 적을 공격해." @ 17 @ [] @ accepted_20260514_002742.jsonl_seed_master_0117, accepted_20260514_035057.jsonl_batch_0012_001, accepted_20260514_035057.jsonl_batch_0012_002, accepted_20260514_035057.jsonl_batch_0012_003, accepted_20260514_035057.jsonl_batch_0012_004, accepted_20260514_035057.jsonl_batch_0012_005, accepted_20260514_035057.jsonl_batch_0012_006, accepted_20260514_035057.jsonl_batch_0012_007, accepted_20260514_035057.jsonl_batch_0012_008, accepted_20260514_035057.jsonl_batch_0012_009, accepted_20260514_035057.jsonl_batch_0012_010, accepted_20260514_035808.jsonl_batch_0013_001, accepted_20260514_035808.jsonl_batch_0013_002, accepted_20260514_035808.jsonl_batch_0013_003, accepted_20260514_035808.jsonl_batch_0013_004, accepted_20260514_035808.jsonl_batch_0013_005, accepted_20260514_035808.jsonl_batch_0013_006
        nearest_target_clear [5.6%(8%) / 1]
          1-1-3-1-3-1 @ "A_02, 가장 가까운 적을 공격해." @ 1 @ [] @ accepted_20260514_002649.jsonl_seed_master_0002
      move_then_attack [10.0%(25%) / 2]
        nearest_target_clear [100.0%(8%) / 2]
          1-1-3-3-3-1 @ "A_02, 제일 가까운 적한테 붙어서 공격해." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0015, accepted_20260514_042028.jsonl_batch_0015_001
    lowest_hp_enemy [7.6%(15%) / 16]
      attack_only [87.5%(45%) / 14]
        multiple_valid_targets [85.7%(10%) / 12]
          1-1-4-1-2-1 @ "A_01, 체력이 제일 낮은 적을 공격해." @ 12 @ [] @ accepted_20260514_002742.jsonl_seed_master_0118, accepted_20260514_043231.jsonl_batch_0016_003, accepted_20260514_043231.jsonl_batch_0016_004, accepted_20260514_043231.jsonl_batch_0016_005, accepted_20260514_043231.jsonl_batch_0016_007, accepted_20260514_043231.jsonl_batch_0016_010, accepted_20260514_044426.jsonl_batch_0017_001, accepted_20260514_044426.jsonl_batch_0017_002, accepted_20260514_044426.jsonl_batch_0017_003, accepted_20260514_044426.jsonl_batch_0017_004, accepted_20260514_044426.jsonl_batch_0017_005, accepted_20260514_044426.jsonl_batch_0017_006
        lowest_hp_target_clear [14.3%(8%) / 2]
          1-1-4-1-4-1 @ "A_03, 체력이 제일 낮은 적을 노려." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0016, accepted_20260514_044542.jsonl_batch_0018_001
      move_then_attack [12.5%(25%) / 2]
        lowest_hp_target_clear [100.0%(8%) / 2]
          1-1-4-3-4-1 @ "A_01, 체력이 제일 낮은 적에게 붙어서 공격해." @ 2 @ [] @ accepted_20260514_002742.jsonl_seed_master_0119, accepted_20260514_044700.jsonl_batch_0019_001
    highest_threat_enemy [15.7%(12%) / 33]
      attack_only [90.9%(45%) / 30]
        multiple_valid_targets [63.3%(10%) / 19]
          1-1-5-1-2-1 @ "A_01, 가장 위협적인 적을 공격해." @ 19 @ [] @ accepted_20260514_002742.jsonl_seed_master_0120, accepted_20260514_045844.jsonl_batch_0020_001, accepted_20260514_045844.jsonl_batch_0020_002, accepted_20260514_045844.jsonl_batch_0020_003, accepted_20260514_045844.jsonl_batch_0020_004, accepted_20260514_045844.jsonl_batch_0020_005, accepted_20260514_045844.jsonl_batch_0020_006, accepted_20260514_045844.jsonl_batch_0020_007, accepted_20260514_045844.jsonl_batch_0020_008, accepted_20260514_045844.jsonl_batch_0020_009, accepted_20260514_045844.jsonl_batch_0020_010, accepted_20260514_051047.jsonl_batch_0021_001, accepted_20260514_051047.jsonl_batch_0021_002, accepted_20260514_051047.jsonl_batch_0021_003, accepted_20260514_051047.jsonl_batch_0021_004, accepted_20260514_051047.jsonl_batch_0021_005, accepted_20260514_051047.jsonl_batch_0021_006, accepted_20260514_051047.jsonl_batch_0021_007, accepted_20260514_051047.jsonl_batch_0021_008
        highest_threat_target_clear [36.7%(7%) / 11]
          1-1-5-1-5-1 @ "A_01, 제일 위험한 적부터 공격해." @ 11 @ [] @ accepted_20260514_002740.jsonl_seed_master_0017, accepted_20260514_052252.jsonl_batch_0022_001, accepted_20260514_052252.jsonl_batch_0022_002, accepted_20260514_052252.jsonl_batch_0022_003, accepted_20260514_052252.jsonl_batch_0022_004, accepted_20260514_052252.jsonl_batch_0022_005, accepted_20260514_052252.jsonl_batch_0022_006, accepted_20260514_052252.jsonl_batch_0022_007, accepted_20260514_052252.jsonl_batch_0022_008, accepted_20260514_052252.jsonl_batch_0022_009, accepted_20260514_052252.jsonl_batch_0022_010
      move_then_attack [9.1%(25%) / 3]
        highest_threat_target_clear [100.0%(7%) / 3]
          1-1-5-3-5-1 @ "A_01, 제일 위험한 적에게 접근해서 공격해." @ 3 @ [] @ accepted_20260514_002742.jsonl_seed_master_0121, accepted_20260514_052521.jsonl_batch_0023_001, accepted_20260514_052521.jsonl_batch_0023_002
    role_based_enemy [6.2%(12%) / 13]
      attack_only [84.6%(45%) / 11]
        multiple_valid_targets [27.3%(10%) / 3]
          1-1-6-1-2-1 @ "A_01, 후열 적을 먼저 공격해." @ 3 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0122, accepted_20260514_052754.jsonl_batch_0024_001, accepted_20260514_052754.jsonl_batch_0024_002
        role_based_target_clear [72.7%(8%) / 8]
          1-1-6-1-6-1 @ "A_02, 적 원거리 유닛을 먼저 끊어." @ 4 @ target_role_ranged_enemy @ accepted_20260514_002740.jsonl_seed_master_0018, accepted_20260514_053136.jsonl_batch_0025_001, accepted_20260514_053136.jsonl_batch_0025_002, accepted_20260514_053136.jsonl_batch_0025_003
          1-1-6-1-6-2 @ "A_02, 후방에 있는 적부터 노려." @ 4 @ target_role_backline_enemy @ accepted_20260514_002740.jsonl_seed_master_0019, accepted_20260514_053519.jsonl_batch_0026_001, accepted_20260514_053519.jsonl_batch_0026_002, accepted_20260514_053519.jsonl_batch_0026_003
      move_then_attack [15.4%(25%) / 2]
        role_based_target_clear [100.0%(8%) / 2]
          1-1-6-3-6-1 @ "A_01, 적 후열 쪽으로 붙어서 공격해." @ 2 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0123, accepted_20260514_053637.jsonl_batch_0027_001
    pressure_source_enemy [2.9%(10%) / 6]
      attack_only [66.7%(45%) / 4]
        pressure_source_target_clear [100.0%(8%) / 4]
          1-1-7-1-7-1 @ "A_01, A_02를 때리는 적을 공격해." @ 2 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0124, accepted_20260514_053754.jsonl_batch_0028_001
          1-1-7-1-7-2 @ "A_03, A_02를 때리는 적을 공격해." @ 2 @ pressure_source_target_clear @ accepted_20260514_002740.jsonl_seed_master_0021, accepted_20260514_053911.jsonl_batch_0029_001
      move_then_attack [33.3%(25%) / 2]
        pressure_source_target_clear [100.0%(8%) / 2]
          1-1-7-3-7-1 @ "A_01, A_02를 압박하는 적에게 붙어서 공격해." @ 2 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0125, accepted_20260514_054031.jsonl_batch_0030_001
    invalid_explicit_target [18.6%(6%) / 39]
      empty_action_expected [100.0%(5%) / 39]
        dead_named_target [33.3%(6%) / 13]
          1-1-11-13-10-1 @ "A_01, 죽은 E_02를 공격해." @ 13 @ named_target_dead @ accepted_20260514_002742.jsonl_seed_master_0126, accepted_20260514_064341.jsonl_batch_0031_001, accepted_20260514_065653.jsonl_batch_0032_001, accepted_20260514_065653.jsonl_batch_0032_002, accepted_20260514_065653.jsonl_batch_0032_003, accepted_20260514_065653.jsonl_batch_0032_004, accepted_20260514_065653.jsonl_batch_0032_005, accepted_20260514_065653.jsonl_batch_0032_006, accepted_20260514_065653.jsonl_batch_0032_007, accepted_20260514_065653.jsonl_batch_0032_008, accepted_20260514_065653.jsonl_batch_0032_009, accepted_20260514_065653.jsonl_batch_0032_010, accepted_20260514_065805.jsonl_batch_0033_001
        untargetable_named_target [66.7%(5%) / 26]
          1-1-11-13-11-1 @ "A_01, 숨어 있는 E_02를 공격해." @ 26 @ named_target_untargetable @ accepted_20260514_002742.jsonl_seed_master_0127, accepted_20260514_070918.jsonl_batch_0034_001, accepted_20260514_070918.jsonl_batch_0034_002, accepted_20260514_070918.jsonl_batch_0034_003, accepted_20260514_070918.jsonl_batch_0034_004, accepted_20260514_070918.jsonl_batch_0034_005, accepted_20260514_070918.jsonl_batch_0034_006, accepted_20260514_070918.jsonl_batch_0034_007, accepted_20260514_070918.jsonl_batch_0034_008, accepted_20260514_070918.jsonl_batch_0034_009, accepted_20260514_070918.jsonl_batch_0034_010, accepted_20260514_072025.jsonl_batch_0035_001, accepted_20260514_072025.jsonl_batch_0035_002, accepted_20260514_072025.jsonl_batch_0035_003, accepted_20260514_072025.jsonl_batch_0035_004, accepted_20260514_072025.jsonl_batch_0035_005, accepted_20260514_072025.jsonl_batch_0035_006, accepted_20260514_072025.jsonl_batch_0035_007, accepted_20260514_072025.jsonl_batch_0035_008, accepted_20260514_072025.jsonl_batch_0035_009, accepted_20260514_072025.jsonl_batch_0035_010, accepted_20260514_072600.jsonl_batch_0036_001, accepted_20260514_072600.jsonl_batch_0036_002, accepted_20260514_072600.jsonl_batch_0036_003, accepted_20260514_072600.jsonl_batch_0036_004, accepted_20260514_072600.jsonl_batch_0036_005
  explicit_multi_actor [16.2%(15%) / 66]
    explicit_enemy_target [15.2%(30%) / 10]
      multi_actor_same_target [30.0%(18%) / 3]
        focus_fire_clear [100.0%(8%) / 3]
          1-2-1-11-8-1 @ "A_01과 A_02는 E_01을 같이 공격해." @ 3 @ [] @ accepted_20260514_002740.jsonl_seed_master_0022, accepted_20260514_072835.jsonl_batch_0037_001, accepted_20260514_072835.jsonl_batch_0037_002
      multi_actor_different_targets [70.0%(7%) / 7]
        focus_fire_clear [100.0%(8%) / 7]
          1-2-1-12-8-1 @ "A_01은 E_01을, A_02는 E_03을 공격해." @ 7 @ [] @ accepted_20260514_002740.jsonl_seed_master_0023, accepted_20260514_073617.jsonl_batch_0038_001, accepted_20260514_073617.jsonl_batch_0038_002, accepted_20260514_073617.jsonl_batch_0038_003, accepted_20260514_073617.jsonl_batch_0038_004, accepted_20260514_073617.jsonl_batch_0038_005, accepted_20260514_073617.jsonl_batch_0038_006
    nearest_enemy [3.0%(15%) / 2]
      multi_actor_different_targets [100.0%(7%) / 2]
        nearest_target_clear [100.0%(8%) / 2]
          1-2-3-12-3-1 @ "A_01과 A_02는 각자 가장 가까운 적을 공격해." @ 2 @ [] @ accepted_20260514_002742.jsonl_seed_master_0128, accepted_20260514_073737.jsonl_batch_0039_001
    lowest_hp_enemy [6.1%(15%) / 4]
      multi_actor_same_target [50.0%(18%) / 2]
        lowest_hp_target_clear [100.0%(8%) / 2]
          1-2-4-11-4-1 @ "A_01과 A_02는 체력이 제일 낮은 적을 같이 공격해." @ 2 @ [] @ accepted_20260514_002742.jsonl_seed_master_0129, accepted_20260514_073857.jsonl_batch_0040_001
      multi_actor_different_targets [50.0%(7%) / 2]
        lowest_hp_target_clear [100.0%(8%) / 2]
          1-2-4-12-4-1 @ "A_01과 A_02는 각자 체력이 제일 낮은 적을 노려." @ 2 @ [] @ accepted_20260514_002742.jsonl_seed_master_0130, accepted_20260514_074017.jsonl_batch_0041_001
    highest_threat_enemy [25.8%(12%) / 17]
      multi_actor_same_target [100.0%(18%) / 17]
        highest_threat_target_clear [100.0%(7%) / 17]
          1-2-5-11-5-1 @ "A_01과 A_02는 제일 위험한 적을 같이 공격해." @ 17 @ [] @ accepted_20260514_002742.jsonl_seed_master_0131, accepted_20260514_075254.jsonl_batch_0042_001, accepted_20260514_075254.jsonl_batch_0042_002, accepted_20260514_075254.jsonl_batch_0042_003, accepted_20260514_075254.jsonl_batch_0042_004, accepted_20260514_075254.jsonl_batch_0042_005, accepted_20260514_075254.jsonl_batch_0042_006, accepted_20260514_075254.jsonl_batch_0042_007, accepted_20260514_075254.jsonl_batch_0042_008, accepted_20260514_075254.jsonl_batch_0042_009, accepted_20260514_075254.jsonl_batch_0042_010, accepted_20260514_080039.jsonl_batch_0043_001, accepted_20260514_080039.jsonl_batch_0043_002, accepted_20260514_080039.jsonl_batch_0043_003, accepted_20260514_080039.jsonl_batch_0043_004, accepted_20260514_080039.jsonl_batch_0043_005, accepted_20260514_080039.jsonl_batch_0043_006
    role_based_enemy [45.5%(12%) / 30]
      multi_actor_same_target [20.0%(18%) / 6]
        role_based_target_clear [100.0%(8%) / 6]
          1-2-6-11-6-1 @ "A_01과 A_02는 적 후열을 같이 공격해." @ 6 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0133, accepted_20260514_080709.jsonl_batch_0044_001, accepted_20260514_080709.jsonl_batch_0044_002, accepted_20260514_080709.jsonl_batch_0044_003, accepted_20260514_080709.jsonl_batch_0044_004, accepted_20260514_080709.jsonl_batch_0044_005
      multi_actor_different_targets [80.0%(7%) / 24]
        role_based_target_clear [100.0%(8%) / 24]
          1-2-6-12-6-1 @ "A_01은 적 전열을 묶고, A_02는 적 후열을 공격해." @ 24 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0132, accepted_20260514_082011.jsonl_batch_0045_001, accepted_20260514_082011.jsonl_batch_0045_002, accepted_20260514_082011.jsonl_batch_0045_003, accepted_20260514_082011.jsonl_batch_0045_004, accepted_20260514_082011.jsonl_batch_0045_005, accepted_20260514_082011.jsonl_batch_0045_006, accepted_20260514_082011.jsonl_batch_0045_007, accepted_20260514_082011.jsonl_batch_0045_008, accepted_20260514_082011.jsonl_batch_0045_009, accepted_20260514_082011.jsonl_batch_0045_010, accepted_20260514_083309.jsonl_batch_0046_001, accepted_20260514_083309.jsonl_batch_0046_002, accepted_20260514_083309.jsonl_batch_0046_003, accepted_20260514_083309.jsonl_batch_0046_004, accepted_20260514_083309.jsonl_batch_0046_005, accepted_20260514_083309.jsonl_batch_0046_006, accepted_20260514_083309.jsonl_batch_0046_007, accepted_20260514_083309.jsonl_batch_0046_008, accepted_20260514_083309.jsonl_batch_0046_009, accepted_20260514_083309.jsonl_batch_0046_010, accepted_20260514_083704.jsonl_batch_0047_001, accepted_20260514_083704.jsonl_batch_0047_002, accepted_20260514_083704.jsonl_batch_0047_003
    pressure_source_enemy [4.5%(10%) / 3]
      multi_actor_same_target [100.0%(18%) / 3]
        pressure_source_target_clear [100.0%(8%) / 3]
          1-2-7-11-7-1 @ "A_01과 A_02는 아군을 압박하는 적을 같이 공격해." @ 3 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0134, accepted_20260514_083945.jsonl_batch_0048_001, accepted_20260514_083945.jsonl_batch_0048_002
    invalid_explicit_target [0.0%(6%) / 0]
  global_condition [12.0%(20%) / 49]
    explicit_enemy_target [51.0%(30%) / 25]
      multi_actor_same_target [100.0%(18%) / 25]
        focus_fire_clear [100.0%(8%) / 25]
          1-3-1-11-8-1 @ "손이 비는 아군은 전부 E_01을 집중 공격해." @ 25 @ free_actor_selection @ accepted_20260514_002649.jsonl_seed_master_0003, accepted_20260514_085936.jsonl_batch_0049_001, accepted_20260514_085936.jsonl_batch_0049_002, accepted_20260514_085936.jsonl_batch_0049_003, accepted_20260514_085936.jsonl_batch_0049_004, accepted_20260514_085936.jsonl_batch_0049_005, accepted_20260514_085936.jsonl_batch_0049_006, accepted_20260514_085936.jsonl_batch_0049_007, accepted_20260514_085936.jsonl_batch_0049_008, accepted_20260514_085936.jsonl_batch_0049_009, accepted_20260514_085936.jsonl_batch_0049_010, accepted_20260514_091202.jsonl_batch_0050_001, accepted_20260514_091202.jsonl_batch_0050_002, accepted_20260514_091202.jsonl_batch_0050_003, accepted_20260514_091202.jsonl_batch_0050_004, accepted_20260514_091202.jsonl_batch_0050_005, accepted_20260514_091202.jsonl_batch_0050_006, accepted_20260514_091202.jsonl_batch_0050_007, accepted_20260514_091202.jsonl_batch_0050_008, accepted_20260514_091202.jsonl_batch_0050_009, accepted_20260514_091202.jsonl_batch_0050_010, accepted_20260514_091703.jsonl_batch_0051_001, accepted_20260514_091703.jsonl_batch_0051_002, accepted_20260514_091703.jsonl_batch_0051_003, accepted_20260514_091703.jsonl_batch_0051_004
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [4.1%(15%) / 2]
      multi_actor_same_target [100.0%(18%) / 2]
        lowest_hp_target_clear [100.0%(8%) / 2]
          1-3-4-11-4-1 @ "공격 가능한 아군은 체력이 제일 낮은 적을 같이 공격해." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0024, accepted_20260514_091820.jsonl_batch_0052_001
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [44.9%(10%) / 22]
      multi_actor_same_target [100.0%(18%) / 22]
        pressure_source_target_clear [100.0%(8%) / 22]
          1-3-7-11-7-1 @ "손이 비는 아군은 압박받는 아군을 때리는 적을 같이 공격해." @ 22 @ free_actor_selection, pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0136, accepted_20260514_093100.jsonl_batch_0053_001, accepted_20260514_093100.jsonl_batch_0053_002, accepted_20260514_093100.jsonl_batch_0053_003, accepted_20260514_093100.jsonl_batch_0053_004, accepted_20260514_093100.jsonl_batch_0053_005, accepted_20260514_093100.jsonl_batch_0053_006, accepted_20260514_093100.jsonl_batch_0053_007, accepted_20260514_093100.jsonl_batch_0053_008, accepted_20260514_093100.jsonl_batch_0053_009, accepted_20260514_093100.jsonl_batch_0053_010, accepted_20260514_094322.jsonl_batch_0054_001, accepted_20260514_094322.jsonl_batch_0054_002, accepted_20260514_094322.jsonl_batch_0054_003, accepted_20260514_094322.jsonl_batch_0054_004, accepted_20260514_094322.jsonl_batch_0054_005, accepted_20260514_094322.jsonl_batch_0054_006, accepted_20260514_094322.jsonl_batch_0054_007, accepted_20260514_094322.jsonl_batch_0054_008, accepted_20260514_094322.jsonl_batch_0054_009, accepted_20260514_094322.jsonl_batch_0054_010, accepted_20260514_095343.jsonl_batch_0055_001
    invalid_explicit_target [0.0%(6%) / 0]
  global_role_based [10.3%(15%) / 42]
    explicit_enemy_target [4.8%(30%) / 2]
      multi_actor_same_target [100.0%(18%) / 2]
        focus_fire_clear [100.0%(8%) / 2]
          1-4-1-11-8-1 @ "근접 아군은 E_01을 묶어." @ 2 @ actor_role_melee @ accepted_20260514_002740.jsonl_seed_master_0026, accepted_20260514_095500.jsonl_batch_0056_001
    nearest_enemy [71.4%(15%) / 30]
      move_then_attack [100.0%(25%) / 30]
        nearest_target_clear [100.0%(8%) / 30]
          1-4-3-3-3-1 @ "근접 아군은 가장 가까운 적에게 붙어서 공격해." @ 30 @ actor_role_melee @ accepted_20260514_002742.jsonl_seed_master_0137, accepted_20260514_100613.jsonl_batch_0057_001, accepted_20260514_100613.jsonl_batch_0057_002, accepted_20260514_100613.jsonl_batch_0057_003, accepted_20260514_100613.jsonl_batch_0057_004, accepted_20260514_100613.jsonl_batch_0057_005, accepted_20260514_100613.jsonl_batch_0057_006, accepted_20260514_100613.jsonl_batch_0057_007, accepted_20260514_100613.jsonl_batch_0057_008, accepted_20260514_100613.jsonl_batch_0057_009, accepted_20260514_100613.jsonl_batch_0057_010, accepted_20260514_101819.jsonl_batch_0058_001, accepted_20260514_101819.jsonl_batch_0058_002, accepted_20260514_101819.jsonl_batch_0058_003, accepted_20260514_101819.jsonl_batch_0058_004, accepted_20260514_101819.jsonl_batch_0058_005, accepted_20260514_101819.jsonl_batch_0058_006, accepted_20260514_101819.jsonl_batch_0058_007, accepted_20260514_101819.jsonl_batch_0058_008, accepted_20260514_101819.jsonl_batch_0058_009, accepted_20260514_101819.jsonl_batch_0058_010, accepted_20260514_103435.jsonl_batch_0059_001, accepted_20260514_103435.jsonl_batch_0059_002, accepted_20260514_103435.jsonl_batch_0059_003, accepted_20260514_103435.jsonl_batch_0059_004, accepted_20260514_103435.jsonl_batch_0059_005, accepted_20260514_103435.jsonl_batch_0059_006, accepted_20260514_103435.jsonl_batch_0059_007, accepted_20260514_103435.jsonl_batch_0059_008, accepted_20260514_103435.jsonl_batch_0059_009
    lowest_hp_enemy [0.0%(15%) / 0]
    highest_threat_enemy [0.0%(12%) / 0]
    role_based_enemy [23.8%(12%) / 10]
      multi_actor_different_targets [100.0%(7%) / 10]
        role_based_target_clear [100.0%(8%) / 10]
          1-4-6-12-6-1 @ "원거리 아군은 적 후열을 먼저 공격해." @ 10 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260514_002740.jsonl_seed_master_0025, accepted_20260514_104536.jsonl_batch_0060_001, accepted_20260514_104536.jsonl_batch_0060_002, accepted_20260514_104536.jsonl_batch_0060_003, accepted_20260514_104536.jsonl_batch_0060_004, accepted_20260514_104536.jsonl_batch_0060_005, accepted_20260514_104536.jsonl_batch_0060_006, accepted_20260514_104536.jsonl_batch_0060_007, accepted_20260514_104536.jsonl_batch_0060_008, accepted_20260514_104536.jsonl_batch_0060_009
    pressure_source_enemy [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(6%) / 0]
  global_state_based [10.0%(15%) / 41]
    explicit_enemy_target [0.0%(30%) / 0]
    nearest_enemy [0.0%(15%) / 0]
    lowest_hp_enemy [73.2%(15%) / 30]
      attack_only [100.0%(45%) / 30]
        lowest_hp_target_clear [100.0%(8%) / 30]
          1-5-4-1-4-1 @ "지금 공격 여유가 있는 아군은 체력이 제일 낮은 적을 공격해." @ 30 @ healthy_actor_selection @ accepted_20260514_002742.jsonl_seed_master_0138, accepted_20260514_110453.jsonl_batch_0061_001, accepted_20260514_110453.jsonl_batch_0061_002, accepted_20260514_110453.jsonl_batch_0061_003, accepted_20260514_110453.jsonl_batch_0061_004, accepted_20260514_110453.jsonl_batch_0061_005, accepted_20260514_110453.jsonl_batch_0061_006, accepted_20260514_110453.jsonl_batch_0061_007, accepted_20260514_110453.jsonl_batch_0061_008, accepted_20260514_110453.jsonl_batch_0061_009, accepted_20260514_110453.jsonl_batch_0061_010, accepted_20260514_111725.jsonl_batch_0062_001, accepted_20260514_111725.jsonl_batch_0062_002, accepted_20260514_111725.jsonl_batch_0062_003, accepted_20260514_111725.jsonl_batch_0062_004, accepted_20260514_111725.jsonl_batch_0062_005, accepted_20260514_111725.jsonl_batch_0062_006, accepted_20260514_111725.jsonl_batch_0062_007, accepted_20260514_111725.jsonl_batch_0062_008, accepted_20260514_111725.jsonl_batch_0062_009, accepted_20260514_111725.jsonl_batch_0062_010, accepted_20260514_112850.jsonl_batch_0063_001, accepted_20260514_112850.jsonl_batch_0063_002, accepted_20260514_112850.jsonl_batch_0063_003, accepted_20260514_112850.jsonl_batch_0063_004, accepted_20260514_112850.jsonl_batch_0063_005, accepted_20260514_112850.jsonl_batch_0063_006, accepted_20260514_112850.jsonl_batch_0063_007, accepted_20260514_112850.jsonl_batch_0063_008, accepted_20260514_112850.jsonl_batch_0063_009
    highest_threat_enemy [24.4%(12%) / 10]
      multi_actor_same_target [100.0%(18%) / 10]
        highest_threat_target_clear [100.0%(7%) / 10]
          1-5-5-11-5-1 @ "체력이 여유 있는 아군은 제일 위험한 적을 압박해." @ 10 @ healthy_actor_selection @ accepted_20260514_002740.jsonl_seed_master_0027, accepted_20260514_114003.jsonl_batch_0064_001, accepted_20260514_114003.jsonl_batch_0064_002, accepted_20260514_114003.jsonl_batch_0064_003, accepted_20260514_114003.jsonl_batch_0064_004, accepted_20260514_114003.jsonl_batch_0064_005, accepted_20260514_114003.jsonl_batch_0064_006, accepted_20260514_114003.jsonl_batch_0064_007, accepted_20260514_114003.jsonl_batch_0064_008, accepted_20260514_114003.jsonl_batch_0064_009
    role_based_enemy [0.0%(12%) / 0]
    pressure_source_enemy [2.4%(10%) / 1]
      multi_actor_same_target [100.0%(18%) / 1]
        pressure_source_target_clear [100.0%(8%) / 1]
          1-5-7-11-7-1 @ "지원 가능한 아군은 아군을 압박하는 적을 같이 공격해." @ 1 @ pressure_source_target_clear @ accepted_20260514_002742.jsonl_seed_master_0139
    invalid_explicit_target [0.0%(6%) / 0]

move [15.4%(22%) / 94]
  explicit_actor [83.0%(45%) / 78]
    explicit_ally_target [79.5%(22%) / 62]
      move_only [80.6%(55%) / 50]
        move_to_alive_ally [84.0%(10%) / 42]
          2-1-2-2-1-1 @ "A_02, A_04에게 이동해." @ 42 @ [] @ accepted_20260514_002649.jsonl_seed_master_0004, accepted_20260514_115253.jsonl_batch_0066_001, accepted_20260514_115253.jsonl_batch_0066_002, accepted_20260514_115253.jsonl_batch_0066_003, accepted_20260514_115253.jsonl_batch_0066_004, accepted_20260514_115253.jsonl_batch_0066_005, accepted_20260514_115253.jsonl_batch_0066_006, accepted_20260514_115253.jsonl_batch_0066_007, accepted_20260514_115253.jsonl_batch_0066_008, accepted_20260514_115253.jsonl_batch_0066_009, accepted_20260514_115253.jsonl_batch_0066_010, accepted_20260514_120446.jsonl_batch_0067_001, accepted_20260514_120446.jsonl_batch_0067_002, accepted_20260514_120446.jsonl_batch_0067_003, accepted_20260514_120446.jsonl_batch_0067_004, accepted_20260514_120446.jsonl_batch_0067_005, accepted_20260514_120446.jsonl_batch_0067_006, accepted_20260514_120446.jsonl_batch_0067_007, accepted_20260514_120446.jsonl_batch_0067_008, accepted_20260514_120446.jsonl_batch_0067_009, accepted_20260514_120446.jsonl_batch_0067_010, accepted_20260514_121642.jsonl_batch_0068_001, accepted_20260514_121642.jsonl_batch_0068_002, accepted_20260514_121642.jsonl_batch_0068_003, accepted_20260514_121642.jsonl_batch_0068_004, accepted_20260514_121642.jsonl_batch_0068_005, accepted_20260514_121642.jsonl_batch_0068_006, accepted_20260514_121642.jsonl_batch_0068_007, accepted_20260514_121642.jsonl_batch_0068_008, accepted_20260514_121642.jsonl_batch_0068_009, accepted_20260514_121642.jsonl_batch_0068_010, accepted_20260514_122845.jsonl_batch_0069_001, accepted_20260514_122845.jsonl_batch_0069_002, accepted_20260514_122845.jsonl_batch_0069_003, accepted_20260514_122845.jsonl_batch_0069_004, accepted_20260514_122845.jsonl_batch_0069_005, accepted_20260514_122845.jsonl_batch_0069_006, accepted_20260514_122845.jsonl_batch_0069_007, accepted_20260514_122845.jsonl_batch_0069_008, accepted_20260514_122845.jsonl_batch_0069_009, accepted_20260514_122845.jsonl_batch_0069_010, accepted_20260514_123001.jsonl_batch_0070_001
        move_to_dead_ally [2.0%(5%) / 1]
          2-1-2-2-2-1 @ "A_02, A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260514_002740.jsonl_seed_master_0028
        help_ally [6.0%(10%) / 3]
          2-1-2-2-8-1 @ "A_02, A_04 근처로 가." @ 3 @ [] @ accepted_20260514_002740.jsonl_seed_master_0030, accepted_20260514_123934.jsonl_batch_0072_001, accepted_20260514_123934.jsonl_batch_0072_002
        move_to_self_attempt [8.0%(5%) / 4]
          2-1-2-2-11-1 @ "A_02, 네 위치로 다시 붙어." @ 4 @ move_to_self_attempt @ accepted_20260514_002740.jsonl_seed_master_0029, accepted_20260514_124259.jsonl_batch_0073_001, accepted_20260514_124259.jsonl_batch_0073_002, accepted_20260514_124259.jsonl_batch_0073_003
      move_then_attack [17.7%(20%) / 11]
        help_ally [100.0%(10%) / 11]
          2-1-2-3-8-1 @ "A_02, A_04 근처로 가서 주변 적을 공격해." @ 11 @ help_ally_then_attack @ accepted_20260514_002740.jsonl_seed_master_0031, accepted_20260514_125535.jsonl_batch_0074_001, accepted_20260514_125535.jsonl_batch_0074_002, accepted_20260514_125535.jsonl_batch_0074_003, accepted_20260514_125535.jsonl_batch_0074_004, accepted_20260514_125535.jsonl_batch_0074_005, accepted_20260514_125535.jsonl_batch_0074_006, accepted_20260514_125535.jsonl_batch_0074_007, accepted_20260514_125535.jsonl_batch_0074_008, accepted_20260514_125535.jsonl_batch_0074_009, accepted_20260514_125535.jsonl_batch_0074_010
      empty_action_expected [1.6%(10%) / 1]
        move_to_self_attempt [100.0%(5%) / 1]
          2-1-2-13-11-1 @ "A_02, A_02에게 이동해." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0141
    explicit_enemy_target [3.8%(18%) / 3]
      move_only [33.3%(55%) / 1]
        approach_enemy_only [100.0%(10%) / 1]
          2-1-1-2-3-1 @ "A_01, E_02에게 접근해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0032
      move_then_attack [66.7%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          2-1-1-3-4-1 @ "A_01, E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0033
        flank_enemy_then_attack [50.0%(8%) / 1]
          2-1-1-3-5-1 @ "A_01, E_02 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260514_002740.jsonl_seed_master_0034
    safe_ally [3.8%(16%) / 3]
      move_only [66.7%(55%) / 2]
        retreat_to_backline_ally [50.0%(12%) / 1]
          2-1-8-2-6-1 @ "A_01, 아군 뒤쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0035
        low_hp_actor_escape [50.0%(10%) / 1]
          2-1-8-2-7-1 @ "A_01, 체력이 낮으니 안전한 아군 쪽으로 빠져." @ 1 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0142
      empty_action_expected [33.3%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          2-1-8-13-12-1 @ "A_01, 안전한 아군 쪽으로 빠져." @ 1 @ no_matching_actor, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0143
    low_hp_ally [2.6%(12%) / 2]
      move_only [50.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          2-1-9-2-9-1 @ "A_01, 체력이 낮은 아군에게 붙어." @ 1 @ low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0036
      move_then_attack [50.0%(20%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          2-1-9-3-9-1 @ "A_01, 체력이 낮은 아군에게 붙어서 주변 적을 공격해." @ 1 @ low_hp_ally_target, help_ally_then_attack @ accepted_20260514_002742.jsonl_seed_master_0144
    backline_ally [2.6%(10%) / 2]
      move_only [100.0%(55%) / 2]
        retreat_to_backline_ally [50.0%(12%) / 1]
          2-1-10-2-6-1 @ "A_01, 후열 아군 쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0145
        low_hp_actor_escape [50.0%(10%) / 1]
          2-1-10-2-7-1 @ "A_01, 체력이 낮으니까 후열 아군 쪽으로 빠져." @ 1 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0146
    role_based_enemy [3.8%(5%) / 3]
      move_only [33.3%(55%) / 1]
        approach_enemy_only [100.0%(10%) / 1]
          2-1-6-2-3-1 @ "A_01, 적 후열 쪽으로 이동해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0149
      move_then_attack [66.7%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          2-1-6-3-4-1 @ "A_01, 적 후열에 접근해서 공격해." @ 1 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0148
        flank_enemy_then_attack [50.0%(8%) / 1]
          2-1-6-3-5-1 @ "A_01, 적 후열 쪽으로 돌아가서 공격해." @ 1 @ flank_requested, target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0147
    invalid_explicit_target [2.6%(7%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        move_to_dead_ally [50.0%(5%) / 1]
          2-1-11-13-2-1 @ "A_02, 쓰러진 A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260514_002742.jsonl_seed_master_0150
        move_to_self_attempt [50.0%(5%) / 1]
          2-1-11-13-11-1 @ "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0151
    none [1.3%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          2-1-12-2-10-1 @ "A_01, 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0037
  explicit_multi_actor [8.5%(10%) / 8]
    explicit_ally_target [12.5%(22%) / 1]
      move_only [100.0%(55%) / 1]
        help_ally [100.0%(10%) / 1]
          2-2-2-2-8-1 @ "A_01과 A_02는 A_04 근처로 이동해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0152
    explicit_enemy_target [25.0%(18%) / 2]
      move_then_attack [100.0%(20%) / 2]
        approach_enemy_then_attack [50.0%(10%) / 1]
          2-2-1-3-4-1 @ "A_01과 A_02는 E_02에게 접근해서 공격해." @ 1 @ [] @ accepted_20260514_002742.jsonl_seed_master_0153
        flank_enemy_then_attack [50.0%(8%) / 1]
          2-2-1-3-5-1 @ "A_01과 A_02는 E_02 뒤쪽으로 돌아가서 공격해." @ 1 @ flank_requested @ accepted_20260514_002742.jsonl_seed_master_0154
    safe_ally [25.0%(16%) / 2]
      move_only [50.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          2-2-8-2-6-1 @ "A_01, A_02는 뒤로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0038
      move_then_attack [50.0%(20%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          2-2-8-3-6-1 @ "A_01과 A_02는 뒤로 빠졌다가 가까운 적을 공격해." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0155
    low_hp_ally [12.5%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          2-2-9-2-9-1 @ "A_01과 A_02는 체력이 낮은 아군에게 붙어." @ 1 @ low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0156
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [12.5%(7%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        move_to_self_attempt [100.0%(5%) / 1]
          2-2-11-13-11-1 @ "A_01과 A_02는 각자 자기 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0157
    none [12.5%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          2-2-12-2-10-1 @ "A_01과 A_02는 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260514_002742.jsonl_seed_master_0158
  global_condition [2.1%(15%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        low_hp_actor_escape [100.0%(10%) / 1]
          2-3-8-2-7-1 @ "체력이 낮은 아군은 전부 뒤로 빠져." @ 1 @ low_hp_actor_selection @ accepted_20260514_002740.jsonl_seed_master_0039
    low_hp_ally [50.0%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          2-3-9-2-9-1 @ "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 1 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0159
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  global_role_based [2.1%(15%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          2-4-8-2-6-1 @ "전열 아군은 안전한 아군 쪽으로 빠져." @ 1 @ frontline_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0160
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [50.0%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          2-4-12-2-10-1 @ "전열 아군은 앞에서 버텨." @ 1 @ frontline_actor_selection, hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0040
  global_state_based [2.1%(10%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      move_only [100.0%(55%) / 1]
        retreat_to_backline_ally [100.0%(12%) / 1]
          2-5-8-2-6-1 @ "압박받는 아군은 안전한 아군 뒤쪽으로 빠져." @ 1 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0161
    low_hp_ally [50.0%(12%) / 1]
      move_only [100.0%(55%) / 1]
        support_low_hp_ally [100.0%(8%) / 1]
          2-5-9-2-9-1 @ "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 1 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0041
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  no_valid_actor [2.1%(5%) / 2]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [50.0%(16%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          2-6-8-13-12-1 @ "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260514_002740.jsonl_seed_master_0042
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [50.0%(10%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_matching_actor [100.0%(5%) / 1]
          2-6-12-13-12-1 @ "움직일 수 있는 아군은 전부 후퇴해." @ 1 @ no_matching_actor @ accepted_20260514_002742.jsonl_seed_master_0162

skill [9.5%(26%) / 58]
  explicit_actor [72.4%(55%) / 42]
    explicit_enemy_target [31.0%(26%) / 13]
      skill_only [92.3%(70%) / 12]
        enemy_skill_valid_target [33.3%(10%) / 4]
          3-1-1-4-1-1 @ "A_01, E_02에게 도약기로 붙어." @ 1 @ mobility_skill_enemy_approach @ accepted_20260514_002741.jsonl_seed_master_0112
          3-1-1-4-1-2 @ "A_03, E_02한테 공격 스킬 써." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0103
          3-1-1-4-1-3 @ "A_03, E_02한테 스킬 써." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0043
          3-1-1-4-1-4 @ "A_03, E_02한테 약화 스킬 써." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0106
        self_skill_enemy_target_conflict [8.3%(8%) / 1]
          3-1-1-4-4-1 @ "A_03, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260514_002740.jsonl_seed_master_0044
        ally_skill_enemy_target_conflict [25.0%(8%) / 3]
          3-1-1-4-5-1 @ "A_04, E_02한테 보호 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0096
          3-1-1-4-5-2 @ "A_04, E_02한테 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002740.jsonl_seed_master_0045
          3-1-1-4-5-3 @ "A_04, E_02한테 회복 스킬 써." @ 1 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0099
        dead_target_forbidden [16.7%(6%) / 2]
          3-1-1-4-9-1 @ "A_03, 죽은 E_02한테 공격 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002740.jsonl_seed_master_0047
          3-1-1-4-9-2 @ "A_03, 죽은 E_02한테 약화 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0108
        aoe_skill_center_selection [8.3%(8%) / 1]
          3-1-1-4-10-1 @ "A_05, E_03 주변에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0164
        actor_has_no_skill [8.3%(8%) / 1]
          3-1-1-4-11-1 @ "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002740.jsonl_seed_master_0046
      move_then_skill [7.7%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          3-1-1-5-12-1 @ "A_03, E_02에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260514_002740.jsonl_seed_master_0048
    explicit_ally_target [31.0%(22%) / 13]
      skill_only [100.0%(70%) / 13]
        ally_skill_valid_target [23.1%(10%) / 3]
          3-1-2-4-2-1 @ "A_04, A_02한테 스킬 써." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0049, accepted_20260514_002741.jsonl_seed_master_0095
          3-1-2-4-2-2 @ "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002741.jsonl_seed_master_0098
        self_skill_enemy_target_conflict [7.7%(8%) / 1]
          3-1-2-4-4-1 @ "A_03, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260514_002741.jsonl_seed_master_0094
        enemy_skill_ally_target_conflict [30.8%(8%) / 4]
          3-1-2-4-6-1 @ "A_01, A_02한테 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002740.jsonl_seed_master_0050
          3-1-2-4-6-2 @ "A_03, A_02한테 공격 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0104
          3-1-2-4-6-3 @ "A_03, A_02한테 약화 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0107
          3-1-2-4-6-4 @ "A_06, A_02 주변에 광역 스킬 써." @ 1 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0110
        resurrection_dead_ally_valid [15.4%(8%) / 2]
          3-1-2-4-7-1 @ "A_04, 쓰러진 A_02한테 스킬 써." @ 2 @ dead_ally_skill_target_allowed @ accepted_20260514_002741.jsonl_seed_master_0051, accepted_20260514_002741.jsonl_seed_master_0101
        resurrection_living_ally_conflict [7.7%(6%) / 1]
          3-1-2-4-8-1 @ "A_04, 살아있는 A_02한테 부활 스킬 써." @ 1 @ text_living_target_but_resurrection_skill @ accepted_20260514_002741.jsonl_seed_master_0052
        dead_target_forbidden [15.4%(6%) / 2]
          3-1-2-4-9-1 @ "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0053
          3-1-2-4-9-2 @ "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0100
    lowest_hp_enemy [4.8%(8%) / 2]
      skill_only [100.0%(70%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          3-1-4-4-1-1 @ "A_03, 체력이 제일 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0165
        aoe_skill_center_selection [50.0%(8%) / 1]
          3-1-4-4-10-1 @ "A_06, 체력이 제일 낮은 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0166
    nearest_enemy [7.1%(5%) / 3]
      skill_only [66.7%(70%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          3-1-3-4-1-1 @ "A_03, 가장 가까운 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0168
        aoe_skill_center_selection [50.0%(8%) / 1]
          3-1-3-4-10-1 @ "A_06, 가장 가까운 적을 중심으로 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0169
      move_then_skill [33.3%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          3-1-3-5-12-1 @ "A_03, 가장 가까운 적에게 접근해서 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0167
    role_based_enemy [9.5%(8%) / 4]
      skill_only [75.0%(70%) / 3]
        enemy_skill_valid_target [33.3%(10%) / 1]
          3-1-6-4-1-1 @ "A_03, 적 후열에게 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0171
        aoe_skill_center_selection [66.7%(8%) / 2]
          3-1-6-4-10-1 @ "A_06, 적 후열이 뭉친 곳에 스킬 써." @ 1 @ target_role_backline_enemy, aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0170
          3-1-6-4-10-2 @ "A_06, 적들이 뭉친 쪽에 스킬 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002649.jsonl_seed_master_0008
      move_then_skill [25.0%(10%) / 1]
        approach_then_skill [100.0%(4%) / 1]
          3-1-6-5-12-1 @ "A_03, 적 후열에게 접근해서 스킬 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0172
    low_hp_ally [2.4%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-1-9-4-2-1 @ "A_04, 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0173
    invalid_explicit_target [4.8%(13%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        dead_target_forbidden [50.0%(6%) / 1]
          3-1-11-13-9-1 @ "A_03, 죽은 E_02한테 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002743.jsonl_seed_master_0174
        no_valid_skill_target [50.0%(4%) / 1]
          3-1-11-13-14-1 @ "A_03, 죽은 E_02한테 스킬 써." @ 1 @ named_target_dead, no_valid_skill_target @ accepted_20260514_002743.jsonl_seed_master_0175
    none [9.5%(8%) / 4]
      skill_only [75.0%(70%) / 3]
        self_skill_no_target [33.3%(8%) / 1]
          3-1-12-4-3-1 @ "A_01, 도약기로 빠져." @ 1 @ mobility_skill_self_escape @ accepted_20260514_002741.jsonl_seed_master_0111
        aoe_skill_center_selection [66.7%(8%) / 2]
          3-1-12-4-10-1 @ "A_06, 적들이 뭉친 쪽에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260514_002741.jsonl_seed_master_0055, accepted_20260514_002741.jsonl_seed_master_0109
      empty_action_expected [25.0%(10%) / 1]
        actor_has_no_skill [100.0%(8%) / 1]
          3-1-12-13-11-1 @ "A_03, 지금 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0176
  explicit_multi_actor [13.8%(10%) / 8]
    explicit_enemy_target [37.5%(26%) / 3]
      multi_actor_same_target [66.7%(7%) / 2]
        enemy_skill_valid_target [50.0%(10%) / 1]
          3-2-1-11-1-1 @ "A_03과 A_06은 E_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0177
        aoe_skill_center_selection [50.0%(8%) / 1]
          3-2-1-11-10-1 @ "A_03과 A_06은 E_02 주변에 스킬을 써." @ 1 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0178
      multi_actor_different_targets [33.3%(3%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          3-2-1-12-1-1 @ "A_03은 E_01에게, A_06은 E_03에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0179
    explicit_ally_target [25.0%(22%) / 2]
      multi_actor_same_target [50.0%(7%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-2-2-11-2-1 @ "A_04와 A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0180
      multi_actor_different_targets [50.0%(3%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-2-2-12-2-1 @ "A_04는 A_01에게, A_05는 A_02에게 스킬을 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0181
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [12.5%(8%) / 1]
      multi_actor_different_targets [100.0%(3%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          3-2-6-12-1-1 @ "A_03은 적 전열에, A_06은 적 후열에 스킬을 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0182
    low_hp_ally [12.5%(10%) / 1]
      multi_actor_same_target [100.0%(7%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-2-9-11-2-1 @ "A_04와 A_05는 체력이 제일 낮은 아군에게 스킬을 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0183
    invalid_explicit_target [0.0%(13%) / 0]
    none [12.5%(8%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          3-2-12-13-13-1 @ "A_03과 A_04는 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002743.jsonl_seed_master_0184
  global_condition [3.4%(10%) / 2]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [50.0%(8%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          3-3-4-4-1-1 @ "스킬 쓸 수 있는 아군은 체력 낮은 적에게 스킬 써." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0185
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [50.0%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-3-9-4-2-1 @ "회복 가능한 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0186
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
          3-4-6-4-1-1 @ "원거리 아군은 적 후열에 스킬을 써." @ 1 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260514_002741.jsonl_seed_master_0058
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_state_based [3.4%(10%) / 2]
    explicit_enemy_target [50.0%(26%) / 1]
      skill_only [100.0%(70%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          3-5-1-4-1-1 @ "스킬을 쓰기 안전한 아군은 E_02에게 스킬 써." @ 1 @ healthy_actor_selection @ accepted_20260514_002743.jsonl_seed_master_0187
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [50.0%(10%) / 1]
      skill_only [100.0%(70%) / 1]
        ally_skill_valid_target [100.0%(10%) / 1]
          3-5-9-4-2-1 @ "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ low_hp_ally_target @ accepted_20260514_002741.jsonl_seed_master_0059
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  no_valid_actor [5.2%(5%) / 3]
    explicit_enemy_target [33.3%(26%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          3-6-1-13-13-1 @ "스킬 가능한 아군은 E_02에게 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002741.jsonl_seed_master_0060
    explicit_ally_target [33.3%(22%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_target [100.0%(4%) / 1]
          3-6-2-13-14-1 @ "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 1 @ no_valid_skill_target @ accepted_20260514_002741.jsonl_seed_master_0061
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [33.3%(8%) / 1]
      empty_action_expected [100.0%(10%) / 1]
        no_valid_skill_actor [100.0%(4%) / 1]
          3-6-12-13-13-1 @ "스킬 가능한 아군은 지금 스킬 써." @ 1 @ no_valid_skill_actor @ accepted_20260514_002743.jsonl_seed_master_0188

skillControl [2.1%(8%) / 13]
  explicit_actor [46.2%(70%) / 6]
    none [100.0%(100%) / 6]
      skillControl_defer [33.3%(55%) / 2]
        explicit_defer_skill [50.0%(25%) / 1]
          4-1-12-9-1-1 @ "A_03, 스킬은 아직 쓰지 말고 5초 후로 미뤄." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0062
        defer_without_duration [50.0%(15%) / 1]
          4-1-12-9-2-1 @ "A_03, 스킬은 좀 아껴." @ 1 @ skillControl_duration_unspecified @ accepted_20260514_002741.jsonl_seed_master_0063
      skillControl_forbid [50.0%(35%) / 3]
        explicit_forbid_skill [33.3%(25%) / 1]
          4-1-12-10-3-1 @ "A_03, 지금은 스킬 쓰지 마." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0064
        forbid_without_duration [33.3%(10%) / 1]
          4-1-12-10-4-1 @ "A_03, 스킬 쓰지 말고 있어." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0065
        actor_has_no_skill [33.3%(5%) / 1]
          4-1-12-10-7-1 @ "A_03, 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002741.jsonl_seed_master_0066
      empty_action_expected [16.7%(10%) / 1]
        selected_actor_dead [100.0%(5%) / 1]
          4-1-12-13-8-1 @ "A_03, 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0189
  explicit_multi_actor [30.8%(20%) / 4]
    none [100.0%(100%) / 4]
      skillControl_defer [25.0%(55%) / 1]
        multi_actor_defer_skill [100.0%(10%) / 1]
          4-2-12-9-5-1 @ "A_03과 A_04는 스킬을 아껴." @ 1 @ multi_actor_skillControl @ accepted_20260514_002741.jsonl_seed_master_0067
      skillControl_forbid [25.0%(35%) / 1]
        multi_actor_forbid_skill [100.0%(5%) / 1]
          4-2-12-10-6-1 @ "A_03과 A_04는 지금 스킬 쓰지 마." @ 1 @ multi_actor_skillControl @ accepted_20260514_002741.jsonl_seed_master_0068
      empty_action_expected [50.0%(10%) / 2]
        actor_has_no_skill [50.0%(5%) / 1]
          4-2-12-13-7-1 @ "A_03과 A_04는 지금 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0191
        selected_actor_dead [50.0%(5%) / 1]
          4-2-12-13-8-1 @ "A_03과 A_04는 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0190
  no_valid_actor [23.1%(10%) / 3]
    none [100.0%(100%) / 3]
      empty_action_expected [100.0%(10%) / 3]
        actor_has_no_skill [33.3%(5%) / 1]
          4-6-12-13-7-1 @ "스킬이 없는 A_03은 지금 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0193
        selected_actor_dead [66.7%(5%) / 2]
          4-6-12-13-8-1 @ "A_03, 스킬 쓰지 마." @ 1 @ named_actor_dead @ accepted_20260514_002741.jsonl_seed_master_0069
          4-6-12-13-8-2 @ "A_03, 스킬 쓰지 말고 있어." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0192

wait [2.5%(8%) / 15]
  explicit_actor [60.0%(60%) / 9]
    explicit_enemy_target [33.3%(10%) / 3]
      wait_only [33.3%(65%) / 1]
        explicit_wait [100.0%(25%) / 1]
          5-1-1-6-1-1 @ "A_04, E_02를 보면서 잠깐 대기해." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0196
      wait_then_attack [66.7%(20%) / 2]
        wait_then_attack_valid [100.0%(15%) / 2]
          5-1-1-7-3-1 @ "A_04, 3초 뒤에 E_02를 공격해." @ 2 @ explicit_wait_duration, wait_then_attack @ accepted_20260514_002743.jsonl_seed_master_0194, accepted_20260514_002743.jsonl_seed_master_0195
    none [66.7%(90%) / 6]
      wait_only [50.0%(65%) / 3]
        explicit_wait [33.3%(25%) / 1]
          5-1-12-6-1-1 @ "A_04, 지금 자리에서 대기해." @ 1 @ [] @ accepted_20260514_002741.jsonl_seed_master_0070
        explicit_wait_duration [33.3%(20%) / 1]
          5-1-12-6-2-1 @ "A_04, 5초만 기다려." @ 1 @ explicit_wait_duration @ accepted_20260514_002741.jsonl_seed_master_0071
        hold_position_wait [33.3%(10%) / 1]
          5-1-12-6-5-1 @ "A_04, 위치 유지하면서 잠깐 버텨." @ 1 @ hold_front_requested @ accepted_20260514_002741.jsonl_seed_master_0072
      wait_then_attack [16.7%(20%) / 1]
        wait_then_attack_valid [100.0%(15%) / 1]
          5-1-12-7-3-1 @ "A_04, 3초 기다렸다가 E_02를 공격해." @ 1 @ wait_then_attack @ accepted_20260514_002741.jsonl_seed_master_0073
      wait_then_skill [16.7%(10%) / 1]
        wait_then_skill_valid [100.0%(10%) / 1]
          5-1-12-8-4-1 @ "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260514_002741.jsonl_seed_master_0074
      empty_action_expected [16.7%(5%) / 1]
        selected_actor_dead [100.0%(6%) / 1]
          5-1-12-13-8-1 @ "A_04, 지금 자리에서 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0198
  explicit_multi_actor [20.0%(15%) / 3]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 3]
      wait_only [33.3%(65%) / 1]
        multi_actor_wait [100.0%(8%) / 1]
          5-2-12-6-6-1 @ "A_03과 A_04는 잠깐 대기해." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0199
      wait_then_attack [33.3%(20%) / 1]
        wait_then_attack_valid [100.0%(15%) / 1]
          5-2-12-7-3-1 @ "A_03과 A_04는 잠깐 기다렸다가 공격해." @ 1 @ wait_then_attack @ accepted_20260514_002743.jsonl_seed_master_0200
      empty_action_expected [33.3%(5%) / 1]
        selected_actor_dead [100.0%(6%) / 1]
          5-2-12-13-8-1 @ "A_03과 A_04는 잠깐 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002743.jsonl_seed_master_0202
  global_condition [6.7%(15%) / 1]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 1]
      wait_only [100.0%(65%) / 1]
        hold_position_wait [100.0%(10%) / 1]
          5-3-12-6-5-1 @ "위험한 아군은 잠깐 대기하면서 버텨." @ 1 @ [] @ accepted_20260514_002743.jsonl_seed_master_0203
  no_valid_actor [13.3%(10%) / 2]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 2]
      empty_action_expected [100.0%(5%) / 2]
        no_matching_wait_actor [50.0%(6%) / 1]
          5-6-12-13-7-1 @ "체력이 낮은 아군은 잠깐 대기해." @ 1 @ no_matching_actor @ accepted_20260514_002741.jsonl_seed_master_0077
        selected_actor_dead [50.0%(6%) / 1]
          5-6-12-13-8-1 @ "A_04, 지금 자리에서 대기해." @ 1 @ named_actor_dead @ accepted_20260514_002741.jsonl_seed_master_0078

empty [3.8%(12%) / 23]
  explicit_actor [43.5%(30%) / 10]
    explicit_enemy_target [50.0%(20%) / 5]
      empty_action_expected [100.0%(100%) / 5]
        named_actor_dead [20.0%(12%) / 1]
          6-1-1-13-1-1 @ "A_01, E_02를 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0205
        named_target_dead [20.0%(10%) / 1]
          6-1-1-13-3-1 @ "A_01, E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260514_002741.jsonl_seed_master_0081
        named_target_untargetable [20.0%(10%) / 1]
          6-1-1-13-4-1 @ "A_01, E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260514_002741.jsonl_seed_master_0082
        actor_outside_allowedActors [20.0%(8%) / 1]
          6-1-1-13-5-1 @ "A_01, E_02를 공격해." @ 1 @ actor_outside_allowedActors @ accepted_20260514_002741.jsonl_seed_master_0080
        attack_target_outside_allowedTargets [20.0%(8%) / 1]
          6-1-1-13-6-1 @ "A_01, E_02를 공격해." @ 1 @ attack_target_outside_allowedTargets @ accepted_20260514_002741.jsonl_seed_master_0083
    explicit_ally_target [10.0%(15%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_target_dead_not_allowed [100.0%(8%) / 1]
          6-1-2-13-8-1 @ "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0084
    invalid_explicit_target [20.0%(30%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        move_to_self_attempt [50.0%(6%) / 1]
          6-1-11-13-7-1 @ "A_02, 네 위치로 다시 붙어." @ 1 @ move_to_self_attempt @ accepted_20260514_002741.jsonl_seed_master_0085
        skill_actor_has_no_skill [50.0%(8%) / 1]
          6-1-11-13-9-1 @ "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002741.jsonl_seed_master_0086
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [20.0%(20%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        named_actor_dead [50.0%(12%) / 1]
          6-1-12-13-1-1 @ "A_01, 지금 공격할 수 있는 적을 찾아 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0206
        no_valid_target [50.0%(8%) / 1]
          6-1-12-13-12-1 @ "A_01, 지금 공격할 수 있는 적을 공격해." @ 1 @ no_valid_target @ accepted_20260514_002745.jsonl_seed_master_0207
  explicit_multi_actor [21.7%(10%) / 5]
    explicit_enemy_target [80.0%(20%) / 4]
      empty_action_expected [100.0%(100%) / 4]
        all_named_actors_dead [25.0%(6%) / 1]
          6-2-1-13-2-1 @ "A_01과 A_02는 E_02를 공격해." @ 1 @ all_named_actors_dead @ accepted_20260514_002741.jsonl_seed_master_0087
        named_target_dead [25.0%(10%) / 1]
          6-2-1-13-3-1 @ "A_01과 A_02는 E_02를 공격해." @ 1 @ named_target_dead @ accepted_20260514_002745.jsonl_seed_master_0209
        named_target_untargetable [25.0%(10%) / 1]
          6-2-1-13-4-1 @ "A_01과 A_02는 E_02를 공격해." @ 1 @ named_target_untargetable @ accepted_20260514_002745.jsonl_seed_master_0210
        attack_target_outside_allowedTargets [25.0%(8%) / 1]
          6-2-1-13-6-1 @ "A_01과 A_02는 E_02를 공격해." @ 1 @ attack_target_outside_allowedTargets @ accepted_20260514_002745.jsonl_seed_master_0208
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [20.0%(30%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_actor_has_no_skill [100.0%(8%) / 1]
          6-2-11-13-9-1 @ "A_03과 A_04는 죽은 E_02한테 스킬 써." @ 1 @ actor_has_no_skill, named_target_dead @ accepted_20260514_002745.jsonl_seed_master_0211
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
          6-3-9-13-10-1 @ "체력이 낮은 아군을 도울 수 있는 아군은 붙어." @ 1 @ no_matching_actor, low_hp_ally_target @ accepted_20260514_002745.jsonl_seed_master_0212
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          6-3-12-13-10-1 @ "체력이 낮은 아군은 뒤로 빠져." @ 1 @ no_matching_actor @ accepted_20260514_002741.jsonl_seed_master_0088
  global_role_based [8.7%(15%) / 2]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_role_actor [100.0%(6%) / 1]
          6-4-6-13-11-1 @ "원거리 아군은 적 후열을 공격해." @ 1 @ no_matching_role_actor @ accepted_20260514_002741.jsonl_seed_master_0089
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_role_actor [100.0%(6%) / 1]
          6-4-12-13-11-1 @ "전열 아군은 앞으로 버텨." @ 1 @ no_matching_role_actor @ accepted_20260514_002745.jsonl_seed_master_0213
  global_state_based [8.7%(10%) / 2]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_valid_target [100.0%(8%) / 1]
          6-5-6-13-12-1 @ "공격 가능한 아군은 적 후열을 공격해." @ 1 @ no_valid_target, target_role_backline_enemy @ accepted_20260514_002745.jsonl_seed_master_0214
    lowest_hp_enemy [50.0%(5%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_valid_target [100.0%(8%) / 1]
          6-5-4-13-12-1 @ "공격 가능한 아군은 체력이 제일 낮은 적을 공격해." @ 1 @ no_valid_target @ accepted_20260514_002741.jsonl_seed_master_0090
    none [0.0%(20%) / 0]
  no_valid_actor [8.7%(10%) / 2]
    explicit_enemy_target [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        named_actor_dead [100.0%(12%) / 1]
          6-6-1-13-1-1 @ "A_01, E_02를 공격해." @ 1 @ named_actor_dead @ accepted_20260514_002745.jsonl_seed_master_0215
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [50.0%(20%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        no_matching_actor [100.0%(10%) / 1]
          6-6-12-13-10-1 @ "살아있는 아군은 전부 후퇴해." @ 1 @ no_valid_actor @ accepted_20260514_002741.jsonl_seed_master_0091
