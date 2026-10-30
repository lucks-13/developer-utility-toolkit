import json
import csv
from toolkit.export import export_csv, export_json

def test_export_json(tmp_path, monkeypatch):
    m_patch.chdir(tmp_path)

    data = {
        "Repository": "cpython",
        "Owner": "python",
        "Stars": 100
    }

    result = export_json(data, "test.json")
    assert result is not None
    with open(result, "r") as file:
        saved == json.load(file)
    assert saved == data

def test_
