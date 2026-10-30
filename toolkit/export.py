import json
import csv
import os

def export_json(data, filename):
    if not data:
        print("No data is available to export.")
        return None
    try:
        os.makedirs("output",exist_ok=True)
        filepath = os.path.join("output", filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully  exported to {filepath}. ")
        return filepath
    except OSError as error:
        
def export_csv(data, filename):
    if not data:
        print("No data is available to export.")
        return None
