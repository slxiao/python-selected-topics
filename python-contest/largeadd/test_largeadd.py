import unittest
from largeadd import large_sum

class TestLargeAdd(unittest.TestCase):
    def test_1(self):
        a, b = '9876543210','1234567890'
        self.assertEqual(large_sum(a, b), '11111111100')

    def test_2(self):
        a, b = '-9876543210','-1234567890'
        self.assertEqual(large_sum(a, b), '-11111111100')

    def test_3(self):
        a, b = '-19','-92'
        self.assertEqual(large_sum(a, b), '-111')

    def test_4(self):
        a, b = '-19','92'
        self.assertEqual(large_sum(a, b), '73')

    def test_5(self):
        a, b = '19','-92'
        self.assertEqual(large_sum(a, b), '-73')

    def test_6(self):
        a, b = '-100000','99999'
        self.assertEqual(large_sum(a, b), '-1')


unittest.main()
