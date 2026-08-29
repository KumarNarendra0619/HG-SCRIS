# BUILD-06B — System / Cross-Dimensional Relationship Engine

## Status
SYSTEM / CROSS-DIMENSIONAL RELATIONSHIP CONTRACT LOCKED

## Purpose
BUILD-06B formalizes defensible relationships among hazard, exposure, vulnerability, demographic, environmental, infrastructural, health, livelihood and institutional dimensions. It separates observed associations, temporal/spatial dependencies, mechanistic relationships, modelled dependencies and causal claims.

The engine is a relationship-analysis layer, **not a causality generator**.

## 1. Core chain

```text
CERTIFIED EVIDENCE
      ↓
VARIABLE / ENTITY REGISTRY
      ↓
RELATIONSHIP CANDIDATE
      ↓
TEMPORAL + SPATIAL ALIGNMENT
      ↓
MECHANISM / MODEL SPECIFICATION
      ↓
STATISTICAL / SPATIAL / NETWORK TEST
      ↓
ALTERNATIVE EXPLANATIONS
      ↓
UNCERTAINTY + CONFOUNDING AUDIT
      ↓
RELATIONSHIP STATUS
      ↓
SYSTEM RELATIONSHIP GRAPH
```

## 2. Relationship contract

Every relationship declares:

```text
relationship_id
relationship_version
source_variable_ref
target_variable_ref
entity/place scope
time scope
relationship type
direction
functional form where applicable
mechanism hypothesis
method
covariates/confounders
spatial structure
temporal structure
uncertainty
evidence refs
limitations
status
```

## 3. Relationship classes

Explicitly distinguish:

```text
DESCRIPTIVE
ASSOCIATIVE
CORRELATIONAL
SPATIAL ASSOCIATION
TEMPORAL ASSOCIATION
NETWORK DEPENDENCY
MECHANISTIC
MODELLED DEPENDENCY
CAUSAL-CANDIDATE
CAUSAL-SUPPORTED
UNKNOWN / UNRESOLVED
```

A relationship cannot be promoted merely because its coefficient is statistically significant.

## 4. H/E/V/R relationship safeguards

Preserve:

```text
HAZARD
  ↓
EXPOSURE
  ↓
POTENTIAL IMPACT
  ↕
VULNERABILITY
  ↓
RISK
```

The engine must not infer that vulnerability causes hazard, or that exposure alone equals risk, unless a specific defensible model says otherwise.

## 5. Cross-dimensional domains

Support registered domains including:

```text
climate
hydrology
geomorphology
hazard
demography
migration
health
land use
settlement
infrastructure
livelihood
ecosystem
water
waste
institutions
governance
accessibility
socioeconomic conditions
```

## 6. Relationship direction

Store direction separately from causal interpretation:

```text
positive
negative
non-monotonic
threshold
U-shaped / inverted-U
conditional
heterogeneous
unknown
```

Direction must be tied to the defined variables and units.

## 7. Functional form

Where quantitatively appropriate, support:

```text
linear
log-linear
logistic
count model
nonlinear
threshold
piecewise
interaction
spatial model
temporal model
network model
machine-learning dependency
```

A flexible predictive model does not automatically provide a causal relationship.

## 8. Temporal relationship engine

Support:

```text
contemporaneous
lagged
lead-lag
seasonal
trend
change-point
before-after
longitudinal
panel
```

Temporal precedence may strengthen a causal hypothesis but is not sufficient by itself to establish causality.

## 9. Spatial relationship engine

Support:

```text
co-location
proximity
distance-decay
spatial autocorrelation
spatial clustering
hotspot overlap
network connectivity
upstream-downstream
spatial lag
spatial heterogeneity
```

Spatial dependence must be considered where relevant; ordinary independent-observation assumptions cannot be silently applied.

## 10. Scale / MAUP safeguard

Relationships must record spatial scale and zoning.

The engine should test sensitivity to plausible spatial aggregation where feasible:

```text
point/grid
settlement
village/ward
block
tehsil
District
regional
```

A relationship observed at one aggregation level must not automatically be generalized to another.

## 11. Temporal scale safeguard

Do not mix:

```text
event-scale
seasonal
annual
multi-year
future-horizon
```

without explicit transformation.

A short-term relationship does not automatically represent a long-term structural relationship.

## 12. Mechanism registry

A mechanistic relationship declares:

```text
source state
mechanism
intermediate variable
target response
boundary conditions
expected direction
supporting evidence
```

Mechanisms may be:

```text
observed
experimentally supported
literature-supported
process-model supported
hypothesized
```

Hypothesized mechanisms must remain labelled as hypotheses.

## 13. Causal inference gate

Potential causal claims require an appropriate identification strategy, such as:

```text
randomized experiment
natural experiment
quasi-experimental design
credible longitudinal causal design
instrumental-variable design where justified
regression discontinuity where justified
difference-in-differences where assumptions hold
validated mechanistic causal model
```

