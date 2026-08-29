# BUILD-02E — Settlement, Population & Critical Infrastructure Exposure Baseline

## Objective
Create a provenance-aware receptor/exposure layer so that downstream hazard corridors can be intersected with people, settlements, buildings, transport and critical facilities.

## Core principle
Exposure is not risk. A settlement inside a geometric downstream corridor is an exposed receptor candidate; actual risk requires a defined hazard intensity/probability model plus vulnerability/consequence assumptions.

## Exposure classes

- settlements
- population
- buildings
- roads
- bridges
- schools
- health facilities
- emergency facilities
- tourism facilities
- critical infrastructure

## Population rule
Do not assign a population value merely because a settlement polygon exists. Population must retain its source and reference year. Spatial redistribution from census units or gridded products must record the allocation method and uncertainty.

## Temporal consistency
For event reconstruction, exposure should be time-matched as far as possible:

`event date → settlement state → population year → infrastructure state`

A present-day settlement layer must not automatically be presented as historical exposure.

## Geometry and source QA
For each exposure layer:

1. validate geometry
2. check duplicates
3. check CRS
4. record observation/reference date
5. record source/version
6. inspect missing identifiers
7. preserve original source identifiers
8. record processing lineage

## Glacier-centric exposure linkage
For each glacier/event scenario:

`validated downstream network → hazard corridor candidate → intersect exposure → aggregate by settlement/reach/admin unit`

The linkage should preserve the route/reach through which an exposure is connected, rather than only recording straight-line distance.

## Screening proximity
A geometric corridor-distance function may be used for preliminary screening when coordinates are in an appropriate projected CRS. Distance bands must be explicitly defined by the scenario/research design and must not be labelled as flood/debris-flow risk thresholds without physical justification.

## Exposure metrics
Where data permit, calculate:

- exposed settlement count
- exposed population
- exposed building count
- exposed road/bridge length/count
- exposed school/health/emergency facility count
- exposed tourism/critical-infrastructure count
- exposure by downstream reach
- exposure by administrative unit
- uncertainty/data-quality coverage

## Network-aware aggregation
A settlement may connect to more than one reach or branch. Avoid double counting by assigning a canonical exposure-event relationship and retaining all relevant reach IDs where multi-connectivity is real.

## Evacuation preparation
Build a separate network-ready asset table for:

- roads
- bridges
- access points
- candidate safe locations
- schools/community buildings where appropriate
- emergency facilities

These are inputs to the later evacuation/safety model, not evacuation orders.

## Safety language
The application must distinguish:

- `EXPOSURE SCREENING`
- `MODELLED HAZARD`
- `RISK SCREENING`
- `EVACUATION SCENARIO`
- `OBSERVED IMPACT`

Never display an exposure intersection as a confirmed future impact.

## Outputs

- exposure master layer
- population/reference-year table
- critical-facility layer
- network-aware exposure relationships
- exposure aggregation tables
- QA report
- provenance manifest
- evacuation-ready asset layer

## Acceptance gate
Exposure becomes production-ready only when source, date/year, geometry, identifiers and QA status are documented. Population and asset counts must retain their temporal reference and uncertainty.

## Next step
BUILD-02F — Historical Himalayan Event Catalogue & Evidence Matrix.
