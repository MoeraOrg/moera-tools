import sys

from moeralib.node import MoeraNode
from moeralib.node.caller import MoeraNodeError, MoeraNodeConnectionError

PROGRAM_NAME = 'moctl'


def error(s: str) -> None:
    print('%s: error: %s' % (PROGRAM_NAME, s), file=sys.stderr)
    sys.exit(1)


def parse_args() -> None:
    pass


def run() -> None:
    node = MoeraNode()
    node.node_url('https://lamed.moera.blog/moera')
    w = node.get_domain('lamed.moera.blog')
    print(repr(w))


def moctl() -> None:
    try:
        parse_args()
        run()
    except (MoeraNodeConnectionError, MoeraNodeError) as e:
        error(str(e))
    except (KeyboardInterrupt, BrokenPipeError):
        pass
