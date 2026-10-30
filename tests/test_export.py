import json
import csv
from toolkit.export import export_csv, export_json

def test_export_json(temp_path, m_patch):
    m_patch.chdir(temp_path)

    data = {
        "Repository": "cpython",
        "Owner": "python",
        "Stars": 100
    }

    result = export_json(data, "test.json")
    assert result is not None
    with open(result, "r") as file:
        saved = json.load(file)
    assert saved == data

def test_export_json_no_data():
    result = export_json(None, "test.json")
    assert result is None

def test_export_csv(temp_path, m_patch):
    m_patch.chdir(temp_path)

    data = [
        {
            "Repository": "cpython",
            "Owner": "Python",
            "Stars": 100
        },
        {
            "Repository": "requests",
            "Owner": "Python",
            "Stars": 80
        }
    ]

    result = export_csv(data, "test.csv")
    assert result is not None
    with open(result, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert len(rows) == 2
    assert rows[0]["Repository"] == "cpython"
    assert rows[1]["Repository"] == "requests"
    

