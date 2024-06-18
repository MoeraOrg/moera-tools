import sys
from importlib.metadata import version
from time import time, strftime, localtime
from typing import NoReturn, Literal

from dateutil.parser import parse as parse_date
from docopt import docopt
from moeralib import naming
from moeralib.naming import MAIN_SERVER, DEV_SERVER, MoeraNamingConnectionError, MoeraNamingError, node_name_parse
from moeralib.naming.types import RegisteredNameInfo, Timestamp, SigningKeyInfo

PROGRAM_NAME = 'moname'
PAGE_SIZE = 100

OPTIONS_HELP = """
Query Moera naming service.

usage:
  moname [--dev | --server SERVER] [--created] [--keys | --all-keys] [--similar] [--at AT] <name>
  moname --list [--dev | --server SERVER] [--created] [--at AT] [--newer NEWER] [<name>]
  moname --add <name>
  moname --help
  moname --version

positional arguments:
  <name>                node name (use _N suffix to set generation)

options:
  -h, --help            show this help message and exit
  -a, --add             register a new name
  -c, --created         show creation time of the names
  -d, --dev             use the development naming server
  -k, --keys            show detailed information including keys
  -K, --all-keys        show detailed information including all current and past keys
  -l, --list            list the registered names
  -s SERVER, --server SERVER
                        naming server URL
  -S, --similar         try to find a similar name, if the provided one is not found
  -t AT, --at AT        get information at the specific date/time
  -w NEWER, --newer NEWER
                        show the names registered after the specific date/time
  -V, --version         show program's version number and exit
"""


class GlobalArgs:
    name: str
    generation: int
    command: Literal["resolve", "list", "add"]
    server: str
    created: bool
    keys: bool | None
    similar: bool
    at: Timestamp | None
    newer: Timestamp | None


args: GlobalArgs = GlobalArgs()


def error(s: str) -> NoReturn:
    print(f'{PROGRAM_NAME}: error: {s}', file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    global args

    program_version = f'{PROGRAM_NAME} (moera-tools) {version("moera-tools")}'
    options = docopt(OPTIONS_HELP, version=program_version)

    if options["<name>"] is not None:
        try:
            (args.name, args.generation) = node_name_parse(options["<name>"])
        except ValueError as e:
            error(str(e))

    args.command = "resolve"
    if options["--list"]:
        args.command = "list"
    if options["--add"]:
        args.command = "add"

    args.server = MAIN_SERVER
    if options["--dev"]:
        args.server = DEV_SERVER
    if options["--server"] is not None:
        args.server = options["--server"]

    args.keys = None
    if options["--keys"]:
        args.keys = False
    if options["--all-keys"]:
        args.keys = True

    args.created = options["--created"]
    args.similar = options["--similar"]
    args.at = str_to_timestamp(options["--at"])
    args.newer = str_to_timestamp(options["--newer"])


def str_to_timestamp(s: str | None) -> Timestamp | None:
    if s is None:
        return None
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


def add_name() -> None:
    pass


def moname() -> None:
    try:
        parse_args()
        match args.command:
            case 'resolve':
                resolve()
            case 'list':
                scan()
            case 'add':
                add_name()
    except (MoeraNamingConnectionError, MoeraNamingError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
