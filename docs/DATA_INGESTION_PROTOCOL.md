# HG-SCRIS Data Ingestion Protocol

## BUILD-01B scope
The first ingestion implementation will establish the reproducible pipeline for glacier inventory, terrain and hydrographic connectivity. Satellite data will initially be registered as a processing source rather than copied into GitHub.

## Pipeline

1. Identify authoritative source/product and version.
2. Acquire data through an approved source/API/manual download route.
3. Record source metadata and acquisition timestamp.
4. Compute a checksum where practical.
5. Store immutable source outside GitHub when files are large.
6. Validate file integrity, CRS, extent, geometry/raster metadata and units.
7. Standardize schema and field names.
8. Create processed output with a new provenance record.
9. Run automated QA tests.
10. Promote only validated outputs to downstream analysis.

## First analytical chain

`RGI glacier → glacier geometry/attributes → DEM terrain → glacier outlet → hydrographic network → downstream path`

## Important limitation
Global datasets are reference layers, not unquestionable ground truth. Himalayan pilot/event areas will receive additional spatial QA against higher-quality regional or local evidence where available.

## Output contract
Every processed output must identify:

- source dataset ID/version
- method ID
- processing date
- software/code version
- CRS
- spatial resolution where applicable
- confidence/evidence class
- known limitations
