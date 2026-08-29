# BUILD-04P — Production Database Implementation, Migrations, Seed Registry & API Skeleton

## Status
IMPLEMENTATION FOUNDATION LOCKED.

## Purpose
Implement the BUILD-04O production contract without changing its scientific meaning. This stage establishes the executable backend foundation: PostgreSQL/PostGIS schema, controlled migrations, seed registries, integrity constraints, and an API skeleton ready for analytical engines.

## 1. Implementation boundary

BUILD-04P implements infrastructure only. It must not embed hazard science, risk equations, vulnerability assumptions, or undocumented defaults.

```text
04O CONTRACT
   ↓
04P DATABASE + API FOUNDATION
   ↓
ANALYTICAL MODULES
```

## 2. Production stack

- PostgreSQL
- PostGIS
- Migration runner (Alembic or equivalent)
- Python API service (FastAPI recommended)
- Pydantic request/response schemas
- Object storage for large artefacts
- Docker Compose for reproducible local development

The exact framework may change, but the database/API contracts must remain stable.

## 3. Database schemas

Use logical PostgreSQL schemas to separate concerns:

```text
core        identity, projects, events, scenarios
catalog     datasets, methods, models, pipelines
execution   runs, inputs, outputs, logs
science     hazard, exposure, vulnerability, impact, risk, evacuation
qa          validation, uncertainty
provenance  lineage relationships
products    research products and certification
```

## 4. Required extensions

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Use database-generated UUIDs internally where appropriate; human-readable HG-SCRIS IDs remain the external identifiers.

## 5. Core tables

Minimum production tables:

```text
core.projects
core.events
core.evidence
core.event_processes
core.event_timeline
core.scenarios
catalog.datasets
catalog.dataset_versions
catalog.methods
catalog.models
catalog.parameter_sets
catalog.pipelines
execution.runs
execution.run_inputs
execution.run_outputs
execution.run_logs
science.hazard_results
science.exposure_results
science.vulnerability_results
science.impact_results
science.risk_results
science.evacuation_results
qa.validation_records
qa.uncertainty_records
provenance.records
products.research_products
```

## 6. Integrity rules

The database must enforce wherever practical:

- primary keys
- foreign keys
- unique constraints
- NOT NULL constraints for mandatory metadata
- controlled status values
- non-negative version numbers
- valid timestamps
- geometry SRID constraints where fixed
- unique dataset-version combinations
- unique method/model versions
- unique scenario names within a project where required
- immutable raw dataset versions

Application validation supplements database constraints; it does not replace them.

## 7. Versioning

Material scientific objects are immutable once used by a completed run.

```text
VERSION 1
   ↓
new material change
   ↓
VERSION 2
```

A correction must create a new version or explicit superseding record. Silent in-place modification of a referenced version is prohibited.

## 8. Seed registries

Seed data should contain only controlled vocabulary and infrastructure metadata, not fabricated scientific evidence.

Initial registries:

```text
scenario types
object states
run statuses
validation types
validation statuses
uncertainty source types
provenance relation types
product types
access/data planes
error codes
```

Example run states:

```text
DRAFT
READY
RUNNING
COMPLETED
PARTIALLY_COMPLETED
FAILED
CANCELLED
SUPERSEDED
```

## 9. Migration strategy

Migration sequence:

```text
0001_extensions
0002_core
0003_catalog
0004_execution
0005_science
0006_qa
0007_provenance
0008_products
0009_indexes_constraints
0010_seed_registries
```

Every migration must be deterministic and idempotent where the migration framework permits. Destructive migrations require an explicit review and backup strategy.

## 10. Spatial indexes

Production vector layers require appropriate GiST indexes.

Examples:

```sql
CREATE INDEX ... ON core.projects USING GIST (study_region);
CREATE INDEX ... ON core.events USING GIST (location);
CREATE INDEX ... ON core.evidence USING GIST (geometry);
```

Exact table/column names must follow the final SQL implementation.

## 11. Artifact storage contract

