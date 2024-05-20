from typing import Tuple

from config.constants import CRYPTO_SHA3_DIGEST_SIZE

# Implement the New Hope key exchange algorithm

def new_hope_key_exchange(public_key_a: bytes, public_key_b: bytes) -> Tuple[bytes, bytes]:
    """
    Perform a New Hope key exchange between two parties.

    :param public_key_a: The public key of party A.
    :param public_key_b: The public key of party B.
    :return: A tuple (shared_secret_a, shared_secret_b), where shared_secret_a and shared_secret_b are the shared secrets
             calculated by party A and party B, respectively.
    """
    # Implement the New Hope key exchange algorithm here
    # ...

    # Calculate the shared secrets using the SHA-3 hash function
    shared_secret_a = sha3_hash(public_key_b + public_key_a)
    shared_secret_b = sha3_hash(public_key_a + public_key_b)

    return shared_secret_a, shared_secret_b
