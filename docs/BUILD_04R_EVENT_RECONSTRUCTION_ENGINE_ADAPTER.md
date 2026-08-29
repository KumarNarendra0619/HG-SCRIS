# BUILD-04R — Event Reconstruction Engine Adapter & Evidence-to-Event Pipeline

## Status
ARCHITECTURE + SCIENTIFIC EXECUTION CONTRACT LOCKED

## Purpose
Connect the first real HG-SCRIS analytical capability—historical event reconstruction—to the BUILD-04Q adapter/job architecture. The objective is not to invent a single reconstruction algorithm. It is to create a reproducible evidence-to-event workflow in which heterogeneous observations are registered, normalized, spatially/temporally aligned, evaluated for quality, reconciled into event-process hypotheses, and exported as versioned reconstruction products with explicit confidence and provenance.

## 1. Scientific principle

A reconstruction is an inference, not a raw observation.

```text
SOURCE EVIDENCE
   ↓
OBSERVATION NORMALIZATION
   ↓
QUALITY / RELEVANCE ASSESSMENT
   ↓
TEMPORAL + SPATIAL ALIGNMENT
   ↓
EVIDENCE RECONCILIATION
   ↓
PROCESS HYPOTHESIS
   ↓
EVENT RECONSTRUCTION
   ↓
CONFIDENCE + UNCERTAINTY
   ↓
VERSIONED RECONSTRUCTION PRODUCT
```

The engine must never silently convert uncertain evidence into observed fact.

## 2. Supported evidence classes

The adapter should support, through typed source adapters:

```text
instrumental observations
remote sensing imagery
DEM / terrain products
meteorological observations
hydrological observations
field observations
photographs / video metadata
official reports
scientific literature
crowdsourced observations
historical maps / records
infrastructure observations
```

Each source retains its original provenance and source-specific quality information.

## 3. Canonical evidence record

Minimum normalized fields:

```text
evidence_id
event_id nullable
source_type
source_reference
observation_time
observation_time_precision
geometry
spatial_precision
observation_variable
value / observation payload
unit
quality_score
relevance_score
source_reliability
processing_level
original_artifact_ref
license/access
notes
```

A normalized record does not overwrite the original source.

## 4. Temporal model

The reconstruction engine must support:

```text
exact timestamp
interval
before/after relation
estimated time
unknown time
```

Temporal precision is stored separately from event time. An estimated timestamp must never be rendered as an exact observation without qualification.

## 5. Spatial model

Evidence may be:

```text
point
line
polygon
raster footprint
place reference
unknown/low precision
```

The engine preserves source geometry and precision metadata. Any derived geometry is separately registered.

## 6. Observation vs interpretation

Three layers are mandatory:

```text
OBSERVATION
   ↓
INTERPRETATION
   ↓
RECONSTRUCTION
```

Example:

```text
Observed debris deposit
       ↓
Possible high-energy flow indicator
       ↓
Reconstructed process footprint
```

The last two layers must carry reasoning/provenance metadata.

## 7. Event-process representation

An event may contain multiple interacting processes.

```text
EVENT
 ├── primary process
 ├── secondary process
 ├── cascading process
 └── compound interaction
```

Each process hypothesis includes:

```text
process_id
type
start/end estimate
spatial footprint
trigger hypothesis
supporting evidence
contradicting evidence
confidence
uncertainty
status
```

## 8. Evidence reconciliation

The engine must not use a single simplistic evidence score as the scientific decision rule.

Reconciliation should preserve:

```text
support
contradiction
independence/dependence
source quality
spatial agreement
temporal agreement
process compatibility
missing evidence
```

Where evidence conflicts, the conflict is recorded rather than averaged away.

## 9. Confidence model

Confidence must be decomposable where possible:

```text
source confidence
measurement/observation confidence
spatial confidence
temporal confidence
interpretation confidence
process confidence
overall reconstruction confidence
```

The exact aggregation method must be declared by the selected method/version and never hidden as a UI heuristic.

## 10. Reconstruction states

```text
DRAFT
EVIDENCE_REGISTERED
EVIDENCE_QA_PASSED
RECONSTRUCTION_IN_PROGRESS
RECONSTRUCTED
REVIEW_REQUIRED
REJECTED
SUPERSEDED
```

A reconstruction marked `REVIEW_REQUIRED` is not publication-ready.

## 11. Contradiction handling

Contradictory evidence generates an explicit conflict object:

```text
conflict_id
evidence_a
evidence_b
conflict_type
severity
possible_explanations
resolution_status
resolution_note
```

The engine must not silently select one source merely because it has a higher nominal score.

## 12. Method registry

Each reconstruction method must declare:

```text
method_id
method_version
scientific basis
required inputs
optional inputs
assumptions
parameters
output schema
known limitations
validation evidence
```

