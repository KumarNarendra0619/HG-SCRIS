# BUILD-01S — Exposure Intelligence Engine

## Objective
Link modelled cascade corridors to settlements, population, buildings and critical infrastructure without conflating exposure with risk.

## Exposure entities
- settlement
- population count
- building/structure
- road/bridge
- school
- health facility
- emergency facility
- utility/critical infrastructure
- other documented receptor

## Core workflow

`Cascade corridor → spatial intersection/proximity → receptor matching → exposure aggregation → scenario/time attribution → uncertainty/provenance`

## Required receptor fields

- receptor_id
- receptor_type
- geometry
- name/administrative unit where applicable
- source
- observation/reference date
- population or capacity where applicable
- vulnerability fields only when sourced and explicitly defined

## Exposure metrics

For each source/scenario/corridor:

- exposed settlements
- exposed population
- exposed buildings
- exposed roads/bridges
- exposed schools/health/emergency facilities
- exposed critical infrastructure
- distance to corridor
- modelled arrival time when available
- scenario identifier

## Spatial methods

Preferred methods depend on geometry:

- polygon intersection for inundation/debris footprints
- line intersection for roads/rivers
- point-in-polygon for facilities
- population-weighted raster zonal statistics where population grids are available
- proximity only as a screening metric when no footprint is available

A proximity buffer must never be labelled as inundation or impact extent.

## Time dimension
Exposure records retain scenario and arrival-time information. A receptor may be exposed under one scenario and not another.

## Exposure vs vulnerability vs risk

`Exposure` answers what is physically located in a modelled hazard area/pathway.

`Vulnerability` describes susceptibility/loss given a hazard.

`Risk` requires hazard, exposure and vulnerability, with probability or scenario weighting where appropriate.

The engine therefore does not generate a risk score merely from population density or distance.

## Uncertainty
Every exposure result should carry:

- hazard scenario ID
- corridor/model version
- receptor data source/date
- spatial method
- positional/data uncertainty where available
- validation status

## Historical event reconstruction
For an observed event, observed damage/impact footprints must be stored separately from modelled exposure. Agreement/disagreement is a validation result, not something to be hidden by forcing the model to match observations.

## Outputs

- source-to-receptor exposure table
- scenario-wise exposure statistics
- settlement exposure layer
- infrastructure exposure layer
- arrival-time table
- exposure uncertainty/provenance report

## Next integration
BUILD-01T will combine hazard intensity, exposure and vulnerability into a transparent risk/impact framework with scenario-specific outputs.