The engine must record the assumptions required by the selected design.

## 14. Confounding audit

Potential confounders should be identified explicitly:

```text
observed confounders
unobserved confounder risk
selection effects
reverse causality
measurement error
spatial confounding
temporal confounding
common-cause structure
```

No method can guarantee removal of unmeasured confounding unless justified by its design.

## 15. Collider / mediator safeguards

Where causal DAGs are used, the system should distinguish:

```text
confounder
mediator
collider
exposure
outcome
```

Adjustment variables must not be treated as harmless controls by default.

## 16. DAG / causal graph support

Represent:

```text
A → B
A ← C → B
A → M → B
A → C ← B
```

with node and edge provenance.

A graph is a formal hypothesis/assumption structure unless supported by appropriate evidence.

## 17. Interaction / effect modification

Support:

```text
A × B → Y
```

and identify whether interaction is:

```text
statistical interaction
mechanistic interaction
effect modification
contextual heterogeneity
unknown
```

Do not interpret statistical interaction automatically as mechanistic interaction.

## 18. Threshold and nonlinear relationships

Detect or test where appropriate:

```text
threshold
critical range
saturation
nonlinear response
regime shift
```

Threshold claims require adequate data support and uncertainty assessment.

## 19. Heterogeneity analysis

Relationship strength may vary by:

```text
place
population group
sex/age group where appropriate
income/livelihood group
hazard intensity
season
urban/rural context
infrastructure condition
institutional context
```

Do not collapse meaningful heterogeneity into a single global coefficient without justification.

## 20. Network relationships

Support system/network relationships such as:

```text
road
river
service
settlement
migration
supply
infrastructure
```

Store:

```text
node
edge
direction
weight
capacity
connectivity
failure propagation
```

Network association does not automatically establish causal propagation.

## 21. Cascading relationships

For cascading systems:

```text
Hazard A
   ↓
System disturbance
   ↓
Infrastructure/service failure
   ↓
Exposure increase
   ↓
Secondary impact
```

Each edge must have evidence/model/assumption metadata.

## 22. Feedback relationships

Support:

```text
A → B
B → A
```

and dynamic feedback loops where the temporal model can identify them.

A cross-sectional correlation cannot by itself establish feedback.

## 23. Common-driver safeguard

If:

```text
A ← C → B
```

both A and B may move together without A causing B.

The engine must flag plausible common-driver explanations.

## 24. Reverse-causality safeguard

For observed A–B relationships:

```text
A → B ?
B → A ?
A ↔ B ?
A ← C → B ?
```

Alternative directions must be considered where scientifically plausible.

## 25. Measurement-error module

Record:

```text
measurement method
measurement uncertainty
proxy status
classification error
geolocation error
temporal error
```

Proxy variables must not be silently treated as exact constructs.

## 26. Model dependency

When relationships are derived from models:

```text
input data
      ↓
model structure
      ↓
parameters
      ↓
relationship estimate
```

The relationship inherits relevant model uncertainty and applicability limits.

## 27. Machine-learning relationships

ML models may identify:

```text
predictive association
feature importance
partial dependence
nonlinear interaction
```

These are not automatically causal effects.

Feature importance must not be reported as causal importance without additional identification evidence.

## 28. Statistical significance safeguard

The engine must not equate:

```text
p < threshold
```

with scientific importance or causality.

Where appropriate report:

```text
effect size
uncertainty interval
practical magnitude
model fit
predictive performance
sensitivity
```

## 29. Multiple testing

When many relationships are screened, record:

```text
number of tests
selection procedure
multiple-testing method where applicable
exploratory vs confirmatory status
```

Discovery-oriented findings must be labelled accordingly.

## 30. Spatial autocorrelation / dependence

Where applicable assess:

```text
Moran-type dependence
local clustering
spatial residual structure
network dependence
```

Failure to account for material dependence must trigger QA review.

## 31. Robustness testing

Test relationship stability against:

```text
alternative model specification
spatial scale
temporal window
covariate set
outlier treatment
measurement definition
sample restriction
model family
```

Classify:

```text
ROBUST
CONDITIONALLY ROBUST
SPECIFICATION-SENSITIVE
SCALE-SENSITIVE
TIME-SENSITIVE
DATA-LIMITED
UNRESOLVED
```

## 32. Evidence convergence for relationships

A relationship may be strengthened by independent evidence from:

```text
field observation
statistical analysis
remote sensing
historical evidence
process model
qualitative evidence
experimental/quasi-experimental evidence
```

Convergence does not override contradictions or design limitations.

## 33. Relationship conflict

If evidence indicates different directions or mechanisms:

```text
relationship A → positive
relationship B → negative
```

retain both and investigate:

```text
scale
context
time
nonlinearity
heterogeneity
method
source dependence
```

