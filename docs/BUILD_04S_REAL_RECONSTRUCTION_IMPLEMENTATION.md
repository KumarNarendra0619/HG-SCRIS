# BUILD-04S — Real Reconstruction Implementation, Evidence Schema Migration & First Research-Ready Event

## Status
IMPLEMENTATION BLUEPRINT LOCKED — scientific calibration remains method-specific.

## Purpose
Turn BUILD-04R's reconstruction contract into an executable, auditable implementation while avoiding the major methodological error of pretending that one generic algorithm can reconstruct every Himalayan disaster. BUILD-04S therefore implements a bounded, method-neutral evidence/reconstruction framework first and allows a specific scientific reconstruction method to be registered and tested through it.

## 1. Scope boundary

BUILD-04S delivers:

- canonical evidence schema implementation;
- evidence normalization and QA;
- temporal/spatial alignment services;
- evidence linkage and contradiction registry;
- process-hypothesis representation;
- reconstruction run orchestration;
- confidence/uncertainty registration;
- expert review gate;
- reproducibility manifest;
- synthetic-to-real test harness;
- bounded first real event pathway.

It does **not** claim a universal Himalayan reconstruction model.

## 2. Implementation architecture

```text
Evidence Sources
      ↓
Evidence Ingestion Adapters
      ↓
Canonical Evidence Registry
      ↓
Evidence QA
      ↓
Temporal/Spatial Normalization
      ↓
Evidence Linkage + Conflict Detection
      ↓
Process Hypothesis Engine
      ↓
Registered Reconstruction Method
      ↓
Reconstruction Product
      ↓
Confidence + Uncertainty
      ↓
Expert Review
      ↓
Research-Ready Registry
```

## 3. Evidence schema

Production evidence record:

```text
evidence_id
project_id
event_id nullable
source_type
source_reference
source_title
observation_time nullable
observation_time_start nullable
observation_time_end nullable
observation_time_precision
geometry nullable
geometry_type
spatial_precision
variable
value_json
unit nullable
quality_score
source_reliability
relevance_score
processing_level
original_artifact_ref
license_ref
access_level
status
created_at
created_by
```

Original evidence is immutable. Normalized derivatives receive their own IDs and provenance links.

## 4. Evidence status lifecycle

```text
REGISTERED
 ↓
NORMALIZED
 ↓
QA_PASSED / QA_FAILED
 ↓
LINKED
 ↓
USED_IN_RECONSTRUCTION
 ↓
SUPERSEDED (only when a new normalized version replaces it)
```

A failed evidence record remains auditable and is not silently deleted.

## 5. Evidence QA

Automated checks include:

```text
schema completeness
geometry validity
CRS validity
unit consistency
timestamp validity
range/plausibility checks
duplicate detection
source-reference integrity
license/access metadata
```

Scientific plausibility checks are method-specific and must not be disguised as generic data cleaning.

## 6. Temporal normalization

Represent:

```text
instant
interval
before
after
estimated
unknown
```

Store precision explicitly. Do not convert an interval into a false exact timestamp.

Temporal relations may be represented as a directed relation graph:

```text
E1 before E2
E2 overlaps E3
E3 after E4
```

## 7. Spatial normalization

Preserve source geometry and CRS. Derived geometries receive separate records.

Supported spatial states:

```text
exact
estimated
approximate
place-level
footprint
unknown
```

Spatial transformations must record the transformation method and parameters.

## 8. Evidence linkage

Linking creates explicit relationships:

```text
duplicate_of
same_observation_as
supports
contradicts
context_for
derived_from
```

Link confidence is separate from scientific reconstruction confidence.

## 9. Contradiction registry

```text
conflict_id
evidence_a
evidence_b
conflict_type
severity
scope
possible_explanations
resolution_status
resolution_note
reviewer
```

Conflict resolution does not delete either source.

## 10. Process hypothesis object

```text
process_id
event_id
process_type
parent_process_id nullable
start_estimate
end_estimate
spatial_footprint_ref
trigger_hypothesis
supporting_evidence[]
contradicting_evidence[]
confidence_ref
uncertainty_ref
status
method_ref
```

This permits cascading and compound processes.

## 11. Reconstruction product

A reconstruction product contains:

```text
reconstruction_id
event_id
run_id
method_id
method_version
process_refs[]
geometry_refs[]
timeline_ref
confidence_ref
uncertainty_ref
conflict_refs[]
artifact_refs[]
state
review_status
```

The product is derived, never treated as raw observation.

