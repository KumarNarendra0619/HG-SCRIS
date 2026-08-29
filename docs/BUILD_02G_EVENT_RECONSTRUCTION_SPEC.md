# BUILD-02G — Multi-Dimensional Event Reconstruction & Cascade Scenario Engine

## Objective
Reconstruct selected Himalayan events as traceable sequences from source evidence through inferred relationships and modelled scenarios. The engine must support comparison of observed, reconstructed and alternative scenarios without presenting model output as historical fact.

## Core reconstruction chain

`Trigger → initiation/source → release/process → terrain interaction → flow/cascade pathway → waterbody/channel response → downstream propagation → exposure → observed impact`

Not every event contains every stage. Missing stages remain explicit.

## Three evidence states

### OBSERVED
Directly documented or mapped evidence.

### INFERRED
Scientifically reasoned relationship supported by available evidence but not directly observed.

### MODELLED
Output of a defined computational scenario.

These states are stored on every reconstruction step and are visually separated in the future application.

## Reconstruction step model
Each step contains:

- step ID
- event ID
- sequence
- stage
- status
- input references
- output reference
- method
- parameters
- uncertainty
- validation reference
- processing version
- lineage ID

## Event reconstruction stages

### R1 — Event definition
Confirm date/time/location and event classification.

### R2 — Source identification
Identify candidate glacier/lake/landslide/rainfall/other source and supporting evidence.

### R3 — Initiation reconstruction
Determine the best-supported initiation mechanism and alternatives where uncertain.

### R4 — Release/process reconstruction
Characterize the event process using available observations and scientific literature.

### R5 — Terrain interaction
Use DEM-derived slope, relief, valley geometry and channel characteristics.

### R6 — Network routing
Trace candidate downstream pathways through validated hydrography.

### R7 — Propagation envelope
Generate scenario-dependent candidate corridors. A geometric envelope is not automatically a hazard intensity field.

### R8 — Exposure intersection
Intersect candidate pathways with temporally appropriate settlements, population and infrastructure.

### R9 — Observed-impact comparison
Compare reconstruction with mapped/documented footprints, damage and impact evidence.

### R10 — Alternative scenarios
Where uncertainty exists, run explicitly labelled alternatives rather than forcing one deterministic answer.

## Physics/process model policy
The first production implementation should use process-specific models where scientifically justified. Do not create a universal "one formula" for all Himalayan cascades. GLOF, debris flow, avalanche, landslide-dam failure and compound flood processes have different governing assumptions.

The system should therefore expose a model registry with:

`process type → model family → required inputs → assumptions → calibration data → validation metrics → applicability limits`

## Scenario levels

### Level 0 — Connectivity screening
Network/terrain based, no hazard intensity claim.

### Level 1 — Geometric propagation scenario
Defined envelope/corridor for exploratory analysis.

### Level 2 — Process-based simulation
Hydraulic, debris-flow, avalanche or other process model where required inputs are available.

### Level 3 — Calibrated reconstruction
Parameters constrained against observed event evidence.

A lower-level scenario must not be labelled as a higher-level result.

## Calibration and validation
For events with observed footprints:

`Observed footprint ↔ reconstructed footprint`

Evaluate suitable metrics such as spatial overlap, omission/commission, distance-to-observed-front, arrival-time error where time data exist, and reach/settlement hit accuracy.

Do not optimize against the same evidence and then report it as independent validation. Use independent evidence, hold-out observations or cross-event validation where feasible.

## Uncertainty propagation
Uncertainty should be tracked for:

- source location
- event timing
- DEM
- channel geometry
- process parameters
- routing
- observed footprint
- exposure data

Where feasible, use scenario ensembles/sensitivity analysis rather than one arbitrary parameter set.

## Event reconstruction product
For each event produce:

- event timeline
- source hypothesis
- reconstructed pathway
- alternative pathways
- terrain profile
- network trace
- observed footprint
- reconstructed footprint
- exposure intersection
- model level
- validation metrics
- uncertainty map/register
- provenance graph

## Animation-ready output
Each reconstruction step should expose a temporal sequence:

`T0 source → T1 initiation → T2 propagation → T3 channel interaction → T4 downstream reach → T5 settlement exposure → T6 observed impact`

Animation is a visualization of model/evidence states, not evidence itself.

## Critical safety rule
The application must not produce an evacuation command from an uncalibrated screening model. Evacuation/safety outputs require explicit scenario assumptions, uncertainty, authority context and appropriate operational validation.

## Acceptance gate
A reconstruction is production-ready only when all major steps have traceable inputs, methods, uncertainty and status, and when modelled outputs are compared against independent or clearly labelled observed evidence where available.

## Next step
BUILD-02H — End-to-End Pilot: one complete event from source data to validated 2D/3D reconstruction.
