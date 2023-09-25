from __future__ import annotations

import re
import sys
from typing import Any, TextIO, Mapping, List, Sequence

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


def params_wrap(template: str, substitute: str, indent: int) -> str:
    line = template % substitute
    if len(line) > 120:
        line = template % ('\n' + ind(indent) + comma_wrap(substitute, indent) + '\n' + ind(indent - 1))
    return line


def read_api(ifname: str) -> Any:
    with open(ifname, 'r') as ifile:
        return yaml.safe_load(ifile)


def generate_enum(enum: Any, tfile: TextIO) -> None:
    values = ", ".join(f'"{item["name"]}"' for item in enum['values'])
    line = params_wrap(f'\n{enum["name"]} = Literal[%s]\n', values, 1)
    tfile.write(line)


def schema_type(sfile: TextIO, indent: int, a_type: str, struct: bool = False, nullable: bool = False,
                default: Any = None, min: float | None = None, max: float | None = None) -> None:
    if struct:
        if nullable:
            sfile.write('to_nullable_object_schema(%s_SCHEMA)' % to_snake(a_type).upper())
        else:
            sfile.write(to_snake(a_type).upper() + '_SCHEMA')
        return

    sfile.write('{\n')
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
    tfile.write(f'\n\nclass {operations["name"]}(Structure):\n')
    for field in operations['fields']:
        tfile.write('    %s: PrincipalValue | None = None\n' % to_snake(field['name']))

    sfile.write('\n')
    sfile.write('{name}_SCHEMA: Any = {{\n'.format(name=to_snake(operations['name']).upper()))
    sfile.write('    "type": "object",\n')
    sfile.write('    "properties": {\n')
    for field in operations['fields']:
        sfile.write(f'{ind(2)}"{field["name"]}": ')
        schema_type(sfile, 2, "string", nullable=True)
        sfile.write(',\n')
    sfile.write('    },\n')
    sfile.write('    "additionalProperties": False\n')
    sfile.write('}\n')


