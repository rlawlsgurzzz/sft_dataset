# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 17.8% | 24% | 19 |
| move | 15.9% | 22% | 17 |
| skill | 39.3% | 26% | 42 |
| skillControl | 8.4% | 8% | 9 |
| wait | 7.5% | 8% | 8 |
| empty | 11.2% | 12% | 12 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 74.8% | 40% | 80 |
| explicit_multi_actor | 6.5% | 12% | 7 |
| global_condition | 3.7% | 16% | 4 |
| global_role_based | 4.7% | 12% | 5 |
| global_state_based | 3.7% | 15% | 4 |
| no_valid_actor | 6.5% | 5% | 7 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 29.9% | 21% | 32 |
| explicit_ally_target | 21.5% | 13% | 23 |
| nearest_enemy | 1.9% | 8% | 2 |
| lowest_hp_enemy | 2.8% | 8% | 3 |
| highest_threat_enemy | 1.9% | 7% | 2 |
| role_based_enemy | 5.6% | 8% | 6 |
| pressure_source_enemy | 1.9% | 6% | 2 |
| safe_ally | 4.7% | 6% | 5 |
| low_hp_ally | 2.8% | 6% | 3 |
| backline_ally | 0.0% | 4% | 0 |
| invalid_explicit_target | 1.9% | 7% | 2 |
| none | 25.2% | 6% | 27 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 9.3% | 13% | 10 |
| move_only | 12.1% | 13% | 13 |
| move_then_attack | 4.7% | 11% | 5 |
| skill_only | 36.4% | 19% | 39 |
| move_then_skill | 0.9% | 4% | 1 |
| wait_only | 3.7% | 6% | 4 |
| wait_then_attack | 0.9% | 3% | 1 |
| wait_then_skill | 0.9% | 2% | 1 |
| skillControl_defer | 3.7% | 4% | 4 |
| skillControl_forbid | 3.7% | 4% | 4 |
| multi_actor_same_target | 4.7% | 6% | 5 |
| multi_actor_different_targets | 1.9% | 3% | 2 |
| empty_action_expected | 16.8% | 12% | 18 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 47.7% | 35% | 51 |
| casual_korean | 32.7% | 20% | 35 |
| elliptical_korean | 0.9% | 20% | 1 |
| tactical_korean | 18.7% | 15% | 20 |
| rough_korean | 0.0% | 10% | 0 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 15.6% | 18% | 7 |
| self_buff | 15.6% | 14% | 7 |
| ally_shield | 15.6% | 13% | 7 |
| ally_heal | 13.3% | 11% | 6 |
| ally_resurrection | 8.9% | 13% | 4 |
| enemy_aoe_attack | 8.9% | 12% | 4 |
| enemy_debuff | 8.9% | 8% | 4 |
| mobility_skill | 4.4% | 5% | 2 |
| no_skill | 8.9% | 6% | 4 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 28.9% | 36% | 13 |
| ally_alive | 24.4% | 22% | 11 |
| self | 17.8% | 16% | 8 |
| ally_dead | 13.3% | 12% | 6 |
| enemy_dead | 6.7% | 5% | 3 |
| none | 8.9% | 9% | 4 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 48.9% | 48% | 22 |
| text_enemy_target_but_self_skill | 4.4% | 8% | 2 |
| text_enemy_target_but_ally_skill | 6.7% | 9% | 3 |
| text_ally_target_but_enemy_skill | 8.9% | 9% | 4 |
| text_dead_target_but_skill_cannot_target_dead | 15.6% | 8% | 7 |
| text_living_target_but_resurrection_skill | 4.4% | 6% | 2 |
| skill_actor_has_no_skill | 8.9% | 7% | 4 |

## Taxonomy Errors

No taxonomy errors found.
