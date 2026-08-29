# Terrain Engine Specification — BUILD-01E

## Objective
Derive reproducible elevation and slope information from an approved DEM and prepare glacier-to-terrain linkage for downstream hydrological routing.

## Inputs
- Standardized glacier inventory from BUILD-01D
- DEM with documented acquisition, version, resolution, vertical datum and CRS

## Outputs
For each glacier, where technically supported:
- glacier geometry
- DEM coverage status
- minimum/maximum/mean/median terrain elevation
- slope statistics
- terrain resolution metadata
- candidate outlet / routing seed
- confidence and provenance

## Slope
Slope is calculated from the DEM surface gradient and reported in degrees. The implementation must preserve DEM resolution and coordinate units; geographic-degree rasters must not be treated as metre-spaced rasters without reprojection or geodesic-aware handling.

## Outlet rule
A glacier polygon does not automatically define a hydrologically valid outlet. Production outlet extraction must be DEM-conditioned and subsequently checked against a drainage network. The geometry-only candidate function in this build is a scaffold and is not a production routing result.

## Quality gates
1. DEM CRS exists and is documented.
2. DEM has valid resolution and nodata metadata.
3. Glacier and DEM CRS are compatible after explicit transformation.
4. Glacier is sufficiently covered by the DEM.
5. Elevation units/vertical datum are documented.
6. Slope values are finite and physically plausible within the DEM domain.
7. Outlet candidates are flagged as candidates until hydrographic validation.

## Scientific caution
Elevation/slope are terrain descriptors, not hazard probabilities. A high-slope glacier or valley segment is not automatically a high-risk location. Hazard generation and downstream consequence modelling occur in later modules.
