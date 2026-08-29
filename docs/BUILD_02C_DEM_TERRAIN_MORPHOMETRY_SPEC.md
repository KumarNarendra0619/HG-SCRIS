# BUILD-02C — DEM/Terrain Baseline & Valley Morphometry

## Objective
Establish a scientifically controlled terrain baseline for elevation, slope, flow routing and valley morphology. These products support—but do not by themselves determine—hazard propagation.

## DEM baseline
Each DEM must retain:

- canonical DEM ID
- source/product
- acquisition/reference date
- horizontal CRS
- vertical datum
- resolution
- extent
- NoData definition
- processing version
- conditioning status
- QA status
- source URL
- lineage ID

## DEM QA
Before terrain derivatives:

1. verify CRS
2. verify vertical datum or explicitly mark unknown
3. inspect resolution and pixel alignment
4. inspect NoData/voids
5. check tile seams
6. identify artefacts/spikes/sinks
7. document mosaicking/resampling
8. preserve original and processed versions

Do not silently mix DEMs with different vertical references or resolutions.

## Terrain derivatives
Generate, where appropriate:

- elevation
- slope
- aspect
- curvature
- local relief
- flow direction
- flow accumulation
- drainage area
- channel gradient
- valley floor / low-relief corridors
- terrain ruggedness

Derived layers must carry DEM ID, processing version and parameter metadata.

## Hydrological conditioning
Hydro-conditioning may be used for drainage extraction, but the conditioned DEM must remain separate from the original terrain surface. Conditioning parameters must be documented because they can alter flow routing.

## Valley morphometry
For each downstream corridor, calculate available geometric indicators such as:

- longitudinal elevation profile
- channel/valley gradient
- valley width
- channel width where mapped
- relative relief
- confinement ratio
- slope distribution
- junction locations

### Confinement ratio
A screening ratio can be defined as:

`channel width / valley width`

It is a geometric descriptor, not a direct prediction of flood/debris-flow hazard.

## Glacier-centric terrain corridor
For a selected glacier:

`Glacier outlet → flow direction → drainage network → longitudinal profile → valley morphology → settlements`

This corridor becomes a common spatial reference for later cascade modelling.

## Flow-routing caution
DEM-derived flow paths must be checked against mapped hydrography. Automated routing can fail in flat areas, braided channels, glaciers, lakes and terrain with DEM artefacts.

## Multi-resolution principle
Use analysis resolution appropriate to the process and data quality. Do not claim metre-scale hazard precision from coarse DEMs or coarse event observations.

## 2D/3D preparation
Generate separate analysis and visualization products where necessary:

- full-resolution analysis raster
- optimized visualization terrain
- generalized vector display layer
- full-resolution export layer

Visualization simplification must never replace the analytical source.

## Outputs

- DEM master registry
- terrain derivatives
- hydrologically conditioned derivative set
- longitudinal profiles
- valley morphometry table
- glacier-to-terrain corridor products
- QA report
- processing/provenance manifest

## Acceptance gate
Terrain enters downstream modelling only when CRS, vertical reference, resolution, NoData and processing lineage are documented and QA status is acceptable.

## Next step
BUILD-02D — Hydrography, Glacier-to-River Connectivity & Downstream Flow Network.
