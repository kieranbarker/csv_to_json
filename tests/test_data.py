import json
from pathlib import Path


def load():
    p = Path("output/people.json")
    return json.loads(p.read_text(encoding="utf-8"))


def test_schema_and_required_fields():
    data = load()
    assert isinstance(data, list)
    for row in data:
        assert set(row.keys()) == {"id", "name", "age"}
        assert isinstance(row["id"], int)
        assert isinstance(row["name"], str)
        assert row["name"] != ""
        assert isinstance(row["age"], int)


def test_uniqueness_of_id():
    data = load()
    ids = [r["id"] for r in data]
    assert len(ids) == len(set(ids))


def test_value_ranges():
    data = load()
    for row in data:
        assert row["age"] >= 0
        assert row["age"] <= 130
