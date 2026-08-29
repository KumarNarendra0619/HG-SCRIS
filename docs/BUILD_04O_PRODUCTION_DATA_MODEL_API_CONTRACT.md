# BUILD-04O — Production Data Model, Database Schema & API Contract

## Status
ARCHITECTURE LOCKED — implementation follows after schema review.

## Purpose
Translate BUILD-04A–04N into a stable production data contract. The database is the system of record for entities, relationships, versions, provenance, scenarios, runs, validation and outputs. UI and analytical modules must consume the contract rather than inventing their own structures.

## 1. Design principles

- Separate raw, derived and published data.
- Stable IDs; never use display names as primary keys.
- Version every material analytical object.
- Preserve historical records; do not silently overwrite research results.
- Keep geometry separate from analytical metadata where practical.
- Separate observed, reconstructed, modelled and scenario states.
- Store provenance as first-class data.
- Keep validation and uncertainty separate from result values.
- Enforce foreign keys and controlled status values.
- Use spatial database capabilities for production geospatial querying.

## 2. Recommended production stack

Primary system of record:

`PostgreSQL + PostGIS`

Supporting components may use object storage for large rasters/model artefacts and a tile/cache layer for visualization. Git stores application code and lightweight configuration; large datasets do not belong in Git history.

## 3. Core entity hierarchy

```text
project
  ├── event
  │    ├── evidence
  │    ├── event_process
  │    └── event_timeline
  │
  ├── dataset
  │    └── dataset_version
  │
  ├── scenario
  │    ├── parameter_set
  │    └── scenario_override
  │
  ├── method
  ├── model
  ├── pipeline
  ├── run
  │    ├── run_input
  │    ├── run_output
  │    └── run_log
  │
  ├── hazard_result
  ├── exposure_result
  ├── vulnerability_result
  ├── impact_result
  ├── risk_result
  ├── evacuation_result
  ├── validation_record
  ├── uncertainty_record
  └── research_product
```

## 4. Stable identifier strategy

Recommended prefixes:

```text
PRJ-      Project
EVT-      Event
EVD-      Evidence
DAT-      Dataset
DVR-      Dataset version
SCN-      Scenario
PAR-      Parameter set
MET-      Method
MOD-      Model
PLN-      Pipeline
RUN-      Execution
HAZ-      Hazard result
EXP-      Exposure result
VUL-      Vulnerability result
IMP-      Impact result
RSK-      Risk result
EVA-      Evacuation result
VAL-      Validation
UNC-      Uncertainty
OUT-      Research output
```

IDs are identifiers, not scientific meaning. Names/titles remain separate fields.

## 5. Common metadata contract

Analytical entities should share, where applicable:

```text
id
version
status
created_at
updated_at
created_by
source_reference
parent_id
provenance_id
validation_status
uncertainty_status
```

## 6. Project

```text
project
- project_id PK
- name
- description
- study_region geometry
- status
- created_at
- updated_at
```

## 7. Event

```text
event
- event_id PK
- project_id FK
- name
- start_time
- end_time
- location geometry
- event_state
- attribution_status
- confidence_status
- description
```

Event state must distinguish historical observation from reconstruction/scenario.

## 8. Evidence

```text
evidence
- evidence_id PK
- event_id FK
- source_type
- source_title
- source_reference
- observation_time
- geometry
- evidence_status
- confidence_status
- notes
```

Evidence records support claims; they are not automatically claims themselves.

## 9. Dataset and dataset_version

```text
dataset
- dataset_id PK
- name
- provider
- data_type
- license

 dataset_version
- dataset_version_id PK
- dataset_id FK
- version
- acquisition_date
- reference_period
- crs
- spatial_extent
- temporal_extent
- storage_uri
- checksum
- quality_status
- parent_dataset_version_id FK nullable
```

Raw versions remain immutable.

## 10. Scenario

```text
scenario
- scenario_id PK
- project_id FK
- event_id FK nullable
- parent_scenario_id FK nullable
- scenario_type
- name
- description
- status
```

Inheritance must be explicit. Effective parameters are resolved at run time and persisted in the run manifest.

## 11. Parameter sets

```text
parameter_set
- parameter_set_id PK
- model_id FK
- version
- parameters_json
- schema_version
- validation_status
```

Parameters should be validated against a model-specific schema before execution.

## 12. Method and model

```text
method
- method_id PK
- name
- version
- domain
- assumptions_json
- input_schema_json
- output_schema_json
- validation_status

model
- model_id PK
- method_id FK
- name
- version
- process_type
- implementation_ref
- resolution
- validation_status
- limitations
```

## 13. Pipeline

```text
pipeline
- pipeline_id PK
- name
- version
- definition_json
- status
```

The definition describes dependencies and module order; it does not contain mutable run results.

## 14. Run

```text
run
- run_id PK
- pipeline_id FK
- scenario_id FK
- status
- started_at
- completed_at
- code_commit
- environment_ref
- manifest_uri
- validation_status
- uncertainty_status
- error_code nullable
```

## 15. Run inputs/outputs

```text
run_input
- run_input_id PK
- run_id FK
- object_type
- object_id
- object_version
- role

run_output
- run_output_id PK
- run_id FK
- object_type
- object_id
- object_version
- artifact_uri
- checksum
```

## 16. Hazard result

```text
hazard_result
- hazard_result_id PK
- run_id FK
- scenario_id FK
- process_type
- state_type
- geometry/raster_ref
- depth_ref nullable
- velocity_ref nullable
- arrival_time_ref nullable
- model_id FK
- model_version
```

