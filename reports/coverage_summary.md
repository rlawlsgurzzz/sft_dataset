# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 48.7% | 24% | 19 |
| move | 38.5% | 22% | 15 |
| skill | 7.7% | 26% | 3 |
| skillControl | 2.6% | 8% | 1 |
| wait | 2.6% | 8% | 1 |
| empty | 0.0% | 12% | 0 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 71.8% | 40% | 28 |
| explicit_multi_actor | 10.3% | 12% | 4 |
| global_condition | 7.7% | 16% | 3 |
| global_role_based | 7.7% | 12% | 3 |
| global_state_based | 2.6% | 15% | 1 |
| no_valid_actor | 0.0% | 5% | 0 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 28.2% | 21% | 11 |
| explicit_ally_target | 15.4% | 13% | 6 |
| nearest_enemy | 5.1% | 8% | 2 |
| lowest_hp_enemy | 5.1% | 8% | 2 |
| highest_threat_enemy | 5.1% | 7% | 2 |
| role_based_enemy | 10.3% | 8% | 4 |
| pressure_source_enemy | 5.1% | 6% | 2 |
| safe_ally | 10.3% | 6% | 4 |
| low_hp_ally | 2.6% | 6% | 1 |
| backline_ally | 0.0% | 4% | 0 |
| invalid_explicit_target | 0.0% | 7% | 0 |
| none | 12.8% | 6% | 5 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 25.6% | 13% | 10 |
| move_only | 30.8% | 13% | 12 |
| move_then_attack | 12.8% | 11% | 5 |
| skill_only | 7.7% | 19% | 3 |
| move_then_skill | 0.0% | 4% | 0 |
| wait_only | 2.6% | 6% | 1 |
| wait_then_attack | 0.0% | 3% | 0 |
| wait_then_skill | 0.0% | 2% | 0 |
| skillControl_defer | 2.6% | 4% | 1 |
| skillControl_forbid | 0.0% | 4% | 0 |
| multi_actor_same_target | 12.8% | 6% | 5 |
| multi_actor_different_targets | 5.1% | 3% | 2 |
| empty_action_expected | 0.0% | 12% | 0 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 43.6% | 35% | 17 |
| casual_korean | 20.5% | 20% | 8 |
| elliptical_korean | 2.6% | 20% | 1 |
| tactical_korean | 33.3% | 15% | 13 |
| rough_korean | 0.0% | 10% | 0 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 0.0% | 18% | 0 |
| self_buff | 33.3% | 14% | 1 |
| ally_shield | 33.3% | 13% | 1 |
| ally_heal | 0.0% | 11% | 0 |
| ally_resurrection | 0.0% | 13% | 0 |
| enemy_aoe_attack | 33.3% | 12% | 1 |
| enemy_debuff | 0.0% | 8% | 0 |
| mobility_skill | 0.0% | 5% | 0 |
| no_skill | 0.0% | 6% | 0 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 33.3% | 36% | 1 |
| ally_alive | 33.3% | 22% | 1 |
| self | 33.3% | 16% | 1 |
| ally_dead | 0.0% | 12% | 0 |
| enemy_dead | 0.0% | 5% | 0 |
| none | 0.0% | 9% | 0 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 100.0% | 48% | 3 |
| text_enemy_target_but_self_skill | 0.0% | 8% | 0 |
| text_enemy_target_but_ally_skill | 0.0% | 9% | 0 |
| text_ally_target_but_enemy_skill | 0.0% | 9% | 0 |
| text_dead_target_but_skill_cannot_target_dead | 0.0% | 8% | 0 |
| text_living_target_but_resurrection_skill | 0.0% | 6% | 0 |
| skill_actor_has_no_skill | 0.0% | 7% | 0 |

## Taxonomy Errors

No taxonomy errors found.
