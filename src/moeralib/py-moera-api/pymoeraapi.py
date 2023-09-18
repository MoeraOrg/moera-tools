from __future__ import annotations

import sys
from typing import Any, TextIO

import yaml

from camel_converter import to_snake


def kebab_to_snake(s: str) -> str:
    return s.replace('-', '_')


def ind(n: int) -> str:
    return n * 4 * ' '


def comma_wrap(s: str, indent: int) -> str:
    max_length = 120 - indent * 4
    result = ''
    while True:
        if len(s) <= max_length:
            result += s
            break
        pos = 0
        while True:
            next = s.find(', ', pos + 1)
            if next < 0 or next > max_length:
                break
            pos = next
        result += s[:pos] + ',\n' + ind(indent)
        s = s[pos + 2:]
    return result


def read_api(ifname: str) -> Any:
    with open(ifname, 'r') as ifile:
        return yaml.safe_load(ifile)


def generate_enum(enum: Any, tfile: TextIO) -> None:
    values = ", ".join('"%s"' % item['name'] for item in enum['values'])
    line = '\n%s = Literal[%s]\n' % (enum['name'], values)
    if len(line) > 120:
        line = '\n%s = Literal[\n    %s\n]\n' % (enum['name'], comma_wrap(values, 1))
    tfile.write(line)


def schema_type(sfile: TextIO, indent: int, a_type: str, struct: bool = False, nullable: bool = False,
                default: Any = None, min: float | None = None, max: float | None = None) -> None:
    if struct and not nullable:
        sfile.write(to_snake(a_type).upper() + '_SCHEMA')
        return
    sfile.write('{\n')
    if struct:
        sfile.write(ind(indent + 1) + to_snake(a_type).upper() + '_SCHEMA.copy().update(type=["object", "null"])')
    else:
        if nullable:
            sfile.write(ind(indent + 1) + f'"type": ["{a_type}", "null"]')
        else:
            sfile.write(ind(indent + 1) + f'"type": "{a_type}"')
    if default is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"default": {default}')
    if min is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"minimum": {min}')
    if max is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"maximum": {max}')
    sfile.write('\n')
    sfile.write(ind(indent) + '}')


def schema_array(sfile: TextIO, indent: int, a_type: str, struct: bool = False, nullable: bool = False,
                 default: Any = None, min_items: int | None = None, max_items: int | None = None,
                 min: float | None = None, max: float | None = None) -> None:
    sfile.write('{\n')
    if nullable:
        sfile.write(ind(indent + 1) + '"type": ["array", "null"],\n')
    else:
        sfile.write(ind(indent + 1) + '"type": "array",\n')
    sfile.write(ind(indent + 1) + '"items": ')
    schema_type(sfile, indent + 1, a_type, struct=struct, nullable=False, min=min, max=max)
    if default is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"default": {default}')
    if min_items is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"minItems": {min_items}')
    if max_items is not None:
        sfile.write(',\n')
        sfile.write(ind(indent + 1) + f'"maxItems": {max_items}')
    sfile.write('\n')
    sfile.write(ind(indent) + '}')


def schema_map_string_int(sfile: TextIO, indent: int, nullable: bool = False) -> None:
    sfile.write('{\n')
    sfile.write(ind(indent + 1) + '"type": ' + ('["object", "null"]' if nullable else 'object') + ',\n')
    sfile.write(ind(indent + 1) + '"patternProperties": {\n')
    sfile.write(ind(indent + 2) + '"^.*$": ')
    schema_type(sfile, indent + 2, 'integer')
    sfile.write('\n')
    sfile.write(ind(indent + 1) + '}')
    sfile.write('\n')
    sfile.write(ind(indent) + '}')


def generate_operations(operations: Any, tfile: TextIO, sfile: TextIO) -> None:
    tfile.write('\n\nclass %s(Structure):\n' % operations['name'])
    for field in operations['fields']:
        tfile.write('    %s: PrincipalValue | None = None\n' % to_snake(field['name']))

    sfile.write('\n')
    sfile.write('{name}_SCHEMA: Any = {{\n'.format(name=to_snake(operations['name']).upper()))
    sfile.write('    "type": "object",\n')
    sfile.write('    "properties": {\n')
    for field in operations['fields']:
        sfile.write('        "%s": ' % field['name'])
        schema_type(sfile, 2, "string", nullable=True)
        sfile.write(',\n')
    sfile.write('    },\n')
    sfile.write('    "additionalProperties": False\n')
    sfile.write('}\n')


