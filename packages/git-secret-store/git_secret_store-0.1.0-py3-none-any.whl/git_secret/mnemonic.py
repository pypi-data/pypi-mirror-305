"""
A modified and heavily simplified version of BIP 39 mnemonics, originally from:

https://github.com/trezor/python-mnemonic
"""

# Copyright (c) 2013 Pavol Rusnak
# Copyright (c) 2017 mruddy
# Copyright (c) 2024 Hashberg Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations
from collections.abc import Iterable, Iterator
import hashlib
import itertools
import secrets
from typing import Any, Self, final, overload
from ._english_words import WORD_IDX, WORD_LIST

@final
class Mnemonic:
    """Implementation of English BIP 39 Mnemonics."""

    @staticmethod
    def random(strength: int) -> Mnemonic:
        """
        Create a new mnemonic using a random generated number as entropy.
        As defined in BIP39, the entropy must be a multiple of 32 bits,
        and its size must be between 128 and 256 bits. Therefore the possible
        values for 'strength' are 128, 160, 192, 224 and 256.
        """
        if strength not in [128, 160, 192, 224, 256]:
            raise ValueError(
                "Invalid strength value. "
                "Allowed values are [128, 160, 192, 224, 256]."
            )
        return Mnemonic(entropy=secrets.token_bytes(strength // 8))

    @overload
    def __new__(cls, *, words: Iterable[str], entropy: None = None) -> Self: ...

    @overload
    def __new__(cls, *, entropy: bytes, words: None = None) -> Self: ...

    def __new__(
        cls,
        *,
        words: Iterable[str] | None = None,
        entropy: bytes | None = None,
    ) -> Self:
        """
        Constructs a mnemonic from words or entropy (exactly one must be given).
        """
        if words is not None:
            assert entropy is None
            words = tuple(words)
            entropy = Mnemonic.__words_to_entropy(words)
        else:
            assert entropy is not None
            words = Mnemonic.__entropy_to_words(entropy)
        self = super().__new__(cls)
        self.__words = words
        self.__entropy = entropy
        return self

    __words: tuple[str, ...]
    __entropy: bytes

    def __str__(self) -> str:
        """Returns the mnemonic as a space-separated string."""
        return " ".join(self.__words)

    def __bytes__(self) -> bytes:
        """Returns the entropy as bytes."""
        return self.__entropy

    def __iter__(self) -> Iterator[str]:
        """Iterates over the words of the mnemonic."""
        return iter(self.__words)

    def __len__(self) -> int:
        """Returns the number of words in the mnemonic."""
        return len(self.__words)

    def __eq__(self, other: Any) -> bool:
        """Compares two mnemonics for equality."""
        if isinstance(other, Mnemonic):
            return self.__words == other.__words
        return NotImplemented

    def __hash__(self) -> int:
        """Returns the hash of the mnemonic."""
        return hash(self.__words)

    @staticmethod
    def __words_to_entropy(words: tuple[str, ...]) -> bytes:
        """
        Utility function to convert a list of words to the original entropy.

        Adapted from <http://tinyurl.com/oxmn476>

        :raises ValueError: If the words don't form a valid mnemonic.
        """
        # 1. Validate number of words in the mnemonic:
        if len(words) not in [12, 15, 18, 21, 24]:
            raise ValueError(
                "Number of words must be 12, 15, 18, 21, or 24, "
                f"found {len(words)} instead."
            )
        # 2. Reconstruct entropy and checksum from words:
        concatLenBits = len(words) * 11
        concatBits = [False] * concatLenBits
        wordindex = 0
        for word in words:
            # Find the word's index in the list:
            ndx = WORD_IDX.get(word)
            if ndx is None:
                raise ValueError(f"Unable to find {word!r} in word list.")
            # Set the next 11 bits to the value of the index:
            for ii in range(11):
                concatBits[(wordindex * 11) + ii] = (
                    ndx & (1 << (10 - ii))
                ) != 0
            wordindex += 1
        # Compute checksum length and entropy length, in bits:
        checksumLengthBits = concatLenBits // 33
        entropyLengthBits = concatLenBits - checksumLengthBits
        # 3. Extract original entropy as bytes:
        entropy = bytearray(entropyLengthBits // 8)
        for ii in range(len(entropy)):
            for jj in range(8):
                if concatBits[(ii * 8) + jj]:
                    entropy[ii] |= 1 << (7 - jj)
        # 4. Take the SHA-256 digest of the entropy:
        hashBytes = hashlib.sha256(entropy).digest()
        hashBits = list(
            itertools.chain.from_iterable(
                [c & (1 << (7 - i)) != 0 for i in range(8)] for c in hashBytes
            )
        )
        # 5. Check all the checksum bits, then return the entropy:
        for i in range(checksumLengthBits):
            if concatBits[entropyLengthBits + i] != hashBits[i]:
                raise ValueError("Failed checksum for mnemonic words.")
        return bytes(entropy)

    @staticmethod
    def __entropy_to_words(entropy: bytes) -> tuple[str, ...]:
        """
        Utility function to convert entropy to a list of words.

        As defined in BIP39, the entropy must be a multiple of 32 bits,
        and its size must be between 128 and 256 bits.
        The return is a tuple of words that encodes the generated entropy.

        :raises ValueError: If the entropy has incorrect number of bytes.
        """
        # 1. Validate entropy length:
        if len(entropy) not in [16, 20, 24, 28, 32]:
            raise ValueError(
                "Entropy length should be 16, 20, 24, 28, or 32, "
                f"found {len(entropy)} instead."
            )
        # 2. Compute entropy digest:
        h = hashlib.sha256(entropy).hexdigest()
        # 3. Compute word-selecting bitstring from entropy and digest:
        b = (
            bin(int.from_bytes(entropy))[2:].zfill(len(entropy) * 8)
            + bin(int(h, 16))[2:].zfill(256)[: len(entropy) * 8 // 32]
        )
        # 4. Select words from the word list, then return them:
        words = []
        for i in range(len(b) // 11):
            idx = int(b[i * 11 : (i + 1) * 11], 2)
            words.append(WORD_LIST[idx])
        return tuple(words)
