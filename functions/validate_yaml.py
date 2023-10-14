import yaml

def validate_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            yaml.safe_load(file)
        print("YAML file is valid.")
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {e}")