import unittest
from longmen import get_result

class TestGetResult(unittest.TestCase):
    def test_1(self):
        m, n, t = 4, 4, 5
        case = '...L.*...*..Z..*'
        self.assertEqual(get_result(m, n, t, case), False)

    def test_2(self):
        m, n, t = 4, 3, 5
        case = '..L*..*..Z.*'
        self.assertEqual(get_result(m, n, t, case), True)

    def test_4(self):
        m, n, t = 1, 11, 10
        case = '..L*..*..Z.*'
        self.assertEqual(get_result(m, n, t, case), False)

    def test_3(self):
        m, n, t = 15, 17, 21
        case = '.*.*.*.*.*........*.*.*.*.*.***.**...*.........*....***.*****.******.*...*............*.*****.***.****Z......*.*........*.***********.**.*...*.......*....*.***.***.*.****.*.....*...*....L.***.*******.*.**...*.......*.*....*.***.***.*.****.*...*...*.*.....'
        self.assertEqual(get_result(m, n, t, case), False)

unittest.main()
