from typing import Tuple

from config.constants import CRYPTO_SHA3_DIGEST_SIZE
from cryptography.signatures.rainbow import rainbow_keygen, rainbow_sign, rainbow_verify

# Provide utility functions for cryptographic operations, such as key generation, encryption, and decryption

def generate_rainbow_keypair() -> Tuple[bytes, bytes]:
    """
    Generate a Rainbow key pair.

    :return: A tuple (private_key, public_key), where private_key is the private key and public_key is the public key.
    """
    return rainbow_keygen(CRYPTO_SHA3_DIGEST_SIZE)

def rainbow_sign_message(message: bytes, private_key: bytes) -> Tuple[bytes, bytes]:
    """
    Sign a message using the Rainbow signature scheme.

    :param message: The message to sign.
    :param private_key: The private key used for signing.
    :return: A tuple (signature, public_key), where signature is the signature and public_key is the public key.
    """
    return rainbow_sign(message, private_key)

def rainbow_verify_signature(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """
    Verify a signature using the Rainbow signature scheme.

    :param message: The message to verify.
    :param signature: The signature to verify.
    :param public_key: The public key used for verification.
    :return: True if the signature is valid, False otherwise.
    """
    return rainbow_verify(message, signature, public_key)
