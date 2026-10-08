"""Two independent finite Rule 30 evolvers.

Rows use increasing spatial position from left to right.  For the single-cell
seed, row t covers positions -t,...,t and its center is row[t].  These
functions make no claim about infinite-time behavior.
"""

from __future__ import annotations

from typing import Iterable, Iterator


# Lookup indexed by the binary neighborhood L C R, from 000 through 111.
_RULE_30_TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def reference_step(row: tuple[int, ...]) -> tuple[int, ...]:
    """Evolve a finite row with zero cells outside its represented interval."""
    if not row or any(bit not in (0, 1) for bit in row):
        raise ValueError("row must be a nonempty tuple of binary digits")
    width = len(row)
    result = []
    for i in range(width + 2):
        left = row[i - 2] if 0 <= i - 2 < width else 0
        center = row[i - 1] if 0 <= i - 1 < width else 0
        right = row[i] if i < width else 0
        result.append(_RULE_30_TABLE[(left << 2) | (center << 1) | right])
    return tuple(result)


def bitset_step(bits: int, width: int) -> tuple[int, int]:
    """Evolve a finite row encoded with its leftmost cell as least bit.

    In the new row, target index i receives old cells i-2, i-1, and i as
    left, center, and right.  Therefore L is bits<<2, C is bits<<1, and R is
    bits.  Rule 30 gives L XOR (C OR R).
    """
    if width < 1 or bits < 0 or bits >= (1 << width):
        raise ValueError("bits must fit a nonempty row of the stated width")
    new_width = width + 2
    new_bits = ((bits << 2) ^ ((bits << 1) | bits)) & ((1 << new_width) - 1)
    return new_bits, new_width


def reference_rows(seed: Iterable[int] = (1,)) -> Iterator[tuple[int, ...]]:
    """Yield successive rows from a finite seed, including time zero."""
    row = tuple(seed)
    if not row or any(bit not in (0, 1) for bit in row):
        raise ValueError("seed must be a nonempty sequence of binary digits")
    while True:
        yield row
        row = reference_step(row)


def bitset_rows(seed: Iterable[int] = (1,)) -> Iterator[tuple[int, int]]:
    """Yield (bits, width) pairs from a finite seed, including time zero."""
    row = tuple(seed)
    if not row or any(bit not in (0, 1) for bit in row):
        raise ValueError("seed must be a nonempty sequence of binary digits")
    bits = sum(bit << i for i, bit in enumerate(row))
    width = len(row)
    while True:
        yield bits, width
        bits, width = bitset_step(bits, width)


def center_column(count: int, *, engine: str = "bitset") -> bytes:
    """Return c_0,...,c_(count-1), packed least-significant-bit first.

    The final byte's unused high bits are zero.  An empty request returns
    empty bytes.  This function uses the single black cell at position zero.
    """
    if count < 0:
        raise ValueError("count must be nonnegative")
    if engine not in ("bitset", "reference"):
        raise ValueError("engine must be bitset or reference")
    output = bytearray((count + 7) // 8)
    if engine == "bitset":
        bits, width = 1, 1
        for t in range(count):
            output[t >> 3] |= ((bits >> t) & 1) << (t & 7)
            bits, width = bitset_step(bits, width)
    else:
        row = (1,)
        for t in range(count):
            output[t >> 3] |= row[t] << (t & 7)
            row = reference_step(row)
    return bytes(output)


def unpack_column(packed: bytes, count: int) -> tuple[int, ...]:
    """Decode exactly count packed column bits."""
    if count < 0 or len(packed) != (count + 7) // 8:
        raise ValueError("packed length and count are inconsistent")
    return tuple((packed[t >> 3] >> (t & 7)) & 1 for t in range(count))
