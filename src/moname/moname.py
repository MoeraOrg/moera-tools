import argparse
import sys
from importlib.metadata import version
from time import time, strftime, localtime
from typing import cast, NoReturn

from dateutil.parser import parse as parse_date

from moeralib import naming
from moeralib.naming import MAIN_SERVER, DEV_SERVER, MoeraNamingConnectionError, MoeraNamingError, node_name_parse
from moeralib.naming.types import RegisteredNameInfo, Timestamp, SigningKeyInfo

PROGRAM_NAME = 'moname'
PAGE_SIZE = 100


class GlobalArgs:
    name: str
    generation: int
    list: bool
    server: str
    created: bool
    keys: bool | None
    similar: bool
    at: Timestamp | None
    newer: Timestamp | None


args: GlobalArgs


def error(s: str) -> NoReturn:
    print(f'{PROGRAM_NAME}: error: {s}', file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    global args

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Query Moera naming service.')
    parser.set_defaults(generation=0, server=MAIN_SERVER, keys=None)
    parser.add_argument('name', metavar='<name>', nargs='?', default='',
                        help='node name (use _N suffix to set generation)')
    parser.add_argument('-c', '--created', action='store_true', dest='created', default=False,
                        help='show creation time of the names')
    parser.add_argument('-d', '--dev', action='store_const', dest='server', const=DEV_SERVER,
                        help='use the development naming server')
    parser.add_argument('-k', '--keys', action='store_false', dest='keys',
                        help='show detailed information including keys')
    parser.add_argument('-K', '--all-keys', action='store_true', dest='keys',
                        help='show detailed information including all current and past keys')
    parser.add_argument('-l', '--list', action='store_true', dest='list', default=False,
                        help='list the registered names')
    parser.add_argument('-s', '--server', dest='server', help='naming server URL')
    parser.add_argument('-S', '--similar', action='store_true', dest='similar', default=False,
                        help='try to find a similar name, if the provided one is not found')
    parser.add_argument('-t', '--at', dest='at', type=str_to_timestamp, default=None,
                        help='get information at the specific date/time')
    parser.add_argument('-w', '--newer', dest='newer', type=str_to_timestamp, default=None,
                        help='show the names registered after the specific date/time')
    program_version = f'{PROGRAM_NAME} (moera-tools) {version("moera-tools")}'
    parser.add_argument('-V', '--version', action='version', version=program_version)
    args = cast(GlobalArgs, parser.parse_args())

    if not args.list:
        if args.name != '':
            try:
                (args.name, args.generation) = node_name_parse(args.name)
            except ValueError as e:
                error(str(e))
        else:
            parser.print_usage()
            sys.exit(1)
        if args.newer is not None:
            error('-w/--newer can be used only with -l/--list')
    else:
        if args.keys is not None:
            if args.keys:
                error('-K/--all-keys cannot be used with -l/--list')
            else:
                error('-k/--keys cannot be used with -l/--list')
        if args.similar:
            error('-S/--similar cannot be used with -l/--list')


def str_to_timestamp(s: str) -> Timestamp:
    return int(parse_date(s, fuzzy=True).timestamp())


def timestamp_to_str(ts: Timestamp) -> str:
    return strftime('%Y-%m-%d %H:%M:%S', localtime(ts))


def print_info(info: RegisteredNameInfo) -> None:
    if args.keys is not None:
        print("name         : %s" % info.name)
        print("generation   : %d" % info.generation)
        print("node URI     : %s" % info.node_uri)
        if info.digest is not None:
            print("digest       : %s" % info.digest.hex())
        if info.updating_key is not None:
            print("updating key : %s" % info.updating_key.hex())
        if info.created is not None:
            print("created      : %s" % timestamp_to_str(info.created))
        if args.keys is False:
            if info.signing_key is not None:
                print("signing key  : %s" % info.signing_key.hex())
            if info.valid_from is not None:
                print("valid from   : %s" % timestamp_to_str(info.valid_from))
    else:
        if args.created and info.created is not None:
            created = timestamp_to_str(info.created)
            print("%s %s_%d\t%s" % (created, info.name, info.generation, info.node_uri))
        else:
            print("%s_%d\t%s" % (info.name, info.generation, info.node_uri))


def print_key(info: SigningKeyInfo) -> None:
    print()
    print("signing key  : %s" % info.key.hex())
    print("valid from   : %s" % timestamp_to_str(info.valid_from))


def resolve() -> None:
    srv = naming.MoeraNaming(args.server)
    if args.at is None:
        info = srv.get_current(args.name, args.generation)
    else:
        info = srv.get_past(args.name, args.generation, args.at)
    if info is None and args.similar:
        info = srv.get_similar(args.name)
        if info is not None and args.at is not None:
            info = srv.get_past(info.name, info.generation, args.at)
    if info is None:
        return
    print_info(info)
    if args.keys is True:
        keys = srv.get_all_keys(info.name, info.generation)
        for key in keys:
            print_key(key)


def scan() -> None:
    srv = naming.MoeraNaming(args.server)
    page = 0
    at = args.at if args.at is not None else int(time())
    while True:
        if args.newer is None:
            infos = srv.get_all(at, page, PAGE_SIZE)
        else:
            infos = srv.get_all_newer(args.newer, page, PAGE_SIZE)
        if len(infos) == 0:
            break
        for info in infos:
            print_info(info)
        page += 1


def moname() -> None:
    try:
        parse_args()
        if not args.list:
            resolve()
        else:
            scan()
    except (MoeraNamingConnectionError, MoeraNamingError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
