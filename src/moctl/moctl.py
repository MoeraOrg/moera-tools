import argparse
import os.path
import sys
from configparser import ConfigParser
from importlib.metadata import version
from time import strftime, localtime
from typing import Callable, cast
from urllib.parse import urlparse

from moeralib.node import MoeraNode, MoeraNodeError, MoeraNodeConnectionError
from moeralib.node.types import Timestamp, DomainAttributes, DomainInfo

PROGRAM_NAME = 'moctl'


class GlobalArgs:
    host_url: str | None
    root_secret: str | None
    token: str | None
    routine: Callable[[], None]
    domain: str


config: ConfigParser
args: GlobalArgs


def error(s: str) -> None:
    print('%s: error: %s' % (PROGRAM_NAME, s), file=sys.stderr)
    sys.exit(1)


def parse_config() -> None:
    global config

    config = ConfigParser(default_section='general')
    config.read(os.path.expanduser("~/.moerc"))


def parse_args() -> None:
    global args

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Moera server management.')
    parser.set_defaults(routine=lambda: routine_help(parser))
    program_version = '%s (moera-tools) %s' % (PROGRAM_NAME, version('moera-tools'))
    parser.add_argument('-H', '--host', dest='host_url', default=config.get('general', 'host', fallback=None),
                        help='host URL')
    parser.add_argument('-S', '--root-secret', dest='root_secret', default=None, help='root admin secret')
    parser.add_argument('-T', '--token', dest='token', default=None, help='admin token')
    parser.add_argument('-V', '--version', action='version', version=program_version)
    subparsers = parser.add_subparsers(title='subcommands', required=True)

    parser_domain = subparsers.add_parser(
        'domain', aliases=['dom'], description='Managing domains.', help='manage domains')
    parser_domain.set_defaults(routine=lambda: routine_help(parser_domain))
    subparsers_domain = parser_domain.add_subparsers(title='operations', required=True)

    parser_domain_list = subparsers_domain.add_parser(
        'list', description='List all domains.', help='list all domains')
    parser_domain_list.set_defaults(routine=domain_list)

    parser_domain_get = subparsers_domain.add_parser(
        'get', description='Show domain info.', help='show domain info')
    parser_domain_get.set_defaults(routine=domain_get)
    parser_domain_get.add_argument('domain', metavar='<domain>', nargs='?', default=None, help='domain name')

    parser_domain_create = subparsers_domain.add_parser(
        'create', description='Create a domain.', help='create a domain')
    parser_domain_create.set_defaults(routine=domain_create)
    parser_domain_create.add_argument('domain', metavar='<domain>', help='domain name')

    parser_domain_delete = subparsers_domain.add_parser(
        'delete', description='Delete a domain.', help='delete a domain')
    parser_domain_delete.set_defaults(routine=domain_delete)
    parser_domain_delete.add_argument('domain', metavar='<domain>', help='domain name')

    args = cast(GlobalArgs, parser.parse_args())

    if args.host_url is None:
        error('host is not set')


def routine_help(parser: argparse.ArgumentParser) -> None:
    parser.print_usage()
    sys.exit(1)


def parameter_for(url: str, param_name: str) -> str | None:
    netloc = urlparse(url).netloc
    for suffix in config.sections():
        if netloc.endswith(suffix) and param_name in config[suffix]:
            return config[suffix][param_name]
    return None


def root_secret_for(url: str) -> str | None:
    if args.root_secret is not None:
        return args.root_secret
    return parameter_for(url, 'secret')


def setup_root_admin_auth(node: MoeraNode) -> None:
    root_secret = root_secret_for(node.root)
    if root_secret is None:
        error('Root admin secret (-S, --root-secret) should be set')
        sys.exit(1)
    node.root_secret(root_secret)
    node.auth_root_admin()


def token_for(url: str) -> str | None:
    if args.token is not None:
        return args.token
    return parameter_for(url, 'token')


def setup_admin_auth(node: MoeraNode) -> None:
    token = token_for(node.root)
    if token is not None:
        node.token(token)
        node.auth_admin()
    else:
        root_secret = root_secret_for(node.root)
        if root_secret is not None:
            node.root_secret(root_secret)
            node.auth_root_admin()
        else:
            error('Admin token (-T, --token) or root admin secret (-S, --root-secret) should be set')
            sys.exit(1)


def timestamp_to_str(ts: Timestamp) -> str:
    return strftime("%Y-%m-%d %H:%M:%S", localtime(ts))


def hostname(url: str) -> str:
    return urlparse(url).netloc.split(':')[0]


def print_domain(domain: DomainInfo) -> None:
    print(f'node ID:\t{domain.node_id}')
    print(f'domain name:\t{domain.name}')
    print(f'created at:\t{timestamp_to_str(domain.created_at)}')


def domain_get() -> None:
    node = MoeraNode()
    node.node_url(args.host_url)
    domain_name = args.domain if args.domain is not None else hostname(node.root)
    print_domain(node.get_domain(domain_name))


def domain_list() -> None:
    node = MoeraNode()
    node.node_url(args.host_url)
    setup_root_admin_auth(node)
    domains = node.get_domains()
    for domain in domains:
        print(f'{domain.name}\t{timestamp_to_str(domain.created_at)}')


def domain_create() -> None:
    node = MoeraNode()
    node.node_url(args.host_url)
    if args.root_secret is not None:
        setup_root_admin_auth(node)
    attrs = DomainAttributes()
    attrs.name = args.domain
    print_domain(node.create_domain(attrs))


def domain_delete() -> None:
    node = MoeraNode()
    node.node_url(args.host_url)
    setup_root_admin_auth(node)
    node.delete_domain(args.domain)


def moctl() -> None:
    try:
        parse_config()
        parse_args()
        args.routine()
    except (MoeraNodeConnectionError, MoeraNodeError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
