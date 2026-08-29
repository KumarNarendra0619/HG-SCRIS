# AUDIT-02 — Configuration, Schema & Cross-Stage Contract Consistency

## Status
AUDIT-02 COMPLETE — CONFIGURATION BASELINE ALIGNED; IMPLEMENTATION GAPS REMAIN OPEN

## Scope
This audit reconciles the repository configuration and cross-stage scientific contracts after the BUILD-01 through BUILD-06E architecture freeze. It does not add new scientific functionality.

## Audited chain

```text
BUILD-01 Foundation
    ↓
BUILD-02 Real Data / Pilot
    ↓
BUILD-03 Analytical + Web Architecture
    ↓
BUILD-04 Production / Vertical Slice
    ↓
BUILD-05 Scenario / Decision Intelligence
    ↓
BUILD-06 Evidence Synthesis / Research Release
```

## Fixes applied

### 1. Project lifecycle metadata

Updated the repository baseline from the obsolete BUILD-01A / v0.1.0 declaration to:

```text
version: 0.6.1
stage: AUDIT-02
```

This is an audit/integration version, not a v1.0 scientific release.

### 2. Confidence model

The obsolete three-class configuration was replaced with the BUILD-06 qualitative five-state model:

```text
HIGH_SUPPORT
MODERATE_SUPPORT
LIMITED_SUPPORT
LOW_SUPPORT
UNRESOLVED
```

Confidence remains claim-specific and is not treated as event probability.

### 3. Scientific evidence states

The project configuration now explicitly registers:

```text
OBSERVED
INFERRED
MODELLED
SCENARIO
UNCERTAIN
```

These states must remain distinguishable through analytical and visualization outputs.

### 4. Spatial reference contract

EPSG:4326 is retained as storage/exchange CRS only. Metric operations must use an explicitly declared project-local projected analysis CRS.

This prevents silent misuse of geographic degrees as metres for distance, area, slope or routing calculations.

### 5. Provenance contract

Provenance was expanded to include:

```text
dataset_id
dataset_version
method_id
parameter_set
processing_date
code_version
scientific_state
confidence
uncertainty_refs
source_refs
```

### 6. Cross-stage contract versions

The configuration now registers explicit versions for:

```text
schema_version: 1.0
evidence_state_model: 1.0
uncertainty_model: 1.0
claim_model: 1.0
provenance_model: 1.0
```

### 7. Release-blocking integrity rules

The baseline now explicitly requires release blocking for:

```text
stale dependencies
orphan dependencies
undefined probability semantics
false precision
failure to separate observed/inferred/modelled states
```

## Remaining findings

### FINDING-02-01 — QA implementation gap

The configuration is now aligned with the scientific QA contract, but the current QA implementation remains a lightweight deterministic core. Full CRS, geometry, raster metadata, temporal metadata, licence and provenance validation still require implementation and tests.

Status: OPEN — AUDIT-03

### FINDING-02-02 — Visualization state enforcement gap

Scientific evidence states are now canonical configuration values, but the visualization layer must still enforce state-aware rendering and prevent accidental conflation of observed, inferred, modelled, scenario and uncertain outputs.

Status: OPEN — AUDIT-03

### FINDING-02-03 — Evacuation engine gap

The routing primitive exists, but complete scenario/time-aware evacuation logic requires hazard-arrival timing, response margin, route availability/closure, safe-zone capacity, alternatives and unserved-demand accounting.

Status: OPEN — AUDIT-03

### FINDING-02-04 — Real-data certification gap

No configuration change can substitute for execution of a complete real Himalayan vertical slice. BUILD-04Z/06E research-readiness remains blocked until the integrated pilot is executed and independently validated.

Status: OPEN — AUDIT-05 onward

### FINDING-02-05 — BUILD-03M transition documentation

BUILD-03L historically points toward BUILD-03M, while the implementation pathway subsequently transitions into BUILD-04. This is a documentation lineage issue, not a scientific-model defect. The transition should be formally recorded in the stage map.

Status: OPEN — AUDIT-03

## Consistency matrix

| Contract | Previous state | Audit-02 state |
|---|---|---|
| Project stage | BUILD-01A | AUDIT-02 |
| Project version | 0.1.0 | 0.6.1 |
| Confidence classes | 3 | 5 |
| Scientific evidence states | implicit/distributed | canonical 5-state registry |
| Storage CRS | EPSG:4326 | EPSG:4326 |
| Analysis CRS | implicit | explicitly project-local projected |
| Provenance | partial | expanded cross-stage contract |
| Contract versioning | absent | explicit |
| Release integrity rules | distributed | explicit baseline |

## Acceptance decision

AUDIT-02 is accepted for configuration and contract alignment.

It does **not** certify the executable platform, scientific validation, or research release.

### Gate

```text
AUDIT-02 = PASS WITH OPEN IMPLEMENTATION FINDINGS

NEXT = AUDIT-03 — IMPLEMENTATION GAP FIX
```

## Principle

No new analytical feature is to be introduced during AUDIT-03 unless an existing cross-stage contract cannot be implemented without it. The priority is to make the already-frozen architecture executable, testable and traceable.
