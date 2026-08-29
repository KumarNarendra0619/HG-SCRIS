# BUILD-06A — Synthesis / Evidence Integration Engine

## Status
SYNTHESIS / EVIDENCE INTEGRATION CONTRACT LOCKED

## Purpose
BUILD-06A integrates certified evidence and outputs from the HG-SCRIS pipeline into a traceable multidimensional synthesis. It connects reconstructed events, hazard, exposure, vulnerability, risk, future pathways, intervention tests and decision stress-tests without double counting evidence or overstating causal certainty.

The engine is an **evidence-integration layer**, not a mechanism for manufacturing certainty from heterogeneous evidence.

## 1. Core scientific chain

```text
CERTIFIED EVIDENCE UNITS
        ↓
SOURCE / DATA PROVENANCE
        ↓
EVIDENCE NORMALIZATION
        ↓
ENTITY / PLACE / TIME ALIGNMENT
        ↓
EVIDENCE DEPENDENCY GRAPH
        ↓
CROSS-DIMENSIONAL INTEGRATION
        ↓
CONVERGENCE / CONFLICT ANALYSIS
        ↓
UNCERTAINTY + QUALITY
        ↓
SYNTHESIS CLAIMS
        ↓
TRACEABLE EVIDENCE PRODUCT
```

## 2. Evidence unit contract

Every evidence unit declares:

```text
evidence_id
evidence_version
source_ref
source_type
author/producer where available
publication/data date
observation/model/simulation status
spatial support
temporal support
variable/indicator
unit
method
sample/coverage where applicable
quality state
uncertainty
limitations
lineage
```

## 3. Evidence classes

Support explicit classes:

```text
OBSERVED
MEASURED
SURVEY-DERIVED
REMOTE-SENSING-DERIVED
ADMINISTRATIVE
HISTORICAL/ARCHIVAL
MODELLED
SIMULATED
PROJECTED
FORECAST
EXPERT-ELICITED
THEORETICAL
```

Evidence class must never be inferred merely from a file name.

## 4. Evidence hierarchy safeguard

The system must not impose a universal hierarchy in which one evidence class is automatically superior in every research question.

Evidence strength depends on:

```text
question fit
methodological quality
measurement validity
independence
coverage
uncertainty
bias risk
replicability
```

## 5. Evidence normalization

Before integration, standardize where defensible:

```text
units
coordinate reference
spatial identifiers
time reference
variable definitions
classification schemes
missing-value semantics
uncertainty representation
```

Original values and transformations must be retained.

## 6. Spatial alignment

Evidence may exist at:

```text
grid
point
line/network
parcel/asset
settlement
ward/village
block/district
watershed
regional
```

Cross-scale integration requires explicit aggregation/downscaling metadata.

No spatial transformation creates direct observations at the target scale.

## 7. Temporal alignment

Support:

```text
event time
observation date
reference period
season
annual series
multi-year period
future horizon
```

Temporal aggregation/interpolation/extrapolation must be declared.

## 8. Entity resolution

The engine resolves common entities across evidence:

```text
place
settlement
administrative unit
hazard event
asset
population group
indicator
intervention
scenario
```

Ambiguous matches remain unresolved rather than being silently merged.

## 9. Evidence dependency graph

A central requirement is to identify non-independent evidence:

```text
Original dataset
      ↓
Report
      ↓
Paper A
      ↓
Review B
```

These are not four independent evidence units.

Dependency links may include:

```text
derived-from
replicates
reuses
cites
calibrated-on
trained-on
shares-source-with
```

## 10. Double-counting prevention

Evidence derived from the same underlying source cannot be counted as independent support multiple times.

The engine maintains:

```text
source lineage
independence group
derived evidence links
weighting/aggregation rule
```

## 11. Evidence quality dimensions

Assess separately:

```text
relevance
validity
completeness
spatial adequacy
temporal adequacy
measurement quality
method quality
bias risk
uncertainty
reproducibility
independence
```

Avoid reducing these to a single unexplained score.

## 12. Cross-dimensional integration

The primary integration structure is:

```text
HAZARD
  ↘
   EXPOSURE → IMPACT / RISK
  ↗              ↑
VULNERABILITY ───┘
      ↑
SOCIAL / ENVIRONMENTAL / INFRASTRUCTURAL CONTEXT
```

Additional dimensions may include:

```text
climate
hydrology
geomorphology
demography
land use
infrastructure
health
livelihoods
ecosystems
institutions
```

