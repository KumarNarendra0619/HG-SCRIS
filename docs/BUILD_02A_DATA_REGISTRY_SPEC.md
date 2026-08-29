# BUILD-02A — Data Registry & Provenance Loader

## Objective
Create the single source-of-truth metadata layer for HG-SCRIS datasets before any scientific modelling begins.

## Registry rule
No dataset is considered analysis-ready merely because it downloaded successfully. Identity, spatial reference, temporal reference, resolution, licence and QA status must be recorded first.

## Required registry fields

`dataset_id, theme, provider, product_or_dataset, spatial_coverage, temporal_coverage, resolution, crs, vertical_datum, access_url, license, acquisition_date, processing_version, qa_status, notes`

## Initial thematic registry

- glacier inventory
- DEM / terrain
- hydrography: rivers, streams, tributaries, lakes
- settlements
- population
- roads/bridges
- schools/health/emergency facilities
- other critical infrastructure
- historical event evidence
- satellite/remote-sensing products
- observed damage/impact evidence

## Provenance chain

`Source → Download/Access → Raw ID → QA → Processing → Derived ID → Model → Visualization`

Every derived dataset must retain its parent dataset IDs and processing version.

## QA gates

### Identity QA
Confirm product name, provider, version and acquisition/reference date.

### Spatial QA
Confirm geometry/raster validity, CRS, extent, resolution and alignment.

### Vertical QA
For DEM/terrain products, record vertical datum or explicitly mark it unknown until verified.

### Temporal QA
Record observation/acquisition date and event time where relevant.

### Completeness QA
Check missing attributes, NoData, empty geometries and duplicate identifiers.

### Licence QA
Record usage/licensing restrictions before public deployment.

### Reproducibility QA
Record software, processing script/version and parameters for derived products.

## Status vocabulary

- `not_started`
- `pending`
- `passed`
- `failed`

A failed dataset cannot silently enter the production modelling pipeline.

## Repository policy

Do not commit large raw DEM, satellite or vector archives. Keep registry metadata, schemas, small fixtures and reproducible processing code in GitHub. Use documented external access/storage for large datasets.

## Google Colab workflow

1. Read registry
2. Select dataset IDs
3. Download/access source
4. Compute file/structure diagnostics
5. Validate CRS/datum/resolution/date
6. Produce QA report
7. Write processed artifact
8. Update provenance
9. Register output dataset ID
10. Pass artifact to modelling pipeline

## AI-assisted development rule
Gemini/AI Studio may generate or refactor code, but generated code must pass tests and data QA. Dataset metadata and scientific assumptions require researcher verification.

## BUILD-02A acceptance criteria

- registry schema committed
- initial thematic records created
- validator implemented
- QA status vocabulary fixed
- provenance chain documented
- large-data repository policy documented
- Colab ingestion workflow defined

## Next step
BUILD-02B — Verified Glacier Inventory & Glacier-State Baseline Loader.
