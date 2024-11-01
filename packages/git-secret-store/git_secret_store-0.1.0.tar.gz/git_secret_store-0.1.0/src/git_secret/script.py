"""
Script for managing a secret store based on the .gitignore file.
"""

from __future__ import annotations

import argparse

from .filestore import FileStore


def _add_encrypt_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the encrypt command."""
    encrypt_subparser = subparsers.add_parser(
        "encrypt", help="Encrypts managed files."
    )
    encrypt_subparser.add_argument(
        "-f",
        "--force",
        help=(
            "If set, overwrites ciphertexts on managed files "
            "with updated-remote or updated-both status."
        ),
        action="store_true",
    )
    encrypt_subparser.add_argument(
        "filenames",
        help=(
            "Managed files to be encrypted. "
            "If none are specified, all managed files will be encrypted."
        ),
        type=str,
        nargs="*",
    )


def _add_decrypt_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the decrypt command."""
    decrypt_subparser = subparsers.add_parser(
        "decrypt", help="Decrypts managed files."
    )
    decrypt_subparser.add_argument(
        "-f",
        "--force",
        help=(
            "If set, overwrites plaintext on managed files "
            "with updated-local or updated-both status."
        ),
        action="store_true",
    )
    decrypt_subparser.add_argument(
        "filenames",
        help=(
            "Files to be decrypted. "
            "If none are specified, all managed files will be decrypted."
        ),
        type=str,
        nargs="*",
    )


def _add_add_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the add command."""
    add_subparser = subparsers.add_parser(
        "add", help="Adds files to the list of managed files."
    )
    add_subparser.add_argument(
        "filenames",
        help=(
            "Files to be added to the list of managed files. "
            "If none are specified, files will be added interactively."
        ),
        type=str,
        nargs="*",
    )


def _add_add_unmanaged_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the add-unmanaged command."""
    add_unmanaged_subparser = subparsers.add_parser(
        "add-unmanaged", help="Adds files to the list of unmanaged files."
    )
    add_unmanaged_subparser.add_argument(
        "filenames",
        help="Files to be added to the list of unmanaged files.",
        type=str,
        nargs="*",
    )


def _add_check_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the check command."""
    check_subparser = subparsers.add_parser(
        "check", help="Checks status of managed files."
    )
    check_subparser.add_argument(
        "-d",
        "--deep",
        help="If set, also check for integrity of ciphertext and remote hash.",
        action="store_true",
    )
    check_subparser.add_argument(
        "filenames",
        help=(
            "Files to be checked. "
            "If none are specified, all managed files will be checked."
        ),
        type=str,
        nargs="*",
    )


def _add_list_unmanaged_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the list-unmanaged command."""
    list_unmanaged_subparser = subparsers.add_parser(
        "list-unmanaged", help="Lists unmanaged files."
    )

def _add_fix_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the fix command."""
    fix_subparser = subparsers.add_parser(
        "fix", help="Attempts to fix any known errors on managed files."
    )
    fix_subparser.add_argument(
        "filenames", help="Files to be fixed.", type=str, nargs="*"
    )


def _add_keycheck_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the keycheck command."""
    keycheck_subparser = subparsers.add_parser(
        "keycheck", help="Checks status of secret key."
    )


def _add_keygen_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the keygen! command."""
    keygen_subparser = subparsers.add_parser(
        "keygen!", help="<ADMIN> Generates a new secret key."
    )
    keygen_subparser.add_argument(
        "-R",
        "--rehash",
        help="If set, a missing key hash is regenerated from an existing key.",
        action="store_true",
    )


def _add_clear_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the clear! command."""
    clear_subparser = subparsers.add_parser(
        "clear!",
        help=(
            "<ADMIN> Clears ciphertext, local hash and remote hash files."
        )
    )
    clear_subparser.add_argument(
        "-f",
        "--force",
        help=(
            "If set, clears files regardless of file status. "
            "Otherwise, only considers managed files with status: "
            "unchanged, local-only, updated-local, or missing."
        ),
        action="store_true",
    )
    clear_subparser.add_argument(
        "filenames",
        help=(
            "Files whose ciphertext, local hash and remote hash files are to "
            "be cleared. If none are specified, all managed files will be "
            "considered for clearance (subject to file status)."
        ),
        type=str,
        nargs="*",
    )


def _add_format_gitignore_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the format-gitignore! command."""
    format_gitignore_subparser = subparsers.add_parser(
        "format-gitignore!", help="<ADMIN> Formats the .gitignore file."
    )

def _add_init_subparser(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Adds subparser for the init! command."""
    init_subparser = subparsers.add_parser(
        "init!",
        help="<ADMIN> Inits the repository for secret storage."
    )
    init_subparser.add_argument(
        "-f",
        "--force",
        help="If set, overwrites the current .gitignore file, if present.",
        action="store_true",
    )

def parse_args() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="secret-store",
        description="Manages a store of secrets based on a Git repository.",
    )
    subparsers = parser.add_subparsers(
        title="subcommands",
        description="Available commands:",
        dest="command",
        required=True,
    )
    _add_encrypt_subparser(subparsers)
    _add_decrypt_subparser(subparsers)
    _add_add_subparser(subparsers)
    _add_add_unmanaged_subparser(subparsers)
    _add_check_subparser(subparsers)
    _add_list_unmanaged_subparser(subparsers)
    _add_fix_subparser(subparsers)
    _add_keycheck_subparser(subparsers)
    _add_init_subparser(subparsers)
    _add_keygen_subparser(subparsers)
    _add_clear_subparser(subparsers)
    _add_format_gitignore_subparser(subparsers)
    return parser.parse_args()


def main() -> None:
    """Main entry point for the git-secret command-line utility."""
    args = parse_args()
    filestore = FileStore()
    keystore = filestore.keystore
    match args.command:
        case "encrypt":
            filestore.encrypt(args.filenames, force=args.force)
        case "decrypt":
            filestore.decrypt(args.filenames, force=args.force)
        case "add":
            if args.filenames:
                filestore.add(args.filenames)
            else:
                filestore.add_interactive()
        case "add-unmanaged":
            filestore.add_unmanaged(args.filenames)
        case "fix":
            filestore.fix(args.filenames)
        case "check":
            filestore.check(args.filenames, deep=args.deep)
        case "list-unmanaged":
            filestore.list_unmanaged()
        case "keycheck":
            keystore.keycheck()
        case "init!":
            filestore.init(force=args.force)
        case "keygen!":
            keystore.keygen(rehash=args.rehash)
        case "clear!":
            filestore.clear(args.filenames, force=args.force)
        case "format-gitignore!":
            filestore.format_gitignore()
