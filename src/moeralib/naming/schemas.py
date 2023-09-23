from ..structure import array_schema

OPERATION_STATUS_SCHEMA = {
    'type': 'string',
    'enum': ['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']
}

OPERATION_STATUS_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "operationId": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "generation": {
            "type": "number"
        },
        "status": OPERATION_STATUS_SCHEMA,
        "added": {
            "type": ["number", "null"]
        },
        "completed": {
            "type": ["number", "null"]
        },
        "errorCode": {
            "type": ["string", "null"]
        },
        "errorMessage": {
            "type": ["string", "null"]
        }
    },
    "required": ["operationId", "name", "generation", "status"],
    "additionalProperties": False
}

REGISTERED_NAME_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "generation": {
            "type": "number"
        },
        "updatingKey": {
            "type": ["string", "null"]
        },
        "nodeUri": {
            "type": "string"
        },
        "created": {
            "type": ["number", "null"]
        },
        "signingKey": {
            "type": ["string", "null"]
        },
        "validFrom": {
            "type": ["number", "null"]
        },
        "digest": {
            "type": ["string", "null"]
        }
    },
    "required": ["name", "generation", "nodeUri"]
}

REGISTERED_NAME_INFO_ARRAY_SCHEMA = array_schema(REGISTERED_NAME_INFO_SCHEMA)

SIGNING_KEY_INFO_SCHEMA = {
    "type": "object",
    "properties": {
        "key": {
            "type": "string"
        },
        "validFrom": {
            "type": "number"
        }
    },
    "required": ["key", "validFrom"],
    "additionalProperties": False
}

SIGNING_KEY_INFO_ARRAY_SCHEMA = array_schema(SIGNING_KEY_INFO_SCHEMA)
