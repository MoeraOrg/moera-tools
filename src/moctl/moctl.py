import argparse
import os.path
import sys
from configparser import ConfigParser
from importlib.metadata import version
from time import strftime, localtime
from typing import Callable, cast, NoReturn, Sequence, List
from urllib.parse import urlparse

from first import first
from moeralib import naming
from moeralib.node import MoeraNode, MoeraNodeError, MoeraNodeConnectionError, moera_root
from moeralib.node.types import (
    Timestamp, DomainAttributes, DomainInfo, Credentials, ProfileAttributes, NameToRegister, RegisteredNameSecret,
    TokenAttributes, TokenName, SettingMetaInfo, SettingInfo, SettingMetaAttributes
)

PROGRAM_NAME = 'moctl'


class GlobalArgs:
    naming_server: str
    provider: str | None
    host_url: str | None
    host_name: str | None
    root_secret: str | None
    token: str | None
    routine: Callable[[MoeraNode], None]
    domain: str
    password: str
    email: str
    node_name: str
    id: str
    token_name: str | None
    name: str
    description: bool
    defaults: bool
    modified: bool
    type: bool
    prefix: str | None
    value: str


config: ConfigParser
args: GlobalArgs


def error(s: str) -> NoReturn:
    print(f'{PROGRAM_NAME}: error: {s}', file=sys.stderr)
    sys.exit(1)


def resolve_host_name(naming_server: str) -> None:
    if args.host_name is None:
        error('Node name is not set')
    try:
        args.host_url = naming.resolve(args.host_name, naming_server)
        if args.host_url is None:
            error(f'Node name not found: {args.host_name}')
    except ValueError as e:
        error(str(e))


def naming_server_url(url: str | None) -> str:
    if url is None or url == 'main':
        return naming.MAIN_SERVER
    if url == 'dev' or url == 'development':
        return naming.DEV_SERVER
    return url


def configure_provider() -> None:
    global config

    config = ConfigParser(default_section='default')
    config.read(os.path.expanduser("~/.moerc"))

    if args.provider is None:
        if args.host_url is None and args.host_name is not None:
            if args.naming_server is not None:
                naming_server = args.naming_server
            else:
                naming_server = naming_server_url(config.get('default', 'naming-server', fallback=naming.MAIN_SERVER))
            resolve_host_name(naming_server)
        if args.host_url is not None:
            netloc = urlparse(moera_root(args.host_url)).netloc
            for provider in config.sections():
                if 'domain' in config[provider] and netloc.endswith(config[provider]['domain']):
                    args.provider = provider
                    break
    if args.provider is None:
        for provider in config.sections():
            if provider != 'default':
                args.provider = provider
                break
    if args.provider is None:
        return
    if args.provider not in config.sections():
        error("Provider is not found in the configuration file: " + args.provider)

    if args.naming_server is None:
        args.naming_server = naming_server_url(config[args.provider].get('naming-server', fallback=naming.MAIN_SERVER))
    if args.host_name is None:
        args.host_name = config[args.provider].get('node-name')
    if args.host_url is None:
        args.host_url = config[args.provider].get('node-url')
    if args.root_secret is None:
        args.root_secret = config[args.provider].get('secret')
    if args.token is None:
        args.token = config[args.provider].get('token')