## 12. Confidence implementation

The platform stores component-level confidence where the selected method supports it:

```text
source
observation
spatial
temporal
interpretation
process
overall
```

Aggregation is method-owned. BUILD-04S must not impose an arbitrary universal weighted average.

## 13. Uncertainty implementation

Supported forms:

```text
qualitative class
interval
range
distribution
spatial uncertainty surface
unknown
```

Unquantified uncertainty remains explicitly `UNKNOWN` rather than receiving a fabricated numeric value.

## 14. Method execution adapter

The real reconstruction method is invoked through the BUILD-04Q adapter contract.

```text
canonical inputs
      ↓
method adapter
      ↓
scientific implementation
      ↓
canonical reconstruction output
```

The adapter validates schemas and records lineage; it does not alter scientific meaning.

## 15. First real-method rule

The first real method must be bounded to one clearly defined process/event class and one study area with sufficient evidence.

Before marking it research-ready, document:

```text
scientific rationale
input requirements
assumptions
parameters
validation strategy
known failure modes
applicability limits
```

Do not market the first pilot as a universal Himalayan event reconstruction engine.

## 16. Synthetic-to-real harness

Two fixtures are mandatory:

```text
SYNTHETIC FIXTURE
    ↓ infrastructure contract
REAL-LIKE CURATED FIXTURE
    ↓ scientific method test
REAL RESEARCH EVENT
```

The real-like fixture contains anonymized/curated structure but remains clearly labelled test data. It must not be represented as field truth.

## 17. Research event onboarding

```text
1. Register project
2. Register historical event
3. Create evidence inventory
4. Attach source artifacts
5. Normalize observations
6. Run evidence QA
7. Resolve spatial/temporal reference
8. Detect duplicates/links
9. Detect contradictions
10. Register reconstruction method
11. Freeze run inputs
12. Execute reconstruction
13. Generate timeline/process outputs
14. Register confidence/uncertainty
15. Independent validation/review
16. Expert review
17. Certify or reject
```

## 18. Independent validation safeguard

Evidence used to construct the reconstruction must not automatically be labelled independent validation evidence.

Validation sources must be explicitly tagged:

```text
CALIBRATION
CONSTRUCTION
INTERNAL_CHECK
INDEPENDENT_VALIDATION
EXPERT_REVIEW
```

## 19. Reproducibility manifest

Persist:

```text
run_id
method/version
all evidence IDs + versions
dataset IDs + versions
parameter set
code commit
container/environment reference
CRS/spatial reference
temporal reference
random seed
input checksums
output checksums
review state
validation state
```

## 20. Research-ready certification

Certification requires:

```text
Evidence provenance complete
AND
Input versions frozen
AND
Method/version registered
AND
Critical conflicts resolved/disclosed
AND
Uncertainty recorded
AND
Validation recorded
AND
Review complete
AND
Manifest generated
```

Otherwise state remains `REVIEW_REQUIRED` or equivalent.

## 21. Security/data governance

Evidence access levels:

```text
RESTRICTED
RESEARCH
PUBLIC
```

Sensitive source material must not be copied into logs or public artifacts. Public products may contain derived information only when the underlying access/license policy permits it.

## 22. Test matrix

Minimum automated tests:

```text
valid evidence ingestion
invalid geometry
invalid CRS
invalid timestamp
missing source reference
duplicate evidence
conflicting evidence
interval time handling
place-level geometry
method schema mismatch
missing input
method execution failure
partial output
checksum mismatch
provenance completeness
review rejection
successful certification
```

## 23. First research-ready event gate

The first event is considered research-ready only after a human reviewer verifies that the system has preserved the distinction between:

```text
what was observed
what was inferred
what was reconstructed
what remains uncertain
what was independently validated
```

The event should be released as a versioned research object, not merely as a map layer.

## 24. Acceptance criteria

BUILD-04S is accepted when:

- executable evidence schema exists;
- evidence QA is operational;
- temporal/spatial precision is retained;
- evidence links/conflicts are persistent;
- process hypotheses are representable;
- one registered reconstruction method can execute through the adapter;
- reconstruction output is versioned;
- confidence and uncertainty are explicit;
- synthetic-to-real test harness passes;
- calibration and independent validation are separated;
- expert review is auditable;
- reproducibility manifest is complete;
- first bounded research event can reach certification without bypassing provenance/QA gates.

## Next step

BUILD-04T — Real Event Evidence Ingestion Connectors, Reconstruction Method Registration & First Bounded Himalayan Pilot Execution.
