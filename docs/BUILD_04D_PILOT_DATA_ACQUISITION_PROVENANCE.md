# BUILD-04D — Pilot Data Acquisition & Provenance

## Purpose
Establish a defensible first Himalayan pilot data package for HG-SCRIS. This stage defines acquisition and provenance; it does not claim that any dataset is automatically scientifically fit for every downstream model.

## Pilot principle
Start with one event/glacier system that has sufficient evidence to demonstrate the complete chain. Prefer data that are openly accessible, versioned, spatially compatible and legally reusable.

## Required data groups

1. Glacier inventory and geometry
2. Glacial lake/source inventory and geometry
3. DEM/terrain
4. River and tributary network
5. Settlements/population/exposure
6. Historical event evidence
7. Infrastructure relevant to exposure/evacuation
8. Optional climate, snow, hydrology and satellite evidence needed by the selected event model

## Candidate source classes

Use authoritative or well-documented sources first, then established scientific repositories, then open geospatial datasets where appropriate. Record the exact source rather than relying on a generic provider name.

Potential source classes include national agencies, scientific mission archives, peer-reviewed event datasets, Copernicus/ESA products, NASA/USGS products, OpenStreetMap for appropriate infrastructure/network features, and openly licensed global glacier/hydrology datasets.

The exact source selected for each variable must be recorded in the registry with licence and access information.

## Acquisition record

Every dataset gets a record containing:

- dataset_id
- dataset_name
- thematic_class
- provider
- canonical_source_url
- access_date
- publication/version date
- licence
- spatial_coverage
- temporal_coverage
- native_CRS
- native_resolution_or_scale
- file_format
- download/reference identifier
- checksum when available
- intended_use
- limitations
- processing_method_id
- QA status
- provenance status

## Data classes

`RAW_REFERENCE` — source as obtained or externally referenced.

`INGESTED` — copied/loaded into the controlled pipeline.

`STANDARDIZED` — deterministic format/CRS/schema normalization applied.

`DERIVED` — generated from one or more source datasets.

`VALIDATED` — passed the applicable QA and scientific validation gate.

`PUBLISHED` — released for application use.

## Spatial policy

Keep native data untouched. Reprojection is performed only on a working copy. Computational CRS is selected according to operation and geographic extent; EPSG:4326 is not treated as a universal metric CRS.

## Temporal policy

Record both source/reference date and processing date. Historical event reconstruction must use exposure/environment snapshots appropriate to the event where available. Current exposure must not silently replace historical exposure.

## Evidence hierarchy

For historical event reconstruction, record evidence type and strength separately. Examples:

- direct observation/official report
- satellite observation
- instrumented measurement
- peer-reviewed reconstruction
- mapped geomorphic evidence
- indirect/inferred evidence

Do not convert evidence strength into an arbitrary numerical score without a documented method.

## Pilot selection gate

A candidate pilot is accepted only when:

- glacier/source can be identified
- drainage relationship can be established
- relevant terrain data exist
- downstream network can be constructed
- settlement/exposure information exists at a usable level
- event evidence is sufficient for reconstruction
- source/licence is documented
- known limitations are recorded

## Acquisition workflow

`Discover → Register → Acquire/Reference → Check licence → Record metadata → Check checksum → Ingest → Run BUILD-04C QA → Quarantine failures → Standardize → Freeze manifest`

## No fabrication rule

If a required dataset cannot be obtained or validated, mark it `MISSING`, `NOT_AVAILABLE`, `NOT_VALIDATED`, or `NOT_APPLICABLE` as appropriate. Do not substitute a convenient dataset without recording the methodological consequence.

## Deliverables

- pilot data registry
- source/provenance manifest
- acquisition checklist
- licence register
- spatial/temporal compatibility report
- BUILD-04C QA report
- pilot readiness decision

## Acceptance gate

BUILD-04D is complete when one pilot event/glacier system has a documented, licensed, provenance-complete data package and all ingested components have passed or been explicitly quarantined by the BUILD-04C QA process. This is a data-readiness gate, not a hazard-model validation claim.

## Next step
BUILD-04E — Pilot Data Standardization, Spatial Harmonization & Canonical Master Layers.
