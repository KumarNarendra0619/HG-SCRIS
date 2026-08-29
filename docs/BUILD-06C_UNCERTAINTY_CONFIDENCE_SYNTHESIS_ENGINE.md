# BUILD-06C — Uncertainty / Confidence Synthesis Engine

## Status
UNCERTAINTY / CONFIDENCE SYNTHESIS CONTRACT LOCKED

## Purpose
BUILD-06C integrates uncertainty across the HG-SCRIS evidence and relationship pipeline and converts it into transparent, claim-specific confidence statements. It prevents fundamentally different uncertainties from being silently collapsed into a single score and prevents uncertainty reduction from being confused with scientific certainty.

The engine is an **uncertainty accounting and confidence synthesis layer**, not a certainty generator.

## 1. Core chain

```text
CERTIFIED EVIDENCE + RELATIONSHIPS
        ↓
UNCERTAINTY REGISTRY
        ↓
UNCERTAINTY TYPE CLASSIFICATION
        ↓
PROPAGATION / DEPENDENCY GRAPH
        ↓
SENSITIVITY + ROBUSTNESS
        ↓
EVIDENCE QUALITY / INDEPENDENCE AUDIT
        ↓
CLAIM-SPECIFIC CONFIDENCE
        ↓
CONFIDENCE LANGUAGE + LIMITATIONS
        ↓
TRACEABLE UNCERTAINTY PACKAGE
```

## 2. Uncertainty contract

Every uncertainty object declares:

```text
uncertainty_id
uncertainty_version
parent_evidence_or_model_ref
uncertainty_type
quantity/parameter affected
representation
range/distribution where justified
estimation method
assumptions
dependencies
spatial scope
temporal scope
sensitivity
propagation status
limitations
```

## 3. Fundamental uncertainty classes

Keep separate:

```text
MEASUREMENT
SAMPLING
SOURCE
PARAMETER
MODEL
STRUCTURAL
SCENARIO
SPATIAL
TEMPORAL
BOUNDARY / SCOPE
IMPLEMENTATION
BEHAVIOR / ADOPTION
COST
DATA COMPLETENESS
EVIDENCE INDEPENDENCE
NORMATIVE / VALUE
```

These must not be merged merely because they all affect confidence.

## 4. Aleatory vs epistemic distinction

Where defensible, distinguish:

```text
ALEATORY / VARIABILITY
EPISTEMIC / KNOWLEDGE UNCERTAINTY
```

If the distinction cannot be defended from the data/model, record the limitation rather than forcing a classification.

## 5. Error vs uncertainty

The engine distinguishes:

```text
known bias/error
random variation
measurement uncertainty
unknown model limitations
```

Known systematic bias must not be hidden inside a symmetric uncertainty interval.

## 6. Measurement uncertainty

Record where applicable:

```text
instrument precision
observer error
classification error
geolocation error
proxy uncertainty
remote-sensing retrieval error
administrative reporting error
```

Measurement uncertainty must remain linked to the measured variable.

## 7. Sampling uncertainty

Support:

```text
sampling design
sample size
sampling variance
confidence interval
bootstrap / resampling
finite population considerations
cluster/design effects
```

Non-probability samples must not automatically receive probability-sampling uncertainty claims.

## 8. Missingness and data completeness

Classify:

```text
MCAR / MAR / MNAR where defensible
structural missingness
coverage gaps
non-response
unknown missingness mechanism
```

Imputation uncertainty must be retained where material.

## 9. Parameter uncertainty

For model parameters:

```text
parameter estimate
uncertainty interval/distribution
calibration source
parameter correlation/dependence
sensitivity
```

Point estimates must not be treated as known constants when uncertainty is material.

## 10. Model uncertainty

Distinguish:

```text
model parameter uncertainty
model specification uncertainty
model structural uncertainty
model class uncertainty
```

Where credible alternative models exist, disagreement must be preserved rather than hidden by arbitrary averaging.

## 11. Scenario uncertainty

Future pathway uncertainty must retain:

```text
scenario definition
scenario plausibility basis
forcing/driver assumptions
boundary conditions
scenario coverage
```

A scenario is not automatically a probability distribution.

## 12. Spatial uncertainty

Track:

