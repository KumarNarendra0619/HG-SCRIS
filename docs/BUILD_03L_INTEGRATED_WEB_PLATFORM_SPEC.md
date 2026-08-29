# BUILD-03L — Integrated HG-SCRIS Web Platform

## Objective
Turn the validated HG-SCRIS research pipeline into a working, research-grade web application. The web client presents precomputed/validated analytical products; it does not silently run unvalidated hazard models or alter scientific classifications.

## Master user flow

`Home → Himalaya Explorer → Glacier Search/Select → Glacier Profile → Downstream Trace → Event Reconstruction → Hazard Scenario → Exposure → Impact/Risk → Evacuation/Safety → 2D/3D/Animation → Export/Research Report`

## Application modules

### 1. Home / Research Overview
- project purpose
- methodology overview
- data/source policy
- coverage status
- observed/modelled distinction
- limitations and disclaimer

### 2. Himalaya Explorer
- regional map
- glacier/lake inventory
- hydrography
- administrative context
- progressive loading
- search and filters

### 3. Glacier Profile
- glacier ID
- location
- elevation/mass/state attributes where available
- linked lake/source
- catchment/outlet
- connected downstream network
- evidence and lineage

### 4. Event Explorer
- event list
- date/time
- event type
- evidence status
- reconstructed timeline
- observed/inferred/modelled classification

### 5. Cascade Trace
Primary action:

`Select glacier/source → trace outlet → downstream reaches → settlements/assets → hazard scenario → impact → evacuation`

All relationships must be ID-backed and reproducible.

### 6. Scenario Explorer
- hazard/process selector
- scenario metadata
- parameter set
- model version
- extent/intensity
- arrival time where supported
- uncertainty
- validation status

### 7. Exposure / Impact / Risk
- population
- infrastructure
- hazard overlap
- vulnerability components
- observed impact
- modelled impact
- scenario risk components
- uncertainty

### 8. Evacuation / Safety
- evacuation origins
- route network
- blocked segments
- safe-zone candidates
- validation status
- route alternatives
- travel-time estimates
- bottlenecks

### 9. 2D / 3D / Animation
Consume BUILD-03K manifests and preserve all provenance states.

### 10. Research / Export
- event report
- scenario report
- map export
- data export where permitted
- animation export where feasible
- reproducibility manifest

## Data architecture

Use a clear separation:

`RAW/EXTERNAL SOURCES → INGESTED → QA → PROCESSED → ANALYTICAL PRODUCT → WEB/API CACHE`

The application must never overwrite raw evidence.

## Web/API principle

The browser should request indexed, versioned analytical products through a lightweight data/API layer. Heavy raster/vector processing and model execution remain offline/batch workflows in Python/Google Colab or scheduled compute.

## Suggested implementation architecture

```text
Python / Colab
      ↓
ETL + QA + Modelling
      ↓
GeoParquet / COG / vector tiles / manifests
      ↓
GitHub-controlled project + data services
      ↓
Web/API layer
      ↓
2D Map + 3D Scene + Animation UI
```

For the pilot, static/versioned assets and a lightweight API are preferred over premature microservices.

## Front-end principles

- map-first but not map-only
- glacier-centric search
- one-click downstream trace
- clear status badges
- source/lineage available from every analytical result
- mobile-friendly 2D core
- desktop-first detailed 3D
- no scientifically misleading color-only encoding

## State labels

Every major analytical result should expose:

`OBSERVED | INFERRED | MODELLED | SCENARIO | UNCERTAIN`

## Query model

Primary query keys:

- region_id
- glacier_id
- lake_id
- reach_id
- event_id
- scenario_id
- settlement_id
- exposure_id
- time_index

Avoid free-text spatial joins at runtime for core trace operations.

## Security

- no secrets in frontend or repository
- environment variables for API keys
- server-side access to protected services
- input validation
- rate limiting where API is exposed
- dependency pinning
- GitHub Actions checks
- audit logs for administrative/data-management operations

## Scientific reproducibility

Every published result page must expose or link to:

- dataset versions
- processing version
- model/scenario version
- analysis date
- reference date
- methodology
- limitations

## Performance strategy

- vector tiles for large vector layers
- Cloud Optimized GeoTIFF / tiled rasters where appropriate
- level-of-detail 3D
- lazy loading
- feature clustering/generalization at small scales
- cached scenario products
- precomputed animation frames/states where necessary

## No-code/AI-assisted development workflow

The project can be developed using Google Colab for Python processing, Gemini-assisted coding/review, and AI Studio for application prototyping. Every generated change must still pass repository tests, data QA and scientific review before becoming a release artifact.

## Deployment target

Initial target: a working public web application connected to the GitHub-controlled HG-SCRIS project. Production deployment should use versioned builds and a separate data/configuration layer where dataset size exceeds repository suitability.

## Acceptance gate

BUILD-03L pilot is complete when a user can select at least one glacier/event and reproducibly navigate through downstream network, exposure, hazard, impact/risk and evacuation outputs in a working web interface; the 2D view works end-to-end; 3D and time animation work for the pilot scenario; provenance/status is visible; and the deployment is reproducible from the repository.

## Next step
BUILD-03M — Data Ingestion, Automated QA/ETL & All-Himalaya Scaling Pipeline.
