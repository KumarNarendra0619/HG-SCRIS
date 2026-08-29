# BUILD-04Q — Analytical Engine Adapter Layer, Job Queue Contract & First End-to-End Synthetic Event Run

## Status
ARCHITECTURE + INTEGRATION CONTRACT LOCKED

## Purpose
Connect the BUILD-04P production foundation to HG-SCRIS analytical modules without coupling the API/database directly to scientific implementations. Establish a stable adapter contract, asynchronous job lifecycle, artifact exchange, dependency checks, provenance capture, and the first synthetic end-to-end execution path.

## 1. Core principle

```text
API / UI
   ↓
ORCHESTRATOR
   ↓
ENGINE ADAPTER
   ↓
ANALYTICAL ENGINE
   ↓
ARTIFACT + METADATA
   ↓
REGISTRY / PROVENANCE / QA
```

The orchestration layer never reimplements scientific equations. Each analytical engine owns its scientific method and declares its contract.

## 2. Engine adapter contract

Every engine exposes a standard logical interface:

```text
engine_id
engine_version
input_schema
parameter_schema
capabilities
required_dependencies
execute()
validate_inputs()
validate_outputs()
health()
```

An engine may be a local Python package, containerized service, external executable, or future remote service, provided the adapter preserves the contract.

## 3. Standard execution request

```text
job_id
run_id
project_id
scenario_id
engine_id
engine_version
method_id
parameter_set_id
inputs[]
effective_parameters
execution_policy
artifact_policy
```

The effective configuration is immutable for that job.

## 4. Standard execution response

```text
job_id
run_id
status
outputs[]
warnings[]
metrics{}
execution_metadata{}
error_code
```

Scientific outputs must identify their engine, method, version and source run.

## 5. Adapter responsibilities

The adapter is responsible for:

- translating canonical HG-SCRIS inputs to engine inputs;
- validating compatibility before execution;
- invoking the engine safely;
- capturing stdout/stderr or structured logs where applicable;
- translating engine outputs back to canonical artifacts;
- calculating/registering checksums;
- reporting warnings and failure codes;
- never silently changing scientific parameters.

## 6. Engine registry

The catalog should maintain:

```text
engine_id
name
version
implementation_ref
container_ref nullable
supported_processes
input_schema
output_schema
resource_requirements
validation_status
availability_status
limitations
```

An engine is not eligible for research execution unless its registry status permits it.

## 7. Job states

```text
CREATED
QUEUED
VALIDATING
READY
RUNNING
SUCCEEDED
SUCCEEDED_WITH_WARNINGS
FAILED
CANCEL_REQUESTED
CANCELLED
RETRY_PENDING
REJECTED
```

State transitions are controlled by the worker/orchestrator, not by arbitrary client requests.

## 8. Queue contract

```text
API
 ↓
CREATE RUN
 ↓
PERSIST JOB
 ↓
QUEUE
 ↓
WORKER
 ↓
ADAPTER
 ↓
ENGINE
```

A production queue may use Redis/RQ, Celery, RabbitMQ, Kafka, or another suitable broker. The broker is replaceable; the job contract is not.

## 9. Idempotency

Every executable job receives an idempotency key derived from the run and execution attempt. Repeated delivery must not create duplicate scientific outputs.

```text
same logical job
   ↓
existing successful result → reuse/return
existing running job       → report status
failed job                 → retry only under policy
```

## 10. Retry policy

Automatic retry is permitted only for infrastructure/transient failures.

Never automatically retry a scientifically invalid input as though it were a transient failure.

Examples:

```text
RETRYABLE
- worker unavailable
- temporary storage failure
- broker timeout

NON_RETRYABLE
- invalid CRS
- missing required input
- invalid parameter
- model incompatibility
- scientific validation failure
```

## 11. Resource policy

Jobs declare:

```text
CPU
memory
storage
maximum duration
parallelism
```

Resource limits are enforced outside the scientific engine. A runaway process must be terminable without corrupting registry state.

## 12. Cancellation

Cancellation follows:

```text
CANCEL_REQUESTED
      ↓
worker receives signal
      ↓
engine terminates safely
      ↓
artifacts cleaned/marked incomplete
      ↓
run = CANCELLED
```

