# BUILD-01I — Settlement & Infrastructure Exposure Engine

## Objective
Translate validated downstream drainage corridors into a reproducible screening of settlements and infrastructure potentially intersecting the modeled corridor.

## Chain

`Glacier → outlet → routed drainage → validated hydrography → candidate hazard corridor → settlement/infrastructure intersection → exposure metrics`

## Exposure is not risk
A settlement intersecting a modeled corridor is **exposed**; this does not mean it will be damaged. Risk requires hazard intensity/probability plus vulnerability and consequence information, which are later modules.

## Settlement schema (minimum)

- settlement_id
- name
- geometry
- population (with year/source)
- administrative units
- evidence/provenance

## Infrastructure schema (minimum)

- infrastructure_id
- type
- geometry
- operational/status information where available
- evidence/provenance

## Spatial screening
Corridor intersections are performed only after CRS alignment. Point, line and polygon infrastructure are retained as distinct geometry types because their exposure interpretation differs.

## Population rule
Population must retain reference year, source and spatial support. Summing population across overlapping source polygons without de-duplication is prohibited.

## Outputs
- exposed settlement inventory
- exposed infrastructure inventory
- population exposed where defensible
- infrastructure counts by type
- distance-to-channel/corridor diagnostics
- source and method provenance
- exposure confidence

## Planned next layer
BUILD-01J will establish hazard intensity/corridor modelling and vulnerability-aware risk scoring. Evacuation and safe-zone analysis must use network accessibility and terrain constraints, not simple Euclidean distance.