```text
location uncertainty
spatial resolution
geocoding error
aggregation uncertainty
downscaling uncertainty
boundary uncertainty
MAUP sensitivity
```

Spatial precision must not exceed the support of the underlying evidence.

## 13. Temporal uncertainty

Track:

```text
date uncertainty
observation window
seasonality
aggregation
interpolation
extrapolation
lag uncertainty
change-point uncertainty
```

Future extrapolation must remain distinguishable from observed time series.

## 14. Boundary / scope uncertainty

Record uncertainty arising from:

```text
system boundary
population boundary
study area
hazard definition
indicator definition
time horizon
inclusion/exclusion rules
```

A narrow study boundary cannot support an unrestricted universal claim.

## 15. Implementation uncertainty

For interventions:

```text
coverage
adoption
compliance
implementation delay
institutional capacity
maintenance
operational failure
```

Modelled technical effectiveness and real-world implementation uncertainty remain separate.

## 16. Behavioral uncertainty

Where human response matters:

```text
adoption
migration
adaptation behavior
compliance
risk perception
response heterogeneity
```

Behavioral assumptions must be explicit rather than silently treated as deterministic.

## 17. Cost uncertainty

Support:

```text
capital cost
operating cost
maintenance cost
inflation/escalation assumption
funding uncertainty
cost overrun
valuation uncertainty
```

Economic decision results inherit relevant cost assumptions.

## 18. Normative / value uncertainty

Separate empirical uncertainty from:

```text
objective weights
risk tolerance
distributional preferences
equity priorities
discounting choices
acceptable residual risk
```

Changing a value judgement may change a decision without changing the empirical evidence.

## 19. Dependency graph

Uncertainty propagation follows dependencies:

```text
Source uncertainty
      ↓
Variable uncertainty
      ↓
Relationship uncertainty
      ↓
Risk/model uncertainty
      ↓
Scenario uncertainty
      ↓
Intervention uncertainty
      ↓
Decision uncertainty
```

Shared sources and common model assumptions must be represented so uncertainty is not incorrectly treated as independent.

## 20. Correlated uncertainty

When uncertainty components are dependent:

```text
U1 ↔ U2
```

independence must not be assumed merely for computational convenience.

Where covariance/dependence is unknown, the limitation is recorded.

## 21. Uncertainty propagation

Support, where methodologically justified:

```text
analytical propagation
Monte Carlo / simulation
bootstrap
Bayesian posterior propagation
ensemble modelling
interval propagation
scenario ensembles
```

The method and assumptions are part of the provenance record.

## 22. Interval interpretation safeguard

An interval must state what it represents:

```text
confidence interval
credible interval
prediction interval
uncertainty range
scenario range
expert range
```

These are not interchangeable.

## 23. Probability safeguard

Probabilities may be reported only when their interpretation is defined.

The engine must distinguish:

```text
frequentist probability
Bayesian probability
subjective/expert probability
scenario weight
frequency estimate
```

A scenario label must never be silently converted into a probability.

## 24. Confidence vs probability

The system distinguishes:

```text
confidence in a claim
probability of an event
probability distribution of a parameter
scenario plausibility
```

A qualitative “high confidence” statement is not automatically a numerical probability.

## 25. Evidence quality synthesis

Confidence synthesis may consider:

```text
relevance
validity
consistency
independence
coverage
precision
bias risk
methodological quality
replicability
uncertainty
```

The rubric must be declared and claim-specific.

## 26. Evidence independence

Multiple papers/reports derived from one dataset must not create artificial confidence through duplication.

Confidence synthesis must use the evidence dependency graph from BUILD-06A.

## 27. Convergence and divergence

Confidence may be informed by:

```text
independent convergence
consistent direction
consistent magnitude
mechanistic support
model agreement
```

But divergence must remain visible:

```text
model disagreement
source conflict
scale disagreement
temporal disagreement
method disagreement
```

## 28. Robustness contribution

Confidence should distinguish:

```text
robust finding
conditionally robust finding
specification-sensitive finding
scale-sensitive finding
time-sensitive finding
model-sensitive finding
```

Robustness does not eliminate uncertainty.

## 29. Sensitivity analysis

Test material uncertainty against:

```text
parameters
model specification
scenario
spatial scale
temporal window
sampling assumptions
missing-data assumptions
weights
thresholds
implementation assumptions
```

