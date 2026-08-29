# BUILD-04T — Real Evidence Connectors, Method Registration & First Bounded Himalayan Pilot

## Status
PILOT EXECUTION CONTRACT LOCKED — no research claim is certified until the evidence, method, validation and review gates pass.

## Purpose
Operationalize BUILD-04S with real-world evidence ingestion connectors and one bounded Himalayan pilot. This stage establishes the acquisition-to-reconstruction chain, source-specific provenance, method registration, evidence freeze, execution controls, and research-readiness gate.

## 1. Scope discipline

The pilot is deliberately narrow. HG-SCRIS must not claim that the first execution reconstructs all Himalayan disasters or all process types.

The pilot is selected only after a pre-screen confirms:

- adequate multi-source evidence;
- usable temporal coverage;
- usable spatial reference;
- method applicability;
- independent validation opportunity;
- lawful/licensed access to required data.

If those conditions are not met, the pilot remains `NOT_READY` and no scientific reconstruction is forced.

## 2. Real evidence connector architecture

```text
Source
  ↓
Connector
  ↓
Raw Artifact Registry
  ↓
Checksum + Metadata
  ↓
Canonical Evidence Normalizer
  ↓
Evidence QA
  ↓
Evidence Registry
```

The connector must preserve the original artifact and source reference. Transformation is represented as a new derived artifact/evidence record.

## 3. Initial connector classes

Implement connectors as interfaces first; activate only sources that are legally and technically accessible:

```text
file/document connector
geospatial vector connector
raster/remote-sensing connector
meteorological observation connector
hydrological observation connector
official-report connector
field-photo/observation connector
literature/reference connector
```

A connector must declare authentication requirements, rate limits, licensing/access conditions, temporal/spatial coverage, supported formats, and failure behavior.

## 4. Raw artifact contract

Every acquired artifact receives:

```text
artifact_id
source_reference
retrieval_time
source_last_modified nullable
media_type
file_size
checksum
license/access metadata
spatial metadata nullable
temporal metadata nullable
connector_id
connector_version
```

Raw artifacts are immutable.

## 5. Connector provenance

```text
SOURCE
 ↓ acquired_by
CONNECTOR + VERSION
 ↓ stored_as
RAW ARTIFACT
 ↓ normalized_to
EVIDENCE VERSION
```

This chain is mandatory before evidence enters reconstruction.

## 6. Method registration

Before execution, the selected reconstruction method must be registered with:

```text
method_id
method_version
scientific rationale
process/event applicability
required evidence
optional evidence
assumptions
parameters
output schema
validation protocol
known limitations
software reference
```

A method cannot execute if its required-input contract is unresolved.

## 7. Pilot selection scorecard

Pilot selection is a gate, not a popularity decision.

Evaluate:

```text
Evidence completeness
Temporal resolvability
Spatial resolvability
Multi-source independence
Method applicability
Independent validation availability
Data licensing/access
Computational feasibility
Expert-review availability
```

Each criterion is recorded with evidence. Do not create an opaque composite score that hides a critical failure.

## 8. Evidence acquisition workflow

```text
1. Identify candidate event
2. Build source inventory
3. Verify access/licence
4. Acquire raw artifacts
5. Verify checksums
6. Register provenance
7. Normalize evidence
8. Run automated QA
9. Human source-quality review
10. Freeze evidence set
```

The frozen evidence set becomes the input boundary for the reconstruction run.

## 9. Evidence freeze

After run creation, evidence versions cannot be silently changed.

```text
EVIDENCE SET V1
       ↓
RECONSTRUCTION RUN
```

Later evidence additions create a new evidence set/reconstruction version rather than modifying the historical run.

## 10. Method execution

```text
Frozen Evidence Set
       ↓
Method Adapter
       ↓
Registered Scientific Method
       ↓
Process/Footprint Reconstruction
       ↓
Timeline
       ↓
Confidence + Uncertainty
```

All method parameters are recorded in the run manifest.

## 11. Independent validation design

Validation evidence must be identified before final certification where feasible.