Large raster fields should normally be stored externally and referenced, not embedded as database blobs.

## 17. Exposure / vulnerability / impact / risk

Each result retains its analytical lineage:

```text
exposure_result
- exposure_result_id PK
- run_id FK
- hazard_result_id FK
- population_ref
- infrastructure_ref
- exposure_metrics_json

vulnerability_result
- vulnerability_result_id PK
- run_id FK
- method_id FK
- vulnerability_metrics_json

impact_result
- impact_result_id PK
- run_id FK
- hazard_result_id FK
- exposure_result_id FK
- vulnerability_result_id FK
- impact_metrics_json
- state_type

risk_result
- risk_result_id PK
- run_id FK
- hazard_result_id FK
- exposure_result_id FK
- vulnerability_result_id FK
- impact_result_id FK
- risk_metrics_json
- uncertainty_record_id FK nullable
```

## 18. Evacuation

```text
evacuation_result
- evacuation_result_id PK
- run_id FK
- scenario_id FK
- network_version
- safe_zone_version
- route_result_ref
- demand_metrics_json
- isolation_metrics_json
- bottleneck_metrics_json
- status
```

## 19. Validation

```text
validation_record
- validation_id PK
- object_type
- object_id
- validation_type
- reference_dataset_version_id FK nullable
- metric_json
- status
- reviewer
- notes
```

Calibration and independent validation must be distinguishable by validation_type.

## 20. Uncertainty

```text
uncertainty_record
- uncertainty_id PK
- object_type
- object_id
- source_type
- method
- description
- range_json nullable
- status
```

Do not force a numeric value when uncertainty cannot defensibly be quantified.

## 21. Provenance

```text
provenance_record
- provenance_id PK
- entity_type
- entity_id
- relation_type
- parent_entity_type
- parent_entity_id
- created_at
```

Core relations:

```text
derived_from
used_by
validated_against
supports_claim
visualized_as
supersedes
```

## 22. Research product

```text
research_product
- output_id PK
- project_id FK
- run_id FK
- scenario_id FK
- product_type
- title
- artifact_uri
- checksum
- certification_status
- publication_status
```

Published products must point to an immutable/frozen run configuration.

## 23. API contract

The API should expose resources rather than raw database tables.

Core endpoints conceptually:

```text
GET    /projects
POST   /projects
GET    /projects/{id}

GET    /events
POST   /events
GET    /events/{id}

GET    /datasets
GET    /datasets/{id}/versions

GET    /scenarios
POST   /scenarios
GET    /scenarios/{id}
POST   /scenarios/{id}/validate

GET    /pipelines
GET    /pipelines/{id}
POST   /runs
GET    /runs/{id}
POST   /runs/{id}/resume
POST   /runs/{id}/cancel

GET    /results/{id}
GET    /results/{id}/provenance
GET    /results/{id}/validation
GET    /results/{id}/uncertainty

GET    /maps
GET    /timeline/{event_id}
GET    /places/{place_id}/profile

POST   /products
GET    /products/{id}
POST   /products/{id}/audit
POST   /products/{id}/reproducibility-package
```

## 24. API rules

- Use stable IDs, never names, for resource addressing.
- Validate request schemas before execution.
- Never accept client-supplied validation status as authoritative.
- Never expose restricted source data through public endpoints.
- Long model jobs are asynchronous and return run_id.
- API responses should identify object version and status.
- Errors use stable machine-readable error codes.

## 25. Transaction boundaries

Database writes should be transactional for metadata state changes. Long numerical jobs must not hold a database transaction open. Instead:

```text
CREATE RUN
   ↓
COMMIT
   ↓
EXECUTE JOB
   ↓
WRITE OUTPUT
   ↓
REGISTER OUTPUT
   ↓
FINALIZE RUN
```

## 26. Spatial database rules

- Store canonical vector geometry in PostGIS.
- Enforce SRID where appropriate.
- Use spatial indexes for production query layers.
- Keep source CRS metadata.
- Do not silently reproject analytical data.
- Large rasters use managed raster/object storage with database metadata references unless a specific PostGIS raster requirement justifies otherwise.

## 27. Data lifecycle

```text
RAW
 ↓
REGISTERED
 ↓
QA_PASSED
 ↓
DERIVED
 ↓
RESEARCH_READY
 ↓
PUBLISHED
 ↓
SUPERSEDED / RETIRED
```

Deletion of source records is governed separately from analytical versioning.

## 28. Security boundaries

Three logical data planes:

```text
RESTRICTED
RESEARCH
PUBLIC
```

API authorization must be checked server-side. UI hiding is not security.

## 29. Schema migration rule

Material schema changes use explicit migration versions. Application code must declare the compatible schema version. Production deployment must fail safely when migration compatibility is not satisfied.

## 30. Acceptance criteria

BUILD-04O is complete when:

- all core entities have stable IDs;
- foreign-key relationships are defined;
- versions are explicit;
- observed/reconstructed/modelled/scenario states are represented;
- provenance is first-class;
- validation and uncertainty are separate entities;
- runs and outputs are traceable;
- scenario inheritance is explicit;
- API resources are defined independently of raw tables;
- spatial storage strategy is fixed;
- large artefacts are externally referenced;
- public/research/restricted boundaries are defined;
- schema migrations are controlled;
- an end-to-end pilot can be represented without ad-hoc fields.

## Next step

BUILD-04P — Production Database Implementation, Migration Scripts, Seed Registry & API Skeleton.
