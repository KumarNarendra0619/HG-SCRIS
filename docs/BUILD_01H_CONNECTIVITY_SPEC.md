# BUILD-01H — Glacier Outlet, Stream Extraction & Hydrography Validation

## Objective
Convert DEM-derived drainage into candidate streams and attach explicit evidence of glacier-to-river connectivity without confusing spatial proximity with hydrological proof.

## Processing chain

`Glacier → DEM-conditioned outlet → D8 routing → accumulation → stream threshold → candidate stream → independent hydrography comparison → connectivity class`

## Stream extraction
Candidate stream cells are generated from flow accumulation using a declared threshold. Threshold selection must be sensitivity-tested because it changes drainage density and glacier-to-river links.

## Hydrography validation
The production workflow compares DEM-derived drainage against an independent hydrographic product. Agreement increases confidence; disagreement triggers QA rather than forced matching.

## Connectivity classes

- **C3 Strong:** DEM-derived route and independent hydrography agree.
- **C2 Moderate:** one validated evidence stream supports the connection.
- **C1 Weak:** proximity/partial evidence only.
- **C0 Unresolved:** no defensible connection established.

## Water bodies
A downstream water body is linked only after the routed path intersects a validated lake/reservoir/water-body dataset or an explicitly documented hydrological endpoint. A visual map intersection alone is not sufficient for a confirmed causal link.

## Outputs
For each glacier:

- outlet seed
- routed downstream path
- candidate stream ID
- tributary/main-channel relationship where supported
- nearest/linked hydrographic feature
- downstream water-body ID where supported
- connectivity evidence class
- distance diagnostics
- source and method provenance

## Scientific boundary
This build establishes **surface drainage connectivity**. It does not estimate flood discharge, inundation depth, flow velocity, travel time, erosion/deposition, or impact extent. Those belong to hazard/hydraulic modules.
