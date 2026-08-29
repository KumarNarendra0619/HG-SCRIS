# BUILD-01Q — Terrain & Valley Morphology Engine

## Objective
Convert DEM and routed network information into reproducible terrain descriptors that constrain, rather than falsely determine, downstream cascade propagation.

## Inputs
- analysis-ready DEM
- glacier/lake/outlet geometries
- routed stream/tributary/river network
- CRS, vertical datum and cell size metadata

## Core terrain variables
- elevation
- slope
- aspect
- curvature
- local relief
- channel/longitudinal gradient
- valley width and confinement
- cross-sectional terrain descriptors where data permit
- terrain bottlenecks and valley expansions

## Processing chain

`DEM QA → datum/CRS check → conditioning policy → terrain derivatives → drainage profile → valley morphology → network enrichment → QC`

DEM conditioning must be explicit. The original DEM is never overwritten.

## Implemented deterministic primitives

The current package provides:

- slope in degrees from a regular DEM grid
- local relief using a configurable odd-sized neighbourhood
- longitudinal gradient from upstream/downstream elevation and distance

These are descriptive terrain metrics. They are not hazard probabilities.

## Valley morphology
Production valley morphology should be derived along the connectivity network rather than from arbitrary map-wide thresholds. For each routed segment, calculate terrain width/confinement and longitudinal profile using documented cross-sections or terrain windows. Store method, window/section parameters and resolution.

## Hydrologic conditioning
Where routing depends on a DEM, conditioning may include sink handling, breach/fill policy, stream burning where justified, and flow-direction/accumulation derivation. The chosen method must be recorded because conditioning can alter drainage pathways.

## Quality control

- DEM CRS and vertical datum verified
- horizontal resolution retained
- vertical units retained
- NoData checked
- slope/range diagnostics
- anomalous gradients flagged
- routed network compared with mapped hydrography
- terrain metrics retain source DEM version

## Scientific boundary
Terrain morphology constrains potential propagation. It does not by itself provide discharge, flow depth, velocity, sediment concentration, probability or risk.

## Output
Each network segment can receive a terrain-enriched record:

`segment_id + distance + elevation + slope + gradient + relief + valley morphology + DEM provenance`

## Next stage
BUILD-01R uses these terrain-enriched pathways to run scenario-based quantitative water/debris propagation. Process models must remain distinguishable from screening heuristics and must expose assumptions and uncertainty.
