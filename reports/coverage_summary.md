# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 22.2% | 24% | 43 |
| move | 20.1% | 22% | 39 |
| skill | 29.9% | 26% | 58 |
| skillControl | 6.7% | 8% | 13 |
| wait | 9.3% | 8% | 18 |
| empty | 11.9% | 12% | 23 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 59.8% | 40% | 116 |
| explicit_multi_actor | 19.6% | 12% | 38 |
| global_condition | 5.7% | 16% | 11 |
| global_role_based | 4.1% | 12% | 8 |
| global_state_based | 4.6% | 15% | 9 |
| no_valid_actor | 6.2% | 5% | 12 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 24.2% | 21% | 47 |
| explicit_ally_target | 12.9% | 13% | 25 |
| nearest_enemy | 4.1% | 8% | 8 |
| lowest_hp_enemy | 5.7% | 8% | 11 |
| highest_threat_enemy | 2.6% | 7% | 5 |
| role_based_enemy | 9.3% | 8% | 18 |
| pressure_source_enemy | 3.1% | 6% | 6 |
| safe_ally | 4.6% | 6% | 9 |
| low_hp_ally | 5.2% | 6% | 10 |
| backline_ally | 1.0% | 4% | 2 |
| invalid_explicit_target | 5.2% | 7% | 10 |
| none | 22.2% | 6% | 43 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 8.2% | 13% | 16 |
| move_only | 11.3% | 13% | 22 |
| move_then_attack | 9.3% | 11% | 18 |
| skill_only | 21.1% | 19% | 41 |
| move_then_skill | 2.1% | 4% | 4 |
| wait_only | 3.1% | 6% | 6 |
| wait_then_attack | 2.1% | 3% | 4 |
| wait_then_skill | 2.1% | 2% | 4 |
| skillControl_defer | 1.5% | 4% | 3 |
| skillControl_forbid | 2.1% | 4% | 4 |
| multi_actor_same_target | 7.7% | 6% | 15 |
| multi_actor_different_targets | 4.1% | 3% | 8 |
| empty_action_expected | 25.3% | 12% | 49 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 58.2% | 35% | 113 |
| casual_korean | 21.6% | 20% | 42 |
| elliptical_korean | 2.6% | 20% | 5 |
| tactical_korean | 17.0% | 15% | 33 |
| rough_korean | 0.5% | 10% | 1 |

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
