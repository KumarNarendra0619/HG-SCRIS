# BUILD-03A — Scientific Data Source Registry

## Status
LOCKED — source registry baseline created 2026-08-29.

## Purpose
Establish a traceable source-of-truth registry before real data ingestion. A dataset is not production-approved merely because it is open or technically downloadable.

## Source-selection rules

1. Prefer authoritative institutional datasets for the primary variable.
2. Record exact product/version, not only the provider name.
3. Record temporal coverage and acquisition/snapshot date separately where applicable.
4. Record spatial resolution and CRS/vertical-reference information.
5. Record access and licence/terms before redistribution.
6. Preserve raw source references and never overwrite raw data.
7. Maintain a fallback source, but do not silently substitute it.
8. Mark scientific limitations explicitly.
9. Use multiple datasets where one cannot support the required inference.
10. Validate source suitability against the event date and process type.

## Baseline source families

### Glacier inventory
- GLIMS Glacier Database: primary multi-temporal glacier-outline evidence.
- Randolph Glacier Inventory v7: standardized global glacier inventory and hypsometry baseline.

RGI v7 is a snapshot-style inventory and should not be used alone to calculate glacier-by-glacier area-change rates.

### Terrain
- Copernicus DEM GLO-30: primary terrain baseline where access and terms permit.
- HydroSHEDS terrain products: hydrologic/terrain fallback and network-support dataset.

### Hydrography
- HydroSHEDS flow direction, accumulation and related products for continental-scale network screening.
- National/local authoritative hydrography should supersede generic global products where available and appropriate.

### Climate
- ERA5: meteorological/reanalysis context and event forcing analysis.
- Local station/gauge observations should be preferred for validation/calibration where available.

### Surface water
- JRC Global Surface Water: historical surface-water context and water-body change screening.
- Event-specific optical/SAR imagery should be used for mapped event footprints where required.

## Dataset suitability classes

`PRIMARY` — suitable as a principal analytical source after QA.

`SUPPORTING` — useful for contextual or cross-check analysis.

`FALLBACK` — used only when primary data are unavailable or unsuitable, with explicit documentation.

`PROVISIONAL` — source registered but access/version/fitness still requires verification.

## Critical temporal rule

A current dataset must not automatically be used to represent a historical event state. The registry records temporal mismatch as a limitation and the event pipeline must carry that limitation forward.

## Critical spatial rule

Nominal resolution is not equivalent to effective accuracy. Terrain, glacier outline, hydrography and exposure datasets require dataset-specific uncertainty/accuracy assessment.

## No-data principle

Missing data are represented as missing/unknown. They must not be silently replaced by an unrelated dataset.

## Registry acceptance gate

A source becomes ingestion-ready only after:

- source URL/reference verified
- exact product/version identified
- access method identified
- format identified
- spatial/temporal coverage recorded
- licence/terms recorded
- scientific use defined
- limitations recorded
- fallback identified

## Current baseline

The initial registry contains source families for cryosphere, terrain, hydrography, climate and historical surface-water context. Event-specific evidence and exposure sources will be expanded in BUILD-03F–03H after the pilot event and study area are frozen.

## Next

BUILD-03B — Glacier and Glacial-Lake Data Ingestion.
