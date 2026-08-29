# HG-SCRIS Data Governance

## Purpose
Define how external geospatial data enter, move through, and leave the HG-SCRIS analytical system.

## Immutable source principle
Raw source data are never edited in place. Any transformation creates a new processing stage and records its provenance.

## Lifecycle

`SOURCE → RAW → INTERIM → PROCESSED → DERIVED → RESULT`

## Required metadata
Every dataset used in analysis must record:

- dataset_id
- dataset_name
- provider
- product/version
- source URL or DOI
- license/usage terms
- acquisition date
- temporal coverage
- spatial extent
- spatial resolution
- CRS
- units
- processing method
- source checksum where practical
- limitations
- citation

## Quality gates
A dataset cannot enter production analysis until identity, CRS, geometry/raster integrity, units, temporal suitability, spatial coverage and missing-data conditions have been checked.

## GitHub storage rule
Large external datasets are not committed to GitHub. The repository stores metadata, code, configuration, lightweight samples and reproducible acquisition/processing instructions.

## Scientific distinction
Observed, published/modelled, derived-estimate and scenario-assumed values must never be silently mixed. Each variable must retain a provenance/evidence class.
