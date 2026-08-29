# BUILD-04F — Glacier-to-River Connectivity, QA & Downstream Trace Engine

## Purpose
Construct a reproducible hydro-connectivity graph that allows HG-SCRIS to trace a selected glacier/source downstream through river reaches, tributaries and confluences to potentially exposed places. This is a connectivity engine, not yet a flood/debris-flow hazard model.

## Core analytical chain

`glacier → lake/source → outlet → headwater/reach → downstream reaches → tributaries/confluences → settlement/exposure`

The trace must be based on explicit feature IDs and network topology. Nearest-feature proximity alone is insufficient to establish hydrological connectivity.

## Inputs

- canonical glacier master
- canonical lake/source master
- canonical hydrography master
- DEM/terrain reference where required for QA or flow-direction support
- settlement/exposure master
- optional authoritative outlet/catchment relationships

## Graph model

Represent the river system as a directed graph:

- node = network junction/outlet/confluence/terminal or analytically relevant point
- edge = river reach
- direction = inferred/validated downstream flow direction
- attributes = length, elevation context, stream order/class, source dataset, QA status

Maintain a feature-level relation table for glacier/source → reach and reach → downstream reach relationships.

## Connectivity hierarchy

### Level 1 — Source linkage
Establish glacier/lake/source to outlet relationship from authoritative geometry, outlet metadata, terrain evidence or documented spatial rules.

### Level 2 — Reach linkage
Attach outlet to the appropriate hydrographic reach using topology/containment and documented snapping tolerance where required.

### Level 3 — Downstream traversal
Traverse only edges whose direction is validated or explicitly marked as inferred.

### Level 4 — Place linkage
Associate settlements/exposure features with relevant downstream reaches using documented spatial rules. A nearby settlement is not automatically considered hydraulically exposed.

## Flow-direction validation

Where explicit direction is unavailable, infer direction using appropriate hydrographic attributes and/or terrain-derived flow evidence. Store the direction method and confidence. Never infer direction solely from feature vertex order.

## Topology QA

Check:

- duplicate reach IDs
- self-loops
- invalid geometries
- disconnected components
- impossible direction conflicts
- multiple downstream edges where unsupported
- missing upstream/downstream references
- duplicate confluence relationships
- cycles in a normally dendritic river graph
- outlet-to-reach mismatch

True braided/anabranching systems must not be incorrectly “fixed” into a simple tree; the network model must preserve legitimate multi-channel structure when supported by the source.

## DEM-assisted checks

Where DEM data are appropriate, use them as supporting evidence for:

- local drainage plausibility
- outlet elevation ordering
- suspicious reverse flow
- reach connectivity

DEM-derived flow should not automatically overwrite authoritative hydrography.

## Downstream trace algorithm

For a selected `source_id`/`glacier_id`:

1. resolve linked outlet
2. resolve outlet reach
3. verify direction status
4. traverse downstream edges
5. record confluences/tributaries encountered
6. calculate cumulative network distance where valid
7. intersect/link downstream settlements/exposure
8. attach QA and provenance to every relationship
9. return an ordered trace manifest

## Trace output

Minimum fields:

- trace_id
- glacier_id
- source_id
- outlet_id
- reach_id
- sequence
- upstream_reach_id
- downstream_reach_id
- network_distance
- confluence_flag
- settlement_id where linked
- connectivity_status
- method_id
- lineage_id
- uncertainty/status

## Place-by-place output

The engine must support:

`source → reach 001 → reach 002 → confluence → reach 003 → settlement A → reach 004 → settlement B`

This ordered structure becomes the basis for later hazard propagation, arrival-time modelling, impact analysis and animation.

## Disconnected/uncertain handling

If a trace cannot be established:

- `DISCONNECTED`
- `AMBIGUOUS`
- `DIRECTION_UNVALIDATED`
- `SOURCE_LINK_UNCERTAIN`

must be returned rather than silently forcing connectivity.

## Network metrics

Where data support them, derive:

- network distance from source
- cumulative downstream elevation change
- reach slope/context
- stream order/class
- number/type of confluences
- drainage hierarchy

These are network/context metrics, not hazard intensity measures.

## Scientific separation

BUILD-04F does **not** determine whether a downstream place will flood, experience debris flow, or be damaged. It establishes the physically plausible network through which a later process-specific cascade model may propagate.

## Reproducibility

Every trace must be reproducible from:

- canonical input versions
- graph version
- trace method ID
- snapping/tolerance parameters if any
- DEM/version if used
- processing code version
- run timestamp

## Performance

Build the graph once for a dataset version and cache/index it. Interactive glacier tracing should query the graph rather than reconstructing topology on every request.

## Deliverables

- directed hydrography graph
- connectivity QA report
- source-to-reach relation table
- downstream trace engine
- trace manifest schema
- unresolved connectivity table
- network metrics table
- unit/integration tests

## Acceptance gate

BUILD-04F is complete when a pilot glacier/source can be reproducibly linked to an outlet, traversed through validated hydrographic reaches, and returned as an ordered downstream trace with confluences, network distance, linked downstream places, provenance and uncertainty/status. No hazard or impact claim is made at this gate.

## Next step
BUILD-04G — Event Reconstruction Engine: Evidence Fusion, Temporal Sequencing & Process Attribution.
