# Rule 30 center-column research

This repository contains a small, reproducible starting point for studying the center column of Rule 30 from a single nonzero cell. It defines the question precisely and provides two finite-row implementations that check one another.

**Status:** The eventual nonperiodicity of this center column is open in this repository. The code computes finite prefixes; no finite computation proves a statement about all future times. This is not a Rule 30 prize submission or a claimed solution.

## The question

Write `x(t,n)` for the cell at time `t` and position `n`, starting with `x(0,0)=1` and zeros elsewhere. The update is

```text
x(t+1,n) = x(t,n-1) XOR (x(t,n) OR x(t,n+1)).
```

For `c_t = x(t,0)`, eventual nonperiodicity asks whether, for every positive period `p` and every starting time `T`, some `t >= T` satisfies `c_t != c_(t+p)`. See [the specification](specification.md) for the truth table, indexing convention, and proof standard.

## Run the checks

Python 3.10 or later is sufficient; the included code has no third-party dependencies.

```sh
python -m unittest discover -s src -p 'test_*.py'
```

`src/rule30.py` implements a cell-by-cell reference step and an integer bitset step. The tests compare full rows for deterministic random finite seeds, compare the first 512 center bits between implementations, and check 1,024 center bits with a third moving-frame recurrence. These checks support the implementation over the stated finite ranges only.

## Scope and provenance

This first public package deliberately contains the specification, finite evolvers, and tests. It does not include ongoing proof drafts, large experimental datasets, or unreviewed prize claims. [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) records the exact local source files and hashes; [TEST_REPORT.md](TEST_REPORT.md) records the checks run on this staged copy.

The Rule 30 center-column prize questions are posed by Stephen Wolfram and the Wolfram Foundation; see [the official prize page](https://rule30prize.org/) and [Wolfram's 2019 announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/). This repository's code and explanatory text were prepared by **Beedbyte**.

## Methods

AI tools assisted drafting and coding for this finite simulation package; the included tests and source manifest make the finite computational claims inspectable. See [ATTRIBUTION.md](ATTRIBUTION.md) for citation guidance.

Website: [beedbyte.tech](https://beedbyte.tech)
