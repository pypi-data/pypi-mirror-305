"""
Implementation of encrypted file logic.
"""

from __future__ import annotations
from functools import cached_property
import os
from typing import ClassVar, Final, Literal, Self, cast, final
from weakref import WeakValueDictionary

from .utils import aes256_decrypt, aes256_encrypt, sha256_hash

RESERVED_EXTENSIONS: Final[tuple[str, ...]] = (
    ".local-hash",
    ".remote-hash",
    ".secret",
    ".error",
)
"""List of reserved file extensions for working files."""

RESERVED_FILENAMES: Final[tuple[str, ...]] = (
    ".gitignore",
    ".git",
    ".mnemonic",
    ".keyhash"
)
"""List of reserved filenames for working files."""


FileStatus = Literal[
    # OK statuses:
    "local-only",
    "remote-only",
    "unchanged",
    "updated-local",
    "updated-remote",
    "updated-both",
    # Error statuses:
    "missing",
    "error",
]
"""Possible file statuses."""

FILE_STATUSES: Final[tuple[FileStatus, ...]] = (
    "local-only",
    "remote-only",
    "unchanged",
    "updated-local",
    "updated-remote",
    "missing",
    "error",
)
"""Possible file statuses."""

ErrorFlag = Literal[
    "missing-ciphertext",
    "invalid-ciphertext",
    "missing-remote-hash",
    "invalid-remote-hash",
]
"""Possible error flags corresponding to an 'error' status."""

ERROR_FLAGS: Final[tuple[ErrorFlag, ...]] = (
    "missing-ciphertext",
    "invalid-ciphertext",
    "missing-remote-hash",
    "invalid-remote-hash",
)
"""Possible error flags corresponding to an 'error' status."""

DecryptOutcome = Literal[
    # OK outcomes:
    "created",
    "updated",
    "unchanged",
    # Error outcomes:
    "missing",
    "skipped",
    "error",
]
"""Possible outcomes of the file decription procedure."""

EncryptOutcome = Literal[
    # OK outcomes:
    "created",
    "updated",
    "unchanged",
    # Error outcomes:
    "missing",
    "skipped",
    "error",
]
"""Possible outcomes of the file encryption procedure."""

FixOutcome = Literal["fixed", "failed", "skipped"]
"""Possible outcomes of the file fix procedure."""


class FilenameError(ValueError):
    """Error in the filename for a known file."""

