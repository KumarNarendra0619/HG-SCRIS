# BUILD-01W — HG-SCRIS Working Research Platform

## Objective
Integrate the HG-SCRIS analytical chain into a deployable web research interface while keeping computation, visualization, provenance and safety communication separate.

## Product boundary
HG-SCRIS is a research and scenario-analysis platform. It is not an official emergency warning, forecast or evacuation-order system.

## Architecture

`Data → QA → Analysis → Scenario → API/Artifacts → Web UI → Map/3D → Animation → Export`

### Research compute layer
Python in Google Colab/local environments performs heavy processing, model calibration, raster/vector analysis and batch runs.

### Repository layer
GitHub stores source code, configuration, schemas, documentation, tests and versioned lightweight example data. Large raw datasets should remain external or in an appropriate data store; the repository stores provenance and download/access instructions.

### Application layer
The web application reads analysis-ready artifacts and exposes controlled scenario/viewer operations. The browser should not run heavyweight scientific processing.

## Main application sections

### 1. Home / Research Dashboard
- project overview
- study region
- data/model version
- methodology summary
- event catalogue

### 2. Glacier Explorer
- glacier inventory
- lake/outlet information
- elevation/mass attributes where available
- source/provenance
- select glacier → downstream trace

### 3. Cascade Explorer
- trigger
- glacier/lake
- stream
- tributary
- river
- downstream settlements
- exposure
- scenario

### 4. Risk & Impact
- hazard intensity
- exposure
- vulnerability
- scenario risk
- impact dimensions
- uncertainty

### 5. Evacuation & Safety
- affected origins
- candidate safe zones
- route status
- travel time
- response margin
- capacity
- blocked/alternative routes

### 6. 2D Map
- scientific layer control
- time slider
- scenario selector
- glacier-centric trace
- observed/modelled toggle
- inspection/provenance panel

### 7. 3D Terrain
- DEM terrain
- glacier/lake/hydrography
- hazard footprint
- settlements/infrastructure
- camera controls
- optional explicit vertical exaggeration

### 8. Event Reconstruction
- observed evidence
- modelled reconstruction
- temporal sequence
- validation comparison

### 9. Data / Methods / Provenance
- datasets
- processing methods
- model assumptions
- versions
- uncertainty
- citations/links

### 10. Export
- GeoJSON/GeoPackage-ready vector outputs where supported
- CSV tables
- raster outputs where supported
- figures/animation metadata
- reproducibility manifest

## State model

Every analysis/view should be defined by:

`project_id + data_version + model_version + scenario_id + CRS + DEM_version + timestamp/frame`

The platform must be able to reconstruct what the user was viewing.

## Safety UX
Use explicit labels:

- OBSERVED
- MODELLED
- SCENARIO
- UNCERTAINTY
- RESEARCH SCREENING

Do not use language implying official warning status.

## Deployment strategy

### Phase A — Local/Colab validation
Run all scientific modules and example cases.

### Phase B — GitHub integration
Run automated tests and package validation on every change.

### Phase C — Static/analysis-ready web deployment
Serve lightweight frontend assets and precomputed analysis artifacts.

### Phase D — Dynamic API if required
Add a small API only when interactive server-side querying cannot be handled from static artifacts.

## Performance rules

- precompute expensive raster analysis
- tile large spatial layers
- simplify display geometries separately from analytical geometries
- lazy-load 3D terrain
- cache scenario states
- keep full-resolution data available for export/analysis

## Minimum viable working site

The first working release must support:

1. choose study/event
2. choose glacier
3. trace downstream pathway
4. choose scenario
5. view 2D hazard/exposure
6. inspect arrival time
7. view candidate evacuation routes/safe zones
8. switch to 3D terrain
9. play/pause time animation
10. inspect provenance
11. export analysis result

## Scientific QA gate before public release

- data provenance complete
- CRS/datum validated
- model assumptions visible
- observed vs modelled separated
- uncertainty represented
- historical event validation completed for pilot cases
- no uncalibrated risk thresholds presented as authoritative
- evacuation outputs clearly labelled as research screening

## October build target
The October target should be a working research-grade site for a bounded pilot region and selected historical events first. Global Himalayan coverage is a data-engineering and validation expansion, not a prerequisite for a scientifically credible MVP.

## Next step
After BUILD-01W, implementation should move from architecture to integration sprints: real datasets, pilot events, application UI, automated tests, deployment and validation.
