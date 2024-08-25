import re
import sys
from importlib.metadata import version
from time import time, strftime, localtime, sleep
from typing import NoReturn, Literal

from dateutil.parser import parse as parse_date
from docopt import docopt
from moeralib import naming
from moeralib.crypto import (generate_mnemonic_key, generate_key, sign_fingerprint, mnemonic_to_private_key,
                             raw_public_key, raw_private_key)
from moeralib.naming import MAIN_SERVER, DEV_SERVER, MoeraNamingConnectionError, MoeraNamingError, node_name_parse
from moeralib.naming.fingerprints import create_put_call_fingerprint0
from moeralib.naming.types import RegisteredNameInfo, Timestamp, SigningKeyInfo

PROGRAM_NAME = 'moname'
PAGE_SIZE = 100

OPTIONS_HELP = '''
Query Moera naming service.

usage:
  moname [--dev | --server SERVER] [--created] [--keys | --all-keys] [--similar] [--at AT] <name>
  moname --list [--dev | --server SERVER] [--created] [--at AT] [--newer NEWER] [<name>]
  moname --add [--dev | --server SERVER] <name> <uri>
  moname --update [--dev | --server SERVER] [--uri URI] [--signing-key] [--updating-key] <name>
  moname --help
  moname --version

positional arguments:
  <name>                node name (use _N suffix to set generation)
  <uri>                 node URI

options:
  -h, --help            show this help message and exit
  -a, --add             register a new name
  -c, --created         show creation time of the names
  -d, --dev             use the development naming server
  -g, --signing-key     generate a new signing key
  -G, --updating-key    generate a new updating key
  -k, --keys            show detailed information including keys
  -K, --all-keys        show detailed information including all current and past keys
  -l, --list            list the registered names
  -s SERVER, --server SERVER
                        naming server URL
  -S, --similar         try to find a similar name, if the provided one is not found
  -t AT, --at AT        get information at the specific date/time
  -u, --update          update an existing name
  -U, --uri URI         a node URI to be set
  -w NEWER, --newer NEWER
                        show the names registered after the specific date/time
  -V, --version         show program's version number and exit
'''


class GlobalArgs:
    name: str
    generation: int
    command: Literal['resolve', 'list', 'add', 'update']
    server: str
    created: bool
    keys: bool | None
    similar: bool
    at: Timestamp | None
    newer: Timestamp | None
    uri: str
    signing_key: bool
    updating_key: bool


args: GlobalArgs = GlobalArgs()


