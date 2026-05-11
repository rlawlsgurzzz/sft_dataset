# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 63.2% | 24% | 12 |
| move | 10.5% | 22% | 2 |
| skill | 15.8% | 26% | 3 |
| skillControl | 5.3% | 8% | 1 |
| wait | 5.3% | 8% | 1 |
| empty | 0.0% | 12% | 0 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 89.5% | 40% | 17 |
| explicit_multi_actor | 5.3% | 12% | 1 |
| global_condition | 5.3% | 16% | 1 |
| global_role_based | 0.0% | 12% | 0 |
| global_state_based | 0.0% | 15% | 0 |
| no_valid_actor | 0.0% | 5% | 0 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 26.3% | 21% | 5 |
| explicit_ally_target | 10.5% | 13% | 2 |
| nearest_enemy | 10.5% | 8% | 2 |
| lowest_hp_enemy | 5.3% | 8% | 1 |
| highest_threat_enemy | 5.3% | 7% | 1 |
| role_based_enemy | 15.8% | 8% | 3 |
| pressure_source_enemy | 5.3% | 6% | 1 |
| safe_ally | 5.3% | 6% | 1 |
| low_hp_ally | 0.0% | 6% | 0 |
| backline_ally | 0.0% | 4% | 0 |
| invalid_explicit_target | 0.0% | 7% | 0 |
| none | 15.8% | 6% | 3 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 47.4% | 13% | 9 |
| move_only | 10.5% | 13% | 2 |
| move_then_attack | 10.5% | 11% | 2 |
| skill_only | 15.8% | 19% | 3 |
| move_then_skill | 0.0% | 4% | 0 |
| wait_only | 5.3% | 6% | 1 |
| wait_then_attack | 0.0% | 3% | 0 |
| wait_then_skill | 0.0% | 2% | 0 |
| skillControl_defer | 5.3% | 4% | 1 |
| skillControl_forbid | 0.0% | 4% | 0 |
| multi_actor_same_target | 5.3% | 6% | 1 |
| multi_actor_different_targets | 0.0% | 3% | 0 |
| empty_action_expected | 0.0% | 12% | 0 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 57.9% | 35% | 11 |
| casual_korean | 15.8% | 20% | 3 |
| elliptical_korean | 5.3% | 20% | 1 |
| tactical_korean | 21.1% | 15% | 4 |
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