PY_TYPES = {
    'String': 'str',
    'String[]': 'list[str]',
    'int': 'int',
    'float': 'float',
    'boolean': 'bool',
    'timestamp': 'Timestamp',
    'byte[]': 'bytes',
    'UUID': 'str',
    'String -> int': 'dict[str, int]'
}


def to_py_type(api_type: str) -> str:
    py_type = PY_TYPES.get(api_type)
    if py_type is None:
        print('Unrecognized field type: ' + api_type)
        exit(1)
    return py_type


SCHEMA_TYPES = {
    'String': ('string', False),
    'String[]': ('string', True),
    'int': ('integer', False),
    'float': ('number', False),
    'boolean': ('boolean', False),
    'timestamp': ('integer', False),
    'byte[]': ('string', False),
    'UUID': ('string', False),
    'String -> int': schema_map_string_int
}


class Structure:
    data: Any
    generated: bool = False
    depends: list[str]
    uses_body: bool = False
    output: bool = False
    output_array: bool = False

    def __init__(self, data: Any) -> None:
        self.data = data
        self.depends = [field['struct'] for field in data['fields'] if 'struct' in field]

    @property
    def generic(self) -> bool:
        return self.uses_body and self.output

    def generate_class(self, tfile: TextIO, structs: dict[str, Structure]) -> None:
        if self.generic:
            tfile.write('\n\nclass %sBase(Generic[B], Structure):\n' % self.data['name'])
        else:
            tfile.write('\n\nclass %s(Structure):\n' % self.data['name'])
        for field in self.data['fields']:
            if field.get('optional', False) and 'py-default' not in field:
                tmpl = '    %s: %s | None = None\n'
            else:
                tmpl = '    %s: %s\n'
            if 'struct' in field:
                if field['struct'] == 'Body':
                    t = 'B' if self.generic else 'str'
                else:
                    t = field['struct']
                    if self.generic and field['struct'] in structs and structs[field['struct']].generic:
                        t += 'Base[B]'
            elif 'enum' in field:
                t = field['enum']
            else:
                if field['type'] == 'any':
                    continue
                t = to_py_type(field['type'])
            if field.get('array', False):
                t = 'list[%s]' % t
            tfile.write(tmpl % (to_snake(field['name']), t))
        if self.generic:
            tfile.write('\n\nEncoded{name} = {name}Base[str]\n'.format(name=self.data['name']))
            tfile.write('{name} = {name}Base[Body]\n'.format(name=self.data['name']))

    def generate_schema(self, sfile: TextIO) -> None:
        sfile.write('\n{name}_SCHEMA: Any = {{\n'
                    .format(name=to_snake(self.data['name']).upper()))
        sfile.write('    "type": "object",\n')
        sfile.write('    "properties": {\n')
        required: list[str] = []
        for field in self.data['fields']:
            if field.get('type') == 'any':
                continue

            sfile.write('        "%s": ' % field['name'])
            default = field.get('py-default')
            optional = field.get('optional', False) and default is None
            array = field.get('array', False)
            if not optional:
                required.append(field['name'])
            struct = False
            if 'struct' in field:
                if field['struct'] == 'Body':
                    t = 'string'
                else:
                    t = field['struct']
                    struct = True
            elif 'enum' in field:
                t = 'string'
            else:
                s_type = SCHEMA_TYPES.get(field['type'])
                if callable(s_type):
                    t = None
                    s_type(sfile, 2, nullable=optional)
                else:
                    assert isinstance(s_type, tuple)
                    t, array = s_type
            if t is not None:
                if array:
                    schema_array(sfile, 2, t, struct=struct, nullable=optional, default=default,
                                 min_items=field.get('min-items'), max_items=field.get('max-items'),
                                 min=field.get('min'), max=field.get('max'))
                else:
                    schema_type(sfile, 2, t, struct=struct, nullable=optional, default=default,
                                min=field.get('min'), max=field.get('max'))
            sfile.write(',\n')
        sfile.write('    },\n')
        if len(required) > 0:
            sfile.write('    "required": [\n')
            for name in required:
                sfile.write(f'        "{name}",\n')
            sfile.write('    ],\n')
        sfile.write('    "additionalProperties": False\n')
        sfile.write('}\n')

        if self.output_array:
            sfile.write('\n%s_ARRAY_SCHEMA = ' % to_snake(self.data['name']).upper())
            schema_array(sfile, 0, self.data['name'], struct=True)
            sfile.write('\n')

    def generate(self, tfile: TextIO, sfile: TextIO, structs: dict[str, Structure]) -> None:
        self.generate_class(tfile, structs)
        if self.output:
            self.generate_schema(sfile)
        self.generated = True