def parse_args() -> None:
    global args

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Moera server management.')
    parser.set_defaults(routine=lambda: routine_help(parser))
    program_version = f'{PROGRAM_NAME} (moera-tools) {version("moera-tools")}'
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-d', '--dev', action='store_const', dest='naming_server', const=naming.DEV_SERVER,
                        help='use the development naming server')
    group.add_argument('-H', '--host', dest='host_url', metavar='URL', default=None, help='node hostname/URL')
    group.add_argument('-N', '--name', dest='host_name', metavar='NAME', default=None, help='node name')
    parser.add_argument('-s', '--naming-server', dest='naming_server', metavar='URL', help='naming server URL')
    parser.add_argument('-S', '--root-secret', dest='root_secret', metavar='SECRET', default=None,
                        help='root admin secret')
    parser.add_argument('-P', '--provider', dest='provider', default=None, help='use one of configured providers')
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
        'delete-password', aliases=['del-password'], description='Delete password.', help='delete password')
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
        'assign', description='Assign an existing node name.', help='assign an existing node name')
    parser_name_assign.set_defaults(routine=name_assign)
    parser_name_assign.add_argument('node_name', metavar='NAME', help='name to assign')

    parser_name_delete = subparsers_name.add_parser(
        'delete', description='Delete node name information.', help='delete node name information')
    parser_name_delete.set_defaults(routine=name_delete)

    # token

    parser_token = subparsers.add_parser(
        'token', aliases=['t'], description='Managing authentication tokens.', help='manage authentication tokens')
    parser_token.set_defaults(routine=lambda: routine_help(parser_token))
    subparsers_token = parser_token.add_subparsers(title='operations', required=True)

    parser_token_list = subparsers_token.add_parser(
        'list', description='List tokens available.', help='list tokens available')
    parser_token_list.set_defaults(routine=token_list)

    parser_token_show = subparsers_token.add_parser(
        'show', description='Show token details.', help='show token details')
    parser_token_show.set_defaults(routine=token_show)
    parser_token_show.add_argument('id', metavar='ID', help='token ID')

    parser_token_create = subparsers_token.add_parser(
        'create', description='Create a new token.', help='create a new token')
    parser_token_create.set_defaults(routine=token_create)
    parser_token_create.add_argument('password', metavar='PASSWORD', help='the current password for authentication')
    parser_token_create.add_argument('-n', '--token-name', dest='token_name', metavar='NAME', default=None,
                                     help='token name')

    parser_token_rename = subparsers_token.add_parser(
        'rename', description='Rename a token.', help='rename a token')
    parser_token_rename.set_defaults(routine=token_rename)
    parser_token_rename.add_argument('id', metavar='ID', help='token ID')
    parser_token_rename.add_argument('-n', '--token-name', dest='token_name', metavar='NAME', default=None,
                                     help='token name')

    parser_token_delete = subparsers_token.add_parser(
        'delete', description='Delete a token.', help='delete a token')
    parser_token_delete.set_defaults(routine=token_delete)
    parser_token_delete.add_argument('id', metavar='ID', help='token ID')

    # option

    parser_option = subparsers.add_parser(
        'option', aliases=['op'], description='Changing options.', help='change options')
    parser_option.set_defaults(routine=lambda: routine_help(parser_option))
    subparsers_option = parser_option.add_subparsers(title='operations', required=True)

    parser_option_show = subparsers_option.add_parser(
        'show', description='Display all options.', help='display all options')
    parser_option_show.set_defaults(routine=option_show)
    parser_option_show.add_argument('-d', '--description', dest='description', action='store_true',
                                    help='show option descriptions')
    parser_option_show.add_argument('--defaults', dest='defaults', action='store_true', help='show default values')
    parser_option_show.add_argument('-m', '--modified', dest='modified', action='store_true',
                                    help='show modified values only')
    parser_option_show.add_argument('--prefix', dest='prefix', default=None, help='filter by name prefix')
    parser_option_show.add_argument('-t', '--type', dest='type', action='store_true', help='show type information')

    parser_option_set = subparsers_option.add_parser(
        'set', description='Set an option.', help='set an option')
    parser_option_set.set_defaults(routine=option_set)
    parser_option_set.add_argument('name', metavar='NAME', help='option name')
    parser_option_set.add_argument('value', metavar='VALUE', help='option value')

    parser_option_reset = subparsers_option.add_parser(
        'reset', description='Reset an option to its default value.', help='reset an option to its default value')
    parser_option_reset.set_defaults(routine=option_reset)
    parser_option_reset.add_argument('name', metavar='NAME', help='option name')

    parser_option_set_default = subparsers_option.add_parser(
        'set-default', description='Set default value of an option.', help='set default value of an option')
    parser_option_set_default.set_defaults(routine=option_set_default)
    parser_option_set_default.add_argument('name', metavar='NAME', help='option name')
    parser_option_set_default.add_argument('value', metavar='VALUE', help='option value')

    parser_option_reset_default = subparsers_option.add_parser(
        'reset-default', description='Reset default value of an option to its built-in value.',
        help='reset default value of an option to its built-in value')
    parser_option_reset_default.set_defaults(routine=option_reset_default)
    parser_option_reset_default.add_argument('name', metavar='NAME', help='option name')

    parser_option_set_privileged = subparsers_option.add_parser(
        'set-privileged', description='Make an option privileged.', help='make an option privileged')
    parser_option_set_privileged.set_defaults(routine=option_set_privileged)
    parser_option_set_privileged.add_argument('name', metavar='NAME', help='option name')

    parser_option_set_not_privileged = subparsers_option.add_parser(
        'set-not-privileged', description='Make an option not privileged.', help='make an option not privileged')
    parser_option_set_not_privileged.set_defaults(routine=option_set_not_privileged)
    parser_option_set_not_privileged.add_argument('name', metavar='NAME', help='option name')

    parser_option_reset_privileged = subparsers_option.add_parser(
        'reset-privileged', description='Reset privileged status of an option to its built-in value.',
        help='reset privileged status of an option to its built-in value')
    parser_option_reset_privileged.set_defaults(routine=option_reset_privileged)
    parser_option_reset_privileged.add_argument('name', metavar='NAME', help='option name')

    args = cast(GlobalArgs, parser.parse_args())

    configure_provider()

    if args.host_url is None and args.host_name is not None:
        resolve_host_name(args.naming_server)
    if args.host_url is None:
        error('host is not set')