Identify uncertainty drivers that materially alter the conclusion.

## 30. Uncertainty budget

Where quantitative decomposition is defensible, generate:

```text
uncertainty source
contribution
method
interaction/dependence
ranking
```

Do not force a variance decomposition when the underlying uncertainty types are incompatible.

## 31. Confidence synthesis rule

A claim-specific confidence assessment should consider:

```text
Evidence quality
        +
Evidence independence
        +
Consistency/convergence
        +
Effect stability
        +
Uncertainty magnitude
        +
Model/assumption dependence
        +
Coverage
        +
Causal identification where relevant
```

The exact aggregation rule must be declared.

## 32. No universal confidence score

A single 0–100 confidence score is prohibited as the default output.

If a user explicitly requests a composite score, the system must expose:

```text
components
weights
normalization
aggregation rule
sensitivity
interpretation
```

## 33. Confidence categories

A project may define a qualitative rubric such as:

```text
HIGH SUPPORT
MODERATE SUPPORT
LIMITED SUPPORT
LOW SUPPORT
UNRESOLVED
```

The rubric must define thresholds and evidence requirements.

## 34. Claim-specific confidence

Confidence is attached to a claim, not to an entire study indiscriminately.

Example:

```text
Claim A → High support
Claim B → Moderate support
Claim C → Limited support
Claim D → Unresolved
```

This prevents a generally strong dataset from falsely strengthening unrelated claims.

## 35. Causal confidence gate

Causal confidence requires explicit consideration of:

```text
identification strategy
assumptions
confounding
reverse causality
selection
measurement
model dependence
sensitivity
```

Strong predictive performance does not substitute for causal identification.

## 36. Forecast / projection uncertainty

For future outputs retain:

```text
initial-condition uncertainty
forcing uncertainty
model uncertainty
parameter uncertainty
scenario uncertainty
structural uncertainty
```

Forecast accuracy and scenario robustness must not be conflated.

## 37. Decision uncertainty

BUILD-05E decision outputs inherit:

```text
outcome uncertainty
scenario uncertainty
implementation uncertainty
cost uncertainty
objective-weight uncertainty
constraint uncertainty
model uncertainty
```

A stable ranking may still be based on uncertain absolute outcomes.

## 38. Residual uncertainty vs residual risk

Keep distinct:

```text
RESIDUAL RISK = remaining risk after intervention
RESIDUAL UNCERTAINTY = remaining uncertainty about estimated/modelled quantities
```

Reducing uncertainty does not necessarily reduce risk.

## 39. Value-of-information linkage

Uncertainty drivers may feed BUILD-05E:

```text
uncertainty driver
      ↓
decision sensitivity
      ↓
information gap
      ↓
monitoring/research priority
```

## 40. Confidence language generator

Narrative output must be constrained by the registered confidence state.

Examples:

```text
High support: evidence is consistent and relatively robust within the declared scope.
Moderate support: evidence supports the claim but material limitations remain.
Limited support: evidence is suggestive but uncertainty or inconsistency is substantial.
Unresolved: evidence is insufficient or materially conflicting.
```

These are templates; project-specific definitions prevail.

## 41. Prohibited language escalation

The engine must not automatically convert:

```text
suggests → demonstrates
associated with → causes
likely → certain
robust under scenarios → inevitable
high support → proven
```

## 42. Uncertainty-to-claim matrix

Generate:

```text
Claim
Evidence refs
Uncertainty refs
Dominant uncertainty sources
Direction
Magnitude
Interval/range
Robustness
Causal status
Confidence status
Confidence rationale
Critical assumptions
Limitations
```

## 43. Uncertainty visualization contract

Where visual outputs are produced, prefer:

```text
intervals
ranges
ensemble spread
probability distributions where valid
scenario bands
sensitivity plots
uncertainty maps
```

Avoid false precision and misleading single-point displays.

## 44. Missing uncertainty metadata

If uncertainty cannot be quantified:

```text
UNQUANTIFIED
```

must be allowed as a valid state.

Absence of a numerical uncertainty estimate does not mean zero uncertainty.

## 45. Uncertainty completeness audit

For every major output ask:

