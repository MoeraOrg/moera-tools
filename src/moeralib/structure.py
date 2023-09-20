from base64 import b64decode
from typing import Any, TypeVar, get_type_hints, get_args, Mapping, List

from camel_converter import dict_to_snake, to_camel


class Structure:
    def __init__(self, data) -> None:
        data = dict_to_snake(data)
        for (attr, value) in data.items():
            if value is not None:
                if is_bytes_attribute(type(self), attr):
                    data[attr] = b64decode(value)
                else:
                    struct = get_structure_attribute_type(type(self), attr)
                    if struct is not None:
                        data[attr] = struct(value)
        self.__dict__.update(data)

    def json(self):
        json = {}
        for name, value in self.__dict__.items():
            if name.startswith('_'):
                continue
            if isinstance(value, Structure):
                value = value.json()
            json[to_camel(name)] = value
        return json

    def __repr__(self) -> str:
        return repr(self.json())


StructType = TypeVar('StructType', bound=Structure)


def is_bytes_attribute(struct_type: type[StructType], attr: str) -> bool:
    hints = get_type_hints(struct_type)
    return attr in hints and (hints[attr] == bytes or bytes in get_args(hints[attr]))


def get_structure_attribute_type(struct_type: type[StructType], attr: str) -> type[Structure] | None:
    hints = get_type_hints(struct_type)
    if attr not in hints:
        return None
    if isinstance(hints[attr], type) and issubclass(hints[attr], Structure):
        return hints[attr]
    for hint in get_args(hints[attr]):
        if isinstance(hint, type) and issubclass(hint, Structure):
            return hint
    return None


def array_schema(schema: Any) -> Any:
    return {
        "type": "array",
        "items": schema
    }


def to_nullable_object_schema(schema: Any) -> Any:
    result = schema.copy()
    result.update(type=["object", "null"])
    return result


def structure_or_none(data, struct_type: type[StructType]) -> StructType | None:
    return struct_type(data) if data is not None else None


def structure_list(data, struct_type: type[StructType]) -> List[StructType]:
    return [struct_type(item) for item in data]


def comma_separated_flags(flags: Mapping[str, bool]) -> str | None:
    names = [name for name, value in flags.items() if value is not None]
    return ','.join(names) if len(names) > 0 else None