## 34. Relationship confidence/status

Use explicit statuses:

```text
DESCRIPTIVE ONLY
ASSOCIATIVE
SUPPORTED MECHANISTIC
MODEL-DEPENDENT
CAUSAL-CANDIDATE
CAUSAL-SUPPORTED
CONFLICTING
INSUFFICIENT
UNRESOLVED
```

## 35. System relationship graph

The final graph may contain:

```text
VARIABLE / ENTITY
      ↓
RELATIONSHIP EDGE
      ↓
EVIDENCE
      ↓
METHOD
      ↓
MECHANISM
      ↓
UNCERTAINTY
      ↓
STATUS
```

Every edge is traceable to its supporting evidence and assumptions.

## 36. Cross-dimensional synthesis

Example structure:

```text
Climate change
     ↓
Hazard intensity
     ↓
Exposure change
     ↓
Infrastructure vulnerability
     ↓
Service disruption
     ↓
Population impact
     ↓
Livelihood / health outcome
```

This is a relationship hypothesis until each edge has appropriate evidence.

## 37. Relationship-to-claim matrix

Generate:

```text
Claim
Relationship ID
Source variable
Target variable
Direction
Scale
Time
Method
Mechanism
Confounders
Evidence IDs
Effect estimate where applicable
Uncertainty
Causal status
Robustness
Limitations
```

## 38. Automated interpretation safeguards

The engine must not:

```text
convert correlation to causation
invent mechanisms
ignore spatial dependence
ignore temporal ordering
hide heterogeneity
hide contradictory evidence
use p-values as effect magnitude
call feature importance causal
infer feedback from cross-sectional correlation
```

## 39. Invalidation

If a material variable definition, source, model, spatial/temporal alignment, covariate structure or causal assumption changes:

```text
upstream change
      ↓
relationship = STALE
      ↓
re-analysis
      ↓
robustness recheck
      ↓
new relationship version
```

## 40. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
RELATIONSHIP_READY
ROBUSTNESS_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 41. First relationship product

Keep the first pilot bounded:

```text
ONE CERTIFIED EVIDENCE PACKAGE
        ↓
5–10 PRE-REGISTERED RELATIONSHIP QUESTIONS
        ↓
SPATIAL + TEMPORAL ALIGNMENT
        ↓
DESCRIPTIVE / ASSOCIATIVE TESTS
        ↓
MECHANISM AUDIT
        ↓
CONFOUNDING / ALTERNATIVE EXPLANATIONS
        ↓
ROBUSTNESS TEST
        ↓
SYSTEM RELATIONSHIP GRAPH
        ↓
RELATIONSHIP-TO-CLAIM MATRIX
```

## 42. Stop conditions

Block or downgrade when:

```text
variable definitions incompatible
spatial scale incompatible
temporal support incompatible
source dependency unknown
material spatial dependence ignored
causal design absent for causal claim
reverse causality plausible and ignored
major confounder risk ignored
mediator/collider adjustment unexplained
measurement error material and ignored
multiple testing ignored in broad screening
model applicability exceeded
contradictory evidence hidden
mechanism invented
stale dependency present
```

## 43. Acceptance tests

```text
variable registry test
relationship schema test
direction test
functional-form test
temporal alignment test
spatial alignment test
MAUP sensitivity test
spatial-dependence test
mechanism test
confounder test
reverse-causality test
DAG test
mediator/collider test
interaction test
threshold test
heterogeneity test
network test
cascade test
feedback test
measurement-error test
ML-causality safeguard test
statistical-significance test
multiple-testing test
robustness test
conflict-preservation test
claim-strength test
provenance test
invalidation test
reproducibility test
```

## 44. Acceptance criteria

BUILD-06B is accepted when:

- all relationships have explicit definitions, direction and scope;
- descriptive, associative, mechanistic, modelled and causal relationships remain distinct;
- spatial and temporal dependence are addressed where material;
- MAUP and scale sensitivity are visible where relevant;
- causal claims require an appropriate identification strategy;
- confounding, reverse causality and measurement error are explicitly audited;
- DAG assumptions can be recorded where causal analysis is used;
- interaction, heterogeneity, threshold and network effects are not silently collapsed;
- ML feature importance is not treated as causality;
- statistical significance is not treated as substantive importance;
- multiple-testing issues are handled for broad screening;
- relationship conflicts are preserved and investigated;
- every relationship edge has evidence and assumption lineage;
- material dependency changes invalidate stale relationships;
- relationship-to-claim traceability is reproducible.

## 45. Transition

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

BUILD-06C — Uncertainty / Confidence Synthesis Engine: integrate measurement, sampling, model, scenario, spatial, temporal, structural and evidence-quality uncertainty into transparent confidence/robustness statements without collapsing fundamentally different uncertainties into a misleading single score.
