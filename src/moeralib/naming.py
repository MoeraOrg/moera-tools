from typing import Any, Literal, TypeAlias, Mapping, cast

import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from moeralib.structure import Json, Structure, structure_or_none, structure_list

MAIN_SERVER = 'https://naming.moera.org/moera-naming'
DEV_SERVER = 'https://naming-dev.moera.org/moera-naming'


Timestamp: TypeAlias = int
OperationStatus: TypeAlias = Literal['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']
OPERATION_STATUS_SCHEMA = {
    'type': 'string',
    'enum': ['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']
}


class OperationStatusInfo(Structure):
    operation_id: str
    name: str
    generation: int
    status: OperationStatus
    added: Timestamp | None = None
    completed: Timestamp | None = None
    error_code: str | None = None
    error_message: str | None = None


OPERATION_STATUS_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "operationId": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "generation": {
            "type": "number"
        },
        "status": OPERATION_STATUS_SCHEMA,
        "added": {
            "type": ["number", "null"]
        },
        "completed": {
            "type": ["number", "null"]
        },
        "errorCode": {
            "type": ["string", "null"]
        },
        "errorMessage": {
            "type": ["string", "null"]
        }
    },
    "required": ["operationId", "name", "generation", "status"],
    "additionalProperties": False
}


class RegisteredNameInfo(Structure):
    name: str
    generation: int
    updating_key: bytes | None = None
    node_uri: str
    created: Timestamp | None = None
    signing_key: bytes | None = None
    valid_from: Timestamp | None = None
    digest: bytes | None = None


REGISTERED_NAME_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "generation": {
            "type": "number"
        },
        "updatingKey": {
            "type": ["string", "null"]
        },
        "nodeUri": {
            "type": "string"
        },
        "created": {
            "type": ["number", "null"]
        },
        "signingKey": {
            "type": ["string", "null"]
        },
        "validFrom": {
            "type": ["number", "null"]
        },
        "digest": {
            "type": ["string", "null"]
        }
    },
    "required": ["name", "generation", "nodeUri"]
}

REGISTERED_NAME_INFO_LIST_SCHEMA = {
    "type": "array",
    "items": REGISTERED_NAME_INFO_SCHEMA
}


class SigningKeyInfo(Structure):
    key: bytes
    valid_from: Timestamp


SIGNING_KEY_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "key": {
            "type": "string"
        },
        "validFrom": {
            "type": "number"
        }
    },
    "required": ["key", "validFrom"],
    "additionalProperties": False
}

SIGNING_KEY_INFO_LIST_SCHEMA = {
    "type": "array",
    "items": SIGNING_KEY_INFO_SCHEMA
}


class MoeraNamingError(Exception):

    def __init__(self, method, message):
        super().__init__(method + ': Naming server error: ' + message)


class MoeraNamingConnectionError(Exception):

    def __init__(self, message):
        super().__init__('Naming server connection error: ' + message)


class MoeraNaming:
    server: str
    call_id: int

    def __init__(self, server: str = MAIN_SERVER) -> None:
        self.server = server
        self.call_id = 0

    def call(self, method: str, params: list[Any],
             schema: Mapping[str, Any] | None = None) -> Json | list[Json] | str | bool | None:
        try:
            r = requests.post(
                self.server,
                json={
                    'method': method,
                    'params': params,
                    'jsonrpc': '2.0',
                    'id': self.call_id,
                }
            )
            self.call_id += 1

            response = r.json()
            if r.status_code not in [200, 201] or 'error' in response:
                if 'error' in response and 'message' in response['error']:
                    raise MoeraNamingError(method, response['error']['message'])
                else:
                    raise MoeraNamingError(method, "Invalid server response: " + repr(response))
            if 'result' not in response:
                raise MoeraNamingError(method, "Invalid server response: " + repr(response))
            result = response['result']
            if schema is not None and result is not None:
                validate(result, schema=schema)

            return result
        except requests.exceptions.InvalidJSONError as e:
            raise MoeraNamingError(method, "Invalid server response") from e
        except requests.exceptions.RequestException as e:
            raise MoeraNamingConnectionError(str(e)) from e
        except ValidationError as e:
            raise MoeraNamingError(method, "Invalid server response: " + repr(e)) from e

    def put(self, name: str, generation: int, updating_key: str | None = None, node_uri: str | None = None,
            signing_key: str | None = None, valid_from: Timestamp | None = None, previous_digest: str | None = None,
            signature: str | None = None) -> str:
        return cast(str, self.call('put', [name, generation, updating_key, node_uri, signing_key, valid_from,
                                           previous_digest, signature]))

    def get_status(self, operation_id: str) -> OperationStatusInfo | None:
        return structure_or_none(cast(Json, self.call('getStatus', [operation_id], OPERATION_STATUS_INFO_SCHEMA)),
                                 OperationStatusInfo)

    def get_current(self, name: str, generation: int) -> RegisteredNameInfo | None:
        return structure_or_none(cast(Json, self.call('getCurrent', [name, generation], REGISTERED_NAME_INFO_SCHEMA)),
                                 RegisteredNameInfo)

    def get_past(self, name: str, generation: int, at: Timestamp) -> RegisteredNameInfo | None:
        return structure_or_none(cast(Json, self.call('getPast', [name, generation, at], REGISTERED_NAME_INFO_SCHEMA)),
                                 RegisteredNameInfo)

    def is_free(self, name: str, generation: int) -> bool:
        return cast(bool, self.call('isFree', [name, generation]))

    def get_similar(self, name: str) -> RegisteredNameInfo | None:
        return structure_or_none(cast(Json, self.call('getSimilar', [name], REGISTERED_NAME_INFO_SCHEMA)),
                                 RegisteredNameInfo)

    def get_all_keys(self, name: str, generation: int) -> list[SigningKeyInfo]:
        return structure_list(cast(list[Json], self.call('getAllKeys', [name, generation],
                                                         SIGNING_KEY_INFO_LIST_SCHEMA)),
                              SigningKeyInfo)

    def get_all(self, at: Timestamp, page: int, size: int) -> list[RegisteredNameInfo]:
        return structure_list(cast(list[Json], self.call('getAll', [at, page, size], REGISTERED_NAME_INFO_LIST_SCHEMA)),
                              RegisteredNameInfo)

    def get_all_newer(self, at: Timestamp, page: int, size: int) -> list[RegisteredNameInfo]:
        return structure_list(cast(list[Json], self.call('getAllNewer', [at, page, size],
                                                         REGISTERED_NAME_INFO_LIST_SCHEMA)),
                              RegisteredNameInfo)
