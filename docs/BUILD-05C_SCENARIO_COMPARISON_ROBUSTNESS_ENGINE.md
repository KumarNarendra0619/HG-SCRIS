# BUILD-05C — Scenario Comparison & Robustness Engine

## Status
SCENARIO COMPARISON / ROBUSTNESS CONTRACT LOCKED

## Purpose
BUILD-05C systematically compares the certified baseline, counterfactuals and future pathways created by BUILD-05A/05B. Its primary purpose is to distinguish genuine, robust scenario signals from changes that depend strongly on assumptions, models, scale, parameters or uncertain inputs.

## 1. Core chain

```text
CERTIFIED BASELINE
      ↓
SCENARIO / PATHWAY SET
      ↓
COMPARABILITY GATE
      ↓
COMMON METRIC SPACE
      ↓
PAIRWISE / MULTI-SCENARIO COMPARISON
      ↓
SENSITIVITY + UNCERTAINTY
      ↓
ROBUSTNESS ASSESSMENT
      ↓
EVIDENCE MATRIX
      ↓
RESEARCH INTERPRETATION
```

## 2. Comparison contract

Every comparison declares:

```text
comparison_id
comparison_version
baseline_ref
scenario_refs[]
pathway_refs[]
comparison_question
spatial_domain
temporal_domain
outcome variables
metric definitions
reference state
denominator where applicable
aggregation rule
uncertainty method
sensitivity design
robustness rule
limitations
```

## 3. Comparability gate

Before any comparison:

```text
same variable definition?
compatible units?
same or transformable spatial support?
same or transformable temporal support?
compatible model semantics?
compatible aggregation?
compatible scenario horizon?
coverage comparable?
```

Failed comparability blocks quantitative comparison or marks it as restricted.

## 4. Comparison types

Support:

```text
baseline vs scenario
scenario vs scenario
pathway vs pathway
intervention vs no-intervention
historical vs counterfactual
short-horizon vs long-horizon
model vs model
ensemble vs ensemble
spatial unit vs spatial unit
```

## 5. Common metric framework

Possible metrics include:

```text
absolute difference
relative difference
percentage change
ratio
risk ratio/rate ratio where valid
excess population/assets
avoided loss
affected-area change
severity distribution change
trajectory divergence
threshold crossing-time difference
cumulative impact difference
rank change
spatial overlap/agreement
```

Each metric stores its mathematical definition, unit and reference state.

## 6. Denominator safeguard

For relative metrics:

```text
change = scenario - reference
relative change = (scenario - reference) / reference
```

The denominator must be explicitly recorded. Near-zero or zero denominators trigger a warning/block rather than silent infinite values.

## 7. Spatial comparison

Support:

```text
grid-to-grid
polygon-to-polygon
asset-to-asset
network-to-network
zonal aggregation
cross-scale comparison
```

Spatial metrics may include:

```text
overlap
intersection/union
correlation where appropriate
rank agreement
hotspot persistence
spatial displacement
boundary disagreement
```

Spatial correlation is not treated as causal evidence.

## 8. Temporal comparison

Compare:

```text
time slices
trajectories
trend/slope
peak timing
duration above threshold
cumulative burden
threshold crossing time
```

Different time resolutions require declared transformation rules.

## 9. Uncertainty-aware comparison

Do not compare point estimates only when uncertainty is material.

Possible outputs:

```text
point difference
interval difference
probability of scenario exceeding baseline where justified
distribution overlap
quantile comparison
ensemble spread
```

A probability statement requires an actual probabilistic model; ensemble counts alone do not establish probability.

## 10. Sensitivity design

Assess changes caused by:

```text
scenario drivers
parameter values
model choice
normalization
weights
cutoffs
spatial resolution
temporal window
missing-data treatment
risk function
intervention effectiveness
boundary conditions
```

## 11. Robustness definition

A conclusion is `ROBUST` only when it remains substantively consistent across the declared plausible assumptions/models/uncertainty range.

Robustness is not defined by a single p-value or a single model fit statistic.

## 12. Robustness classes

```text
ROBUST
CONDITIONALLY ROBUST
ASSUMPTION-SENSITIVE
MODEL-SENSITIVE
SCALE-SENSITIVE
DATA-LIMITED
CONFLICTING
UNRESOLVED
```

## 13. Robustness scoring safeguard

If a numerical robustness score is used, the score must be accompanied by:

```text
underlying scenarios
assumption set
threshold
metric
weighting
aggregation
uncertainty
```

A black-box robustness score is not accepted as scientific evidence.

## 14. Scenario ranking

Scenarios may be ranked by declared outcome criteria, but ranking must not imply:

```text
most likely
most probable
best policy
most realistic
```

unless independently supported by the appropriate evidence/model.

## 15. Multi-objective comparison

Where multiple outcomes matter:

```text
Outcome A
Outcome B
Outcome C
      ↓
trade-off matrix
      ↓
Pareto / dominance analysis where appropriate
```

Weights must not be introduced without explicit methodological declaration.

## 16. Trade-off and unintended consequence audit

For each scenario inspect:

```text
benefit in target outcome
harm/change in other outcomes
spatial displacement
population displacement
risk transfer
secondary/cascading effects
inequality/equity implications
```

