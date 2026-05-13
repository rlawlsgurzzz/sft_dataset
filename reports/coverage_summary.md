# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 25.0% | 24% | 49 |
| move | 19.4% | 22% | 38 |
| skill | 29.6% | 26% | 58 |
| skillControl | 6.6% | 8% | 13 |
| wait | 7.7% | 8% | 15 |
| empty | 11.7% | 12% | 23 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 61.2% | 40% | 120 |
| explicit_multi_actor | 18.9% | 12% | 37 |
| global_condition | 5.1% | 16% | 10 |
| global_role_based | 4.1% | 12% | 8 |
| global_state_based | 4.6% | 15% | 9 |
| no_valid_actor | 6.1% | 5% | 12 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 27.0% | 21% | 53 |
| explicit_ally_target | 12.2% | 13% | 24 |
| nearest_enemy | 4.1% | 8% | 8 |
| lowest_hp_enemy | 5.6% | 8% | 11 |
| highest_threat_enemy | 2.6% | 7% | 5 |
| role_based_enemy | 9.2% | 8% | 18 |
| pressure_source_enemy | 3.1% | 6% | 6 |
| safe_ally | 4.6% | 6% | 9 |
| low_hp_ally | 5.1% | 6% | 10 |
| backline_ally | 1.0% | 4% | 2 |
| invalid_explicit_target | 5.1% | 7% | 10 |
| none | 20.4% | 6% | 40 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 11.2% | 13% | 22 |
| move_only | 11.2% | 13% | 22 |
| move_then_attack | 9.2% | 11% | 18 |
| skill_only | 20.9% | 19% | 41 |
| move_then_skill | 1.5% | 4% | 3 |
| wait_only | 3.1% | 6% | 6 |
| wait_then_attack | 2.0% | 3% | 4 |
| wait_then_skill | 0.5% | 2% | 1 |
| skillControl_defer | 1.5% | 4% | 3 |
| skillControl_forbid | 2.0% | 4% | 4 |
| multi_actor_same_target | 7.7% | 6% | 15 |
| multi_actor_different_targets | 4.1% | 3% | 8 |
| empty_action_expected | 25.0% | 12% | 49 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 59.2% | 35% | 116 |
| casual_korean | 21.4% | 20% | 42 |
| elliptical_korean | 2.6% | 20% | 5 |
| tactical_korean | 16.3% | 15% | 32 |
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
