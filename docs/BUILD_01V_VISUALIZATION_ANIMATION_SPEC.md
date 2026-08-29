# BUILD-01V — 2D/3D Spatio-Temporal Visualization & Animation Engine

## Objective
Turn validated HG-SCRIS model outputs into an interactive research visualization in which every visual layer remains traceable to its source dataset, model scenario and timestamp.

## Visualization principle
The map is an analytical interface, not decoration. Animation must be driven by modelled/observed timestamps and spatial states; it must never invent movement between unsupported observations.

## Canonical layers

1. Terrain / DEM
2. Glacier inventory
3. Glacial lakes
4. Streams / tributaries / rivers
5. Glacier-to-settlement connectivity
6. Trigger/source location
7. Modelled hazard footprint
8. Hazard arrival-time contours/segments where supported
9. Exposed population and assets
10. Evacuation routes
11. Candidate safe zones
12. Observed historical footprint/damage

## 2D mode

Primary research map should support:

- pan/zoom
- layer control
- glacier/source selection
- downstream trace
- scenario selection
- time slider
- feature inspection
- legend
- uncertainty/provenance display
- export of map state/data

## 3D mode

Terrain should be rendered from the DEM with physically meaningful vertical positioning. Glacier/lake/hydrography/hazard layers should be draped or positioned against terrain using their actual coordinates/elevations where available.

Avoid exaggerated vertical scale in scientific views. If vertical exaggeration is used for readability, it must be displayed explicitly.

## Animation model

`Scenario → timestamp sequence → spatial state per timestamp → renderer`

A frame can contain:

- hazard extent
- arrival status
- exposed receptors
- route status
- safe-zone status
- observed/modelled status

Animation must be deterministic and reproducible from stored frame/state data.

## Event reconstruction mode

Historical events require two visually distinct evidence classes:

- **Observed:** satellite/field/report-derived evidence
- **Modelled:** simulation or routing result

The UI must not visually imply that modelled polygons were observed.

## Glacier-centric interaction

When a glacier is selected, the interface should expose:

`Glacier → Lake/Outlet → Stream → Tributary → River → Settlements → Exposure → Risk → Evacuation`

and highlight the corresponding downstream corridor in both 2D and 3D.

## Animation sequence for a cascade

Example logical sequence:

`T0 source → T1 release → T2 first channel reach → T3 tributary junction → T4 main valley → T5 settlement exposure → T6 downstream settlement → T7 evacuation state`

Actual timestamps and extents must come from the scenario model or documented event observations.

## Cartographic design

Use a restrained scientific hierarchy. Avoid excessive colors, animation speed, glow effects or 3D exaggeration that can obscure uncertainty or create false precision.

The interface should provide both:

- presentation mode for communication
- inspection mode for research/QA

## Performance architecture

The browser should not recompute heavy scientific models. Precompute/serve analysis-ready tiles, vector features, terrain tiles and time-indexed states. Python/Colab remains the research computation layer; the web application is the visualization/interaction layer.

## Reproducibility

Each visualization state should be identifiable by:

- project/data version
- scenario ID
- model version
- timestamp/frame ID
- CRS
- DEM version
- uncertainty/evidence class

## Safety

Evacuation/safe-zone visualization is research screening. It must not be presented as an official emergency warning or evacuation order.

## Outputs

- interactive 2D research map
- interactive 3D terrain scene
- time-slider animation
- glacier-centric downstream trace
- scenario comparison
- observed-vs-modelled event reconstruction
- map/data export
- reproducibility metadata

## Next integration
BUILD-01W will package the complete analytical chain into the working HG-SCRIS web platform, with data ingestion, scenario controls, map/3D viewer, analysis panels, provenance and research export.