Examples of potentially independent evidence classes:

```text
independent field observations
separate authoritative datasets
independent remote-sensing acquisition
post-event survey records
independent expert mapping
```

Evidence used to build the reconstruction is not automatically independent merely because it comes from another file or source record.

## 12. Pilot execution states

```text
CANDIDATE
SCREENING
DATA_ACQUISITION
EVIDENCE_QA
EVIDENCE_FROZEN
METHOD_READY
RUNNING
RECONSTRUCTED
VALIDATION
EXPERT_REVIEW
RESEARCH_READY
REJECTED
SUPERSEDED
```

## 13. First bounded Himalayan pilot

The actual event identity is selected through the pilot scorecard rather than hard-coded by software architecture.

Required pilot package:

```text
Event profile
Evidence inventory
Spatial boundary
Temporal window
Process scope
Method card
Parameter set
Validation plan
Known limitations
Expert reviewer assignment
```

The pilot must be one process/event class with sufficient evidence. Compound-process expansion follows only after the bounded case passes validation.

## 14. Place-by-place execution

For the selected event:

```text
Event
 ↓
Study places
 ↓
Local evidence bundle
 ↓
Local process hypothesis
 ↓
Local reconstruction
 ↓
Local confidence/uncertainty
 ↓
Cross-place reconciliation
```

Cross-place aggregation must preserve local differences and cannot erase contradictory local evidence.

## 15. Data-quality stop conditions

Execution must stop or move to `REVIEW_REQUIRED` when:

```text
critical evidence missing
critical source inaccessible
spatial reference unresolved
temporal alignment impossible
method applicability violated
independent validation unavailable
critical contradiction unresolved
artifact checksum failure
output schema failure
```

No default/fabricated evidence may be inserted to make the pipeline complete.

## 16. Reproducibility package

Pilot execution produces:

```text
run manifest
evidence manifest
data-source inventory
method card
parameter manifest
software/code version
environment/container reference
input checksums
output checksums
validation report
conflict register
uncertainty record
expert-review record
limitations statement
```

## 17. Research-ready certification

The pilot is `RESEARCH_READY` only when:

```text
Evidence provenance complete
AND evidence set frozen
AND method/version registered
AND execution reproducible
AND critical QA passed
AND independent validation performed or explicitly unavailable/disclosed
AND uncertainty documented
AND conflicts disclosed/resolved
AND expert review completed
AND limitations documented
```

`RESEARCH_READY` does not mean universally true. It means the reconstruction has passed the defined research-quality gates for its stated scope.

## 18. Output package

The certified pilot produces:

```text
1. Event reconstruction object
2. Place-by-place reconstruction layers
3. Event timeline
4. Process hypothesis table
5. Confidence/uncertainty products
6. Evidence-to-output provenance graph
7. Validation report
8. Limitations statement
9. Machine-readable manifest
```

## 19. Security and licensing

Connectors must not bypass access controls, paywalls, authentication restrictions, robots/access policies, or license terms. Restricted source material remains restricted in storage and output handling.

## 20. Acceptance tests

```text
connector acquisition test
checksum test
provenance test
normalization test
QA test
license/access metadata test
evidence freeze test
method registration test
input compatibility test
execution test
output validation test
independent-validation classification test
review gate test
reproducibility test
supersession test
```

## 21. Acceptance criteria

BUILD-04T is accepted when:

- real evidence connector interfaces are operational;
- at least one lawful real-source acquisition path is proven;
- raw artifacts and checksums are preserved;
- source-to-evidence provenance is complete;
- evidence QA and freeze are operational;
- one bounded reconstruction method is registered;
- pilot selection is evidence-based;
- the pilot can execute through the BUILD-04Q adapter;
- place-by-place reconstruction is supported;
- independent validation is explicitly separated from construction evidence;
- stop conditions prevent forced completion;
- reproducibility package is generated;
- expert review and certification gates are auditable.

## Next step

BUILD-04U — First Pilot Results QA, Independent Validation, Error Analysis, Reconstruction Calibration & Evidence-to-Risk Handoff.
