import unittest
from codes.main_cls import Calc


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUp')
        a = 4
        b = 2
        cls.calc1 = Calc(a, b)

        a = 4
        b = 4
        cls.calc2 = Calc(a, b)

        a = 4
        b = 0
        cls.calc3 = Calc(a, b)
        

    def test_add(self):
        print('test_add')
        expected_result = 6
        actual_result = self.calc1.add()
        self.assertEqual(expected_result, actual_result)

    def test_add2(self):
        print('test_add2')
        expected_result = 8
        actual_result = self.calc2.add()
        self.assertEqual(expected_result, actual_result)

    def test_divide_with_valid_data(self):
        print('test_divide_with_valid_data')
        expected_result = 2
        actual_result = self.calc1.divide()
        self.assertEqual(expected_result, actual_result)
    
    def test_divide_with_raise_error(self):
        print('test_divide_with_raise_error')
        self.assertRaises(ZeroDivisionError, self.calc3.divide)

    @classmethod
    def tearDownClass(cls):
        print('tearDown')
        del cls.calc1
        del cls.calc2
        del cls.calc3

# class TestCalc(unittest.TestCase):

#     def test_add(self):
#         a = 4
#         b = 3
#         calc = Calc(a, b)
#         expected_result = 7
#         actual_result = calc.add()
#         self.assertEqual(expected_result, actual_result)

#     def test_add2(self):
#         a = 4
#         b = 4
#         calc = Calc(a, b)
#         expected_result = 8
#         actual_result = calc.add()
#         self.assertEqual(expected_result, actual_result)

#     def test_divide_with_valid_data(self):
#         a = 4
#         b = 2
#         calc = Calc(a, b)
#         expected_result = 2
#         actual_result = calc.divide()
#         self.assertEqual(expected_result, actual_result)
    
#     def test_divide_with_raise_error(self):
#         a = 4
#         b = 0
#         calc = Calc(a, b)
#         self.assertRaises(ZeroDivisionError, calc.divide)


# if __name__ == '__main__':
#     unittest.main()