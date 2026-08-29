# BUILD-04B — Real-Data Contract & Pilot Ingestion

## Purpose
Move HG-SCRIS from specification-only assets toward a controlled real-data pipeline. BUILD-04B defines the canonical data contract and pilot-ingestion gate without fabricating missing observations.

## Repository audit baseline
The repository already contains configuration, data manifests/schemas, multiple production package domains, tests, and a pilot acceptance module. The current project configuration still reports BUILD-01A and EPSG:4326 as the working CRS, so version/stage metadata must be updated only when the corresponding implementation is actually released.

## Canonical data lifecycle

`EXTERNAL SOURCE → RAW REFERENCE → INGESTED → QA → STANDARDIZED → DERIVED → VALIDATED → PUBLISHED`

Raw source files are immutable references. Derived products must retain lineage to their source dataset and processing run.

## Canonical entity identifiers

- glacier_id
- lake_id
- source_id
- catchment_id
- reach_id
- tributary_id
- event_id
- scenario_id
- settlement_id
- exposure_id
- evacuation_origin_id
- safe_zone_id

IDs are stable within the project namespace and must not encode mutable attributes.

## Mandatory provenance
Every ingested/derived dataset must record:

- dataset_id
- dataset_version
- source_name
- source_url/catalogue reference where available
- access/download date
- spatial coverage
- temporal coverage
- CRS
- original resolution/scale
- processing method_id
- parameter_set
- processing date
- code version
- QA status
- confidence/uncertainty
- licence/usage constraint

## Spatial contract

- Store original CRS metadata.
- Transform to analysis CRS only through an explicit, logged step.
- Do not use EPSG:4326 for distance/area/slope calculations unless the operation is explicitly geodesic and appropriate.
- Preserve geometry validity and dimensionality.
- Record source resolution/scale.

## Core pilot datasets

Priority order:

1. glacier inventory
2. glacial lake inventory
3. DEM
4. hydrography/network
5. settlement/exposure
6. historical event evidence
7. event/hazard reconstruction inputs
8. evacuation network

## Ingestion gate
A dataset enters `INGESTED` only after:

- source identity is recorded
- file/endpoint is accessible
- format is recognized
- CRS is identified
- geometry/table schema is readable
- required identifier fields are mapped
- licence/usage status is recorded

## QA gate
Required checks include:

### Tabular
- required columns
- type consistency
- null rates
- duplicate IDs
- range checks
- date validity
- categorical domain checks

### Vector
- CRS
- geometry validity
- empty geometries
- duplicate features
- multipart/geometry-type consistency
- self-intersection where relevant
- spatial extent sanity
- topology checks where network data are involved

### Raster
- CRS
- pixel size
- nodata
- extent
- data type
- value-range sanity
- alignment where products are combined

## Pilot selection rule
The first real pilot must have:

- a clearly documented glacier/source
- a defensible downstream hydrographic connection
- at least one settlement/exposure dataset
- event evidence sufficient for reconstruction, OR a clearly defined scenario basis
- data licence permitting the intended research use

The pilot is a validation vehicle, not evidence that the same model is valid everywhere in the Himalaya.

## No-data policy
Missing data are represented explicitly as `MISSING`, `NOT_AVAILABLE`, `NOT_APPLICABLE`, or `NOT_VALIDATED`. Never substitute invented values merely to complete a map.

## Release states

`RAW_REFERENCE`
`INGESTED`
`QA_PASSED`
`STANDARDIZED`
`DERIVED`
`VALIDATED`
`PUBLISHED`

## Required pilot outputs

- pilot data manifest
- standardized glacier layer
- standardized lake/source layer
- DEM metadata record
- hydrography network subset
- settlement/exposure subset
- evidence/event subset
- QA report
- lineage manifest

## Engineering rule
Large external datasets should not be committed blindly into GitHub. GitHub stores code, schemas, manifests, small fixtures and reproducibility metadata; large rasters/vector archives use appropriate external/versioned storage with stable references.

## Acceptance gate
BUILD-04B passes only when one pilot dataset family has completed the ingestion and QA gates with reproducible metadata and no fabricated observations. The pilot may remain `NOT_VALIDATED` until scientific validation is completed.

## Next step
BUILD-04C — Automated Ingestion + QA Notebook and Production Data Validators.
