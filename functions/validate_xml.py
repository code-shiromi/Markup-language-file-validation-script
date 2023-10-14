import xml.etree.ElementTree as ET

def validate_xml(file_path):
    try:
        ET.parse(file_path)
        print("XML file is valid.")
    except ET.ParseError as e:
        print(f"Invalid XML file: {e}")