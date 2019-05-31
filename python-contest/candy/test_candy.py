import unittest
from candy import get_num

class TestCandy(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_num(3, [4,5,6,4]), 3)
        self.assertEqual(get_num(3, [1,1,1]), 1)
        self.assertEqual(get_num(2, [4,5,6,4]), 4)

unittest.main()
