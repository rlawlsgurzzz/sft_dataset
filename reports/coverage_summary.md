# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 33.3% | 24% | 19 |
| move | 29.8% | 22% | 17 |
| skill | 33.3% | 26% | 19 |
| skillControl | 1.8% | 8% | 1 |
| wait | 1.8% | 8% | 1 |
| empty | 0.0% | 12% | 0 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 71.9% | 40% | 41 |
| explicit_multi_actor | 7.0% | 12% | 4 |
| global_condition | 5.3% | 16% | 3 |
| global_role_based | 7.0% | 12% | 4 |
| global_state_based | 5.3% | 15% | 3 |
| no_valid_actor | 3.5% | 5% | 2 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 31.6% | 21% | 18 |
| explicit_ally_target | 19.3% | 13% | 11 |
| nearest_enemy | 3.5% | 8% | 2 |
| lowest_hp_enemy | 3.5% | 8% | 2 |
| highest_threat_enemy | 3.5% | 7% | 2 |
| role_based_enemy | 8.8% | 8% | 5 |
| pressure_source_enemy | 3.5% | 6% | 2 |
| safe_ally | 8.8% | 6% | 5 |
| low_hp_ally | 5.3% | 6% | 3 |
| backline_ally | 0.0% | 4% | 0 |
| invalid_explicit_target | 0.0% | 7% | 0 |
| none | 12.3% | 6% | 7 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 17.5% | 13% | 10 |
| move_only | 22.8% | 13% | 13 |
| move_then_attack | 8.8% | 11% | 5 |
| skill_only | 29.8% | 19% | 17 |
| move_then_skill | 1.8% | 4% | 1 |
| wait_only | 1.8% | 6% | 1 |
| wait_then_attack | 0.0% | 3% | 0 |
| wait_then_skill | 0.0% | 2% | 0 |
| skillControl_defer | 1.8% | 4% | 1 |
| skillControl_forbid | 0.0% | 4% | 0 |
| multi_actor_same_target | 8.8% | 6% | 5 |
| multi_actor_different_targets | 3.5% | 3% | 2 |
| empty_action_expected | 3.5% | 12% | 2 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 33.3% | 35% | 19 |
| casual_korean | 33.3% | 20% | 19 |
| elliptical_korean | 1.8% | 20% | 1 |
| tactical_korean | 31.6% | 15% | 18 |
| rough_korean | 0.0% | 10% | 0 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 21.1% | 18% | 4 |
| self_buff | 15.8% | 14% | 3 |
| ally_shield | 15.8% | 13% | 3 |
| ally_heal | 10.5% | 11% | 2 |
| ally_resurrection | 10.5% | 13% | 2 |
| enemy_aoe_attack | 10.5% | 12% | 2 |
| enemy_debuff | 5.3% | 8% | 1 |
| mobility_skill | 0.0% | 5% | 0 |
| no_skill | 10.5% | 6% | 2 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 31.6% | 36% | 6 |
| ally_alive | 26.3% | 22% | 5 |
| self | 15.8% | 16% | 3 |
| ally_dead | 10.5% | 12% | 2 |
| enemy_dead | 5.3% | 5% | 1 |
| none | 10.5% | 9% | 2 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 57.9% | 48% | 11 |
| text_enemy_target_but_self_skill | 5.3% | 8% | 1 |
| text_enemy_target_but_ally_skill | 5.3% | 9% | 1 |
| text_ally_target_but_enemy_skill | 5.3% | 9% | 1 |
| text_dead_target_but_skill_cannot_target_dead | 10.5% | 8% | 2 |
| text_living_target_but_resurrection_skill | 5.3% | 6% | 1 |
| skill_actor_has_no_skill | 10.5% | 7% | 2 |

## Taxonomy Errors

No taxonomy errors found.