A cancelled run cannot be treated as a completed scientific result.

## 13. Dependency resolution

Before queueing:

```text
Scenario
  ↓
Pipeline
  ↓
Engine
  ↓
Required datasets
  ↓
Required model/method versions
  ↓
Required upstream outputs
  ↓
READY / REJECTED
```

The adapter must reject incompatible inputs rather than guessing conversions.

## 14. Artifact exchange

Canonical artifact descriptor:

```text
artifact_id
artifact_type
media_type
uri
checksum
size
crs nullable
spatial_extent nullable
temporal_extent nullable
producer_engine
producer_version
run_id
```

## 15. Provenance capture

For every output:

```text
OUTPUT
 ↓ derived_from
INPUTS
 ↓ generated_by
ENGINE + VERSION
 ↓ executed_as
RUN + SCENARIO
 ↓ configured_by
EFFECTIVE PARAMETERS
```

No output is considered registry-complete until lineage metadata is available.

## 16. Synthetic engine

BUILD-04Q introduces a deliberately simple `SYNTHETIC_TEST` engine for integration testing only.

It must:

- consume a synthetic event and synthetic spatial inputs;
- produce deterministic synthetic hazard/exposure/risk/evacuation artifacts;
- use no real disaster claim;
- carry `SYNTHETIC_TEST` status through every derived output;
- be permanently ineligible for publication/operational use.

Its purpose is to prove infrastructure, not scientific validity.

## 17. First end-to-end test event

```text
Synthetic Event
   ↓
Event Registration
   ↓
Synthetic Dataset Versions
   ↓
Synthetic Scenario
   ↓
Scenario Validation
   ↓
Pipeline Resolution
   ↓
Job Queue
   ↓
Synthetic Engine Adapter
   ↓
Synthetic Hazard
   ↓
Synthetic Exposure
   ↓
Synthetic Risk
   ↓
Synthetic Evacuation
   ↓
Output Registry
   ↓
Provenance
   ↓
Validation Record
```

## 18. Determinism requirement

The first synthetic run must be deterministic under a fixed:

```text
engine version
input versions
parameter set
scenario
random seed
```

Repeated execution should produce equivalent metrics and content checksums where the engine is designed to be deterministic.

## 19. Scientific-state separation

Every analytical result carries a state such as:

```text
OBSERVED
RECONSTRUCTED
MODELLED
SCENARIO
SYNTHETIC_TEST
```

These states must never be conflated in the UI or exported as though they were equivalent evidence.

## 20. Failure injection tests

The integration suite must deliberately test:

```text
missing input
invalid CRS
invalid parameter
engine unavailable
worker timeout
engine crash
partial artifact
provenance failure
output schema mismatch
cancellation
duplicate job delivery
```

Expected behavior is controlled failure with an auditable status—not silent fallback.

## 21. Observability

Every job emits structured events:

```text
job_id
run_id
engine_id
attempt
state
start_time
end_time
duration
worker_id
error_code
```

Sensitive data and credentials are excluded.

## 22. Security boundary

Untrusted input must never become arbitrary shell execution. Engines run with least privilege, constrained filesystem/network access where feasible, and explicit resource limits.

## 23. Adapter test contract

Every real analytical adapter must pass:

```text
schema test
input validation test
version test
execution test
output schema test
artifact integrity test
provenance test
failure test
```

Only then can it be marked `RESEARCH_READY`.

## 24. Acceptance criteria

BUILD-04Q is accepted when:

- canonical engine adapter interface is defined;
- engine registry contract is defined;
- job states are controlled;
- queue contract is stable;
- idempotency is implemented at the contract level;
- retry/cancellation rules are defined;
- dependency validation occurs before execution;
- canonical artifact descriptors exist;
- provenance is captured automatically;
- synthetic engine is isolated from real research;
- deterministic synthetic end-to-end run is possible;
- failure injection cases are defined;
- outputs retain scientific state;
- no analytical module is forced to expose its internal implementation;
- real engines can later be plugged in without changing the API contract.

## Next step

BUILD-04R — First Real Analytical Adapter: Event Reconstruction Engine + Evidence-to-Event Execution Pipeline.
