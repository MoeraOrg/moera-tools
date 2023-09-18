from base64 import b64decode
from typing import Any, TypeVar, get_type_hints, get_args, TypeAlias

from camel_converter import dict_to_snake

Json: TypeAlias = dict[str, Any]


class Structure:
    def __init__(self, data: Json) -> None:
        data = dict_to_snake(data)
        for (attr, value) in data.items():
            if is_bytes_attribute(type(self), attr) and value is not None:
                data[attr] = b64decode(value)
        self.__dict__.update(data)


StructType = TypeVar('StructType', bound=Structure)


def structure_or_none(data: Json | None, struct_type: type[StructType]) -> StructType | None:
    return struct_type(data) if data is not None else None


def structure_list(data: list[Json], struct_type: type[StructType]) -> list[StructType]:
    return [struct_type(item) for item in data]


def is_bytes_attribute(struct_type: type[StructType], attr: str) -> bool:
    hints = get_type_hints(struct_type)
    return attr in hints and (hints[attr] == bytes or bytes in get_args(hints[attr]))