The engine records whether each relationship is observed, modelled, hypothesized or assumption-based.

## 13. Event reconstruction integration

Historical/event evidence may be integrated as:

```text
EVENT
 ↓
HAZARD FOOTPRINT
 ↓
EXPOSURE AT EVENT TIME
 ↓
VULNERABILITY CONDITIONS
 ↓
OBSERVED IMPACT
 ↓
RESPONSE / RECOVERY
 ↓
LESSONS FOR FUTURE PATHWAYS
```

Future inference must not be treated as direct historical evidence.

## 14. Convergence analysis

When independent evidence supports the same finding:

```text
Evidence A
Evidence B
Evidence C
      ↓
CONVERGENCE
```

Convergence strengthens confidence only to the extent that the evidence is genuinely independent and methodologically credible.

## 15. Conflict analysis

When evidence disagrees:

```text
Evidence A → finding X
Evidence B → finding Y
        ↓
CONFLICT ANALYSIS
```

Possible causes:

```text
scale difference
time difference
different measurement
sampling variation
model structure
source dependency
contextual heterogeneity
real temporal/spatial change
```

Conflict must be retained, not averaged away automatically.

## 16. Evidence synthesis states

For each synthesis claim:

```text
SUPPORTED
CONVERGENT
CONDITIONALLY SUPPORTED
MIXED
CONFLICTING
INSUFFICIENT
UNRESOLVED
```

## 17. Claim strength gate

The synthesis language must match evidence:

```text
Observed
Associated with
Consistent with
Suggests
Modelled as
Scenario-conditioned
Supports the hypothesis that
Demonstrates causal effect only when justified
```

The system must prevent automatic upgrading from association to causation.

## 18. Causal evidence gate

A causal claim requires an appropriate identification design/evidence base.

Possible supporting designs may include:

```text
randomized experiment
natural experiment
quasi-experiment
credible longitudinal causal design
validated mechanistic causal model
```

Correlation, spatial overlap, before-after description or scenario contrast alone does not automatically establish causality.

## 19. Evidence-to-claim matrix

Generate:

```text
Claim
Evidence IDs
Evidence classes
Independence group
Direction
Magnitude where available
Uncertainty
Quality dimensions
Contradictory evidence
Causal status
Synthesis status
Limitations
```

## 20. Multidimensional triangulation

Triangulation may combine:

```text
quantitative
qualitative
spatial
temporal
remote sensing
field observation
administrative
historical
model-based
```

Triangulation is not simple majority voting.

## 21. Weighting safeguard

Evidence weighting is allowed only with an explicit method.

Weights must preserve:

```text
evidence quality rationale
independence
relevance
uncertainty
weight sensitivity
```

No hidden weighting.

## 22. Uncertainty synthesis

Separate:

```text
measurement uncertainty
sampling uncertainty
source uncertainty
model uncertainty
scenario uncertainty
spatial uncertainty
temporal uncertainty
structural uncertainty
```

Synthesis must not produce false precision by combining heterogeneous uncertainty formats without justification.

## 23. Confidence language

If qualitative confidence language is used, its rubric must be declared.

Example:

```text
HIGHER SUPPORT
MODERATE SUPPORT
LIMITED SUPPORT
LOW SUPPORT
UNRESOLVED
```

These labels are not universal probabilities unless formally calibrated.

## 24. Hazard–Exposure–Vulnerability–Risk integration

The engine preserves the distinction:

```text
HAZARD ≠ EXPOSURE ≠ VULNERABILITY ≠ RISK
```

Risk outputs must retain their functional definition and not be conflated with any one component.

## 25. Future pathway integration

Outputs from BUILD-05B/05C may be incorporated as:

```text
scenario-conditioned evidence
projection
forecast where eligible
robustness result
```

They must not be silently merged with observations as though they were the same evidence type.

## 26. Intervention integration

BUILD-05D outputs enter as:

```text
modelled intervention effect
potential avoided impact
residual risk
implementation-sensitive result
adaptation robustness
```

Observed intervention outcomes remain separately classified.

## 27. Decision integration

BUILD-05E outputs enter as:

```text
option performance
stress-test result
regret
robustness
failure condition
trade-off
monitoring need
```

Decision preference remains separate from empirical evidence.

## 28. Evidence synthesis graph

The integrated graph may be represented as:

