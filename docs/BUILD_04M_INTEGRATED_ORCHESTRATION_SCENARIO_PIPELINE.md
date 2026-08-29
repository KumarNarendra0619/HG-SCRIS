# BUILD-04M — Integrated Research Orchestration, Scenario Manager & End-to-End Pipeline Controller

## Purpose
Connect the HG-SCRIS analytical modules into one controlled, dependency-aware, reproducible research workflow without collapsing distinct scientific concepts into a single opaque model.

## Core principle

`ORCHESTRATE, DON'T OVERWRITE`

The controller coordinates modules, versions, dependencies, scenarios, validation gates and outputs. It does not silently modify source data or bypass scientific eligibility rules.

## End-to-end pipeline

```text
DATA INGESTION
    ↓
DATA QA / VERSIONING
    ↓
EVENT IDENTIFICATION
    ↓
EVENT RECONSTRUCTION
    ↓
NETWORK / CONNECTIVITY
    ↓
PROCESS-SPECIFIC HAZARD MODEL
    ↓
EXPOSURE
    ↓
VULNERABILITY
    ↓
IMPACT
    ↓
RISK
    ↓
EVACUATION / ACCESSIBILITY
    ↓
2D / 3D / TEMPORAL VISUALIZATION
    ↓
VALIDATION + UNCERTAINTY
    ↓
RESEARCH PRODUCT
```

## 1. Pipeline manifest

Every end-to-end workflow receives a pipeline_run_id and records:

- project_id
- event_id
- scenario_id
- pipeline_version
- selected modules
- dependency graph
- dataset versions
- method versions
- model versions
- parameter sets
- execution order
- run IDs
- validation gates
- final certification state

## 2. Dependency-aware execution

Modules execute only when prerequisites are satisfied.

Example:

```text
Hazard model
  requires → reconstructed event
  requires → eligible terrain/network inputs

Risk
  requires → hazard result
  requires → exposure
  requires → approved vulnerability method

Evacuation
  requires → hazard timing
  requires → network
  requires → safe-zone candidates
```

If a prerequisite fails, downstream execution is blocked or explicitly marked unavailable. The controller must not manufacture missing inputs.

## 3. Scenario Manager

Scenarios are first-class objects, not temporary parameter edits.

Minimum fields:

```text
scenario_id
scenario_name
scenario_type
parent_scenario_id
hazard/process assumptions
source parameters
terrain/network state
exposure snapshot
vulnerability method
routing assumptions
created_by
created_at
status
```

Scenario types may include:

- HISTORICAL_RECONSTRUCTION
- BASELINE
- SENSITIVITY
- LOW
- BASE
- HIGH
- COMPOUND
- STRESS_TEST
- FUTURE_SCENARIO
- SYNTHETIC_TEST

## 4. Scenario inheritance

A scenario may inherit a baseline configuration but material changes must be explicit.

```text
BASELINE
   ↓
Scenario S1
   ├── source volume changed
   ├── network closure changed
   └── population snapshot changed
```

Inherited values must remain traceable to their parent scenario.

## 5. No hidden parameter changes

The controller must display effective parameters before execution.

```text
DEFAULT
  ↓
INHERITED
  ↓
OVERRIDDEN
  ↓
FINAL EFFECTIVE VALUE
```

Every override requires provenance.

## 6. Pipeline states

```text
DRAFT
↓
CONFIGURED
↓
READY_FOR_QA
↓
QA_PASSED
↓
RUNNING
↓
PARTIALLY_COMPLETED / COMPLETED / FAILED
↓
VALIDATION_PENDING
↓
RESEARCH_READY
↓
PUBLISHED / SUPERSEDED
```

## 7. Failure handling

Failures must be explicit and recoverable.

Required categories:

- INPUT_MISSING
- INPUT_INVALID
- CRS_MISMATCH
- VERSION_CONFLICT
- MODEL_NOT_ELIGIBLE
- PARAMETER_INVALID
- COMPUTATION_FAILED
- VALIDATION_FAILED
- PROVENANCE_INCOMPLETE
- RESOURCE_LIMIT

A failed downstream module must not be represented as a successful final risk result.

## 8. Partial execution

The controller supports safe resume:

```text
Completed modules
      ↓
checkpoint
      ↓
failed module
      ↓
fix input/configuration
      ↓
resume from valid checkpoint
```

Previously completed immutable runs remain available for audit.

## 9. Scenario comparison

Compare scenarios without overwriting them:

```text
Scenario A
Scenario B
Scenario C
```

Comparison outputs can include:

