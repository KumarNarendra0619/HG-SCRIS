# BUILD-05E — Decision / Policy Stress-Test Engine

## Status
DECISION / POLICY STRESS-TEST CONTRACT LOCKED

## Purpose
BUILD-05E is the decision-support gate of the 05-series. It tests interventions, portfolios and policy options across multiple plausible futures, constraints, shocks and objectives. It identifies options that are robust, fragile, conditional, no-regret, trade-off-heavy or unacceptable under declared assumptions.

It does **not** automatically prescribe policy, optimize society according to hidden values, or convert model outputs into certainty.

## 1. Core chain

```text
CERTIFIED BASELINE
      ↓
SCENARIOS / FUTURE PATHWAYS
      ↓
INTERVENTIONS / PORTFOLIOS
      ↓
OBJECTIVES + CONSTRAINTS
      ↓
DECISION RULES
      ↓
STRESS TESTS
      ↓
OUTCOME / RISK RESPONSE
      ↓
TRADE-OFF + EQUITY + RESIDUAL RISK
      ↓
ROBUSTNESS
      ↓
DECISION EVIDENCE MATRIX
```

## 2. Decision contract

Every decision analysis declares:

```text
decision_id
decision_version
baseline_ref
scenario_set_refs[]
intervention_refs[]
objective_set
constraints
decision criteria
decision rule
planning horizon
spatial domain
temporal domain
uncertainty policy
stress-test set
stakeholder/value assumptions
limitations
```

## 3. Decision support vs automatic policy prescription

The engine outputs:

```text
decision evidence
option performance
robustness
trade-offs
residual risk
failure conditions
```

It does not output an unconditional command such as `choose policy X` unless a user explicitly defines the decision rule and value assumptions that justify that selection.

## 4. Decision objectives

Support multiple objectives such as:

```text
risk reduction
population protection
asset protection
service continuity
equity
cost efficiency
environmental protection
resilience
implementation feasibility
loss avoidance
```

Objectives must have explicit definitions, units and direction of preference.

## 5. Objective weighting safeguard

Weights may be used only when explicitly declared.

The system must preserve:

```text
objective
weight
normalization
aggregation rule
value source/rationale
sensitivity to weight
```

Hidden or default normative weights are prohibited.

## 6. Constraints

Support:

```text
budget
capacity
land availability
implementation time
institutional capacity
coverage requirement
legal/regulatory constraint
environmental constraint
technical feasibility
minimum protection threshold
maximum acceptable residual risk
```

Constraint violations must remain visible even when an option performs well on other objectives.

## 7. Decision rules

Possible explicit rules:

```text
maximize risk reduction
minimize cost
cost-effectiveness threshold
minimize worst-case loss
minimize regret
satisficing
lexicographic priority
Pareto dominance
robust decision making
threshold rule
```

The selected rule is part of the reproducibility record.

## 8. Stress-test architecture

Each option is evaluated under multiple conditions:

```text
baseline
plausible future A
plausible future B
plausible future C
high-impact stress
implementation shortfall
cost overrun
coverage failure
compound hazard
model disagreement
parameter extremes
```

Stress cases must be declared as scenarios or bounded perturbations; arbitrary worst cases are not presented as probable futures.

## 9. Robust decision assessment

An option may be classified:

```text
ROBUST
CONDITIONALLY ROBUST
NO-REGRET CANDIDATE
LOW-REGRET CANDIDATE
FRAGILE
SCENARIO-DEPENDENT
MODEL-SENSITIVE
IMPLEMENTATION-SENSITIVE
COST-SENSITIVE
UNRESOLVED
```

`NO-REGRET` is a substantive claim and requires explicit criteria; it is not a default label for low-cost interventions.

## 10. Regret analysis

Where appropriate:

```text
Regret(option, scenario)
= outcome of best feasible option in that scenario
  − outcome of selected option in that scenario
```

Direction and units depend on the objective. The exact regret definition must be stored.

## 11. Worst-case / minimax safeguards

Worst-case analysis must define:

```text
stress set
feasible domain
outcome metric
worst-case criterion
```

A selected mathematical worst case is not automatically a physically plausible catastrophe.

## 12. Robust Decision Making (RDM)

Where RDM-style analysis is used:

```text
multiple plausible futures
        ↓
option performance matrix
        ↓
vulnerability / failure conditions
        ↓
robustness across futures
        ↓
adaptive strategy
```

The engine records the futures under which each option fails.

## 13. Decision fragility

For each option identify:

```text
critical assumptions
failure thresholds
sensitive drivers
model dependencies
implementation dependencies
cost thresholds
coverage thresholds
```

