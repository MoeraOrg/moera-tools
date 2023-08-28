import argparse
import sys
from importlib.metadata import version
from time import time

from moeralib import naming
from moeralib.naming import RegisteredNameInfo, MAIN_SERVER, DEV_SERVER, MoeraNamingConnectionError, MoeraNamingError

PROGRAM_NAME = 'moname'
PAGE_SIZE = 100


class GlobalArgs:
    name: str
    generation: int
    list: bool
    server: str


args: GlobalArgs


def error(s: str) -> None:
    print('%s: error: %s' % (PROGRAM_NAME, s), file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    global args

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Query Moera naming service.')
    parser.set_defaults(generation=0, server=MAIN_SERVER)
    parser.add_argument('name', metavar='<name>', nargs='?', default='',
                        help='node name (use _N suffix to set generation)')
    parser.add_argument('-l', '--list', action='store_true', dest='list', default=False,
                        help='list the registered names')
    parser.add_argument('-d', '--dev', action='store_const', dest='server', const=DEV_SERVER,
                        help='naming server URL')
    parser.add_argument('-s', '--server', dest='server', help='naming server URL')
    program_version = '%s (moera-tools) %s' % (PROGRAM_NAME, version('moera-tools'))
    parser.add_argument('-V', '--version', action='version', version=program_version)
    args = parser.parse_args()

    if not args.list:
        if args.name != '':
            pos = args.name.rfind('_')
            if pos >= 0:
                (name, gen) = (args.name[0:pos], args.name[pos + 1:])
                args.name = name
                try:
                    args.generation = int(gen)
                except ValueError:
                    error('invalid generation: "%d"' % gen)
            else:
                args.generation = 0
        else:
            parser.print_usage()
            sys.exit(1)


def print_info(info: RegisteredNameInfo) -> None:
    if info is None:
        return
    print("%s_%d\t%s" % (info.name, info.generation, info.node_uri))


def resolve():
    srv = naming.MoeraNaming(args.server)
    info = srv.get_current(args.name, args.generation)
    print_info(info)


def scan():
    srv = naming.MoeraNaming(args.server)
    page = 0
    now = int(time())
    while True:
        infos = srv.get_all(now, page, PAGE_SIZE)
        if len(infos) == 0:
            break
        for info in infos:
            print_info(info)
        page += 1


def moname():
    try:
        parse_args()
        if not args.list:
            resolve()
        else:
            scan()
    except (MoeraNamingConnectionError, MoeraNamingError) as e:
        error(str(e))
