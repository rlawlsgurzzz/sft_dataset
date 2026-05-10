# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 30.0% | 24% | 3 |
| move | 20.0% | 22% | 2 |
| skill | 30.0% | 26% | 3 |
| skillControl | 10.0% | 8% | 1 |
| wait | 10.0% | 8% | 1 |
| empty | 0.0% | 12% | 0 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 80.0% | 40% | 8 |
| explicit_multi_actor | 10.0% | 12% | 1 |
| global_condition | 10.0% | 16% | 1 |
| global_role_based | 0.0% | 12% | 0 |
| global_state_based | 0.0% | 15% | 0 |
| no_valid_actor | 0.0% | 5% | 0 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 20.0% | 21% | 2 |
| explicit_ally_target | 20.0% | 13% | 2 |
| nearest_enemy | 10.0% | 8% | 1 |
| lowest_hp_enemy | 0.0% | 8% | 0 |
| highest_threat_enemy | 0.0% | 7% | 0 |
| role_based_enemy | 10.0% | 8% | 1 |
| pressure_source_enemy | 0.0% | 6% | 0 |
| safe_ally | 10.0% | 6% | 1 |
| low_hp_ally | 0.0% | 6% | 0 |
| backline_ally | 0.0% | 4% | 0 |
| invalid_explicit_target | 0.0% | 7% | 0 |
| none | 30.0% | 6% | 3 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 20.0% | 13% | 2 |
| move_only | 20.0% | 13% | 2 |
| move_then_attack | 0.0% | 11% | 0 |
| skill_only | 30.0% | 19% | 3 |
| move_then_skill | 0.0% | 4% | 0 |
| wait_only | 10.0% | 6% | 1 |
| wait_then_attack | 0.0% | 3% | 0 |
| wait_then_skill | 0.0% | 2% | 0 |
| skillControl_defer | 10.0% | 4% | 1 |
| skillControl_forbid | 0.0% | 4% | 0 |
| multi_actor_same_target | 10.0% | 6% | 1 |
| multi_actor_different_targets | 0.0% | 3% | 0 |
| empty_action_expected | 0.0% | 12% | 0 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 50.0% | 35% | 5 |
| casual_korean | 30.0% | 20% | 3 |
| elliptical_korean | 10.0% | 20% | 1 |
| tactical_korean | 10.0% | 15% | 1 |
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
