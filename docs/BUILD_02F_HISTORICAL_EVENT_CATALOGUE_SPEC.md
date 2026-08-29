# BUILD-02F — Historical Himalayan Event Catalogue & Evidence Matrix

## Objective
Create a reproducible event database for Himalayan cryosphere-related hazards and downstream impacts, with an evidence matrix strong enough to support event reconstruction and model validation.

## Scientific principle
The catalogue records what is observed/documented. It must not convert an uncertain report into a model fact. Observed evidence, inferred relationships and modelled outputs remain separate.

## Event classes
The catalogue can represent, among others:

- glacier-related flood
- glacial lake outburst flood (GLOF)
- ice/debris avalanche
- rock-ice/debris cascade
- landslide-dammed lake failure
- rain-on-snow / compound flood
- extreme rainfall + cryosphere interaction
- other cryosphere-linked cascade

The `trigger_type` and `process_type` fields are separate so that a meteorological trigger is not confused with the resulting process.

## Event record
Each event should capture:

`event_id, name, date/time, location, trigger, process, glacier/lake/outlet, hydrography, observed footprint, affected settlements, impact, casualties/displacement, sources, evidence level, uncertainty, lineage, QA`

## Evidence matrix
Each factual claim should be traceable to an evidence record containing:

- evidence ID
- event ID
- evidence type
- source name
- source URL/reference
- observation date
- spatial reference
- temporal reference
- claim
- confidence
- independent-source flag
- notes

## Evidence hierarchy
Prefer evidence according to its suitability for the specific claim:

1. direct field/official observation and authoritative records
2. satellite/remote-sensing evidence
3. peer-reviewed/scientific reconstruction
4. documented institutional reports
5. reputable contemporaneous reporting
6. crowdsourced/secondary material as supplementary evidence

A lower-ranked source is not automatically false; it requires appropriate corroboration and uncertainty treatment.

## Claim-level reconstruction
For an event, break broad statements into testable claims:

`Claim → Evidence → Spatial/temporal support → Confidence → Model use`

Example categories:

- source location
- trigger timing
- flow direction
- inundated area
- deposition area
- channel change
- settlement impact
- road/bridge damage
- casualty/displacement observations

## Observed vs inferred vs modelled
Three statuses are mandatory conceptually:

### Observed
Directly documented/mapped.

### Inferred
Reasoned from evidence but not directly observed.

### Modelled
Produced by HG-SCRIS calculations/scenarios.

These must not be visually conflated in maps or animation.

## Conflict handling
If two sources disagree:

- retain both source claims
- document the conflict
- do not average categorical claims blindly
- assign uncertainty
- identify what additional evidence would resolve the conflict

## Evidence score
The repository includes a transparent screening score based on confidence and independent-source coverage. It is explicitly **not** a statistical probability that an event or claim is true. Publication-level inference must use claim-specific evidence assessment.

## Event reconstruction inputs
For selected events, the catalogue will feed:

`event timing → source glacier/lake → terrain state → hydrography → observed footprint → exposed receptors → model scenario`

## Historical state rule
Where possible, use data temporally appropriate to the event. Present-day glacier boundaries, settlements or infrastructure must not automatically be substituted for historical state without documenting the temporal mismatch.

## Required pilot event categories
The pilot set should include multiple cascade mechanisms rather than only one hazard type. Candidate events should be selected after evidence screening, not merely by fame or media visibility.

## Outputs

- historical event catalogue
- claim-level evidence matrix
- event source bibliography/manifest
- observed footprint references
- event uncertainty register
- event-to-glacier/lake/hydrography crosswalk
- event readiness score/status

## Acceptance gate
An event is reconstruction-ready only when its timing/location/process are sufficiently documented for the intended analysis and the major claims have traceable evidence. Missing evidence remains explicit.

## Next step
BUILD-02G — Multi-Dimensional Event Reconstruction & Cascade Scenario Engine.