def scan_body_usage(structs: dict[str, Structure]) -> None:
    for struct in structs.values():
        if 'Body' in struct.depends:
            struct.uses_body = True

    modified = True
    while modified:
        modified = False
        for struct in structs.values():
            if struct.uses_body:
                continue
            for dep in struct.depends:
                if dep in structs and structs[dep].uses_body:
                    struct.uses_body = True
                    modified = True


def scan_output_usage(api: Any, structs: dict[str, Structure]) -> None:
    for obj in api['objects']:
        for request in obj.get('requests', []):
            if 'out' not in request:
                continue
            if 'struct' not in request['out']:
                continue
            struct = request['out']['struct']
            if struct not in structs:
                continue
            structs[struct].output = True
            structs[struct].output_array |= request['out'].get('array', False)

    modified = True
    while modified:
        modified = False
        for struct in structs.values():
            if not struct.output:
                continue
            for dep in struct.depends:
                if dep in structs and not structs[dep].output:
                    structs[dep].output = True
                    modified = True


def scan_structures(api: Any) -> dict[str, Structure]:
    structs: dict[str, Structure] = {struct['name']: Structure(struct) for struct in api['structures']}
    scan_body_usage(structs)
    scan_output_usage(api, structs)
    return structs


def generate_structures(structs: dict[str, Structure], tfile: TextIO, sfile: TextIO) -> None:
    gen = True
    while gen:
        gen = False
        for struct in structs.values():
            if struct.generated:
                continue
            if any(not structs[d].generated for d in struct.depends if d in structs):
                continue
            struct.generate(tfile, sfile, structs)
            gen = True
    loop = [s.data['name'] for s in structs.values() if not s.generated]
    if len(loop) > 0:
        print('Dependency loop in structures: ' + ', '.join(loop))
        exit(1)


PREAMBLE_TYPES = '''# This file is generated

from typing import Generic, Literal, TypeAlias, TypeVar

from moeralib.structure import Structure

Timestamp: TypeAlias = int
PrincipalValue: TypeAlias = str

B = TypeVar('B')
'''

PREAMBLE_SCHEMAS = '''# This file is generated

from typing import Any
'''


def generate_types(api: Any, outdir: str) -> None:
    structs = scan_structures(api)

    with open(outdir + '/type.py', 'w+') as tfile:
        with open(outdir + '/schema.py', 'w+') as sfile:
            tfile.write(PREAMBLE_TYPES)
            sfile.write(PREAMBLE_SCHEMAS)
            for enum in api['enums']:
                generate_enum(enum, tfile)
            for operations in api['operations']:
                generate_operations(operations, tfile, sfile)
            generate_structures(structs, tfile, sfile)

    # with open(outdir + '/node.py', 'w+') as afile:
    #     afile.write(PREAMBLE_CALLS)
    #     generate_calls(api, structs, afile)


if len(sys.argv) < 2 or sys.argv[1] == '':
    print("Usage: py-moera-api <node_api.yml file path> <output directory>")
    exit(1)

api = read_api(sys.argv[1])
outdir = sys.argv[2] if len(sys.argv) >= 3 else '.'
generate_types(api, outdir)
