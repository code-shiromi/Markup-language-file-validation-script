import sys
from functions import (
    validate_json,
    validate_yaml,
    validate_xml,
    validate_toml,
    validate_csv,
    validate_ini
)

def validate_file(file_path, file_type):
    validators = {
        'json': validate_json,
        'yaml': validate_yaml,
        'xml': validate_xml,
        'toml': validate_toml,
        'csv': validate_csv,
        'ini': validate_ini
    }
    
    if file_type in validators:
        validators[file_type](file_path)
    else:
        print(f"Unsupported file type: {file_type}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate.py [file_path] [file_type]")
        sys.exit(1)
    
    file_path, file_type = sys.argv[1], sys.argv[2]
    validate_file(file_path, file_type)