# Repository maintenance

A separate workspace is not required. The repository is the persistent scientific record and can be maintained from the existing Chat.

## Repository scope

Maintain the research account, proofs, attribution, numerical checks, and verification records. Keep editorial planning outside the scientific reading route.

Use [the results index](research/RESULTS.md) to locate each established result and its precise scope. Read `research/AUTHOR_ACCOUNT.md` for the physical account and `research/PROOF_MAP.md` for the foundational dependencies. The two time-dependent proofs are complementary, not duplicate accounts:

- `research/FINITE_TIME_CERTIFICATE.md` bounds the sharp event at a deterministic time through static spectral quantities. Its event-local continuum error is compared with the square root of the rare probability. Fourier smoothing and auxiliary momentum margins do not change the source or detector.
- `research/OBSERVATION_TIME.md` controls the relevant continuum and band norms near resonance and gives a sufficient joint time–detuning regime. For fixed relative accuracy the bound holds at every sufficiently late deterministic time. It is neither an optimal waiting-time law nor an interval-certified numerical operating window.

The detuning theorem describes the limiting measure. A finite-time rare-event detection guarantee requires the separate time-dependent bounds under their stated assumptions. The [alternative finite-time estimate](research/ALTERNATIVE_TIME_BOUND.md) gives a complementary conservative derivation. Use the exact lattice edge in an on-shell resolvent. Retain both source/detector overlap factors, unconditional probability normalization, and the stated order of limits. A narrow continuous spectral peak is not another bound-state atom; a linewidth is not a proved full-amplitude relaxation time.

Further changes should reconcile a specific scientific issue or incorporate an explicit author request. Do not automatically enlarge the Hamiltonian, add a device model, optimize every sufficient constant, or replace the local preparation to strengthen the presentation. A documented limitation is part of the result, not a request for an unrelated extension.

## Authority and preservation

The user authorizes modifications and merge only in `GoGoKo699/Resonant-Dimer-Transport`. This permission does not transfer to another repository. Before writing, inspect live main and open changes; preserve concurrent work. Use a feature branch, verify the actual proposed head, merge with an expected-head guard, and verify merged main separately.

Follow `AGENTS.md` and `REPRODUCIBILITY.md`. Preserve the immutable source archives, scientific assertions, numerical tolerances, canonical reports, and license. These live instructions govern maintenance.
