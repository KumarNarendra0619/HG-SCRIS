# AUDIT-03 — Implementation Gap Fix

## Status
PARTIALLY CLOSED — CORE GAPS PATCHED; REAL-DATA CERTIFICATION PENDING

## Scope
AUDIT-03 closes the implementation gaps identified by the all-stage BUILD audit without adding a new scientific module.

## Fixes applied

### 1. Ingestion QA
`src/hgscris/ingestion/qa_engine.py` now provides deterministic checks for:
- required schema fields;
- complete/unique identifiers;
- domain values;
- source existence;
- CRS declaration;
- core dataset provenance;
- geometry type declaration;
- spatial support/resolution metadata.

The engine remains validation-only and does not silently repair or infer scientific data.

### 2. Scientific visualization state
`LayerSpec` now requires an explicit scientific state:
- OBSERVED
- INFERRED
- MODELLED
- SCENARIO
- UNCERTAIN

Non-observed layers require a source/version reference. This prevents visual output from silently presenting inferred or modelled information as observed fact.

### 3. Evacuation safety primitives
Routing now supports:
- blocked-node constraints;
- maximum travel-time constraints;
- deterministic tie-breaking;
- explicit hazard-arrival time;
- response delay;
- temporal safety margin;
- explicit `None` when temporal hazard timing is unavailable.

The implementation does not invent hazard-arrival times.

## Remaining gaps

The following are intentionally not declared closed by AUDIT-03:

1. Full geospatial binary validation for all raster/vector formats.
2. Complete scenario-aware evacuation network engine with capacities and dynamic closures.
3. Real Himalayan event vertical-slice execution.
4. Independent validation of the real pilot.
5. Full 06A–06E population with certified pilot outputs.
6. Formal reconciliation of the historical BUILD-03M transition in the stage ledger.

## Acceptance status

| Area | Status |
|---|---|
| QA metadata primitives | PASS |
| Scientific visualization states | PASS |
| Basic evacuation temporal safety | PASS |
| Silent inference prevention | PASS |
| Real-data E2E execution | PENDING |
| Independent validation | PENDING |
| Research-ready certification | BLOCKED |

## Next gate

`AUDIT-04 — Synthetic End-to-End Integration Test`

AUDIT-04 must exercise the actual repository modules as one deterministic chain before a real Himalayan event is used for certification.
