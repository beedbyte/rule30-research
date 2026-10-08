# Test report

Run on 8 October 2026 in the staged directory with Python 3.12.1:

```sh
python -B -m unittest discover -s src -p 'test_*.py' -v
```

Result: **5 tests passed** in 0.211 seconds on the final staged copy.

| Test | Check |
| --- | --- |
| `test_known_initial_rows_and_center` | Six known initial rows and 12 center bits match fixed expected values. |
| `test_full_rows_for_random_finite_seeds` | Reference and bitset evolvers agree for 152 deterministic seeds of widths 1–19 over 35 rows each. |
| `test_single_seed_center_across_engines` | Both evolvers agree on the first 512 center bits. |
| `test_moving_right_edge_frame` | A separate moving-frame recurrence agrees on the first 1,024 center bits. |
| `test_packing_partial_byte` | Packed output length and unused high bits are checked for requests of 0–25 bits. |

All three copied files match the source-project SHA-256 hashes listed in [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md). A case-insensitive scan of the copied specification and Python files for credential and private-network markers found no matches. The package contains no environment file.

These tests check implementation consistency and selected finite outputs. They do not verify eventual nonperiodicity or any other infinite-time claim.
