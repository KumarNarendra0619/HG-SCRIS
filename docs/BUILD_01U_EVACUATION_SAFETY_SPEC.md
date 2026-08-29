# BUILD-01U — Evacuation & Safety Intelligence Engine

## Objective
Transform scenario-specific hazard footprints and arrival-time outputs into transparent evacuation-route and safe-zone screening results.

## Core principle
A location is not declared officially safe by this research engine. The system identifies **candidate safe zones and evacuation routes under a defined scenario**, subject to validation by competent authorities and field conditions.

## Inputs

- modelled hazard footprint
- hazard arrival time
- settlement/population exposure
- pedestrian/road network
- road/bridge status
- slope/elevation/terrain constraints
- candidate refuge/safe-zone locations
- capacity
- accessibility
- scenario ID and model version

## Evacuation workflow

`Hazard scenario → affected origins → network filtering → blocked/unsafe segments → reachable candidate zones → route optimization → travel time → capacity check → route/safe-zone screening`

## Route constraints
Routes should be evaluated using:

- hazard intersection
- bridge/road vulnerability
- slope/gradient
- network connectivity
- travel time
- road capacity where data exist
- alternative route availability
- scenario-specific closures

Shortest distance alone is not the default optimization criterion. Travel time and safety constraints take precedence where data support them.

## Safe-zone screening
Candidate safe zones should be evaluated using:

1. outside the modelled hazard footprint under the scenario
2. reachable from the origin
3. adequate capacity for assigned demand
4. acceptable travel time
5. terrain/accessibility constraints
6. proximity to emergency support where available
7. uncertainty/data-quality status

Elevation alone must not define a safe zone.

## Arrival-time logic
For each origin:

`hazard_arrival_time − evacuation_travel_time = available_response_margin`

A positive margin is a screening result, not a guarantee. Uncertainty in hazard arrival and human response time must be represented in production analysis.

## Dynamic routing
Routes should be recalculated by scenario/time slice as roads or bridges become unsafe. A single static route is insufficient for a cascading event.

## Population allocation
When population exceeds one safe zone's capacity, demand should be distributed among multiple reachable zones using an explicit allocation rule. Unassigned demand must be reported rather than silently dropped.

## Safety hierarchy

`Official warning/field instruction > validated emergency information > modelled evacuation recommendation > exploratory research visualization`

The platform is not an official emergency-warning system.

## Outputs

- evacuation route layer
- route travel time
- hazard arrival time
- response margin
- candidate safe zones
- safe-zone capacity utilization
- unserved/over-capacity population
- blocked route segments
- alternate routes
- scenario/time-step status
- uncertainty/provenance

## Validation
Historical/event reconstruction can compare modelled accessibility with observed road/bridge failures and documented evacuation paths. Field validation is required before operational use.

## Next integration
BUILD-01V will turn the validated spatial-temporal outputs into interactive 2D/3D cartography and time animation, with the underlying model values remaining inspectable rather than hidden behind visual effects.
