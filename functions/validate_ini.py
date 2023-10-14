import configparser

def validate_ini(file_path):
    try:
        config = configparser.ConfigParser()
        config.read(file_path)
        print("INI file is valid.")
    except configparser.ParsingError as e:
        print(f"Invalid INI file: {e}")