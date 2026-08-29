# BUILD-03C — DEM & Terrain Ingestion Specification

## Objective
Create a reproducible terrain foundation for HG-SCRIS from a documented DEM, then derive terrain metrics required for glacier context, hydrological connectivity, valley characterization and later process-based modelling.

## Core principle
A DEM is an analytical input, not a hazard model. Elevation/slope alone must never be presented as a flood, debris-flow or evacuation boundary.

## Data flow

`DEM source → download → integrity check → CRS/datum audit → spatial subset → void/artefact QA → standardized raster → terrain derivatives → QA → manifest`

## Required source metadata

Every DEM must record:

- dataset/product
- provider
- version
- acquisition/reference date where available
- spatial resolution/cell size
- vertical datum/reference
- horizontal CRS
- vertical units
- coverage
- licence/terms
- source URL
- download date
- processing version
- lineage ID

## Terrain derivatives

Primary derivatives:

1. elevation
2. slope
3. aspect
4. local relief
5. curvature where appropriate
6. flow direction
7. flow accumulation
8. drainage extraction inputs
9. valley/longitudinal profiles
10. glacier/lake terrain statistics

Flow-direction and accumulation products are analytical intermediates. They are not themselves proof of an observed flood pathway.

## Hydrologic conditioning

If the DEM is used for flow routing, the conditioning method must be explicit. Do not silently fill all depressions because genuine glacial lakes and closed terrain depressions can be meaningful features. Conditioning should be applied only where justified for the routing task and with the original DEM preserved.

## Resolution rule

Do not resample a DEM merely to make the map look smoother. Analytical resolution must be documented. If a process model requires finer terrain than the selected DEM can represent, the limitation must be reported rather than hidden by interpolation.

## Terrain metrics for glacier/lake

For each glacier and lake, calculate where supported:

- minimum/maximum/mean elevation
- elevation range
- mean slope
- slope distribution
- aspect distribution
- local relief
- surrounding terrain characteristics

These are descriptive/contextual metrics unless subsequently incorporated into a validated process model.

## Valley analysis

For downstream risk analysis, derive terrain context along validated hydrography:

`reach → upstream elevation → downstream elevation → longitudinal gradient → local slope/relief → valley context`

Valley slope must not be substituted for channel slope without explicitly defining the measurement.

## DEM QA

### Technical QA

- file readable
- raster dimensions valid
- CRS present
- units present
- nodata defined
- pixel size consistent
- extent valid
- unexpected gaps identified
- extreme-value scan

### Scientific QA

- resolution appropriate for intended use
- temporal suitability documented
- vertical datum compatible
- mountainous terrain limitations documented
- known artefacts/voids documented

## Outputs

`dem_master`

`elevation_cog`

`slope_cog`

`aspect_cog`

`relief_cog`

`flow_direction_cog`

`flow_accumulation_cog`

`terrain_statistics`

`terrain_qa`

`terrain_manifest`

## Web/analysis separation

Keep analytical rasters separate from web-optimized visualization tiles. Browser visualization may use a display-optimized derivative; scientific calculations must reference the declared analytical raster.

## Reproducibility

Google Colab notebooks/scripts must read the source manifest, process deterministic inputs, write outputs and update lineage metadata. The raw DEM is immutable.

## Acceptance gate

BUILD-03C is complete for a pilot only when the selected DEM has passed technical and scientific QA, terrain derivatives are reproducibly generated, and every derivative can be traced to the exact DEM/version and processing configuration.

## Next step
BUILD-03D — Hydrography, River–Tributary Network & Downstream Connectivity.
