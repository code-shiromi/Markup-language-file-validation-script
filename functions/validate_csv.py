import csv

def validate_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                item = {headers[i]: value for i, value in enumerate(row)}
        print("CSV file is valid.")
    except csv.Error as e:
        print(f"Invalid CSV file: {e}")