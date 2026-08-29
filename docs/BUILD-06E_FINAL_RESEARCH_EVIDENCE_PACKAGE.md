# BUILD-06E — Final Research Evidence Package

## Status
FINAL RESEARCH EVIDENCE PACKAGE CONTRACT LOCKED

## Purpose
BUILD-06E freezes the complete HG-SCRIS analytical state into an auditable, reproducible and versioned research evidence package. It is the terminal packaging and release-control layer for the current 06-series. It does not create new scientific evidence; it certifies, inventories, validates and packages outputs produced upstream.

The package is a **research release artifact**, not a claim of scientific infallibility.

## 1. Core chain

```text
CERTIFIED DATA
      ↓
EVIDENCE REGISTRY
      ↓
EVENT RECONSTRUCTION
      ↓
BASELINE / RELATIONSHIPS
      ↓
FUTURE PATHWAYS
      ↓
INTERVENTIONS
      ↓
DECISION ANALYSIS
      ↓
UNCERTAINTY + CONFIDENCE
      ↓
CLAIMS + NARRATIVE
      ↓
VALIDATION / QA
      ↓
FINAL EVIDENCE PACKAGE
      ↓
RELEASE / ARCHIVE
```

## 2. Package identity

Every release must contain:

```text
package_id
package_version
project_id
study title
study scope
study area
population/system boundary
time horizon
release status
creation timestamp
software/build versions
```

## 3. Package manifest

The manifest inventories all material objects:

```text
data assets
data dictionaries
source registry
evidence objects
event records
relationship objects
uncertainty objects
scenario definitions
intervention definitions
decision rules
claims
figures
maps
tables
reports
references
QA records
validation records
provenance records
configuration files
reproducibility instructions
```

## 4. Immutable release principle

Once a package is marked `RESEARCH_RELEASE`:

```text
material objects are version-pinned
checksums/hashes are recorded where applicable
upstream versions are frozen
manifest is immutable
changes require a new package version
```

No silent replacement of source data, model output, figures or text is permitted.

## 5. Evidence ledger

The final package contains a complete evidence ledger:

```text
evidence_id
source
source version/date
source type
spatial scope
temporal scope
variable/construct
method
provenance
independence group
quality status
uncertainty refs
relationship refs
claim refs
```

## 6. Data inventory

For each data asset record:

```text
data_id
filename / logical identifier
format
provider/source
acquisition date
reference period
spatial coverage
temporal coverage
resolution
units
CRS where applicable
processing history
missingness status
quality status
checksum
license/access constraints
```

## 7. Data lineage

The package must reconstruct:

```text
RAW / SOURCE
    ↓
INGESTED
    ↓
CLEANED
    ↓
TRANSFORMED
    ↓
DERIVED
    ↓
ANALYSED
    ↓
REPORTED
```

Every derived output must have upstream lineage.

## 8. Event reconstruction package

Where applicable include:

```text
event identity
chronology
location/footprint
hazard characteristics
exposure
vulnerability
impact records
response
recovery
source conflicts
evidence gaps
reconstruction confidence
```

Historical reconstruction must remain distinguishable from direct observation and modelled reconstruction.

## 9. Relationship graph

Include the final BUILD-06B graph containing:

```text
entities / variables
relationship edges
direction
relationship class
mechanism
method
spatial scope
temporal scope
evidence refs
uncertainty refs
robustness
causal status
limitations
```

## 10. Uncertainty register

Include BUILD-06C objects:

```text
measurement
sampling
parameter
model
structural
scenario
spatial
temporal
boundary
implementation
behavioural
cost
data completeness
independence
normative/value
```

The release must preserve unquantified uncertainty where it exists.

## 11. Confidence register

For each major claim record:

```text
claim_id
confidence status
confidence rubric/version
evidence quality
independence
consistency
robustness
dominant uncertainty
causal status
scope
rationale
```

A confidence label without rationale is not release-ready.

## 12. Scenario package

For every scenario retain:

```text
scenario_id
scenario description
assumptions
drivers
boundary conditions
time horizon
spatial scope
model/version
scenario outputs
uncertainty
limitations
```

Scenarios must not be represented as observations.

## 13. Intervention package

For every intervention:

```text
intervention_id
mechanism
coverage
implementation assumptions
technical effect
implementation-adjusted effect
residual risk
cost assumptions
trade-offs
uncertainty
scenario dependence
```

## 14. Decision package

Include:

```text
decision question
options
objectives
constraints
weights/preferences
decision rule
scenario set
uncertainty treatment
sensitivity results
robustness results
selected/recommended option where applicable
reasons
limitations
```

Normative choices must remain explicit.

## 15. Claim registry

Every major claim must contain:

```text
claim_id
claim text
claim class
evidence refs
relationship refs
uncertainty refs
scenario refs
intervention refs
decision refs
confidence
causal status
scope
limitations
report locations
```

## 16. Claim closure test

A claim is `CLOSED` only when:

