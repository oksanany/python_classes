import unittest

from task5 import *


class TestHourIncome(unittest.TestCase):

    def test_get_hour_income(self):
        service = HourIncome('test_input.json')
        result = service.get_hour_income()['hour_income']
        variants = ["{:.2f}".format(200000/8/i) for i in range(20,24)]
        self.assertIn(result, variants)

if __name__ == "__main__":
  unittest.main()
