# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 26.7% | 24% | 44 |
| move | 24.2% | 22% | 40 |
| skill | 31.5% | 26% | 52 |
| skillControl | 5.5% | 8% | 9 |
| wait | 4.8% | 8% | 8 |
| empty | 7.3% | 12% | 12 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 70.3% | 40% | 116 |
| explicit_multi_actor | 12.7% | 12% | 21 |
| global_condition | 3.6% | 16% | 6 |
| global_role_based | 4.2% | 12% | 7 |
| global_state_based | 4.2% | 15% | 7 |
| no_valid_actor | 4.8% | 5% | 8 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 23.0% | 21% | 38 |
| explicit_ally_target | 15.8% | 13% | 26 |
| nearest_enemy | 4.8% | 8% | 8 |
| lowest_hp_enemy | 6.1% | 8% | 10 |
| highest_threat_enemy | 3.0% | 7% | 5 |
| role_based_enemy | 9.7% | 8% | 16 |
| pressure_source_enemy | 4.2% | 6% | 7 |
| safe_ally | 6.1% | 6% | 10 |
| low_hp_ally | 4.2% | 6% | 7 |
| backline_ally | 1.2% | 4% | 2 |
| invalid_explicit_target | 4.2% | 7% | 7 |
| none | 17.6% | 6% | 29 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 10.3% | 13% | 17 |
| move_only | 13.9% | 13% | 23 |
| move_then_attack | 10.9% | 11% | 18 |
| skill_only | 28.5% | 19% | 47 |
| move_then_skill | 2.4% | 4% | 4 |
| wait_only | 2.4% | 6% | 4 |
| wait_then_attack | 0.6% | 3% | 1 |
| wait_then_skill | 0.6% | 2% | 1 |
| skillControl_defer | 2.4% | 4% | 4 |
| skillControl_forbid | 2.4% | 4% | 4 |
| multi_actor_same_target | 6.7% | 6% | 11 |
| multi_actor_different_targets | 3.0% | 3% | 5 |
| empty_action_expected | 15.8% | 12% | 26 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 61.2% | 35% | 101 |
| casual_korean | 23.0% | 20% | 38 |
| elliptical_korean | 1.8% | 20% | 3 |
| tactical_korean | 13.3% | 15% | 22 |
| rough_korean | 0.6% | 10% | 1 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 18.2% | 18% | 10 |
| self_buff | 12.7% | 14% | 7 |
| ally_shield | 12.7% | 13% | 7 |
| ally_heal | 12.7% | 11% | 7 |
| ally_resurrection | 7.3% | 13% | 4 |
| enemy_aoe_attack | 14.5% | 12% | 8 |
| enemy_debuff | 10.9% | 8% | 6 |
| mobility_skill | 3.6% | 5% | 2 |
| no_skill | 7.3% | 6% | 4 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 40.0% | 36% | 22 |
| ally_alive | 21.8% | 22% | 12 |
| self | 14.5% | 16% | 8 |
| ally_dead | 10.9% | 12% | 6 |
| enemy_dead | 5.5% | 5% | 3 |
| none | 7.3% | 9% | 4 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 58.2% | 48% | 32 |
| text_enemy_target_but_self_skill | 3.6% | 8% | 2 |
| text_enemy_target_but_ally_skill | 5.5% | 9% | 3 |
| text_ally_target_but_enemy_skill | 7.3% | 9% | 4 |
| text_dead_target_but_skill_cannot_target_dead | 12.7% | 8% | 7 |
| text_living_target_but_resurrection_skill | 3.6% | 6% | 2 |
| skill_actor_has_no_skill | 7.3% | 7% | 4 |

## Taxonomy Errors

No taxonomy errors found.
