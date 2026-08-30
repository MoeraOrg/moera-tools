import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import moname.moname as cli
from moeralib.naming.types import RegisteredNameInfo


def registered_name(name: str, generation: int, node_uri: str) -> RegisteredNameInfo:
    info = RegisteredNameInfo()
    info.name = name
    info.generation = generation
    info.node_uri = node_uri
    return info


class PaginatedNaming:
    def __init__(self, pages: list[list[RegisteredNameInfo]] | None = None) -> None:
        self.requested_pages = []
        self.pages = pages if pages is not None else [
            [
                registered_name('alice', 0, 'https://alice.example/moera'),
                registered_name('alice', 2, 'https://alice-two.example/moera'),
            ],
            [
                registered_name('alex', 0, 'https://alex.example/moera'),
                registered_name('alla', 5, 'https://alla.example/moera'),
                registered_name('bob', 0, 'https://bob.example/moera'),
            ],
            [],
        ]

    def get_all(self, at: int, page: int, page_size: int) -> list[RegisteredNameInfo]:
        self.requested_pages.append(page)
        return self.pages[page]


class ListFilterTest(unittest.TestCase):
    def test_list_filter_matches_name_prefix_across_generations_and_downloads_every_page(self) -> None:
        cli.args = SimpleNamespace(
            server='https://naming.example/moera',
            at=123,
            newer=None,
            created=False,
            keys=None,
            name='al',
            generation=0,
            generation_specified=False,
            ignore_case=False,
        )
        service = PaginatedNaming()

        output = io.StringIO()
        with patch.object(cli.naming, 'MoeraNaming', new=lambda server: service), redirect_stdout(output):
            cli.scan()

        self.assertEqual(
            output.getvalue(),
            'alice_0\thttps://alice.example/moera\n'
            'alice_2\thttps://alice-two.example/moera\n'
            'alex_0\thttps://alex.example/moera\n'
            'alla_5\thttps://alla.example/moera\n',
        )
        self.assertEqual(service.requested_pages, [0, 1, 2])

    def test_list_filter_with_generation_matches_prefix_only_in_that_generation(self) -> None:
        cli.args = SimpleNamespace(
            server='https://naming.example/moera', at=123, newer=None, created=False, keys=None,
            name='al', generation=0, generation_specified=True, ignore_case=False,
        )
        service = PaginatedNaming()

        output = io.StringIO()
        with patch.object(cli.naming, 'MoeraNaming', new=lambda server: service), redirect_stdout(output):
            cli.scan()

        self.assertEqual(
            output.getvalue(),
            'alice_0\thttps://alice.example/moera\n'
            'alex_0\thttps://alex.example/moera\n',
        )

    def test_list_filter_can_ignore_case(self) -> None:
        cli.args = SimpleNamespace(
            server='https://naming.example/moera', at=123, newer=None, created=False, keys=None,
            name='al', generation=0, generation_specified=False, ignore_case=True,
        )
        service = PaginatedNaming([
            [
                registered_name('Alice', 0, 'https://alice.example/moera'),
                registered_name('ALex', 2, 'https://alex.example/moera'),
                registered_name('bob', 0, 'https://bob.example/moera'),
            ],
            [],
        ])

        output = io.StringIO()
        with patch.object(cli.naming, 'MoeraNaming', new=lambda server: service), redirect_stdout(output):
            cli.scan()

        self.assertEqual(
            output.getvalue(),
            'Alice_0\thttps://alice.example/moera\n'
            'ALex_2\thttps://alex.example/moera\n',
        )

    def test_list_parser_distinguishes_generation_suffix_and_accepts_ignore_case(self) -> None:
        parsed_args = cli.GlobalArgs()

        with patch.object(cli, 'args', parsed_args), \
                patch.object(sys, 'argv', ['moname', '--list', '--ignore-case', 'al_0']), \
                redirect_stderr(io.StringIO()):
            try:
                cli.parse_args()
            except SystemExit as e:
                self.fail(f'list filter arguments were rejected with exit code {e.code}')

        self.assertEqual(parsed_args.name, 'al')
        self.assertEqual(parsed_args.generation, 0)
        self.assertTrue(parsed_args.generation_specified)
        self.assertTrue(parsed_args.ignore_case)

    def test_list_parser_accepts_short_ignore_case_option(self) -> None:
        parsed_args = cli.GlobalArgs()

        with patch.object(cli, 'args', parsed_args), \
                patch.object(sys, 'argv', ['moname', '--list', '-i', 'al']), \
                redirect_stderr(io.StringIO()):
            try:
                cli.parse_args()
            except SystemExit as e:
                self.fail(f'short ignore-case option was rejected with exit code {e.code}')

        self.assertTrue(parsed_args.ignore_case)
        self.assertFalse(parsed_args.generation_specified)


if __name__ == '__main__':
    unittest.main()
