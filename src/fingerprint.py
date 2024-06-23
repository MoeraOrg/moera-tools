from typing import List, Union, Optional, Tuple, Any, Literal, Mapping

FingerprintPrimitiveType = Union[Literal['string', 'boolean', 'number'] | 'FingerprintSchema']
FingerprintSchema = List[Tuple[str, FingerprintPrimitiveType]]
Fingerprint = Mapping[str, Any]


class FingerprintWriter:

    def __init__(self):
        self._data = bytearray()

    def _append_null(self) -> None:
        self._data.append(0xff)

    def _append_string(self, string: Optional[str]) -> None:
        if string is None:
            self._append_null()
            return
        buf = string.encode()
        self._append_number(len(buf))
        self._data.extend(buf)

    def _append_boolean(self, b: bool) -> None:
        self._data.append(1 if b else 0)

    def _append_number(self, l: int) -> None:
        if l < 0xfc:
            len = 1
        elif l <= 0xffff:
            self._data.append(0xfc)
            len = 2
        elif l <= 0xffffffff:
            self._data.append(0xfd)
            len = 4
        else:
            self._data.append(0xfe)
            len = 8
        for _ in range(len):
            self._data.append(l & 0xff)
            l >>= 8

    def _append_bytes(self, b: bytes) -> None:
        self._append_number(len(b))
        self._data.extend(b)

    def _append_fingerprint(self, fingerprint: Fingerprint, schema: FingerprintSchema) -> None:
        for field in schema:
            self.append(fingerprint[field[0]], field[1])

    def append(self, value: Any, type: FingerprintPrimitiveType) -> None:
        if value is None:
            self._append_null()
        elif isinstance(type, list):
            self._append_fingerprint(value, type)
        elif type == 'string':
            self._append_string(value)
        elif type == 'boolean':
            self._append_boolean(value)
        elif type == 'number':
            self._append_number(value)
        elif type == 'bytes':
            self._append_bytes(value)

    def to_bytes(self) -> bytes:
        return bytes(self._data)
