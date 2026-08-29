# Hydrology Engine Specification — BUILD-01F

## Objective
Establish the hydrological connectivity layer required by the G2S Cascade Engine: glacier/source → candidate outlet → drainage network → tributary → river → downstream water body.

## Core principle
Nearest-line matching is only a spatial seed. It is **not** evidence that water flows from a glacier into that line. Production connectivity requires a downstream-directed network derived from authoritative hydrography and/or a validated DEM flow model.

## Processing chain

`Glacier → DEM-conditioned outlet → flow direction → flow accumulation → drainage network → network topology → downstream traversal`

## Required attributes
A production river network should provide, where available:

- stable feature ID
- basin/catchment ID
- stream order
- upstream/downstream topology
- source/product/version
- geometry
- direction evidence

## Connectivity confidence
Each glacier-to-water-body connection will receive an evidence class:

- **C3 — Strong:** DEM routing and independent hydrography agree.
- **C2 — Moderate:** one validated routing source supports connectivity with no major contradiction.
- **C1 — Weak:** spatial proximity/partial evidence only.
- **C0 — Unresolved:** connectivity cannot be established.

C1/C0 links must not be presented as confirmed downstream flow paths.

## Current implementation boundary
BUILD-01F provides network validation and nearest-river seed primitives. It deliberately does not infer downstream direction from arbitrary line geometry. DEM-conditioned flow direction, accumulation and graph traversal are promoted to the next hydrology build after the data products and vertical/planimetric assumptions are fixed.
