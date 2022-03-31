import argparse
import textwrap
from .lib import report_row


def rightofway_cli() -> argparse.ArgumentParser:
    rightofway = argparse.ArgumentParser(
        prog='Right of Way',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            print the state of the parties,
            or execute sub commands to manage the parties
            or execute sub commands to return right-of-way:
                bat rightofway {sub command}
        '''),
    )
    
    ## set default to show help fx if no args given
    rightofway.set_defaults(func=Commands.default)
    
    # Required arguments
    rightofway.add_argument(
        dest='party_a',
        default=0,
        help='Number of members in party A',
    )

    rightofway.add_argument(
        dest='party_b',
        default=0,
        help='Number of members in party B',
    )

    # Add additional sub-commands to this cli
    commands = rightofway.add_subparsers(
        dest='rightofway.cmds',
        title='rightofway commands',
        description='for additonal details on each command use: '
        '"bat rightofway x {command name} --help"',
    )

    report = commands.add_parser(
        'report',
        help='some kind of help should be here...',
        description='reports which group has right of way',
    )

    report.set_defaults(func=Commands.report)
    
    return rightofway
    
class Commands:

    @staticmethod
    def default(_) -> None:
        print('here is your help stuff')
    
    
    @staticmethod
    def report(conf) -> None:
        A = conf.party_a
        B = conf.party_b
        print(report_row(A, B))
        # print(conf.__dict__)