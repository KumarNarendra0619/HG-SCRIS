import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

from hgscris.hydrology.stream import extract_stream_mask
from hgscris.hydrology.connectivity import connectivity_evidence, attach_connectivity_evidence


def test_stream_threshold():
    acc = np.array([[1, 5], [10, 20]], dtype=float)
    mask = extract_stream_mask(acc, 10)
    assert mask.tolist() == [[False, False], [True, True]]


def test_c3_connectivity():
    result = connectivity_evidence(12.0, True, True)
    assert result["connectivity_class"] == "C3"


def test_attach_evidence():
    glaciers = gpd.GeoDataFrame({"glacier_id": ["G1"]}, geometry=[Point(0, 0)], crs="EPSG:4326")
    evidence = pd.DataFrame({"glacier_id": ["G1"], "connectivity_class": ["C2"]})
    out = attach_connectivity_evidence(glaciers, evidence)
    assert out.loc[0, "connectivity_class"] == "C2"
