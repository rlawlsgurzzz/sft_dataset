# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 21.3% | 24% | 44 |
| move | 19.3% | 22% | 40 |
| skill | 32.4% | 26% | 67 |
| skillControl | 6.8% | 8% | 14 |
| wait | 9.2% | 8% | 19 |
| empty | 11.1% | 12% | 23 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 61.8% | 40% | 128 |
| explicit_multi_actor | 18.8% | 12% | 39 |
| global_condition | 5.3% | 16% | 11 |
| global_role_based | 3.9% | 12% | 8 |
| global_state_based | 4.3% | 15% | 9 |
| no_valid_actor | 5.8% | 5% | 12 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 24.2% | 21% | 50 |
| explicit_ally_target | 13.5% | 13% | 28 |
| nearest_enemy | 3.9% | 8% | 8 |
| lowest_hp_enemy | 5.3% | 8% | 11 |
| highest_threat_enemy | 2.4% | 7% | 5 |
| role_based_enemy | 8.7% | 8% | 18 |
| pressure_source_enemy | 3.4% | 6% | 7 |
| safe_ally | 4.8% | 6% | 10 |
| low_hp_ally | 4.8% | 6% | 10 |
| backline_ally | 1.0% | 4% | 2 |
| invalid_explicit_target | 4.8% | 7% | 10 |
| none | 23.2% | 6% | 48 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 8.2% | 13% | 17 |
| move_only | 11.1% | 13% | 23 |
| move_then_attack | 8.7% | 11% | 18 |
| skill_only | 24.2% | 19% | 50 |
| move_then_skill | 1.9% | 4% | 4 |
| wait_only | 3.4% | 6% | 7 |
| wait_then_attack | 1.9% | 3% | 4 |
| wait_then_skill | 1.9% | 2% | 4 |
| skillControl_defer | 1.9% | 4% | 4 |
| skillControl_forbid | 1.9% | 4% | 4 |
| multi_actor_same_target | 7.2% | 6% | 15 |
| multi_actor_different_targets | 3.9% | 3% | 8 |
| empty_action_expected | 23.7% | 12% | 49 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 57.0% | 35% | 118 |
| casual_korean | 23.2% | 20% | 48 |
| elliptical_korean | 2.9% | 20% | 6 |
| tactical_korean | 16.4% | 15% | 34 |
| rough_korean | 0.5% | 10% | 1 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 23.9% | 18% | 17 |
| self_buff | 9.9% | 14% | 7 |
| ally_shield | 11.3% | 13% | 8 |
| ally_heal | 14.1% | 11% | 10 |
| ally_resurrection | 5.6% | 13% | 4 |
| enemy_aoe_attack | 12.7% | 12% | 9 |
| enemy_debuff | 8.5% | 8% | 6 |
| mobility_skill | 2.8% | 5% | 2 |
| no_skill | 11.3% | 6% | 8 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 39.4% | 36% | 28 |
| ally_alive | 22.5% | 22% | 16 |
| self | 11.3% | 16% | 8 |
| ally_dead | 8.5% | 12% | 6 |
| enemy_dead | 7.0% | 5% | 5 |
| none | 11.3% | 9% | 8 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 59.2% | 48% | 42 |
| text_enemy_target_but_self_skill | 2.8% | 8% | 2 |
| text_enemy_target_but_ally_skill | 4.2% | 9% | 3 |
| text_ally_target_but_enemy_skill | 5.6% | 9% | 4 |
| text_dead_target_but_skill_cannot_target_dead | 12.7% | 8% | 9 |
| text_living_target_but_resurrection_skill | 2.8% | 6% | 2 |
| skill_actor_has_no_skill | 11.3% | 7% | 8 |

## Taxonomy Errors

No taxonomy errors found.
