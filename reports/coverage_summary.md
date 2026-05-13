# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 47.9% | 24% | 135 |
| move | 13.5% | 22% | 38 |
| skill | 20.6% | 26% | 58 |
| skillControl | 4.6% | 8% | 13 |
| wait | 5.3% | 8% | 15 |
| empty | 8.2% | 12% | 23 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 73.0% | 40% | 206 |
| explicit_multi_actor | 13.1% | 12% | 37 |
| global_condition | 3.5% | 16% | 10 |
| global_role_based | 2.8% | 12% | 8 |
| global_state_based | 3.2% | 15% | 9 |
| no_valid_actor | 4.3% | 5% | 12 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 43.6% | 21% | 123 |
| explicit_ally_target | 8.5% | 13% | 24 |
| nearest_enemy | 8.5% | 8% | 24 |
| lowest_hp_enemy | 3.9% | 8% | 11 |
| highest_threat_enemy | 1.8% | 7% | 5 |
| role_based_enemy | 6.4% | 8% | 18 |
| pressure_source_enemy | 2.1% | 6% | 6 |
| safe_ally | 3.2% | 6% | 9 |
| low_hp_ally | 3.5% | 6% | 10 |
| backline_ally | 0.7% | 4% | 2 |
| invalid_explicit_target | 3.5% | 7% | 10 |
| none | 14.2% | 6% | 40 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 24.5% | 13% | 69 |
| move_only | 7.8% | 13% | 22 |
| move_then_attack | 20.2% | 11% | 57 |
| skill_only | 14.5% | 19% | 41 |
| move_then_skill | 1.1% | 4% | 3 |
| wait_only | 2.1% | 6% | 6 |
| wait_then_attack | 1.4% | 3% | 4 |
| wait_then_skill | 0.4% | 2% | 1 |
| skillControl_defer | 1.1% | 4% | 3 |
| skillControl_forbid | 1.4% | 4% | 4 |
| multi_actor_same_target | 5.3% | 6% | 15 |
| multi_actor_different_targets | 2.8% | 3% | 8 |
| empty_action_expected | 17.4% | 12% | 49 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 71.6% | 35% | 202 |
| casual_korean | 14.9% | 20% | 42 |
| elliptical_korean | 1.8% | 20% | 5 |
| tactical_korean | 11.3% | 15% | 32 |
| rough_korean | 0.4% | 10% | 1 |

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
