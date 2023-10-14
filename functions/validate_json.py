import json

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        print("JSON file is valid.")
    except ValueError as e:
        print(f"Invalid JSON file: {e}")