PY_TYPES = {
    'String': 'str',
    'String[]': 'List[str]',
    'int': 'int',
    'float': 'float',
    'boolean': 'bool',
    'timestamp': 'Timestamp',
    'byte[]': 'bytes',
    'UUID': 'str',
    'String -> int': 'Mapping[str, int]'
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
    depends: Sequence[str]
    uses_body: bool = False
    output: bool = False
    output_array: bool = False

    def __init__(self, data: Any) -> None:
        self.data = data
        self.depends = [field['struct'] for field in data['fields'] if 'struct' in field]

    @property
    def generic(self) -> bool:
        return self.uses_body and self.output

    def generate_class(self, tfile: TextIO) -> None:
        tfile.write(f'\n\nclass {self.data["name"]}(Structure):\n')
        for field in self.data['fields']:
            if field.get('optional', False) and 'py-default' not in field:
                tmpl = '    %s: %s | None = None\n'
            else:
                tmpl = '    %s: %s\n'
            if 'struct' in field:
                t = field['struct']
            elif 'enum' in field:
                t = field['enum']
            else:
                if field['type'] == 'any':
                    continue
                t = to_py_type(field['type'])
            if field.get('array', False):
                t = f'List[{t}]'
            tfile.write(tmpl % (to_snake(field['name']), t))

    def generate_schema(self, sfile: TextIO) -> None:
        sfile.write('\n{name}_SCHEMA: Any = {{\n'
                    .format(name=to_snake(self.data['name']).upper()))
        sfile.write('    "type": "object",\n')
        sfile.write('    "properties": {\n')
        required: List[str] = []
        for field in self.data['fields']:
            if field.get('type') == 'any':
                continue

            sfile.write(f'{ind(2)}"{field["name"]}": ')
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
            sfile.write('\n{name}_ARRAY_SCHEMA = array_schema({name}_SCHEMA)\n'
                        .format(name=to_snake(self.data['name']).upper()))

    def generate(self, tfile: TextIO, sfile: TextIO) -> None:
        self.generate_class(tfile)
        if self.output:
            self.generate_schema(sfile)
        self.generated = True


def scan_body_usage(structs: Mapping[str, Structure]) -> None:
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


def scan_output_usage(api: Any, structs: Mapping[str, Structure]) -> None:
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


def scan_structures(api: Any) -> Mapping[str, Structure]:
    structs: Mapping[str, Structure] = {struct['name']: Structure(struct) for struct in api['structures']}
    scan_body_usage(structs)
    scan_output_usage(api, structs)
    return structs


def generate_structures(structs: Mapping[str, Structure], tfile: TextIO, sfile: TextIO) -> None:
    gen = True
    while gen:
        gen = False
        for struct in structs.values():
            if struct.generated:
                continue
            if any(not structs[d].generated for d in struct.depends if d in structs):
                continue
            struct.generate(tfile, sfile)
            gen = True
    loop = [s.data['name'] for s in structs.values() if not s.generated]
    if len(loop) > 0:
        print('Dependency loop in structures: ' + ', '.join(loop))
        exit(1)


def is_no_auth(auth: str) -> bool:
    variants = auth.split(" or ")
    return variants == ['none'] or variants == ['signature']


def generate_calls(api: Any, structs: Mapping[str, Structure], afile: TextIO) -> None:
    for obj in api['objects']:
        for request in obj.get('requests', []):
            if 'function' not in request:
                continue

            function = to_snake(request['function'])
            params = 'self'
            call_params = f'"{function}", location, method="{request["type"]}"'

            tail_params = ''
            url_params: Mapping[str, str] = {}
            flag_name: str | None = None
            flag_py_name: str | None = None
            flags: Sequence[str] = []
            if 'params' in request:
                for param in request['params']:
                    if 'name' not in param:
                        print('Missing name of parameter of the request "{method} {url}"'
                              .format(method=request['type'], url=request['url']))
                        exit(1)
                    name = param['name']
                    py_name = to_snake(name)
                    url_params[name] = py_name
                    if 'enum' in param:
                        py_type = 'types.' + param['enum']
                    else:
                        py_type = to_py_type(param['type'])
                    if 'flags' in param:
                        flag_name = name
                        flag_py_name = py_name
                        flags = [flag['name'] for flag in param['flags']]
                        for flag in flags:
                            params += f', with_{flag}: bool = False'
                    else:
                        if param.get('optional', False):
                            tail_params += f', {py_name}: {py_type} | None = None'
                        else:
                            params += f', {py_name}: {py_type}'
            if 'in' in request:
                inp = request['in']
                if 'type' in inp:
                    if inp['type'] != 'blob':
                        print('Unrecognised type "{type}" of the input body of the request "{method} {url}"'
                              .format(type=inp['type'], method=request['type'], url=request['url']))
                        exit(1)
                    params += ', file: IO, file_type: str'
                    call_params += f', body_file=file, body_file_type=file_type'
                else:
                    if 'name' not in inp:
                        print('Missing name of body of the request "{method} {url}"'
                              .format(method=request['type'], url=request['url']))
                        exit(1)
                    name = to_snake(inp['name'])
                    py_type = 'types.' + inp['struct']
                    if inp.get('array', False):
                        py_type = f'List[{py_type}]'
                    params += f', {name}: {py_type}'
                    call_params += f', body={name}'
            params += tail_params

            if is_no_auth(request.get('auth', 'none')):
                call_params += ', auth=False'

            location: str = request['url']
            if len(url_params) > 0:
                uparams = []
                p = re.compile(r'{(\w+)}')
                for name in p.findall(location):
                    if name not in url_params:
                        print('Unknown parameter "{param}" referenced in location "{url}"'
                              .format(param=name, url=request['url']))
                        exit(1)
                    uparams.append(f'{name}=quote_plus({url_params[name]})')
                    del url_params[name]
                location = params_wrap(
                    f'{ind(2)}location = "{location}".format(%s)\n',
                    ', '.join(uparams),
                    3
                )
            else:
                location = f'{ind(2)}location = "{location}"\n'

            subs = []
            for name, py_name in url_params.items():
                subs.append(f'"{name}": {py_name}')
            if len(subs) > 0:
                query_params = params_wrap(f'{ind(2)}params = {{%s}}\n', ', '.join(subs), 3)
                call_params += ', params=params'
            else:
                query_params = ''

            result = 'types.Result'
            result_schema = 'schemas.RESULT_SCHEMA'
            result_array = False
            result_body = False
            if 'out' in request:
                out = request['out']
                if 'type' in out:
                    if out['type'] != 'blob':
                        print('Unrecognised type "{type}" of the output body of the request "{method} {url}"'
                              .format(type=out['type'], method=request['type'], url=request['url']))
                        exit(1)
                    result = 'IO'
                    result_schema = '"blob"'
                else:
                    struct = out['struct']
                    result = 'types.' + struct
                    if struct in structs and structs[struct].uses_body:
                        result_body = True
                    if out.get('array', False):
                        result_schema = 'schemas.%s_ARRAY_SCHEMA' % to_snake(struct).upper()
                        result_array = True
                    else:
                        result_schema = 'schemas.%s_SCHEMA' % to_snake(struct).upper()
            call_params += f', schema={result_schema}'
            if result_body:
                call_params += ', bodies=True'

            if result_array:
                afile.write(params_wrap(f'\n{ind(1)}def {function}(%s) -> List[{result}]:\n', params, 2))
            else:
                afile.write(params_wrap(f'\n{ind(1)}def {function}(%s) -> {result}:\n', params, 2))
            afile.write(location)
            if flag_name is not None:
                items = ', '.join(f'"{flag}": with_{flag}' for flag in flags)
                afile.write(f'{ind(2)}{flag_py_name} = comma_separated_flags({{{items}}})\n')
            afile.write(query_params)
            afile.write(params_wrap(f"{ind(2)}data = self.call(%s)\n", call_params, 3))
            if result == 'IO':
                afile.write(f"{ind(2)}return cast(IO, data)\n")
            elif result_array:
                afile.write(f"{ind(2)}return structure_list(data, {result})\n")
            else:
                afile.write(f"{ind(2)}return {result}(data)\n")


PREAMBLE_TYPES = '''# This file is generated

from typing import List, Literal, Mapping, Sequence, TypeAlias

from ..structure import Structure

Timestamp: TypeAlias = int
PrincipalValue: TypeAlias = str
'''

PREAMBLE_SCHEMAS = '''# This file is generated

from typing import Any

from ..structure import to_nullable_object_schema, array_schema
'''

PREAMBLE_CALLS = '''# This file is generated

from typing import IO, List, Sequence, cast
from urllib.parse import quote_plus

from . import types, schemas
from .caller import Caller
from ..structure import comma_separated_flags, structure_list


class MoeraNode(Caller):
'''


def generate_types(api: Any, outdir: str) -> None:
    structs = scan_structures(api)

    with open(outdir + '/types.py', 'w+') as tfile:
        with open(outdir + '/schemas.py', 'w+') as sfile:
            tfile.write(PREAMBLE_TYPES)
            sfile.write(PREAMBLE_SCHEMAS)
            for enum in api['enums']:
                generate_enum(enum, tfile)
            for operations in api['operations']:
                generate_operations(operations, tfile, sfile)
            generate_structures(structs, tfile, sfile)

    with open(outdir + '/node.py', 'w+') as afile:
        afile.write(PREAMBLE_CALLS)
        generate_calls(api, structs, afile)


if len(sys.argv) < 2 or sys.argv[1] == '':
    print("Usage: py-moera-api <node_api.yml file path> <output directory>")
    exit(1)

api = read_api(sys.argv[1])
outdir = sys.argv[2] if len(sys.argv) >= 3 else '.'
generate_types(api, outdir)
