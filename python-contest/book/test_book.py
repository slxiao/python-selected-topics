import unittest
from book import get_min_money

class TestBook(unittest.TestCase):
    def test(self):
        case = '11223345'
        self.assertEqual(get_min_money(case), 51.2)
        case = '1323'
        self.assertEqual(get_min_money(case), 29.6)
        case = '51323415545421541422444355251135224151524555515554452442333332413415431225335341'
        self.assertEqual(get_min_money(case), 504.0)

unittest.main()
