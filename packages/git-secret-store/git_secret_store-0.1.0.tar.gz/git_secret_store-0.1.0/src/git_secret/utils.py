"""
Cryptographic utility functions for hashing, encryption, and decryption.
"""

from __future__ import annotations
import hashlib

try:
    import Cryptodome
    if not Cryptodome.version_info >= (3, 19):
        raise ModuleNotFoundError()
    from Cryptodome.Cipher import AES
    from Cryptodome.Hash import HMAC, SHA256
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "You must have PyCryptodome installed.\n"
        "pip install -U pycryptodomex>=3.19"
    ) from None


def sha256_hash(plaintext: str | bytes) -> bytes:
    """SHA3-256 hash of the given plaintext."""
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    m = hashlib.sha3_256()
    m.update(plaintext)
    return m.digest()


def aes256_encrypt(plaintext: bytes, aes_key: bytes) -> bytes:
    """
    Encrypts the given plaintext using AES-256 in OCB mode. Example from:

    www.pycryptodome.org/src/examples#encrypt-and-authenticate-data-in-one-step

    :raises ValueError: if the key is not 32 bytes long.
    """
    if len(aes_key) != 32:
        raise ValueError("AES key must be 32 bytes long.")
    cipher = AES.new(aes_key, AES.MODE_OCB)
    payload, tag = cipher.encrypt_and_digest(plaintext)
    assert len(cipher.nonce) == 15
    ciphertext = bytearray()
    ciphertext.extend(tag)
    ciphertext.extend(cipher.nonce)
    ciphertext.extend(payload)
    return bytes(ciphertext)


def aes256_decrypt(ciphertext: bytes, aes_key: bytes) -> bytes | None:
    """
    Decripts the given ciphertext using AES-256 in OCB mode. Example from:

    www.pycryptodome.org/src/examples#encrypt-and-authenticate-data-in-one-step

    Returns None if verification fails.

    :raises ValueError: if the key is not 32 bytes long.
    :raises ValueError: if the ciphertext is not at least 31 bytes long.
    """
    if len(aes_key) != 32:
        raise ValueError("AES key must be 32 bytes long.")
    if len(ciphertext) < 31:
        raise ValueError("Ciphertext must be at least 31 bytes long.")
    tag = ciphertext[:16]
    nonce = ciphertext[16:31]
    payload = ciphertext[31:]
    try:
        cipher = AES.new(aes_key, AES.MODE_OCB, nonce=nonce)
        message = cipher.decrypt_and_verify(payload, tag)
    except ValueError:
        return None
    return message
