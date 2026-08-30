import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import moctl.moctl as cli
from moeralib.node.types import ProfileAttributes, ProfileInfo


class RecordingNode:
    def __init__(self, full_name: str | None = None) -> None:
        self.full_name = full_name
        self.admin_authenticated = False
        self.updated_profile = None

    def token(self, token: str) -> None:
        pass

    def auth_admin(self) -> None:
        self.admin_authenticated = True

    def get_profile(self) -> ProfileInfo:
        profile = ProfileInfo()
        profile.full_name = self.full_name
        return profile

    def update_profile(self, profile: ProfileAttributes) -> None:
        self.updated_profile = profile


class ProfileCommandTest(unittest.TestCase):
    def test_profile_subcommands_are_registered(self) -> None:
        cases = [
            ('profile', ['get-full-name'], 'profile_get_full_name', None),
            ('profile', ['set-full-name', 'Alice Smith'], 'profile_set_full_name', 'Alice Smith'),
            ('pr', ['get-full-name'], 'profile_get_full_name', None),
        ]

        for object_name, arguments, routine_name, full_name in cases:
            with self.subTest(object_name=object_name, arguments=arguments), patch.object(
                sys, 'argv', ['moctl', '-H', 'https://mynode', object_name, *arguments]
            ), patch.object(cli, 'configure_provider'), redirect_stderr(io.StringIO()):
                try:
                    cli.parse_args()
                except SystemExit:
                    accepted = False
                else:
                    accepted = True

            self.assertTrue(accepted, f'profile {arguments[0]} subcommand was not accepted')
            self.assertEqual(cli.args.routine.__name__, routine_name)
            if full_name is not None:
                self.assertEqual(cli.args.full_name, full_name)

    def test_get_full_name_prints_profile_value(self) -> None:
        node = RecordingNode('Alice Smith')

        output = io.StringIO()
        with redirect_stdout(output):
            cli.profile_get_full_name(node)

        self.assertEqual(output.getvalue(), 'Alice Smith\n')

    def test_set_full_name_updates_only_profile_full_name(self) -> None:
        cli.args = SimpleNamespace(
            full_name='Alice Smith', token='admin-token', root_secret=None
        )
        node = RecordingNode()

        output = io.StringIO()
        with redirect_stdout(output):
            cli.profile_set_full_name(node)

        self.assertTrue(node.admin_authenticated)
        self.assertIsNotNone(node.updated_profile)
        self.assertEqual(node.updated_profile.full_name, 'Alice Smith')
        self.assertIsNone(node.updated_profile.email)
        self.assertEqual(output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
