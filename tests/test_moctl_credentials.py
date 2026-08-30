import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import moctl.moctl as cli
from moeralib.node.types import CredentialsCreated


def credentials_created(created: bool, login_disabled: bool | None = None) -> CredentialsCreated:
    info = CredentialsCreated()
    info.created = created
    info.login_disabled = login_disabled
    return info


class RecordingNode:
    def __init__(self, info: CredentialsCreated | None = None) -> None:
        self.info = info
        self.credentials = None

    def check_credentials(self) -> CredentialsCreated:
        return self.info

    def create_credentials(self, credentials) -> None:
        self.credentials = credentials


class CredentialsCommandTest(unittest.TestCase):
    def test_disable_login_subcommand_is_registered(self) -> None:
        with patch.object(
            sys, 'argv', ['moctl', '-H', 'https://mynode', 'credentials', 'disable-login']
        ), patch.object(cli, 'configure_provider'):
            cli.parse_args()

        self.assertIs(cli.args.routine, cli.credentials_disable_login)

    def test_disable_login_creates_credentials_with_only_disabled_flag(self) -> None:
        node = RecordingNode()

        cli.credentials_disable_login(node)

        self.assertTrue(node.credentials.login_disabled)
        self.assertIsNone(node.credentials.login)
        self.assertIsNone(node.credentials.password)

    def test_check_reports_disabled_login(self) -> None:
        node = RecordingNode(credentials_created(True, True))

        output = io.StringIO()
        with redirect_stdout(output):
            cli.credentials_check(node)

        self.assertEqual(output.getvalue(), 'Login is disabled\n')


if __name__ == '__main__':
    unittest.main()
