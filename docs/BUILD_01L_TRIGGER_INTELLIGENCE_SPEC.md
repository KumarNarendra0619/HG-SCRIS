# BUILD-01L — Glacier / Glacial-Lake Trigger Intelligence

## Objective
Create the source-condition layer that identifies and prioritises glaciers and glacial lakes for cascade scenario analysis, while keeping screening distinct from failure probability.

## Source variables
The production inventory may include, where available and sourced:

- glacier ID and geometry
- glacier area and change through time
- elevation range and hypsometry
- slope/aspect and terrain setting
- debris cover indicators
- glacier velocity or motion indicators
- terminus position/change
- glacial-lake ID, area, elevation and change
- lake volume or depth estimates with uncertainty
- moraine/dam geometry and stability indicators
- surrounding slope/rock/ice instability indicators
- seismic, precipitation, temperature or other documented trigger observations
- historical event evidence

Every observation retains acquisition date, source, spatial resolution and uncertainty where available.

## Trigger screening
A transparent weighted index is provided only for **prioritisation**. Factors must be normalized to [0,1], weights must be explicit, and the resulting class is labelled a screening priority—not a failure probability.

No threshold in this module means "GLOF will occur".

## Event-specific trigger determination
Historical reconstruction will use observed evidence first, then process-based inference. A trigger hypothesis must retain evidence type and confidence and must not be treated as established merely because a screening index is high.

## Production trigger workflow

`Glacier/Lake inventory → temporal change detection → geomorphic/terrain indicators → trigger evidence → screening priority → scenario definition → cascade engine`

## Quality controls

1. Stable glacier/lake identifiers.
2. Acquisition dates retained.
3. Source and resolution retained.
4. No mixing of observation years without temporal labeling.
5. Missing values remain missing; no silent zero-filling.
6. Screening score reproducible from stored factors and weights.
7. Screening score never labelled as probability.
8. Historical observations separated from model outputs.

## Planned outputs
Per glacier/lake:

- trigger-source record
- temporal-change metrics
- trigger indicator table
- screening priority class
- evidence/confidence metadata
- scenario-ready trigger definition
- provenance and uncertainty

## Scientific boundary
BUILD-01L does not estimate a calibrated GLOF probability, lake-failure probability, outburst discharge or breach hydrograph. Those require event/process-specific modelling and validation.