A scenario that reduces one risk while transferring risk elsewhere must not be labelled globally beneficial without qualification.

## 17. Robust hotspot analysis

A hotspot may be classified as:

```text
persistent hotspot
scenario-specific hotspot
model-sensitive hotspot
scale-sensitive hotspot
uncertain hotspot
```

Hotspot persistence requires a declared threshold and comparison set.

## 18. Evidence matrix

Generate a structured matrix:

```text
Claim
Reference state
Scenario(s)
Metric
Direction of change
Magnitude
Uncertainty
Sensitivity
Robustness class
Supporting evidence
Limitations
```

This becomes the principal bridge from computational output to scientific interpretation.

## 19. Claim discipline

The engine distinguishes:

```text
Observed difference
Modelled difference
Scenario-conditioned difference
Association
Causal effect
Forecast
Projection
```

No stronger claim may be generated than the underlying design supports.

## 20. Statistical testing

Where appropriate, statistical tests may be used, but they are not mandatory for every spatial/scenario comparison.

The system should choose or register methods according to:

```text
outcome type
sample/dependency structure
spatial dependence
temporal dependence
distribution
comparison design
```

Multiple testing and dependence must be considered where relevant.

## 21. Spatial dependence safeguard

Pixel/zone-level observations are not automatically independent.

Where inferential statistics are used, spatial/temporal dependence must be considered or the result labelled descriptive.

## 22. Model disagreement

When models disagree:

```text
Model A → outcome
Model B → outcome
Model C → outcome
        ↓
disagreement analysis
        ↓
robustness classification
```

Disagreement is evidence about model uncertainty, not a reason to average models blindly.

## 23. Scenario ensemble comparison

For ensembles, report:

```text
central tendency where justified
range
quantiles where probabilistic interpretation is valid
ensemble spread
agreement rate only with clear denominator
outlier pathways
```

Avoid false precision.

## 24. Threshold-based robustness

If a practical/scientific threshold is declared:

```text
threshold
metric
reference
scenario set
uncertainty treatment
```

must be stored.

Threshold crossing under one scenario does not prove a physical tipping point.

## 25. Causal interpretation gate

A scenario comparison may support causal interpretation only when an appropriate causal identification design exists.

Otherwise output language remains:

```text
scenario-conditioned difference
modelled change
conditional contrast
```

## 26. Reproducibility

Every comparison records:

```text
input versions
scenario versions
baseline version
metric definitions
aggregation
parameters
software/environment
random seed where applicable
output checksums
```

## 27. Invalidation

If any compared baseline/scenario/pathway dependency changes materially:

```text
dependency changed
      ↓
comparison = STALE
      ↓
re-run
      ↓
new comparison version
```

## 28. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
COMPARISON_READY
ROBUSTNESS_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 29. First robust comparison product

The first pilot remains bounded:

```text
ONE certified baseline
      +
2–3 registered scenarios/pathways
      ↓
ONE common outcome
      ↓
ONE comparison metric set
      ↓
UNCERTAINTY + SENSITIVITY
      ↓
ROBUSTNESS CLASSIFICATION
      ↓
EVIDENCE MATRIX
```

## 30. Stop conditions

Block or downgrade when:

```text
inputs not comparable
units incompatible
reference state undefined
denominator invalid
spatial/temporal mismatch unresolved
probability claimed without probabilistic basis
causal claim unsupported
material uncertainty omitted
scenario dependency stale
statistical independence falsely assumed
model disagreement hidden
```

## 31. Acceptance tests

```text
comparison schema test
comparability gate test
unit test
reference/denominator test
spatial comparison test
temporal comparison test
uncertainty comparison test
sensitivity test
robustness classification test
ranking semantics test
multi-objective test
trade-off audit
hotspot persistence test
claim-discipline test
spatial-dependence test
model-disagreement test
ensemble semantics test
provenance test
invalidation test
reproducibility test
```

## 32. Acceptance criteria

BUILD-05C is accepted when:

- baseline and scenarios are compared only after compatibility checks;
- every metric has an explicit definition, unit and reference state;
- denominators and zero/near-zero cases are controlled;
- spatial and temporal dependence are not silently ignored;
- uncertainty is retained in comparisons;
- robustness is assessed across declared plausible assumptions/models;
- robustness classes distinguish model, scale and data sensitivity;
- scenario rankings do not imply probability without evidence;
- trade-offs and risk transfers are visible;
- model disagreement is retained rather than hidden by arbitrary averaging;
- causal claims are gated by appropriate identification evidence;
- evidence matrices link computational contrasts to defensible claims;
- dependency changes invalidate stale comparisons;
- a bounded robust comparison can be reproduced.

## 33. Transition

```text
05A SCENARIO / COUNTERFACTUAL
        ↓
05B FUTURE STATE / PATHWAY
        ↓
05C COMPARISON + ROBUSTNESS
        ↓
05D ADAPTATION / INTERVENTION TESTING
        ↓
05E DECISION / POLICY STRESS TEST
```

## Next step

BUILD-05D — Adaptation / Intervention Testing Engine: test explicit interventions against certified baseline and scenario pathways, quantify potential risk reduction, trade-offs, residual risk, implementation uncertainty and robustness without treating modelled intervention effects as guaranteed causal impacts.
