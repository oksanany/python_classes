import unittest

from task2_manual import *
from task2_import import *


class TestConverter(unittest.TestCase):

    def test_read_data_to_list(self):
        filename = 'input_missing_data.csv'
        answer = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,,200000,5\n', ',,,,']
        result = read_data_to_list(filename)
        self.assertEqual(answer, result)

    def test_to_json(self):
        data_manual = read_data_to_list('input.csv')
        data_import = read_csv_data('input.csv')
        converter = ManualCsvConverter(data_manual)
        result_manual = converter.to_json()
        result_import = ImportCsvConverter(data_import)
        self.assertEqual(result_import, result_manual)

    def test_to_json_with_empty_csv(self):
        data_manual = read_data_to_list('input_empty.csv')
        data_import = read_csv_data('input_empty.csv')
        converter = ManualCsvConverter(data_manual)
        result_manual = converter.to_json()
        result_import = ImportCsvConverter(data_import)
        self.assertEqual(result_import, result_manual)

    def test_to_json_with_missing_data(self):
        data_manual = read_data_to_list('input_missing_data.csv')
        data_import = read_csv_data('input_missing_data.csv')
        converter = ManualCsvConverter(data_manual)
        result_manual = converter.to_json()
        result_import = ImportCsvConverter(data_import)
        self.assertEqual(result_import, result_manual)

if __name__ == "__main__":
  unittest.main()



