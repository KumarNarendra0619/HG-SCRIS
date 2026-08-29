# BUILD-01K — Multi-Hazard Cascade Engine

## Objective
Represent the physical cascade from glacier/lake trigger through mass and water processes, drainage, settlements and infrastructure as an explicit directed graph.

## Architecture

`Trigger → process material → channel entry → tributary/river → downstream system → exposed receptors → impact`

The graph can represent combinations such as:

- GLOF: lake/outburst → water → stream → river
- Debris flow: trigger → debris → stream → river
- Rock/ice avalanche: trigger → rock/possible impulse water → stream
- Compound scenarios: multiple process branches converging on a channel

## Evidence discipline
Every edge carries an evidence class (`C3`, `C2`, `C1`, `C0`) and a status (`candidate` by default). The standard rule library intentionally initializes process links as C0 candidates. They must be upgraded only after event, EO, DEM, hydrography, field or literature evidence is attached.

## Why a graph
A single raster hazard score cannot adequately represent branching and cascading Himalayan processes. A directed graph preserves sequence, branching, convergence and provenance and can later feed spatial routing, scenario simulation and animation.

## Event reconstruction
Historical events will be represented as observed/modelled graphs. Observed evidence and inferred links must remain separate. Calibration and validation observations must be partitioned to avoid circular validation.

## Future scenario
The same graph structure supports parameterized future scenarios. Scenario outputs must retain trigger assumptions, forcing, parameter set, data versions, model version and uncertainty.

## Current boundary
BUILD-01K is a **cascade representation engine**, not yet a quantitative cascade simulator. It does not calculate discharge, flow depth, velocity, sediment concentration, entrainment, arrival time, damage or mortality.

Those require specialized process models in subsequent builds.
