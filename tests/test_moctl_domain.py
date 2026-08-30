import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import moctl.moctl as cli
from moeralib.node.types import DomainAvailable


class RecordingNode:
    def __init__(self, domain_name: str) -> None:
        self.domain_name = domain_name
        self.requested_node_name = None

    def is_domain_available(self, node_name: str) -> DomainAvailable:
        self.requested_node_name = node_name
        info = DomainAvailable()
        info.name = self.domain_name
        return info


class DomainCommandTest(unittest.TestCase):
    def test_available_subcommand_accepts_node_name(self) -> None:
        with patch.object(
            sys, 'argv', ['moctl', '-H', 'https://mynode', 'domain', 'available', 'thatnode']
        ), patch.object(cli, 'configure_provider'), redirect_stderr(io.StringIO()):
            try:
                cli.parse_args()
            except SystemExit:
                self.fail('domain available subcommand was not accepted')

        self.assertEqual(cli.args.node_name, 'thatnode')
        self.assertEqual(cli.args.routine.__name__, 'domain_available')

    def test_available_prints_recommended_domain_name(self) -> None:
        cli.args = SimpleNamespace(node_name='thatnode')
        node = RecordingNode('thatnode.example')

        output = io.StringIO()
        with redirect_stdout(output):
            cli.domain_available(node)

        self.assertEqual(node.requested_node_name, 'thatnode')
        self.assertEqual(output.getvalue(), 'thatnode.example\n')


if __name__ == '__main__':
    unittest.main()
