# BUILD-03G — Settlement, Population & Infrastructure Exposure Integration

## Objective
Build a temporally explicit, source-traceable exposure layer linking settlements and critical infrastructure to the validated downstream hydrographic network and later hazard scenarios.

## Core principle
Exposure is not risk. A settlement connected to a downstream network is a potential exposure candidate. It becomes scenario-affected only after a documented hazard/process model or observed event footprint supports that conclusion.

## Exposure entities

- settlement
- population
- building footprint where available
- road
- bridge
- school
- health facility
- emergency facility
- administrative facility
- utility/water infrastructure
- tourism infrastructure
- agriculture/livelihood assets where data quality permits
- other critical infrastructure

## Master exposure schema

Each entity must retain:

- HG-SCRIS exposure ID
- original source ID
- source dataset/provider
- geometry
- feature type
- name/locality
- administrative unit
- observation/reference date
- population value and reference date where applicable
- source resolution/scale where applicable
- network connectivity status
- nearest/linked reach ID
- network distance
- elevation/terrain reference where available
- data quality status
- lineage

## Settlement representation

Do not treat a settlement centroid as its complete spatial extent. Where building footprints or settlement polygons exist, preserve them. A centroid may be used as a fallback for screening and must be labelled accordingly.

## Population temporal rule

Population values are time-stamped. A current population estimate must not silently be used as historical event exposure. Where historical population is unavailable, the mismatch is recorded as uncertainty rather than hidden.

## Network linkage

Preferred relationship:

`settlement/asset → spatial/network linkage → validated reach → downstream source`

Linkage types:

- directly intersecting
- hydraulically/network connected candidate
- proximity-screened
- inferred
- unknown

Spatial proximity alone is not hydraulic connectivity.

## Exposure states

`BASELINE_EXPOSURE`

`NETWORK_CONNECTED`

`OBSERVED_EVENT_AFFECTED`

`MODEL_SCENARIO_AFFECTED`

`UNCERTAIN`

These states must remain separate in database and visualization.

## Critical infrastructure

Infrastructure receives functional importance attributes where defensible. Do not assign arbitrary weights without a documented method. A hospital, bridge, road, school and water facility have different failure consequences and may require different impact models.

## Exposure metrics

Candidate metrics include:

- population potentially connected downstream
- number/type of infrastructure assets
- network distance from source
- elevation difference
- settlement/building density where available
- accessibility constraints where available
- criticality class
- observed damage count/extent for historical events

These are exposure descriptors, not risk scores.

## Historical-event integration

For a reconstructed event:

`observed footprint + exposure baseline at/near event date → observed affected exposure`

If the event-date exposure baseline is unavailable, the result must be marked temporally mismatched.

## Future scenario integration

For scenario modelling:

`hazard/process footprint + exposure snapshot → scenario exposure`

Avoid calling this a prediction unless the underlying hazard model has been validated for the relevant process and spatial scale.

## QA

Check:

- geometry validity
- duplicate features
- source ID integrity
- temporal metadata
- population plausibility
- missing values
- administrative consistency
- network linkage consistency
- coordinate/CRS validity
- conflicting source records

## Privacy and aggregation

Public-facing maps should avoid unnecessary personally identifiable information. Population should generally be aggregated to appropriate spatial units unless a legitimate, documented research need requires finer representation.

## Outputs

`settlement_master`

`population_reference`

`infrastructure_master`

`exposure_network_links`

`exposure_baseline`

`historical_affected_exposure`

`scenario_exposure`

`exposure_qa`

`exposure_manifest`

## 2D visualization

Layers should support:

- settlements
- population classes
- infrastructure categories
- connected downstream network
- observed event footprint
- modelled scenario footprint
- evacuation/safety layers later

## 3D visualization

Expose settlements and critical assets on terrain with optional elevation-aware symbols. Vertical exaggeration is visualization metadata only.

## Acceptance gate

BUILD-03G is complete for a pilot when settlement and infrastructure sources are registered, temporally qualified, geometrically QA'd, linked to the hydrographic network where defensible, and separated into baseline/observed/modelled exposure states.

## Next step
BUILD-03H — Hazard/Impact Scenario Engine: process-specific inundation, debris-flow, GLOF and cascade modelling framework.
