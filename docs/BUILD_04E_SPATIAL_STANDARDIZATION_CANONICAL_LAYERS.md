# BUILD-04E — Pilot Data Standardization, Spatial Harmonization & Canonical Master Layers

## Purpose
Convert the provenance-controlled pilot datasets from BUILD-04D into consistent, analysis-ready master layers without altering the original observations.

## Core rule
`RAW ≠ STANDARDIZED ≠ DERIVED ≠ VALIDATED`

Every transformation must be deterministic, documented and reproducible.

## Standardization pipeline

```text
RAW / INGESTED
      ↓
FORMAT + SCHEMA CHECK
      ↓
CRS / GEOMETRY / RASTER QA
      ↓
FIELD NORMALIZATION
      ↓
SPATIAL HARMONIZATION
      ↓
CANONICAL IDs
      ↓
MASTER LAYERS
      ↓
CROSS-LAYER CONSISTENCY QA
      ↓
PILOT READY
```

## Canonical master layers

### Glacier master
Minimum conceptual fields:

- glacier_id
- source_dataset_id
- geometry
- area_native / area_calculated where appropriate
- elevation attributes where available
- inventory date
- glacier/source classification
- lineage_id
- qa_status

### Lake/source master

- lake_id
- source_id
- geometry
- linked_glacier_id where defensible
- area
- elevation
- inventory/reference date
- source_dataset_id
- lineage_id
- qa_status

### Hydrography master

- reach_id
- upstream_id/downstream_id where available
- river/tributary class
- geometry
- flow-direction status
- source_dataset_id
- topology status
- lineage_id

### Settlement/exposure master

- settlement_id
- geometry
- name
- population/reference date where available
- exposure class
- source_dataset_id
- temporal status
- lineage_id
- qa_status

### Terrain master

- dem_id
- raster reference
- CRS
- pixel size
- vertical datum if known
- acquisition/reference date
- AOI
- NoData definition
- source_dataset_id
- QA status

## CRS policy

Native CRS is preserved in provenance. Working CRS is selected by analytical operation. Geographic coordinates may be retained for interchange, but metric calculations must use an appropriate projected or geodesic method.

## Raster harmonization

Do not resample merely to make datasets look aligned. Define a target grid only for an analytical operation that requires it, recording:

- target CRS
- resolution
- extent
- alignment/origin
- resampling method
- source rasters
- NoData treatment

Continuous and categorical rasters require different resampling logic.

## Vector harmonization

Standardize:

- geometry type
- CRS
- field names
- field types
- categorical domains
- multipart policy
- validity rules

Do not dissolve or simplify features unless the analytical purpose requires it and the operation is recorded.

## Canonical ID policy

IDs are stable, opaque identifiers. Do not encode mutable attributes such as names, dates or coordinates in IDs.

Identity resolution must be based on documented spatial/source matching rules. Ambiguous matches remain unresolved rather than being silently merged.

## Cross-layer consistency checks

At minimum:

- glacier/lake spatial relationship
- source/lake/outlet relationship
- hydrography connectivity
- river direction plausibility
- settlement-to-network relationship
- DEM/AOI coverage
- layer extent consistency
- duplicate canonical IDs
- temporal compatibility

## Geometry and topology

Geometry validity is a QA property, not a cosmetic repair step. Automated repairs must be deterministic and logged. Network topology must distinguish genuine disconnected features from data errors.

## Temporal harmonization

Maintain source/reference dates. Current data must not silently replace historical layers used in event reconstruction. If multiple temporal snapshots are combined, the resulting product is explicitly labelled as a derived scenario/snapshot.

## Lineage

Each canonical feature must be traceable to one or more source records and transformation steps. Derived relationships such as `glacier → lake → reach` must carry relationship provenance.

## Master-layer storage principle

The repository stores schemas, manifests, fixtures and reproducible code. Large production geospatial datasets should use the project's designated external/versioned data storage rather than bloating Git history.

## Pilot deliverables

- canonical glacier layer
- canonical lake/source layer
- canonical hydrography layer
- canonical settlement/exposure layer
- canonical terrain reference
- harmonization manifest
- cross-layer QA report
- unresolved identity/match table
- data dictionary
- pilot data freeze manifest

## Acceptance gate

BUILD-04E is complete when the selected pilot datasets are transformed into canonical, provenance-linked master layers; spatial/temporal harmonization parameters are recorded; cross-layer consistency checks are run; unresolved matches are explicitly listed; and the resulting package is ready for downstream network tracing without modifying raw source data.

## Next step
BUILD-04F — Glacier-to-River Network Construction, Connectivity QA & Downstream Trace Engine.
