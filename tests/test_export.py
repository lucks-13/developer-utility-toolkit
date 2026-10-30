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

    