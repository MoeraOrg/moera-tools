from base64 import b64decode
from typing import Any, TypeVar, get_type_hints, get_args, TypeAlias

from camel_converter import dict_to_snake

Json: TypeAlias = dict[str, Any]


class Structure:
    data: Json = {}

    def __init__(self, data: Json) -> None:
        self.data = dict_to_snake(data)
        for (attr, value) in self.data.items():
            if is_bytes_attribute(type(self), attr) and value is not None:
                self.data[attr] = b64decode(value)

    def __getattr__(self, item: str) -> Any:
        if item not in self.data:
            return None
        else:
            return self.data[item]


StructType = TypeVar('StructType', bound=Structure)


def structure_or_none(data: Json | None, struct_type: type[StructType]) -> StructType | None:
    if data is not None:
        return struct_type(data)
    else:
        return None


def structure_list(data: list[Json], struct_type: type[StructType]) -> list[StructType]:
    return list(map(lambda item: struct_type(item), data))


def is_bytes_attribute(struct_type: type[StructType], attr: str) -> bool:
    hints = get_type_hints(struct_type)
    return attr in hints and (hints[attr] == bytes or bytes in get_args(hints[attr]))
