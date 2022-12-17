def main(input):
    data = read_data_to_list(input)
    converter = ManualCsvConverter(data)
    result = converter.to_json()
    write_data('output.json', result)

def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

class ManualCsvConverter:

    def __init__(self, csv_data):
        if csv_data:
            self.title = csv_data[0]
            self.values = csv_data[1:]
        else:
            self.title = ''
            self.values = ''

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        return values

    def convert_row_to_json(self, data):
        values = []
        for key, value in data.items():
            if not value.isnumeric():
                value = '"{}"'.format(value)
            values.append("""  "{}": {}""".format(key, value))
        formatted_values = ",\n".join(['  "{}": "{}"'.format(key, value) for key, value in data.items()])
        pretty_line = """ {{\n{}\n }}""".format(formatted_values)
        return pretty_line

    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        if result:
            return "[\n{}\n]".format(",\n".join(result))
        else:
            return "[]"



if __name__ == "__main__":
    main('input_missing_data.csv')




