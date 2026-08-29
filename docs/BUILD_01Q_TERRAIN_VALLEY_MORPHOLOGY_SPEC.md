# BUILD-01Q — Terrain & Valley Morphology Engine

## Objective
Convert DEM and routed channel geometry into auditable terrain descriptors for cascade routing and hazard propagation.

## Core terrain variables
- elevation
- slope
- aspect
- curvature
- local relief
- longitudinal/channel gradient
- valley-floor geometry
- channel confinement
- drainage position

## Processing chain
`DEM → CRS/vertical-datum QC → void/nodata QC → terrain derivatives → hydrologic conditioning (if routing requires) → valley/channel sampling → morphology attributes → QC → downstream models`

## Scientific rules
1. DEM-derived drainage is a model result, not automatically ground truth.
2. Vertical datum, horizontal CRS, resolution and acquisition/source metadata must be retained.
3. Terrain derivatives must use a documented cell size and method.
4. Area/gradient calculations must use appropriate units.
5. Slope alone must never be interpreted as a direct hazard probability.
6. Valley morphology constrains possible propagation but does not by itself establish flow depth, velocity or impact.

## Valley characterization
For each routed source-to-receptor corridor, derive where data permit:
- elevation profile
- cumulative distance
- longitudinal gradient
- local slope statistics
- relief
- valley width/confinement proxies
- channel gradient
- tributary junctions
- terrain bottlenecks/expansions

## Integration
BUILD-01P supplies the network path. BUILD-01Q enriches each path segment with terrain attributes. BUILD-01R will use these attributes, together with event/process parameters, for quantitative hazard propagation.

## Outputs
- DEM derivative layers
- source-to-receptor elevation profiles
- segment slope/gradient attributes
- valley morphology table
- terrain QC report
- processing/provenance manifest

## Validation
Terrain routing and morphology must be compared against mapped hydrography, imagery and historical event footprints where available. Event-specific observations are kept separate from modelled outputs.
