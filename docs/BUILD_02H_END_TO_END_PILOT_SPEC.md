# BUILD-02H — End-to-End Scientific Pilot

## Purpose
Prove that the HG-SCRIS architecture can execute one complete, reproducible event workflow from source data through reconstruction, exposure analysis, validation and visualization before scaling to the full Himalayan domain.

## Pilot philosophy
Do not build the whole Himalaya first. A single well-documented pilot event is the integration test for the scientific pipeline. The pilot event must be selected after evidence screening and data availability assessment.

## Full pipeline

`source registry → glacier baseline → DEM/terrain → hydrography → event evidence → event reconstruction → exposure → validation → 2D outputs → 3D outputs → animation package → reproducibility manifest`

## Pilot selection criteria
Score candidate events on:

- quality of event timing/location evidence
- identifiable source glacier/lake/process
- suitable DEM availability
- hydrography quality
- observed footprint availability
- exposure data availability
- independent validation evidence
- relevance to Himalayan cascade processes

Do not select an event merely because it is famous or recent.

## Pilot stages

### P0 — Freeze pilot definition
Record event, study area, research question, model level and acceptance criteria.

### P1 — Data ingestion
Register every source and preserve original references.

### P2 — Glacier/lake source reconstruction
Link candidate source features with confidence and alternatives.

### P3 — Terrain processing
Prepare DEM, slope, flow routing and valley morphology with full provenance.

### P4 — Hydrography graph
Validate outlet, stream, tributary and downstream reach relationships.

### P5 — Event evidence reconstruction
Build claim-level evidence matrix and separate observed/inferred information.

### P6 — Scenario generation
Run only models whose input requirements and applicability are satisfied.

### P7 — Exposure intersection
Map settlements, population and critical infrastructure against scenario pathways.

### P8 — Validation
Compare model/reconstruction against independent observed evidence where available.

### P9 — 2D visualization
Produce research map layers with source, status, uncertainty and timestamp metadata.

### P10 — 3D visualization
Create terrain-based scene using a visualization-optimized surface while preserving analytical data separately.

### P11 — Temporal animation
Animate evidence/model states in chronological sequence. Observed, inferred and modelled states must remain distinguishable.

### P12 — Reproducibility package
Export manifest, input references, processing versions, parameters, outputs and QA results.

## Minimum pilot outputs

1. glacier/source map
2. DEM/terrain products
3. hydrography network
4. reconstructed event pathway
5. observed footprint
6. modelled scenario footprint if justified
7. exposure map/table
8. validation report
9. 2D web-ready layers
10. 3D scene-ready layers
11. animation-ready timeline
12. provenance/reproducibility manifest

## Acceptance gates
Pilot is `READY` only if:

- all required datasets are present
- provenance/lineage is complete
- QA gates pass
- the chosen model is applicable to the process
- validation evidence is identified
- limitations are documented

If observed validation evidence is unavailable, the pilot may still run as a **screening demonstration**, but it must not be presented as a validated reconstruction.

## Website integration
The pilot becomes the reference implementation for the future web application. UI should expose:

`Event → Source → Terrain → Network → Scenario → Exposure → Validation → 2D → 3D → Animation`

Each output should provide provenance and uncertainty metadata.

## Engineering principle
Python processing should be notebook/script based and reproducible in Google Colab. The production web interface can be built separately through the GitHub-backed application stack. Do not put heavy scientific computation into the browser.

## October delivery strategy
The pilot is the integration milestone. Once it passes, scale the same validated pipeline to additional events and eventually the Himalayan domain. Do not expand domain coverage before the pilot exposes and resolves data/model/visualization failures.

## Next phase
After BUILD-02H, proceed to implementation tracks for real data ingestion, process-specific modelling, web UI, 2D/3D visualization, animation, QA automation and deployment.