def routine_help(parser: argparse.ArgumentParser) -> None:
    parser.print_usage()
    sys.exit(1)


def run() -> None:
    node = MoeraNode(args.host_url)
    args.routine(node)


def setup_root_admin_auth(node: MoeraNode, optional: bool = False) -> None:
    if args.root_secret is None:
        if optional:
            return
        error('Root admin secret (-S, --root-secret) should be set')
    node.root_secret(args.root_secret)
    node.auth_root_admin()


def setup_admin_auth(node: MoeraNode, optional: bool = False) -> None:
    if args.token is not None:
        node.token(args.token)
        node.auth_admin()
    else:
        if args.root_secret is not None:
            node.root_secret(args.root_secret)
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
    domain_name = cast(str, urlparse(node.root).netloc).split(':')[0]
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


def token_list(node: MoeraNode) -> None:
    setup_admin_auth(node)
    for info in node.get_tokens():
        title = info.name if info.name is not None else info.token
        line = f'{info.id}\t{title}'
        if info.plugin_name is not None:
            line += f'\t{info.plugin_name}'
        print(line)


def token_show(node: MoeraNode) -> None:
    setup_admin_auth(node)
    info = node.get_token_info(args.id)
    print(f'ID:\t{info.id}')
    print(f'token:\t{info.token}')
    if info.name is not None:
        print(f'name:\t{info.name}')
    if info.permissions is not None:
        print(f'permissions:\t{", ".join(info.permissions)}')
    if info.plugin_name is not None:
        print(f'plugin:\t{info.plugin_name}')
    print(f'created at:\t{timestamp_to_str(info.created_at)}')
    if info.deadline is not None:
        print(f'deadline:\t{timestamp_to_str(info.deadline)}')
    if info.last_used_at is not None:
        print(f'last used at:\t{timestamp_to_str(info.last_used_at)}')
    if info.last_used_browser is not None:
        print(f'last used browser:\t{info.last_used_browser}')
    if info.last_used_ip is not None:
        print(f'last used IP:\t{info.last_used_ip}')


def token_create(node: MoeraNode) -> None:
    attrs = TokenAttributes()
    attrs.login = 'admin'
    attrs.password = args.password
    attrs.name = args.token_name
    info = node.create_token(attrs)
    print(f'ID:\t{info.id}')
    print(f'token:\t{info.token}')
    if info.name is not None:
        print(f'name:\t{info.name}')


def token_rename(node: MoeraNode) -> None:
    setup_admin_auth(node)
    tname = TokenName()
    tname.name = args.token_name
    info = node.update_token(args.id, tname)
    print(f'ID:\t{info.id}')
    print(f'token:\t{info.token}')
    if info.name is not None:
        print(f'name:\t{info.name}')


