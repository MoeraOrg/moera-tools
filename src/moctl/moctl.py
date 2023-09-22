import argparse
import os.path
import sys
from configparser import ConfigParser
from importlib.metadata import version
from time import strftime, localtime
from typing import Callable, cast, NoReturn
from urllib.parse import urlparse

from moeralib import naming
from moeralib.naming import MoeraNaming, node_name_parse
from moeralib.node import MoeraNode, MoeraNodeError, MoeraNodeConnectionError
from moeralib.node.types import Timestamp, DomainAttributes, DomainInfo, Credentials, ProfileAttributes, NameToRegister, \
    RegisteredNameSecret

PROGRAM_NAME = 'moctl'


class GlobalArgs:
    naming_server: str
    host_url: str | None
    host_name: str | None
    root_secret: str | None
    token: str | None
    routine: Callable[[MoeraNode], None]
    domain: str
    password: str
    email: str
    node_name: str


config: ConfigParser
args: GlobalArgs


def error(s: str) -> NoReturn:
    print('%s: error: %s' % (PROGRAM_NAME, s), file=sys.stderr)
    sys.exit(1)


def parse_config() -> None:
    global config

    config = ConfigParser(default_section='general')
    config.read(os.path.expanduser("~/.moerc"))


def parse_args() -> None:
    global args

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Moera server management.')
    parser.set_defaults(routine=lambda: routine_help(parser),
                        naming_server=config.get('general', 'naming-server', fallback=naming.MAIN_SERVER))
    program_version = '%s (moera-tools) %s' % (PROGRAM_NAME, version('moera-tools'))
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-d', '--dev', action='store_const', dest='naming_server', const=naming.DEV_SERVER,
                        help='use the development naming server')
    group.add_argument('-H', '--host', dest='host_url', metavar='URL',
                       default=config.get('general', 'host', fallback=None), help='node hostname/URL')
    group.add_argument('-N', '--name', dest='host_name', metavar='NAME',
                       default=config.get('general', 'name', fallback=None), help='node name')
    parser.add_argument('-s', '--naming-server', dest='naming_server', metavar='URL', help='naming server URL')
    parser.add_argument('-S', '--root-secret', dest='root_secret', metavar='SECRET', default=None,
                        help='root admin secret')
    parser.add_argument('-T', '--token', dest='token', default=None, help='admin token')
    parser.add_argument('-V', '--version', action='version', version=program_version)
    subparsers = parser.add_subparsers(title='subcommands', required=True)

    # domain

    parser_domain = subparsers.add_parser(
        'domain', aliases=['dom'], description='Managing domains.', help='manage domains')
    parser_domain.set_defaults(routine=lambda: routine_help(parser_domain))
    subparsers_domain = parser_domain.add_subparsers(title='operations', required=True)

    parser_domain_list = subparsers_domain.add_parser(
        'list', description='List all domains.', help='list all domains')
    parser_domain_list.set_defaults(routine=domain_list)

    parser_domain_show = subparsers_domain.add_parser(
        'show', description='Show domain info.', help='show domain info')
    parser_domain_show.set_defaults(routine=domain_show)

    parser_domain_create = subparsers_domain.add_parser(
        'create', description='Create a domain.', help='create a domain')
    parser_domain_create.set_defaults(routine=domain_create)
    parser_domain_create.add_argument('domain', metavar='DOMAIN', help='domain name')

    parser_domain_delete = subparsers_domain.add_parser(
        'delete', description='Delete a domain.', help='delete a domain')
    parser_domain_delete.set_defaults(routine=domain_delete)
    parser_domain_delete.add_argument('domain', metavar='DOMAIN', help='domain name')

    # credentials

    parser_credentials = subparsers.add_parser(
        'credentials', aliases=['cr'], description='Managing credentials.', help='manage credentials')
    parser_credentials.set_defaults(routine=lambda: routine_help(parser_credentials))
    subparsers_credentials = parser_credentials.add_subparsers(title='operations', required=True)

    parser_credentials_check = subparsers_credentials.add_parser(
        'check', description='Check credentials.', help='check credentials')
    parser_credentials_check.set_defaults(routine=credentials_check)

    parser_credentials_set_password = subparsers_credentials.add_parser(
        'set-password', description='Set password.', help='set password')
    parser_credentials_set_password.set_defaults(routine=credentials_set_password)
    parser_credentials_set_password.add_argument('password', metavar='PASSWORD', help='password to set')

    parser_credentials_delete = subparsers_credentials.add_parser(
        'delete', description='Delete credentials.', help='delete credentials')
    parser_credentials_delete.set_defaults(routine=credentials_delete)

    parser_credentials_get_email = subparsers_credentials.add_parser(
        'get-email', description='Get e-mail address.', help='get e-mail address')
    parser_credentials_get_email.set_defaults(routine=credentials_get_email)

    parser_credentials_set_email = subparsers_credentials.add_parser(
        'set-email', description='Set e-mail address.', help='set e-mail address')
    parser_credentials_set_email.set_defaults(routine=credentials_set_email)
    parser_credentials_set_email.add_argument('email', metavar='ADDRESS', help='e-mail address to set')

    # name

    parser_name = subparsers.add_parser(
        'name', aliases=['nm'], description='Managing node name.', help='manage node name')
    parser_name.set_defaults(routine=lambda: routine_help(parser_name))
    subparsers_name = parser_name.add_subparsers(title='operations', required=True)

    parser_name_show = subparsers_name.add_parser(
        'show', description='Show node name.', help='show node name')
    parser_name_show.set_defaults(routine=name_show)

    parser_name_status = subparsers_name.add_parser(
        'status', description='Show node name operation status.', help='show node name operation status')
    parser_name_status.set_defaults(routine=name_status)

    parser_name_register = subparsers_name.add_parser(
        'register', aliases=['reg'], description='Register node name.', help='register node name')
    parser_name_register.set_defaults(routine=name_register)
    parser_name_register.add_argument('node_name', metavar='NAME', help='name to register')

    parser_name_assign = subparsers_name.add_parser(
        'assign', aliases=['reg'], description='Assign an existing node name.', help='assign an existing node name')
    parser_name_assign.set_defaults(routine=name_assign)
    parser_name_assign.add_argument('node_name', metavar='NAME', help='name to assign')

    parser_name_delete = subparsers_name.add_parser(
        'delete', description='Delete node name information.', help='delete node name information')
    parser_name_delete.set_defaults(routine=name_delete)

    args = cast(GlobalArgs, parser.parse_args())

    if args.host_name is not None:
        resolve_host_name()
    if args.host_url is None:
        error('host is not set')