Multiple reconstruction methods may coexist. HG-SCRIS should support method comparison rather than hard-coding one universal method.

## 13. Adapter input contract

```text
run_id
project_id
event_id
method_id
method_version
evidence_refs[]
dataset_refs[]
parameter_set
spatial_reference
temporal_reference
review_policy
```

All referenced versions are frozen for the run.

## 14. Adapter output contract

```text
reconstruction_id
event_id
run_id
process_hypotheses[]
reconstruction_geometry_refs[]
timeline_ref
confidence_ref
uncertainty_ref
conflict_refs[]
method_id
method_version
artifact_refs[]
status
```

## 15. Evidence-to-event pipeline

```text
1. INGEST
2. REGISTER
3. NORMALIZE
4. QUALITY CHECK
5. TEMPORAL ALIGNMENT
6. SPATIAL ALIGNMENT
7. DUPLICATE / LINK ANALYSIS
8. PROCESS CANDIDATE GENERATION
9. EVIDENCE RECONCILIATION
10. CONFLICT DETECTION
11. RECONSTRUCTION
12. CONFIDENCE / UNCERTAINTY
13. HUMAN REVIEW GATE
14. VERSION + PUBLISH TO REGISTRY
```

## 16. Human review gate

High-consequence reconstruction should support expert review before certification.

Reviewers can:

```text
accept
reject
request revision
flag evidence conflict
change interpretation with justification
```

Reviewer changes become provenance records; they do not erase the prior machine-generated state.

## 17. Place-by-place reconstruction

The engine supports a place-centric decomposition:

```text
EVENT
 ↓
PLACE
 ↓
EVIDENCE SET
 ↓
LOCAL PROCESS
 ↓
LOCAL IMPACT
 ↓
LOCAL CONFIDENCE
```

This allows event reconstruction to be rebuilt spatially rather than forcing one homogeneous footprint over an entire region.

## 18. Event timeline

Timeline output supports:

```text
pre-event conditions
trigger/onset
process transitions
peak phase
secondary/cascading processes
recession/recovery indicators
post-event observations
```

Each timeline assertion points back to evidence or an explicitly labelled inference.

## 19. Uncertainty representation

Uncertainty may be represented as:

```text
interval
range
probability distribution
qualitative class
spatial confidence surface
unknown
```

The engine must not manufacture numeric probability distributions where the evidence does not support them.

## 20. Reproducibility manifest

Every reconstruction run records:

```text
method + version
input evidence IDs + versions
dataset versions
parameter set
software/code version
environment
spatial/temporal reference
random seed if applicable
execution timestamp
review state
output checksums
```

## 21. First real adapter pilot

The first real adapter should be implemented as a **method-neutral reconstruction adapter** around one explicitly documented reconstruction method.

Pilot sequence:

```text
Registered historical event
      ↓
Curated evidence bundle
      ↓
Evidence QA
      ↓
Method execution
      ↓
Place/process reconstruction
      ↓
Timeline
      ↓
Confidence + uncertainty
      ↓
Expert review
      ↓
Versioned reconstruction
```

Do not begin by claiming that the pilot reconstructs every Himalayan hazard type. Validate one bounded process/event class first, then expand.

## 22. Validation strategy

Validation must distinguish:

```text
internal consistency
cross-source agreement
spatial validation
temporal validation
independent reference validation
expert review
```

Calibration data must not be presented as independent validation data.

## 23. Failure modes

Explicitly test:

```text
missing evidence
conflicting timestamps
incompatible CRS
duplicate observations
source unavailable
unsupported variable
insufficient evidence
method incompatibility
geometry invalidity
confidence below threshold
review rejection
partial execution
```

No silent fallback to fabricated/default evidence.

## 24. Publication gate

A reconstruction can become `RESEARCH_READY` only when:

```text
all critical evidence has provenance
method/version is registered
input versions are frozen
conflicts are resolved or explicitly disclosed
uncertainty is represented
validation status is recorded
review requirements are satisfied
reproducibility manifest exists
```

## 25. Acceptance criteria

BUILD-04R is accepted when:

- canonical evidence contract is defined;
- observation/interpretation/reconstruction layers are separated;
- temporal/spatial precision is retained;
- compound event processes are supported;
- contradiction handling is explicit;
- reconstruction methods are versioned;
- adapter input/output contracts are defined;
- place-by-place reconstruction is supported;
- event timeline is provenance-linked;
- uncertainty is explicit;
- expert review is auditable;
- reproducibility manifest is mandatory;
- validation types are separated;
- bounded first-real-method pilot is defined;
- no reconstruction is silently promoted to observed fact.

## Next step

BUILD-04S — Real Reconstruction Engine Implementation, Evidence Schema Migration, Synthetic-to-Real Test Harness & First Research-Ready Event.
