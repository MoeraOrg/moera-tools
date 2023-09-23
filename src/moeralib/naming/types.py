from typing import TypeAlias, Literal

from ..structure import Structure

Timestamp: TypeAlias = int
OperationStatus: TypeAlias = Literal['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']


class OperationStatusInfo(Structure):
    operation_id: str
    name: str
    generation: int
    status: OperationStatus
    added: Timestamp | None = None
    completed: Timestamp | None = None
    error_code: str | None = None
    error_message: str | None = None


class RegisteredNameInfo(Structure):
    name: str
    generation: int
    updating_key: bytes | None = None
    node_uri: str
    created: Timestamp | None = None
    signing_key: bytes | None = None
    valid_from: Timestamp | None = None
    digest: bytes | None = None


class SigningKeyInfo(Structure):
    key: bytes
    valid_from: Timestamp
