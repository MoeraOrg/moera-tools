from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from ecpy.curves import Curve
from mnemonic import Mnemonic

from fingerprint import Fingerprint, FingerprintSchema, FingerprintWriter


def generate_key() -> ec.EllipticCurvePrivateKey:
    return ec.generate_private_key(ec.SECP256K1())


def generate_mnemonic_key() -> (str, ec.EllipticCurvePrivateKey):
    mnemonic = Mnemonic().generate(strength=256)
    private_key = mnemonic_to_private_key(mnemonic)
    return mnemonic, private_key


def mnemonic_to_private_key(mnemonic: str) -> ec.EllipticCurvePrivateKey:
    seed = Mnemonic().to_seed(mnemonic)
    private_value = int.from_bytes(seed, 'big') % Curve.get_curve('secp256k1').field
    private_key = ec.derive_private_key(private_value, ec.SECP256K1())
    return private_key


def raw_public_key(public_key: ec.EllipticCurvePublicKey) -> bytes:
    numbers = public_key.public_numbers()
    return numbers.x.to_bytes(32, 'big') + numbers.y.to_bytes(32, 'big')


def fingerprint_bytes(fingerprint: Fingerprint, schema: FingerprintSchema) -> bytes:
    writer = FingerprintWriter()
    writer.append(fingerprint, schema)
    return writer.to_bytes()


def digest_fingerprint(fingerprint: Fingerprint, schema: FingerprintSchema) -> bytes:
    digest = hashes.Hash(hashes.SHA3_256())
    digest.update(fingerprint_bytes(fingerprint, schema))
    return digest.finalize()


def sign_fingerprint(fingerprint: Fingerprint, schema: FingerprintSchema,
                     private_key: ec.EllipticCurvePrivateKey) -> bytes:
    return private_key.sign(fingerprint_bytes(fingerprint, schema), ec.ECDSA(hashes.SHA3_256()))


def verify_fingerprint_signature(fingerprint: Fingerprint, schema: FingerprintSchema, signature: bytes,
                                 public_key: ec.EllipticCurvePublicKey) -> bool:
    try:
        public_key.verify(signature, fingerprint_bytes(fingerprint, schema), ec.ECDSA(hashes.SHA3_256()))
        return True
    except InvalidSignature:
        return False
