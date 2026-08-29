# BUILD-03F — Historical Event Evidence & Reconstruction

## Objective
Reconstruct historical Himalayan hazard events from independently traceable evidence and separate observed facts, defensible inferences and modelled results.

## Evidence classes

- official government / agency records
- peer-reviewed scientific literature
- satellite imagery and derived change products
- DEM / terrain evidence
- meteorological and hydrological observations/products
- field observations / photographs / geotagged evidence
- authoritative news reporting for chronology and corroboration
- community/local testimony when systematically documented

Secondary reports are supporting evidence, not automatically ground truth.

## Event record

Each event receives a stable event ID and records:

- event name/location
- event date/time and timezone status
- hazard/process type
- source/trigger candidate
- affected valley/basin
- source glacier/lake/landform candidate
- downstream pathway
- observed impact
- uncertainty
- evidence references
- reconstruction status

## Evidence-led workflow

`event discovery → source collection → temporal normalization → spatial georeferencing → evidence extraction → source independence check → event timeline → trigger/source hypothesis → pathway reconstruction → observed impact mapping → contradiction review → reconstruction status`

## Three epistemic states

Every material claim must be labelled:

`OBSERVED` — directly supported by evidence.

`INFERRED` — reasoned from observed evidence using an explicit method.

`MODELLED` — produced by a computational/process model.

Never display inferred/modelled output as historical observation.

## Source independence

Multiple copies of the same wire story, report or satellite-derived product are not independent evidence. The registry records an independent source group so corroboration is not double-counted.

## Event timeline

Build a normalized sequence:

`pre-event conditions → trigger candidate → source/process initiation → cascade/pathway → downstream response → observed impact → recovery/post-event state`

Unknown times remain unknown; the system must not manufacture timestamps from publication times.

## Reconstruction logic

For each event:

1. establish what is directly observed;
2. identify plausible trigger/source candidates;
3. test spatial consistency against glacier/lake, DEM and hydrography layers;
4. test temporal consistency against forcing and imagery;
5. trace downstream connectivity;
6. map observed impacts;
7. identify contradictions;
8. assign reconstruction status;
9. retain uncertainty and alternative hypotheses.

## Historical imagery

Before/after imagery can establish spatial change but cannot automatically establish the physical cause. Acquisition date and observation date must be preserved separately from publication date.

## Trigger attribution

Candidate triggers may include extreme precipitation, rapid snow/ice change, lake breach, avalanche/icefall, landslide, channel blockage or compound processes. A candidate trigger is not accepted solely because it is temporally correlated with the event.

## Compound events

Events may contain multiple sequential processes. Represent them as a directed event graph rather than forcing a single-hazard label:

`trigger → source failure → flow/debris/GLOF → channel response → secondary failure → settlement impact`

## Contradictions

Conflicting evidence must be retained. If credible evidence conflicts, reconstruction status becomes `CONTESTED` until resolved or explicitly presented as alternative hypotheses.

## Reconstruction status

- `OBSERVED_SUPPORTED`
- `OBSERVED_PLUS_INFERRED`
- `INFERRED_ONLY`
- `CONTESTED`
- `INSUFFICIENT_EVIDENCE`

These are evidence states, not probabilities.

## Spatial products

For each reconstructed event, where supported:

- source feature
- source uncertainty zone
- connected network
- observed pathway/footprint
- observed affected places
- inferred pathway
- modelled scenario pathway
- uncertainty/alternative pathway

## Critical separation

`NETWORK_CONNECTED` does not mean `HISTORICALLY_AFFECTED`.

`HISTORICALLY_AFFECTED` does not mean `FUTURE_HAZARD`.

`FUTURE_HAZARD` requires an explicit scenario/process model.

## Validation

Validation should use independent evidence where possible, such as satellite-derived footprints, official damage records, field observations, gauge data and independently mapped channel changes. The same dataset used to build a reconstruction should not be treated as independent validation.

## Outputs

`event_master`

`event_evidence`

`event_timeline`

`event_source_candidates`

`event_pathway_reconstruction`

`event_observed_impacts`

`event_contradictions`

`event_reconstruction_status`

`event_manifest`

## Acceptance gate

BUILD-03F is complete for a pilot when an event can be reconstructed from source records through timeline, source/trigger hypotheses, downstream pathway and observed impacts, with every material claim traceable to evidence and clearly labelled as observed, inferred or modelled.

## Next step
BUILD-03G — Settlement, Infrastructure & Exposure Inventory.
