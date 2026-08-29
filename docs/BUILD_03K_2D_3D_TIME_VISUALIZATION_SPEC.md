# BUILD-03K — Scientific 2D/3D Visualization & Time Animation Engine

## Objective
Create the visualization layer that renders HG-SCRIS analytical outputs without changing their scientific meaning. The interface must distinguish observed, inferred, modelled, scenario and uncertain information.

## Design principle
Visualization is an analytical presentation layer, not a modelling layer. Styling, animation or 3D exaggeration must never alter the underlying measurements or classifications.

## Core interaction

`Region → Glacier → Source/Lake → Trigger → Cascade → Hydrography → Hazard → Exposure → Impact/Risk → Evacuation/Safety`

The user should be able to select a glacier/source and trace the downstream system place-by-place.

## 2D map architecture

Base layers:

- administrative geography
- terrain/hillshade where appropriate
- glacier inventory
- glacial lakes
- rivers/tributaries
- settlements
- infrastructure

Analytical overlays:

- event evidence
- reconstructed pathway
- hazard footprint
- hazard intensity
- exposure
- vulnerability
- observed impact
- modelled impact
- risk components
- evacuation routes
- safe-zone candidates
- uncertainty

## Layer-state rule

Every analytical feature should carry a state such as:

`OBSERVED`

`INFERRED`

`MODELLED`

`SCENARIO`

`UNCERTAIN`

The UI must not visually imply that modelled or inferred features are observed facts.

## Glacier-centric trace

Primary interaction:

`select glacier → show source/lake → show outlet → highlight connected reaches → show downstream settlements → show hazard/impact scenario → show evacuation options`

The trace must be reproducible from stored IDs, not from ad-hoc spatial clicks.

## Place-by-place panel

For a selected downstream place, show:

- place ID/name
- linked reach
- network distance from source
- elevation context
- hazard scenario
- hazard intensity where available
- exposure
- impact state
- evacuation origin
- candidate/validated safe zone
- uncertainty
- evidence/lineage references

## 3D architecture

3D scene components:

`terrain + glacier + lake + river network + hazard surface/volume + settlements + infrastructure + evacuation routes`

3D vertical exaggeration must be explicitly labelled and must not modify analytical values.

## 3D performance principle

Use level-of-detail, tiled/vector/raster pyramids and progressive loading for regional views. Detailed 3D scenes should load only after a user selects a smaller area/event.

## Time animation

Animation states are derived from event/model timestamps or explicit scenario time steps.

Example:

`T0 source → T1 release → T2 propagation → T3 confluence → T4 settlement exposure → T5 impact → T6 evacuation`

If timing is simulated, label it `SCENARIO TIME`; never present it as observed event time.

## Animation controls

Minimum controls:

- play/pause
- timeline scrubber
- playback speed
- event/scenario selector
- layer visibility
- current timestamp/time-step
- reset

## Animation data contract

Each frame/state should reference:

- scenario/event ID
- time index
- geometry/feature IDs
- state
- source/model lineage
- intensity fields where applicable

Avoid generating separate uncontrolled copies of the same geometry for every frame.

## Scientific cartography

Maps must support:

- scale
- north orientation
- legend
- units
- data timestamp/reference date
- scenario label
- source/lineage access
- uncertainty/status indication

Colour ramps must be consistent with variable semantics and accessible to colour-vision-deficient users.

## Uncertainty visualization

Uncertainty should be represented explicitly through appropriate visual variables such as opacity, hatching, boundary style or dedicated uncertainty layers. Do not hide uncertainty solely in metadata.

## Interaction safety

Clicking a modelled hazard polygon must not make it appear as an observed footprint. Tooltips and legends must preserve provenance state.

## Export

Support, subject to implementation feasibility:

- map image
- GeoJSON/vector export
- raster export
- event/scenario report
- animation/video export
- reproducibility manifest

Exports must retain scenario/date/source metadata.

## Web architecture

The visualization layer should consume preprocessed analytical products rather than execute expensive regional modelling on every map interaction. Heavy Python/GeoAI processing remains in the analysis pipeline; the web client focuses on query, rendering and animation.

## Performance targets

- regional overview: progressive/lazy loading
- glacier selection: responsive source-to-downstream highlighting
- detailed event: load only required tiles/features
- animation: precomputed or cached time states where feasible

Exact latency targets are implementation benchmarks, not scientific claims.

## Mobile/responsive principle

Core 2D tracing and event summaries should remain usable on smaller screens. Full 3D may be desktop-first if device performance requires it.

## Outputs

`map_style_registry`

`visualization_layer_registry`

`trace_view_config`

`animation_manifest`

`scene_manifest`

`export_manifest`

## Acceptance gate

BUILD-03K is complete for a pilot when one validated event/source can be traced from glacier/source through hydrography, hazard, exposure, impact and evacuation layers in 2D; the same event can be rendered in 3D; and a documented event/scenario timeline can be animated without confusing modelled timing with observed timing.

## Next step
BUILD-03L — Integrated HG-SCRIS Web Application, API/Data Services & Research Dashboard.
