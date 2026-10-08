# Canonical specification

## Dynamics

The state `x(t,n)` lies in `{0,1}` for `t ∈ ℕ` and `n ∈ ℤ`. The initial condition is `x(0,0)=1` and `x(0,n)=0` for `n ≠ 0`. The simultaneous update is

`x(t+1,n) = x(t,n-1) XOR (x(t,n) OR x(t,n+1))`.

Here `L=x(t,n-1)`, `C=x(t,n)`, `R=x(t,n+1)`. The ordered truth table is `111→0`, `110→0`, `101→0`, `100→1`, `011→1`, `010→1`, `001→1`, `000→0`. Positions increase to the right. The support at time `t` lies in `[-t,t]`, so finite-window implementations may take all cells outside that interval to be zero.

The center sequence is `c_t=x(t,0)` for `t≥0`.

## Exact question

The prize target is the statement

`∀p∈ℕ, p≥1 ⇒ ∀T∈ℕ, ∃t∈ℕ, t≥T ∧ c_t≠c_(t+p)`.

Its negation is *eventual periodicity*: `∃T≥0, ∃p≥1, ∀t≥T, c_(t+p)=c_t`. Ordinary periodicity is the special case `T=0`. The target does not follow from the whole spacetime orbit being aperiodic, aperiodicity of an adjacent pair, empirical balance, randomness heuristics, or finite period searches without a quantified argument.

## Claim discipline

Every claim in this repository must be marked `PROVED`, `COMPUTATIONALLY VERIFIED FOR FINITE RANGE`, `HEURISTIC`, `CONJECTURE`, `DISPROVED`, or `UNKNOWN`. A `PROVED` entry needs a precise statement and a complete argument. Finite computations need source, parameters, output, runtime, and, where useful, artifact hashes. The auditor records `PASS`, `FAIL`, or `UNRESOLVED` separately. Novelty claims require a documented literature check.

For a claimed complete proof, independently verify numerical consequences, run adversarial audit, obtain an independent proof reconstruction, inspect prior art, formalize critical lemmas where practical, test quantified intermediate claims over large finite ranges, and present a minimal proof. Until these stages succeed, the status is at most `CANDIDATE COMPLETE PROOF`.