- hazard extent difference
- arrival-time difference
- exposed population difference
- infrastructure difference
- risk difference
- evacuation-route difference
- isolation difference

Differences must reference the exact versions used in each scenario.

## 10. Sensitivity analysis

Where model structure permits, the controller can run controlled parameter perturbations.

```text
Parameter X
 ├── low
 ├── base
 └── high
```

Sensitivity results must not be mislabeled as uncertainty probabilities.

## 11. Validation orchestration

Validation gates are executed after the relevant module outputs exist.

```text
DATA QA
 ↓
EVENT QA
 ↓
MODEL QA
 ↓
HAZARD VALIDATION
 ↓
EXPOSURE QA
 ↓
RISK VALIDATION
 ↓
EVACUATION QA
 ↓
FINAL RESEARCH QA
```

The exact gates are conditional on the modules and evidence available.

## 12. Provenance integration

The pipeline controller consumes BUILD-04L governance records rather than creating a parallel lineage system.

Every output points back to:

```text
pipeline_run_id
module_run_id
input versions
method/model versions
scenario_id
```

## 13. Output registry

Every production artifact is registered:

```text
output_id
output_type
pipeline_run_id
module_run_id
scenario_id
state
validation_status
file/location reference
checksum
created_at
supersedes
```

Examples:

- event reconstruction layer
- hazard raster
- hazard vector
- exposure table
- risk surface
- evacuation route layer
- 2D map
- 3D scene configuration
- animation
- research report

## 14. Reproducibility bundle

The controller should generate a machine-readable bundle containing:

```text
pipeline manifest
scenario manifest
data manifest
method/model manifests
parameter manifest
run manifests
validation report
uncertainty report
output registry
code/dependency references
```

## 15. Research modes

### Exploration mode
Fast iteration; outputs remain DRAFT and cannot silently become publication products.

### Research mode
Full provenance, QA and validation controls enabled.

### Publication mode
Frozen input/method/model versions and final QA required before certification.

### Emergency/operational view
Only validated/approved products are exposed; speculative research outputs remain separated.

## 16. Human approval gates

Automated execution does not replace scientific judgement.

Approval checkpoints may be required for:

- event/process attribution
- model eligibility
- parameter overrides
- vulnerability method selection
- final validation
- publication certification

## 17. Resource-aware execution

Heavy tasks may be delegated to appropriate compute environments, while lightweight orchestration remains local/web-compatible.

The controller records execution target and resource metadata but does not require a specific infrastructure vendor.

## 18. Security and integrity

The controller should enforce:

- immutable raw inputs
- validated configuration schema
- controlled writes
- no arbitrary executable configuration from untrusted inputs
- artifact checksum verification
- least-privilege execution where supported
- secrets excluded from manifests/logs

## 19. API/UI contract

The UI should expose five primary actions:

```text
CREATE PROJECT
CREATE EVENT
CREATE SCENARIO
RUN PIPELINE
AUDIT RESULT
```

Advanced users can inspect module-level configuration, while non-coders see guided forms and status indicators.

## 20. Pipeline dashboard

Suggested state view:

```text
PROJECT: HG Event X

[✓] Data QA
[✓] Event Reconstruction
[✓] Network
[✓] Hazard
[✓] Exposure
[✓] Vulnerability
[✓] Risk
[✓] Evacuation
[✓] Visualization
[!] Validation pending

Scenario: BASE
Pipeline: PR-0007
Status: VALIDATION_PENDING
```

## 21. End-to-end acceptance test

A pilot pipeline must be able to:

1. register a dataset and event;
2. create a scenario;
3. resolve dependencies;
4. run eligible modules in order;
5. stop safely on failed prerequisites;
6. checkpoint and resume;
7. register every output;
8. execute applicable QA/validation gates;
9. preserve uncertainty and provenance;
10. generate a reproducibility bundle;
11. compare at least two scenarios without overwriting either;
12. produce a final research-ready status only when required gates pass.

## 22. Non-goals

BUILD-04M does not:

- replace scientific model packages;
- invent missing observations;
- automatically certify scientific validity;
- convert uncertainty into arbitrary probabilities;
- issue autonomous emergency orders;
- overwrite historical runs;
- treat visual similarity as validation.

## Acceptance gate

BUILD-04M is architecturally complete when the modules from BUILD-04A through BUILD-04L can be represented as a dependency-aware pipeline, scenarios are versioned and comparable, failures are explicit, checkpoints are resumable, outputs are registered, and the complete run can produce a reproducibility package.

## Next step
BUILD-04N — Integrated HG-SCRIS Research Workspace, No-Code UI/UX, Project/Event/Scenario Management and Analyst Dashboard.
