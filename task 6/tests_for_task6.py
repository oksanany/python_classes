import unittest

from task6 import Complex


class TestComplex(unittest.TestCase):

    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)

    def test_equal_img(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertNotEqual(first, second)

    def test_print(self):
        num = Complex(1,5)
        self.assertEqual(num.__str__(), '1 + 5i')

    def test_print_negative_imaginary(self):
        num = Complex(1, -5)
        self.assertEqual(num.__str__(), '1 - 5i')

    def test_print_no_real(self):
        num = Complex(0, -5)
        self.assertEqual(num.__str__(), '-5i')

    def test_print_real(self):
        num = Complex(-1, 0)
        self.assertEqual(num.__str__(), '-1')

    def test_sum(self):
        first = Complex(-1, 2)
        second = Complex(2, -1)
        third = first + second
        self.assertEqual(third.__str__(), '1 + i')

    def test_sum_to_zero(self):
        first = Complex(-1, 2)
        second = Complex(1, -2)
        third = first + second
        self.assertEqual(third.__str__(), '0')

    def test_subtract(self):
        first = Complex(-1, 2)
        second = Complex(1, -2)
        third = first - second
        self.assertEqual(third.__str__(), '-2 + 4i')

    def test_subtract_to_no_real(self):
        first = Complex(1, 2)
        second = Complex(1, 8)
        third = first - second
        self.assertEqual(third.__str__(), '-6i')

    def test_multiply_no_real(self):
        first = Complex(-1, 2)
        second = Complex(2, -1)
        third = first*second
        self.assertEqual(third.__str__(), '5i')

    def test_multiply(self):
        first = Complex(1, 2)
        second = Complex(2, 3)
        third = first*second
        self.assertEqual(third.__str__(), '-4 + 7i')

    def test_multiply_by_zero(self):
        first = Complex(-1, 2)
        second = Complex(0, -0)
        third = first*second
        self.assertEqual(third.__str__(), '0')

    def test_abs_zero(self):
        num = Complex(0,0)
        self.assertEqual(abs(num), 0.0)

    def test_abs_int(self):
        num = Complex(-4, 3)
        self.assertEqual(abs(num), 5.0)

    def test_abs(self):
        num = Complex(-1, 2)
        self.assertEqual(abs(num), 2.24)









if __name__ == "__main__":
    unittest.main()