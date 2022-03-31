from unittest import TestCase
from unittest.mock import patch

from ..cli import (
    argparse,
    rightofway_cli,
    Commands,
)

SRC = 'bat.rightofway.cli'


class TestRightOfWayCli(TestCase):

    def test_rightofway_cli(t):
        rightofway_cli()
        
    def test_report(t):
        pass

class TestCommands(TestCase):
    @patch('builtins.print')
    @patch(f'{SRC}.report_row', autospec=True)
    def test_report(t, report_row, print):
        args = argparse.Namespace(party_a=2, party_b=9)
        Commands.report(args)
        print.assert_called_with(report_row.return_value)

