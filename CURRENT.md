# Current work: continue in Chat

This project continues in the existing Chat. A separate workspace is not required, and progress is not conditional on workspace quota becoming available. The repository is the persistent scientific record.

## Scientific account and next bounded task

Read `research/AUTHOR_ACCOUNT.md` for the claims-first account, then `research/PROOF_MAP.md` and `research/THRESHOLD_ENDPOINT.md`. The endpoint correction uses the exact lattice threshold rather than the continuum energy approximation. It does not change the resonant pole, velocity tail, or preparation-size claims. `maintenance/CONTINUATION_REVIEW.json` records its scope and the source comparison. The detuning theorem alone is not a finite-time rare-event detection guarantee or efficient superballistic transport.

The detuning result is now proved in `research/DETUNING_CROSSOVER.md`: the global maximum velocity is asymptotic to K_z J/delta, every maximizing momentum is of order delta^(1/(1-z)), and the unconditional probability near a fixed fraction of that cutoff is of order delta^((4z-1)/(1-z)). The proof includes compact derivative convergence, exclusion of competing momentum scales, and the source/detector-weighted crossover. The inherited scattering framework is still credited; this is not a new interaction or general universality claim.

The finite-time estimate is in `research/FINITE_TIME_CERTIFICATE.md`. It controls the sharp coincidence event at every specified time by a velocity-shell term, a quantitative band error, and an event-local continuum amplitude error. A sufficient deterministic observation time is expressed in static spectral variation and band norms; their finiteness is proved. The continuum error only needs to be small compared with the square root of the rare-event probability. Neither momentum exclusion nor Fourier smoothing in the proof modifies the preparation or detector.

The static-budget dependence is controlled in `research/OBSERVATION_TIME.md`. Its momentum-integrated continuum norm is at most C/(Jt) uniformly near resonance; fiberwise variation is allowed to diverge as |P|^(z-1). Sharper band norms yield a sufficient joint time–detuning regime. At z=3/4, Jt delta^7/sqrt(log(2/delta)) tending to infinity recovers the asymptotic near-cutoff probability at the actual deterministic observation time. This is not an optimal time exponent or a numerical operating window. The piecewise exponent is a feature of the sufficient estimate, not an asserted phase transition. The continuous spectral peak in Section 5 is not another bound-state atom.

The next bounded task is to compress the physical account for a manuscript and stress-test its decisive proof inputs, especially the uniform boundary-resolvent variation estimate. Preserve the distinction between the source-resolved transport claim, its sufficient finite-time justification, and established two-body scattering ingredients. Do not automatically optimize every bound, add more coefficients, or enlarge the Hamiltonian before assessing whether the central physical message stands on its own.

Keep the two source/detector overlap factors, preparation-size restriction, and infinite-lattice/long-time/high-velocity order explicit. Credit the finite-momentum contact scattering framework and other established ingredients. Do not automatically add finite-density particles, disorder, loss, external forces, alternate hopping, or a device implementation.

## Authority and preservation

The user authorizes modifications and merge only in `GoGoKo699/Resonant-Dimer-Transport`. This permission does not transfer to another repository. Before writing, inspect live main and preserve concurrent work. Use a feature branch, verify the actual proposed head, merge with an expected-head guard, and verify merged main separately.

Follow `AGENTS.md` and `REPRODUCIBILITY.md`. Preserve the imported research files, historical failed runs, scientific assertions, numerical tolerances, and canonical reports. Current instructions supersede the archived handoff's uncreated-repository and workspace-transfer status, not its scientific statements. Do not repeat initialization over newer work.