```text
Evidence exists
      ↓
Evidence is valid
      ↓
Dependencies are current
      ↓
Relationship is valid where required
      ↓
Uncertainty is registered
      ↓
Confidence is justified
      ↓
Scope is defined
      ↓
Narrative wording is compliant
```

Otherwise it remains `OPEN`, `LIMITED`, or `UNRESOLVED`.

## 17. Report package

Include final generated products such as:

```text
full research report
technical report
policy/decision brief where applicable
executive summary
methodology appendix
event reconstruction appendix
evidence ledger
uncertainty appendix
references
figures
maps
tables
```

Each product must reference the same frozen evidence state.

## 18. Figure / map / table registry

Every visual or table receives:

```text
object_id
object type
source data refs
processing refs
claim refs
caption/title
units
scope
uncertainty
version
```

This prevents figures from becoming detached from the evidence package.

## 19. Reference package

References must be validated and frozen with:

```text
author metadata
title
publication/source
year
identifier where available
access date where relevant
source provenance
```

No fabricated or unresolved citation may be silently included in a research release.

## 20. Reproducibility manifest

The package must declare:

```text
operating environment
software versions
library versions
workflow/build versions
configuration
input identifiers
random seeds where applicable
model parameters
execution order
validation procedures
rendering instructions
```

## 21. Environment capture

Where feasible preserve:

```text
runtime version
OS/container identity
dependency lockfile
package manager metadata
external service versions
API/model identifiers
```

External services that cannot be frozen must have their access date/version/response metadata recorded where available.

## 22. Computational provenance

Record:

```text
workflow_id
stage
input refs
operation
parameters
output refs
execution timestamp
software/build version
status
```

## 23. Validation record

Include:

```text
validation_id
object tested
test type
expected result
observed result
status
reviewer/system
limitations
```

Validation must distinguish automated QA from substantive scientific review.

## 24. Audit trail

The release must preserve:

```text
creation
modification
supersession
re-analysis
validation
approval/review
release
```

Material changes require traceable version history.

## 25. Integrity checks

Where technically feasible:

```text
file checksum
manifest checksum
object count
reference count
orphan-object detection
dangling-reference detection
schema validation
version consistency
```

## 26. Orphan and dangling dependency audit

The release must identify:

```text
claim without evidence
figure without source
report without claim lineage
relationship without evidence
uncertainty without parent object
scenario without definition
intervention without assumptions
decision result without rule
```

Any material orphan/dangling dependency blocks `RESEARCH_RELEASE`.

## 27. Staleness audit

Check all dependency states:

```text
CURRENT
STALE
SUPERSEDED
INVALID
UNKNOWN
```

A material stale object cannot be included as current evidence.

## 28. Contradiction register

Preserve unresolved conflicts:

```text
conflict_id
objects in conflict
nature of conflict
possible explanation
resolution status
impact on claims
```

Conflict must not be erased during final packaging.

## 29. Sensitivity / robustness register

Package:

```text
analysis
alternative specification
changed assumption
result
conclusion impact
robustness status
```

## 30. External validity register

For major claims record:

```text
population scope
geographic scope
time scope
hazard/context scope
model domain
scenario domain
known transfer limitations
```

## 31. Human review record

Research release requires recorded review status for:

```text
scientific interpretation
methods
uncertainty
citations
figures/maps/tables
claim language
conclusions
recommendations
```

Reviewer identity may be stored according to project governance/privacy rules.

## 32. Release states

```text
DRAFT
INCOMPLETE
QA_FAILED
QA_PASSED
SCIENTIFIC_REVIEW_PENDING
SCIENTIFIC_REVIEWED
RESEARCH_RELEASE
SUPERSEDED
WITHDRAWN
```

`RESEARCH_RELEASE` requires all mandatory gates to pass.

## 33. Release gate

The package may enter `RESEARCH_RELEASE` only if:

```text
all material inputs versioned
all major claims closed or explicitly unresolved
all major outputs traceable
no material stale dependencies
QA passed
reference integrity passed
uncertainty register complete to declared scope
human scientific review completed
reproducibility manifest complete
release manifest frozen
```

## 34. Research-release certificate

Generate a machine-readable certificate containing:

```text
package_id
package_version
release_state
manifest_hash
input_versions
build_versions
QA status
scientific-review status
known limitations
unresolved conflicts
release timestamp
```

The certificate attests to package integrity and declared review status, not universal truth.

## 35. Re-analysis and supersession

If new evidence arrives:

```text
NEW EVIDENCE
      ↓
IMPACT ANALYSIS
      ↓
AFFECTED OBJECTS
      ↓
RE-ANALYSIS
      ↓
NEW PACKAGE VERSION
      ↓
OLD PACKAGE = SUPERSEDED
```

The historical release remains archived rather than overwritten.

## 36. Minimal reproducible package

A minimal release must contain at least:

