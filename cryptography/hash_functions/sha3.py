import functools
import secrets
from typing import List, Optional

import pysha3

from config.constants import CRYPTO_SHA3_DIGEST_SIZE, CRYPTO_SHA3_ROUNDS

# Implement the SHA-3 hash function

def sha3_hash(message: bytes, digest_size: Optional[int] = None) -> bytes:
    """
    Hash a message using the SHA-3 algorithm.

    :param message: The message to hash.
    :param digest_size: The desired digest size. If None, the default size (64 bytes) is used.
    :return: The hash digest.
    """
    if digest_size is None:
        digest_size = CRYPTO_SHA3_DIGEST_SIZE

    sha3_hash = pysha3.Keccak(digest_size=digest_size, rounds=CRYPTO_SHA3_ROUNDS)
    sha3_hash.update(message)
    return sha3_hash.digest()

def sha3_hash_list(messages: List[bytes], digest_size: Optional[int] = None) -> bytes:
    """
    Hash a list of messages using the SHA-3 algorithm.

    :param messages: The list of messages to hash.
    :param digest_size: The desired digest size. If None, the default size (64 bytes) is used.
    :return: The hash digest.
    """
    if digest_size is None:
        digest_size = CRYPTO_SHA3_DIGEST_SIZE

    padded_messages = functools.reduce(lambda x, y: x + y, [message + secrets.token_bytes(1) for message in messages])
    return sha3_hash(padded_messages, digest_size)
