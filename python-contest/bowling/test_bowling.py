import unittest
from bowling import get_bowling_score

class TestBlowing(unittest.TestCase):
    def test_1(self):
        pattern = 'X|X|X|X|X|X|X|X|X|X||XX'
        self.assertEqual(get_bowling_score(pattern), 300)

    def test_2(self):
        pattern = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
        self.assertEqual(get_bowling_score(pattern), 90)

    def test_3(self):
        pattern = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5'
        self.assertEqual(get_bowling_score(pattern), 150)

    def test_4(self):
        pattern = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
        self.assertEqual(get_bowling_score(pattern), 167)

    def test_5(self):
        pattern = '9/|9/|2/|61|31|X|8-|2/|5/|6/||-'
        self.assertEqual(get_bowling_score(pattern), 125)

if __name__ == '__main__':
    unittest.main()