```text
manifest
source/evidence registry
input references or permitted data
workflow/configuration
claim registry
relationship registry
uncertainty registry
final report
QA record
reproducibility manifest
release certificate
```

## 37. Archive structure

Recommended structure:

```text
HG-SCRIS-RESEARCH-PACKAGE/
├── manifest/
├── data/
├── evidence/
├── events/
├── relationships/
├── uncertainty/
├── scenarios/
├── interventions/
├── decisions/
├── claims/
├── figures/
├── maps/
├── tables/
├── reports/
├── references/
├── qa/
├── provenance/
├── reproducibility/
└── release/
```

Actual storage may vary, but logical separation must be preserved.

## 38. Security / privacy boundary

The research package must not expose restricted or personally identifiable data beyond approved governance rules.

Where raw data cannot be redistributed, package:

```text
data descriptor
access conditions
checksum where possible
derivation metadata
reproducibility instructions
```

Do not weaken privacy merely to improve reproducibility.

## 39. License / rights metadata

Every redistributable object should declare applicable:

```text
license
attribution
usage restriction
redistribution status
```

## 40. Final evidence graph snapshot

The release includes a frozen graph connecting:

```text
DATA
 ↓
EVIDENCE
 ↓
EVENTS
 ↓
RELATIONSHIPS
 ↓
UNCERTAINTY
 ↓
SCENARIOS
 ↓
INTERVENTIONS
 ↓
DECISIONS
 ↓
CLAIMS
 ↓
REPORTS
```

This is the central audit structure of the final package.

## 41. Research integrity safeguards

The package must prevent:

```text
fabricated evidence
fabricated citations
silent data substitution
silent model substitution
hidden preprocessing
hidden exclusions
certainty inflation
claim drift
scope drift
orphan figures
orphan claims
stale outputs
selective conflict removal
unrecorded normative changes
```

## 42. Final scientific boundary

The package certifies:

```text
what was analysed
how it was analysed
which evidence supported it
what assumptions were used
what uncertainty remained
what claims were supported
what remained unresolved
```

It does **not** certify that every conclusion is universally true.

## 43. Final package quality dimensions

Evaluate:

```text
traceability
completeness
validity
consistency
reproducibility
transparency
uncertainty disclosure
scientific review
external-validity discipline
version integrity
```

## 44. Stop conditions

Block `RESEARCH_RELEASE` when:

```text
manifest incomplete
material data unversioned
claim lineage missing
material stale dependency exists
orphan/dangling dependency exists
QA failed
reference integrity failed
uncertainty material but undisclosed
contradiction materially hidden
report generated from mixed versions
reproducibility manifest incomplete
human scientific review incomplete
restricted data exposed
release certificate missing
```

## 45. Acceptance tests

```text
package identity test
manifest completeness test
data inventory test
data lineage test
event package test
relationship graph test
uncertainty register test
confidence register test
scenario package test
intervention package test
decision package test
claim closure test
report consistency test
figure/map/table provenance test
reference integrity test
reproducibility test
environment capture test
computational provenance test
validation record test
audit trail test
integrity/checksum test
orphan dependency test
dangling dependency test
staleness test
contradiction register test
robustness register test
external-validity test
human-review test
release-state test
release-certificate test
supersession test
security/privacy test
license/rights test
final evidence graph test
research-integrity test
```

## 46. Acceptance criteria

BUILD-06E is accepted when:

- the complete analytical state is versioned and manifest-controlled;
- all material data, evidence, relationships, uncertainty, scenarios, interventions, decisions and claims are traceable;
- the final evidence graph is frozen for the release;
- all major claims have explicit closure status;
- stale, orphaned and dangling dependencies are detected;
- contradictions remain visible;
- uncertainty and confidence metadata are preserved;
- figures, maps, tables and reports point to the same frozen evidence state;
- methods and computational provenance are reproducible to the declared scope;
- references are validated and cannot be silently fabricated;
- external validity is explicitly bounded;
- security, privacy, licensing and redistribution constraints are respected;
- automated QA and human scientific review are separately recorded;
- a release certificate records package integrity and review status;
- new evidence creates a new package version rather than silently modifying a released package;
- `RESEARCH_RELEASE` is impossible until all mandatory release gates pass.

## 47. 06-series completion

```text
06A  EVIDENCE INTEGRATION
 ↓
06B  SYSTEM / CROSS-DIMENSIONAL RELATIONSHIPS
 ↓
06C  UNCERTAINTY / CONFIDENCE SYNTHESIS
 ↓
06D  SCIENTIFIC NARRATIVE / REPORT
 ↓
06E  FINAL RESEARCH EVIDENCE PACKAGE
```

BUILD-06E is the terminal release-control layer of the current 06-series.

## 48. Next architectural phase

After the 06-series is validated as a complete chain, the next phase should **not** automatically add more analytical complexity. First perform an end-to-end architecture audit, integration test and pilot release using a bounded Himalayan case. Only after that audit should any post-06 build series be frozen.
