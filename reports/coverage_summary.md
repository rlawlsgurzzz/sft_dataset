# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 66.8% | 24% | 408 |
| move | 15.4% | 22% | 94 |
| skill | 9.5% | 26% | 58 |
| skillControl | 2.1% | 8% | 13 |
| wait | 2.5% | 8% | 15 |
| empty | 3.8% | 12% | 23 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 58.1% | 40% | 355 |
| explicit_multi_actor | 15.4% | 12% | 94 |
| global_condition | 9.2% | 16% | 56 |
| global_role_based | 7.7% | 12% | 47 |
| global_state_based | 7.7% | 15% | 47 |
| no_valid_actor | 2.0% | 5% | 12 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 25.5% | 21% | 156 |
| explicit_ally_target | 13.1% | 13% | 80 |
| nearest_enemy | 9.0% | 8% | 55 |
| lowest_hp_enemy | 9.2% | 8% | 56 |
| highest_threat_enemy | 9.8% | 7% | 60 |
| role_based_enemy | 10.5% | 8% | 64 |
| pressure_source_enemy | 5.2% | 6% | 32 |
| safe_ally | 1.5% | 6% | 9 |
| low_hp_ally | 1.6% | 6% | 10 |
| backline_ally | 0.3% | 4% | 2 |
| invalid_explicit_target | 7.7% | 7% | 47 |
| none | 6.5% | 6% | 40 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 24.2% | 13% | 148 |
| move_only | 11.1% | 13% | 68 |
| move_then_attack | 16.7% | 11% | 102 |
| skill_only | 6.7% | 19% | 41 |
| move_then_skill | 0.5% | 4% | 3 |
| wait_only | 1.0% | 6% | 6 |
| wait_then_attack | 0.7% | 3% | 4 |
| wait_then_skill | 0.2% | 2% | 1 |
| skillControl_defer | 0.5% | 4% | 3 |
| skillControl_forbid | 0.7% | 4% | 4 |
| multi_actor_same_target | 15.9% | 6% | 97 |
| multi_actor_different_targets | 7.9% | 3% | 48 |
| empty_action_expected | 14.1% | 12% | 86 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 48.1% | 35% | 294 |
| casual_korean | 21.3% | 20% | 130 |
| elliptical_korean | 5.4% | 20% | 33 |
| tactical_korean | 11.6% | 15% | 71 |
| rough_korean | 13.6% | 10% | 83 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 25.8% | 18% | 16 |
| self_buff | 4.8% | 14% | 3 |
| ally_shield | 9.7% | 13% | 6 |
| ally_heal | 16.1% | 11% | 10 |
| ally_resurrection | 4.8% | 13% | 3 |
| enemy_aoe_attack | 14.5% | 12% | 9 |
| enemy_debuff | 9.7% | 8% | 6 |
| mobility_skill | 3.2% | 5% | 2 |
| no_skill | 11.3% | 6% | 7 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 45.2% | 36% | 28 |
| ally_alive | 22.6% | 22% | 14 |
| self | 6.5% | 16% | 4 |
| ally_dead | 8.1% | 12% | 5 |
| enemy_dead | 6.5% | 5% | 4 |
| none | 11.3% | 9% | 7 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 61.3% | 48% | 38 |
| text_enemy_target_but_self_skill | 1.6% | 8% | 1 |
| text_enemy_target_but_ally_skill | 4.8% | 9% | 3 |
| text_ally_target_but_enemy_skill | 6.5% | 9% | 4 |
| text_dead_target_but_skill_cannot_target_dead | 11.3% | 8% | 7 |
| text_living_target_but_resurrection_skill | 1.6% | 6% | 1 |
| skill_actor_has_no_skill | 11.3% | 7% | 7 |

## Taxonomy Errors

No taxonomy errors found.
