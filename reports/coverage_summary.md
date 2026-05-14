# Coverage Summary

## intent_family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack | 21.5% | 24% | 408 |
| move | 22.7% | 22% | 432 |
| skill | 27.5% | 26% | 523 |
| skillControl | 8.5% | 8% | 162 |
| wait | 8.4% | 8% | 159 |
| empty | 11.3% | 12% | 215 |

## Actor Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_actor | 57.6% | 40% | 1093 |
| explicit_multi_actor | 15.1% | 12% | 287 |
| global_condition | 8.8% | 16% | 168 |
| global_role_based | 6.3% | 12% | 120 |
| global_state_based | 6.2% | 15% | 117 |
| no_valid_actor | 6.0% | 5% | 114 |

## Target Selection

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| explicit_enemy_target | 26.4% | 21% | 501 |
| explicit_ally_target | 13.2% | 13% | 250 |
| nearest_enemy | 4.3% | 8% | 82 |
| lowest_hp_enemy | 5.0% | 8% | 95 |
| highest_threat_enemy | 3.2% | 7% | 60 |
| role_based_enemy | 6.4% | 8% | 121 |
| pressure_source_enemy | 1.7% | 6% | 32 |
| safe_ally | 4.1% | 6% | 77 |
| low_hp_ally | 4.5% | 6% | 85 |
| backline_ally | 1.6% | 4% | 31 |
| invalid_explicit_target | 7.4% | 7% | 141 |
| none | 22.3% | 6% | 424 |

## Action Pattern

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| attack_only | 7.8% | 13% | 148 |
| move_only | 13.0% | 13% | 247 |
| move_then_attack | 10.7% | 11% | 203 |
| skill_only | 19.4% | 19% | 368 |
| move_then_skill | 1.3% | 4% | 25 |
| wait_only | 5.5% | 6% | 104 |
| wait_then_attack | 1.5% | 3% | 29 |
| wait_then_skill | 0.1% | 2% | 1 |
| skillControl_defer | 3.7% | 4% | 70 |
| skillControl_forbid | 3.5% | 4% | 66 |
| multi_actor_same_target | 7.0% | 6% | 133 |
| multi_actor_different_targets | 3.2% | 3% | 61 |
| empty_action_expected | 23.4% | 12% | 444 |

## Command Style

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| direct_korean | 31.7% | 35% | 602 |
| casual_korean | 31.0% | 20% | 588 |
| elliptical_korean | 8.6% | 20% | 163 |
| tactical_korean | 12.4% | 15% | 235 |
| rough_korean | 16.4% | 10% | 311 |

## Skill Family

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_single_target_attack | 30.0% | 18% | 158 |
| self_buff | 8.0% | 14% | 42 |
| ally_shield | 6.8% | 13% | 36 |
| ally_heal | 14.4% | 11% | 76 |
| ally_resurrection | 12.1% | 13% | 64 |
| enemy_aoe_attack | 12.1% | 12% | 64 |
| enemy_debuff | 3.2% | 8% | 17 |
| mobility_skill | 7.8% | 5% | 41 |
| no_skill | 5.5% | 6% | 29 |

## Skill Target Kind

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| enemy_alive | 36.4% | 36% | 192 |
| ally_alive | 26.2% | 22% | 138 |
| self | 15.4% | 16% | 81 |
| ally_dead | 7.2% | 12% | 38 |
| enemy_dead | 9.3% | 5% | 49 |
| none | 5.5% | 9% | 29 |

## Conflict Type

| key | current_ratio | target_ratio | count |
|---|---:|---:|---:|
| null | 54.6% | 48% | 288 |
| text_enemy_target_but_self_skill | 4.4% | 8% | 23 |
| text_enemy_target_but_ally_skill | 8.2% | 9% | 43 |
| text_ally_target_but_enemy_skill | 8.5% | 9% | 45 |
| text_dead_target_but_skill_cannot_target_dead | 9.9% | 8% | 52 |
| text_living_target_but_resurrection_skill | 5.5% | 6% | 29 |
| skill_actor_has_no_skill | 5.5% | 7% | 29 |

## Taxonomy Errors

No taxonomy errors found.
