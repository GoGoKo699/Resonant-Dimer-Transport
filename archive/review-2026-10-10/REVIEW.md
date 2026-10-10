# Proof and contribution review

10 October 2026. This pass continues only the resonant moving-dimer calculation. The incoming source is `prior/FOLLOWUP.md`; the earlier spectral source is `prior/prior/PILOT.md`. All forty imported files are unchanged. No repository is created, read, modified or merged.

## Review outcome

No blocking mathematical defect was identified in the scoped infinite-lattice contact-transport theorem. The potentially consequential steps were checked explicitly: cusp versus smooth continuum edges, absence of a source-coupled atom at a continuum energy, the finite exceptional set needed to exclude singular continuous contact spectrum, both source/detector overlaps, passage from amplitude convergence to the whole unnormalized contact probability law, and the characteristic-function rather than uncontrolled stationary-phase proof. The long-time/high-velocity order remains essential.

A corollary completes the size interpretation already present in the same eigenstate: the scaled normalized relative wavefunction converges in L2, hence the best overlap with a relative source of radius R has a limiting profile in PR. Fixed capture probability requires R of order 1/P, or order (v/J)^(1/(1-z)). This does not construct a physical loading protocol or grant momentum selection to the original local quench.

The finite-time perturbation estimate |delta probability| <= t|delta U| is another elementary corollary. It does not provide the missing uniform-in-velocity continuum-convergence rate or an optimal tuning requirement.

## Strongest predecessor reconstruction

### Sun--Feng--Zhang

Read the primary published two-magnon section at Eqs. (5)--(8), the later negative-energy three-magnon discussion, and compare with the readable v1 preprint, whose arbitrary-momentum T-matrix is Eq. (5). The published article is *Efimov effect in long-range quantum spin chains*, Communications Physics **9**, 146 (2026), arXiv:2502.20759.

Primary published text: https://www.nature.com/articles/s42005-026-02580-0
Primary v1 text: https://arxiv.org/html/2502.20759v1

At resonance, subtract their zero-momentum zero-energy loop, put k=P and E=J|P|^z e, and rescale q=|P|x. This gives precisely |P|^(1-z)F_z(e)/(2J). The pole equation is thus supplied by their effective theory. Its derivative determines the residue exponent. Once local creation and local detection contribute two overlaps, ordinary pushforward of momentum to band velocity gives the tail exponent. The new wavefunction-scaling corollary is also based on the same contact pole, not a new universality principle.

Their inspected two-body discussion explicitly evaluates the rest bound pole and then applies finite momentum at negative energies in the three-body equation. I did not find our complete positive-energy below-fixed-momentum-continuum local-quench theorem stated in those passages. That absence is not proof that none of its consequences are implicit; the reconstruction above identifies the direct implications rather than relying on the absence of a phrase.

### Kranzl and collaborators

Read the primary HTML of *Observation of magnon bound states in the long-range, anisotropic Heisenberg model*, arXiv:2212.03899v2, especially Sections III--IV and the discussion of bound-state participation. It supplies the directly relevant distinction between unbounded single-magnon velocity and finite velocity for the bound branch in its chosen regime. Its local neighboring-magnon preparation and nearby-pair measurements are precedents for the observable.

https://arxiv.org/html/2212.03899v2

The primary text specifies exponent 1.4 for that experimental realization, different interactions, and a repulsively bound branch. Our z interval corresponds to hopping exponents strictly between 1.5 and 2. No figure value, experimental velocity, or advertised operating window has been extracted for the present model. Their data are not reanalyzed or refuted. A word such as 'always' in a discussion of their selected branch is not an unrestricted theorem about every model of binding.

### Other inherited ingredients and source-access boundaries

The Albeverio--Lakaev--Makarov--Muminov primary record was checked again. It explicitly establishes nonzero-momentum below-threshold spectrum from a rest eigenvalue/virtual level under its three-dimensional positivity-preserving hypotheses. The full theorem reading is recorded in the preserved pilot rather than newly claimed here. https://arxiv.org/abs/math-ph/0501013

The Ciaurri--Roncal--Stinga--Torrea--Varona primary record confirms the fractional lattice operator and its established kernel framework. Its detailed formulas were read in the pilot; they are not a new model ingredient. https://arxiv.org/abs/1608.08913

Frymark--Liaw's rank-one spectral formulas and Fukuhara's local magnon observation remain credited from the preserved source readings. This pass's attempted HTML routes did not return those bodies, so a fresh full-text reread is not claimed. The original formulas and their source roles were checked against the explicit derivation here.

The Dominguez-Castro primary article returned HTTP 429 on this pass. Its earlier two-species power-law model comparison remains in the preserved pilot. Failure to reread it does not support an absence claim. No new source-access hold is asserted as proof of novelty.

Targeted searches using bound pairs, fractional dispersion, resonance, and long-range hopping did not reveal a directly covering complete local-quench theorem. Search coverage is neither exhaustive nor a priority certificate. Unrelated topological edge-state and single-magnon sources were not used to support the dimer result. Figures or diagrams were not required for the equations used in this review.

## Contribution judgment

**GO for a bounded project record and focused author-facing assessment.** The result has a definite microscopic statement, a specified unconditioned position event, a complete asymptotic answer, and explicit restrictions from source weight and pair size. It answers the original local-preparation objection rather than substituting a new problem. A dedicated record is appropriate; no repository was created during this pass.

The positive case is the failure of finite-velocity regularization by binding at a resonance, demonstrated in a local observation rather than only a pole plot. The skeptical case is substantial: the two-body framework is already available, the central exponent is ordinary residue/velocity power counting, the strict distinction requires resonance tuning and iterated limits, and the high-speed events are rare. The available result is not a demonstration of efficient superballistic transport. Familiar tools and rare events do not automatically make a theorem insignificant, but neither does proving a sharp asymptotic formula establish PRL-level broad interest.

Keep the central claim as the source-resolved resonance contrast. Do not create separate novelty headlines from the scaling profile, gamma-function coefficients, generic pushforward exponent, or elementary Duhamel continuity bound. No many-body, disordered, lossy, or alternate-device expansion is needed merely to make this bounded result assessable.

Suggested working repository name: **Resonant-Dimer-Transport**. It has not been checked or created. The existing repositories and manuscript programmes remain protected.
