from typing import Any, TypeVar

from camel_converter import dict_to_snake

Json = dict[str, Any]


class Structure:
    data: Json = {}

    def __init__(self, data: Json) -> None:
        self.data = dict_to_snake(data)

    def __getattr__(self, item: str) -> Any:
        if item not in self.data:
            return None
        else:
            return self.data[item]


StructType = TypeVar(bound=Structure)


def structure_or_none(data: Json | None, struct_type: StructType) -> StructType | None:
    if data is not None:
        return struct_type(data)
    else:
        return None


def structure_list(data: list[Json], struct_type: StructType) -> list[StructType]:
    return list(map(lambda item: struct_type(item), data))
