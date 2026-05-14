# General Coverage

attack [21.5%(24%) / 408]
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

move [22.7%(22%) / 432]
  explicit_actor [55.6%(45%) / 240]
    explicit_ally_target [39.2%(22%) / 94]
      move_only [53.2%(55%) / 50]
        move_to_alive_ally [84.0%(10%) / 42]
          2-1-2-2-1-1 @ "A_02, A_04에게 이동해." @ 42 @ [] @ accepted_20260514_002649.jsonl_seed_master_0004, accepted_20260514_115253.jsonl_batch_0066_001, accepted_20260514_115253.jsonl_batch_0066_002, accepted_20260514_115253.jsonl_batch_0066_003, accepted_20260514_115253.jsonl_batch_0066_004, accepted_20260514_115253.jsonl_batch_0066_005, accepted_20260514_115253.jsonl_batch_0066_006, accepted_20260514_115253.jsonl_batch_0066_007, accepted_20260514_115253.jsonl_batch_0066_008, accepted_20260514_115253.jsonl_batch_0066_009, accepted_20260514_115253.jsonl_batch_0066_010, accepted_20260514_120446.jsonl_batch_0067_001, accepted_20260514_120446.jsonl_batch_0067_002, accepted_20260514_120446.jsonl_batch_0067_003, accepted_20260514_120446.jsonl_batch_0067_004, accepted_20260514_120446.jsonl_batch_0067_005, accepted_20260514_120446.jsonl_batch_0067_006, accepted_20260514_120446.jsonl_batch_0067_007, accepted_20260514_120446.jsonl_batch_0067_008, accepted_20260514_120446.jsonl_batch_0067_009, accepted_20260514_120446.jsonl_batch_0067_010, accepted_20260514_121642.jsonl_batch_0068_001, accepted_20260514_121642.jsonl_batch_0068_002, accepted_20260514_121642.jsonl_batch_0068_003, accepted_20260514_121642.jsonl_batch_0068_004, accepted_20260514_121642.jsonl_batch_0068_005, accepted_20260514_121642.jsonl_batch_0068_006, accepted_20260514_121642.jsonl_batch_0068_007, accepted_20260514_121642.jsonl_batch_0068_008, accepted_20260514_121642.jsonl_batch_0068_009, accepted_20260514_121642.jsonl_batch_0068_010, accepted_20260514_122845.jsonl_batch_0069_001, accepted_20260514_122845.jsonl_batch_0069_002, accepted_20260514_122845.jsonl_batch_0069_003, accepted_20260514_122845.jsonl_batch_0069_004, accepted_20260514_122845.jsonl_batch_0069_005, accepted_20260514_122845.jsonl_batch_0069_006, accepted_20260514_122845.jsonl_batch_0069_007, accepted_20260514_122845.jsonl_batch_0069_008, accepted_20260514_122845.jsonl_batch_0069_009, accepted_20260514_122845.jsonl_batch_0069_010, accepted_20260514_123001.jsonl_batch_0070_001
        move_to_dead_ally [2.0%(5%) / 1]
          2-1-2-2-2-1 @ "A_02, A_04에게 이동해." @ 1 @ named_target_dead @ accepted_20260514_002740.jsonl_seed_master_0028
        help_ally [6.0%(10%) / 3]
          2-1-2-2-8-1 @ "A_02, A_04 근처로 가." @ 3 @ [] @ accepted_20260514_002740.jsonl_seed_master_0030, accepted_20260514_123934.jsonl_batch_0072_001, accepted_20260514_123934.jsonl_batch_0072_002
        move_to_self_attempt [8.0%(5%) / 4]
          2-1-2-2-11-1 @ "A_02, 네 위치로 다시 붙어." @ 4 @ move_to_self_attempt @ accepted_20260514_002740.jsonl_seed_master_0029, accepted_20260514_124259.jsonl_batch_0073_001, accepted_20260514_124259.jsonl_batch_0073_002, accepted_20260514_124259.jsonl_batch_0073_003
      move_then_attack [40.4%(20%) / 38]
        help_ally [100.0%(10%) / 38]
          2-1-2-3-8-1 @ "A_02, A_04 근처로 가서 주변 적을 공격해." @ 38 @ help_ally_then_attack @ accepted_20260514_002740.jsonl_seed_master_0031, accepted_20260514_125535.jsonl_batch_0074_001, accepted_20260514_125535.jsonl_batch_0074_002, accepted_20260514_125535.jsonl_batch_0074_003, accepted_20260514_125535.jsonl_batch_0074_004, accepted_20260514_125535.jsonl_batch_0074_005, accepted_20260514_125535.jsonl_batch_0074_006, accepted_20260514_125535.jsonl_batch_0074_007, accepted_20260514_125535.jsonl_batch_0074_008, accepted_20260514_125535.jsonl_batch_0074_009, accepted_20260514_125535.jsonl_batch_0074_010, accepted_20260514_133938.jsonl_batch_0075_001, accepted_20260514_133938.jsonl_batch_0075_002, accepted_20260514_133938.jsonl_batch_0075_003, accepted_20260514_133938.jsonl_batch_0075_004, accepted_20260514_133938.jsonl_batch_0075_005, accepted_20260514_133938.jsonl_batch_0075_006, accepted_20260514_133938.jsonl_batch_0075_007, accepted_20260514_133938.jsonl_batch_0075_008, accepted_20260514_133938.jsonl_batch_0075_009, accepted_20260514_133938.jsonl_batch_0075_010, accepted_20260514_135211.jsonl_batch_0076_001, accepted_20260514_135211.jsonl_batch_0076_002, accepted_20260514_135211.jsonl_batch_0076_003, accepted_20260514_135211.jsonl_batch_0076_004, accepted_20260514_135211.jsonl_batch_0076_005, accepted_20260514_135211.jsonl_batch_0076_006, accepted_20260514_135211.jsonl_batch_0076_007, accepted_20260514_135211.jsonl_batch_0076_008, accepted_20260514_135211.jsonl_batch_0076_009, accepted_20260514_135211.jsonl_batch_0076_010, accepted_20260514_140059.jsonl_batch_0077_001, accepted_20260514_140059.jsonl_batch_0077_002, accepted_20260514_140059.jsonl_batch_0077_003, accepted_20260514_140059.jsonl_batch_0077_004, accepted_20260514_140059.jsonl_batch_0077_005, accepted_20260514_140059.jsonl_batch_0077_006, accepted_20260514_140059.jsonl_batch_0077_007
      empty_action_expected [6.4%(10%) / 6]
        move_to_self_attempt [100.0%(5%) / 6]
          2-1-2-13-11-1 @ "A_02, A_02에게 이동해." @ 6 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0141, accepted_20260514_140634.jsonl_batch_0078_001, accepted_20260514_140634.jsonl_batch_0078_002, accepted_20260514_140634.jsonl_batch_0078_003, accepted_20260514_140634.jsonl_batch_0078_004, accepted_20260514_140634.jsonl_batch_0078_005
    explicit_enemy_target [23.3%(18%) / 56]
      move_only [51.8%(55%) / 29]
        approach_enemy_only [100.0%(10%) / 29]
          2-1-1-2-3-1 @ "A_01, E_02에게 접근해." @ 29 @ [] @ accepted_20260514_002740.jsonl_seed_master_0032, accepted_20260514_141836.jsonl_batch_0079_001, accepted_20260514_141836.jsonl_batch_0079_002, accepted_20260514_141836.jsonl_batch_0079_003, accepted_20260514_141836.jsonl_batch_0079_004, accepted_20260514_141836.jsonl_batch_0079_005, accepted_20260514_141836.jsonl_batch_0079_006, accepted_20260514_141836.jsonl_batch_0079_007, accepted_20260514_141836.jsonl_batch_0079_008, accepted_20260514_141836.jsonl_batch_0079_009, accepted_20260514_141836.jsonl_batch_0079_010, accepted_20260514_143039.jsonl_batch_0080_001, accepted_20260514_143039.jsonl_batch_0080_002, accepted_20260514_143039.jsonl_batch_0080_003, accepted_20260514_143039.jsonl_batch_0080_004, accepted_20260514_143039.jsonl_batch_0080_005, accepted_20260514_143039.jsonl_batch_0080_006, accepted_20260514_143039.jsonl_batch_0080_007, accepted_20260514_143039.jsonl_batch_0080_008, accepted_20260514_143039.jsonl_batch_0080_009, accepted_20260514_143039.jsonl_batch_0080_010, accepted_20260514_144009.jsonl_batch_0081_001, accepted_20260514_144009.jsonl_batch_0081_002, accepted_20260514_144009.jsonl_batch_0081_003, accepted_20260514_144009.jsonl_batch_0081_004, accepted_20260514_144009.jsonl_batch_0081_005, accepted_20260514_144009.jsonl_batch_0081_006, accepted_20260514_144009.jsonl_batch_0081_007, accepted_20260514_144009.jsonl_batch_0081_008
      move_then_attack [48.2%(20%) / 27]
        approach_enemy_then_attack [55.6%(10%) / 15]
          2-1-1-3-4-1 @ "A_01, E_02에게 접근해서 공격해." @ 15 @ [] @ accepted_20260514_002740.jsonl_seed_master_0033, accepted_20260514_145215.jsonl_batch_0082_001, accepted_20260514_145215.jsonl_batch_0082_002, accepted_20260514_145215.jsonl_batch_0082_003, accepted_20260514_145215.jsonl_batch_0082_004, accepted_20260514_145215.jsonl_batch_0082_005, accepted_20260514_145215.jsonl_batch_0082_006, accepted_20260514_145215.jsonl_batch_0082_007, accepted_20260514_145215.jsonl_batch_0082_008, accepted_20260514_145215.jsonl_batch_0082_009, accepted_20260514_145215.jsonl_batch_0082_010, accepted_20260514_145708.jsonl_batch_0083_001, accepted_20260514_145708.jsonl_batch_0083_002, accepted_20260514_145708.jsonl_batch_0083_003, accepted_20260514_145708.jsonl_batch_0083_004
        flank_enemy_then_attack [44.4%(8%) / 12]
          2-1-1-3-5-1 @ "A_01, E_02 뒤쪽으로 돌아가서 공격해." @ 12 @ flank_requested @ accepted_20260514_002740.jsonl_seed_master_0034, accepted_20260514_150925.jsonl_batch_0084_001, accepted_20260514_150925.jsonl_batch_0084_002, accepted_20260514_150925.jsonl_batch_0084_003, accepted_20260514_150925.jsonl_batch_0084_004, accepted_20260514_150925.jsonl_batch_0084_005, accepted_20260514_150925.jsonl_batch_0084_006, accepted_20260514_150925.jsonl_batch_0084_007, accepted_20260514_150925.jsonl_batch_0084_008, accepted_20260514_150925.jsonl_batch_0084_009, accepted_20260514_150925.jsonl_batch_0084_010, accepted_20260514_151043.jsonl_batch_0085_001
    safe_ally [2.5%(16%) / 6]
      move_only [66.7%(55%) / 4]
        retreat_to_backline_ally [50.0%(12%) / 2]
          2-1-8-2-6-1 @ "A_01, 아군 뒤쪽으로 빠져." @ 2 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0035, accepted_20260514_151200.jsonl_batch_0086_001
        low_hp_actor_escape [50.0%(10%) / 2]
          2-1-8-2-7-1 @ "A_01, 체력이 낮으니 안전한 아군 쪽으로 빠져." @ 2 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0142, accepted_20260514_151318.jsonl_batch_0087_001
      empty_action_expected [33.3%(10%) / 2]
        no_matching_actor [100.0%(5%) / 2]
          2-1-8-13-12-1 @ "A_01, 안전한 아군 쪽으로 빠져." @ 2 @ no_matching_actor, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0143, accepted_20260514_151427.jsonl_batch_0088_001
    low_hp_ally [1.7%(12%) / 4]
      move_only [50.0%(55%) / 2]
        support_low_hp_ally [100.0%(8%) / 2]
          2-1-9-2-9-1 @ "A_01, 체력이 낮은 아군에게 붙어." @ 2 @ low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0036, accepted_20260514_151544.jsonl_batch_0089_001
      move_then_attack [50.0%(20%) / 2]
        support_low_hp_ally [100.0%(8%) / 2]
          2-1-9-3-9-1 @ "A_01, 체력이 낮은 아군에게 붙어서 주변 적을 공격해." @ 2 @ low_hp_ally_target, help_ally_then_attack @ accepted_20260514_002742.jsonl_seed_master_0144, accepted_20260514_151702.jsonl_batch_0090_001
    backline_ally [12.9%(10%) / 31]
      move_only [100.0%(55%) / 31]
        retreat_to_backline_ally [35.5%(12%) / 11]
          2-1-10-2-6-1 @ "A_01, 후열 아군 쪽으로 빠져." @ 11 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0145, accepted_20260514_152850.jsonl_batch_0091_001, accepted_20260514_152850.jsonl_batch_0091_002, accepted_20260514_152850.jsonl_batch_0091_003, accepted_20260514_152850.jsonl_batch_0091_004, accepted_20260514_152850.jsonl_batch_0091_005, accepted_20260514_152850.jsonl_batch_0091_006, accepted_20260514_152850.jsonl_batch_0091_007, accepted_20260514_152850.jsonl_batch_0091_008, accepted_20260514_152850.jsonl_batch_0091_009, accepted_20260514_152850.jsonl_batch_0091_010
        low_hp_actor_escape [64.5%(10%) / 20]
          2-1-10-2-7-1 @ "A_01, 체력이 낮으니까 후열 아군 쪽으로 빠져." @ 20 @ low_hp_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0146, accepted_20260514_154457.jsonl_batch_0092_001, accepted_20260514_154457.jsonl_batch_0092_002, accepted_20260514_154457.jsonl_batch_0092_003, accepted_20260514_154457.jsonl_batch_0092_004, accepted_20260514_154457.jsonl_batch_0092_005, accepted_20260514_154457.jsonl_batch_0092_006, accepted_20260514_154457.jsonl_batch_0092_007, accepted_20260514_154457.jsonl_batch_0092_008, accepted_20260514_154457.jsonl_batch_0092_009, accepted_20260514_154457.jsonl_batch_0092_010, accepted_20260514_155625.jsonl_batch_0093_001, accepted_20260514_155625.jsonl_batch_0093_002, accepted_20260514_155625.jsonl_batch_0093_003, accepted_20260514_155625.jsonl_batch_0093_004, accepted_20260514_155625.jsonl_batch_0093_005, accepted_20260514_155625.jsonl_batch_0093_006, accepted_20260514_155625.jsonl_batch_0093_007, accepted_20260514_155625.jsonl_batch_0093_008, accepted_20260514_155625.jsonl_batch_0093_009
    role_based_enemy [10.0%(5%) / 24]
      move_only [62.5%(55%) / 15]
        approach_enemy_only [100.0%(10%) / 15]
          2-1-6-2-3-1 @ "A_01, 적 후열 쪽으로 이동해." @ 15 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0149, accepted_20260514_160819.jsonl_batch_0094_001, accepted_20260514_160819.jsonl_batch_0094_002, accepted_20260514_160819.jsonl_batch_0094_003, accepted_20260514_160819.jsonl_batch_0094_004, accepted_20260514_160819.jsonl_batch_0094_005, accepted_20260514_160819.jsonl_batch_0094_006, accepted_20260514_160819.jsonl_batch_0094_007, accepted_20260514_160819.jsonl_batch_0094_008, accepted_20260514_160819.jsonl_batch_0094_009, accepted_20260514_160819.jsonl_batch_0094_010, accepted_20260514_161310.jsonl_batch_0095_001, accepted_20260514_161310.jsonl_batch_0095_002, accepted_20260514_161310.jsonl_batch_0095_003, accepted_20260514_161310.jsonl_batch_0095_004
      move_then_attack [37.5%(20%) / 9]
        approach_enemy_then_attack [88.9%(10%) / 8]
          2-1-6-3-4-1 @ "A_01, 적 후열에 접근해서 공격해." @ 8 @ target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0148, accepted_20260514_162136.jsonl_batch_0096_001, accepted_20260514_162136.jsonl_batch_0096_002, accepted_20260514_162136.jsonl_batch_0096_003, accepted_20260514_162136.jsonl_batch_0096_004, accepted_20260514_162136.jsonl_batch_0096_005, accepted_20260514_162136.jsonl_batch_0096_006, accepted_20260514_162136.jsonl_batch_0096_007
        flank_enemy_then_attack [11.1%(8%) / 1]
          2-1-6-3-5-1 @ "A_01, 적 후열 쪽으로 돌아가서 공격해." @ 1 @ flank_requested, target_role_backline_enemy @ accepted_20260514_002742.jsonl_seed_master_0147
    invalid_explicit_target [10.0%(7%) / 24]
      empty_action_expected [100.0%(10%) / 24]
        move_to_dead_ally [70.8%(5%) / 17]
          2-1-11-13-2-1 @ "A_02, 쓰러진 A_04에게 이동해." @ 17 @ named_target_dead @ accepted_20260514_002742.jsonl_seed_master_0150, accepted_20260514_163929.jsonl_batch_0098_001, accepted_20260514_163929.jsonl_batch_0098_002, accepted_20260514_163929.jsonl_batch_0098_003, accepted_20260514_163929.jsonl_batch_0098_004, accepted_20260514_163929.jsonl_batch_0098_005, accepted_20260514_163929.jsonl_batch_0098_006, accepted_20260514_163929.jsonl_batch_0098_007, accepted_20260514_163929.jsonl_batch_0098_008, accepted_20260514_163929.jsonl_batch_0098_009, accepted_20260514_163929.jsonl_batch_0098_010, accepted_20260514_164608.jsonl_batch_0099_001, accepted_20260514_164608.jsonl_batch_0099_002, accepted_20260514_164608.jsonl_batch_0099_003, accepted_20260514_164608.jsonl_batch_0099_004, accepted_20260514_164608.jsonl_batch_0099_005, accepted_20260514_164608.jsonl_batch_0099_006
        move_to_self_attempt [29.2%(5%) / 7]
          2-1-11-13-11-1 @ "A_02, 네 위치로 다시 붙어." @ 7 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0151, accepted_20260514_165257.jsonl_batch_0100_001, accepted_20260514_165257.jsonl_batch_0100_002, accepted_20260514_165257.jsonl_batch_0100_003, accepted_20260514_165257.jsonl_batch_0100_004, accepted_20260514_165257.jsonl_batch_0100_005, accepted_20260514_165257.jsonl_batch_0100_006
    none [0.4%(10%) / 1]
      move_only [100.0%(55%) / 1]
        hold_front [100.0%(7%) / 1]
          2-1-12-2-10-1 @ "A_01, 전열을 유지해." @ 1 @ hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0037
  explicit_multi_actor [15.0%(10%) / 65]
    explicit_ally_target [6.2%(22%) / 4]
      move_only [100.0%(55%) / 4]
        help_ally [100.0%(10%) / 4]
          2-2-2-2-8-1 @ "A_01과 A_02는 A_04 근처로 이동해." @ 4 @ [] @ accepted_20260514_002742.jsonl_seed_master_0152, accepted_20260514_165804.jsonl_batch_0102_001, accepted_20260514_165804.jsonl_batch_0102_002, accepted_20260514_165804.jsonl_batch_0102_003
    explicit_enemy_target [64.6%(18%) / 42]
      move_then_attack [100.0%(20%) / 42]
        approach_enemy_then_attack [54.8%(10%) / 23]
          2-2-1-3-4-1 @ "A_01과 A_02는 E_02에게 접근해서 공격해." @ 23 @ [] @ accepted_20260514_002742.jsonl_seed_master_0153, accepted_20260514_171059.jsonl_batch_0103_001, accepted_20260514_171059.jsonl_batch_0103_002, accepted_20260514_171059.jsonl_batch_0103_003, accepted_20260514_171059.jsonl_batch_0103_004, accepted_20260514_171059.jsonl_batch_0103_005, accepted_20260514_171059.jsonl_batch_0103_006, accepted_20260514_171059.jsonl_batch_0103_007, accepted_20260514_171059.jsonl_batch_0103_008, accepted_20260514_171059.jsonl_batch_0103_009, accepted_20260514_171059.jsonl_batch_0103_010, accepted_20260514_172346.jsonl_batch_0104_001, accepted_20260514_172346.jsonl_batch_0104_002, accepted_20260514_172346.jsonl_batch_0104_003, accepted_20260514_172346.jsonl_batch_0104_004, accepted_20260514_172346.jsonl_batch_0104_005, accepted_20260514_172346.jsonl_batch_0104_006, accepted_20260514_172346.jsonl_batch_0104_007, accepted_20260514_172346.jsonl_batch_0104_008, accepted_20260514_172346.jsonl_batch_0104_009, accepted_20260514_172346.jsonl_batch_0104_010, accepted_20260514_172623.jsonl_batch_0105_001, accepted_20260514_172623.jsonl_batch_0105_002
        flank_enemy_then_attack [45.2%(8%) / 19]
          2-2-1-3-5-1 @ "A_01과 A_02는 E_02 뒤쪽으로 돌아가서 공격해." @ 19 @ flank_requested @ accepted_20260514_002742.jsonl_seed_master_0154, accepted_20260514_173929.jsonl_batch_0106_001, accepted_20260514_173929.jsonl_batch_0106_002, accepted_20260514_173929.jsonl_batch_0106_003, accepted_20260514_173929.jsonl_batch_0106_004, accepted_20260514_173929.jsonl_batch_0106_005, accepted_20260514_173929.jsonl_batch_0106_006, accepted_20260514_173929.jsonl_batch_0106_007, accepted_20260514_173929.jsonl_batch_0106_008, accepted_20260514_173929.jsonl_batch_0106_009, accepted_20260514_173929.jsonl_batch_0106_010, accepted_20260514_174954.jsonl_batch_0107_001, accepted_20260514_174954.jsonl_batch_0107_002, accepted_20260514_174954.jsonl_batch_0107_003, accepted_20260514_174954.jsonl_batch_0107_004, accepted_20260514_174954.jsonl_batch_0107_005, accepted_20260514_174954.jsonl_batch_0107_006, accepted_20260514_174954.jsonl_batch_0107_007, accepted_20260514_174954.jsonl_batch_0107_008
    safe_ally [6.2%(16%) / 4]
      move_only [50.0%(55%) / 2]
        retreat_to_backline_ally [100.0%(12%) / 2]
          2-2-8-2-6-1 @ "A_01, A_02는 뒤로 빠져." @ 2 @ retreat_to_safe_ally @ accepted_20260514_002740.jsonl_seed_master_0038, accepted_20260514_175114.jsonl_batch_0108_001
      move_then_attack [50.0%(20%) / 2]
        retreat_to_backline_ally [100.0%(12%) / 2]
          2-2-8-3-6-1 @ "A_01과 A_02는 뒤로 빠졌다가 가까운 적을 공격해." @ 2 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0155, accepted_20260514_175238.jsonl_batch_0109_001
    low_hp_ally [3.1%(12%) / 2]
      move_only [100.0%(55%) / 2]
        support_low_hp_ally [100.0%(8%) / 2]
          2-2-9-2-9-1 @ "A_01과 A_02는 체력이 낮은 아군에게 붙어." @ 2 @ low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0156, accepted_20260514_175359.jsonl_batch_0110_001
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [16.9%(7%) / 11]
      empty_action_expected [100.0%(10%) / 11]
        move_to_self_attempt [100.0%(5%) / 11]
          2-2-11-13-11-1 @ "A_01과 A_02는 각자 자기 위치로 다시 붙어." @ 11 @ move_to_self_attempt @ accepted_20260514_002742.jsonl_seed_master_0157, accepted_20260514_180505.jsonl_batch_0111_001, accepted_20260514_180505.jsonl_batch_0111_002, accepted_20260514_180505.jsonl_batch_0111_003, accepted_20260514_180505.jsonl_batch_0111_004, accepted_20260514_180505.jsonl_batch_0111_005, accepted_20260514_180505.jsonl_batch_0111_006, accepted_20260514_180505.jsonl_batch_0111_007, accepted_20260514_180505.jsonl_batch_0111_008, accepted_20260514_180505.jsonl_batch_0111_009, accepted_20260514_180505.jsonl_batch_0111_010
    none [3.1%(10%) / 2]
      move_only [100.0%(55%) / 2]
        hold_front [100.0%(7%) / 2]
          2-2-12-2-10-1 @ "A_01과 A_02는 전열을 유지해." @ 2 @ hold_front_requested @ accepted_20260514_002742.jsonl_seed_master_0158, accepted_20260514_180627.jsonl_batch_0112_001
  global_condition [10.4%(15%) / 45]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [51.1%(16%) / 23]
      move_only [100.0%(55%) / 23]
        low_hp_actor_escape [100.0%(10%) / 23]
          2-3-8-2-7-1 @ "체력이 낮은 아군은 전부 뒤로 빠져." @ 23 @ low_hp_actor_selection @ accepted_20260514_002740.jsonl_seed_master_0039, accepted_20260514_181753.jsonl_batch_0113_001, accepted_20260514_181753.jsonl_batch_0113_002, accepted_20260514_181753.jsonl_batch_0113_003, accepted_20260514_181753.jsonl_batch_0113_004, accepted_20260514_181753.jsonl_batch_0113_005, accepted_20260514_181753.jsonl_batch_0113_006, accepted_20260514_181753.jsonl_batch_0113_007, accepted_20260514_181753.jsonl_batch_0113_008, accepted_20260514_181753.jsonl_batch_0113_010, accepted_20260514_182926.jsonl_batch_0114_001, accepted_20260514_182926.jsonl_batch_0114_002, accepted_20260514_182926.jsonl_batch_0114_003, accepted_20260514_182926.jsonl_batch_0114_004, accepted_20260514_182926.jsonl_batch_0114_005, accepted_20260514_182926.jsonl_batch_0114_006, accepted_20260514_182926.jsonl_batch_0114_007, accepted_20260514_182926.jsonl_batch_0114_008, accepted_20260514_182926.jsonl_batch_0114_010, accepted_20260514_183421.jsonl_batch_0115_001, accepted_20260514_183421.jsonl_batch_0115_002, accepted_20260514_183421.jsonl_batch_0115_003, accepted_20260514_183421.jsonl_batch_0115_004
    low_hp_ally [48.9%(12%) / 22]
      move_only [100.0%(55%) / 22]
        support_low_hp_ally [100.0%(8%) / 22]
          2-3-9-2-9-1 @ "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 22 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002742.jsonl_seed_master_0159, accepted_20260514_191140.jsonl_batch_0116_001, accepted_20260514_191140.jsonl_batch_0116_002, accepted_20260514_191140.jsonl_batch_0116_003, accepted_20260514_191140.jsonl_batch_0116_004, accepted_20260514_191140.jsonl_batch_0116_005, accepted_20260514_191140.jsonl_batch_0116_006, accepted_20260514_191140.jsonl_batch_0116_007, accepted_20260514_191140.jsonl_batch_0116_008, accepted_20260514_191140.jsonl_batch_0116_009, accepted_20260514_191140.jsonl_batch_0116_010, accepted_20260514_192254.jsonl_batch_0117_001, accepted_20260514_192254.jsonl_batch_0117_002, accepted_20260514_192254.jsonl_batch_0117_003, accepted_20260514_192254.jsonl_batch_0117_004, accepted_20260514_192254.jsonl_batch_0117_005, accepted_20260514_192254.jsonl_batch_0117_006, accepted_20260514_192254.jsonl_batch_0117_007, accepted_20260514_192254.jsonl_batch_0117_008, accepted_20260514_192254.jsonl_batch_0117_009, accepted_20260514_192254.jsonl_batch_0117_010, accepted_20260514_192409.jsonl_batch_0118_001
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  global_role_based [8.6%(15%) / 37]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [43.2%(16%) / 16]
      move_only [100.0%(55%) / 16]
        retreat_to_backline_ally [100.0%(12%) / 16]
          2-4-8-2-6-1 @ "전열 아군은 안전한 아군 쪽으로 빠져." @ 16 @ frontline_actor_selection, retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0160, accepted_20260514_193552.jsonl_batch_0119_001, accepted_20260514_193552.jsonl_batch_0119_002, accepted_20260514_193552.jsonl_batch_0119_003, accepted_20260514_193552.jsonl_batch_0119_004, accepted_20260514_193552.jsonl_batch_0119_005, accepted_20260514_193552.jsonl_batch_0119_006, accepted_20260514_193552.jsonl_batch_0119_007, accepted_20260514_193552.jsonl_batch_0119_008, accepted_20260514_193552.jsonl_batch_0119_009, accepted_20260514_193552.jsonl_batch_0119_010, accepted_20260514_194145.jsonl_batch_0120_001, accepted_20260514_194145.jsonl_batch_0120_002, accepted_20260514_194145.jsonl_batch_0120_003, accepted_20260514_194145.jsonl_batch_0120_004, accepted_20260514_194145.jsonl_batch_0120_005
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [56.8%(10%) / 21]
      move_only [100.0%(55%) / 21]
        hold_front [100.0%(7%) / 21]
          2-4-12-2-10-1 @ "전열 아군은 앞에서 버텨." @ 21 @ frontline_actor_selection, hold_front_requested @ accepted_20260514_002740.jsonl_seed_master_0040, accepted_20260514_195355.jsonl_batch_0121_001, accepted_20260514_195355.jsonl_batch_0121_002, accepted_20260514_195355.jsonl_batch_0121_003, accepted_20260514_195355.jsonl_batch_0121_004, accepted_20260514_195355.jsonl_batch_0121_005, accepted_20260514_195355.jsonl_batch_0121_006, accepted_20260514_195355.jsonl_batch_0121_007, accepted_20260514_195355.jsonl_batch_0121_008, accepted_20260514_195355.jsonl_batch_0121_009, accepted_20260514_195355.jsonl_batch_0121_010, accepted_20260514_200630.jsonl_batch_0122_001, accepted_20260514_200630.jsonl_batch_0122_002, accepted_20260514_200630.jsonl_batch_0122_003, accepted_20260514_200630.jsonl_batch_0122_004, accepted_20260514_200630.jsonl_batch_0122_005, accepted_20260514_200630.jsonl_batch_0122_006, accepted_20260514_200630.jsonl_batch_0122_007, accepted_20260514_200630.jsonl_batch_0122_008, accepted_20260514_200630.jsonl_batch_0122_009, accepted_20260514_200630.jsonl_batch_0122_010
  global_state_based [5.3%(10%) / 23]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [78.3%(16%) / 18]
      move_only [100.0%(55%) / 18]
        retreat_to_backline_ally [100.0%(12%) / 18]
          2-5-8-2-6-1 @ "압박받는 아군은 안전한 아군 뒤쪽으로 빠져." @ 18 @ retreat_to_safe_ally @ accepted_20260514_002742.jsonl_seed_master_0161, accepted_20260514_202848.jsonl_batch_0124_001, accepted_20260514_202848.jsonl_batch_0124_002, accepted_20260514_202848.jsonl_batch_0124_003, accepted_20260514_202848.jsonl_batch_0124_004, accepted_20260514_202848.jsonl_batch_0124_005, accepted_20260514_202848.jsonl_batch_0124_006, accepted_20260514_202848.jsonl_batch_0124_007, accepted_20260514_202848.jsonl_batch_0124_008, accepted_20260514_202848.jsonl_batch_0124_009, accepted_20260514_202848.jsonl_batch_0124_010, accepted_20260514_203906.jsonl_batch_0125_001, accepted_20260514_203906.jsonl_batch_0125_002, accepted_20260514_203906.jsonl_batch_0125_003, accepted_20260514_203906.jsonl_batch_0125_004, accepted_20260514_203906.jsonl_batch_0125_005, accepted_20260514_203906.jsonl_batch_0125_006, accepted_20260514_203906.jsonl_batch_0125_007
    low_hp_ally [21.7%(12%) / 5]
      move_only [100.0%(55%) / 5]
        support_low_hp_ally [100.0%(8%) / 5]
          2-5-9-2-9-1 @ "여유 있는 아군은 체력이 낮은 아군에게 붙어." @ 5 @ free_actor_selection, low_hp_ally_target @ accepted_20260514_002740.jsonl_seed_master_0041, accepted_20260514_204548.jsonl_batch_0126_001, accepted_20260514_204548.jsonl_batch_0126_002, accepted_20260514_204548.jsonl_batch_0126_003, accepted_20260514_204548.jsonl_batch_0126_004
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [0.0%(10%) / 0]
  no_valid_actor [5.1%(5%) / 22]
    explicit_ally_target [0.0%(22%) / 0]
    explicit_enemy_target [0.0%(18%) / 0]
    safe_ally [45.5%(16%) / 10]
      empty_action_expected [100.0%(10%) / 10]
        no_matching_actor [100.0%(5%) / 10]
          2-6-8-13-12-1 @ "체력이 낮은 아군은 뒤로 빠져." @ 10 @ no_matching_actor @ accepted_20260514_002740.jsonl_seed_master_0042, accepted_20260514_205523.jsonl_batch_0127_001, accepted_20260514_205523.jsonl_batch_0127_002, accepted_20260514_205523.jsonl_batch_0127_003, accepted_20260514_205523.jsonl_batch_0127_004, accepted_20260514_205523.jsonl_batch_0127_005, accepted_20260514_205523.jsonl_batch_0127_006, accepted_20260514_205523.jsonl_batch_0127_007, accepted_20260514_205523.jsonl_batch_0127_008, accepted_20260514_205523.jsonl_batch_0127_009
    low_hp_ally [0.0%(12%) / 0]
    backline_ally [0.0%(10%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    invalid_explicit_target [0.0%(7%) / 0]
    none [54.5%(10%) / 12]
      empty_action_expected [100.0%(10%) / 12]
        no_matching_actor [100.0%(5%) / 12]
          2-6-12-13-12-1 @ "움직일 수 있는 아군은 전부 후퇴해." @ 12 @ no_matching_actor @ accepted_20260514_002742.jsonl_seed_master_0162, accepted_20260514_210614.jsonl_batch_0128_001, accepted_20260514_210614.jsonl_batch_0128_002, accepted_20260514_210614.jsonl_batch_0128_003, accepted_20260514_210614.jsonl_batch_0128_004, accepted_20260514_210614.jsonl_batch_0128_005, accepted_20260514_210614.jsonl_batch_0128_006, accepted_20260514_210614.jsonl_batch_0128_007, accepted_20260514_210614.jsonl_batch_0128_008, accepted_20260514_210614.jsonl_batch_0128_009, accepted_20260514_210614.jsonl_batch_0128_010, accepted_20260514_210927.jsonl_batch_0129_001

skill [27.5%(26%) / 523]
  explicit_actor [66.9%(55%) / 350]
    explicit_enemy_target [23.4%(26%) / 82]
      skill_only [97.6%(70%) / 80]
        enemy_skill_valid_target [10.0%(10%) / 8]
          3-1-1-4-1-1 @ "A_01, E_02에게 도약기로 붙어." @ 2 @ mobility_skill_enemy_approach @ accepted_20260514_002741.jsonl_seed_master_0112, accepted_20260514_211047.jsonl_batch_0130_001
          3-1-1-4-1-2 @ "A_03, E_02한테 공격 스킬 써." @ 2 @ [] @ accepted_20260514_002741.jsonl_seed_master_0103, accepted_20260514_211207.jsonl_batch_0131_001
          3-1-1-4-1-3 @ "A_03, E_02한테 스킬 써." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0043, accepted_20260514_211327.jsonl_batch_0132_001
          3-1-1-4-1-4 @ "A_03, E_02한테 약화 스킬 써." @ 2 @ [] @ accepted_20260514_002741.jsonl_seed_master_0106, accepted_20260514_211448.jsonl_batch_0133_001
        self_skill_enemy_target_conflict [28.8%(8%) / 23]
          3-1-1-4-4-1 @ "A_03, E_02한테 스킬 써." @ 23 @ explicit_enemy_target_conflicts_with_self_skill @ accepted_20260514_002740.jsonl_seed_master_0044, accepted_20260514_212719.jsonl_batch_0134_001, accepted_20260514_212719.jsonl_batch_0134_002, accepted_20260514_212719.jsonl_batch_0134_003, accepted_20260514_212719.jsonl_batch_0134_004, accepted_20260514_212719.jsonl_batch_0134_005, accepted_20260514_212719.jsonl_batch_0134_006, accepted_20260514_212719.jsonl_batch_0134_007, accepted_20260514_212719.jsonl_batch_0134_008, accepted_20260514_212719.jsonl_batch_0134_009, accepted_20260514_212719.jsonl_batch_0134_010, accepted_20260514_213948.jsonl_batch_0135_001, accepted_20260514_213948.jsonl_batch_0135_002, accepted_20260514_213948.jsonl_batch_0135_003, accepted_20260514_213948.jsonl_batch_0135_004, accepted_20260514_213948.jsonl_batch_0135_005, accepted_20260514_213948.jsonl_batch_0135_006, accepted_20260514_213948.jsonl_batch_0135_007, accepted_20260514_213948.jsonl_batch_0135_008, accepted_20260514_213948.jsonl_batch_0135_009, accepted_20260514_213948.jsonl_batch_0135_010, accepted_20260514_214223.jsonl_batch_0136_001, accepted_20260514_214223.jsonl_batch_0136_002
        ally_skill_enemy_target_conflict [53.8%(8%) / 43]
          3-1-1-4-5-1 @ "A_04, E_02한테 보호 스킬 써." @ 18 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0096, accepted_20260514_215511.jsonl_batch_0137_001, accepted_20260514_215511.jsonl_batch_0137_002, accepted_20260514_215511.jsonl_batch_0137_003, accepted_20260514_215511.jsonl_batch_0137_004, accepted_20260514_215511.jsonl_batch_0137_005, accepted_20260514_215511.jsonl_batch_0137_006, accepted_20260514_215511.jsonl_batch_0137_007, accepted_20260514_215511.jsonl_batch_0137_008, accepted_20260514_215511.jsonl_batch_0137_009, accepted_20260514_215511.jsonl_batch_0137_010, accepted_20260514_220411.jsonl_batch_0138_001, accepted_20260514_220411.jsonl_batch_0138_002, accepted_20260514_220411.jsonl_batch_0138_003, accepted_20260514_220411.jsonl_batch_0138_004, accepted_20260514_220411.jsonl_batch_0138_005, accepted_20260514_220411.jsonl_batch_0138_006, accepted_20260514_220411.jsonl_batch_0138_007
          3-1-1-4-5-2 @ "A_04, E_02한테 스킬 써." @ 13 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002740.jsonl_seed_master_0045, accepted_20260514_221649.jsonl_batch_0139_001, accepted_20260514_221649.jsonl_batch_0139_002, accepted_20260514_221649.jsonl_batch_0139_003, accepted_20260514_221649.jsonl_batch_0139_004, accepted_20260514_221649.jsonl_batch_0139_005, accepted_20260514_221649.jsonl_batch_0139_006, accepted_20260514_221649.jsonl_batch_0139_007, accepted_20260514_221649.jsonl_batch_0139_008, accepted_20260514_221649.jsonl_batch_0139_009, accepted_20260514_221649.jsonl_batch_0139_010, accepted_20260514_221927.jsonl_batch_0140_001, accepted_20260514_221927.jsonl_batch_0140_002
          3-1-1-4-5-3 @ "A_04, E_02한테 회복 스킬 써." @ 12 @ explicit_enemy_target_conflicts_with_ally_skill @ accepted_20260514_002741.jsonl_seed_master_0099, accepted_20260514_223225.jsonl_batch_0141_001, accepted_20260514_223225.jsonl_batch_0141_002, accepted_20260514_223225.jsonl_batch_0141_003, accepted_20260514_223225.jsonl_batch_0141_004, accepted_20260514_223225.jsonl_batch_0141_005, accepted_20260514_223225.jsonl_batch_0141_006, accepted_20260514_223225.jsonl_batch_0141_007, accepted_20260514_223225.jsonl_batch_0141_008, accepted_20260514_223225.jsonl_batch_0141_009, accepted_20260514_223505.jsonl_batch_0142_001, accepted_20260514_223505.jsonl_batch_0142_002
        dead_target_forbidden [3.8%(6%) / 3]
          3-1-1-4-9-1 @ "A_03, 죽은 E_02한테 공격 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002740.jsonl_seed_master_0047
          3-1-1-4-9-2 @ "A_03, 죽은 E_02한테 약화 스킬 써." @ 2 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0108, accepted_20260514_223846.jsonl_batch_0144_001
        aoe_skill_center_selection [2.5%(8%) / 2]
          3-1-1-4-10-1 @ "A_05, E_03 주변에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0164, accepted_20260514_224007.jsonl_batch_0145_001
        actor_has_no_skill [1.2%(8%) / 1]
          3-1-1-4-11-1 @ "A_03, E_02한테 스킬 써." @ 1 @ actor_has_no_skill @ accepted_20260514_002740.jsonl_seed_master_0046
      move_then_skill [2.4%(10%) / 2]
        approach_then_skill [100.0%(4%) / 2]
          3-1-1-5-12-1 @ "A_03, E_02에게 접근해서 스킬 써." @ 2 @ [] @ accepted_20260514_002740.jsonl_seed_master_0048, accepted_20260514_232327.jsonl_batch_0150_001
    explicit_ally_target [38.3%(22%) / 134]
      skill_only [100.0%(70%) / 134]
        ally_skill_valid_target [3.7%(10%) / 5]
          3-1-2-4-2-1 @ "A_04, A_02한테 스킬 써." @ 3 @ [] @ accepted_20260514_002740.jsonl_seed_master_0049, accepted_20260514_002741.jsonl_seed_master_0095, accepted_20260514_232535.jsonl_batch_0151_001
          3-1-2-4-2-2 @ "A_04, 체력이 낮은 A_02한테 회복 스킬 써." @ 2 @ low_hp_ally_target @ accepted_20260514_002741.jsonl_seed_master_0098, accepted_20260514_232657.jsonl_batch_0152_001
        self_skill_enemy_target_conflict [13.4%(8%) / 18]
          3-1-2-4-4-1 @ "A_03, A_02한테 스킬 써." @ 18 @ explicit_ally_target_conflicts_with_self_skill @ accepted_20260514_002741.jsonl_seed_master_0094, accepted_20260514_233855.jsonl_batch_0153_001, accepted_20260514_233855.jsonl_batch_0153_002, accepted_20260514_233855.jsonl_batch_0153_003, accepted_20260514_233855.jsonl_batch_0153_004, accepted_20260514_233855.jsonl_batch_0153_005, accepted_20260514_233855.jsonl_batch_0153_006, accepted_20260514_233855.jsonl_batch_0153_007, accepted_20260514_233855.jsonl_batch_0153_008, accepted_20260514_233855.jsonl_batch_0153_009, accepted_20260514_233855.jsonl_batch_0153_010, accepted_20260514_234733.jsonl_batch_0154_001, accepted_20260514_234733.jsonl_batch_0154_002, accepted_20260514_234733.jsonl_batch_0154_003, accepted_20260514_234733.jsonl_batch_0154_004, accepted_20260514_234733.jsonl_batch_0154_005, accepted_20260514_234733.jsonl_batch_0154_006, accepted_20260514_234733.jsonl_batch_0154_007
        enemy_skill_ally_target_conflict [33.6%(8%) / 45]
          3-1-2-4-6-1 @ "A_01, A_02한테 스킬 써." @ 13 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002740.jsonl_seed_master_0050, accepted_20260515_000021.jsonl_batch_0155_001, accepted_20260515_000021.jsonl_batch_0155_002, accepted_20260515_000021.jsonl_batch_0155_003, accepted_20260515_000021.jsonl_batch_0155_004, accepted_20260515_000021.jsonl_batch_0155_005, accepted_20260515_000021.jsonl_batch_0155_006, accepted_20260515_000021.jsonl_batch_0155_007, accepted_20260515_000021.jsonl_batch_0155_008, accepted_20260515_000021.jsonl_batch_0155_009, accepted_20260515_000021.jsonl_batch_0155_010, accepted_20260515_000300.jsonl_batch_0156_001, accepted_20260515_000300.jsonl_batch_0156_002
          3-1-2-4-6-2 @ "A_03, A_02한테 공격 스킬 써." @ 13 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0104, accepted_20260515_001505.jsonl_batch_0157_001, accepted_20260515_001505.jsonl_batch_0157_002, accepted_20260515_001505.jsonl_batch_0157_003, accepted_20260515_001505.jsonl_batch_0157_004, accepted_20260515_001505.jsonl_batch_0157_005, accepted_20260515_001505.jsonl_batch_0157_006, accepted_20260515_001505.jsonl_batch_0157_007, accepted_20260515_001505.jsonl_batch_0157_008, accepted_20260515_001505.jsonl_batch_0157_009, accepted_20260515_001505.jsonl_batch_0157_010, accepted_20260515_001746.jsonl_batch_0158_001, accepted_20260515_001746.jsonl_batch_0158_002
          3-1-2-4-6-3 @ "A_03, A_02한테 약화 스킬 써." @ 7 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0107, accepted_20260515_002507.jsonl_batch_0159_001, accepted_20260515_002507.jsonl_batch_0159_002, accepted_20260515_002507.jsonl_batch_0159_003, accepted_20260515_002507.jsonl_batch_0159_004, accepted_20260515_002507.jsonl_batch_0159_005, accepted_20260515_002507.jsonl_batch_0159_006
          3-1-2-4-6-4 @ "A_06, A_02 주변에 광역 스킬 써." @ 12 @ explicit_ally_target_conflicts_with_enemy_skill @ accepted_20260514_002741.jsonl_seed_master_0110, accepted_20260515_003750.jsonl_batch_0160_001, accepted_20260515_003750.jsonl_batch_0160_002, accepted_20260515_003750.jsonl_batch_0160_003, accepted_20260515_003750.jsonl_batch_0160_004, accepted_20260515_003750.jsonl_batch_0160_005, accepted_20260515_003750.jsonl_batch_0160_006, accepted_20260515_003750.jsonl_batch_0160_007, accepted_20260515_003750.jsonl_batch_0160_008, accepted_20260515_003750.jsonl_batch_0160_009, accepted_20260515_003750.jsonl_batch_0160_010, accepted_20260515_003912.jsonl_batch_0161_001
        resurrection_dead_ally_valid [26.1%(8%) / 35]
          3-1-2-4-7-1 @ "A_04, 쓰러진 A_02한테 스킬 써." @ 35 @ dead_ally_skill_target_allowed @ accepted_20260514_002741.jsonl_seed_master_0051, accepted_20260514_002741.jsonl_seed_master_0101, accepted_20260515_005126.jsonl_batch_0162_001, accepted_20260515_005126.jsonl_batch_0162_002, accepted_20260515_005126.jsonl_batch_0162_004, accepted_20260515_005126.jsonl_batch_0162_005, accepted_20260515_005126.jsonl_batch_0162_006, accepted_20260515_005126.jsonl_batch_0162_007, accepted_20260515_005126.jsonl_batch_0162_008, accepted_20260515_005126.jsonl_batch_0162_009, accepted_20260515_010347.jsonl_batch_0163_001, accepted_20260515_010347.jsonl_batch_0163_003, accepted_20260515_010347.jsonl_batch_0163_004, accepted_20260515_010347.jsonl_batch_0163_005, accepted_20260515_010347.jsonl_batch_0163_006, accepted_20260515_010347.jsonl_batch_0163_007, accepted_20260515_010347.jsonl_batch_0163_008, accepted_20260515_010347.jsonl_batch_0163_009, accepted_20260515_010347.jsonl_batch_0163_010, accepted_20260515_011613.jsonl_batch_0164_001, accepted_20260515_011613.jsonl_batch_0164_002, accepted_20260515_011613.jsonl_batch_0164_004, accepted_20260515_011613.jsonl_batch_0164_005, accepted_20260515_011613.jsonl_batch_0164_006, accepted_20260515_011613.jsonl_batch_0164_007, accepted_20260515_011613.jsonl_batch_0164_008, accepted_20260515_011613.jsonl_batch_0164_009, accepted_20260515_011613.jsonl_batch_0164_010, accepted_20260515_012605.jsonl_batch_0165_001, accepted_20260515_012605.jsonl_batch_0165_002, accepted_20260515_012605.jsonl_batch_0165_004, accepted_20260515_012605.jsonl_batch_0165_005, accepted_20260515_012605.jsonl_batch_0165_006, accepted_20260515_012605.jsonl_batch_0165_007, accepted_20260515_012605.jsonl_batch_0165_008
        resurrection_living_ally_conflict [21.6%(6%) / 29]
          3-1-2-4-8-1 @ "A_04, 살아있는 A_02한테 부활 스킬 써." @ 29 @ text_living_target_but_resurrection_skill @ accepted_20260514_002741.jsonl_seed_master_0052, accepted_20260515_013837.jsonl_batch_0166_001, accepted_20260515_013837.jsonl_batch_0166_002, accepted_20260515_013837.jsonl_batch_0166_003, accepted_20260515_013837.jsonl_batch_0166_004, accepted_20260515_013837.jsonl_batch_0166_005, accepted_20260515_013837.jsonl_batch_0166_006, accepted_20260515_013837.jsonl_batch_0166_007, accepted_20260515_013837.jsonl_batch_0166_008, accepted_20260515_013837.jsonl_batch_0166_009, accepted_20260515_013837.jsonl_batch_0166_010, accepted_20260515_015116.jsonl_batch_0167_001, accepted_20260515_015116.jsonl_batch_0167_002, accepted_20260515_015116.jsonl_batch_0167_003, accepted_20260515_015116.jsonl_batch_0167_004, accepted_20260515_015116.jsonl_batch_0167_005, accepted_20260515_015116.jsonl_batch_0167_006, accepted_20260515_015116.jsonl_batch_0167_007, accepted_20260515_015116.jsonl_batch_0167_008, accepted_20260515_015116.jsonl_batch_0167_009, accepted_20260515_015116.jsonl_batch_0167_010, accepted_20260515_020238.jsonl_batch_0168_001, accepted_20260515_020238.jsonl_batch_0168_003, accepted_20260515_020238.jsonl_batch_0168_004, accepted_20260515_020238.jsonl_batch_0168_005, accepted_20260515_020238.jsonl_batch_0168_006, accepted_20260515_020238.jsonl_batch_0168_007, accepted_20260515_020238.jsonl_batch_0168_008, accepted_20260515_020238.jsonl_batch_0168_009
        dead_target_forbidden [1.5%(6%) / 2]
          3-1-2-4-9-1 @ "A_04, 쓰러진 A_02한테 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0053
          3-1-2-4-9-2 @ "A_04, 죽은 A_02한테 회복 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0100
    lowest_hp_enemy [1.1%(8%) / 4]
      skill_only [100.0%(70%) / 4]
        enemy_skill_valid_target [50.0%(10%) / 2]
          3-1-4-4-1-1 @ "A_03, 체력이 제일 낮은 적에게 스킬 써." @ 2 @ [] @ accepted_20260514_002743.jsonl_seed_master_0165, accepted_20260515_020846.jsonl_batch_0171_001
        aoe_skill_center_selection [50.0%(8%) / 2]
          3-1-4-4-10-1 @ "A_06, 체력이 제일 낮은 적을 중심으로 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0166, accepted_20260515_021531.jsonl_batch_0172_001
    nearest_enemy [8.6%(5%) / 30]
      skill_only [30.0%(70%) / 9]
        enemy_skill_valid_target [22.2%(10%) / 2]
          3-1-3-4-1-1 @ "A_03, 가장 가까운 적에게 스킬 써." @ 2 @ [] @ accepted_20260514_002743.jsonl_seed_master_0168, accepted_20260515_021650.jsonl_batch_0173_001
        aoe_skill_center_selection [77.8%(8%) / 7]
          3-1-3-4-10-1 @ "A_06, 가장 가까운 적을 중심으로 스킬 써." @ 7 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0169, accepted_20260515_022358.jsonl_batch_0174_001, accepted_20260515_022358.jsonl_batch_0174_002, accepted_20260515_022358.jsonl_batch_0174_003, accepted_20260515_022358.jsonl_batch_0174_004, accepted_20260515_022358.jsonl_batch_0174_005, accepted_20260515_022358.jsonl_batch_0174_006
      move_then_skill [70.0%(10%) / 21]
        approach_then_skill [100.0%(4%) / 21]
          3-1-3-5-12-1 @ "A_03, 가장 가까운 적에게 접근해서 스킬 써." @ 21 @ [] @ accepted_20260514_002743.jsonl_seed_master_0167, accepted_20260515_023627.jsonl_batch_0175_001, accepted_20260515_023627.jsonl_batch_0175_002, accepted_20260515_023627.jsonl_batch_0175_003, accepted_20260515_023627.jsonl_batch_0175_004, accepted_20260515_023627.jsonl_batch_0175_005, accepted_20260515_023627.jsonl_batch_0175_006, accepted_20260515_023627.jsonl_batch_0175_007, accepted_20260515_023627.jsonl_batch_0175_008, accepted_20260515_023627.jsonl_batch_0175_009, accepted_20260515_023627.jsonl_batch_0175_010, accepted_20260515_024853.jsonl_batch_0176_001, accepted_20260515_024853.jsonl_batch_0176_002, accepted_20260515_024853.jsonl_batch_0176_003, accepted_20260515_024853.jsonl_batch_0176_004, accepted_20260515_024853.jsonl_batch_0176_005, accepted_20260515_024853.jsonl_batch_0176_006, accepted_20260515_024853.jsonl_batch_0176_007, accepted_20260515_024853.jsonl_batch_0176_008, accepted_20260515_024853.jsonl_batch_0176_009, accepted_20260515_024853.jsonl_batch_0176_010
    role_based_enemy [2.3%(8%) / 8]
      skill_only [75.0%(70%) / 6]
        enemy_skill_valid_target [33.3%(10%) / 2]
          3-1-6-4-1-1 @ "A_03, 적 후열에게 스킬 써." @ 2 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0171, accepted_20260515_025011.jsonl_batch_0177_001
        aoe_skill_center_selection [66.7%(8%) / 4]
          3-1-6-4-10-1 @ "A_06, 적 후열이 뭉친 곳에 스킬 써." @ 2 @ target_role_backline_enemy, aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0170, accepted_20260515_025132.jsonl_batch_0178_001
          3-1-6-4-10-2 @ "A_06, 적들이 뭉친 쪽에 스킬 써." @ 2 @ aoe_skill_requires_single_center_target @ accepted_20260514_002649.jsonl_seed_master_0008, accepted_20260515_025252.jsonl_batch_0179_001
      move_then_skill [25.0%(10%) / 2]
        approach_then_skill [100.0%(4%) / 2]
          3-1-6-5-12-1 @ "A_03, 적 후열에게 접근해서 스킬 써." @ 2 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0172, accepted_20260515_025413.jsonl_batch_0180_001
    low_hp_ally [0.6%(10%) / 2]
      skill_only [100.0%(70%) / 2]
        ally_skill_valid_target [100.0%(10%) / 2]
          3-1-9-4-2-1 @ "A_04, 체력이 낮은 아군에게 스킬 써." @ 2 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0173, accepted_20260515_025533.jsonl_batch_0181_001
    invalid_explicit_target [13.1%(13%) / 46]
      empty_action_expected [100.0%(10%) / 46]
        dead_target_forbidden [56.5%(6%) / 26]
          3-1-11-13-9-1 @ "A_03, 죽은 E_02한테 스킬 써." @ 26 @ skill_target_dead_not_allowed @ accepted_20260514_002743.jsonl_seed_master_0174, accepted_20260515_030716.jsonl_batch_0182_001, accepted_20260515_030716.jsonl_batch_0182_002, accepted_20260515_030716.jsonl_batch_0182_003, accepted_20260515_030716.jsonl_batch_0182_004, accepted_20260515_030716.jsonl_batch_0182_005, accepted_20260515_030716.jsonl_batch_0182_006, accepted_20260515_030716.jsonl_batch_0182_008, accepted_20260515_030716.jsonl_batch_0182_009, accepted_20260515_030716.jsonl_batch_0182_010, accepted_20260515_032513.jsonl_batch_0183_001, accepted_20260515_032513.jsonl_batch_0183_002, accepted_20260515_032513.jsonl_batch_0183_003, accepted_20260515_032513.jsonl_batch_0183_004, accepted_20260515_032513.jsonl_batch_0183_005, accepted_20260515_032513.jsonl_batch_0183_006, accepted_20260515_032513.jsonl_batch_0183_007, accepted_20260515_032513.jsonl_batch_0183_008, accepted_20260515_032513.jsonl_batch_0183_009, accepted_20260515_032513.jsonl_batch_0183_010, accepted_20260515_033213.jsonl_batch_0184_001, accepted_20260515_033213.jsonl_batch_0184_002, accepted_20260515_033213.jsonl_batch_0184_003, accepted_20260515_033213.jsonl_batch_0184_004, accepted_20260515_033213.jsonl_batch_0184_005, accepted_20260515_033213.jsonl_batch_0184_006
        no_valid_skill_target [43.5%(4%) / 20]
          3-1-11-13-14-1 @ "A_03, 죽은 E_02한테 스킬 써." @ 20 @ named_target_dead, no_valid_skill_target @ accepted_20260514_002743.jsonl_seed_master_0175, accepted_20260515_034401.jsonl_batch_0185_001, accepted_20260515_034401.jsonl_batch_0185_002, accepted_20260515_034401.jsonl_batch_0185_003, accepted_20260515_034401.jsonl_batch_0185_004, accepted_20260515_034401.jsonl_batch_0185_005, accepted_20260515_034401.jsonl_batch_0185_006, accepted_20260515_034401.jsonl_batch_0185_007, accepted_20260515_034401.jsonl_batch_0185_008, accepted_20260515_034401.jsonl_batch_0185_009, accepted_20260515_034401.jsonl_batch_0185_010, accepted_20260515_035552.jsonl_batch_0186_001, accepted_20260515_035552.jsonl_batch_0186_002, accepted_20260515_035552.jsonl_batch_0186_003, accepted_20260515_035552.jsonl_batch_0186_004, accepted_20260515_035552.jsonl_batch_0186_005, accepted_20260515_035552.jsonl_batch_0186_006, accepted_20260515_035552.jsonl_batch_0186_007, accepted_20260515_035552.jsonl_batch_0186_009, accepted_20260515_035552.jsonl_batch_0186_010
    none [12.6%(8%) / 44]
      skill_only [95.5%(70%) / 42]
        self_skill_no_target [92.9%(8%) / 39]
          3-1-12-4-3-1 @ "A_01, 도약기로 빠져." @ 39 @ mobility_skill_self_escape @ accepted_20260514_002741.jsonl_seed_master_0111, accepted_20260515_041552.jsonl_batch_0187_001, accepted_20260515_041552.jsonl_batch_0187_002, accepted_20260515_041552.jsonl_batch_0187_003, accepted_20260515_041552.jsonl_batch_0187_004, accepted_20260515_041552.jsonl_batch_0187_005, accepted_20260515_041552.jsonl_batch_0187_006, accepted_20260515_041552.jsonl_batch_0187_007, accepted_20260515_041552.jsonl_batch_0187_008, accepted_20260515_041552.jsonl_batch_0187_009, accepted_20260515_041552.jsonl_batch_0187_010, accepted_20260515_042811.jsonl_batch_0188_001, accepted_20260515_042811.jsonl_batch_0188_002, accepted_20260515_042811.jsonl_batch_0188_003, accepted_20260515_042811.jsonl_batch_0188_004, accepted_20260515_042811.jsonl_batch_0188_005, accepted_20260515_042811.jsonl_batch_0188_006, accepted_20260515_042811.jsonl_batch_0188_007, accepted_20260515_042811.jsonl_batch_0188_008, accepted_20260515_042811.jsonl_batch_0188_009, accepted_20260515_042811.jsonl_batch_0188_010, accepted_20260515_044024.jsonl_batch_0189_001, accepted_20260515_044024.jsonl_batch_0189_002, accepted_20260515_044024.jsonl_batch_0189_003, accepted_20260515_044024.jsonl_batch_0189_004, accepted_20260515_044024.jsonl_batch_0189_005, accepted_20260515_044024.jsonl_batch_0189_006, accepted_20260515_044024.jsonl_batch_0189_007, accepted_20260515_044024.jsonl_batch_0189_008, accepted_20260515_044024.jsonl_batch_0189_009, accepted_20260515_044024.jsonl_batch_0189_010, accepted_20260515_045019.jsonl_batch_0190_001, accepted_20260515_045019.jsonl_batch_0190_002, accepted_20260515_045019.jsonl_batch_0190_003, accepted_20260515_045019.jsonl_batch_0190_004, accepted_20260515_045019.jsonl_batch_0190_005, accepted_20260515_045019.jsonl_batch_0190_006, accepted_20260515_045019.jsonl_batch_0190_007, accepted_20260515_045019.jsonl_batch_0190_008
        aoe_skill_center_selection [7.1%(8%) / 3]
          3-1-12-4-10-1 @ "A_06, 적들이 뭉친 쪽에 스킬 써." @ 3 @ aoe_skill_requires_single_center_target @ accepted_20260514_002741.jsonl_seed_master_0055, accepted_20260514_002741.jsonl_seed_master_0109, accepted_20260515_045139.jsonl_batch_0191_001
      empty_action_expected [4.5%(10%) / 2]
        actor_has_no_skill [100.0%(8%) / 2]
          3-1-12-13-11-1 @ "A_03, 지금 스킬 써." @ 2 @ actor_has_no_skill @ accepted_20260514_002743.jsonl_seed_master_0176, accepted_20260515_045253.jsonl_batch_0192_001
  explicit_multi_actor [11.1%(10%) / 58]
    explicit_enemy_target [65.5%(26%) / 38]
      multi_actor_same_target [94.7%(7%) / 36]
        enemy_skill_valid_target [5.6%(10%) / 2]
          3-2-1-11-1-1 @ "A_03과 A_06은 E_02에게 스킬을 써." @ 2 @ [] @ accepted_20260514_002743.jsonl_seed_master_0177, accepted_20260515_045416.jsonl_batch_0193_001
        aoe_skill_center_selection [94.4%(8%) / 34]
          3-2-1-11-10-1 @ "A_03과 A_06은 E_02 주변에 스킬을 써." @ 34 @ aoe_skill_requires_single_center_target @ accepted_20260514_002743.jsonl_seed_master_0178, accepted_20260515_050728.jsonl_batch_0194_001, accepted_20260515_050728.jsonl_batch_0194_002, accepted_20260515_050728.jsonl_batch_0194_003, accepted_20260515_050728.jsonl_batch_0194_004, accepted_20260515_050728.jsonl_batch_0194_005, accepted_20260515_050728.jsonl_batch_0194_006, accepted_20260515_050728.jsonl_batch_0194_007, accepted_20260515_050728.jsonl_batch_0194_008, accepted_20260515_050728.jsonl_batch_0194_009, accepted_20260515_050728.jsonl_batch_0194_010, accepted_20260515_052040.jsonl_batch_0195_001, accepted_20260515_052040.jsonl_batch_0195_002, accepted_20260515_052040.jsonl_batch_0195_003, accepted_20260515_052040.jsonl_batch_0195_004, accepted_20260515_052040.jsonl_batch_0195_005, accepted_20260515_052040.jsonl_batch_0195_006, accepted_20260515_052040.jsonl_batch_0195_007, accepted_20260515_052040.jsonl_batch_0195_008, accepted_20260515_052040.jsonl_batch_0195_009, accepted_20260515_052040.jsonl_batch_0195_010, accepted_20260515_053348.jsonl_batch_0196_001, accepted_20260515_053348.jsonl_batch_0196_002, accepted_20260515_053348.jsonl_batch_0196_003, accepted_20260515_053348.jsonl_batch_0196_004, accepted_20260515_053348.jsonl_batch_0196_005, accepted_20260515_053348.jsonl_batch_0196_006, accepted_20260515_053348.jsonl_batch_0196_007, accepted_20260515_053348.jsonl_batch_0196_008, accepted_20260515_053348.jsonl_batch_0196_009, accepted_20260515_053348.jsonl_batch_0196_010, accepted_20260515_053752.jsonl_batch_0197_001, accepted_20260515_053752.jsonl_batch_0197_002, accepted_20260515_053752.jsonl_batch_0197_003
      multi_actor_different_targets [5.3%(3%) / 2]
        enemy_skill_valid_target [100.0%(10%) / 2]
          3-2-1-12-1-1 @ "A_03은 E_01에게, A_06은 E_03에게 스킬을 써." @ 2 @ [] @ accepted_20260514_002743.jsonl_seed_master_0179, accepted_20260515_053917.jsonl_batch_0198_001
    explicit_ally_target [25.9%(22%) / 15]
      multi_actor_same_target [13.3%(7%) / 2]
        ally_skill_valid_target [100.0%(10%) / 2]
          3-2-2-11-2-1 @ "A_04와 A_05는 A_02에게 스킬을 써." @ 2 @ [] @ accepted_20260514_002743.jsonl_seed_master_0180, accepted_20260515_054039.jsonl_batch_0199_001
      multi_actor_different_targets [86.7%(3%) / 13]
        ally_skill_valid_target [100.0%(10%) / 13]
          3-2-2-12-2-1 @ "A_04는 A_01에게, A_05는 A_02에게 스킬을 써." @ 13 @ [] @ accepted_20260514_002743.jsonl_seed_master_0181, accepted_20260515_055320.jsonl_batch_0200_001, accepted_20260515_055320.jsonl_batch_0200_002, accepted_20260515_055320.jsonl_batch_0200_003, accepted_20260515_055320.jsonl_batch_0200_004, accepted_20260515_055320.jsonl_batch_0200_005, accepted_20260515_055320.jsonl_batch_0200_006, accepted_20260515_055320.jsonl_batch_0200_007, accepted_20260515_055320.jsonl_batch_0200_008, accepted_20260515_055320.jsonl_batch_0200_009, accepted_20260515_055320.jsonl_batch_0200_010, accepted_20260515_055556.jsonl_batch_0201_001, accepted_20260515_055556.jsonl_batch_0201_002
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [1.7%(8%) / 1]
      multi_actor_different_targets [100.0%(3%) / 1]
        enemy_skill_valid_target [100.0%(10%) / 1]
          3-2-6-12-1-1 @ "A_03은 적 전열에, A_06은 적 후열에 스킬을 써." @ 1 @ target_role_backline_enemy @ accepted_20260514_002743.jsonl_seed_master_0182
    low_hp_ally [3.4%(10%) / 2]
      multi_actor_same_target [100.0%(7%) / 2]
        ally_skill_valid_target [100.0%(10%) / 2]
          3-2-9-11-2-1 @ "A_04와 A_05는 체력이 제일 낮은 아군에게 스킬을 써." @ 2 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0183, accepted_20260515_055845.jsonl_batch_0203_001
    invalid_explicit_target [0.0%(13%) / 0]
    none [3.4%(8%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        no_valid_skill_actor [100.0%(4%) / 2]
          3-2-12-13-13-1 @ "A_03과 A_04는 지금 스킬 써." @ 2 @ no_valid_skill_actor @ accepted_20260514_002743.jsonl_seed_master_0184, accepted_20260515_055958.jsonl_batch_0204_001
  global_condition [6.3%(10%) / 33]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [75.8%(8%) / 25]
      skill_only [100.0%(70%) / 25]
        enemy_skill_valid_target [100.0%(10%) / 25]
          3-3-4-4-1-1 @ "스킬 쓸 수 있는 아군은 체력 낮은 적에게 스킬 써." @ 25 @ [] @ accepted_20260514_002743.jsonl_seed_master_0185, accepted_20260515_061426.jsonl_batch_0205_001, accepted_20260515_061426.jsonl_batch_0205_002, accepted_20260515_061426.jsonl_batch_0205_003, accepted_20260515_061426.jsonl_batch_0205_004, accepted_20260515_061426.jsonl_batch_0205_005, accepted_20260515_061426.jsonl_batch_0205_006, accepted_20260515_061426.jsonl_batch_0205_007, accepted_20260515_061426.jsonl_batch_0205_008, accepted_20260515_061426.jsonl_batch_0205_009, accepted_20260515_061426.jsonl_batch_0205_010, accepted_20260515_062639.jsonl_batch_0206_001, accepted_20260515_062639.jsonl_batch_0206_002, accepted_20260515_062639.jsonl_batch_0206_003, accepted_20260515_062639.jsonl_batch_0206_004, accepted_20260515_062639.jsonl_batch_0206_005, accepted_20260515_062639.jsonl_batch_0206_006, accepted_20260515_062639.jsonl_batch_0206_007, accepted_20260515_062639.jsonl_batch_0206_008, accepted_20260515_062639.jsonl_batch_0206_009, accepted_20260515_062639.jsonl_batch_0206_010, accepted_20260515_063135.jsonl_batch_0207_001, accepted_20260515_063135.jsonl_batch_0207_002, accepted_20260515_063135.jsonl_batch_0207_003, accepted_20260515_063135.jsonl_batch_0207_004
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [24.2%(10%) / 8]
      skill_only [100.0%(70%) / 8]
        ally_skill_valid_target [100.0%(10%) / 8]
          3-3-9-4-2-1 @ "회복 가능한 아군은 체력이 낮은 아군에게 스킬 써." @ 8 @ low_hp_ally_target @ accepted_20260514_002743.jsonl_seed_master_0186, accepted_20260515_063955.jsonl_batch_0208_001, accepted_20260515_063955.jsonl_batch_0208_002, accepted_20260515_063955.jsonl_batch_0208_003, accepted_20260515_063955.jsonl_batch_0208_004, accepted_20260515_063955.jsonl_batch_0208_005, accepted_20260515_063955.jsonl_batch_0208_006, accepted_20260515_063955.jsonl_batch_0208_007
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_role_based [4.6%(10%) / 24]
    explicit_enemy_target [0.0%(26%) / 0]
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [100.0%(8%) / 24]
      skill_only [100.0%(70%) / 24]
        enemy_skill_valid_target [100.0%(10%) / 24]
          3-4-6-4-1-1 @ "원거리 아군은 적 후열에 스킬을 써." @ 24 @ actor_role_ranged, target_role_backline_enemy @ accepted_20260514_002741.jsonl_seed_master_0058, accepted_20260515_065226.jsonl_batch_0209_001, accepted_20260515_065226.jsonl_batch_0209_002, accepted_20260515_065226.jsonl_batch_0209_003, accepted_20260515_065226.jsonl_batch_0209_004, accepted_20260515_065226.jsonl_batch_0209_005, accepted_20260515_065226.jsonl_batch_0209_007, accepted_20260515_065226.jsonl_batch_0209_008, accepted_20260515_065226.jsonl_batch_0209_009, accepted_20260515_065226.jsonl_batch_0209_010, accepted_20260515_070444.jsonl_batch_0210_001, accepted_20260515_070444.jsonl_batch_0210_002, accepted_20260515_070444.jsonl_batch_0210_003, accepted_20260515_070444.jsonl_batch_0210_004, accepted_20260515_070444.jsonl_batch_0210_005, accepted_20260515_070444.jsonl_batch_0210_006, accepted_20260515_070444.jsonl_batch_0210_007, accepted_20260515_070444.jsonl_batch_0210_008, accepted_20260515_070444.jsonl_batch_0210_009, accepted_20260515_070444.jsonl_batch_0210_010, accepted_20260515_070947.jsonl_batch_0211_001, accepted_20260515_070947.jsonl_batch_0211_002, accepted_20260515_070947.jsonl_batch_0211_003, accepted_20260515_070947.jsonl_batch_0211_004
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  global_state_based [6.5%(10%) / 34]
    explicit_enemy_target [5.9%(26%) / 2]
      skill_only [100.0%(70%) / 2]
        enemy_skill_valid_target [100.0%(10%) / 2]
          3-5-1-4-1-1 @ "스킬을 쓰기 안전한 아군은 E_02에게 스킬 써." @ 2 @ healthy_actor_selection @ 2accepted_20260514_190145.jsonl_2batch_0001_001, accepted_20260514_002743.jsonl_seed_master_0187
    explicit_ally_target [0.0%(22%) / 0]
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [94.1%(10%) / 32]
      skill_only [100.0%(70%) / 32]
        ally_skill_valid_target [100.0%(10%) / 32]
          3-5-9-4-2-1 @ "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 32 @ low_hp_ally_target @ 2accepted_20260514_191342.jsonl_2batch_0002_001, 2accepted_20260514_191342.jsonl_2batch_0002_002, 2accepted_20260514_191342.jsonl_2batch_0002_003, 2accepted_20260514_191342.jsonl_2batch_0002_004, 2accepted_20260514_191342.jsonl_2batch_0002_005, 2accepted_20260514_191342.jsonl_2batch_0002_006, 2accepted_20260514_191342.jsonl_2batch_0002_007, 2accepted_20260514_191342.jsonl_2batch_0002_008, 2accepted_20260514_191342.jsonl_2batch_0002_009, 2accepted_20260514_191342.jsonl_2batch_0002_010, 2accepted_20260514_192535.jsonl_2batch_0003_001, 2accepted_20260514_192535.jsonl_2batch_0003_002, 2accepted_20260514_192535.jsonl_2batch_0003_003, 2accepted_20260514_192535.jsonl_2batch_0003_004, 2accepted_20260514_192535.jsonl_2batch_0003_005, 2accepted_20260514_192535.jsonl_2batch_0003_006, 2accepted_20260514_192535.jsonl_2batch_0003_007, 2accepted_20260514_192535.jsonl_2batch_0003_008, 2accepted_20260514_192535.jsonl_2batch_0003_009, 2accepted_20260514_192535.jsonl_2batch_0003_010, 2accepted_20260514_193722.jsonl_2batch_0004_001, 2accepted_20260514_193722.jsonl_2batch_0004_002, 2accepted_20260514_193722.jsonl_2batch_0004_003, 2accepted_20260514_193722.jsonl_2batch_0004_004, 2accepted_20260514_193722.jsonl_2batch_0004_005, 2accepted_20260514_193722.jsonl_2batch_0004_006, 2accepted_20260514_193722.jsonl_2batch_0004_007, 2accepted_20260514_193722.jsonl_2batch_0004_008, 2accepted_20260514_193722.jsonl_2batch_0004_009, 2accepted_20260514_193722.jsonl_2batch_0004_010, 2accepted_20260514_193840.jsonl_2batch_0005_001, accepted_20260514_002741.jsonl_seed_master_0059
    invalid_explicit_target [0.0%(13%) / 0]
    none [0.0%(8%) / 0]
  no_valid_actor [4.6%(5%) / 24]
    explicit_enemy_target [54.2%(26%) / 13]
      empty_action_expected [100.0%(10%) / 13]
        no_valid_skill_actor [100.0%(4%) / 13]
          3-6-1-13-13-1 @ "스킬 가능한 아군은 E_02에게 스킬 써." @ 13 @ no_valid_skill_actor @ 2accepted_20260514_194946.jsonl_2batch_0006_001, 2accepted_20260514_194946.jsonl_2batch_0006_002, 2accepted_20260514_194946.jsonl_2batch_0006_003, 2accepted_20260514_194946.jsonl_2batch_0006_004, 2accepted_20260514_194946.jsonl_2batch_0006_005, 2accepted_20260514_194946.jsonl_2batch_0006_006, 2accepted_20260514_194946.jsonl_2batch_0006_007, 2accepted_20260514_194946.jsonl_2batch_0006_008, 2accepted_20260514_194946.jsonl_2batch_0006_009, 2accepted_20260514_194946.jsonl_2batch_0006_010, 2accepted_20260514_195203.jsonl_2batch_0007_001, 2accepted_20260514_195203.jsonl_2batch_0007_002, accepted_20260514_002741.jsonl_seed_master_0060
    explicit_ally_target [8.3%(22%) / 2]
      empty_action_expected [100.0%(10%) / 2]
        no_valid_skill_target [100.0%(4%) / 2]
          3-6-2-13-14-1 @ "회복 스킬이 있는 아군은 체력이 낮은 아군에게 스킬 써." @ 2 @ no_valid_skill_target @ 2accepted_20260514_195315.jsonl_2batch_0008_001, accepted_20260514_002741.jsonl_seed_master_0061
    lowest_hp_enemy [0.0%(8%) / 0]
    nearest_enemy [0.0%(5%) / 0]
    role_based_enemy [0.0%(8%) / 0]
    low_hp_ally [0.0%(10%) / 0]
    invalid_explicit_target [0.0%(13%) / 0]
    none [37.5%(8%) / 9]
      empty_action_expected [100.0%(10%) / 9]
        no_valid_skill_actor [100.0%(4%) / 9]
          3-6-12-13-13-1 @ "스킬 가능한 아군은 지금 스킬 써." @ 9 @ no_valid_skill_actor @ 2accepted_20260514_200139.jsonl_2batch_0009_001, 2accepted_20260514_200139.jsonl_2batch_0009_002, 2accepted_20260514_200139.jsonl_2batch_0009_003, 2accepted_20260514_200139.jsonl_2batch_0009_004, 2accepted_20260514_200139.jsonl_2batch_0009_005, 2accepted_20260514_200139.jsonl_2batch_0009_006, 2accepted_20260514_200139.jsonl_2batch_0009_007, 2accepted_20260514_200139.jsonl_2batch_0009_008, accepted_20260514_002743.jsonl_seed_master_0188

skillControl [8.5%(8%) / 162]
  explicit_actor [69.1%(70%) / 112]
    none [100.0%(100%) / 112]
      skillControl_defer [47.3%(55%) / 53]
        explicit_defer_skill [54.7%(25%) / 29]
          4-1-12-9-1-1 @ "A_03, 스킬은 아직 쓰지 말고 5초 후로 미뤄." @ 29 @ [] @ 2accepted_20260514_201329.jsonl_2batch_0010_001, 2accepted_20260514_201329.jsonl_2batch_0010_002, 2accepted_20260514_201329.jsonl_2batch_0010_003, 2accepted_20260514_201329.jsonl_2batch_0010_004, 2accepted_20260514_201329.jsonl_2batch_0010_005, 2accepted_20260514_201329.jsonl_2batch_0010_006, 2accepted_20260514_201329.jsonl_2batch_0010_007, 2accepted_20260514_201329.jsonl_2batch_0010_008, 2accepted_20260514_201329.jsonl_2batch_0010_009, 2accepted_20260514_201329.jsonl_2batch_0010_010, 2accepted_20260514_205304.jsonl_2batch_0011_001, 2accepted_20260514_205304.jsonl_2batch_0011_002, 2accepted_20260514_205304.jsonl_2batch_0011_003, 2accepted_20260514_205304.jsonl_2batch_0011_004, 2accepted_20260514_205304.jsonl_2batch_0011_005, 2accepted_20260514_205304.jsonl_2batch_0011_006, 2accepted_20260514_205304.jsonl_2batch_0011_007, 2accepted_20260514_205304.jsonl_2batch_0011_008, 2accepted_20260514_205304.jsonl_2batch_0011_009, 2accepted_20260514_205304.jsonl_2batch_0011_010, 2accepted_20260514_210231.jsonl_2batch_0012_001, 2accepted_20260514_210231.jsonl_2batch_0012_002, 2accepted_20260514_210231.jsonl_2batch_0012_003, 2accepted_20260514_210231.jsonl_2batch_0012_004, 2accepted_20260514_210231.jsonl_2batch_0012_005, 2accepted_20260514_210231.jsonl_2batch_0012_006, 2accepted_20260514_210231.jsonl_2batch_0012_007, 2accepted_20260514_210231.jsonl_2batch_0012_008, accepted_20260514_002741.jsonl_seed_master_0062
        defer_without_duration [45.3%(15%) / 24]
          4-1-12-9-2-1 @ "A_03, 스킬은 좀 아껴." @ 24 @ skillControl_duration_unspecified @ 2accepted_20260514_211420.jsonl_2batch_0013_001, 2accepted_20260514_211420.jsonl_2batch_0013_002, 2accepted_20260514_211420.jsonl_2batch_0013_003, 2accepted_20260514_211420.jsonl_2batch_0013_004, 2accepted_20260514_211420.jsonl_2batch_0013_005, 2accepted_20260514_211420.jsonl_2batch_0013_006, 2accepted_20260514_211420.jsonl_2batch_0013_007, 2accepted_20260514_211420.jsonl_2batch_0013_008, 2accepted_20260514_211420.jsonl_2batch_0013_009, 2accepted_20260514_211420.jsonl_2batch_0013_010, 2accepted_20260514_212608.jsonl_2batch_0014_001, 2accepted_20260514_212608.jsonl_2batch_0014_002, 2accepted_20260514_212608.jsonl_2batch_0014_003, 2accepted_20260514_212608.jsonl_2batch_0014_004, 2accepted_20260514_212608.jsonl_2batch_0014_005, 2accepted_20260514_212608.jsonl_2batch_0014_006, 2accepted_20260514_212608.jsonl_2batch_0014_007, 2accepted_20260514_212608.jsonl_2batch_0014_008, 2accepted_20260514_212608.jsonl_2batch_0014_009, 2accepted_20260514_212608.jsonl_2batch_0014_010, 2accepted_20260514_212944.jsonl_2batch_0015_001, 2accepted_20260514_212944.jsonl_2batch_0015_002, 2accepted_20260514_212944.jsonl_2batch_0015_003, accepted_20260514_002741.jsonl_seed_master_0063
      skillControl_forbid [50.9%(35%) / 57]
        explicit_forbid_skill [68.4%(25%) / 39]
          4-1-12-10-3-1 @ "A_03, 지금은 스킬 쓰지 마." @ 39 @ [] @ 2accepted_20260514_214125.jsonl_2batch_0016_001, 2accepted_20260514_214125.jsonl_2batch_0016_002, 2accepted_20260514_214125.jsonl_2batch_0016_003, 2accepted_20260514_214125.jsonl_2batch_0016_004, 2accepted_20260514_214125.jsonl_2batch_0016_005, 2accepted_20260514_214125.jsonl_2batch_0016_006, 2accepted_20260514_214125.jsonl_2batch_0016_007, 2accepted_20260514_214125.jsonl_2batch_0016_008, 2accepted_20260514_214125.jsonl_2batch_0016_009, 2accepted_20260514_214125.jsonl_2batch_0016_010, 2accepted_20260514_215310.jsonl_2batch_0017_001, 2accepted_20260514_215310.jsonl_2batch_0017_002, 2accepted_20260514_215310.jsonl_2batch_0017_003, 2accepted_20260514_215310.jsonl_2batch_0017_004, 2accepted_20260514_215310.jsonl_2batch_0017_005, 2accepted_20260514_215310.jsonl_2batch_0017_006, 2accepted_20260514_215310.jsonl_2batch_0017_007, 2accepted_20260514_215310.jsonl_2batch_0017_008, 2accepted_20260514_215310.jsonl_2batch_0017_009, 2accepted_20260514_215310.jsonl_2batch_0017_010, 2accepted_20260514_220445.jsonl_2batch_0018_001, 2accepted_20260514_220445.jsonl_2batch_0018_002, 2accepted_20260514_220445.jsonl_2batch_0018_003, 2accepted_20260514_220445.jsonl_2batch_0018_004, 2accepted_20260514_220445.jsonl_2batch_0018_005, 2accepted_20260514_220445.jsonl_2batch_0018_006, 2accepted_20260514_220445.jsonl_2batch_0018_007, 2accepted_20260514_220445.jsonl_2batch_0018_008, 2accepted_20260514_220445.jsonl_2batch_0018_009, 2accepted_20260514_220445.jsonl_2batch_0018_010, 2accepted_20260514_221401.jsonl_2batch_0019_001, 2accepted_20260514_221401.jsonl_2batch_0019_002, 2accepted_20260514_221401.jsonl_2batch_0019_003, 2accepted_20260514_221401.jsonl_2batch_0019_004, 2accepted_20260514_221401.jsonl_2batch_0019_005, 2accepted_20260514_221401.jsonl_2batch_0019_006, 2accepted_20260514_221401.jsonl_2batch_0019_007, 2accepted_20260514_221401.jsonl_2batch_0019_008, accepted_20260514_002741.jsonl_seed_master_0064
        forbid_without_duration [29.8%(10%) / 17]
          4-1-12-10-4-1 @ "A_03, 스킬 쓰지 말고 있어." @ 17 @ [] @ 2accepted_20260514_222546.jsonl_2batch_0020_001, 2accepted_20260514_222546.jsonl_2batch_0020_002, 2accepted_20260514_222546.jsonl_2batch_0020_003, 2accepted_20260514_222546.jsonl_2batch_0020_004, 2accepted_20260514_222546.jsonl_2batch_0020_005, 2accepted_20260514_222546.jsonl_2batch_0020_006, 2accepted_20260514_222546.jsonl_2batch_0020_007, 2accepted_20260514_222546.jsonl_2batch_0020_008, 2accepted_20260514_222546.jsonl_2batch_0020_009, 2accepted_20260514_222546.jsonl_2batch_0020_010, 2accepted_20260514_223252.jsonl_2batch_0021_001, 2accepted_20260514_223252.jsonl_2batch_0021_002, 2accepted_20260514_223252.jsonl_2batch_0021_003, 2accepted_20260514_223252.jsonl_2batch_0021_004, 2accepted_20260514_223252.jsonl_2batch_0021_005, 2accepted_20260514_223252.jsonl_2batch_0021_006, accepted_20260514_002741.jsonl_seed_master_0065
        actor_has_no_skill [1.8%(5%) / 1]
          4-1-12-10-7-1 @ "A_03, 스킬 쓰지 마." @ 1 @ actor_has_no_skill @ accepted_20260514_002741.jsonl_seed_master_0066
      empty_action_expected [1.8%(10%) / 2]
        selected_actor_dead [100.0%(5%) / 2]
          4-1-12-13-8-1 @ "A_03, 스킬 쓰지 말고 있어." @ 2 @ named_actor_dead @ 2accepted_20260514_223517.jsonl_2batch_0023_001, accepted_20260514_002743.jsonl_seed_master_0189
  explicit_multi_actor [19.8%(20%) / 32]
    none [100.0%(100%) / 32]
      skillControl_defer [53.1%(55%) / 17]
        multi_actor_defer_skill [100.0%(10%) / 17]
          4-2-12-9-5-1 @ "A_03과 A_04는 스킬을 아껴." @ 17 @ multi_actor_skillControl @ 2accepted_20260514_224711.jsonl_2batch_0024_001, 2accepted_20260514_224711.jsonl_2batch_0024_002, 2accepted_20260514_224711.jsonl_2batch_0024_003, 2accepted_20260514_224711.jsonl_2batch_0024_004, 2accepted_20260514_224711.jsonl_2batch_0024_005, 2accepted_20260514_224711.jsonl_2batch_0024_006, 2accepted_20260514_224711.jsonl_2batch_0024_007, 2accepted_20260514_224711.jsonl_2batch_0024_008, 2accepted_20260514_224711.jsonl_2batch_0024_009, 2accepted_20260514_224711.jsonl_2batch_0024_010, 2accepted_20260514_225439.jsonl_2batch_0025_001, 2accepted_20260514_225439.jsonl_2batch_0025_002, 2accepted_20260514_225439.jsonl_2batch_0025_003, 2accepted_20260514_225439.jsonl_2batch_0025_004, 2accepted_20260514_225439.jsonl_2batch_0025_005, 2accepted_20260514_225439.jsonl_2batch_0025_006, accepted_20260514_002741.jsonl_seed_master_0067
      skillControl_forbid [28.1%(35%) / 9]
        multi_actor_forbid_skill [100.0%(5%) / 9]
          4-2-12-10-6-1 @ "A_03과 A_04는 지금 스킬 쓰지 마." @ 9 @ multi_actor_skillControl @ 2accepted_20260514_230407.jsonl_2batch_0026_001, 2accepted_20260514_230407.jsonl_2batch_0026_002, 2accepted_20260514_230407.jsonl_2batch_0026_003, 2accepted_20260514_230407.jsonl_2batch_0026_004, 2accepted_20260514_230407.jsonl_2batch_0026_005, 2accepted_20260514_230407.jsonl_2batch_0026_006, 2accepted_20260514_230407.jsonl_2batch_0026_007, 2accepted_20260514_230407.jsonl_2batch_0026_008, accepted_20260514_002741.jsonl_seed_master_0068
      empty_action_expected [18.8%(10%) / 6]
        actor_has_no_skill [50.0%(5%) / 3]
          4-2-12-13-7-1 @ "A_03과 A_04는 지금 스킬 쓰지 마." @ 3 @ actor_has_no_skill @ 2accepted_20260514_230624.jsonl_2batch_0027_001, 2accepted_20260514_230624.jsonl_2batch_0027_002, accepted_20260514_002743.jsonl_seed_master_0191
        selected_actor_dead [50.0%(5%) / 3]
          4-2-12-13-8-1 @ "A_03과 A_04는 스킬 쓰지 말고 있어." @ 3 @ named_actor_dead @ 2accepted_20260514_230838.jsonl_2batch_0028_001, 2accepted_20260514_230838.jsonl_2batch_0028_002, accepted_20260514_002743.jsonl_seed_master_0190
  no_valid_actor [11.1%(10%) / 18]
    none [100.0%(100%) / 18]
      empty_action_expected [100.0%(10%) / 18]
        actor_has_no_skill [44.4%(5%) / 8]
          4-6-12-13-7-1 @ "스킬이 없는 A_03은 지금 스킬 쓰지 마." @ 8 @ actor_has_no_skill @ 2accepted_20260514_231521.jsonl_2batch_0029_001, 2accepted_20260514_231521.jsonl_2batch_0029_002, 2accepted_20260514_231521.jsonl_2batch_0029_003, 2accepted_20260514_231521.jsonl_2batch_0029_004, 2accepted_20260514_231521.jsonl_2batch_0029_005, 2accepted_20260514_231521.jsonl_2batch_0029_006, 2accepted_20260514_231521.jsonl_2batch_0029_007, accepted_20260514_002743.jsonl_seed_master_0193
        selected_actor_dead [55.6%(5%) / 10]
          4-6-12-13-8-1 @ "A_03, 스킬 쓰지 마." @ 5 @ named_actor_dead @ 2accepted_20260514_231944.jsonl_2batch_0030_001, 2accepted_20260514_231944.jsonl_2batch_0030_002, 2accepted_20260514_231944.jsonl_2batch_0030_003, 2accepted_20260514_231944.jsonl_2batch_0030_004, accepted_20260514_002741.jsonl_seed_master_0069
          4-6-12-13-8-2 @ "A_03, 스킬 쓰지 말고 있어." @ 5 @ named_actor_dead @ 2accepted_20260514_232406.jsonl_2batch_0031_001, 2accepted_20260514_232406.jsonl_2batch_0031_002, 2accepted_20260514_232406.jsonl_2batch_0031_003, 2accepted_20260514_232406.jsonl_2batch_0031_004, accepted_20260514_002743.jsonl_seed_master_0192

wait [8.4%(8%) / 159]
  explicit_actor [59.7%(60%) / 95]
    explicit_enemy_target [22.1%(10%) / 21]
      wait_only [66.7%(65%) / 14]
        explicit_wait [100.0%(25%) / 14]
          5-1-1-6-1-1 @ "A_04, E_02를 보면서 잠깐 대기해." @ 14 @ [] @ 2accepted_20260514_233600.jsonl_2batch_0032_001, 2accepted_20260514_233600.jsonl_2batch_0032_002, 2accepted_20260514_233600.jsonl_2batch_0032_003, 2accepted_20260514_233600.jsonl_2batch_0032_004, 2accepted_20260514_233600.jsonl_2batch_0032_005, 2accepted_20260514_233600.jsonl_2batch_0032_006, 2accepted_20260514_233600.jsonl_2batch_0032_007, 2accepted_20260514_233600.jsonl_2batch_0032_008, 2accepted_20260514_233600.jsonl_2batch_0032_009, 2accepted_20260514_233600.jsonl_2batch_0032_010, 2accepted_20260514_233942.jsonl_2batch_0033_001, 2accepted_20260514_233942.jsonl_2batch_0033_002, 2accepted_20260514_233942.jsonl_2batch_0033_003, accepted_20260514_002743.jsonl_seed_master_0196
      wait_then_attack [33.3%(20%) / 7]
        wait_then_attack_valid [100.0%(15%) / 7]
          5-1-1-7-3-1 @ "A_04, 3초 뒤에 E_02를 공격해." @ 7 @ explicit_wait_duration, wait_then_attack @ 2accepted_20260514_234558.jsonl_2batch_0034_001, 2accepted_20260514_234558.jsonl_2batch_0034_002, 2accepted_20260514_234558.jsonl_2batch_0034_003, 2accepted_20260514_234558.jsonl_2batch_0034_004, 2accepted_20260514_234558.jsonl_2batch_0034_005, accepted_20260514_002743.jsonl_seed_master_0194, accepted_20260514_002743.jsonl_seed_master_0195
    none [77.9%(90%) / 74]
      wait_only [81.1%(65%) / 60]
        explicit_wait [45.0%(25%) / 27]
          5-1-12-6-1-1 @ "A_04, 지금 자리에서 대기해." @ 27 @ [] @ 2accepted_20260514_235735.jsonl_2batch_0035_001, 2accepted_20260514_235735.jsonl_2batch_0035_002, 2accepted_20260514_235735.jsonl_2batch_0035_003, 2accepted_20260514_235735.jsonl_2batch_0035_004, 2accepted_20260514_235735.jsonl_2batch_0035_005, 2accepted_20260514_235735.jsonl_2batch_0035_006, 2accepted_20260514_235735.jsonl_2batch_0035_007, 2accepted_20260514_235735.jsonl_2batch_0035_008, 2accepted_20260514_235735.jsonl_2batch_0035_009, 2accepted_20260514_235735.jsonl_2batch_0035_010, 2accepted_20260515_000917.jsonl_2batch_0036_001, 2accepted_20260515_000917.jsonl_2batch_0036_002, 2accepted_20260515_000917.jsonl_2batch_0036_003, 2accepted_20260515_000917.jsonl_2batch_0036_004, 2accepted_20260515_000917.jsonl_2batch_0036_005, 2accepted_20260515_000917.jsonl_2batch_0036_006, 2accepted_20260515_000917.jsonl_2batch_0036_007, 2accepted_20260515_000917.jsonl_2batch_0036_008, 2accepted_20260515_000917.jsonl_2batch_0036_009, 2accepted_20260515_000917.jsonl_2batch_0036_010, 2accepted_20260515_001621.jsonl_2batch_0037_001, 2accepted_20260515_001621.jsonl_2batch_0037_002, 2accepted_20260515_001621.jsonl_2batch_0037_003, 2accepted_20260515_001621.jsonl_2batch_0037_004, 2accepted_20260515_001621.jsonl_2batch_0037_005, 2accepted_20260515_001621.jsonl_2batch_0037_006, accepted_20260514_002741.jsonl_seed_master_0070
        explicit_wait_duration [51.7%(20%) / 31]
          5-1-12-6-2-1 @ "A_04, 5초만 기다려." @ 31 @ explicit_wait_duration @ 2accepted_20260515_002807.jsonl_2batch_0038_001, 2accepted_20260515_002807.jsonl_2batch_0038_002, 2accepted_20260515_002807.jsonl_2batch_0038_003, 2accepted_20260515_002807.jsonl_2batch_0038_004, 2accepted_20260515_002807.jsonl_2batch_0038_005, 2accepted_20260515_002807.jsonl_2batch_0038_006, 2accepted_20260515_002807.jsonl_2batch_0038_007, 2accepted_20260515_002807.jsonl_2batch_0038_008, 2accepted_20260515_002807.jsonl_2batch_0038_009, 2accepted_20260515_002807.jsonl_2batch_0038_010, 2accepted_20260515_003951.jsonl_2batch_0039_001, 2accepted_20260515_003951.jsonl_2batch_0039_002, 2accepted_20260515_003951.jsonl_2batch_0039_003, 2accepted_20260515_003951.jsonl_2batch_0039_004, 2accepted_20260515_003951.jsonl_2batch_0039_005, 2accepted_20260515_003951.jsonl_2batch_0039_006, 2accepted_20260515_003951.jsonl_2batch_0039_007, 2accepted_20260515_003951.jsonl_2batch_0039_008, 2accepted_20260515_003951.jsonl_2batch_0039_009, 2accepted_20260515_003951.jsonl_2batch_0039_010, 2accepted_20260515_005137.jsonl_2batch_0040_001, 2accepted_20260515_005137.jsonl_2batch_0040_002, 2accepted_20260515_005137.jsonl_2batch_0040_003, 2accepted_20260515_005137.jsonl_2batch_0040_004, 2accepted_20260515_005137.jsonl_2batch_0040_005, 2accepted_20260515_005137.jsonl_2batch_0040_006, 2accepted_20260515_005137.jsonl_2batch_0040_007, 2accepted_20260515_005137.jsonl_2batch_0040_008, 2accepted_20260515_005137.jsonl_2batch_0040_009, 2accepted_20260515_005137.jsonl_2batch_0040_010, accepted_20260514_002741.jsonl_seed_master_0071
        hold_position_wait [3.3%(10%) / 2]
          5-1-12-6-5-1 @ "A_04, 위치 유지하면서 잠깐 버텨." @ 2 @ hold_front_requested @ 2accepted_20260515_005251.jsonl_2batch_0041_001, accepted_20260514_002741.jsonl_seed_master_0072
      wait_then_attack [13.5%(20%) / 10]
        wait_then_attack_valid [100.0%(15%) / 10]
          5-1-12-7-3-1 @ "A_04, 3초 기다렸다가 E_02를 공격해." @ 10 @ wait_then_attack @ 2accepted_20260515_010351.jsonl_2batch_0042_001, 2accepted_20260515_010351.jsonl_2batch_0042_002, 2accepted_20260515_010351.jsonl_2batch_0042_003, 2accepted_20260515_010351.jsonl_2batch_0042_004, 2accepted_20260515_010351.jsonl_2batch_0042_005, 2accepted_20260515_010351.jsonl_2batch_0042_006, 2accepted_20260515_010351.jsonl_2batch_0042_007, 2accepted_20260515_010351.jsonl_2batch_0042_008, 2accepted_20260515_010351.jsonl_2batch_0042_009, accepted_20260514_002741.jsonl_seed_master_0073
      wait_then_skill [1.4%(10%) / 1]
        wait_then_skill_valid [100.0%(10%) / 1]
          5-1-12-8-4-1 @ "A_04, 3초 기다렸다가 스킬 써." @ 1 @ wait_then_skill @ accepted_20260514_002741.jsonl_seed_master_0074
      empty_action_expected [4.1%(5%) / 3]
        selected_actor_dead [100.0%(6%) / 3]
          5-1-12-13-8-1 @ "A_04, 지금 자리에서 대기해." @ 3 @ named_actor_dead @ 2accepted_20260515_011221.jsonl_2batch_0044_001, 2accepted_20260515_011221.jsonl_2batch_0044_002, accepted_20260514_002743.jsonl_seed_master_0198
  explicit_multi_actor [17.6%(15%) / 28]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 28]
      wait_only [50.0%(65%) / 14]
        multi_actor_wait [100.0%(8%) / 14]
          5-2-12-6-6-1 @ "A_03과 A_04는 잠깐 대기해." @ 14 @ [] @ 2accepted_20260515_012354.jsonl_2batch_0045_001, 2accepted_20260515_012354.jsonl_2batch_0045_002, 2accepted_20260515_012354.jsonl_2batch_0045_003, 2accepted_20260515_012354.jsonl_2batch_0045_004, 2accepted_20260515_012354.jsonl_2batch_0045_005, 2accepted_20260515_012354.jsonl_2batch_0045_006, 2accepted_20260515_012354.jsonl_2batch_0045_007, 2accepted_20260515_012354.jsonl_2batch_0045_008, 2accepted_20260515_012354.jsonl_2batch_0045_009, 2accepted_20260515_012354.jsonl_2batch_0045_010, 2accepted_20260515_012736.jsonl_2batch_0046_001, 2accepted_20260515_012736.jsonl_2batch_0046_002, 2accepted_20260515_012736.jsonl_2batch_0046_003, accepted_20260514_002743.jsonl_seed_master_0199
      wait_then_attack [42.9%(20%) / 12]
        wait_then_attack_valid [100.0%(15%) / 12]
          5-2-12-7-3-1 @ "A_03과 A_04는 잠깐 기다렸다가 공격해." @ 12 @ wait_then_attack @ 2accepted_20260515_014000.jsonl_2batch_0047_001, 2accepted_20260515_014000.jsonl_2batch_0047_002, 2accepted_20260515_014000.jsonl_2batch_0047_003, 2accepted_20260515_014000.jsonl_2batch_0047_004, 2accepted_20260515_014000.jsonl_2batch_0047_005, 2accepted_20260515_014000.jsonl_2batch_0047_006, 2accepted_20260515_014000.jsonl_2batch_0047_007, 2accepted_20260515_014000.jsonl_2batch_0047_008, 2accepted_20260515_014000.jsonl_2batch_0047_009, 2accepted_20260515_014000.jsonl_2batch_0047_010, 2accepted_20260515_014120.jsonl_2batch_0048_001, accepted_20260514_002743.jsonl_seed_master_0200
      empty_action_expected [7.1%(5%) / 2]
        selected_actor_dead [100.0%(6%) / 2]
          5-2-12-13-8-1 @ "A_03과 A_04는 잠깐 대기해." @ 2 @ named_actor_dead @ 2accepted_20260515_014336.jsonl_2batch_0049_001, accepted_20260514_002743.jsonl_seed_master_0202
  global_condition [10.1%(15%) / 16]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 16]
      wait_only [100.0%(65%) / 16]
        hold_position_wait [100.0%(10%) / 16]
          5-3-12-6-5-1 @ "위험한 아군은 잠깐 대기하면서 버텨." @ 16 @ [] @ 2accepted_20260515_015443.jsonl_2batch_0050_001, 2accepted_20260515_015443.jsonl_2batch_0050_002, 2accepted_20260515_015443.jsonl_2batch_0050_003, 2accepted_20260515_015443.jsonl_2batch_0050_004, 2accepted_20260515_015443.jsonl_2batch_0050_005, 2accepted_20260515_015443.jsonl_2batch_0050_006, 2accepted_20260515_015443.jsonl_2batch_0050_007, 2accepted_20260515_015443.jsonl_2batch_0050_008, 2accepted_20260515_015443.jsonl_2batch_0050_009, 2accepted_20260515_015443.jsonl_2batch_0050_010, 2accepted_20260515_020039.jsonl_2batch_0051_001, 2accepted_20260515_020039.jsonl_2batch_0051_002, 2accepted_20260515_020039.jsonl_2batch_0051_003, 2accepted_20260515_020039.jsonl_2batch_0051_004, 2accepted_20260515_020039.jsonl_2batch_0051_005, accepted_20260514_002743.jsonl_seed_master_0203
  no_valid_actor [12.6%(10%) / 20]
    explicit_enemy_target [0.0%(10%) / 0]
    none [100.0%(90%) / 20]
      empty_action_expected [100.0%(5%) / 20]
        no_matching_wait_actor [55.0%(6%) / 11]
          5-6-12-13-7-1 @ "체력이 낮은 아군은 잠깐 대기해." @ 11 @ no_matching_actor @ 2accepted_20260515_021101.jsonl_2batch_0052_001, 2accepted_20260515_021101.jsonl_2batch_0052_002, 2accepted_20260515_021101.jsonl_2batch_0052_003, 2accepted_20260515_021101.jsonl_2batch_0052_004, 2accepted_20260515_021101.jsonl_2batch_0052_005, 2accepted_20260515_021101.jsonl_2batch_0052_006, 2accepted_20260515_021101.jsonl_2batch_0052_007, 2accepted_20260515_021101.jsonl_2batch_0052_008, 2accepted_20260515_021101.jsonl_2batch_0052_009, 2accepted_20260515_021101.jsonl_2batch_0052_010, accepted_20260514_002741.jsonl_seed_master_0077
        selected_actor_dead [45.0%(6%) / 9]
          5-6-12-13-8-1 @ "A_04, 지금 자리에서 대기해." @ 9 @ named_actor_dead @ 2accepted_20260515_022247.jsonl_2batch_0053_001, 2accepted_20260515_022247.jsonl_2batch_0053_002, 2accepted_20260515_022247.jsonl_2batch_0053_003, 2accepted_20260515_022247.jsonl_2batch_0053_004, 2accepted_20260515_022247.jsonl_2batch_0053_005, 2accepted_20260515_022247.jsonl_2batch_0053_006, 2accepted_20260515_022247.jsonl_2batch_0053_007, 2accepted_20260515_022247.jsonl_2batch_0053_008, accepted_20260514_002741.jsonl_seed_master_0078

empty [11.3%(12%) / 215]
  explicit_actor [40.0%(30%) / 86]
    explicit_enemy_target [72.1%(20%) / 62]
      empty_action_expected [100.0%(100%) / 62]
        named_actor_dead [3.2%(12%) / 2]
          6-1-1-13-1-1 @ "A_01, E_02를 공격해." @ 2 @ named_actor_dead @ 2accepted_20260515_022357.jsonl_2batch_0054_001, accepted_20260514_002745.jsonl_seed_master_0205
        named_target_dead [27.4%(10%) / 17]
          6-1-1-13-3-1 @ "A_01, E_02를 공격해." @ 17 @ named_target_dead @ 2accepted_20260515_023509.jsonl_2batch_0055_001, 2accepted_20260515_023509.jsonl_2batch_0055_002, 2accepted_20260515_023509.jsonl_2batch_0055_003, 2accepted_20260515_023509.jsonl_2batch_0055_004, 2accepted_20260515_023509.jsonl_2batch_0055_005, 2accepted_20260515_023509.jsonl_2batch_0055_006, 2accepted_20260515_023509.jsonl_2batch_0055_007, 2accepted_20260515_023509.jsonl_2batch_0055_008, 2accepted_20260515_023509.jsonl_2batch_0055_009, 2accepted_20260515_023509.jsonl_2batch_0055_010, 2accepted_20260515_024258.jsonl_2batch_0056_001, 2accepted_20260515_024258.jsonl_2batch_0056_002, 2accepted_20260515_024258.jsonl_2batch_0056_003, 2accepted_20260515_024258.jsonl_2batch_0056_004, 2accepted_20260515_024258.jsonl_2batch_0056_006, 2accepted_20260515_024258.jsonl_2batch_0056_007, accepted_20260514_002741.jsonl_seed_master_0081
        named_target_untargetable [9.7%(10%) / 6]
          6-1-1-13-4-1 @ "A_01, E_02를 공격해." @ 6 @ named_target_untargetable @ 2accepted_20260515_025410.jsonl_2batch_0057_004, 2accepted_20260515_030211.jsonl_2batch_0058_002, 2accepted_20260515_030211.jsonl_2batch_0058_003, 2accepted_20260515_030211.jsonl_2batch_0058_004, 2accepted_20260515_030211.jsonl_2batch_0058_007, accepted_20260514_002741.jsonl_seed_master_0082
        actor_outside_allowedActors [45.2%(8%) / 28]
          6-1-1-13-5-1 @ "A_01, E_02를 공격해." @ 28 @ actor_outside_allowedActors @ 2accepted_20260515_032442.jsonl_2batch_0059_001, 2accepted_20260515_032442.jsonl_2batch_0059_002, 2accepted_20260515_032442.jsonl_2batch_0059_006, 2accepted_20260515_032442.jsonl_2batch_0059_007, 2accepted_20260515_032442.jsonl_2batch_0059_008, 2accepted_20260515_032442.jsonl_2batch_0059_009, 2accepted_20260515_032442.jsonl_2batch_0059_010, 2accepted_20260515_033328.jsonl_2batch_0060_003, 2accepted_20260515_033328.jsonl_2batch_0060_004, 2accepted_20260515_033328.jsonl_2batch_0060_005, 2accepted_20260515_033328.jsonl_2batch_0060_006, 2accepted_20260515_033328.jsonl_2batch_0060_007, 2accepted_20260515_040240.jsonl_2batch_0063_001, 2accepted_20260515_040240.jsonl_2batch_0063_002, 2accepted_20260515_040240.jsonl_2batch_0063_003, 2accepted_20260515_040240.jsonl_2batch_0063_004, 2accepted_20260515_040240.jsonl_2batch_0063_005, 2accepted_20260515_040240.jsonl_2batch_0063_006, 2accepted_20260515_040240.jsonl_2batch_0063_007, 2accepted_20260515_040240.jsonl_2batch_0063_008, 2accepted_20260515_040240.jsonl_2batch_0063_009, 2accepted_20260515_040240.jsonl_2batch_0063_010, 2accepted_20260515_041127.jsonl_2batch_0064_001, 2accepted_20260515_041127.jsonl_2batch_0064_003, 2accepted_20260515_041127.jsonl_2batch_0064_004, 2accepted_20260515_041127.jsonl_2batch_0064_006, 2accepted_20260515_041127.jsonl_2batch_0064_008, accepted_20260514_002741.jsonl_seed_master_0080
        attack_target_outside_allowedTargets [14.5%(8%) / 9]
          6-1-1-13-6-1 @ "A_01, E_02를 공격해." @ 9 @ attack_target_outside_allowedTargets @ 2accepted_20260515_034437.jsonl_2batch_0061_004, 2accepted_20260515_042234.jsonl_2batch_0065_002, 2accepted_20260515_042234.jsonl_2batch_0065_005, 2accepted_20260515_042234.jsonl_2batch_0065_006, 2accepted_20260515_042234.jsonl_2batch_0065_007, 2accepted_20260515_042234.jsonl_2batch_0065_008, 2accepted_20260515_042234.jsonl_2batch_0065_009, 2accepted_20260515_042703.jsonl_2batch_0066_003, accepted_20260514_002741.jsonl_seed_master_0083
    explicit_ally_target [1.2%(15%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_target_dead_not_allowed [100.0%(8%) / 1]
          6-1-2-13-8-1 @ "A_04, 쓰러진 A_02에게 보호 스킬 써." @ 1 @ skill_target_dead_not_allowed @ accepted_20260514_002741.jsonl_seed_master_0084
    invalid_explicit_target [23.3%(30%) / 20]
      empty_action_expected [100.0%(100%) / 20]
        move_to_self_attempt [75.0%(6%) / 15]
          6-1-11-13-7-1 @ "A_02, 네 위치로 다시 붙어." @ 15 @ move_to_self_attempt @ 2accepted_20260515_043842.jsonl_2batch_0067_001, 2accepted_20260515_043842.jsonl_2batch_0067_002, 2accepted_20260515_043842.jsonl_2batch_0067_003, 2accepted_20260515_043842.jsonl_2batch_0067_004, 2accepted_20260515_043842.jsonl_2batch_0067_005, 2accepted_20260515_043842.jsonl_2batch_0067_006, 2accepted_20260515_043842.jsonl_2batch_0067_007, 2accepted_20260515_043842.jsonl_2batch_0067_008, 2accepted_20260515_043842.jsonl_2batch_0067_009, 2accepted_20260515_043842.jsonl_2batch_0067_010, 2accepted_20260515_044318.jsonl_2batch_0068_001, 2accepted_20260515_044318.jsonl_2batch_0068_002, 2accepted_20260515_044318.jsonl_2batch_0068_003, 2accepted_20260515_044318.jsonl_2batch_0068_004, accepted_20260514_002741.jsonl_seed_master_0085
        skill_actor_has_no_skill [25.0%(8%) / 5]
          6-1-11-13-9-1 @ "A_03, E_02한테 스킬 써." @ 5 @ actor_has_no_skill @ 2accepted_20260515_044753.jsonl_2batch_0069_001, 2accepted_20260515_044753.jsonl_2batch_0069_002, 2accepted_20260515_044753.jsonl_2batch_0069_003, 2accepted_20260515_044753.jsonl_2batch_0069_004, accepted_20260514_002741.jsonl_seed_master_0086
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [3.5%(20%) / 3]
      empty_action_expected [100.0%(100%) / 3]
        named_actor_dead [66.7%(12%) / 2]
          6-1-12-13-1-1 @ "A_01, 지금 공격할 수 있는 적을 찾아 공격해." @ 2 @ named_actor_dead @ 2accepted_20260515_044903.jsonl_2batch_0070_001, accepted_20260514_002745.jsonl_seed_master_0206
        no_valid_target [33.3%(8%) / 1]
          6-1-12-13-12-1 @ "A_01, 지금 공격할 수 있는 적을 공격해." @ 1 @ no_valid_target @ accepted_20260514_002745.jsonl_seed_master_0207
  explicit_multi_actor [17.7%(10%) / 38]
    explicit_enemy_target [97.4%(20%) / 37]
      empty_action_expected [100.0%(100%) / 37]
        all_named_actors_dead [40.5%(6%) / 15]
          6-2-1-13-2-1 @ "A_01과 A_02는 E_02를 공격해." @ 15 @ all_named_actors_dead @ 2accepted_20260515_050126.jsonl_2batch_0072_001, 2accepted_20260515_050126.jsonl_2batch_0072_002, 2accepted_20260515_050126.jsonl_2batch_0072_003, 2accepted_20260515_050126.jsonl_2batch_0072_004, 2accepted_20260515_050126.jsonl_2batch_0072_005, 2accepted_20260515_050126.jsonl_2batch_0072_006, 2accepted_20260515_050126.jsonl_2batch_0072_007, 2accepted_20260515_050126.jsonl_2batch_0072_008, 2accepted_20260515_050126.jsonl_2batch_0072_009, 2accepted_20260515_050126.jsonl_2batch_0072_010, 2accepted_20260515_050559.jsonl_2batch_0073_001, 2accepted_20260515_050559.jsonl_2batch_0073_002, 2accepted_20260515_050559.jsonl_2batch_0073_003, 2accepted_20260515_050559.jsonl_2batch_0073_004, accepted_20260514_002741.jsonl_seed_master_0087
        named_target_dead [21.6%(10%) / 8]
          6-2-1-13-3-1 @ "A_01과 A_02는 E_02를 공격해." @ 8 @ named_target_dead @ 2accepted_20260515_051348.jsonl_2batch_0074_001, 2accepted_20260515_051348.jsonl_2batch_0074_002, 2accepted_20260515_051348.jsonl_2batch_0074_003, 2accepted_20260515_051348.jsonl_2batch_0074_004, 2accepted_20260515_051348.jsonl_2batch_0074_005, 2accepted_20260515_051348.jsonl_2batch_0074_006, 2accepted_20260515_051348.jsonl_2batch_0074_007, accepted_20260514_002745.jsonl_seed_master_0209
        named_target_untargetable [21.6%(10%) / 8]
          6-2-1-13-4-1 @ "A_01과 A_02는 E_02를 공격해." @ 8 @ named_target_untargetable @ 2accepted_20260515_052143.jsonl_2batch_0075_001, 2accepted_20260515_052143.jsonl_2batch_0075_002, 2accepted_20260515_052143.jsonl_2batch_0075_003, 2accepted_20260515_052143.jsonl_2batch_0075_004, 2accepted_20260515_052143.jsonl_2batch_0075_005, 2accepted_20260515_052143.jsonl_2batch_0075_006, 2accepted_20260515_052143.jsonl_2batch_0075_007, accepted_20260514_002745.jsonl_seed_master_0210
        attack_target_outside_allowedTargets [16.2%(8%) / 6]
          6-2-1-13-6-1 @ "A_01과 A_02는 E_02를 공격해." @ 6 @ attack_target_outside_allowedTargets @ 2accepted_20260515_052840.jsonl_2batch_0076_001, 2accepted_20260515_052840.jsonl_2batch_0076_002, 2accepted_20260515_052840.jsonl_2batch_0076_003, 2accepted_20260515_052840.jsonl_2batch_0076_005, 2accepted_20260515_052840.jsonl_2batch_0076_006, accepted_20260514_002745.jsonl_seed_master_0208
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [2.6%(30%) / 1]
      empty_action_expected [100.0%(100%) / 1]
        skill_actor_has_no_skill [100.0%(8%) / 1]
          6-2-11-13-9-1 @ "A_03과 A_04는 죽은 E_02한테 스킬 써." @ 1 @ actor_has_no_skill, named_target_dead @ accepted_20260514_002745.jsonl_seed_master_0211
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [0.0%(20%) / 0]
  global_condition [11.6%(25%) / 25]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [32.0%(5%) / 8]
      empty_action_expected [100.0%(100%) / 8]
        no_matching_actor [100.0%(10%) / 8]
          6-3-9-13-10-1 @ "체력이 낮은 아군을 도울 수 있는 아군은 붙어." @ 8 @ no_matching_actor, low_hp_ally_target @ 2accepted_20260515_054304.jsonl_2batch_0078_001, 2accepted_20260515_054304.jsonl_2batch_0078_002, 2accepted_20260515_054304.jsonl_2batch_0078_003, 2accepted_20260515_054304.jsonl_2batch_0078_004, 2accepted_20260515_054304.jsonl_2batch_0078_005, 2accepted_20260515_054304.jsonl_2batch_0078_006, 2accepted_20260515_054304.jsonl_2batch_0078_007, accepted_20260514_002745.jsonl_seed_master_0212
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [68.0%(20%) / 17]
      empty_action_expected [100.0%(100%) / 17]
        no_matching_actor [100.0%(10%) / 17]
          6-3-12-13-10-1 @ "체력이 낮은 아군은 뒤로 빠져." @ 17 @ no_matching_actor @ 2accepted_20260515_055343.jsonl_2batch_0079_001, 2accepted_20260515_055343.jsonl_2batch_0079_002, 2accepted_20260515_055343.jsonl_2batch_0079_003, 2accepted_20260515_055343.jsonl_2batch_0079_004, 2accepted_20260515_055343.jsonl_2batch_0079_005, 2accepted_20260515_055343.jsonl_2batch_0079_006, 2accepted_20260515_055343.jsonl_2batch_0079_007, 2accepted_20260515_055343.jsonl_2batch_0079_008, 2accepted_20260515_055343.jsonl_2batch_0079_009, 2accepted_20260515_055343.jsonl_2batch_0079_010, 2accepted_20260515_060007.jsonl_2batch_0080_001, 2accepted_20260515_060007.jsonl_2batch_0080_002, 2accepted_20260515_060007.jsonl_2batch_0080_003, 2accepted_20260515_060007.jsonl_2batch_0080_004, 2accepted_20260515_060007.jsonl_2batch_0080_005, 2accepted_20260515_060007.jsonl_2batch_0080_006, accepted_20260514_002741.jsonl_seed_master_0088
  global_role_based [7.9%(15%) / 17]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [35.3%(5%) / 6]
      empty_action_expected [100.0%(100%) / 6]
        no_matching_role_actor [100.0%(6%) / 6]
          6-4-6-13-11-1 @ "원거리 아군은 적 후열을 공격해." @ 6 @ no_matching_role_actor @ 2accepted_20260515_060539.jsonl_2batch_0081_001, 2accepted_20260515_060539.jsonl_2batch_0081_002, 2accepted_20260515_060539.jsonl_2batch_0081_003, 2accepted_20260515_060539.jsonl_2batch_0081_004, 2accepted_20260515_060539.jsonl_2batch_0081_005, accepted_20260514_002741.jsonl_seed_master_0089
    lowest_hp_enemy [0.0%(5%) / 0]
    none [64.7%(20%) / 11]
      empty_action_expected [100.0%(100%) / 11]
        no_matching_role_actor [100.0%(6%) / 11]
          6-4-12-13-11-1 @ "전열 아군은 앞으로 버텨." @ 11 @ no_matching_role_actor @ 2accepted_20260515_061601.jsonl_2batch_0082_001, 2accepted_20260515_061601.jsonl_2batch_0082_002, 2accepted_20260515_061601.jsonl_2batch_0082_003, 2accepted_20260515_061601.jsonl_2batch_0082_004, 2accepted_20260515_061601.jsonl_2batch_0082_005, 2accepted_20260515_061601.jsonl_2batch_0082_006, 2accepted_20260515_061601.jsonl_2batch_0082_007, 2accepted_20260515_061601.jsonl_2batch_0082_008, 2accepted_20260515_061601.jsonl_2batch_0082_009, 2accepted_20260515_061601.jsonl_2batch_0082_010, accepted_20260514_002745.jsonl_seed_master_0213
  global_state_based [8.8%(10%) / 19]
    explicit_enemy_target [0.0%(20%) / 0]
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [26.3%(5%) / 5]
      empty_action_expected [100.0%(100%) / 5]
        no_valid_target [100.0%(8%) / 5]
          6-5-6-13-12-1 @ "공격 가능한 아군은 적 후열을 공격해." @ 5 @ no_valid_target, target_role_backline_enemy @ 2accepted_20260515_062232.jsonl_2batch_0083_002, 2accepted_20260515_062232.jsonl_2batch_0083_004, 2accepted_20260515_062232.jsonl_2batch_0083_005, 2accepted_20260515_062232.jsonl_2batch_0083_006, accepted_20260514_002745.jsonl_seed_master_0214
    lowest_hp_enemy [73.7%(5%) / 14]
      empty_action_expected [100.0%(100%) / 14]
        no_valid_target [100.0%(8%) / 14]
          6-5-4-13-12-1 @ "공격 가능한 아군은 체력이 제일 낮은 적을 공격해." @ 14 @ no_valid_target @ 2accepted_20260515_063229.jsonl_2batch_0084_001, 2accepted_20260515_063229.jsonl_2batch_0084_002, 2accepted_20260515_063229.jsonl_2batch_0084_003, 2accepted_20260515_063229.jsonl_2batch_0084_004, 2accepted_20260515_063229.jsonl_2batch_0084_005, 2accepted_20260515_063229.jsonl_2batch_0084_006, 2accepted_20260515_063229.jsonl_2batch_0084_007, 2accepted_20260515_063229.jsonl_2batch_0084_008, 2accepted_20260515_063229.jsonl_2batch_0084_009, 2accepted_20260515_063229.jsonl_2batch_0084_010, 2accepted_20260515_063540.jsonl_2batch_0085_001, 2accepted_20260515_063540.jsonl_2batch_0085_002, 2accepted_20260515_063540.jsonl_2batch_0085_003, accepted_20260514_002741.jsonl_seed_master_0090
    none [0.0%(20%) / 0]
  no_valid_actor [14.0%(10%) / 30]
    explicit_enemy_target [93.3%(20%) / 28]
      empty_action_expected [100.0%(100%) / 28]
        named_actor_dead [100.0%(12%) / 28]
          6-6-1-13-1-1 @ "A_01, E_02를 공격해." @ 28 @ named_actor_dead @ 2accepted_20260515_064641.jsonl_2batch_0086_001, 2accepted_20260515_064641.jsonl_2batch_0086_002, 2accepted_20260515_064641.jsonl_2batch_0086_003, 2accepted_20260515_064641.jsonl_2batch_0086_004, 2accepted_20260515_064641.jsonl_2batch_0086_005, 2accepted_20260515_064641.jsonl_2batch_0086_006, 2accepted_20260515_064641.jsonl_2batch_0086_007, 2accepted_20260515_064641.jsonl_2batch_0086_008, 2accepted_20260515_064641.jsonl_2batch_0086_009, 2accepted_20260515_064641.jsonl_2batch_0086_010, 2accepted_20260515_065742.jsonl_2batch_0087_001, 2accepted_20260515_065742.jsonl_2batch_0087_002, 2accepted_20260515_065742.jsonl_2batch_0087_003, 2accepted_20260515_065742.jsonl_2batch_0087_004, 2accepted_20260515_065742.jsonl_2batch_0087_005, 2accepted_20260515_065742.jsonl_2batch_0087_006, 2accepted_20260515_065742.jsonl_2batch_0087_007, 2accepted_20260515_065742.jsonl_2batch_0087_008, 2accepted_20260515_065742.jsonl_2batch_0087_009, 2accepted_20260515_065742.jsonl_2batch_0087_010, 2accepted_20260515_070539.jsonl_2batch_0088_001, 2accepted_20260515_070539.jsonl_2batch_0088_002, 2accepted_20260515_070539.jsonl_2batch_0088_003, 2accepted_20260515_070539.jsonl_2batch_0088_004, 2accepted_20260515_070539.jsonl_2batch_0088_005, 2accepted_20260515_070539.jsonl_2batch_0088_006, 2accepted_20260515_070539.jsonl_2batch_0088_007, accepted_20260514_002745.jsonl_seed_master_0215
    explicit_ally_target [0.0%(15%) / 0]
    invalid_explicit_target [0.0%(30%) / 0]
    low_hp_ally [0.0%(5%) / 0]
    role_based_enemy [0.0%(5%) / 0]
    lowest_hp_enemy [0.0%(5%) / 0]
    none [6.7%(20%) / 2]
      empty_action_expected [100.0%(100%) / 2]
        no_matching_actor [100.0%(10%) / 2]
          6-6-12-13-10-1 @ "살아있는 아군은 전부 후퇴해." @ 2 @ no_valid_actor @ 2accepted_20260515_070648.jsonl_2batch_0089_001, accepted_20260514_002741.jsonl_seed_master_0091