A decision is fragile when small plausible changes materially alter its performance or ranking.

## 14. Tipping / trigger rules

Adaptive policy options may use:

```text
indicator
threshold
trigger
response
review date
exit/adjustment condition
```

Trigger thresholds must have a declared scientific, operational or policy basis.

## 15. Adaptive pathway

Support:

```text
MONITOR
  ↓
TRIGGER CONDITION
  ↓
IMPLEMENT
  ↓
OBSERVE
  ↓
REASSESS
  ↓
ADJUST / SCALE / EXIT
```

This is a conditional decision pathway, not a guarantee of optimality.

## 16. Portfolio stress testing

Portfolios may contain:

```text
single intervention
A+B
A+C
A+B+C
phased portfolio
adaptive portfolio
```

Interactions must be explicitly modelled or treated as uncertain.

## 17. Budget stress test

Evaluate:

```text
base budget
budget reduction
cost overrun
maintenance shortfall
funding delay
```

Budget constraints must not be silently relaxed to make an option feasible.

## 18. Implementation stress test

Test:

```text
full coverage
partial coverage
low adoption
delayed implementation
maintenance failure
institutional capacity reduction
```

Technical effectiveness and implementation feasibility remain separate dimensions.

## 19. Compound shock stress test

Where relevant:

```text
hazard A
hazard B
infrastructure failure
service disruption
population displacement
```

may be combined under a registered compound pathway. The engine must not multiply probabilities or effects without a valid dependency model.

## 20. Equity and distributional decision audit

For each option, where data permit:

```text
aggregate benefit
benefit distribution
residual risk distribution
who gains?
who loses?
who remains unprotected?
spatial inequality
population-group inequality
```

A high aggregate benefit does not override severe distributional harm unless the declared decision framework explicitly permits that trade-off.

## 21. Cost-effectiveness decision gate

Where economic analysis is used:

```text
cost
      ↓
benefit / avoided impact
      ↓
common valuation basis
      ↓
time horizon
      ↓
discounting where applicable
      ↓
sensitivity
```

No economic ranking is valid when valuation assumptions are incompatible.

## 22. Multi-criteria decision analysis

MCDA may be used where appropriate:

```text
objectives
 ↓
normalization
 ↓
weights / preferences
 ↓
aggregation
 ↓
option ranking
```

The system must expose sensitivity to weights and normalization choices.

## 23. Pareto frontier

Where objectives conflict:

```text
Option set
   ↓
Pareto-dominated options
   ↓
Non-dominated options
   ↓
Decision-maker preference
```

Pareto dominance does not identify the single socially best option.

## 24. No-regret / low-regret analysis

An option may be labelled `NO-REGRET CANDIDATE` only if predefined criteria show that it performs acceptably across the declared plausible future set and does not create unacceptable material harms under that set.

## 25. Robustness across model classes

Where multiple credible models exist:

```text
Model A
Model B
Model C
   ↓
Option performance
   ↓
Model disagreement
   ↓
Robustness classification
```

Blind model averaging is not a substitute for model-uncertainty analysis.

## 26. Uncertainty architecture

Separate:

```text
scenario uncertainty
driver uncertainty
model uncertainty
parameter uncertainty
implementation uncertainty
cost uncertainty
behavior/adoption uncertainty
structural uncertainty
value/weight uncertainty
```

Normative uncertainty and empirical uncertainty must not be conflated.

## 27. Sensitivity analysis

Test:

```text
objective weights
normalization
decision rule
budget
coverage
effectiveness
implementation delay
model choice
scenario set
thresholds
cost
```

Identify which recommendations are stable and which change under reasonable alternatives.

## 28. Value-of-information screening

Where feasible, identify uncertain inputs for which additional information could materially change the decision:

```text
uncertain variable
expected decision sensitivity
information gap
potential value of additional data
priority for research/monitoring
```

This is a screening tool unless a formal value-of-information method is implemented.

## 29. Monitoring and learning plan

A decision product may specify:

```text
indicator
baseline
target/threshold
monitoring frequency
responsible data source
trigger condition
review point
```

Monitoring recommendations must remain distinct from observed evidence.

## 30. Decision evidence matrix

Generate:

```text
Decision option
Scenario/future
Objective
Constraint status
Performance
Residual risk
Trade-offs
Equity
Critical assumptions
Failure conditions
Uncertainty
Robustness
Evidence
Limitations
```

## 31. Claim discipline

The engine distinguishes:

```text
modelled performance
scenario-conditioned performance
robust performance
causal impact
forecast
policy preference
```