def routine_help(parser: argparse.ArgumentParser) -> None:
    parser.print_usage()
    sys.exit(1)


def resolve_host_name() -> None:
    try:
        (name, gen) = node_name_parse(args.host_name)
    except ValueError as e:
        error(str(e))
    naming = MoeraNaming(args.naming_server)
    info = naming.get_current(name, gen)
    if info is None:
        error(f'Node name not found: {args.host_name}')
    args.host_url = info.node_uri


def run() -> None:
    node = MoeraNode()
    node.node_url(args.host_url)
    args.routine(node)


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


def setup_root_admin_auth(node: MoeraNode, optional: bool = False) -> None:
    root_secret = root_secret_for(node.root)
    if root_secret is None:
        if optional:
            return
        error('Root admin secret (-S, --root-secret) should be set')
    node.root_secret(root_secret)
    node.auth_root_admin()


def token_for(url: str) -> str | None:
    if args.token is not None:
        return args.token
    return parameter_for(url, 'token')


def setup_admin_auth(node: MoeraNode, optional: bool = False) -> None:
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
            if optional:
                return
            error('Admin token (-T, --token) or root admin secret (-S, --root-secret) should be set')


def timestamp_to_str(ts: Timestamp) -> str:
    return strftime('%Y-%m-%d %H:%M:%S', localtime(ts))


def print_domain(domain: DomainInfo) -> None:
    print(f'node ID:\t{domain.node_id}')
    print(f'domain name:\t{domain.name}')
    print(f'created at:\t{timestamp_to_str(domain.created_at)}')


def domain_show(node: MoeraNode) -> None:
    setup_root_admin_auth(node, optional=True)
    domain_name = urlparse(node.root).netloc.split(':')[0]
    print_domain(node.get_domain(domain_name))


def domain_list(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    domains = node.get_domains()
    for domain in domains:
        print(f'{domain.node_id}\t{domain.name}\t{timestamp_to_str(domain.created_at)}')


def domain_create(node: MoeraNode) -> None:
    setup_root_admin_auth(node, optional=True)
    attrs = DomainAttributes()
    attrs.name = args.domain
    print_domain(node.create_domain(attrs))


def domain_delete(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    node.delete_domain(args.domain)


def credentials_check(node: MoeraNode) -> None:
    info = node.check_credentials()
    if info.created:
        print('Credentials are set')
    else:
        print('Credentials are NOT set')


def credentials_set_password(node: MoeraNode) -> None:
    credentials = Credentials()
    credentials.login = 'admin'
    credentials.password = args.password
    node.create_credentials(credentials)


def credentials_delete(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    node.delete_credentials()


def credentials_get_email(node: MoeraNode) -> None:
    setup_admin_auth(node, optional=True)
    profile = node.get_profile()
    if profile.email is not None:
        print(profile.email)


def credentials_set_email(node: MoeraNode) -> None:
    setup_admin_auth(node)
    profile = ProfileAttributes()
    profile.email = args.email
    node.update_profile(profile)


def name_show(node: MoeraNode) -> None:
    info = node.get_node_name()
    if info.name is not None:
        print(info.name)


def name_status(node: MoeraNode) -> None:
    setup_admin_auth(node)
    info = node.get_node_name()
    if info.name is not None:
        print(f'name:\t{info.name}')
    if info.operation_status is not None:
        status = f'status: {info.operation_status}'
        if info.operation_status_updated is not None:
            status += f' ({timestamp_to_str(info.operation_status_updated)})'
        print(status)
    if info.operation_error_code is not None:
        print(f'error: {info.operation_error_message} ({info.operation_error_code})')


def name_register(node: MoeraNode) -> None:
    setup_admin_auth(node)
    reg = NameToRegister()
    reg.name = args.node_name
    info = node.create_node_name(reg)
    if info.mnemonic is not None:
        i = 1
        for word in info.mnemonic:
            print(f'{i:2}. {word}')
            i += 1


def name_assign(node: MoeraNode) -> None:
    setup_admin_auth(node)
    secret = RegisteredNameSecret()
    secret.name = args.node_name
    secret.mnemonic = []
    if sys.stdin.isatty():
        print('Enter 24 secret words:')
    for n in range(24):
        try:
            secret.mnemonic.append(input())
        except EOFError:
            break
    if len(secret.mnemonic) != 24:
        error('Wrong secret words')
    node.update_node_name(secret)


def name_delete(node: MoeraNode) -> None:
    setup_admin_auth(node)
    node.delete_node_name()


# TODO manage tokens, manage settings, posting (?)


def moctl() -> None:
    try:
        parse_config()
        parse_args()
        run()
    except (MoeraNodeConnectionError, MoeraNodeError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
