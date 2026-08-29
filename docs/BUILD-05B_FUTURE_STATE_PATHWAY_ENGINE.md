# BUILD-05B — Future-State / Pathway Engine

## Status
FUTURE-STATE ENGINE CONTRACT LOCKED

## Purpose
BUILD-05B converts registered scenarios from BUILD-05A into explicit, temporally structured future states and trajectories. It does not claim to predict the future by default. It produces conditional projections/pathways whose assumptions, drivers, models, uncertainty and applicability are visible and reproducible.

## 1. Core scientific chain

```text
CERTIFIED BASELINE
      ↓
REGISTERED SCENARIO
      ↓
DRIVER TRAJECTORIES
      ↓
SYSTEM / SPATIAL / TEMPORAL PATHWAY
      ↓
FUTURE STATE(S)
      ↓
HAZARD / EXPOSURE / VULNERABILITY / RISK RESPONSE
      ↓
UNCERTAINTY ENVELOPE
      ↓
PATHWAY COMPARISON
```

## 2. Future-state contract

Every future-state run declares:

```text
future_run_id
future_run_version
baseline_id/version
scenario_id/version
pathway_id/version
time horizon
start/end dates or time slices
driver trajectories
model versions
parameters
boundary conditions
spatial domain
output variables
uncertainty method
validation/back-testing method where applicable
forecast/projection status
applicability domain
limitations
```

## 3. Projection vs forecast safeguard

```text
PROJECTION
= conditional model output under declared assumptions

FORECAST
= prediction intended to estimate what will occur

PATHWAY
= structured trajectory under a specified set of drivers/assumptions

SCENARIO
= conditional description of possible future conditions
```

A future-state product is labelled `FORECAST` only when an explicit forecasting framework, training/calibration strategy, predictive target and evaluation protocol are registered.

## 4. Driver trajectory registry

Each driver trajectory contains:

```text
driver_id
trajectory_id
baseline value
future values/range
time steps
unit
source
source version
trajectory rationale
spatial support
temporal support
confidence/uncertainty
correlation/dependence assumptions
```

Trajectories may be deterministic, bounded, stochastic or ensemble-based.

## 5. Pathway definition

A pathway is represented as:

```text
INITIAL STATE
      ↓
DRIVER CHANGE
      ↓
SYSTEM RESPONSE
      ↓
INTERMEDIATE STATE
      ↓
FEEDBACK / INTERACTION
      ↓
FUTURE STATE
```

Where mechanisms are unknown, the pathway must be labelled assumption-based rather than causal fact.

## 6. Temporal engine

Support:

```text
event-time trajectories
seasonal states
annual time steps
multi-year trajectories
time-slice projections
continuous trajectories where supported
```

Temporal interpolation/extrapolation must be declared and cannot silently create observations.

## 7. Spatial engine

Support:

```text
grid cells
settlements
wards/villages
administrative units
assets
network segments
watersheds
custom analytical zones
```

Spatial resolution must not exceed defensible evidence/model support without explicit downscaling assumptions.

## 8. Downscaling and upscaling

Any transformation records:

```text
source scale
output scale
method
parameters
training/reference data
assumptions
uncertainty
validation evidence
```

Downscaled outputs are not treated as direct observations.

## 9. State variables

Future state variables may include:

```text
hazard intensity/frequency
exposure population/assets
vulnerability indicators
risk metrics
land use/land cover
demographic structure
infrastructure/system state
environmental variables
```

Each variable retains units, definition, source/model lineage and temporal support.

## 10. Dynamic dependency graph

Where variables interact:

```text
Driver A ──→ State B
    │          │
    └────→ State C ──→ Risk
               ↑
             Driver D
```

Dependencies must be registered. Correlation must not be presented as a causal mechanism without evidence.

## 11. Feedbacks

Potential feedbacks may be represented:

```text
hazard → damage → exposure redistribution
exposure → land-use change → future exposure
vulnerability reduction → adaptive response → future vulnerability
```

Feedbacks require explicit rules/evidence and versioning.

## 12. Scenario ensemble

Multiple pathways may be executed:

```text
Baseline
Pathway A
Pathway B
Pathway C
Stress pathway
```

The engine reports:

```text
central trajectory where justified
range/envelope
ensemble spread
outlier pathways
robust patterns
assumption-sensitive patterns
```

Ensemble frequency is not automatically probability.

## 13. Uncertainty architecture

Separate:

```text
initial-condition uncertainty
driver uncertainty
parameter uncertainty
model uncertainty
structural uncertainty
scenario uncertainty
spatial uncertainty
temporal uncertainty
implementation uncertainty
```

Uncertainty may be represented as:

```text
intervals
quantiles
distributions
scenario ranges
ensemble spread
qualitative bounds
```

depending on evidence.

## 14. Uncertainty propagation

```text
BASELINE UNCERTAINTY
        +
DRIVER UNCERTAINTY
        +
MODEL/PARAMETER UNCERTAINTY
        ↓
FUTURE-STATE UNCERTAINTY
        ↓
RISK UNCERTAINTY
```

The engine must identify uncertainty sources rather than collapse all uncertainty into one unexplained confidence score.

## 15. Calibration and evaluation

For forecasting models:

```text
training/calibration period
        ↓
validation period
        ↓
out-of-sample test
        ↓
forecast evaluation
```

For conditional projections where future truth is unavailable:

