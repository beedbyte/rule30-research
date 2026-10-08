"""Meaningful cross-checks of independent Rule 30 implementations.

Run from the project root with: python -m unittest discover -s src -p 'test_*.py'
"""

import random
import unittest

from rule30 import (
    bitset_rows,
    center_column,
    reference_rows,
    unpack_column,
)


class Rule30Tests(unittest.TestCase):
    def test_known_initial_rows_and_center(self):
        expected_rows = (
            "1",
            "111",
            "11001",
            "1101111",
            "110010001",
            "11011110111",
        )
        rows = reference_rows()
        self.assertEqual(tuple("".join(map(str, next(rows))) for _ in expected_rows), expected_rows)
        center = unpack_column(center_column(12), 12)
        self.assertEqual("".join(map(str, center)), "110111001100")

    def test_full_rows_for_random_finite_seeds(self):
        rng = random.Random(30030)
        for width in range(1, 20):
            for _ in range(8):
                seed = tuple(rng.randrange(2) for _ in range(width))
                reference = reference_rows(seed)
                bitset = bitset_rows(seed)
                for t in range(35):
                    cells = next(reference)
                    bits, bit_width = next(bitset)
                    self.assertEqual(bit_width, width + 2 * t)
                    self.assertEqual(cells, tuple((bits >> i) & 1 for i in range(bit_width)))

    def test_single_seed_center_across_engines(self):
        count = 512
        self.assertEqual(center_column(count, engine="reference"), center_column(count, engine="bitset"))

    def test_moving_right_edge_frame(self):
        # Independent of both finite-row indexing conventions: bit k is
        # x(t,t-k).  The center is bit t.
        moving_bits = 1
        column = unpack_column(center_column(1024), 1024)
        for t, expected in enumerate(column):
            self.assertEqual((moving_bits >> t) & 1, expected)
            moving_bits ^= (moving_bits << 1) | (moving_bits << 2)

    def test_packing_partial_byte(self):
        for count in range(0, 26):
            packed = center_column(count)
            self.assertEqual(len(packed), (count + 7) // 8)
            if count % 8:
                self.assertEqual(packed[-1] >> (count % 8), 0)


if __name__ == "__main__":
    unittest.main()
