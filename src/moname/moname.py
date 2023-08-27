import argparse
import sys
from importlib.metadata import version

from moeralib import naming
from moeralib.naming import RegisteredNameInfo

PROGRAM_NAME = 'moname'


class GlobalArgs:
    name: str
    generation: int


args: GlobalArgs


def error(s: str) -> None:
    print('{0}: error: {1}'.format(PROGRAM_NAME, s), file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    global args
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description='Query Moera naming service.')
    parser.add_argument('name', metavar='<name>', help='node name (use _N suffix to set generation)')
    program_version = '{0} (moera-tools) {1}'.format(PROGRAM_NAME, version('moera-tools'))
    parser.add_argument('-V', '--version', action='version', version=program_version)
    args = parser.parse_args()
    if args.name != '':
        pos = args.name.rfind('_')
        if pos >= 0:
            (name, gen) = (args.name[0:pos], args.name[pos + 1:])
            args.name = name
            try:
                args.generation = int(gen)
            except ValueError:
                error('invalid generation: "{0}"'.format(gen))
        else:
            args.generation = 0


def print_info(info: RegisteredNameInfo) -> None:
    if info is None:
        return
    print("{0}_{1}\t{2}".format(info.name, info.generation, info.node_uri))


def resolve():
    srv = naming.MoeraNaming()
    info = srv.get_current(args.name, args.generation)
    print_info(info)


def moname():
    parse_args()
    resolve()
