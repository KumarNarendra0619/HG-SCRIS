# BUILD-05A — Scenario / Counterfactual Engine

## Status
SCENARIO ENGINE CONTRACT LOCKED

## Purpose
BUILD-05A creates a controlled scenario and counterfactual layer above the certified 04-series baseline. It does not rewrite the observed/reconstructed event. Instead, it freezes a baseline and creates explicitly parameterized alternative states, pathways or interventions so that differences can be attributed to declared scenario assumptions.

## 1. Core scientific chain

```text
CERTIFIED BASELINE
      ↓
SCENARIO QUESTION
      ↓
SCENARIO DEFINITION
      ↓
CHANGED ASSUMPTIONS / DRIVERS
      ↓
SCENARIO EXECUTION
      ↓
HAZARD / EXPOSURE / VULNERABILITY / RISK RESPONSE
      ↓
BASELINE–SCENARIO DIFFERENCE
      ↓
UNCERTAINTY + SENSITIVITY
      ↓
SCENARIO COMPARISON
```

## 2. Baseline immutability

The certified baseline is read-only for scenario generation.

```text
BASELINE vX
    │
    ├── Scenario A
    ├── Scenario B
    └── Scenario C
```

Scenario artifacts reference the exact baseline version and must never overwrite it.

## 3. Scenario definition contract

Every scenario declares:

```text
scenario_id
scenario_version
baseline_id
baseline_version
scenario_type
research_question
geographic_domain
temporal_domain
changed_variables
driver assumptions
boundary conditions
model versions
parameters
intervention assumptions where applicable
uncertainty policy
comparison metric
applicability domain
limitations
```

A scenario without explicit changed assumptions is not a valid counterfactual.

## 4. Scenario classes

Support registered classes:

```text
historical counterfactual
no-intervention / intervention
policy scenario
climate/environmental scenario
demographic scenario
land-use scenario
infrastructure scenario
hazard-intensity scenario
exposure-growth scenario
vulnerability-reduction scenario
compound/cascading scenario
stress-test / worst-case bounded scenario
sensitivity scenario
```

The engine must not imply that a scenario is a forecast unless it contains an explicit forecasting framework.

## 5. Counterfactual logic

A counterfactual asks:

```text
What would the outcome have been if
specified condition X had been different,
while the declared baseline conditions remained fixed?
```

The engine must identify:

```text
changed condition
held-constant conditions
mechanism/pathway
outcome
comparison reference
```

Unsupported causal claims are prohibited.

## 6. Scenario vs forecast vs projection

Metadata must distinguish:

```text
SCENARIO
= conditional representation of a possible state/pathway

PROJECTION
= model output conditional on assumptions

FORECAST
= prediction intended to estimate a future outcome

COUNTERFACTUAL
= alternative outcome/state under changed conditions relative to a reference
```

A scenario result must not be labelled a forecast merely because it has a future date.

## 7. Driver registry

Every changed driver is registered with:

```text
driver_id
driver_name
baseline_value
scenario_value/range
delta
unit
source
source_version
spatial support
temporal support
confidence
rationale
```

Drivers may be deterministic, bounded or probabilistic.

## 8. Intervention registry

For intervention scenarios:

```text
intervention_id
intervention_type
target_asset/population/place
start_time
duration
coverage
effect assumption
implementation constraint
source/evidence
uncertainty
```

The engine must not assume an intervention achieves 100% effectiveness unless explicitly specified and justified.

## 9. Causal pathway contract

Where causal interpretation is intended:

```text
DRIVER / INTERVENTION
        ↓
MECHANISM
        ↓
SYSTEM RESPONSE
        ↓
HAZARD / EXPOSURE / VULNERABILITY CHANGE
        ↓
RISK / OUTCOME CHANGE
```

The pathway and assumptions must be declared. Spatial correlation alone is not treated as causation.

## 10. Scenario execution modes

Support:

```text
parameter substitution
parameter sweep
threshold scenario
spatial allocation change
temporal trajectory change
intervention effect simulation
model ensemble
Monte Carlo / probabilistic scenario
rule-based scenario
```

Execution mode is recorded in the scenario manifest.

## 11. Baseline–scenario comparability

Before comparison verify:

```text
same spatial support
same temporal reference or declared transformation
same variable definition
compatible units
compatible model semantics
compatible aggregation
compatible coverage
```

If not comparable, the comparison is blocked or explicitly restricted.

## 12. Difference metrics

Depending on the outcome:

```text
absolute difference
relative difference
percentage change
risk ratio / rate ratio where appropriate
excess exposed population
avoided loss
change in affected area
change in severity distribution
rank change
spatial agreement/disagreement
```

The denominator and reference state must be explicit.

## 13. Avoided impact / intervention effect

Where valid:

```text
Baseline outcome
      −
Intervention scenario outcome
      =
Potential avoided outcome
```

This is a modelled counterfactual difference, not automatically an observed causal treatment effect.

## 14. Multi-scenario comparison

Scenario sets may contain:

```text
Baseline
Low
Central
High
Alternative policy A
Alternative policy B
Stress case
```

All scenario assumptions must be versioned and comparable.

## 15. Uncertainty

Separate:

```text
baseline uncertainty
scenario-driver uncertainty
parameter uncertainty
model uncertainty
structural uncertainty
implementation uncertainty
scenario sampling uncertainty
```

Scenario ranges must not be presented as probabilistic forecasts unless probabilities are actually justified.

## 16. Sensitivity analysis

Assess material sensitivity to:

```text
changed driver magnitude
model parameters
intervention effectiveness
spatial allocation
temporal assumptions
risk function
vulnerability weights
scenario boundary conditions
```

