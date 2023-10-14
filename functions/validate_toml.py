import toml

def validate_toml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            toml.load(file)
        print("TOML file is valid.")
    except toml.TomlDecodeError as e:
        print(f"Invalid TOML file: {e}")