Large files are not stored directly in ordinary metadata tables.

```text
DB metadata
   ↓
artifact_uri
checksum
media type
size
spatial/temporal metadata
   ↓
object storage
```

The checksum is used for integrity verification.

## 12. API skeleton

Base path:

```text
/api/v1
```

Initial resource groups:

```text
/projects
/events
/datasets
/scenarios
/methods
/models
/pipelines
/runs
/results
/places
/products
```

The API exposes resources, not arbitrary SQL tables.

## 13. Required API operations

```text
GET    /projects
POST   /projects
GET    /projects/{project_id}

GET    /events
POST   /events
GET    /events/{event_id}

GET    /datasets
GET    /datasets/{dataset_id}/versions

GET    /scenarios
POST   /scenarios
GET    /scenarios/{scenario_id}
POST   /scenarios/{scenario_id}/validate

GET    /pipelines
GET    /pipelines/{pipeline_id}

POST   /runs
GET    /runs/{run_id}
POST   /runs/{run_id}/resume
POST   /runs/{run_id}/cancel

GET    /results/{result_id}
GET    /results/{result_id}/provenance
GET    /results/{result_id}/validation
GET    /results/{result_id}/uncertainty

GET    /places/{place_id}/profile

POST   /products
GET    /products/{output_id}
POST   /products/{output_id}/audit
```

## 14. API response contract

Responses should expose at minimum:

```text
id
version
status
data
links
```

Errors:

```text
code
message
request_id
details
```

Do not expose database stack traces to clients.

## 15. Run creation contract

Creating a run must:

1. validate scenario;
2. resolve pipeline dependencies;
3. freeze effective parameter values;
4. register dataset/method/model versions;
5. create a run record;
6. return run_id;
7. execute asynchronously.

The effective configuration becomes part of the run manifest.

## 16. Authentication and authorization boundary

Authentication is handled by the application layer. Authorization is checked server-side on every protected resource.

Logical access planes:

```text
RESTRICTED
RESEARCH
PUBLIC
```

The frontend must never be treated as the security boundary.

## 17. Audit fields

Mutable metadata tables should include:

```text
created_at
updated_at
created_by
updated_by
```

Where scientific immutability is required, updates are rejected rather than merely logged.

## 18. Observability

API and worker services should emit structured logs containing:

```text
request_id
run_id
project_id
scenario_id
operation
status
duration
error_code
```

Secrets, credentials and sensitive source content must not enter logs.

## 19. Health endpoints

Minimum operational endpoints:

```text
GET /health/live
GET /health/ready
```

Readiness should verify required dependencies such as the database before reporting the service ready.

## 20. Testing layers

BUILD-04P requires a test pyramid:

```text
Unit tests
   ↓
Schema/contract tests
   ↓
Database integration tests
   ↓
API integration tests
   ↓
End-to-end smoke test
```

The first end-to-end test should create a project, register a dataset/version, create an event and scenario, validate the scenario, create a run, register a mock output, and inspect provenance.

## 21. Scientific safeguard

Mock outputs in infrastructure tests must be explicitly marked:

```text
SYNTHETIC_TEST
```

They must never be eligible for publication or operational use.

## 22. Acceptance gate

BUILD-04P is accepted only when:

- PostGIS database starts reproducibly;
- all core migrations execute cleanly;
- foreign keys and constraints are active;
- controlled vocabularies are seeded;
- API starts successfully;
- OpenAPI contract is generated;
- project/event/dataset/scenario CRUD works;
- scenario validation endpoint works;
- run creation returns a run_id;
- mock asynchronous execution works;
- outputs can be registered;
- provenance can be queried;
- validation/uncertainty records can be queried;
- health checks work;
- restricted/public boundaries are enforced;
- integration smoke tests pass;
- no scientific result is generated by the infrastructure layer itself.

## Next step

BUILD-04Q — Analytical Engine Adapter Layer, Job Queue Contract & First End-to-End Synthetic Event Run.