```text
SOURCE
  ↓
EVIDENCE
  ↓
FINDING
  ↓
RELATIONSHIP
  ↓
SYNTHESIS CLAIM
  ↓
SCENARIO / INTERVENTION IMPLICATION
  ↓
DECISION EVIDENCE
```

Every downstream claim retains upstream lineage.

## 29. Contradiction resolution protocol

When evidence conflicts:

```text
1. Verify source identity
2. Verify independence
3. Check variable definitions
4. Check spatial scale
5. Check temporal period
6. Check method/model
7. Check uncertainty
8. Check coverage/bias
9. Determine whether conflict is substantive
10. Preserve unresolved conflict if not resolvable
```

## 30. Synthesis narrative generator safeguards

Automated narrative may generate only from registered evidence and claims.

It must not:

```text
invent mechanisms
invent citations
upgrade certainty
hide contradictory evidence
invent missing values
convert projections into observations
convert association into causation
```

## 31. Reproducible synthesis package

Every synthesis stores:

```text
input evidence IDs/versions
source dependency graph
transformations
alignment rules
weighting rules
integration rules
claim rules
software/environment
output version
```

## 32. Invalidation

If a material source, evidence unit, transformation, scenario, intervention or model changes:

```text
upstream dependency changed
        ↓
synthesis = STALE
        ↓
recompute
        ↓
re-audit claims
        ↓
new synthesis version
```

## 33. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
INTEGRATION_READY
SYNTHESIS_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 34. First synthesis product

Keep the first integration bounded:

```text
CERTIFIED BASELINE
      +
ONE EVENT RECONSTRUCTION
      +
2–3 H/E/V/R evidence layers
      +
2–3 future/scenario results
      +
ONE intervention test
      +
ONE decision stress-test
      ↓
EVIDENCE DEPENDENCY GRAPH
      ↓
CONVERGENCE / CONFLICT
      ↓
EVIDENCE-TO-CLAIM MATRIX
      ↓
MULTIDIMENSIONAL SYNTHESIS
```

## 35. Stop conditions

Block or downgrade when:

```text
evidence provenance missing
source dependency unknown
same dataset counted as independent multiple times
spatial/temporal mismatch unresolved
variable definitions incompatible
modelled output treated as observation
projection treated as forecast without eligibility
causal claim unsupported
contradictory evidence hidden
uncertainty omitted
false precision introduced
missing mechanism invented
stale dependency present
```

## 36. Acceptance tests

```text
evidence schema test
source provenance test
independence/dependency test
double-counting test
unit normalization test
spatial alignment test
temporal alignment test
entity resolution test
quality-dimension test
H/E/V/R separation test
event-reconstruction test
convergence test
conflict-preservation test
claim-strength test
causal gate test
triangulation test
weight transparency test
uncertainty synthesis test
future-pathway integration test
intervention integration test
decision integration test
narrative safeguard test
invalidation test
provenance test
reproducibility test
```

## 37. Acceptance criteria

BUILD-06A is accepted when:

- every integrated evidence unit has provenance and versioning;
- evidence classes remain distinct;
- source dependencies and independence groups are explicit;
- double counting is prevented;
- spatial and temporal alignment is declared;
- H/E/V/R concepts remain analytically distinct;
- event reconstruction is integrated without confusing historical and future evidence;
- convergence and contradiction are both retained;
- evidence strength is not reduced to an unexplained universal score;
- causal claims are gated by appropriate identification evidence;
- projections, forecasts, models and observations remain distinguishable;
- intervention and decision outputs remain conditionally classified;
- evidence-to-claim traceability is complete;
- automated narratives cannot invent evidence or upgrade certainty;
- material dependency changes invalidate downstream synthesis;
- the synthesis package is reproducible under the declared environment.

## 38. Transition

```text
BUILD-05 CERTIFIED DECISION-SUPPORT LAYER
                 ↓
06A SYNTHESIS / EVIDENCE INTEGRATION
                 ↓
06B SYSTEM / CROSS-DIMENSIONAL RELATIONSHIP ENGINE
                 ↓
06C UNCERTAINTY / CONFIDENCE SYNTHESIS
                 ↓
06D SCIENTIFIC NARRATIVE / REPORT ENGINE
                 ↓
06E FINAL RESEARCH EVIDENCE PACKAGE
```

## Next step

BUILD-06B — System / Cross-Dimensional Relationship Engine: formalize defensible relationships among hazard, exposure, vulnerability, demographic, environmental, infrastructural and institutional dimensions, distinguishing observed associations, mechanistic links, modelled dependencies and causal claims.
