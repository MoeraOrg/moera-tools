from typing import Any, cast, Sequence, Tuple

import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from . import schemas, types
from ..structure import structure_or_none, structure_list

MAIN_SERVER = 'https://naming.moera.org/moera-naming'
DEV_SERVER = 'https://naming-dev.moera.org/moera-naming'


class MoeraNamingError(Exception):

    def __init__(self, method: str, message: str):
        super().__init__(method + ': Naming server error: ' + message)


class MoeraNamingConnectionError(Exception):

    def __init__(self, message: str):
        super().__init__('Naming server connection error: ' + message)


class MoeraNaming:
    _server: str
    _call_id: int

    def __init__(self, server: str = MAIN_SERVER) -> None:
        self._server = server
        self._call_id = 0

    def call(self, method: str, params: Sequence[Any], schema: Any = None):
        try:
            r = requests.post(
                self._server,
                json={
                    'method': method,
                    'params': params,
                    'jsonrpc': '2.0',
                    'id': self._call_id,
                }
            )
            self._call_id += 1

            response = r.json()
            if r.status_code not in [200, 201] or 'error' in response:
                if 'error' in response and 'message' in response['error']:
                    raise MoeraNamingError(method, response['error']['message'])
                else:
                    raise MoeraNamingError(method, 'Invalid server response: ' + repr(response))
            if 'result' not in response:
                raise MoeraNamingError(method, 'Invalid server response: ' + repr(response))
            result = response['result']
            if schema is not None and result is not None:
                validate(result, schema=schema)

            return result
        except requests.exceptions.InvalidJSONError as e:
            raise MoeraNamingError(method, 'Invalid server response') from e
        except requests.exceptions.RequestException as e:
            raise MoeraNamingConnectionError(str(e)) from e
        except ValidationError as e:
            raise MoeraNamingError(method, 'Invalid server response: ' + repr(e)) from e

    def put(self, name: str, generation: int, updating_key: str | None = None, node_uri: str | None = None,
            signing_key: str | None = None, valid_from: types.Timestamp | None = None,
            previous_digest: str | None = None, signature: str | None = None) -> str:
        return cast(str, self.call('put', [name, generation, updating_key, node_uri, signing_key, valid_from,
                                           previous_digest, signature]))

    def get_status(self, operation_id: str) -> types.OperationStatusInfo | None:
        return structure_or_none(self.call('getStatus', [operation_id], schemas.OPERATION_STATUS_INFO_SCHEMA),
                                 types.OperationStatusInfo)

    def get_current(self, name: str, generation: int) -> types.RegisteredNameInfo | None:
        return structure_or_none(self.call('getCurrent', [name, generation], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def get_past(self, name: str, generation: int, at: types.Timestamp) -> types.RegisteredNameInfo | None:
        return structure_or_none(self.call('getPast', [name, generation, at], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def is_free(self, name: str, generation: int) -> bool:
        return cast(bool, self.call('isFree', [name, generation]))

    def get_similar(self, name: str) -> types.RegisteredNameInfo | None:
        return structure_or_none(self.call('getSimilar', [name], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def get_all_keys(self, name: str, generation: int) -> list[types.SigningKeyInfo]:
        return structure_list(self.call('getAllKeys', [name, generation], schemas.SIGNING_KEY_INFO_ARRAY_SCHEMA),
                              types.SigningKeyInfo)

    def get_all(self, at: types.Timestamp, page: int, size: int) -> list[types.RegisteredNameInfo]:
        return structure_list(self.call('getAll', [at, page, size], schemas.REGISTERED_NAME_INFO_ARRAY_SCHEMA),
                              types.RegisteredNameInfo)

    def get_all_newer(self, at: types.Timestamp, page: int, size: int) -> list[types.RegisteredNameInfo]:
        return structure_list(self.call('getAllNewer', [at, page, size], schemas.REGISTERED_NAME_INFO_ARRAY_SCHEMA),
                              types.RegisteredNameInfo)


def node_name_parse(node_name: str) -> Tuple[str, int]:
    name = node_name
    generation = 0

    pos = node_name.rfind('_')
    if pos >= 0:
        (name, gen) = (node_name[0:pos], node_name[pos + 1:])
        try:
            generation = int(gen)
        except ValueError:
            raise ValueError(f'invalid generation: "{gen}"')

    return name, generation


def resolve(name: str, naming_server=MAIN_SERVER) -> str | None:
    (name, gen) = node_name_parse(name)
    naming = MoeraNaming(naming_server)
    info = naming.get_current(name, gen)
    return info.node_uri if info is not None else None
