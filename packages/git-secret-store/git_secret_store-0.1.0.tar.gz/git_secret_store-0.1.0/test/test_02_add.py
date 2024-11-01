
import os
from git_secret.filestore import FileStore
from git_secret.keystore import KeyStore
from git_secret.mnemonic import Mnemonic
from git_secret.utils import sha256_hash

import pathlib
import pytest

def test_add(tmp_path: pathlib.Path) -> None:
    FILENAME = "testfile.txt"
    os.chdir(tmp_path)
    filestore = FileStore()
    assert filestore.init()
    assert filestore.keystore.keygen()
    assert not filestore.add([FILENAME])
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("Test file contents.")
    assert filestore.add([FILENAME])
    # TODO: check .gitignore contents.
