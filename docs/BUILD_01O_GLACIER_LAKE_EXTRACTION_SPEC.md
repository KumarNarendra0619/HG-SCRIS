# BUILD-01O — Glacier & Glacial Lake Extraction Engine

## Objective
Convert analysis-ready remote-sensing inputs into reproducible glacier and glacial-lake geometries, then generate geometry QA and change metrics suitable for BUILD-01M and BUILD-01L.

## Extraction principle

`Source imagery → preprocessing → candidate mask → segmentation/classification → polygonization → geometry QA → validation → measurement → temporal record`

The extraction algorithm is deliberately not hard-coded to one sensor or one spectral threshold. The method must be recorded per product/region/date.

## Supported method families

- manual/visual interpretation
- rule-based spectral/index masks
- supervised/unsupervised segmentation
- machine-learning/deep-learning segmentation
- hybrid expert + automated refinement

Automated output is a candidate product until validation is completed.

## Glacier attributes
Minimum production record:

- glacier_id
- geometry
- observation_date
- area_m2
- source/product
- extraction_method
- processing_version
- validation_status
- uncertainty/accuracy where available

Optional: elevation statistics, hypsometry, slope/aspect, debris-cover class, terminus position, velocity and temporal lineage.

## Lake attributes
Minimum production record:

- lake_id
- geometry
- observation_date
- area_m2
- elevation_m where available
- source/product
- extraction_method
- processing_version
- validation_status
- uncertainty/accuracy where available

Optional: perimeter, depth/volume estimates, moraine/dam attributes and connected glacier ID.

## Geometry QA

1. CRS must be present.
2. Geometry must be polygon/multipolygon.
3. Empty/null geometry is rejected.
4. Stable IDs are required.
5. Duplicate IDs within a snapshot are rejected.
6. Area is calculated only in an appropriate projected CRS.
7. Topology/self-intersection checks must be added to the production validation workflow.

## Validation
Validation samples must be independent of the training/threshold selection used to produce an automated extraction. Report suitable metrics such as intersection-over-union, omission/commission error, area error and boundary accuracy where the design permits.

## Temporal lineage
A glacier/lake polygon from one date must be linked to its corresponding entity in later dates through stable IDs and documented matching rules. Apparent disappearance/appearance must be flagged for review rather than silently creating or deleting entities.

## Critical scientific rule
A spectral/ML polygon is not automatically a true glacier or lake boundary. Snow, cloud, shadow, debris, seasonal meltwater and mixed pixels can cause false extraction. Validation is mandatory before using an extracted boundary as authoritative evidence.

## Outputs

- glacier snapshot inventory
- lake snapshot inventory
- validated geometry layer
- extraction QA report
- area measurements
- temporal change records
- provenance manifest
- uncertainty/accuracy metadata

## Next integration
BUILD-01P will connect extracted glacier/lake geometries with DEM, hydrography and glacier-to-settlement routing so each source can be traced downstream into potential hazard corridors.
