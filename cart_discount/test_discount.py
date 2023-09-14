import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_two_prices(self):
        prices = [20, 1]
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_min_item_is_duplicated(self):
        prices = [20, 4, 4, 15]
        expected_discount = 4
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_input_is_negative(self):
        prices = [-30, 8, 20]
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_invalid_input(self):
        prices = ['test', 15, 8]
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_float_lowest_input(self):
        prices = [5.5, 10, 20]
        expected_discount = 5.5
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_float_not_lowest_input(self):
        prices = [25.5, 10, 20]
        expected_discount = 10
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    def test_if_empty_list(self):
        prices = []
        expected_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)



if __name__ == '__main__':
    unittest.main()