Only the strongest defensible claim may be generated.

## 32. Human decision authority

Final policy choice remains with the authorized decision-maker/stakeholders.

The system may expose:

```text
best under rule X
robust across futures
fails under condition Y
trade-off with objective Z
```

but must not disguise a value judgement as a scientific fact.

## 33. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
STRESS_TEST_READY
ROBUSTNESS_PENDING
DECISION_EVIDENCE_READY
RESEARCH_READY
SUPERSEDED
REJECTED
```

`RESEARCH_READY` means reproducible and methodologically defensible for declared decision-support use; it does not mean policy certainty.

## 34. Output contract

```text
decision_id
decision_version
baseline_ref
scenario_set_refs[]
intervention_set_refs[]
objective_set_ref
constraint_set_ref
decision_rule_ref
stress_test_set_ref
option_performance_matrix
regret_matrix where applicable
pareto_set where applicable
robustness_results
failure_conditions
residual_risk_results
equity_results
cost_results where available
uncertainty_ref
sensitivity_ref
monitoring_ref
value_of_information_ref where available
decision_evidence_matrix
limitations
quality_state
```

## 35. Invalidation

If any material baseline, scenario, intervention, model, objective, constraint or decision-rule dependency changes:

```text
dependency changes
      ↓
decision analysis = STALE
      ↓
re-run
      ↓
re-evaluate
      ↓
new version
```

Changing normative weights or decision rules must also invalidate affected rankings even if the underlying science is unchanged.

## 36. Stop conditions

Block or downgrade when:

```text
baseline/scenarios uncertified
option undefined
objective undefined
hidden weights
constraint omitted
stress domain undefined
worst case presented as probability without basis
causal policy effect claimed without identification evidence
implementation feasibility ignored
residual risk hidden
equity impacts omitted where material
model disagreement hidden
cost assumptions incompatible
adaptive trigger unsupported
stale dependencies
```

## 37. First decision stress-test product

Keep the first pilot narrow:

```text
ONE certified baseline
      ↓
3 registered future/scenario pathways
      ↓
2–3 intervention options
      ↓
ONE primary objective
      ↓
2–3 material constraints
      ↓
DECLARED decision rule
      ↓
stress testing
      ↓
robustness + regret
      ↓
trade-off + equity + residual risk
      ↓
DECISION EVIDENCE MATRIX
```

## 38. Acceptance tests

```text
decision schema test
objective definition test
weight transparency test
constraint test
decision-rule test
scenario coverage test
stress-domain test
regret calculation test
RDM test
fragility test
adaptive-trigger test
portfolio interaction test
budget stress test
implementation stress test
compound-shock dependency test
equity test
cost-effectiveness test
MCDA sensitivity test
Pareto test
no-regret criteria test
model-disagreement test
uncertainty test
sensitivity test
value-of-information test
monitoring-plan test
claim-discipline test
provenance test
invalidation test
reproducibility test
```

## 39. Acceptance criteria

BUILD-05E is accepted when:

- decision analyses are explicitly linked to certified baselines, scenarios and intervention versions;
- objectives, constraints and decision rules are transparent;
- normative weights are never hidden;
- options are tested across multiple plausible futures and declared stress conditions;
- robust, fragile and scenario-dependent performance are distinguished;
- regret/worst-case claims use explicit definitions and domains;
- implementation and budget failures are stress-tested;
- residual risk, risk transfer and equity are visible;
- compound shocks use explicit dependency assumptions;
- model disagreement is retained;
- uncertainty and sensitivity include value/weight uncertainty where relevant;
- no-regret claims have explicit criteria;
- monitoring and learning triggers can be recorded;
- policy preference is not disguised as scientific fact;
- material dependency or decision-rule changes invalidate stale analyses;
- a bounded decision evidence product can be reproduced.

## 40. BUILD-05 completion gate

```text
04Z CERTIFIED BASELINE
        ↓
05A SCENARIO / COUNTERFACTUAL
        ↓
05B FUTURE STATE / PATHWAY
        ↓
05C COMPARISON + ROBUSTNESS
        ↓
05D ADAPTATION / INTERVENTION
        ↓
05E DECISION / POLICY STRESS TEST
        ↓
BUILD-05 CERTIFIED DECISION-SUPPORT LAYER
```

## Next step

BUILD-06A — Synthesis / Evidence Integration Engine: integrate certified evidence, reconstructed events, hazard–exposure–vulnerability–risk layers, future pathways, intervention tests and decision-stress results into a traceable multidimensional synthesis without double counting evidence or overstating causal certainty.
