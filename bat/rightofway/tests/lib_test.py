from unittest import TestCase

from ..lib import report_row, ROW_MESSAGE


class LibTests(TestCase):

    def test_report_row(t):
        A = 3
        B = 4
        ret = report_row(A, B)
        t.assertEqual(ret, ROW_MESSAGE.format('B'))