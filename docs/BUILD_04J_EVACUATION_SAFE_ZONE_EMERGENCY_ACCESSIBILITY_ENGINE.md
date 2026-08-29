# BUILD-04J — Evacuation, Safe-Zone & Emergency Accessibility Engine

## Purpose
Convert time-dependent hazard and exposure information into reproducible evacuation demand, safe-zone suitability and emergency accessibility analysis. This is a decision-support layer; it must not present a route as safe merely because it is geometrically shortest.

## Core chain

```text
HAZARD ARRIVAL / INTENSITY
        +
POPULATION / EXPOSURE
        +
ROAD + TRAIL + BRIDGE NETWORK
        +
NETWORK CAPACITY / CONDITION
        +
HAZARD-INDUCED BLOCKAGES
        ↓
EVACUATION DEMAND
        ↓
SAFE-ZONE CANDIDATES
        ↓
ROUTE FEASIBILITY
        ↓
TRAVEL / CLEARANCE TIME
        ↓
BOTTLENECKS + ISOLATION
        ↓
PRIMARY + ALTERNATIVE EVACUATION PLAN
```

## Scientific boundary
A route is not classified as safe solely from distance or network connectivity. Safety requires explicit consideration of hazard timing, route exposure, crossings, capacity, terrain/access constraints and scenario assumptions. A safe-zone candidate is not automatically an approved emergency shelter.

## Inputs

- BUILD-04F directed hydrography/network graph
- BUILD-04H hazard extent, arrival time and intensity where available
- BUILD-04I population and exposure layers
- roads/trails/bridges and critical infrastructure
- elevation/slope/terrain constraints where relevant
- known shelters/open spaces/assembly points where available
- administrative boundaries and operational constraints

## Evacuation demand
For each settlement/exposure unit derive, where data support it:

- exposed population
- evacuation population
- mobility/accessibility constraints
- origin location
- required clearance time
- demand scenario

Do not infer individual vulnerability from coarse population data. Aggregate only to a defensible spatial unit.

## Safe-zone candidate model
Candidate areas may include verified shelters, designated assembly areas or analytically screened open/high-ground locations. Candidate screening can consider:

- outside the modelled hazard footprint for the scenario
- adequate elevation/terrain separation where relevant
- sufficient usable area
- road/trail accessibility
- distance/travel time from origins
- secondary hazard exposure
- capacity
- proximity to critical services
- potential isolation by bridge/road failure

Analytical candidates must be labelled `CANDIDATE`, not `OFFICIAL_SHELTER`, unless supported by an authoritative source.

## Route model
Represent evacuation as a time-dependent network:

- node = settlement, junction, bridge, shelter/assembly point or other relevant point
- edge = road/trail/route segment
- attributes = length, estimated travel time, surface/class, capacity where available, hazard status, closure status, provenance

## Time-dependent routing
A route must be evaluated against hazard arrival time:

```text
route clearance time < hazard arrival time
```

where sufficient timing data exist. Include a safety buffer as an explicit scenario parameter rather than hiding it inside travel time.

If arrival time is unknown, route status must not be reported as definitively safe.

## Hazard-induced network failure
Model scenario-dependent failures such as:

- bridge closure/failure
- road inundation
- debris blockage
- landslide blockage
- channel crossing loss
- network isolation

Each closure must have provenance and scenario association. Do not delete the original road network; maintain a scenario-specific network state.

## Accessibility metrics
Where data permit calculate:

- shortest travel distance
- estimated travel time
- time to nearest feasible safe-zone
- number of feasible routes
- route redundancy
- population isolated
- critical bottlenecks
- bridge dependence
- network service loss

## Multi-route planning
For each origin, identify:

1. primary feasible route
2. alternative route(s)
3. route failure condition
4. estimated travel/clearance time
5. bottleneck(s)

Do not force an alternative where none exists; return `NO_FEASIBLE_ALTERNATIVE`.

## Capacity and congestion
Where capacity data exist, incorporate them explicitly. A shortest-path result must not be interpreted as an evacuation-time estimate when congestion or capacity constraints are ignored.

Where capacity is unavailable, clearly label travel time as an uncongested/network estimate.

## Safe-zone capacity
For a candidate safe zone, track:

- usable area/capacity source
- estimated demand
- capacity ratio
- accessibility
- hazard status
- secondary hazard status
- official/designated status

Do not invent shelter capacity.

## Isolation analysis
A settlement is potentially isolated when all feasible connections to a relevant safe-zone/service network are unavailable under a scenario. Record:

- failed links
- remaining links
- isolation time/state
- affected population
- scenario_id

## Scenario framework
Support at minimum:

- baseline network
- hazard-only closures
- compound hazard closures
- bridge failure scenario
- road blockage scenario
- conservative/high-impact scenario where justified

Scenario results must never overwrite the baseline network.

## Uncertainty
Route status should distinguish:

- `FEASIBLE`
- `CONDITIONALLY_FEASIBLE`
- `UNCERTAIN`
- `BLOCKED`
- `ISOLATED`
- `NO_FEASIBLE_ROUTE`

Travel times and safe-zone suitability inherit uncertainty from hazard arrival, network condition, terrain and capacity assumptions.

## Emergency decision outputs
For each settlement:

- evacuation demand
- primary route
- alternative route
- nearest feasible safe zone
- estimated travel time
- hazard arrival time
- available time margin
- bottleneck
- isolation risk/status
- route confidence/status

## Time margin
Where both quantities are available:

`time_margin = hazard_arrival_time − estimated_clearance/travel_time`

A positive margin does not by itself guarantee successful evacuation; it is a decision-support metric subject to uncertainty and operational constraints.

## Place-by-place emergency profile
Example structure:

```text
SETTLEMENT A
  ↓
Hazard arrival: T+35 min
  ↓
Population exposed: N
  ↓
Primary route: R01 → R04 → SZ01
  ↓
Travel estimate: 18 min
  ↓
Time margin: 17 min
  ↓
Bridge B01: critical dependency
  ↓
Alternative: R07 → SZ02
  ↓
Status: CONDITIONALLY_FEASIBLE
```

## Validation
Where historical evacuation information exists, compare reconstructed/modelled route states against:

- observed road/bridge closures
- observed evacuation routes
- documented safe locations
- observed isolation
- event timelines

Do not validate solely by comparing map appearance.

## Reproducibility
Every evacuation result must retain:

- hazard version
- network version
- population/exposure version
- safe-zone dataset version
- routing method
- travel-speed assumptions
- capacity assumptions
- closure rules
- safety-buffer parameter
- scenario_id
- code/model version
- run_id

## Output tables

- evacuation_demand
- safe_zone_candidates
- evacuation_routes
- route_alternatives
- network_failures
- isolation_results
- bottlenecks
- emergency_place_profiles
- evacuation_run_manifest

## UI principle
The public interface should show actionable status without false precision:

`Route status → arrival time → estimated travel time → time margin → alternative → key blockage`

Research mode should expose assumptions, parameters, source versions and uncertainty.

## Acceptance gate
BUILD-04J is operationally complete when a pilot scenario can reproducibly identify exposed population, screen and classify safe-zone candidates, construct a scenario-aware evacuation network, calculate feasible/blocked routes with documented assumptions, identify bottlenecks and isolation, and return place-by-place emergency profiles with provenance and uncertainty.

## Next step
BUILD-04K — 2D/3D Spatio-Temporal Visualization, Event Replay & Cascade Animation Engine.