Identify conclusions that are robust versus assumption-sensitive.

## 17. Scenario ensembles

Where multiple plausible parameter/model combinations are used:

```text
Scenario ensemble
      ↓
Outcome distribution / range
      ↓
Robustness assessment
```

Ensemble spread is not automatically the same as formal probability.

## 18. Spatial scenario engine

Support:

```text
grid-cell scenarios
administrative scenarios
settlement scenarios
asset-level scenarios
corridor/network scenarios
watershed scenarios
custom analytical zones
```

Spatial transformations retain provenance and uncertainty.

## 19. Temporal scenario engine

Support:

```text
event-time counterfactual
seasonal scenario
annual scenario
multi-year trajectory
future time-slice
intervention before/after scenario
```

Temporal extrapolation must be explicitly labelled and justified.

## 20. Scenario quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
SIMULATION_READY
VALIDATION_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

Scenario `RESEARCH_READY` means reproducible and fit for the declared research use; it does not mean future truth.

## 21. Scenario output contract

```text
scenario_id
scenario_version
baseline_ref
scenario_definition
driver_refs[]
intervention_refs[]
model_refs[]
output_artifacts[]
comparison_artifacts[]
uncertainty_ref
sensitivity_ref
validation_ref where applicable
limitations
quality_state
```

## 22. Validation strategy

Scenario validation depends on the scenario class:

```text
historical counterfactual → historical back-testing / natural experiments where defensible
parameter scenario → calibration/validation against relevant observations
intervention scenario → evidence-based effect validation where available
future scenario → internal consistency + structural/parameter validation; future truth cannot be directly validated in advance
```

No future scenario receives an observed-truth validation claim before the future occurs.

## 23. Back-testing

For historical scenarios:

```text
Known historical baseline
      ↓
Generate scenario using information available under declared setup
      ↓
Compare modelled outcome with independent historical outcome
```

Avoid information leakage from future observations into scenario construction.

## 24. Causal inference safeguard

The scenario engine is not automatically a causal inference engine.

Causal effect claims require an appropriate identification strategy, assumptions and evidence. Scenario difference alone does not prove causality.

## 25. Scenario provenance

Every scenario must trace:

```text
baseline artifact
baseline version/checksum
changed driver sources
intervention evidence
model version
parameters
execution environment
random seed where applicable
outputs
comparison metrics
```

## 26. Scenario branching and lineage

```text
CERTIFIED BASELINE
       │
       ├── SCN-001
       │     ├── SCN-001-A
       │     └── SCN-001-B
       │
       └── SCN-002
```

Branch lineage must be machine-readable.

## 27. Scenario invalidation

If a baseline or model dependency changes materially:

```text
dependency changes
      ↓
scenario marked STALE
      ↓
re-execution
      ↓
re-validation where applicable
      ↓
new scenario version
```

Certified baseline changes must never leave dependent scenario outputs silently certified.

## 28. Decision-use safeguard

```text
SCENARIO
≠
PREDICTION
≠
WARNING
≠
POLICY CERTAINTY
```

Decision users must see assumptions, uncertainty, scenario type and limitations.

## 29. First validated scenario

The first pilot must be deliberately narrow:

```text
ONE certified baseline
      ↓
ONE changed driver/intervention
      ↓
ONE declared mechanism/model
      ↓
ONE outcome
      ↓
ONE comparison domain
      ↓
SENSITIVITY + UNCERTAINTY
      ↓
FIRST VALIDATED SCENARIO PRODUCT
```

## 30. Stop conditions

Block or downgrade when:

```text
baseline not certified
changed driver undefined
causal mechanism claimed but unsupported
baseline/scenario incomparable
units incompatible
spatial mismatch unresolved
temporal mismatch unresolved
scenario probability implied without basis
future scenario labelled as forecast without forecasting model
critical provenance missing
model outside applicability domain
material uncertainty hidden
```

## 31. Acceptance tests

```text
baseline immutability test
scenario schema test
driver registry test
intervention registry test
scenario-type classification test
counterfactual logic test
causal-claim safeguard test
spatial comparability test
temporal comparability test
unit compatibility test
difference-metric test
uncertainty test
sensitivity test
ensemble semantics test
back-testing leakage test
provenance test
branch-lineage test
invalidation test
quality-state test
reproducibility test
```

## 32. Acceptance criteria

BUILD-05A is accepted when:

- certified baselines remain immutable;
- scenarios are explicit branches from frozen baselines;
- changed drivers and held-constant conditions are declared;
- scenario, projection, forecast and counterfactual semantics are separated;
- causal claims require explicit mechanisms and evidence;
- baseline and scenario outputs are tested for comparability;
- difference metrics have explicit denominators and units;
- uncertainty and sensitivity are retained;
- ensembles are not mislabelled as probabilities;
- future scenarios are not presented as validated future truth;
- scenario provenance is complete;
- upstream dependency changes invalidate stale scenarios;
- decision-use limitations are explicit;
- a bounded first validated scenario product can be reproduced.

## 33. Transition from 04-series to 05-series

```text
04Z CERTIFIED BASELINE
        ↓
05A SCENARIO / COUNTERFACTUAL ENGINE
        ↓
05B FUTURE STATE / PATHWAY ENGINE
        ↓
05C SCENARIO COMPARISON + ROBUSTNESS
        ↓
05D ADAPTATION / INTERVENTION TESTING
```

## Next step

BUILD-05B — Future-State / Pathway Engine: generate temporally explicit future states and trajectories from registered scenarios, with driver trajectories, pathway consistency, uncertainty envelopes and strict separation between projection and forecast.
