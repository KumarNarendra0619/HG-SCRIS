# BUILD-04C — Automated Ingestion + QA Engine

## Status
LOCKED — implementation baseline

## Purpose
Establish a deterministic gate between external data and HG-SCRIS analytical processing. The engine validates source existence, schema, identifiers, domains and metadata before data are promoted to processed/analytical status.

## Non-negotiable rule
QA may flag an error, quarantine a dataset, or produce a controlled normalization. It must not silently invent, overwrite or impute scientific observations.

## Pipeline

`SOURCE → INGEST → DETECT → VALIDATE → QA REPORT → QUARANTINE/PASS → STANDARDIZE → MANIFEST`

## QA classes

### File/source
- source exists
- readable format
- expected file type
- non-zero size
- declared source/version present

### Tabular
- required columns
- datatype compatibility
- null/blank checks for key fields
- unique canonical IDs
- allowed domain values
- date parsing
- numeric range checks

### Vector
- geometry type
- valid geometry
- empty geometry
- CRS presence
- extent plausibility
- duplicate feature IDs
- multipart handling status

### Raster
- CRS
- dimensions
- transform/pixel size
- NoData metadata
- numeric range
- expected band count
- alignment/extent metadata

### Metadata/provenance
- dataset_id
- version
- source
- access date
- spatial/temporal coverage
- CRS/resolution
- licence
- method/processing information where applicable

## QA result states

`PASS`

`FAIL`

`WARN`

`QUARANTINED`

A WARN cannot be silently converted to PASS by the pipeline.

## Controlled normalization

Normalization may include deterministic operations such as:

- field-name canonicalization
- CRS transformation when explicitly configured
- datatype casting when lossless
- standardized date representation
- whitespace normalization
- controlled category mapping

Every transformation must be logged in the lineage manifest.

## Quarantine

Failed datasets are retained as source references but excluded from downstream analytical products until reviewed/reprocessed.

## Output contract

Each ingestion run produces:

- QA report
- normalized output reference if applicable
- source manifest
- processing timestamp
- code/version identifier
- status

## Initial implementation

`src/hgscris/ingestion/qa_engine.py` contains small deterministic primitives for required columns, unique IDs, allowed domains, source existence and machine-readable QA reporting. Larger geospatial validators should be added only with corresponding tests and fixture data.

## Test policy

Every validator must have positive and negative fixtures. Tests must verify that invalid data fail rather than being silently repaired.

## Promotion rule

`RAW → INGESTED` requires successful source/format checks.

`INGESTED → STANDARDIZED` requires schema and normalization checks.

`STANDARDIZED → ANALYTICAL` requires all mandatory QA checks to PASS or an explicitly documented exception.

## Acceptance gate

BUILD-04C is complete for the pilot when at least one real source passes through the ingestion contract, produces a machine-readable QA report and provenance manifest, and invalid fixture data are correctly rejected/quarantined by automated tests.

## Next step
BUILD-04D — Real Pilot Dataset Selection, Acquisition & Provenance Registration.
