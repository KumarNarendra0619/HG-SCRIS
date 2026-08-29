# BUILD-03B — Glacier + Glacial Lake Data Ingestion

## Objective
Build the first real cryosphere data package for HG-SCRIS using traceable glacier and glacial-lake sources. This stage creates the master cryosphere layer; it does not yet claim a complete Himalayan hazard assessment.

## Source roles

### RGI 7.0
Use as the standardized baseline glacier inventory. RGI 7.0 is derived from GLIMS and provides glacier outlines plus attributes/hypsometry. Treat it as a snapshot-style inventory and not as a glacier-by-glacier area-change series.

### GLIMS
Use for multi-temporal glacier analyses and source-level glacier observations. Preserve GLIMS analysis/source dates and provenance because different analyses may represent different dates and data quality.

### ICIMOD regional lake inventories
Use where regional coverage/date/method are appropriate for Himalayan glacial-lake context. Record the inventory date and classification method; do not silently merge inventories from incompatible dates.

### RGI lake-terminating classification
Use as a glacier-to-lake linkage aid. It is not a replacement for independent lake polygons.

## Data model

### Glacier master entity
Required conceptual fields:

`hgscris_glacier_id, source_id, source_dataset, geometry, source_date, area_km2, min_elev_m, max_elev_m, mean_elev_m, region, basin, source_confidence, temporal_role, lineage_id, qa_status`

### Lake master entity
Required conceptual fields:

`hgscris_lake_id, source_lake_id, source_dataset, geometry, observation_date, area_km2, elevation_m, lake_type, glacier_link, outlet_link, source_confidence, temporal_role, lineage_id, qa_status`

### Link entities
Never encode relationships only in geometry. Maintain explicit crosswalks:

`glacier ↔ lake`

`lake ↔ outlet`

`glacier ↔ source_dataset`

`lake ↔ source_dataset`

## Stable identifiers

Source identifiers are preserved unchanged. HG-SCRIS adds a source-qualified identifier such as:

`RGI7:RGI60-01.00001`

This prevents collisions while preserving provenance.

## Ingestion workflow

`download → checksum/manifest → inspect → CRS check → geometry validity → duplicate check → attribute validation → normalize IDs → standardize format → write processed layer → lineage record`

## Geometry QA

Check:

- geometry validity
- empty/null geometry
- self-intersection where applicable
- duplicate features
- unexpected multipart geometry
- invalid coordinate ranges
- CRS consistency
- gross area anomalies
- overlap anomalies within the same source where they indicate possible duplication

Do not automatically delete suspicious features. Flag them for review.

## Temporal QA

Each geometry must retain its source/observation date or documented temporal range where available.

A 2000-era RGI outline may be used for baseline inventory, but must not be labelled as a 2026 outline or as a 2013 event-state outline.

## Glacier area

Area may be stored when provided or computed from a validated projected geometry. Computed area must record the processing CRS/method. Source area and computed area are separate fields when both exist.

## Elevation / mass

Elevation attributes may be sourced from the inventory or derived from an approved DEM in a later terrain-processing stage. The system must not invent glacier mass from area alone.

Mass/thickness/balance will be represented only when supported by an explicit dataset or a documented scientific model. Unknown remains null.

## Glacier–lake linkage

Link confidence levels:

- `direct_source`
- `spatially_supported`
- `inferred`
- `unknown`

A nearby lake is not automatically a lake belonging to a glacier.

## Lake outlet

Outlet linkage is deferred to the validated hydrography stage unless a source explicitly provides it. This avoids creating false connectivity from nearest-neighbour geometry.

## Output layers

1. `glacier_master`
2. `glacier_source_crosswalk`
3. `lake_master`
4. `glacier_lake_crosswalk`
5. `cryosphere_qa_flags`
6. `cryosphere_manifest`

## No-go rules

- Do not overwrite raw source data.
- Do not merge different temporal inventories into one geometry without retaining dates.
- Do not fabricate glacier mass.
- Do not infer lake ownership from distance alone.
- Do not infer downstream outlet from nearest stream alone.
- Do not classify a lake as dangerous solely from area.

## Acceptance gate
BUILD-03B is ready for the next stage when the pilot-area glacier/lake subset has source traceability, valid geometry, stable IDs, temporal metadata, QA flags and reproducible processing lineage.

## Next
BUILD-03C — DEM / Terrain Ingestion and Terrain-Derived Cryosphere Metrics.
