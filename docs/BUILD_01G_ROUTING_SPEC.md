# BUILD-01G — DEM Flow Routing + G2S Network Engine

## Objective
Move HG-SCRIS from proximity-based river matching to explicit DEM-derived drainage routing and a directed downstream graph.

## Implemented primitives

1. **D8 flow direction** — each valid DEM cell selects the neighbour with the steepest positive downhill gradient.
2. **D8 flow accumulation** — unit-cell contributing area is propagated through the directed drainage graph.
3. **Routing graph** — DEM cells become directed graph nodes/edges pointing downstream.
4. **Downstream traversal** — a start cell can be followed to an outlet.

## Production workflow

`DEM → conditioning → flow direction → accumulation → stream threshold → drainage network → glacier outlet seed → graph traversal → downstream river/water body`

## Conditioning is explicit

BUILD-01G does **not** silently fill or breach depressions. DEM conditioning can materially alter Himalayan valley routing, especially around glaciers, lakes, dams, terraces and steep terrain. The conditioning method must therefore be selected, documented and validated before production use.

## Stream extraction

A flow-accumulation threshold is not a universal constant. It must be parameterized and sensitivity-tested by terrain, DEM resolution and study objective. The production system will retain the threshold used for every result.

## Glacier connection

A glacier polygon is converted to a DEM/routing seed only after DEM coverage and CRS checks. Candidate outlets remain candidates until the routed path is checked against independent hydrography.

## Scientific interpretation

The routing engine establishes **potential surface drainage connectivity**, not flood discharge, inundation depth, travel time or hazard probability. Those require additional hydraulic/hazard models and event-specific forcing.

## QA requirements

- detect nodata and disconnected DEM regions
- check graph cycles
- document conditioning
- preserve DEM resolution and CRS
- sensitivity-test stream thresholds
- compare routed drainage with independent hydrography
- assign connectivity confidence
