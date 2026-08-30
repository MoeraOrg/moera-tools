import argparse
import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import moctl.moctl as cli
from moeralib.node import MoeraNodeApiError
from moeralib.node.types import GrantInfo, Result


def grant_info(node_name: str, *scope: str) -> GrantInfo:
    info = GrantInfo()
    info.node_name = node_name
    info.scope = list(scope)
    return info


class RecordingNode:
    def __init__(self) -> None:
        self.admin_token = None
        self.admin_authenticated = False
        self.grants = [
            grant_info('alice_0', 'view-content', 'react'),
            grant_info('bob_1', 'view-profile'),
        ]
        self.requested_node_name = None
        self.change = None
        self.revoked_node_name = None

    def token(self, token: str) -> None:
        self.admin_token = token

    def auth_admin(self) -> None:
        self.admin_authenticated = True

    def get_all_grants(self) -> list[GrantInfo]:
        return self.grants

    def get_grant(self, node_name: str) -> GrantInfo:
        self.requested_node_name = node_name
        return grant_info(node_name, 'view-content', 'react')

    def grant_or_revoke(self, node_name: str, change):
        self.requested_node_name = node_name
        self.change = change
        return grant_info(node_name, *change.scope)

    def revoke_all(self, node_name: str) -> None:
        self.revoked_node_name = node_name


class MissingGrantNode(RecordingNode):
    def get_grant(self, node_name: str) -> GrantInfo:
        result = Result()
        result.error_code = 'not-found'
        result.message = 'Grant not found'
        raise MoeraNodeApiError('get_grant', result)


class GrantCommandTest(unittest.TestCase):
    def setUp(self) -> None:
        cli.args = SimpleNamespace(token='admin-token', root_secret=None)

    def test_parse_scopes_trims_spaces_around_comma_separated_values(self) -> None:
        self.assertEqual(cli.parse_scopes('view-content, react'), ['view-content', 'react'])

    def test_parse_scopes_rejects_space_separated_values(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            cli.parse_scopes('view-content react')

    def test_grant_subcommands_are_registered_with_expected_arguments(self) -> None:
        cases = [
            (['grant', 'list'], cli.grant_list, None, None),
            (['grant', 'show', 'thatnode'], cli.grant_show, 'thatnode', None),
            (['grant', 'grant', 'thatnode', 'view-content, react'], cli.grant_grant,
             'thatnode', ['view-content', 'react']),
            (['grant', 'revoke', 'thatnode', 'all'], cli.grant_revoke, 'thatnode', ['all']),
        ]

        for arguments, routine, node_name, scopes in cases:
            with self.subTest(arguments=arguments):
                with patch.object(sys, 'argv', ['moctl', '-H', 'https://mynode', *arguments]), \
                        patch.object(cli, 'configure_provider'):
                    cli.parse_args()
                self.assertIs(cli.args.routine, routine)
                if node_name is not None:
                    self.assertEqual(cli.args.node_name, node_name)
                if scopes is not None:
                    self.assertEqual(cli.args.scopes, scopes)

    def test_unquoted_space_after_comma_is_rejected_by_argument_parser(self) -> None:
        with patch.object(
            sys, 'argv', ['moctl', '-H', 'https://mynode', 'grant', 'grant', 'thatnode', 'view-content,', 'react']
        ), patch.object(cli, 'configure_provider'), redirect_stderr(io.StringIO()):
            with self.assertRaisesRegex(SystemExit, '2'):
                cli.parse_args()

    def test_grant_list_prints_every_grant(self) -> None:
        node = RecordingNode()

        output = io.StringIO()
        with redirect_stdout(output):
            cli.grant_list(node)

        self.assertEqual(output.getvalue(), 'alice_0\tview-content, react\nbob_1\tview-profile\n')
        self.assertTrue(node.admin_authenticated)

    def test_grant_show_expands_node_name_before_request(self) -> None:
        cli.args.node_name = 'thatnode'
        node = RecordingNode()

        output = io.StringIO()
        with redirect_stdout(output):
            cli.grant_show(node)

        self.assertEqual(node.requested_node_name, 'thatnode_0')
        self.assertEqual(output.getvalue(), 'thatnode_0\tview-content, react\n')

    def test_grant_show_prints_nothing_when_grant_does_not_exist(self) -> None:
        cli.args.node_name = 'thatnode'
        output = io.StringIO()

        with redirect_stdout(output):
            cli.grant_show(MissingGrantNode())

        self.assertEqual(output.getvalue(), '')

    def test_grant_show_reports_malformed_node_name_as_cli_error(self) -> None:
        cli.args.node_name = 'thatnode_bad'
        node = RecordingNode()
        output = io.StringIO()

        with redirect_stderr(output):
            with self.assertRaisesRegex(SystemExit, '1'):
                cli.grant_show(node)

        self.assertEqual(output.getvalue(), 'moctl: error: invalid generation: "bad"\n')
        self.assertIsNone(node.requested_node_name)

    def test_grant_grants_scopes_to_expanded_node_name(self) -> None:
        cli.args.node_name = 'thatnode'
        cli.args.scopes = ['view-content', 'react']
        node = RecordingNode()

        with redirect_stdout(io.StringIO()):
            cli.grant_grant(node)

        self.assertEqual(node.requested_node_name, 'thatnode_0')
        self.assertEqual(node.change.scope, ['view-content', 'react'])
        self.assertFalse(node.change.revoke)

    def test_grant_revoke_revokes_selected_scopes(self) -> None:
        cli.args.node_name = 'thatnode'
        cli.args.scopes = ['view-content', 'react']
        node = RecordingNode()

        with redirect_stdout(io.StringIO()):
            cli.grant_revoke(node)

        self.assertEqual(node.requested_node_name, 'thatnode_0')
        self.assertEqual(node.change.scope, ['view-content', 'react'])
        self.assertTrue(node.change.revoke)
        self.assertIsNone(node.revoked_node_name)

    def test_grant_revoke_all_uses_revoke_all_endpoint(self) -> None:
        cli.args.node_name = 'thatnode'
        cli.args.scopes = ['all']
        node = RecordingNode()

        cli.grant_revoke(node)

        self.assertEqual(node.revoked_node_name, 'thatnode_0')
        self.assertIsNone(node.change)


if __name__ == '__main__':
    unittest.main()
