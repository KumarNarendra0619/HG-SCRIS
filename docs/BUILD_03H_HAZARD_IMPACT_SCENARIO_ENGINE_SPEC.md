# BUILD-03H — Hazard & Impact Scenario Engine

## Objective
Create a process-specific scenario framework that converts validated cryosphere, terrain, hydrography, forcing and event evidence into reproducible hazard/impact scenarios. The engine must never equate downstream connectivity with hazard extent.

## Process families

1. GLOF / lake-breach flood
2. fluvial flood
3. debris flow
4. landslide runout and channel interaction
5. avalanche
6. icefall / ice-debris cascade
7. compound cascades

## Architecture

`source/trigger → process model → propagation/runout → terrain/network interaction → hazard footprint → intensity/time metrics → exposure overlay → impact → validation → uncertainty`

## Process-specific rule

No single universal model or threshold will be applied to all Himalayan hazards. Each process requires its own physical assumptions, parameters, calibration/validation strategy and limitations.

## Three evidence states

- OBSERVED_HAZARD: mapped/recorded event evidence supports the footprint
- MODELLED_SCENARIO: a documented model generated the scenario
- UNVALIDATED_SCENARIO: exploratory result not yet suitable for authoritative interpretation

## Scenario inputs

Required references may include:

- glacier/lake state
- event/trigger evidence
- DEM and terrain derivatives
- hydrography network
- precipitation/temperature/snow/hydrology forcing
- source volume/area where defensible
- process parameters
- exposure snapshot

## GLOF workflow

`lake/source characterization → breach/source hypothesis → outflow hydrograph or justified source representation → hydraulic routing → terrain/channel interaction → downstream extent/depth/velocity/arrival time → validation`

Do not infer breach discharge from lake area alone without an explicit empirical/physical relationship and uncertainty.

## Fluvial flood workflow

`forcing/discharge → hydraulic/hydrologic model → channel/floodplain routing → depth/velocity/extent → observed validation`

Where discharge is unavailable, scenario assumptions must be explicit; rainfall cannot silently be converted into discharge without a documented model.

## Debris-flow workflow

`source initiation → entrainment/volume assumptions → channel routing/runout → deposition/impact footprint → validation`

A simple DEM-derived flow path is not equivalent to debris-flow runout.

## Landslide workflow

`source identification → volume/material assumptions → slope/runout model → channel interaction if applicable → downstream propagation → validation`

Susceptibility maps must not be labelled as event runout maps.

## Avalanche / icefall workflow

`source zone → release scenario → terrain-constrained runout → valley interaction → exposure intersection → validation`

Use process-specific source and mobility assumptions.

## Compound cascade

Represent as a directed graph:

`trigger A → process B → interaction C → process D → downstream impact`

Each node and edge stores evidence/model basis, timing, uncertainty and lineage.

## Intensity outputs

Where supported by the selected process model:

- inundation/runout extent
- depth
- velocity
- discharge/outflow
- arrival time
- duration
- deposition/runout thickness
- flow energy or other process-specific intensity

Only metrics actually supported by the model are populated.

## Uncertainty

Scenario outputs must retain uncertainty from:

- source characterization
- DEM/resolution
- forcing
- model parameters
- boundary conditions
- process assumptions
- exposure date mismatch

Prefer scenario ensembles/ranges over a single false-precision footprint when uncertainty is material.

## Validation hierarchy

Where possible:

`historical observed footprint → hindcast → parameter evaluation → independent event validation → scenario use`

Validation data must not be reused as if independent validation.

## Impact integration

Impact is a separate analytical stage:

`hazard intensity + exposed asset + vulnerability/consequence function → impact`

Exposure alone is not impact. A building inside a footprint does not automatically imply total loss.

## Evacuation separation

Evacuation/safe-zone analysis is not part of hazard generation. It will use validated hazard outputs plus route/network/accessibility constraints in a later stage.

## 2D visualization

Support toggles for:

- source
- trigger
- modelled corridor
- hazard extent
- intensity
- arrival time
- observed footprint
- exposed assets
- impact
- uncertainty

Never visually merge observed and modelled footprints without a clear legend/state.

## 3D visualization

Render terrain, source, channel, valley and hazard surface/volume. Vertical exaggeration is display metadata only.

## Time animation

Animation states must be tied to model time steps or documented event timestamps:

`T0 source → T1 release → T2 propagation → T3 confluence → T4 settlement exposure → T5 recession/deposition`

Do not animate arbitrary movement solely because two places are network-connected.

## Reproducibility

Every scenario stores:

- scenario ID
- process
- model/version
- input IDs
- parameter-set ID
- spatial/temporal configuration
- boundary conditions
- output references
- validation status
- uncertainty reference
- lineage

## Acceptance gate

BUILD-03H is complete for a pilot when at least one process-specific model pathway is executable from registered inputs to a traceable output, with explicit assumptions, validation hooks and observed/modelled separation. A framework-only map is not considered a validated hazard model.

## Next step
BUILD-03I — Vulnerability, Consequence, Risk & Impact Scoring Engine.
