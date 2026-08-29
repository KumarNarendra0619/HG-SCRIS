# BUILD-01J — Hazard & Cascade Corridor Engine

## Objective
Create a reproducible hazard-corridor layer between validated drainage connectivity (BUILD-01H) and exposure (BUILD-01I).

## Important distinction
A spatial corridor is not automatically a hazard probability, risk score, or observed impact footprint. The engine therefore labels each result by model type and preserves scenario parameters.

## Current screening model
The first executable primitive is a parameterized channel buffer in a projected CRS. It is intended for rapid screening and architecture testing only.

`validated channel → width parameter → screening corridor`

## Production hazard models planned

1. GLOF / lake-outburst inundation modelling
2. Debris-flow / mass-movement routing
3. Floodplain/inundation modelling
4. Compound cascade routing (ice/rock/debris → water → sediment → channel response)
5. Event-specific reconstruction using observed evidence

## Scenario structure
Every scenario must retain:

- scenario_id
- trigger_type
- forcing class
- corridor method
- parameter set ID
- event date when applicable
- input dataset versions
- model/code version
- uncertainty/limitations

## Parameter sensitivity
Corridor width and other hazard parameters must be sensitivity-tested. A single arbitrary width must never be presented as a scientifically established impact boundary.

## Event reconstruction rule
For historical events, observed footprints/evidence must be kept separate from modelled footprints. Model calibration/validation must not use the same observations without a documented holdout strategy.

## Output classes
- `screening_corridor`
- `modelled_hazard_extent`
- `observed_event_footprint`
- `validated_hazard_extent`

Only the latter two may be presented as evidence-based event footprints, and only with appropriate provenance.

## Scientific boundary
BUILD-01J does not yet calculate discharge, flow depth, velocity, arrival time, entrainment, sediment volume, structural damage, mortality, or evacuation success. Those require specialized hazard, vulnerability, and network modules.