```text
What is uncertain?
How large is it?
Why is it uncertain?
Is it quantified?
Is it dependent on another uncertainty?
Does it change the conclusion?
What evidence could reduce it?
```

## 46. Invalidation

If a material evidence, model, parameter, scenario, uncertainty distribution, dependence assumption, confidence rubric or decision weight changes:

```text
upstream change
      ↓
uncertainty synthesis = STALE
      ↓
recompute
      ↓
re-audit confidence
      ↓
new version
```

## 47. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
UNCERTAINTY_READY
PROPAGATION_PENDING
CONFIDENCE_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 48. First uncertainty product

Keep the first pilot bounded:

```text
ONE INTEGRATED CLAIM SET
        ↓
IDENTIFY 5–10 MAJOR UNCERTAINTIES
        ↓
CLASSIFY UNCERTAINTY TYPES
        ↓
MAP DEPENDENCIES
        ↓
RUN SENSITIVITY / ROBUSTNESS
        ↓
IDENTIFY DOMINANT UNCERTAINTY DRIVERS
        ↓
ASSIGN CLAIM-SPECIFIC CONFIDENCE
        ↓
GENERATE UNCERTAINTY-TO-CLAIM MATRIX
```

## 49. Stop conditions

Block or downgrade when:

```text
interval meaning undefined
probability meaning undefined
uncertainty types silently mixed
independence assumed without basis
known bias hidden in uncertainty interval
scenario treated as probability without justification
model disagreement hidden
missingness ignored where material
spatial/temporal uncertainty omitted
causal confidence inferred from prediction alone
normative uncertainty mixed with empirical uncertainty
confidence score lacks transparent rubric
false precision introduced
uncertainty materially affects conclusion but is hidden
stale dependency present
```

## 50. Acceptance tests

```text
uncertainty registry test
uncertainty classification test
aleatory/epistemic test
error-vs-uncertainty test
measurement test
sampling test
missingness test
parameter test
model uncertainty test
scenario uncertainty test
spatial uncertainty test
temporal uncertainty test
boundary uncertainty test
implementation uncertainty test
behavioral uncertainty test
cost uncertainty test
normative uncertainty test
dependency graph test
correlated uncertainty test
propagation test
interval semantics test
probability semantics test
confidence-vs-probability test
evidence quality test
independence test
convergence/divergence test
robustness test
sensitivity test
uncertainty budget test
claim-specific confidence test
causal confidence test
forecast/projection test
decision uncertainty test
residual risk/uncertainty distinction test
VOI linkage test
language escalation test
provenance test
invalidation test
reproducibility test
```

## 51. Acceptance criteria

BUILD-06C is accepted when:

- all material uncertainties are registered and typed;
- empirical, model, scenario and normative uncertainties remain distinct;
- known bias is not disguised as random uncertainty;
- interval and probability semantics are explicit;
- source dependencies prevent artificial confidence inflation;
- correlated uncertainties are not assumed independent without justification;
- uncertainty propagation is reproducible where performed;
- qualitative confidence has an explicit rubric;
- confidence is attached to individual claims rather than indiscriminately to the study;
- robustness and confidence remain conceptually distinct;
- causal confidence requires appropriate identification evidence;
- forecast, projection and scenario uncertainty remain distinguishable;
- decision uncertainty includes relevant implementation, cost and value uncertainty;
- residual risk is not confused with residual uncertainty;
- uncertainty drivers can be linked to monitoring/value-of-information priorities;
- automated narrative cannot escalate certainty beyond the registered state;
- material dependency changes invalidate stale confidence results;
- the uncertainty package is reproducible.

## 52. Transition

```text
06A SYNTHESIS / EVIDENCE INTEGRATION
                 ↓
06B SYSTEM / CROSS-DIMENSIONAL RELATIONSHIPS
                 ↓
06C UNCERTAINTY / CONFIDENCE SYNTHESIS
                 ↓
06D SCIENTIFIC NARRATIVE / REPORT ENGINE
                 ↓
06E FINAL RESEARCH EVIDENCE PACKAGE
```

## Next step

BUILD-06D — Scientific Narrative / Report Engine: convert certified evidence, relationships, uncertainty, event reconstruction, future pathways, interventions and decision results into reproducible research narratives, tables and report structures while enforcing claim-level provenance and certainty controls.
