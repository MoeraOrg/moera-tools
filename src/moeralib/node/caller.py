import json
from copy import deepcopy
from enum import Enum
from typing import Any, IO, Mapping, Sequence

import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from moeralib.node import schemas
from moeralib.node.types import Result, BodyFormat, SourceFormat, Body
from moeralib.structure import Structure


class MoeraNodeError(Exception):

    def __init__(self, name: str, message: str):
        super().__init__(name + ': Node error: ' + message)


class MoeraNodeApiError(MoeraNodeError):
    error_code: str

    def __init__(self, name: str, result: Result):
        super().__init__(name, result.message if result.message is not None else '')
        self.error_code = result.error_code


class MoeraNodeConnectionError(Exception):

    def __init__(self, message: str):
        super().__init__('Node connection error: ' + message)


def decode_body(name: str, encoded: str, format: BodyFormat | SourceFormat | None) -> Body:
    if format is not None and format.lower() == "application":
        return Body({"text": ""})
    try:
        body = json.loads(encoded)
        validate(body, schema=schemas.BODY_SCHEMA)
        return Body(body)
    except json.JSONDecodeError as e:
        raise MoeraNodeError(name, 'Invalid body encoding') from e
    except ValidationError as e:
        raise MoeraNodeError(name, 'Invalid body: ' + repr(e)) from e


def decode_bodies(name: str, data):
    if isinstance(data, Sequence):
        return [decode_bodies(name, item) for item in data]
    decoded = deepcopy(data)
    if data.get('stories', None) is not None:
        decoded['stories'] = [decode_bodies(name, item) for item in data['stories']]
    if data.get('comments', None) is not None:
        decoded['comments'] = [decode_bodies(name, item) for item in data['comments']]
    if data.get('comment', None) is not None:
        decoded['comment'] = decode_bodies(name, data['comment'])
    if data.get('posting', None) is not None:
        decoded['posting'] = decode_bodies(name, data['posting'])
    if data.get('body', None) is not None:
        decoded['body'] = decode_body(name, data['body'], data.get('body_format', None))
    if data.get('body_preview', None) is not None:
        decoded['body_preview'] = decode_body(name, data['body_preview'], data.get('body_format', None))
    if data.get('body_src', None) is not None:
        decoded['body_src'] = decode_body(name, data['body_src'], data.get('body_src_format', None))
    return decoded


class NodeAuth(Enum):
    NONE = 0
    PEER = 1
    ADMIN = 2
    ROOT_ADMIN = 3


class Caller:
    root: str | None = None
    _root_secret: str | None = None
    _token: str | None = None
    _carte: str | None = None
    _auth_method: NodeAuth = NodeAuth.NONE

    def node_url(self, url: str) -> None:
        if not url.startswith('http:') and not url.startswith('https:'):
            url = 'https://' + url
        url = url.removesuffix('/').removesuffix('/api')
        if not url.endswith('/moera'):
            url += '/moera'
        self.root = url

    def root_secret(self, secret: str) -> None:
        self._root_secret = secret

    def token(self, token: str) -> None:
        self._token = token

    def carte(self, carte: str) -> None:
        self._carte = carte

    def auth_method(self, auth_method: NodeAuth) -> None:
        self._auth_method = auth_method

    def no_auth(self) -> None:
        self.auth_method(NodeAuth.NONE)

    def auth(self) -> None:
        self.auth_method(NodeAuth.PEER)

    def auth_admin(self) -> None:
        self.auth_method(NodeAuth.ADMIN)

    def auth_root_admin(self) -> None:
        self.auth_method(NodeAuth.ROOT_ADMIN)

    def call(self, name: str, location: str, params: Mapping[str, str | int | None] | None = None, method: str = 'GET',
             body: Structure | Sequence[Structure] | None = None, body_file: IO | None = None,
             body_file_type: str | None = None, auth: bool = True, schema: Any = None,
             bodies: bool = False):
        try:
            body_encoded = None
            if body is not None:
                if isinstance(body, Sequence):
                    body_encoded = [b.json() for b in body]
                else:
                    body_encoded = body.json()

            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json' if body_file_type is None else body_file_type
            }
            bearer: str | None = None
            if auth:
                match self._auth_method:
                    case NodeAuth.PEER:
                        if self._carte is None:
                            raise ValueError('Carte is not set')
                        bearer = 'carte:' + self._carte
                    case NodeAuth.ADMIN:
                        if self._token is None:
                            raise ValueError('Token is not set')
                        bearer = 'token:' + self._token
                    case NodeAuth.ROOT_ADMIN:
                        if self._root_secret is None:
                            raise ValueError('Root secret is not set')
                        bearer = 'secret:' + self._root_secret
            if bearer is not None:
                headers['Authorization'] = f'Bearer {bearer}'

            if self.root is None:
                raise ValueError('Node URL is not set')

            r = requests.request(
                method=method,
                url=self.root + '/api' + location,
                params=params,
                headers=headers,
                json=body_encoded,
                data=body_file,
                stream=schema == "blob"
            )

            response = r.json()
            if r.status_code not in [200, 201]:
                validate(response, schema=schemas.RESULT_SCHEMA)
                raise MoeraNodeApiError(name, Result(response))
            if schema is not None and schema != "blob":
                validate(response, schema=schema)

            if bodies:
                return decode_bodies(name, response)
            else:
                return response
        except requests.exceptions.InvalidJSONError as e:
            raise MoeraNodeError(name, 'Invalid server response') from e
        except requests.exceptions.RequestException as e:
            raise MoeraNodeConnectionError(str(e)) from e
        except ValidationError as e:
            raise MoeraNodeError(name, 'Invalid server response: ' + repr(e)) from e
