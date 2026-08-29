# BUILD-01P — Glacier → Waterbody → River → Settlement Connectivity Engine

## Objective
Create a traceable spatial/network backbone linking each glacier or glacial lake to downstream streams, tributaries, rivers, water bodies and exposed settlements/infrastructure.

## Conceptual chain

`Glacier → lake/outlet → stream → tributary → river → water body → settlement/infrastructure`

The chain is represented as a directed graph. Spatial geometry and graph topology are retained separately so that routing assumptions can be audited.

## Node classes

- glacier
- glacial lake
- outlet
- stream
- tributary
- river
- water body
- settlement
- infrastructure

## Edge attributes
Each link should retain, where applicable:

- source and target IDs
- link type
- routing method
- flow-direction evidence
- distance/length
- elevation drop
- confidence/evidence class
- source dataset
- processing version

## Routing hierarchy

### Level 1 — Inventory connectivity
Use authoritative hydrography/inventory relationships where available.

### Level 2 — DEM-derived routing
Use hydrologically conditioned DEM flow direction/accumulation to connect outlets to drainage.

### Level 3 — Constrained network matching
Resolve DEM drainage against mapped streams/tributaries/rivers using topology and spatial tolerance.

### Level 4 — Expert/event verification
For historical events, compare the inferred route with imagery, reports, field observations and observed deposits/footprints.

No single routing method is treated as infallible.

## Glacier-to-settlement trace
For each source, the system can generate:

`source_id → downstream waterbody → stream/tributary → river → receptor`

and preserve the complete node sequence. This path becomes the backbone for hazard corridor propagation and later animation.

## Multiple pathways
A source may have multiple plausible downstream branches. The engine must retain branching rather than forcing a single route where network evidence is ambiguous.

## Elevation and slope integration
Each routed segment should later be enriched with DEM-derived elevation, slope, longitudinal gradient and valley geometry. These attributes are descriptive/model inputs, not direct risk scores.

## Critical scientific distinction
Connectivity does not mean hazard occurrence. A settlement connected downstream to a glacier is **potentially connected/exposed**, not automatically at risk. Hazard intensity, probability, vulnerability and scenario assumptions are required before risk classification.

## Event reconstruction
Historical event routing should produce an observed/evidence-supported pathway separately from a modelled pathway. Discrepancies must be retained for validation rather than hidden.

## Outputs

- source-to-waterbody network
- glacier/lake downstream traces
- tributary and river hierarchy
- settlement/infrastructure receptor links
- path distance and elevation attributes
- routing confidence/evidence
- ambiguity/multiple-path flags
- provenance manifest

## Next integration
BUILD-01Q will add terrain/valley morphology and longitudinal hydraulic-routing inputs so the connectivity backbone can become a spatially parameterized cascade corridor.