```text
structural consistency
historical hindcasting where defensible
parameter validation
scenario plausibility
sensitivity analysis
```

Future outcomes cannot be claimed as already validated.

## 16. Hindcasting

Where suitable:

```text
Historical initial state
      ↓
Apply model/pathway using information available at that time
      ↓
Project to known later period
      ↓
Compare with observations
```

Information leakage must be audited.

## 17. Robustness classification

Future conclusions are classified:

```text
ROBUST
CONDITIONALLY ROBUST
ASSUMPTION-SENSITIVE
MODEL-SENSITIVE
DATA-LIMITED
UNRESOLVED
```

A single model run cannot establish robustness.

## 18. Future-state comparison

Compare pathways using:

```text
absolute change
relative change
percentage change
trajectory slope
threshold crossing time
cumulative exposure
cumulative/expected loss
affected area
population affected
spatial transition
rank change
```

Metrics must retain units and reference states.

## 19. Threshold and tipping-point safeguards

If thresholds are used:

```text
threshold definition
physical/theoretical basis
uncertainty
crossing criterion
hysteresis/irreversibility assumption where applicable
```

A statistical threshold must not automatically be called a physical tipping point.

## 20. Compound and cascading future pathways

Support explicit chains:

```text
Climate/environmental driver
        ↓
Hazard change
        ↓
Exposure redistribution
        ↓
Vulnerability response
        ↓
Risk change
        ↓
Secondary/cascading impact
```

Each link must have its own model/assumption and uncertainty metadata.

## 21. Adaptation feedback

Where adaptation is included:

```text
Baseline
   ↓
Hazard/exposure trajectory
   ↓
Adaptation intervention
   ↓
Changed vulnerability/exposure
   ↓
Changed risk trajectory
```

Adaptation effectiveness is scenario-specific and must not be treated as guaranteed.

## 22. Future-state quality states

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

`RESEARCH_READY` refers to methodological fitness and reproducibility for the declared conditional use, not certainty about future reality.

## 23. Output contract

```text
future_run_id
future_run_version
baseline_ref
scenario_ref
pathway_ref
time_horizon
time_steps
driver_trajectory_refs[]
model_refs[]
state_variables[]
output_artifacts[]
uncertainty_ref
sensitivity_ref
evaluation_ref
robustness_class
forecast_status
limitations
quality_state
```

## 24. Forecast eligibility gate

A product can receive `FORECAST_ELIGIBLE` only when:

```text
predictive target defined
forecast horizon defined
forecast model registered
training/calibration protocol defined
out-of-sample evaluation available
baseline comparator defined
error metrics appropriate
uncertainty quantified or appropriately bounded
leakage checks passed
applicability domain declared
```

Otherwise it remains a projection/scenario product.

## 25. Scenario-to-future lineage

```text
CERTIFIED BASELINE
      ↓
SCENARIO VERSION
      ↓
DRIVER TRAJECTORIES
      ↓
PATHWAY VERSION
      ↓
FUTURE RUN
      ↓
OUTPUT VERSION
```

Every output retains exact dependency references.

## 26. Invalidation

If any material dependency changes:

```text
dependency change
      ↓
future run = STALE
      ↓
re-execution
      ↓
re-evaluation
      ↓
new version
```

Certified downstream products cannot remain valid against superseded dependencies.

## 27. Stop conditions

Block or downgrade when:

```text
baseline uncertified
scenario undefined
driver trajectory unsupported
future state confused with observation
projection labelled forecast without forecast protocol
spatial downscaling unsupported
temporal extrapolation hidden
probability implied without basis
critical uncertainty omitted
causal pathway unsupported
model outside applicability domain
information leakage detected
```

## 28. Acceptance tests

```text
baseline immutability test
scenario dependency test
driver trajectory schema test
time-step consistency test
spatial support test
downscaling/upscaling test
unit compatibility test
projection-vs-forecast classification test
pathway dependency test
feedback test
ensemble semantics test
uncertainty propagation test
hindcast leakage test
forecast eligibility test
robustness classification test
threshold semantics test
adaptation-effect test
provenance test
invalidation test
reproducibility test
```

## 29. Acceptance criteria

BUILD-05B is accepted when:

- future states are generated only from registered scenarios and frozen baselines;
- driver trajectories are explicit and versioned;
- pathways are temporally and spatially structured;
- projection, scenario, pathway and forecast semantics are separated;
- future model outputs are not represented as observations;
- downscaling assumptions and uncertainty are retained;
- uncertainty sources remain distinguishable;
- ensemble spread is not mislabelled as probability;
- hindcasting and forecasting leakage controls are implemented;
- robustness is classified by assumption/model sensitivity;
- threshold claims require explicit scientific basis;
- adaptation feedback is explicit where used;
- complete scenario-to-output lineage is maintained;
- dependency changes invalidate stale products;
- a bounded future-state product can be reproduced under the declared environment.

## 30. Transition

```text
05A SCENARIO / COUNTERFACTUAL
        ↓
05B FUTURE STATE / PATHWAY
        ↓
05C SCENARIO COMPARISON + ROBUSTNESS
        ↓
05D ADAPTATION / INTERVENTION TESTING
        ↓
05E DECISION / POLICY STRESS TEST
```

## Next step

BUILD-05C — Scenario Comparison & Robustness Engine: systematically compare baseline, counterfactual and future pathways, quantify differences, identify robust/fragile conclusions and generate a defensible scenario evidence matrix.