def error(s: str) -> NoReturn:
    print(f'{PROGRAM_NAME}: error: {s}', file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    global args

    program_version = f'{PROGRAM_NAME} (moera-tools) {version("moera-tools")}'
    options = docopt(OPTIONS_HELP, version=program_version)

    if options['<name>'] is not None:
        try:
            (args.name, args.generation) = node_name_parse(options['<name>'])
        except ValueError as e:
            error(str(e))

    args.command = 'resolve'
    if options['--list']:
        args.command = 'list'
    if options['--add']:
        args.command = 'add'
    if options['--update']:
        args.command = 'update'

    args.server = MAIN_SERVER
    if options['--dev']:
        args.server = DEV_SERVER
    if options['--server'] is not None:
        args.server = options['--server']

    args.keys = None
    if options['--keys']:
        args.keys = False
    if options['--all-keys']:
        args.keys = True

    args.created = options['--created']
    args.similar = options['--similar']
    args.at = str_to_timestamp(options['--at'])
    args.newer = str_to_timestamp(options['--newer'])
    if options['--uri'] is not None:
        args.uri = options['--uri']
    else:
        args.uri = options['<uri>']
    args.signing_key = options['--signing-key']
    args.updating_key = options['--updating-key']


def str_to_timestamp(s: str | None) -> Timestamp | None:
    if s is None:
        return None
    return int(parse_date(s, fuzzy=True).timestamp())


def timestamp_to_str(ts: Timestamp) -> str:
    return strftime('%Y-%m-%d %H:%M:%S', localtime(ts))


def print_info(info: RegisteredNameInfo) -> None:
    if args.keys is not None:
        print('name         : %s' % info.name)
        print('generation   : %d' % info.generation)
        print('node URI     : %s' % info.node_uri)
        if info.digest is not None:
            print('digest       : %s' % info.digest.hex())
        if info.updating_key is not None:
            print('updating key : %s' % info.updating_key.hex())
        if info.created is not None:
            print('created      : %s' % timestamp_to_str(info.created))
        if args.keys is False:
            if info.signing_key is not None:
                print('signing key  : %s' % info.signing_key.hex())
            if info.valid_from is not None:
                print('valid from   : %s' % timestamp_to_str(info.valid_from))
    else:
        if args.created and info.created is not None:
            created = timestamp_to_str(info.created)
            print('%s %s_%d\t%s' % (created, info.name, info.generation, info.node_uri))
        else:
            print('%s_%d\t%s' % (info.name, info.generation, info.node_uri))


def print_key(info: SigningKeyInfo) -> None:
    print()
    print('signing key  : %s' % info.key.hex())
    print('valid from   : %s' % timestamp_to_str(info.valid_from))


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


def input_mnemonic(verbose: bool) -> str:
    words = []
    chop = re.compile(r'^[^a-zA-Z]*|[^a-zA-Z]*$')
    if verbose:
        print('Enter 24 secret words:')
    for n in range(24):
        try:
            word = chop.sub('', input())
            words.append(word)
        except EOFError:
            break
    if len(words) != 24:
        error('Wrong secret words')
    return ' '.join(words)


def wait_for_operation(srv: naming.MoeraNaming, op_id: str, verbose: bool) -> None:
    if verbose:
        print('Request sent, waiting for the operation to complete...')
    while True:
        status = srv.get_status(op_id)
        if status.status == 'SUCCEEDED':
            break
        if status.status == 'FAILED':
            error('Operation failed: ' + status.error_message)
        sleep(3)


def output_mnemonic(mnemonic, verbose):
    if verbose:
        print('Secret words:')
    i = 1
    for word in mnemonic.split(' '):
        print(f'{i:2}. {word}')
        i += 1


def output_signing_key(signing_key, verbose):
    print(('Signing key: ' if verbose else '') + raw_private_key(signing_key).hex())


def add_name() -> None:
    verbose = sys.stdout.isatty()

    mnemonic, updating_key = generate_mnemonic_key()
    put_updating_key = raw_public_key(updating_key.public_key())
    signing_key = generate_key()
    put_signing_key = raw_public_key(signing_key.public_key())
    valid_from = int(time()) + 600

    srv = naming.MoeraNaming(args.server)
    op_id = srv.put(args.name, args.generation, put_updating_key, args.uri, put_signing_key, valid_from, None, None)
    wait_for_operation(srv, op_id, verbose)

    output_mnemonic(mnemonic, verbose)
    print()
    output_signing_key(signing_key, verbose)


def update_name() -> None:
    verbose_in = sys.stdin.isatty()
    verbose_out = sys.stdout.isatty()

    srv = naming.MoeraNaming(args.server)
    info = srv.get_current(args.name, args.generation)
    if info is None:
        error(f'Name {args.name}_{args.generation} is not found')

    prev_updating_key = mnemonic_to_private_key(input_mnemonic(verbose_in))
    node_uri = args.uri if args.uri is not None else info.node_uri
    mnemonic = None
    fp_updating_key = info.updating_key
    put_updating_key = None
    if args.updating_key:
        mnemonic, updating_key = generate_mnemonic_key()
        fp_updating_key = raw_public_key(updating_key.public_key())
        put_updating_key = fp_updating_key
    signing_key = None
    fp_signing_key = info.signing_key
    put_signing_key = None
    fp_valid_from = info.valid_from
    put_valid_from = None
    if args.signing_key:
        signing_key = generate_key()
        fp_signing_key = raw_public_key(signing_key.public_key())
        put_signing_key = fp_signing_key
        fp_valid_from = int(time()) + 600
        put_valid_from = fp_valid_from

    fingerprint = create_put_call_fingerprint0(args.name, args.generation, fp_updating_key, node_uri, fp_signing_key,
                                               fp_valid_from, info.digest)
    signature = sign_fingerprint(fingerprint, prev_updating_key)
    op_id = srv.put(args.name, args.generation, put_updating_key, node_uri, put_signing_key, put_valid_from,
                    info.digest, signature)
    wait_for_operation(srv, op_id, verbose_out)

    if mnemonic is not None:
        output_mnemonic(mnemonic, verbose_out)
    if signing_key is not None:
        if mnemonic is not None:
            print()
        output_signing_key(signing_key, verbose_out)


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
            case 'update':
                update_name()
    except (MoeraNamingConnectionError, MoeraNamingError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