@final
class ManagedFile:
    """Class managing access to a File."""

    @staticmethod
    def validate_filename(filename: str) -> None:
        # 1. Check for disallowed filenames:
        if filename in RESERVED_FILENAMES:
            raise FilenameError(f"Filename cannot be {filename}")
        # 2. Checks for disallowed extensions:
        for ext in RESERVED_EXTENSIONS:
            if filename.endswith(ext):
                raise FilenameError(f"Filename extension cannot be {ext}")

    def __new__(cls, filename: str, key: bytes) -> Self:
        """Creates an interface to an encrypted file."""
        self = ManagedFile.__instances.get(filename)
        if self is None:
            # 1. Validate filename:
            ManagedFile.validate_filename(filename)
            # 2. Validates the AES key:
            if len(key) != 32:
                raise ValueError("AES key must be 32 bytes long.")
            # 3. Creates the new instance:
            self = super().__new__(cls)
            self.__filename = filename
            self.__key = key
            # 4. Register the new instance in the weak value dictionary:
            ManagedFile.__instances[filename] = self
        return self

    @property
    def filename(self) -> str:
        """The filename for the plaintext file."""
        return self.__filename

    @cached_property
    def error(self) -> ErrorFlag | None:
        """Returns the current error, or None if no error is known."""
        try:
            with open(self.filename + ".error", "r") as f:
                flag = f.read().strip()
            if flag not in ERROR_FLAGS:
                raise IOError(
                    f"Invalid error flag {flag!r} in {self.filename}.error"
                )
            return cast(ErrorFlag, flag)
        except FileNotFoundError:
            return None

    def status(self, *, deep: bool = False) -> FileStatus:
        """
        Computes the file status.

        Optionally, perform a 'deep' check, which additionally enforces
        consistency between the stored remote hash and the computed remote hash,
        i.e. the hash of the decrypted ciphertext.
        """
        # 1. Perform basic status computation:
        status = self.__status
        # 2. Perform deep check if requested (unless status is 'error' already):
        if not deep or status == "error":
            return status
        if (ciphertext := self.__read_file(".secret")) is not None:
            remote_plaintext = aes256_decrypt(ciphertext, self.__key)
            if remote_plaintext is None:
                self.__set_error("invalid-ciphertext")
                return "error"
            if sha256_hash(remote_plaintext) != self.__stored_remote_hash:
                self.__set_error("invalid-remote-hash")
                return "error"
        # 3. Return non-error status:
        return status

    def fix(self) -> FixOutcome:
        """Attempts to fix errors."""
        if not self.error:
            return "skipped"
        ciphertext = self.__read_file(".secret")
        stored_remote_hash = self.__stored_remote_hash
        if ciphertext is None:
            if stored_remote_hash is not None:
                return "failed"  # missing ciphertext
            return "skipped"
        remote_plaintext = aes256_decrypt(ciphertext, self.__key)
        if remote_plaintext is None:
            return "failed"  # error decrypting ciphertext
        computed_remote_hash = sha256_hash(remote_plaintext)
        if stored_remote_hash != computed_remote_hash:
            self.__write_file(computed_remote_hash, ".remote-hash")
            self.__clear_error()
            return "fixed"
        return "skipped"

    def decrypt(self, *, force: bool = False) -> DecryptOutcome:
        """
        Decripts the ciphertext file, overwriting the current contents of the
        hash file and the plaintext file.
        If status is 'updated-local', the 'force' option must be explicitly
        set to True or decryption is skipped.
        """
        # 1. Compute status:
        status = self.status()
        # 2. Handle cases where decryption is not needed:
        match status:
            case "unchanged" | "local-only":
                return "unchanged"
            case "missing":
                return "missing"
            case "error":
                return "error"
            case "updated-local" if not force:
                return "skipped"
            case "updated-both" if not force:
                return "skipped"
        # 3. Handle cases where decryption is needed:
        # - "updated-local", if force=True
        # - "updated-both", if force=True
        # - "remote-only"
        # - "updated-remote"
        ciphertext = self.__read_file(".secret")
        assert ciphertext is not None # already handled by status='missing'
        # 3.1. check consistency with remote hash:
        remote_plaintext = aes256_decrypt(ciphertext, self.__key)
        if remote_plaintext is None:
            self.__set_error("invalid-ciphertext")
            return "error"
        computed_remote_hash = sha256_hash(remote_plaintext)
        if computed_remote_hash != self.__stored_remote_hash:
            self.__set_error("invalid-remote-hash")
            return "error"
        # 3.2. Update plaintext and local hash:
        self.__write_file(remote_plaintext, "")
        self.__write_file(sha256_hash(remote_plaintext), ".local-hash")
        # 3.3. Return outcome:
        return "created" if status == "remote-only" else "updated"

    def encrypt(self, *, force: bool = False) -> EncryptOutcome:
        """
        Encrypts the plaintext file, overwriting the current contents of the
        hash file and the ciphertext file.
        If status is 'updated-remote', the 'force' option must be explicitly
        set to True or encryption is not performed.
        """
        # 1. Compute status:
        status = self.status()
        # 2. Handle cases where encryption is not needed:
        match status:
            case "unchanged" | "remote-only":
                return "unchanged"
            case "missing":
                return "missing"
            case "error":
                return "error"
            case "updated-remote" if not force:
                return "skipped"
            case "updated-both" if not force:
                return "skipped"
        # 3. Handle cases where encryption is needed:
        # - "updated-remote", if force=True
        # - "updated-both", if force=True
        # - "local-only"
        # - "updated-local"
        plaintext = self.__read_file()
        assert plaintext is not None # already handled by status='missing'
        # 3.1. Update ciphertext, local hash and remote hash:
        ciphertext = aes256_encrypt(plaintext, self.__key)
        self.__write_file(sha256_hash(plaintext), ".local-hash")
        self.__write_file(ciphertext, ".secret")
        self.__write_file(sha256_hash(plaintext), ".remote-hash")
        # 3.2. Return outcome:
        return "created" if status == "local-only" else "updated"

    def clear_cache(self) -> None:
        """Clears caches for cached properties"""
        for name, member in ManagedFile.__dict__.items():
            if isinstance(member, cached_property):
                try:
                    delattr(self, name)
                except AttributeError:
                    pass

    def __str__(self) -> str:
        """Returns the filename."""
        return self.filename

    def __has_file(
        self, kind: Literal["", ".secret", ".local-hash", ".remote-hash"] = ""
    ) -> bool:
        """Checks whether the file exists."""
        return os.path.exists(self.filename + kind)

    def __set_error(self, flag: ErrorFlag) -> None:
        """Sets the error flag for this file."""
        if self.error:
            return
        self.__status = "error" # sets cached status to 'error'
        with open(self.filename + ".error", "w") as f:
            f.write(flag)
        self.error = flag

    def __clear_error(self) -> None:
        """Clears the error flag for this file."""
        if not self.error:
            return
        try:
            del self.__status # clears cached status
        except AttributeError:
            pass
        os.remove(self.filename + ".error")
        self.error = None


    __instances: ClassVar[WeakValueDictionary[str, ManagedFile]] = WeakValueDictionary()
    """A private static weak value dictionary of existing instances."""

    __filename: str
    """Filename of the encrypted file."""

    __key: bytes
    """Secret AES-256 key used for encryption and decryption."""

    __Kind = Literal["", ".secret", ".local-hash", ".remote-hash"]
    """The four possible kinds of file read and written."""

    def __read_file(
        self, kind: ManagedFile.__Kind = ""
    ) -> bytes | None:
        """Reads the contents of one of the underlying files."""
        try:
            with open(self.filename + kind, "rb") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def __write_file(
        self,
        content: bytes,
        kind: ManagedFile.__Kind = "",
    ) -> None:
        """Writes the contents of one of the underlying files."""
        with open(self.filename + kind, "wb") as f:
            f.write(content)

    @cached_property
    def __computed_local_hash(self) -> bytes | None:
        """Computes and caches the hash for the local plaintext."""
        plaintext = self.__read_file()
        return None if plaintext is None else sha256_hash(plaintext)

    @cached_property
    def __stored_local_hash(self) -> bytes | None:
        """Reads and caches the stored hash for the local plaintext."""
        return self.__read_file(".local-hash")

    @cached_property
    def __stored_remote_hash(self) -> bytes | None:
        """Reads and caches the stored hash for the remote plaintext."""
        return self.__read_file(".remote-hash")

    @cached_property
    def __status(self) -> FileStatus:
        """Computes file status based on local hash vs remote hash."""
        if self.error:
            return "error"
        computed_local_hash = self.__computed_local_hash
        stored_remote_hash = self.__stored_remote_hash
        has_cipher = self.__has_file(".secret")
        if stored_remote_hash is None:
            if has_cipher:
                ciphertext = self.__read_file(".secret")
                assert ciphertext is not None
                remote_plaintext = aes256_decrypt(ciphertext, self.__key)
                if remote_plaintext is None:
                    self.__set_error("invalid-ciphertext")
                else:
                    self.__set_error("missing-remote-hash")
                return "error"
            if computed_local_hash is None:
                return "missing"
            return "local-only"
        if not has_cipher:
            self.__set_error("missing-ciphertext")
            return "error"
        if computed_local_hash is None:
            return "remote-only"
        stored_local_hash = self.__stored_local_hash
        if computed_local_hash == stored_remote_hash:
            # includes the case where there is no stored local hash,
            # or the stored local hash differs from the computed local hash
            return "unchanged"
        if computed_local_hash == stored_local_hash:
            # in this case, they both differ from the stored remote hash
            return "updated-remote"
        if stored_local_hash == stored_remote_hash:
            # in this case, they both differ from the computed local hash
            return "updated-local"
        # all three hashes differ, including the case with no stored local hash
        return "updated-both"
