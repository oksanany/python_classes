import csv
import json
def read_csv_data(filename):
    data = []
    with open(filename, encoding='utf-8') as row:
        csv_data = csv.DictReader(row)
        for row in csv_data:
            data.append(row)
    return data

def write_data(result):
    with open('output2.json', 'w', encoding='utf-8') as file:
        file.write(result)


def ImportCsvConverter(csv_data):
    result = json.dumps(csv_data, indent=1)
    return result

def main(input):
    csv_data = read_csv_data(input)
    result = ImportCsvConverter(csv_data)
    write_data(result)

if __name__ == "__main__":
    main('input_missing_data.csv')
