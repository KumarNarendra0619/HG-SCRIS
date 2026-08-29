# BUILD-01N — Remote-Sensing Data Engine

## Objective
Establish a source-controlled data-adapter and QC layer for glacier, lake and terrain observations. Heavy raster processing can run in Google Colab; the repository stores code, schemas, manifests and reproducibility metadata rather than large raw scenes.

## Data families

1. Optical satellite imagery — glacier/lake surface mapping and temporal change.
2. DEM products — elevation, slope, aspect, drainage and terrain derivatives.
3. Glacier inventories — stable glacier IDs, outlines and reference attributes.
4. Glacial-lake inventories — lake IDs, outlines, elevation and temporal attributes.
5. Hydrography — streams, rivers, tributaries and water bodies.
6. Ancillary observations — event reports, field evidence and other documented sources.

Specific products, dates, spatial resolution and licenses must be selected per study region and variable; no product is treated as universally superior.

## Scene metadata contract
Each scene records:

- scene ID
- acquisition date
- product family
- cloud fraction when available
- source/provider
- processing level
- asset URI or stable reference

## Processing principle

`Catalog → AOI filter → date filter → cloud/quality filter → reprojection/resampling where justified → masking → derived product → QC → analysis-ready asset`

The original source is never overwritten. Processing parameters and software version must be recorded.

## DEM preparation
DEM conditioning, hydrologic enforcement, resolution choice and vertical reference must be documented before routing. DEM-derived drainage is treated as a model result and independently compared with hydrography (BUILD-01H).

## Glacier/lake extraction
Extraction methods may include manual/semiautomatic interpretation, spectral indices, segmentation or ML. The method, training/validation data, threshold and accuracy metrics must be stored. Automated extraction is never accepted as ground truth by default.

## Temporal consistency
Observations from different dates/products must retain date and source metadata. Change metrics are computed only after geometry/measurement comparability is checked.

## QC minimum

- CRS and spatial reference
- dimensions/resolution
- finite-data fraction
- valid range
- nodata handling
- acquisition date
- source/product identity
- processing level
- uncertainty/accuracy where available

## Cloud and seasonal bias
Cloud filtering alone is insufficient for glacier/lake change analysis. Seasonal timing, snow cover, shadows, debris cover and sensor differences can produce apparent change. Comparison windows therefore require explicit temporal rules.

## Reproducible storage strategy

GitHub:
- Python package
- notebooks/scripts
- schemas
- manifests
- parameter files
- tests
- documentation

Google Colab:
- heavy downloads
- raster processing
- model execution
- intermediate analysis

Object/cloud storage or external data portals:
- large rasters/scenes
- derived tiles
- event-specific outputs

Raw data should not be committed to GitHub unless licensing and repository size make that appropriate.

## Planned outputs

- analysis-ready glacier inventory
- analysis-ready lake inventory
- temporal observation table
- DEM derivatives
- scene manifest
- QC report
- provenance manifest
- data-version identifiers

## Scientific boundary
BUILD-01N establishes reliable data ingestion and QC. It does not claim glacier/lake extraction accuracy until the selected datasets and validation samples are actually evaluated.
