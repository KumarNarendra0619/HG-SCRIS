# BUILD-02D — Hydrography, Glacier-to-River Connectivity & Downstream Flow Network

## Objective
Build a validated hydrographic graph linking glacier/lake outlets to streams, tributaries, river reaches and downstream receptors. This is the network backbone for glacier-centric cascade analysis.

## Canonical chain
`Glacier → Lake → Outlet → Stream → Tributary → River Reach → Settlement/Infrastructure`

Not every glacier has a lake, and not every network is a simple chain. The data model therefore supports a directed graph rather than forcing a single linear path.

## Feature classes
- glacial lake
- lake outlet
- stream/reach
- tributary
- main river/reach
- confluence/junction
- glacier outlet/source point

## Required relationship fields
Every directed edge records:
- upstream ID
- downstream ID
- routing method
- connectivity status
- source/version
- lineage
- uncertainty

## Connectivity evidence
Connectivity should be established using a combination of:
1. mapped hydrography
2. DEM flow direction/accumulation
3. glacier/lake outlet geometry
4. terrain inspection
5. event-specific observations where available

No single nearest-feature rule is sufficient for final scientific linkage.

## Network QA
Check:
- geometry validity
- duplicate reaches
- direction consistency
- disconnected features
- impossible self-loops
- cycles in directed drainage graph
- confluence topology
- glacier/lake outlet placement
- DEM-routing vs mapped-hydrography disagreement

Unresolved disagreements become `pending` rather than being silently corrected.

## Branching networks
A downstream network may branch, and a glacier may influence multiple reachable receptors under different scenarios. The graph must preserve branches. A single-chain helper is only valid when the graph has one downstream successor at each step.

## Glacier-centric downstream trace
For selected glacier G:

`G → reachable hydrography → downstream reaches → settlements/infrastructure`

The trace must be scenario-aware when hazard propagation or flow magnitude changes which branches are relevant.

## Hydrological vs hazard connectivity
Hydrological connectivity does NOT equal hazard exposure. A settlement downstream of a glacier is a potential receptor, not automatically a risk location. Hazard intensity, travel time, topography, process type and exposure analysis must be applied later.

## Network attributes
Where data support them, retain:
- reach length
- upstream/downstream elevation
- longitudinal slope
- network order
- drainage area
- junction IDs
- source date

## Event-specific connectivity
Historical events may deviate from present-day routing because channels, lakes, debris deposits, bridges and infrastructure change. Event reconstruction must therefore support event-date network states where evidence exists.

## Outputs
- hydrography master layer
- directed connectivity graph
- glacier-to-lake linkage
- glacier/lake-to-outlet linkage
- outlet-to-reach linkage
- reach-to-settlement receptor linkage
- connectivity QA report
- unresolved-linkage register
- provenance manifest

## Scientific acceptance gate
A connectivity edge is `passed` only when its direction, evidence, source and method are documented. Pending edges may be displayed as uncertain/exploratory but must not silently enter validated cascade results.

## Next step
BUILD-02E — Settlement, Population & Critical Infrastructure Exposure Baseline.
