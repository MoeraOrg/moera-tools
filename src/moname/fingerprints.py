from fingerprint import FingerprintSchema, Fingerprint

PUT_CALL_FINGERPRINT_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('name', 'string'),
    ('generation', 'number'),
    ('updating_key', 'bytes'),
    ('node_uri', 'string'),
    ('signing_key', 'bytes'),
    ('valid_from', 'number'),
    ('previous_digest', 'bytes'),
]


def create_put_call_fingerprint(name: str, generation: int, updating_key: bytes, node_uri: str, signing_key: bytes,
                                valid_from: int, previous_digest: bytes | None) -> Fingerprint:
    return {'version': 0} | locals()
