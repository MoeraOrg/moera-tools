from typing import Any, Literal

import requests

from moeralib.structure import Json, Structure, structure_or_none, structure_list

MAIN_SERVER = 'https://naming.moera.org/moera-naming'
DEV_SERVER = 'https://naming-dev.moera.org/moera-naming'


Timestamp = int
OperationStatus = Literal['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']


class OperationStatusInfo(Structure):
    operationId: str
    status: OperationStatus
    added: Timestamp | None
    completed: Timestamp | None
    error_code: str | None
    error_message: str | None
    generation: int | None


class RegisteredNameInfo(Structure):
    name: str
    generation: int
    updating_key: str
    node_uri: str
    signing_key: str | None
    valid_from: Timestamp | None
    digest: str


class MoeraNamingError(Exception):

    def __init__(self, message):
        super().__init__('Naming server returned error: ' + message)


class MoeraNaming:
    server: str
    call_id: int

    def __init__(self, server: str = MAIN_SERVER) -> None:
        self.server = server
        self.call_id = 0

    def call(self, method: str, *params: Any) -> Json | list[Json] | str | bool | None:
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
        if r.status_code not in [200, 201]:
            result = r.json()
            raise MoeraNamingError(result['message'])

        return r.json()['result']

    def put(self, name: str, generation: int, updating_key: str | None = None, node_uri: str | None = None,
            signing_key: str | None = None, valid_from: Timestamp | None = None, previous_digest: str | None = None,
            signature: str | None = None) -> str:
        return self.call('put', name, generation, updating_key, node_uri, signing_key, valid_from,
                         previous_digest, signature)

    def get_status(self, operation_id: str) -> OperationStatusInfo | None:
        return structure_or_none(self.call('getCurrent', operation_id), OperationStatusInfo)

    def get_current(self, name: str, generation: int) -> RegisteredNameInfo | None:
        return structure_or_none(self.call('getCurrent', name, generation), RegisteredNameInfo)

    def get_past(self, name: str, generation: int, at: Timestamp) -> RegisteredNameInfo | None:
        return structure_or_none(self.call('getPast', name, generation, at), RegisteredNameInfo)

    def is_free(self, name: str, generation: int) -> bool:
        return self.call('isFree', name, generation)

    def get_similar(self, name: str) -> RegisteredNameInfo | None:
        return structure_or_none(self.call('getSimilar', name), RegisteredNameInfo)

    def get_all(self, at: Timestamp, page: int, size: int) -> list[RegisteredNameInfo]:
        return structure_list(self.call('getAll', at, page, size), RegisteredNameInfo)
