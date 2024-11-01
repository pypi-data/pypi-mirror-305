"""
Implementation of secret key management, based on BIP 39 mnemonics.
"""

from __future__ import annotations
import os
from typing import ClassVar, Self, final
from weakref import WeakValueDictionary
from .mnemonic import Mnemonic
from .utils import sha256_hash


class KeyStoreError(IOError):
    """Error loading the key store."""

@final
class KeyStore:
    """Singleton object, managing access to the key store."""

    def __new__(cls) -> Self:
        """Returns the key store manager."""
        self = KeyStore.__instance
        if self is None:
            self = super().__new__(cls)
            # In the future, we might wish to customise these filenames.
            self.__mnemonic_filename = ".mnemonic"
            self.__keyhash_filename = ".keyhash"
            self.__loaded = False
            KeyStore.__instance = self
        return self

    @property
    def mnemonic(self) -> Mnemonic:
        """
        The BIP 39 mnemonic from which the key is generated.
        """
        self.__load()
        return self.__mnemonic

    @property
    def key(self) -> bytes:
        """
        The secret AES-256 key, i.e. the entropy of the mnemonic.
        """
        self.__load()
        return self.__key

    def keycheck(self) -> bool:
        """
        Command: checks that the secret key is present and valid.
        """
        try:
            self.__load(require_keyhash=True)
            print("✔️🔑 secret key is valid")
            return True
        except IOError as e:
            print(f"❌🔑 missing secret key: {e}")
        except ValueError as e:
            print(f"❌🔑 invalid secret key: {e}")
        return False

    def keygen(self, rehash: bool = False) -> bool:
        """
        Command: generates a new secret key.

        If rehash=True and the mnemonic file exists, generates a new key hash
        file. This shouldn't ordinarily be necessary, since the key hash file
        is generated at keygen time and should be committed into the repository.
        """
        mnemonic_filename = self.__mnemonic_filename
        keyhash_filename = self.__keyhash_filename
        # 1. Fail if key hash already exists:
        if os.path.exists(keyhash_filename):
            print(
                f"❌🔑 Secret key hash file {keyhash_filename} already exists."
            )
            return False
        # 2. Fail if the mnemonic file exists:
        if os.path.exists(mnemonic_filename):
            # Before failing, if rehash=True, regenerate the missing key hash:
            if rehash:
                key_hash = sha256_hash(self.key)
                with open(keyhash_filename, "wb") as keyhash_file:
                    keyhash_file.write(key_hash)
                print(
                    f"✔️🔑 Secret key hash written to file {keyhash_filename}."
                )
                return True
            print(f"❌🔑 Secret key file {mnemonic_filename} already exists.")
            return False
        # 3. Generate a random BIP 39 mnemonic and hash its entropy:
        mnemonic = Mnemonic.random(strength=256)
        key_hash = sha256_hash(bytes(mnemonic))
        # 4. Write the mnemonic and its hash to files:
        with open(mnemonic_filename, "w", encoding="utf-8") as mnemonic_file:
            mnemonic_file.write("\n".join(mnemonic))
        with open(keyhash_filename, "wb") as keyhash_file:
            keyhash_file.write(key_hash)
        # 5. Print success messages:
        print(f"✔️🔑 Secret key written to file {mnemonic_filename}.")
        print(f"✔️🔑 Secret key hash written to file {keyhash_filename}.")
        return True

    __instance: ClassVar[KeyStore | None] = None
    """The singleton instance of the key store."""

    __mnemonic_filename: str
    """The filename of the mnemonic file."""

    __keyhash_filename: str
    """The filename of the key hash file."""

    __loaded: bool
    __mnemonic: Mnemonic
    __key: bytes

    def __load(self, require_keyhash: bool = False) -> None:
        """
        Loads the BIP 39 mnemonic.

        :raises KeyStoreError: if the mnemonic file is missing
        :raises KeyStoreError: if the mnemonic is invalid
        :raises KeyStoreError: if the mnemonic does not match the key hash
        """
        if self.__loaded:
            return
        mnemonic_filename = self.__mnemonic_filename
        keyhash_filename = self.__keyhash_filename
        if not os.path.exists(mnemonic_filename):
            raise KeyStoreError(f"File {mnemonic_filename} not found.")
        with open(mnemonic_filename, "r", encoding="utf-8") as f:
            mnemonic_file_str = f.read()
        words = [
            word.strip()
            for word in mnemonic_file_str.split("\n")
            if word.strip()
        ]
        try:
            mnemonic = Mnemonic(words=words)
        except ValueError as e:
            raise KeyStoreError(f"Invalid mnemonic: {e}") from None
        if os.path.exists(keyhash_filename):
            with open(keyhash_filename, "rb") as mnemonic_hashfile:
                mnemonic_hash = mnemonic_hashfile.read()
            if sha256_hash(bytes(mnemonic)) != mnemonic_hash:
                raise KeyStoreError(
                    f"Key does not match {keyhash_filename} contents."
                )
        elif require_keyhash:
            raise KeyStoreError(f"File {keyhash_filename} not found.")
        self.__mnemonic = mnemonic
        self.__key = bytes(mnemonic)
