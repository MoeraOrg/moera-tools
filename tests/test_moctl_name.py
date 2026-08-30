import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import moctl.moctl as cli
from moeralib.node import MoeraNodeError
from moeralib.node.types import KeyMnemonic, NameToRegister, RegisteredNameSecret


class RecordingNode:
    def __init__(self, words: list[str], store_error: Exception | None = None) -> None:
        self.words = words
        self.store_error = store_error
        self.admin_authenticated = False
        self.registered_name = None
        self.stored_mnemonic = None
        self.stored_mnemonic_requested = False
        self.stored_mnemonic_deleted = False

    def token(self, token: str) -> None:
        pass

    def auth_admin(self) -> None:
        self.admin_authenticated = True

    def create_node_name(self, name: NameToRegister) -> RegisteredNameSecret:
        self.registered_name = name.name
        info = RegisteredNameSecret()
        info.name = name.name
        info.mnemonic = self.words
        return info

    def store_mnemonic(self, mnemonic: KeyMnemonic) -> None:
        self.stored_mnemonic = mnemonic
        if self.store_error is not None:
            raise self.store_error

    def get_stored_mnemonic(self) -> KeyMnemonic:
        self.stored_mnemonic_requested = True
        mnemonic = KeyMnemonic()
        mnemonic.mnemonic = self.words
        return mnemonic

    def delete_stored_mnemonic(self) -> None:
        self.stored_mnemonic_deleted = True


class NameCommandTest(unittest.TestCase):
    def test_word_management_subcommands_are_registered(self) -> None:
        cases = [
            ('show-words', 'name_show_words'),
            ('delete-words', 'name_delete_words'),
        ]

        for command, routine_name in cases:
            with self.subTest(command=command), patch.object(
                sys, 'argv', ['moctl', '-H', 'https://mynode', 'name', command]
            ), patch.object(cli, 'configure_provider'), redirect_stderr(io.StringIO()):
                try:
                    cli.parse_args()
                except SystemExit:
                    accepted = False
                else:
                    accepted = True

            self.assertTrue(accepted, f'name {command} subcommand was not accepted')
            self.assertEqual(cli.args.routine.__name__, routine_name)

    def test_register_parser_accepts_store_words_options(self) -> None:
        cases = [
            ([], False),
            (['-w'], True),
            (['--store-words'], True),
        ]

        for options, expected in cases:
            with self.subTest(options=options), patch.object(
                sys, 'argv', ['moctl', '-H', 'https://mynode', 'name', 'register', *options, 'thatnode']
            ), patch.object(cli, 'configure_provider'), redirect_stderr(io.StringIO()):
                cli.parse_args()

            self.assertIs(getattr(cli.args, 'store_words', None), expected)

    def test_show_words_prints_stored_mnemonic(self) -> None:
        cli.args = SimpleNamespace(token='admin-token', root_secret=None)
        node = RecordingNode(['alpha', 'bravo'])

        output = io.StringIO()
        with redirect_stdout(output):
            cli.name_show_words(node)

        self.assertTrue(node.admin_authenticated)
        self.assertTrue(node.stored_mnemonic_requested)
        self.assertEqual(output.getvalue(), ' 1. alpha\n 2. bravo\n')

    def test_delete_words_deletes_stored_mnemonic_without_output(self) -> None:
        cli.args = SimpleNamespace(token='admin-token', root_secret=None)
        node = RecordingNode([])

        output = io.StringIO()
        with redirect_stdout(output):
            cli.name_delete_words(node)

        self.assertTrue(node.admin_authenticated)
        self.assertTrue(node.stored_mnemonic_deleted)
        self.assertEqual(output.getvalue(), '')

    def test_register_stores_words_without_printing_them(self) -> None:
        cli.args = SimpleNamespace(
            node_name='thatnode', store_words=True, token='admin-token', root_secret=None
        )
        node = RecordingNode(['alpha', 'bravo'])

        output = io.StringIO()
        with redirect_stdout(output):
            cli.name_register(node)

        self.assertEqual(node.registered_name, 'thatnode')
        self.assertIsNotNone(node.stored_mnemonic)
        self.assertEqual(node.stored_mnemonic.mnemonic, ['alpha', 'bravo'])
        self.assertEqual(output.getvalue(), '')

    def test_register_prints_words_without_store_option(self) -> None:
        cli.args = SimpleNamespace(
            node_name='thatnode', store_words=False, token='admin-token', root_secret=None
        )
        node = RecordingNode(['alpha', 'bravo'])

        output = io.StringIO()
        with redirect_stdout(output):
            cli.name_register(node)

        self.assertIsNone(node.stored_mnemonic)
        self.assertEqual(output.getvalue(), ' 1. alpha\n 2. bravo\n')

    def test_register_prints_words_when_storing_fails(self) -> None:
        cli.args = SimpleNamespace(
            node_name='thatnode', store_words=True, token='admin-token', root_secret=None
        )
        node = RecordingNode(['alpha', 'bravo'], MoeraNodeError('store_mnemonic', 'failed'))

        output = io.StringIO()
        with redirect_stdout(output), self.assertRaisesRegex(MoeraNodeError, 'failed'):
            cli.name_register(node)

        self.assertEqual(output.getvalue(), ' 1. alpha\n 2. bravo\n')


if __name__ == '__main__':
    unittest.main()
