import unittest
from codes.main import add, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        a = 4
        b = 3
        expected_result = 7
        actual_result = add(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_add2(self):
        a = 4
        b = 4
        expected_result = 8
        actual_result = add(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide_with_valid_data(self):
        a = 4
        b = 2
        expected_result = 2
        actual_result = divide(a, b)
        self.assertEqual(expected_result, actual_result)
    
    def test_divide_with_raise_error(self):
        a = 4
        b = 0
        self.assertRaises(ZeroDivisionError, divide, a, b)


# if __name__ == '__main__':
#     unittest.main()