"""
Implementation of the file store.
"""

from __future__ import annotations
from collections.abc import Callable, Container, Mapping
import os
from types import MappingProxyType
from typing import ClassVar, Self, final

from .files import FILE_STATUSES, ManagedFile, FilenameError
from .keystore import KeyStore, KeyStoreError

class FileStoreError(IOError):
    """Error loading the file store."""

@final
class FileStore:
    """Singleton object, managing access to the file store."""

    def __new__(cls) -> Self:
        """Returns the file store manager."""
        self = FileStore.__instance
        if self is None:
            self = super().__new__(cls)
            self.__keystore = KeyStore()
            self.__loaded = False
            FileStore.__instance = self
        return self

    @property
    def keystore(self) -> KeyStore:
        """The key store for this file store."""
        return self.__keystore

    @property
    def managed_files(self) -> Mapping[str, ManagedFile]:
        """
        Known managed files (encrypted), indexed by filename.
        """
        self.__load()
        return MappingProxyType(self.__managed_files)

    @property
    def folders(self) -> frozenset[str]:
        """
        Folders containing known managed files.
        """
        self.__load()
        return frozenset(self.__folders)

    @property
    def unmanaged_files(self) -> frozenset[str]:
        """
        Known unmanaged files (not encrypted).
        """
        self.__load()
        return frozenset(self.__unmanaged_files)

    def reload(self) -> None:
        """Reloads the file store data from the .gitignore file."""
        if self.__loaded:
            self.__loaded = False
            self.__load()

    def init(self, *, force: bool = False) -> bool:
        if os.path.exists(".gitignore") and not force:
            print("❌ .gitignore already exists. Use --force to overwrite.")
            return False
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write("# wildcard ignores:\n")
            f.write("*\n")
            f.write("*/\n")
            f.write("# special files:\n")
            f.write("!.gitignore\n")
            f.write("!.keyhash\n")
        print("✔️ Initialized .gitignore file.")
        return True

    def encrypt(self, filenames: list[str], *, force: bool = False) -> bool:
        """
        Command: encrypts managed files.

        If filenames are passed, only encrypts files with given names.
        If force is True, overwrites any remote-only changes during encryption.
        """
        self.keystore.keycheck()
        return self.__apply_file_op(
            "encrypt",
            lambda file: file.encrypt(force=force),
            error_statuses={"error", "missing", "skipped"},
            silent_statuses={"unchanged"},
            filenames=filenames if filenames else None,
        )

    def decrypt(self, filenames: list[str], *, force: bool = False) -> bool:
        """
        Command: decrypts managed files.

        If filenames are passed, only decrypts files with given names.
        If force is True, overwrites any local-only changes during decryption.
        """
        self.keystore.keycheck()
        return self.__apply_file_op(
            "decrypt",
            lambda file: file.decrypt(force=force),
            error_statuses={"error", "missing", "skipped"},
            silent_statuses={"unchanged"},
            filenames=filenames if filenames else None,
        )

    def check(self, filenames: list[str], *, deep: bool = False) -> bool:
        """
        Command: checks the status of managed files.

        If filenames are passed, only checks files with given names.
        If force is True, overwrites any local-only changes during decryption.
        """
        self.keystore.keycheck()
        return self.__apply_file_op(
            "check",
            lambda file: file.status(deep=deep),
            error_statuses={"error", "missing"},
            filenames=filenames if filenames else None,
            explain_error=lambda file, _: (
                None if (error:=file.error) is None else error
            ),
        )

    def list_unmanaged(self) -> bool:
        """
        Command: lists known unmanaged files (not encrypted).
        """
        # 1. Attempt to load file list, failing gracefully:
        try:
            plaintext_files = sorted(self.unmanaged_files)
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        # 2. List plaintext files, with basic status:
        for filename in plaintext_files:
            if not os.path.exists(filename):
                print(f"❌ {filename}: missing")
                continue
            if not os.path.isfile(filename):
                print(f"❌ {filename}: not a file")
                continue
            print(f"✔️ {filename}")
        return True

    def fix(self, filenames: list[str]) -> bool:
        """
        Command: attempts to fix issues with known managed files.

        If filenames are passed, only fixes files with given names.
        """
        self.keystore.keycheck()
        return self.__apply_file_op(
            "fix",
            lambda file: file.fix(),
            error_statuses={"failed"},
            silent_statuses={"skipped"},
            filenames=filenames if filenames else None,
        )

    def add_unmanaged(self, filenames: list[str]) -> bool:
        """
        Command: Adds given files as unmanaged files (not encrypted).
        """
        if not filenames:
            print("No files to add.")
            return True
        # 0. Make sure the user understands what it happening
        print("** THIS OPERATION MIGHT LEAK SECRETS **")
        while True:
            response = input(
                f"Are you sure you want to proceed? [yes/no]: "
            ).strip().lower()
            if response == "yes":
                break
            elif response == "no":
                print("Operation aborted.")
                return True
        # 1. Attempt to load file list, failing gracefully:
        try:
            plaintext_files = self.unmanaged_files
            encrypted_files = self.managed_files
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        # 2. Validate the filenames to add:
        new_files: list[str] = []
        for filename in filenames:
            if filename in plaintext_files:
                print(f"✔️ {filename}: known")
                continue
            try:
                ManagedFile.validate_filename(filename)
            except FilenameError as e:
                print(f"❌ {filename}: {e}")
                continue
            if filename in encrypted_files:
                print(f"❌ {filename}: already added as encrypted")
                continue
            if not os.path.exists(filename):
                print(f"❌ {filename}: missing")
                continue
            if not os.path.isfile(filename):
                print(f"❌ {filename}: not a file")
                continue
            new_files.append(filename)
            print(f"✔️ {filename}: added")
        if not new_files:
            return True
        # 3. Add the new files to the .gitignore file:
        folders = set(self.folders)
        new_folders: set[str] = set()
        with open(".gitignore", "a") as f:
            f.seek(0, os.SEEK_END)
            for filename in new_files:
                if "/" in filename:
                    path = filename.split("/")[:-1]
                    for i in range(1, len(path) + 1):
                        folder = "/".join(path[:i])+"/"
                        if folder not in folders:
                            f.write(f"!{folder}\n")
                            folders.add(folder)
                            new_folders.add(folder)
                f.write(f"!{filename}\n")
        # 4. Update the internal files mapping:
        self.__unmanaged_files.update(new_files)
        self.__folders.update(new_folders)
        return True

    def add(self, filenames: list[str]) -> bool:
        """
        Command: Adds given files as managed files.

        If not filenames are passed, triggers interactive file addition.
        """
        # 1. Attempt to load file list, failing gracefully:
        try:
            plaintext_files = self.unmanaged_files
            encrypted_files = self.managed_files
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        try:
            key = self.keystore.key
        except KeyStoreError as e:
            print(f"❌ {e}")
            return False
        # 2. Validate the filenames to add:
        new_files: list[ManagedFile] = []
        no_errors = True
        for filename in filenames:
            if filename in encrypted_files:
                print(f"✔️ {filename}: known")
                continue
            if not os.path.exists(filename):
                print(f"❌ {filename}: missing")
                no_errors = False
                continue
            if not os.path.isfile(filename):
                print(f"❌ {filename}: not a file")
                no_errors = False
                continue
            if filename in plaintext_files:
                print(f"❌ {filename}: already added as plaintext")
                no_errors = False
                continue
            try:
                new_files.append(ManagedFile(filename, key))
                print(f"✔️ {filename}: added")
            except FilenameError as e:
                print(f"❌ {filename}: {e}")
                no_errors = False
        if not new_files:
            return no_errors
        # 3. Add the new files to the .gitignore file:
        folders = set(self.folders)
        new_folders: set[str] = set()
        with open(".gitignore", "a") as f:
            f.seek(0, os.SEEK_END)
            for file in new_files:
                filename = file.filename
                if "/" in filename:
                    path = filename.split("/")[:-1]
                    for i in range(1, len(path) + 1):
                        folder = "/".join(path[:i])+"/"
                        if folder not in folders:
                            f.write(f"!{folder}\n")
                            folders.add(folder)
                            new_folders.add(folder)
                f.write(f"!{filename}.secret\n")
                f.write(f"!{filename}.remote-hash\n")
        # 4. Update the internal files mapping:
        self.__managed_files.update({file.filename: file for file in new_files})
        self.__folders.update(new_folders)
        return no_errors

    def add_interactive(self) -> bool:
        """
        Command: Navigaes all files in the repository which are not yet known
                 to the store (and don't have reserved filenames) and asks the
                 user whether they should be added, individually.
        """
        try:
            files_known = {*self.managed_files, *self.unmanaged_files}
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        try:
            key = self.keystore.key
        except KeyStoreError as e:
            print(f"❌ {e}")
            return False
        filenames: list[str] = []
        any_prompt = False
        for root, _, files in os.walk("."):
            for file in files:
                filename = os.path.join(root, file).replace("\\", "/")
                if filename.startswith("."):
                    filename = filename[2:]
                if filename.startswith("."):
                    continue
                try:
                    ManagedFile.validate_filename(filename)
                except FilenameError as e:
                    continue
                if filename in files_known:
                    continue
                if not os.path.exists(filename):
                    continue
                if not os.path.isfile(filename):
                    continue
                any_prompt = True
                while True:
                    response = input(
                        f"Add {filename}? [y/n]: "
                    ).strip().lower()
                    if response == "y":
                        filenames.append(filename)
                        break
                    elif response == "n":
                        break
        if not filenames:
            print("No files added." if any_prompt else "No files to add.")
            return True
        while True:
            response = input(
                f"Add {len(filenames)} new files? [yes/no]: "
            ).strip().lower()
            if response == "yes":
                self.add(filenames)
                break
            elif response == "no":
                print("No files added.")
                break
        return True

    def clear(self, filenames: list[str], *, force: bool = False) -> bool:
        """
        Command: clears local hash, remote hash & ciphertext for managed files.

        If filenames are passed, only clears files with given names.
        If force is False, only clears files with the following statuses:
        'unchanged', 'local-only', 'updated-local', or 'missing'.
        If force is True, clears files with any status.
        """
        print("** THIS IS A DESTRUCTIVE OPERATION **")
        while True:
            response = input(
                f"Are you sure you want to proceed? [yes/no]: "
            ).strip().lower()
            if response == "yes":
                break
            elif response == "no":
                print("Operation aborted.")
                return True
        if force:
            clearable_statuses = FILE_STATUSES
        else:
            clearable_statuses = (
                "unchanged", "local-only", "updated-local", "missing"
            )
        self.__apply_file_op(
            "check",
            lambda file: file.status(deep=True),
            error_statuses={*FILE_STATUSES}-{*clearable_statuses},
            filenames=filenames if filenames else None,
        )
        files_to_clear: dict[str, ManagedFile] = {
            filename: file
            for filename, file in self.managed_files.items()
            if file.status() in clearable_statuses
            and (not filenames or filename in filenames)
        }
        while True:
            response = input(
                f"Are you ** REALLY SURE ** you want to proceed? [yes/no]: "
            ).strip().lower()
            if response == "yes":
                break
            elif response == "no":
                print("Operation aborted.")
                return True
        removed_count = 0
        for filename, file in files_to_clear.items():
            try:
                os.remove(filename+".secret")
                print(f"Removed {filename}.secret")
                removed_count += 1
            except FileNotFoundError:
                pass
            try:
                os.remove(filename+".remote-hash")
                print(f"Removed {filename}.remote-hash")
                removed_count += 1
            except FileNotFoundError:
                pass
            try:
                os.remove(filename+".local-hash")
                print(f"Removed {filename}.local-hash")
                removed_count += 1
            except FileNotFoundError:
                pass
        if removed_count:
            print(f"Cleared {removed_count} files.")
        else:
            print("No files to clear.")
        return True

    def format_gitignore(self) -> bool:
        """
        Command: formats the .gitignore file, storing the contents of the old
                 .gitignore file in a .gitignore.old file.

        Note: the .gitignore file should already be managed by the git-secret
              command, so this command is not strictly necessary in normal use.
        """
        # 1. Attempt to load file list, failing gracefully:
        try:
            plaintext_files = self.unmanaged_files
            encrypted_files = self.managed_files
            folders = self.folders
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        # 2. Create a backup of the old .gitignore
        if os.path.exists(".gitignore.old"):
            print(
                f"❌ found existing .gitignore.old file. "
                "Use --force to overwrite."
            )
            return False
        try:
            with open(".gitignore", "r", encoding="utf-8") as f:
                gitignore_contents = f.read()
            with open(".gitignore.old", "w", encoding="utf-8") as f:
                f.write(gitignore_contents)
        except IOError as e:
            print(f"❌ {e}")
            return False
        # 3. Write the formatted .gitignore
        lines = [
            "# wildcard ignores:",
            "*",
            "*/",
            "# special files:",
            "!.gitignore",
            "!.keyhash",
        ]
        lines.append("# unmanaged files:")
        for filename in sorted(plaintext_files):
            lines.append("!"+filename)
        included_folders: set[str] = set()
        lines.append("# managed files:")
        def sort_key(filename: str) -> tuple[str, ...]:
            return tuple(filename.split("/"))
        for filename in sorted(encrypted_files, key=sort_key):
            if "/" in filename:
                path = filename.split("/")[:-1]
                for i in range(1, len(path)+1):
                    folder = "/".join(path[:i])+"/"
                    if folder in included_folders:
                        continue
                    lines.append("!"+folder)
                    included_folders.add(folder)
            lines.append("!"+filename+".secret")
            lines.append("!"+filename+".remote-hash")
        lines.append("")
        try:
            with open(".gitignore", "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
        except IOError as e:
            print(f"❌ {e}")
            return False
        return True

    __instance: ClassVar[FileStore | None] = None
    """The singleton instance of the file store."""

    __keystore: KeyStore
    """The key store for this file store."""

    __loaded: bool
    """Whether the file store data has been loaded."""

    __managed_files: dict[str, ManagedFile]
    """Known managed files (encrypted), indexed by filename."""

    __folders: set[str]
    """Folders containing known managed files."""

    __unmanaged_files: set[str]
    """Known unmanaged files (not encrypted)."""

    def __apply_file_op(
        self,
        opname: str,
        op: Callable[[ManagedFile], str],
        *,
        error_statuses: Container[str] = (),
        silent_statuses: Container[str] = (),
        filenames: list[str] | None = None,
        explain_error: Callable[[ManagedFile, str], str | None] | None = None,
    ) -> bool:
        """
        Logic common to encrypt, decrypt, check and fix functions:

        - An operation 'op' with screen name 'opname' is applied to all files,
          returning a string status for each file.
        - A set of error statuses can be provided, which is used to display a ❌
          or ✔️ mark for each file, depending on whether the returned status is
          in the error statuses or not.
        - A set of silent statuses can be provided, which is used to suppress
          printing of files where the returned status is in the silent statuses.
        - A function explaining errors can be provided, called when the returned
          status is in the error statuses to generate a custom error message.
        """
        # 1. Attempt to load file list, failing gracefully:
        try:
            files = self.managed_files
        except FileStoreError as e:
            print(f"❌ {e}")
            return False
        # 2. Filter files by filenames, if provided:
        if filenames is not None:
            # 2.1 Fail if any unknown filenames are provided:
            any_unknown_filenames = False
            for filename in filenames:
                if filename not in files:
                    print(f"❌ Unknown filename: {filename!r}")
                    any_unknown_filenames = True
            if any_unknown_filenames:
                return False
            # 2.2 Only keep given filenames:
            files = {
                filename: file
                for filename, file in files.items()
                if filename in filenames
            }
        # 3. Apply the operation to the files:
        status_count: dict[str, int] = {}
        any_error = False
        for filename, file in files.items():
            # 3.1 Apply the operation to the file and get a status:
            status = op(file)
            status_count[status] = status_count.get(status, 0) + 1
            error = status in error_statuses
            any_error |= error
            # 3.2 Print the status of the file, if not marked as silent:
            if status not in silent_statuses:
                if error:
                    if (
                        explain_error is not None
                        and (explanation := explain_error(file, status))
                        is not None
                    ):
                        print(f"❌ {filename}: {status}, {explanation}")
                    else:
                        print(f"❌ {filename}: {status}")
                else:
                    print(f"✔️ {filename}: {status}")
        # 4. Print summary of the operation:
        if not status_count:
            print(f"No files to {opname}.")
            return True
        status_count_str = ", ".join(
            f"{count} {status}" for status, count in status_count.items()
        )
        print(f"{opname.capitalize()}ed files: {status_count_str}")
        # 5. Exit with error code if any error occurred:
        return not any_error

    def __load(self) -> None:
        """
        Loads the file store data from the .gitignore file.

        :raises FileStoreError: if something went wrong while loading files.
        :raises KeyStoreError: if something went wrong while loading the key.
        """
        key = self.keystore.key
        if self.__loaded:
            return
        # 1. Load and sanitize lines:
        try:
            with open(".gitignore", "r") as gitignore:
                lines = [line.strip() for line in gitignore.read().split("\n")]
        except FileNotFoundError:
            raise FileStoreError("File .gitignore not found.") from None
        if lines[-1] != "":
            raise FileStoreError(
                "Empty final line required in .gitignore file."
            )
        original_lineno: dict[int, int] = {}
        for i, line in enumerate(lines):
            if line.startswith("#"):
                continue
            original_lineno[len(original_lineno)+1] = i+1
        lines = [line for line in lines if line and not line.startswith("#")]
        # 2. Check that the wildcard ignores are presend:
        FIXED_LINES = [
            "*",
            "*/",
            "!.gitignore",
            "!.keyhash",
        ]
        for i, fixed_line in enumerate(FIXED_LINES):
            if lines[i] != fixed_line:
                lineno = original_lineno[i+1]
                raise FileStoreError(
                    f"On line {lineno} of .gitignore: "
                    f"expected {fixed_line}"
                )
        # 3. Parse known files:
        encrypted_files: dict[str, ManagedFile] = {}
        folders: set[tuple[str, ...]] = set()
        plaintext_files: set[str] = set()
        for idx, line in enumerate(lines[len(FIXED_LINES):]):
            lineno = original_lineno[idx + len(FIXED_LINES)+1]
            # 3.1. Lines must start with !:
            if not line.startswith("!"):
                raise FileStoreError(
                    f"On line {lineno} of .gitignore: "
                    "expected line to start by !"
                )
            # 3.2. Lines that end with / are folders:
            if line.endswith("/"):
                folders.add(tuple(line[1:].split("/")[:-1]))
                continue
            # 3.3 Lines that end with .remote-hash must be preceded by .secret:
            if line.endswith(".remote-hash"):
                if line[1:-12] not in encrypted_files:
                    raise FileStoreError(
                        f"On line {lineno} of .gitignore: "
                        f"{line[1:-12]}.remote-hash must be "
                        f"preceded by {line[1:-12]}.secret"
                    )
                continue
            # 3.4 Lines which don't end by .secret are plaintext file lines
            if not line.endswith(".secret"):
                filename = line[1:]
                if filename in encrypted_files:
                    raise FileStoreError(
                        f"On line {lineno} of .gitignore: "
                        f"filename {filename} is both plaintext and encrypted."
                    )
                plaintext_files.add(filename)
                continue
            # Line ends with .secret, this is an encrypted file.
            # 3.5 Validate filename:
            try:
                file = ManagedFile(filename := line[1:-7], key)
            except FilenameError as e:
                raise FileStoreError(
                    f"On line {lineno} of .gitignore: {e}"
                ) from None
            # 3.6 Check that filename is not repeated and not plaintext:
            if filename in encrypted_files:
                raise FileStoreError(
                    f"On line {lineno} of .gitignore: "
                    f"filename {filename} is repeated."
                )
            if filename in plaintext_files:
                raise FileStoreError(
                    f"On line {lineno} of .gitignore: "
                    f"filename {filename} is both encrypted and plaintext."
                )
            # 3.7 Check that ancestor folders are all known:
            if "/" in filename:
                path = tuple(filename.split("/"))[:-1]
                for i in range(1, len(path) + 1):
                    if path[:i] not in folders:
                        path_str = "/".join(path[:i]) + "/"
                        raise FileStoreError(
                            f"On line {lineno} of .gitignore: "
                            f"ancestor folder {path_str} of {filename} "
                            "is not known."
                        )
            # 3.8 Add file to encrypted files:
            encrypted_files[filename] = file
        # 4. Update internal state:
        self.__managed_files = encrypted_files
        self.__folders = {"/".join(folder)+"/" for folder in folders}
        self.__unmanaged_files = plaintext_files
        self.__loaded = True
