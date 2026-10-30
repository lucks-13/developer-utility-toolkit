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
        print(f"Error : {error}")
        return None
    
def export_csv(data, filename):
    if not data:
        print("No data is available to export.")
        return None
    try:
        os.makedirs("output", exist_ok=True)
        filepath = os.path.join("output", filename)
        if isinstance(data, dict):
            data = [data]

        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            print("Invalid data format, Unable to export CSV.")
            return None

        if not data:
            print("No data is available to export.")
            return None

        fieldnames = data[0].keys()
        with open(filepath, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully  exported to {filepath}. ")
        return filepath
    except OSError as error:
        print(f"Error : {error}")
        return None


