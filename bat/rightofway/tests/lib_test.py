from unittest import TestCase

from ..lib import report_row, ROW_MESSAGE


class LibTests(TestCase):

    def test_report_row(t):
        ret = report_row()
        t.assertEqual(ret, ROW_MESSAGE)