def token_delete(node: MoeraNode) -> None:
    setup_admin_auth(node)
    node.delete_token(args.id)


def get_default_options(metadata: Sequence[SettingMetaInfo]) -> List[SettingInfo]:
    options = []
    for meta in metadata:
        if args.prefix is not None and not meta.name.startswith(args.prefix):
            continue
        option = SettingInfo()
        option.name = meta.name
        option.value = meta.default_value
        options.append(option)
    return options


def option_show(node: MoeraNode) -> None:
    setup_admin_auth(node)
    metadata = node.get_node_settings_metadata()
    meta_map: dict[str, SettingMetaInfo] = {m.name: m for m in metadata}
    if args.defaults:
        options = get_default_options(metadata)
    else:
        options = node.get_node_settings(args.prefix)
    for option in options:
        meta = meta_map.get(option.name)
        privileged = ' '
        changed = ' '
        if meta is not None:
            if meta.privileged:
                privileged = 'P'
            if meta.default_value != option.value:
                changed = '*'
            elif args.modified:
                continue
        if option.value is not None:
            value = option.value.replace('\n', '\\n')
        else:
            value = 'null'
        line = f'{privileged}{changed} {option.name} = {value}'
        if meta is not None:
            if args.type:
                line = f'{line:<40}\t({format_type_info(meta)})'
            if args.description:
                line += f'\t{meta.title}'
        print(line)


def format_type_info(meta: SettingMetaInfo) -> str:
    type_info: str = meta.type
    if meta.modifiers is not None:
        if meta.modifiers.format is not None:
            type_info += f':{meta.modifiers.format}'
        if meta.modifiers.min is not None:
            type_info += f', min={meta.modifiers.min}'
        if meta.modifiers.max is not None:
            type_info += f', max={meta.modifiers.max}'
        if meta.modifiers.multiline is True:
            type_info += ', multiline'
        if meta.modifiers.never is True:
            type_info += ', never'
        if meta.modifiers.always is True:
            type_info += ', always'
        if meta.modifiers.principals is not None:
            type_info += f', [{", ".join(meta.modifiers.principals)}]'
    return type_info


def option_set(node: MoeraNode) -> None:
    setup_admin_auth(node)
    info = SettingInfo()
    info.name = args.name
    info.value = args.value
    node.update_settings([info])


def option_reset(node: MoeraNode) -> None:
    setup_admin_auth(node)
    info = SettingInfo()
    info.name = args.name
    info.value = None
    node.update_settings([info])


def get_option_metadata(node):
    meta = first([m for m in node.get_node_settings_metadata(prefix=args.name) if m.name == args.name])
    if meta is None:
        error("Option not found: " + args.name)
    return meta


def option_set_default(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    meta = get_option_metadata(node)
    attrs = SettingMetaAttributes()
    attrs.name = args.name
    attrs.default_value = args.value
    attrs.privileged = meta.privileged
    node.update_node_settings_metadata([attrs])


def option_reset_default(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    meta = get_option_metadata(node)
    attrs = SettingMetaAttributes()
    attrs.name = args.name
    attrs.default_value = None
    attrs.privileged = meta.privileged
    node.update_node_settings_metadata([attrs])


def option_set_privileged(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    meta = get_option_metadata(node)
    attrs = SettingMetaAttributes()
    attrs.name = args.name
    attrs.default_value = meta.default_value
    attrs.privileged = True
    node.update_node_settings_metadata([attrs])


def option_set_not_privileged(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    meta = get_option_metadata(node)
    attrs = SettingMetaAttributes()
    attrs.name = args.name
    attrs.default_value = meta.default_value
    attrs.privileged = False
    node.update_node_settings_metadata([attrs])


def option_reset_privileged(node: MoeraNode) -> None:
    setup_root_admin_auth(node)
    meta = get_option_metadata(node)
    attrs = SettingMetaAttributes()
    attrs.name = args.name
    attrs.default_value = meta.default_value
    attrs.privileged = None
    node.update_node_settings_metadata([attrs])


def moctl() -> None:
    try:
        parse_args()
        run()
    except (MoeraNodeConnectionError, MoeraNodeError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
