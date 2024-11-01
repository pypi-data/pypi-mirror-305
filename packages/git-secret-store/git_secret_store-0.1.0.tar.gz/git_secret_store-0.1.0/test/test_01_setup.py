
import os
from git_secret.filestore import FileStore
from git_secret.keystore import KeyStore
from git_secret.mnemonic import Mnemonic
from git_secret.utils import sha256_hash

import pathlib

def _test_init_outcome() -> None:
    assert os.path.exists(".gitignore")
    with open(".gitignore", "r", encoding="utf-8") as f:
        assert f.read() == "*\n*/\n!.gitignore\n!.keyhash\n"

def test_init_clean(tmp_path: pathlib.Path) -> None:
    os.chdir(tmp_path)
    filestore = FileStore()
    assert filestore.init()
    _test_init_outcome()

def test_init_unclean(tmp_path: pathlib.Path) -> None:
    os.chdir(tmp_path)
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write("")
    filestore = FileStore()
    assert not filestore.init()
    assert filestore.init(force=True)
    _test_init_outcome()

def _test_keygen_outcome(keystore: KeyStore) -> None:
    assert os.path.exists(".mnemonic")
    assert os.path.exists(".keyhash")
    with open(".mnemonic", "r", encoding="utf-8") as f:
        mnemonic_lines = f.read()
    mnemonic = Mnemonic(words=mnemonic_lines.splitlines())
    assert keystore.mnemonic == mnemonic
    assert keystore.key == bytes(mnemonic)
    with open(".keyhash", "rb") as f:
        assert f.read() == sha256_hash(keystore.key)
    assert keystore.keycheck()

def test_keygen_clean(tmp_path: pathlib.Path) -> None:
    os.chdir(tmp_path)
    filestore = FileStore()
    keystore = filestore.keystore
    assert filestore.init()
    assert keystore.keygen()
    _test_keygen_outcome(keystore)

def test_keygen_unclean(tmp_path: pathlib.Path) -> None:
    os.chdir(tmp_path)
    filestore = FileStore()
    keystore = filestore.keystore
    assert filestore.init()
    with open(".keyhash", "wb") as f:
        f.write(b"")
    assert not keystore.keygen()
    assert not keystore.keycheck()

def test_keygen_rehash(tmp_path: pathlib.Path) -> None:
    os.chdir(tmp_path)
    filestore = FileStore()
    keystore = filestore.keystore
    assert filestore.init()
    assert keystore.keygen()
    os.remove(".keyhash")
    assert not keystore.keycheck()
    assert keystore.keygen(rehash=True)
    _test_keygen_outcome(keystore)
