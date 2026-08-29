from hgscris.cryosphere.normalize import GlacierRecord, detect_duplicate_ids, normalize_id


def test_normalize_id_is_source_qualified():
    assert normalize_id("RGI7", "RGI60-01.00001") == "RGI7:RGI60-01.00001"


def test_duplicate_detection():
    assert detect_duplicate_ids(["A", "B", "A"]) == ["A"]


def test_glacier_record_validation():
    record = GlacierRecord("G1", "RGI7", "geom/G1", "2000", 2.0, 4000, 6000)
    assert record.validate() == []
