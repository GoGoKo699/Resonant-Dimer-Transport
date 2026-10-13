#!/usr/bin/env python3
"""Generate the scientific reading route from immutable supplied sources."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/review-2026-10-10'
PAGES=[
 ('THEOREM.md','research/THEOREM.md','Resonant dimer transport: local observation and preparation size','## 1. Fixed physical task','## 6. Attribution and assessment'),
 ('prior/FOLLOWUP.md','research/TRANSPORT_PROOF.md','Local-source transport proof','## 1. Same model; specified source and detector','## 8. Verification'),
 ('prior/prior/PILOT.md','research/SPECTRAL_PROOF.md','Spectral foundation of the resonant dimer','## 1. A fully specified microscopic model','## 10. What the next bounded calculation must decide'),
 ('REVIEW.md','research/CONTRIBUTION.md','Contribution and attribution','## Review outcome',None),
]
CONTRIBUTION_TEXT="""## Source-resolved resonance contrast

The result connects the exact fractional-lattice contact pole to a specified
local source and same-site detector. At the rest-binding resonance, the
persistent coincidence signal has an algebraic velocity tail; at each fixed
stronger attraction its limiting support is bounded. The calculation retains
both contact overlaps and the unconditional probability per prepared pair.
The scaled relative wavefunction quantifies the source support required for
fixed overlap, while the finite-time proofs control the sharp event at a
deterministic observation time.

## Established ingredients

| Source | Ingredient and relevant model |
|---|---|
| [Sun, Feng, and Zhang](https://www.nature.com/articles/s42005-026-02580-0) · [preprint v1](https://arxiv.org/html/2502.20759v1) | Their finite-momentum contact loop and resonance subtraction supply the continuum pole equation. Homogeneity predicts the pole, residue, and detuning powers. Their microscopic hard-core spin model and auxiliary-field residues require a separate normalization from the onsite contact probability used here. |
| [Albeverio, Lakaev, Makarov, and Muminov](https://arxiv.org/abs/math-ph/0501013) | Theorem 5.4 establishes motion-induced lattice binding under smooth three-dimensional positivity-preserving hypotheses. Section 3 of the spectral foundation gives the explicit one-dimensional fractional-cusp proof. |
| [Ciaurri, Roncal, Stinga, Torrea, and Varona](https://arxiv.org/abs/1608.08913) | The fractional discrete Laplacian, its exact hopping kernel, and long-distance power law are established model ingredients. |
| [Domínguez-Castro](https://www.mdpi.com/2218-2004/11/8/110) | The two-species power-law hopping model with onsite interaction includes a total-momentum scattering equation and disappearance of attractive rest dimers. |
| [Kranzl and collaborators](https://arxiv.org/html/2212.03899v2) | Local neighboring-magnon preparation and nearby-pair position measurements distinguish bound and scattering propagation. Their selected repulsive hard-core branch has finite velocity in a different interaction and exponent regime. |
| [Fukuhara and collaborators](https://arxiv.org/pdf/1305.6598) | Local two-spin preparation and position correlations resolve free and bound motion in the short-range Heisenberg chain. |
| [Frymark and Liaw](https://arxiv.org/pdf/1904.09833) | The Aronszajn–Krein resolvent identity, point-mass weights, and continuous densities provide the rank-one spectral formulas. |

The [author account](AUTHOR_ACCOUNT.md#relationship-to-established-work)
gives the claim-by-claim comparison, including the published supplements,
public author response, and the local-pair dynamics of Macrì and collaborators.
The exact loop specialization is in
[the spectral foundation](SPECTRAL_PROOF.md#9-relationship-to-established-work).

## What the proofs establish

The additional control is microscopic and measurement-specific: lattice
limits for energy, velocity, and normalized contact weight; continuum contact
separation; the velocity pushforward with two overlaps; the global detuning
cutoff and its absolute probability; and the growing relative-support capture
profile. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) bounds
sharp-event error through static spectral budgets, and
[the joint observation-time theorem](OBSERVATION_TIME.md) proves a sufficient
simultaneous time–detuning regime.

The pole equation, local-pair observation, and motion-induced binding remain
attributed to the sources above. The high-speed coincidence events are rare,
and their internal preparation radius grows with velocity. The resonance
velocity tail takes long time at fixed velocity before high velocity; the
joint theorem states its own simultaneous sufficient regime. The support
result is a fiberwise overlap optimum; the sharp-event error bound retains
the onsite source and same-site detector. The [proof map](PROOF_MAP.md)
locates each complete derivation.
"""
REPLACEMENTS={
 'THEOREM.md': [
  ('Both particle numbers are fixed at one. There is no bath, disorder, external force, many-body background, changing interaction, or measurement during evolution. Lattice spacing and $\\hbar$ are one. The kinetic operator is the established fractional discrete Laplacian, not an exact pure power hopping at short distance and not a claim that an identified apparatus implements its full kernel.',
   'Both particle numbers are fixed at one, and the Hamiltonian is time independent and translation invariant. Lattice spacing and $\\hbar$ are one. The kinetic operator is the established fractional discrete Laplacian, with the exact short-distance kernel specified in the [spectral foundation](SPECTRAL_PROOF.md).'),
  ('They concern the infinite lattice followed by long time. They are not assertions of zero finite-time tails or a finite-density transport transition.',
   'They concern the infinite lattice followed by long time, with finite-time accuracy controlled separately in the [finite-time certificate](FINITE_TIME_CERTIFICATE.md).'),
  ('## 2. Spectral inputs and what has been reviewed','## 2. Spectral inputs'),
  ('The preserved pilot supplies complete proofs of the following facts.',
   'The [spectral foundation](SPECTRAL_PROOF.md) supplies complete proofs of the following facts.'),
  ('The pilot proves, including a separate differentiation argument,',
   'The spectral foundation proves, including a separate differentiation argument,'),
  ('The finite curvature was derived through the autocorrelation', 'The finite curvature follows from the autocorrelation'),
  ('The proof review checks why its contact spectral measure here is one atom plus an integrable density, rather than invoking that conclusion for arbitrary rank-one perturbations.',
   'The contact spectral measure has one atom plus an integrable density, as follows from the explicit dispersion and threshold structure.'),
  ('This verifies the specific spectral step used below. It is an author-side proof review, not external independent review.',
   'These dispersion-specific properties establish the spectral decomposition used below.'),
  ('For $z=3/4$, the preserved values are', 'For $z=3/4$, numerical quadrature gives'),
  ('The exponent in (3) is not a second universality mechanism. Whenever', 'Whenever'),
  ('## 4. New corollary: the whole relative wavefunction has a controlled size scaling','## 4. Scaled relative wavefunction and preparation size'),
  ('The preceding notes controlled the root-mean-square size and fixed finite supports. They did not assert a result for support growing with $1/P$. This section derives that result from the same normalized eigenfunction; it introduces no new Hamiltonian or pulse/preparation dynamics.',
   'The normalized eigenfunction determines the optimal overlap for relative support growing with $1/P$.'),
  ('This is a kinematic overlap result, not a protocol for loading the state, not a bound on preparation time, and not a normalized exact-total-momentum state on the infinite center-of-mass lattice. It applies fiberwise and to suitably narrow normalizable momentum wave packets.',
   'This is a kinematic overlap optimum. It applies fiberwise and to suitably narrow normalizable momentum wave packets; its radius quantifies state support rather than preparation dynamics.'),
  ('The new diagnostic reconstructs (4) without importing the previous scalar solver.',
   'An independent quadrature diagnostic reconstructs (4).'),
  ('Equation (1) is also explicit in the continuum amplitude, but this review does not produce a usable uniform rate for $\\eta(t)$. Thus (3) still takes long time at fixed $v$, followed by large $v$. A bound of order $10^{-2}$ on total continuum error would not certify a rare $10^{-8}$ coincidence tail. No assertion of a finite-time high-velocity experimental window, strict finite-time light cone, or advantageous information transfer follows. These are restrictions on the stated interpretation, not requirements to add another model before reviewing the present theorem.',
   'The [joint observation-time theorem](OBSERVATION_TIME.md) proves a uniform momentum-integrated bound $\\eta_U(t)\\le C/(Jt)$ near resonance and combines it with band-norm estimates to give a sufficient simultaneous time–detuning regime. The resonance tail (3) retains its long-time-at-fixed-velocity, then high-velocity order. Relative accuracy for a rare event requires the [event-local error bound](FINITE_TIME_CERTIFICATE.md), which compares continuum amplitude with the square root of its probability.'),
 ],
 'REVIEW.md': [],
 'prior/FOLLOWUP.md': [
  ('## 1. Same model; specified source and detector', '## 1. Model, source, and detector'),
  ('Set \\(U=U_c\\), with the exact value in the preserved pilot.',
   'Set \\(U=U_c\\), with the exact value in [the spectral foundation](SPECTRAL_PROOF.md).'),
  ('There is no spectral filtering, prior projection onto dimers, momentum postselection, or spatially extended preparation. At time t measure both positions.',
   'At time t measure both positions after unitary evolution from this onsite source.'),
  ('The detector can recognize which lattice sites the two distinguishable particles occupy. It is not a proposed implementation of the precise fractional hopping kernel.',
   'The detector resolves the lattice positions of both distinguishable particles.'),
  ('The pilot proves a unique relative-coordinate bound state',
   'The [spectral foundation](SPECTRAL_PROOF.md) proves a unique relative-coordinate bound state'),
  ('These spectral facts are inputs from `prior/PILOT.md`; the statements below about preparation and propagation are additional derivations.',
   'These spectral facts are the inputs to the preparation and propagation derivations below.'),
  ('the pilot gives \\(I_P(E_{th})>1/U_c\\)', 'the spectral foundation gives \\(I_P(E_{th})>1/U_c\\)'),
  ('The pilot gives the unique eigenvalue below it.', 'The spectral foundation gives the unique eigenvalue below it.'),
  ('E\'_d was established separately in the pilot.', 'E\'_d is established separately in the spectral foundation.'),
  ('**Order of limits:** t tends to infinity at fixed v first; then v/J tends to infinity. We have not bounded the relative continuum error uniformly when v grows with t. A fixed-time far-spatial-tail expansion need not have exponent eight. This is not a finite-time arrival guarantee or an optimal signal-discrimination protocol.',
   '**Order of limits:** t tends to infinity at fixed v first; then v/J tends to infinity. The exponent belongs to this limiting velocity measure. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [joint observation-time theorem](OBSERVATION_TIME.md) control the sharp event at deterministic times under their stated conditions.'),
  ('the pilot\'s expansion', 'the spectral expansion'),
  ('At finite times they can coincide; they have not been declared absent from the full wave function.',
   'At finite times they can coincide, and their scattering component remains in the full wavefunction.'),
  ('by the same local/tail splitting as in the pilot.', 'by the local/tail splitting in the spectral foundation.'),
  ('The pilot\'s resolvent Fourier coefficients give', 'The resolvent Fourier coefficients give'),
  ('The source/measurement roles are substantial, not decorative citations.',
   'The contact scattering framework, local-pair measurement, and spectral identities have the following predecessors.'),
  ('the arbitrary-momentum contact T-matrix and its resonance subtraction already supply the continuum pole equation used in the pilot. The present propagation tail is obtained from that branch and its contact residue using standard spectral/Fourier arguments. It is not a newly invented dimer field or effective scattering theory. The current primary published two-magnon section was inspected, including Eqs. (5)--(8). Its discussion evaluates the rest pole and then treats three magnons; absence of a printed local-quench tail is not a priority certificate.',
   'the arbitrary-momentum contact T-matrix and its resonance subtraction supply the continuum pole equation. The propagation law here combines the normalized lattice contact residue with the specified source and detector through spectral/Fourier arguments.'),
  ('The primary preprint\'s preparation discussion and coincidence geometry were read. This is another direct predecessor for the observable, not the fractional threshold asymptotic.',
   'This is a direct predecessor for the local-pair observable.'),
  ('The source comparison uses the readable primary text. A screenshot request for the Kranzl figure failed; no graph coordinate, fit or figure-only parameter was extracted from it. The numerical values in this note are calculations of the stipulated model, not experimental values. This is a targeted comparison, not exhaustive priority clearance or external proof review.',
   'The [author account](AUTHOR_ACCOUNT.md#relationship-to-established-work) compares the models and observables in detail.'),
 ],
 'prior/prior/PILOT.md': [
  ('There is no bath, drive, preparation by acceleration, many-body background, disorder or changing interaction.',
   'The Hamiltonian is time independent and translation invariant.'),
  ('This is **not** the exact pure-power kernel J/|r|^(1+z) at short distances. It is a convenient standard microscopic regularization with the same long-wavelength power. No current apparatus is asserted to implement every coefficient or independently tunable interaction in this model.',
   'The gamma-function kernel fixes the microscopic short-distance hopping; its long-distance power is J/|r|^(1+z) times the stated coefficient.'),
  ('This proof does not turn a finite ring\'s lowest level into an infinite-lattice bound state. It establishes a fiber eigenvalue separated from that fiber\'s continuum. It also does not say that adding center-of-mass momentum dynamically converts an arbitrary scattering preparation into the eigenstate.',
   'This establishes an infinite-lattice relative-coordinate eigenstate separated from the continuum at its conserved total momentum.'),
  ('At e=1 the same argument holds after isolating the two moving cusps and dominating them by |x-1/2|^(-z) and |x+1/2|^(-z).',
   'At the endpoint use the exact lattice energy $E=E_{\\rm th}(P)=\\epsilon_z(P)$, not $E=J|P|^z$. The latter is above the lattice edge, so Eq. (8) cannot be extended by substituting e=1. The [exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint expansion with coefficient F_z(1), using uniform cusp domination and the same tail splitting.'),
  ('It is a diverging **spectral group velocity**. No relativistic causality statement, guaranteed fast state transfer, ballistic front, or local-quench probability has been deduced from it.',
   'It is a diverging **spectral group velocity**. Its local-source coincidence weight is derived in [the transport proof](TRANSPORT_PROOF.md).'),
  ('The exact momentum is essential. Momentum-changing disorder or an external operation can provide decay channels not present in this translation-invariant problem. No such operation is added here. Bound wave functions in a long-range hopping model need not decay exponentially.',
   'Total momentum is conserved in this translation-invariant problem. Bound wavefunctions in a long-range hopping model need not decay exponentially.'),
  ('## 9. Strongest predecessor reconstruction', '## 9. Relationship to established work'),
  ('### [SFZ] already supplies the universal pole equation', '### [SFZ] Finite-momentum pole equation'),
  ('### [ALMM] already establishes motion-induced lattice binding', '### [ALMM] Motion-induced lattice binding'),
  ('### [K23] already observes momentum-selective magnon binding', '### [K23] Momentum-selective magnon binding'),
  ('The short fractional proof in Section 3 extends the specific calculation outside those smooth hypotheses; it does not discover that mechanism.',
   'Section 3 supplies the explicit calculation for the fractional cusp outside those smooth hypotheses.'),
  ('We neither reanalyze their data nor refute their specified finite-velocity result. Their spectroscopy provides relevant context, not a demonstrated realization of our model or an unrestricted theorem that all bound pairs have finite velocity.',
   'Their spectroscopy establishes finite velocity for the specified branch and provides context for the resonance contrast in this contact model.'),
  ('It removes any claim that using mobile distinguishable particles or a finite binding threshold is new. [CRSTV] supplies the fractional lattice kinetic operator and exact kernel, so that operator is inherited too.',
   '[CRSTV] supplies the fractional lattice kinetic operator and exact kernel. These model ingredients remain attributed to the respective sources.'),
  ('Thus (7) is an **exact specialization of their effective theory**, not a newly invented scattering equation. The factor 1/2 changes T normalization, not the pole. The existence of a root between 0 and 1, its interpretation as a fractional bound branch, the lattice convergence proof, and the matrix-resolvent controls are the calculations made here. The cited passages evaluate the rest bound pole and use nonzero momenta for the three-body equation; they do not spell out this positive-energy below-continuum branch. That absence does not make consequences of their equation independent conceptual inventions.',
   'Thus (7) is an **exact specialization of their effective theory**. The factor 1/2 changes T normalization, while the pole equation is unchanged. Sections 3–6 establish the root between 0 and 1, its below-fixed-momentum-continuum interpretation, lattice convergence, differentiated velocity, and normalized contact weight.'),
  ('**Contribution under assessment:** a controlled resonance-to-bound-pair dispersion contrast, with the fractional moving pole and its vanishing local spectral weight made explicit in microscopic models. The central sign/residue calculations are short consequences of an existing two-body framework. No claim of a new Efimov effect, first motion-bound dimer, experimental contradiction, or independent invention of the contact effective theory is justified.',
   'The spectral result is a controlled resonance-to-bound-pair dispersion contrast in the exact lattice model, with a fractional moving pole and vanishing local spectral weight. Its scattering framework and motion-induced binding mechanism remain attributed above. The [transport proof](TRANSPORT_PROOF.md) carries the normalized local overlaps into the observed probability law.'),
  ('Read the introduction, Hypotheses 3.1 and 5.1, and Theorem 5.4/proof.',
   'Introduction, Hypotheses 3.1 and 5.1, and Theorem 5.4/proof.'),
  ('Read the published two-magnon section and its arbitrary-momentum T-matrix, compared with preprint v1 and the accessible combined PDF. Source equations are identified by version. No figure or table values are used.',
   'Published two-magnon section and arbitrary-momentum T-matrix; preprint v1 provides the indicated alternative equation numbering.'),
  ('Read Sec. III and Appendix E--F, including the sign of the bound branch, stated velocity behavior and preparation. Figure screenshots were unavailable; no plotted points were digitized or used to infer a numerical parameter not stated in prose.',
   'Section III and Appendices E–F: bound-branch sign, velocity behavior, and preparation.'),
  ('Read the two-body construction, Eqs. (8)--(10), and its zero-momentum analysis. The many-body polaron result is not used here.',
   'Two-body construction, Eqs. (8)–(10), and zero-momentum analysis.'),
  ('Read Theorem 1.1, kernel (1.7), and power-law bounds (1.8).',
   'Theorem 1.1, kernel (1.7), and power-law bounds (1.8).'),
  ('The source comparison is targeted, not exhaustive priority clearance or external proof review. Sources are not redistributed in this package.',
   'Primary sources are linked under their own publication and distribution terms.'),
 ],
}

INLINE_REPLACEMENTS={'REVIEW.md': [],
 'THEOREM.md': [],
 'prior/FOLLOWUP.md': [{'count': 1, 'new': 'At time $`t`$ measure', 'old': 'At time t measure'},
                       {'count': 1, 'new': 'is exactly $`j`$.', 'old': 'is exactly j.'},
                       {'count': 1, 'new': 'of weight $`Z(P)`$,', 'old': 'of weight Z(P),'},
                       {'count': 1, 'new': 'For the explicit $`A_P`$,', 'old': 'For the explicit A_P,'},
                       {'count': 1, 'new': 'of $`dq/(2\\pi)`$ under $`A_P`$', 'old': 'of dq/(2pi) under A_P'},
                       {'count': 1, 'new': 'For $`0<P<\\pi`$,', 'old': 'For 0<P<pi,'},
                       {'count': 1, 'new': 'of $`\\epsilon`$ on $`(0,\\pi)`$', 'old': 'of epsilon on (0,pi)'},
                       {'count': 1,
                        'new': 'shows that $`A_P(q)`$ strictly',
                        'old': 'shows that A_P(q) strictly'},
                       {'count': 1, 'new': 'decreases on $`(0,P/2)`$', 'old': 'decreases on (0,P/2)'},
                       {'count': 1, 'new': 'increases on $`(P/2,\\pi)`$', 'old': 'increases on (P/2,pi)'},
                       {'count': 1, 'new': 'lower cusp at $`P/2`$', 'old': 'lower cusp at P/2'},
                       {'count': 1,
                        'new': 'smooth maxima at $`0`$ and $`\\pi`$;',
                        'old': 'smooth maxima at 0 and pi;'},
                       {'count': 1, 'new': 'the $`P=\\pi`$ case', 'old': 'the P=pi case'},
                       {'count': 1, 'new': '$`A_P`$ is analytic', 'old': 'A_P is analytic'},
                       {'count': 2, 'new': 'almost every $`P`$.', 'old': 'almost every P.'},
                       {'count': 1, 'new': 'rest threshold at $`P=0`$', 'old': 'rest threshold at P=0'},
                       {'count': 1, 'new': 'total mass $`1-Z(P)`$,', 'old': 'total mass 1-Z(P),'},
                       {'count': 3, 'new': 'At $`z=3/4`$', 'old': 'At z=3/4'},
                       {'count': 1, 'new': 'sites. $`W_c`$ is', 'old': 'sites. W_c is'},
                       {'count': 1, 'new': 'test function $`f`$,', 'old': 'test function f,'},
                       {'count': 1, 'new': 'measure of mass $`W_c`$.', 'old': 'measure of mass W_c.'},
                       {'count': 1, 'new': 'Dividing by $`W_c`$ gives', 'old': 'Dividing by W_c gives'},
                       {'count': 1,
                        'new': 'The translation of $`Z`$ converges in $`L^2`$ and $`Z`$ is bounded',
                        'old': 'The translation of Z converges in L2 and Z is bounded'},
                       {'count': 1,
                        'new': "used; $`E'_d`$ is established",
                        'old': "used; E'_d is established"},
                       {'count': 1, 'new': 'continuity points $`v>0`$,', 'old': 'continuity points v>0,'},
                       {'count': 1, 'new': "Because $`E'_d`$ diverges", 'old': "Because E'_d diverges"},
                       {'count': 1, 'new': 'and $`Z(P)>0`$ at', 'old': 'and Z(P)>0 at'},
                       {'count': 1, 'new': 'momentum, $`Q(v)>0`$ at', 'old': 'momentum, Q(v)>0 at'},
                       {'count': 1, 'new': 'large finite $`v`$.', 'old': 'large finite v.'},
                       {'count': 1, 'new': 'The small-$`P`$ asymptotics', 'old': 'The small-P asymptotics'},
                       {'count': 2, 'new': 'factor $`Z`$ is', 'old': 'factor Z is'},
                       {'count': 1,
                        'new': 'Replacing $`Z^2`$ by $`Z`$ would',
                        'old': 'Replacing Z squared by Z would'},
                       {'count': 1, 'new': "monotonicity of $`E'_d`$ is", 'old': "monotonicity of E'_d is"},
                       {'count': 1,
                        'new': 'integrating $`Z^2`$ proves',
                        'old': 'integrating Z squared proves'},
                       {'count': 1,
                        'new': '| $`v/J`$ | Near-zero cutoff $`P`$ | $`Q(v)`$, per initially prepared pair |',
                        'old': '| v/J | Near-zero cutoff P | Q(v), per initially prepared pair |'},
                       {'count': 1, 'new': "crossing of $`E'_d=v`$,", 'old': "crossing of E'_d=v,"},
                       {'count': 1,
                        'new': '**Order of limits:** $`t`$ tends to infinity at fixed $`v`$ first; then '
                               '$`v/J`$ tends to infinity.',
                        'old': '**Order of limits:** t tends to infinity at fixed v first; then v/J tends to '
                               'infinity.'},
                       {'count': 1, 'new': 'for every $`L(t)/t`$ tending', 'old': 'for every L(t)/t tending'},
                       {'count': 1, 'new': 'For every fixed $`U>U_c`$,', 'old': 'For every fixed U>Uc,'},
                       {'count': 1, 'new': 'for all $`P`$.', 'old': 'for all P.'},
                       {'count': 1, 'new': 'At $`P=0`$ it has $`E_0<0`$', 'old': 'At P=0 it has E0<0'},
                       {'count': 1, 'new': 'At $`U=U_c`$,', 'old': 'At U=Uc,'},
                       {'count': 1, 'new': 'For $`U=0`$ there', 'old': 'For U=0 there'},
                       {'count': 1, 'new': 'to its $`q`$ derivative', 'old': 'to its q derivative'},
                       {'count': 1, 'new': 'Scaling $`q=Px`$ yields', 'old': 'Scaling q=Px yields'},
                       {'count': 1, 'new': 'integrable for $`z>1/2`$;', 'old': 'integrable for z>1/2;'},
                       {'count': 1,
                        'new': 'total momentum $`[p,2p]`$ has',
                        'old': 'total momentum [p,2p] has'},
                       {'count': 1, 'new': 'This statement fixes $`R`$;', 'old': 'This statement fixes R;'},
                       {'count': 1, 'new': 'its large-$`v`$ tail', 'old': 'its large-v tail'},
                       {'count': 1, 'new': 'multiplied by $`S_R`$.', 'old': 'multiplied by S_R.'},
                       {'count': 1, 'new': 'same-site detector $`R=0`$.', 'old': 'same-site detector R=0.'}],
 'prior/prior/PILOT.md': [{'count': 1,
                           'new': 'Use two distinguishable particles, one of each species, on the infinite '
                                  'lattice $`\\mathbb{Z}`$. Lattice spacing and $`\\hbar`$ are one. Both '
                                  'have the dispersion',
                           'old': 'Use two distinguishable particles, one of each species, on the infinite '
                                  'lattice Z. Lattice spacing and hbar are one. Both have the dispersion'},
                          {'count': 1,
                           'new': 'They interact only on the same site, with attractive potential '
                                  '$`-U\\delta_{x_a,x_b},\\ U>0`$. The complete Hamiltonian is bounded and '
                                  'self-adjoint in the two-particle sector. The Hamiltonian is time '
                                  'independent and translation invariant.',
                           'old': 'They interact only on the same site, with attractive potential -U '
                                  'delta_(x_a,x_b), U>0. The complete Hamiltonian is bounded and '
                                  'self-adjoint in the two-particle sector. The Hamiltonian is time '
                                  'independent and translation invariant.'},
                          {'count': 1,
                           'new': 'The single-particle operator is the established fractional power '
                                  '$`J(-\\Delta)^{z/2}`$ of the discrete Laplacian [CRSTV]. Its hopping at '
                                  'nonzero integer separation $`r`$ is positive in the convention '
                                  '$`H=\\mathrm{diagonal}-\\sum_r t_r\\mathrm{translation}_r`$:',
                           'old': 'The single-particle operator is the established fractional power '
                                  'J(-Delta)^(z/2) of the discrete Laplacian [CRSTV]. Its hopping at nonzero '
                                  'integer separation r is positive in the convention H=diagonal - sum_r t_r '
                                  'translation_r:'},
                          {'count': 1,
                           'new': 'The gamma-function kernel fixes the microscopic short-distance hopping; '
                                  'its long-distance power is $`J/\\lvert r\\rvert^{1+z}`$ times the stated '
                                  'coefficient.',
                           'old': 'The gamma-function kernel fixes the microscopic short-distance hopping; '
                                  'its long-distance power is J/|r|^(1+z) times the stated coefficient.'},
                          {'count': 1,
                           'new': 'Total crystal momentum $`P`$ is conserved. In a $`P`$ fiber the '
                                  'relative-momentum Hamiltonian acts in $`L^2([-\\pi,\\pi],dq/(2\\pi))`$ as',
                           'old': 'Total crystal momentum P is conserved. In a P fiber the relative-momentum '
                                  'Hamiltonian acts in L^2([-pi,pi],dq/(2pi)) as'},
                          {'count': 1,
                           'new': 'where $`\\lvert1\\rangle`$ is the constant normalized function. A '
                                  'below-continuum eigenvalue satisfies the exact rank-one equation',
                           'old': 'where |1> is the constant normalized function. A below-continuum '
                                  'eigenvalue satisfies the exact rank-one equation'},
                          {'count': 1,
                           'new': 'Its relative wave function is proportional to $`(A_P-E)^{-1}`$. For fixed '
                                  '$`P`$ and $`E`$ below the band it is normalizable. A momentum eigenstate '
                                  'is not a normalizable center-of-mass state on the entire infinite '
                                  'lattice; one may form wave packets from the fibers. Binding here means '
                                  'relative-coordinate localization below the scattering continuum **at the '
                                  'conserved $`P`$**, not a negative energy relative to the global '
                                  'two-particle minimum.',
                           'old': 'Its relative wave function is proportional to (A_P-E)^(-1). For fixed P '
                                  'and E below the band it is normalizable. A momentum eigenstate is not a '
                                  'normalizable center-of-mass state on the entire infinite lattice; one may '
                                  'form wave packets from the fibers. Binding here means relative-coordinate '
                                  'localization below the scattering continuum **at the conserved P**, not a '
                                  'negative energy relative to the global two-particle minimum.'},
                          {'count': 1,
                           'new': 'The chord identity and $`0<z<1`$ give',
                           'old': 'The chord identity and 0<z<1 give'},
                          {'count': 1,
                           'new': 'Therefore $`\\epsilon_z`$ is subadditive on the momentum circle and',
                           'old': 'Therefore epsilon_z is subadditive on the momentum circle and'},
                          {'count': 1,
                           'new': 'The two threshold configurations put the individual momenta at $`0`$ and '
                                  '$`P`$. Equal sharing $`P/2,P/2`$ has higher energy. The subadditivity is '
                                  'strict away from configurations involving a zero momentum.',
                           'old': 'The two threshold configurations put the individual momenta at 0 and P. '
                                  'Equal sharing P/2,P/2 has higher energy. The subadditivity is strict away '
                                  'from configurations involving a zero momentum.'},
                          {'count': 1,
                           'new': 'At $`P=0`$ the threshold integral is finite because $`z<1`$. Its beta '
                                  'integral gives',
                           'old': 'At P=0 the threshold integral is finite because z<1. Its beta integral '
                                  'gives'},
                          {'count': 1,
                           'new': 'For $`U<U_c`$ there is no rest bound state. For $`U>U_c`$ there is '
                                  'exactly one negative rest eigenvalue. At $`U=U_c`$ the formal zero-energy '
                                  'solution is proportional to $`1/(2\\epsilon_z(q))`$, hence behaves as '
                                  '$`\\lvert q\\rvert^{-z}`$. It is integrable but not square integrable for '
                                  '$`z>1/2`$. Thus the threshold is a resonance, not a normalizable '
                                  'zero-energy dimer.',
                           'old': 'For U<Uc there is no rest bound state. For U>Uc there is exactly one '
                                  'negative rest eigenvalue. At U=Uc the formal zero-energy solution is '
                                  'proportional to 1/(2epsilon_z(q)), hence behaves as |q|^(-z). It is '
                                  'integrable but not square integrable for z>1/2. Thus the threshold is a '
                                  'resonance, not a normalizable zero-energy dimer.'},
                          {'count': 1,
                           'new': 'The parameter window is not arbitrary: $`z<1`$ permits a nonzero rest '
                                  'binding threshold, while $`z>1/2`$ makes the threshold solution '
                                  'nonnormalizable and the renormalized finite-energy difference ultraviolet '
                                  'convergent. These roles also occur in the two-body resonance analysis of '
                                  '[SFZ].',
                           'old': 'The parameter window is not arbitrary: z<1 permits a nonzero rest binding '
                                  'threshold, while z>1/2 makes the threshold solution nonnormalizable and '
                                  'the renormalized finite-energy difference ultraviolet convergent. These '
                                  'roles also occur in the two-body resonance analysis of [SFZ].'},
                          {'count': 1,
                           'new': '## 3. Exact bound state for every nonzero momentum at $`U=U_c`$',
                           'old': '## 3. Exact bound state for every nonzero momentum at U=Uc'},
                          {'count': 1, 'new': 'For $`a,b>0`$,', 'old': 'For a,b>0,'},
                          {'count': 1,
                           'new': 'Apply this pointwise to the two shifted dispersions and use translation '
                                  'invariance of the integral. For $`P\\not\\equiv0\\pmod{2\\pi}`$ the '
                                  'inequality is strict on a set of positive measure, so',
                           'old': 'Apply this pointwise to the two shifted dispersions and use translation '
                                  'invariance of the integral. For P not zero modulo 2pi the inequality is '
                                  'strict on a set of positive measure, so'},
                          {'count': 1,
                           'new': 'For the other endpoint, use uncentered momentum $`p=q+P/2`$. '
                                  'Subadditivity gives',
                           'old': 'For the other endpoint, use uncentered momentum p=q+P/2. Subadditivity '
                                  'gives'},
                          {'count': 1,
                           'new': 'almost everywhere, with strict inequality on a set of positive measure. '
                                  'The zeros of the denominator are integrable cusps of order $`\\lvert '
                                  'p\\rvert^z`$ or $`\\lvert p-P\\rvert^z`$. Thus',
                           'old': 'almost everywhere, with strict inequality on a set of positive measure. '
                                  'The zeros of the denominator are integrable cusps of order |p|^z or '
                                  '|p-P|^z. Thus'},
                          {'count': 1,
                           'new': 'Since $`I_P(E)`$ is continuous and strictly increasing below the edge, '
                                  '(4)–(5) bracket exactly one eigenvalue at $`U=U_c`$:',
                           'old': 'Since I_P(E) is continuous and strictly increasing below the edge, '
                                  '(4)–(5) bracket exactly one eigenvalue at U=Uc:'},
                          {'count': 1, 'new': 'Define, for $`e\\le1`$,', 'old': 'Define, for e<=1,'},
                          {'count': 1,
                           'new': 'At $`e=1`$ the threshold singularities remain integrable. At infinity the '
                                  'difference is $`O(\\lvert x\\rvert^{-2z})`$ plus $`O(\\lvert '
                                  'x\\rvert^{-z-2})`$; $`z>1/2`$ ensures convergence. The subtraction at '
                                  '$`x=0`$ is integrable because $`z<1`$.',
                           'old': 'At e=1 the threshold singularities remain integrable. At infinity the '
                                  'difference is O(|x|^(-2z)) plus O(|x|^(-z-2)); z>1/2 ensures convergence. '
                                  'The subtraction at x=0 is integrable because z<1.'},
                          {'count': 1,
                           'new': 'A useful sign proof does not require numerical root finding. At $`e=0`$, '
                                  'replace the subtraction in the integral by one quarter of the sum of its '
                                  'two shifted versions. The integral of the change tends to zero under '
                                  'symmetric large cutoffs. The integrand becomes',
                           'old': 'A useful sign proof does not require numerical root finding. At e=0, '
                                  'replace the subtraction in the integral by one quarter of the sum of its '
                                  'two shifted versions. The integral of the change tends to zero under '
                                  'symmetric large cutoffs. The integrand becomes'},
                          {'count': 1,
                           'new': 'with $`a=\\lvert x+1/2\\rvert^z`$ and $`b=\\lvert x-1/2\\rvert^z`$. Hence '
                                  '$`F_z(0)<0`$. At $`e=1`$, shift to $`p=x+1/2`$ and use '
                                  '$`\\lvert1-p\\rvert^z\\le1+\\lvert p\\rvert^z`$. The resulting integrand '
                                  'relative to $`1/(2\\lvert p\\rvert^z)`$ is strictly positive almost '
                                  'everywhere. Hence $`F_z(1)>0`$. Also',
                           'old': 'with a=|x+1/2|^z and b=|x-1/2|^z. Hence F_z(0)<0. At e=1, shift to '
                                  'p=x+1/2 and use |1-p|^z<=1+|p|^z. The resulting integrand relative to '
                                  '1/(2|p|^z) is strictly positive almost everywhere. Hence F_z(1)>0. Also'},
                          {'count': 1,
                           'new': 'There is a unique $`c_z\\in(0,1)`$ with $`F_z(c_z)=0`$.',
                           'old': 'There is a unique c_z in (0,1) with F_z(c_z)=0.'},
                          {'count': 1,
                           'new': 'For $`e`$ in a compact subset below $`1`$,',
                           'old': 'For e in a compact subset below 1,'},
                          {'count': 1,
                           'new': 'Here is an explicit convergence argument. On $`\\lvert q\\rvert\\le '
                                  'M\\lvert P\\rvert`$ scale $`q=\\lvert P\\rvert x`$ and use '
                                  '$`\\epsilon_z(q)=J\\lvert q\\rvert^z[1+O(q^2)]`$. For fixed $`M`$ the '
                                  'subtraction is dominated near $`x=0`$ by $`\\lvert x\\rvert^{-z}`$; the '
                                  'positive gap $`1-e`$ controls the other denominator. In the intermediate '
                                  'tail $`M\\lvert P\\rvert\\le\\lvert q\\rvert\\le q_0`$, with $`M\\ge2`$, '
                                  'symmetric Taylor expansion of the shifted dispersion bounds the '
                                  'difference by',
                           'old': 'Here is an explicit convergence argument. On |q|<=M|P| scale q=|P|x and '
                                  'use epsilon_z(q)=J|q|^z[1+O(q^2)]. For fixed M the subtraction is '
                                  'dominated near x=0 by |x|^(-z); the positive gap 1-e controls the other '
                                  'denominator. In the intermediate tail M|P|<=|q|<=q0, with M>=2, symmetric '
                                  'Taylor expansion of the shifted dispersion bounds the difference by'},
                          {'count': 1,
                           'new': 'After division by $`\\lvert P\\rvert^{1-z}/J`$, its integral is bounded '
                                  'by $`C[M^{1-2z}+M^{-1-z}]`$. The part $`\\lvert q\\rvert\\ge q_0`$ is '
                                  '$`O(\\lvert P\\rvert^z+P^2)`$ before division and vanishes because '
                                  '$`2z>1`$. First take $`P`$ to zero at fixed $`M`$, then $`M`$ to '
                                  'infinity. Constants may depend on $`z`$ and the compact $`e`$ interval. '
                                  'At the endpoint use the exact lattice energy $`E=E_{\\rm '
                                  'th}(P)=\\epsilon_z(P)`$, not $`E=J|P|^z`$. The latter is above the '
                                  'lattice edge, so Eq. (8) cannot be extended by substituting $`e=1`$. The '
                                  '[exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint '
                                  'expansion with coefficient $`F_z(1)`$, using uniform cusp domination and '
                                  'the same tail splitting.',
                           'old': 'After division by |P|^(1-z)/J, its integral is bounded by '
                                  'C[M^(1-2z)+M^(-1-z)]. The part |q|>=q0 is O(|P|^z+P^2) before division '
                                  'and vanishes because 2z>1. First take P to zero at fixed M, then M to '
                                  'infinity. Constants may depend on z and the compact e interval. At the '
                                  'endpoint use the exact lattice energy $`E=E_{\\rm '
                                  'th}(P)=\\epsilon_z(P)`$, not $`E=J|P|^z`$. The latter is above the '
                                  'lattice edge, so Eq. (8) cannot be extended by substituting e=1. The '
                                  '[exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint '
                                  'expansion with coefficient F_z(1), using uniform cusp domination and the '
                                  'same tail splitting.'},
                          {'count': 1,
                           'new': 'Monotonicity and two fixed energies bracketing $`c_z`$ transfer (8) to '
                                  'the exact eigenvalue:',
                           'old': 'Monotonicity and two fixed energies bracketing c_z transfer (8) to the '
                                  'exact eigenvalue:'},
                          {'count': 1,
                           'new': '| $`z`$ | $`c_z`$ | limiting relative binding $`1-c_z`$ |',
                           'old': '| z | c_z | limiting relative binding 1-c_z |'},
                          {'count': 1,
                           'new': 'The exact lattice calculation at $`z=0.75`$ gives '
                                  '$`E_d(P)/(JP^z)=0.6454158452,\\ 0.6378187108,\\ 0.6352643638`$ at '
                                  '$`P=0.1,0.01,0.001`$, approaching $`c_z`$. These are below-band pole '
                                  'calculations, not fitted dispersion exponents.',
                           'old': 'The exact lattice calculation at z=0.75 gives E_d(P)/(J P^z) = '
                                  '0.6454158452, 0.6378187108, 0.6352643638 at P=0.1,0.01,0.001, approaching '
                                  'c_z. These are below-band pole calculations, not fitted dispersion '
                                  'exponents.'},
                          {'count': 1,
                           'new': "The numerator's cusps have integrable powers $`\\lvert q\\pm "
                                  'P/2\\rvert^{z-1}`$. Scale $`q=Px`$ for $`P>0`$. Put $`B_z(x)=\\lvert '
                                  "x+1/2\\rvert^z+\\lvert x-1/2\\rvert^z`$ and $`b_z(x)=zB_z(x)-xB'_z(x)`$. "
                                  'The numerator is $`J^{-1}P^{-z}[N_z(c_z)+o(1)]`$, where $`N_z(e)=\\int '
                                  'b_z/(B_z-e)^2`$. Its scaled tail is $`O(M^{-1-z})`$; the denominator is '
                                  "$`J^{-2}P^{1-2z}[F'_z(c_z)+o(1)]`$. Both statements follow from the same "
                                  'splitting as above and dominated convergence at the moving cusps.',
                           'old': "The numerator's cusps have integrable powers |q+-P/2|^(z-1). Scale q=Px "
                                  "for P>0. Put B_z(x)=|x+1/2|^z+|x-1/2|^z and b_z(x)=zB_z(x)-xB'_z(x). The "
                                  'numerator is J^(-1)P^(-z)[N_z(c_z)+o(1)], where N_z(e)=integral '
                                  'b_z/(B_z-e)^2. Its scaled tail is O(M^(-1-z)); the denominator is '
                                  "J^(-2)P^(1-2z)[F'_z(c_z)+o(1)]. Both statements follow from the same "
                                  'splitting as above and dominated convergence at the moving cusps.'},
                          {'count': 1,
                           'new': 'The boundary term vanishes because it is $`O(\\lvert x\\rvert^{1-2z})`$ '
                                  'plus $`O(\\lvert x\\rvert^{-1-z})`$. At the root this is '
                                  "$`zc_zF'_z(c_z)`$. Hence",
                           'old': 'The boundary term vanishes because it is O(|x|^(1-2z)) plus '
                                  "O(|x|^(-1-z)). At the root this is zc_zF'_z(c_z). Hence"},
                          {'count': 1,
                           'new': 'Fix $`U>U_c`$, so that $`E_0=E_d(0)<0`$. Then',
                           'old': 'Fix U>Uc, so that E0=E_d(0)<0. Then'},
                          {'count': 1,
                           'new': "The coefficient is finite because $`[\\epsilon'_z(q)]^2`$ is integrable "
                                  'for $`z>1/2`$. The effective mass is $`1/[2C(U)]`$. This holds for the '
                                  'same fractional single-particle kinetics, not by replacing it with a '
                                  'quadratic approximation.',
                           'old': "The coefficient is finite because epsilon'_z(q)^2 is integrable for "
                                  'z>1/2. The effective mass is 1/[2C(U)]. This holds for the same '
                                  'fractional single-particle kinetics, not by replacing it with a quadratic '
                                  'approximation.'},
                          {'count': 1,
                           'new': 'A clean proof controls the cusp instead of formally inserting a '
                                  'nonintegrable second derivative. For $`E<0`$ use',
                           'old': 'A clean proof controls the cusp instead of formally inserting a '
                                  'nonintegrable second derivative. For E<0 use'},
                          {'count': 1,
                           'new': 'Each $`h_s`$ is in the periodic Sobolev space $`H^1`$. Its '
                                  'autocorrelation equals $`\\lVert h_s\\rVert^2-P^2\\lVert '
                                  "h'_s\\rVert^2/2+o(P^2)`$, and the difference is bounded by $`P^2\\lVert "
                                  "h'_s\\rVert^2/2`$. Integrating in $`s`$ is justified by $`E<0`$ and gives",
                           'old': 'Each h_s is in the periodic Sobolev space H^1. Its autocorrelation equals '
                                  "||h_s||^2-P^2||h'_s||^2/2+o(P^2), and the difference is bounded by "
                                  "P^2||h'_s||^2/2. Integrating in s is justified by E<0 and gives"},
                          {'count': 1,
                           'new': "$`I_P(E)=I_0(E)-P^2\\int\\frac{[\\epsilon'_z]^2}{(2\\epsilon_z-E)^3}+o(P^2)`$.",
                           'old': "I_P(E)=I_0(E)-P^2 integral epsilon'^2/(2epsilon-E)^3+o(P^2)."},
                          {'count': 1,
                           'new': 'The implicit function relation proves (12). The differentiated '
                                  "autocorrelation argument also gives $`E'_d(P)=2C(U)P+o(P)`$.",
                           'old': 'The implicit function relation proves (12). The differentiated '
                                  "autocorrelation argument also gives E'_d(P)=2C(U)P+o(P)."},
                          {'count': 1,
                           'new': 'The resonance is therefore singular: the finite-mass description at fixed '
                                  '$`U>U_c`$ does not extend to $`U=U_c`$. The constants in (12) are not '
                                  'uniform as $`E_0`$ approaches zero.',
                           'old': 'The resonance is therefore singular: the finite-mass description at fixed '
                                  'U>Uc does not extend to U=Uc. The constants in (12) are not uniform as E0 '
                                  'approaches zero.'},
                          {'count': 1,
                           'new': 'At $`z=0.75`$ the coefficient is $`0.6816851254\\ldots`$, so $`Z(P)`$ is '
                                  'asymptotic to that constant times $`\\sqrt{\\lvert P\\rvert}`$. This is '
                                  'the spectral weight of the discrete line seen by onsite pair creation; it '
                                  'is not the fraction of every possible prepared pair that binds.',
                           'old': 'At z=0.75 the coefficient is 0.6816851254..., so Z(P) is asymptotic to '
                                  'that constant times sqrt(|P|). This is the spectral weight of the '
                                  'discrete line seen by onsite pair creation; it is not the fraction of '
                                  'every possible prepared pair that binds.'},
                          {'count': 1,
                           'new': 'In a finite-volume regularization the normalized operator creating the '
                                  'probe is $`L^{-1/2}\\sum_x e^{iPx}a_x^\\dagger b_x^\\dagger`$. Its vacuum '
                                  'spectral measure has a line of weight $`Z(P)`$ at $`E_d(P)`$, plus a '
                                  'continuum. The infinite-volume limit defines the fiber quantity. Both the '
                                  'gap and its contact weight decrease toward $`P=0`$. Consequently, '
                                  'increasingly small momenta demand spectral resolution and have decreasing '
                                  'overlap with this local pair source.',
                           'old': 'In a finite-volume regularization the normalized operator creating the '
                                  'probe is L^(-1/2) sum_x exp(iPx) a_x^dagger b_x^dagger. Its vacuum '
                                  'spectral measure has a line of weight Z(P) at E_d(P), plus a continuum. '
                                  'The infinite-volume limit defines the fiber quantity. Both the gap and '
                                  'its contact weight decrease toward P=0. Consequently, increasingly small '
                                  'momenta demand spectral resolution and have decreasing overlap with this '
                                  'local pair source.'},
                          {'count': 1,
                           'new': 'The contact example is not the only interaction supporting the '
                                  'low-momentum pole. As a specified control, keep the same fractional '
                                  'kinetic energy, forbid double occupancy, and put an attraction $`-V`$ at '
                                  'relative separations $`\\pm1`$. Consider identical bosons, so the even '
                                  'relative-coordinate sector is the physical one. This is the two-magnon '
                                  'structure of a long-range XY chain with a nearest-neighbor longitudinal '
                                  "attraction, though our short-distance hopping kernel differs from [SFZ]'s "
                                  'pure power.',
                           'old': 'The contact example is not the only interaction supporting the '
                                  'low-momentum pole. As a specified control, keep the same fractional '
                                  'kinetic energy, forbid double occupancy, and put an attraction -V at '
                                  'relative separations +-1. Consider identical bosons, so the even '
                                  'relative-coordinate sector is the physical one. This is the two-magnon '
                                  'structure of a long-range XY chain with a nearest-neighbor longitudinal '
                                  "attraction, though our short-distance hopping kernel differs from [SFZ]'s "
                                  'pure power.'},
                          {'count': 1,
                           'new': 'Define $`g_r(E,P)=\\int\\cos(rq)/(A_P-E)`$. Eliminating the forbidden '
                                  'site by a Schur complement gives the even nearest-neighbor resolvent',
                           'old': 'Define g_r(E,P)=integral cos(rq)/(A_P-E). Eliminating the forbidden site '
                                  'by a Schur complement gives the even nearest-neighbor resolvent'},
                          {'count': 1,
                           'new': 'The threshold vector has numerator proportional to $`\\cos(q)-a`$; since '
                                  '$`1-a>0`$, it is again a nonnormalizable resonance, not a threshold '
                                  'eigenstate. Each fixed-$`r`$ $`g_r`$ has the same leading change as '
                                  '$`g_0`$ in (8), because $`\\cos(rq)=1+O(q^2)`$ in the singular region. '
                                  'Taylor expansion of (14) gives',
                           'old': 'The threshold vector has numerator proportional to cos(q)-a; since 1-a>0, '
                                  'it is again a nonnormalizable resonance, not a threshold eigenstate. Each '
                                  'fixed-r g_r has the same leading change as g_0 in (8), because '
                                  'cos(rq)=1+O(q^2) in the singular region. Taylor expansion of (14) gives'},
                          {'count': 1,
                           'new': 'The prefactor is strictly positive. Thus at $`V=V_c`$ there is a '
                                  'below-band even eigenvalue for all sufficiently small nonzero $`P`$ with '
                                  '**the same $`c_z`$**. The assertion is local in momentum; no all-$`P`$ '
                                  'hard-core theorem is claimed. Monotonicity follows directly from the '
                                  'resolvent of the projected kinetic operator below its spectrum. No other '
                                  'even below-band state can occur because the remaining attractive '
                                  'interaction has rank one there.',
                           'old': 'The prefactor is strictly positive. Thus at V=Vc there is a below-band '
                                  'even eigenvalue for all sufficiently small nonzero P with **the same '
                                  'c_z**. The assertion is local in momentum; no all-P hard-core theorem is '
                                  'claimed. Monotonicity follows directly from the resolvent of the '
                                  'projected kinetic operator below its spectrum. No other even below-band '
                                  'state can occur because the remaining attractive interaction has rank one '
                                  'there.'},
                          {'count': 1,
                           'new': 'For $`z=.75`$, $`V_c/J=1.4411355579\\ldots`$. The ratios $`E_{\\rm '
                                  'hc}/(JP^z)`$ are $`0.5949493530,0.6195852551,0.6293576619`$ at '
                                  '$`P=.1,.01,.001`$, approaching $`c_z`$ from the other side of the contact '
                                  'result. This is a microscopic control, not proof of universality for '
                                  'arbitrary interactions or every spin apparatus.',
                           'old': 'For z=.75, Vc/J=1.4411355579.... The ratios E_hc/(J P^z) are '
                                  '0.5949493530,0.6195852551,0.6293576619 at P=.1,.01,.001, approaching c_z '
                                  'from the other side of the contact result. This is a microscopic control, '
                                  'not proof of universality for arbitrary interactions or every spin '
                                  'apparatus.'},
                          {'count': 1,
                           'new': 'For the contact model define $`U_c(P)=1/I_P(E_{\\rm th}(P))`$. Equations '
                                  '(5) and (8) imply',
                           'old': 'For the contact model define Uc(P)=1/I_P(E_th(P)). Equations (5) and (8) '
                                  'imply'},
                          {'count': 1,
                           'new': 'In a joint weak-detuning limit, set $`h=J(U^{-1}-U_c^{-1})/\\lvert '
                                  'P\\rvert^{1-z}\\ge0`$. Away from its threshold endpoint the universal '
                                  'bound equation is $`F_z(e)=h`$. It has a solution below continuum exactly '
                                  'for $`0\\le h<F_z(1)`$; for $`h>F_z(1)`$ no such pole occurs in that '
                                  'scaling window. At equality the pole meets the continuum. This does not '
                                  'prove global monotonicity in $`P`$ or a unique critical momentum '
                                  'throughout the Brillouin zone.',
                           'old': 'In a joint weak-detuning limit, set h=J(U^(-1)-Uc^(-1))/|P|^(1-z)>=0. '
                                  'Away from its threshold endpoint the universal bound equation is '
                                  'F_z(e)=h. It has a solution below continuum exactly for 0<=h<F_z(1); for '
                                  'h>F_z(1) no such pole occurs in that scaling window. At equality the pole '
                                  'meets the continuum. This does not prove global monotonicity in P or a '
                                  'unique critical momentum throughout the Brillouin zone.'},
                          {'count': 1,
                           'new': 'A finite control with $`z=.75`$ and $`U=.7U_c`$ has no below-band contact '
                                  'state at $`P=.0001`$, but has one at $`P=.1`$. The momentum-dependent '
                                  'availability of binding itself is not a new general observation [ALMM, '
                                  'K23].',
                           'old': 'A finite control with z=.75 and U=.7Uc has no below-band contact state at '
                                  'P=.0001, but has one at P=.1. The momentum-dependent availability of '
                                  'binding itself is not a new general observation [ALMM, K23].'},
                          {'count': 1,
                           'new': 'The 2026 published text of Sun, Feng and Zhang [SFZ], Eqs. (6),(8), gives '
                                  'the arbitrary-total-momentum contact T-matrix and its resonance '
                                  'subtraction. The v1 preprint numbers the same formulas (5),(7). Their '
                                  'scattering parameter denoted $`P`$ is **not our total momentum $`P`$**.',
                           'old': 'The 2026 published text of Sun, Feng and Zhang [SFZ], Eqs. (6),(8), gives '
                                  'the arbitrary-total-momentum contact T-matrix and its resonance '
                                  'subtraction. The v1 preprint numbers the same formulas (5),(7). Their '
                                  'scattering parameter denoted P is **not our total momentum P**.'},
                          {'count': 1,
                           'new': 'At their resonance, set their total momentum $`k=P`$, energy $`E=u\\lvert '
                                  'P\\rvert^z e`$, and their kinetic coefficient $`u=J`$. Subtract their '
                                  'zero-energy, zero-momentum integral and send the dimensionless cutoff to '
                                  'infinity. Their result becomes',
                           'old': 'At their resonance, set their total momentum k=P, energy E=u|P|^z e, and '
                                  'their kinetic coefficient u=J. Subtract their zero-energy, zero-momentum '
                                  'integral and send the dimensionless cutoff to infinity. Their result '
                                  'becomes'},
                          {'count': 1,
                           'new': 'Thus (7) is an **exact specialization of their effective theory**. The '
                                  'factor $`1/2`$ changes $`T`$ normalization, while the pole equation is '
                                  'unchanged. Sections 3–6 establish the root between $`0`$ and $`1`$, its '
                                  'below-fixed-momentum-continuum interpretation, lattice convergence, '
                                  'differentiated velocity, and normalized contact weight.',
                           'old': 'Thus (7) is an **exact specialization of their effective theory**. The '
                                  'factor 1/2 changes T normalization, while the pole equation is unchanged. '
                                  'Sections 3–6 establish the root between 0 and 1, its '
                                  'below-fixed-momentum-continuum interpretation, lattice convergence, '
                                  'differentiated velocity, and normalized contact weight.'},
                          {'count': 1,
                           'new': '[CRSTV] O. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea and J. L. '
                                  'Varona, *Nonlocal discrete diffusion equations and the fractional '
                                  'discrete Laplacian, regularity and applications*, arXiv:1608.08913v2. '
                                  'Theorem 1.1, kernel (1.7), and power-law bounds (1.8). Our $`z`$ equals '
                                  'twice their fractional power $`s`$, with mesh $`h=1`$. '
                                  'https://arxiv.org/pdf/1608.08913',
                           'old': '[CRSTV] O. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea and J. L. '
                                  'Varona, *Nonlocal discrete diffusion equations and the fractional '
                                  'discrete Laplacian, regularity and applications*, arXiv:1608.08913v2. '
                                  'Theorem 1.1, kernel (1.7), and power-law bounds (1.8). Our z equals twice '
                                  'their fractional power s, with mesh h=1. '
                                  'https://arxiv.org/pdf/1608.08913'}]}

def sha(data):return hashlib.sha256(data).hexdigest()
def equations(text):
 # Delimiter conversion only; no equation contents are normalized.
 return re.findall(r'\\\[(.*?)\\\]|\$\$(.*?)\$\$',text,re.S)
def format_math(text):
 """Keep TeX protected from Markdown and labels outside native MathML tables."""
 text=re.sub(r'\\operatorname\s*\{([^{}]+)\}',r'\\mathrm{\1}',text)
 text=re.sub(r'\\operatorname\s+([A-Za-z]+)',r'\\mathrm{\1}',text)
 text=re.sub(r'\\mathbb\s+([A-Za-z])',r'\\mathbb{\1}',text)
 text=re.sub(r'\\mathbf([0-9])',r'\\mathbf{\1}',text)
 def display(match):
  body=match.group(1) if match.group(1) is not None else match.group(2)
  labels=re.findall(r'\\tag\{([^{}]+)\}',body)
  body=re.sub(r'\s*\\tag\{[^{}]+\}', '',body).strip()
  body=re.sub(r'[ \t]*([<>])[ \t]*',r' \1 ',body)
  result='```math\n'+body+'\n```'
  if labels:result+='\n\n**('+', '.join(labels)+')**'
  return result
 return re.sub(r'\$\$\n(.*?)\n\$\$|```math\n(.*?)\n```',display,text,flags=re.S)
def format_inline(text):
 """Use GitHub's protected inline syntax outside code and display blocks."""
 parts=re.split(r'(```[^\n]*\n.*?\n```|\$`[^\n]*?`\$|`[^`\n]*`)',text,flags=re.S)
 for i in range(0,len(parts),2):
  parts[i]=re.sub(r'(?<![\\$])\$(?![$`])([^\n$]+?)(?<!\\)\$(?![$`])',
   lambda m:'$`'+m.group(1)+'`$',parts[i])
 return ''.join(parts)
def expected():
 output={};ledger={'archive':str(ARCHIVE.relative_to(ROOT)),'pages':[]}
 for source,dest,title,start,stop in PAGES:
  raw=(ARCHIVE/source).read_text();selected=raw[raw.index(start):]
  if stop is not None:selected=selected[:selected.index(stop)]
  if source=='prior/prior/PILOT.md':selected+='\n'+raw[raw.index('## Primary sources'):]
  if source=='prior/FOLLOWUP.md':selected=selected[:selected.index('\n**What changed:**')]
  if source=='REVIEW.md':
   selected=selected[:selected.index('\nSuggested working repository name:')]
   begin=selected.index('**GO for a bounded project record')
   end=selected.index('\n\n',begin)
   selected=selected[:begin]+selected[end+2:]
  replacements = [(selected, CONTRIBUTION_TEXT)] if source=='REVIEW.md' else REPLACEMENTS[source]
  transformed=selected
  for old,new in replacements:
   if transformed.count(old)!=1:raise ValueError('Nonunique literal transform: '+old)
   transformed=transformed.replace(old,new,1)
  if equations(selected)!=equations(transformed):raise ValueError('Equation changed')
  transformed=transformed.replace('\\[','$$').replace('\\]','$$').replace('\\(','$').replace('\\)','$')
  transformed=format_math(transformed)
  transformed=format_inline(transformed)
  display_before_inline=re.findall(r'^```math\n(.*?)\n```',transformed,re.M|re.S)
  inline_replacements=INLINE_REPLACEMENTS.get(source,[])
  for change in inline_replacements:
   if transformed.count(change['old'])!=change['count']:
    raise ValueError('Inline transform count mismatch: '+change['old'])
   transformed=transformed.replace(change['old'],change['new'])
  if re.findall(r'^```math\n(.*?)\n```',transformed,re.M|re.S)!=display_before_inline:
   raise ValueError('Inline formatting changed display math')
  footer='\n\n---\n\n[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)\n'
  data=('# '+title+'\n\n'+transformed.strip()+footer).encode()
  output[dest]=data
  ledger['pages'].append({'source':source,'destination':dest,'source_sha256':sha(raw.encode()),'start':start,'stop':stop,
   'append_sources':source=='prior/prior/PILOT.md','remove_repository_allocation':source=='REVIEW.md',
   'omit_historical_allocation_tail':source=='prior/FOLLOWUP.md',
   'omit_editorial_planning_sentence':source=='REVIEW.md',
   'presentation_cleanup':'Reader-facing scientific account; source attribution and equation content preserved.',
   'scientific_correction':('research/THRESHOLD_ENDPOINT.md' if source=='prior/prior/PILOT.md' else 'research/OBSERVATION_TIME.md' if source in ('THEOREM.md','prior/FOLLOWUP.md') else None),
   'literal_replacements':replacements,'inline_replacements':inline_replacements,'display_equations':len(equations(selected)),
   'equations_sha256':sha(json.dumps(equations(selected)).encode()),'output_sha256':sha(data),
   'footer_links':['research/PROOF_MAP.md','REPRODUCIBILITY.md'],
   'math_rendering':{'display':'fenced math','inline':'GitHub dollar-backtick delimiters','equation_labels':'Markdown outside TeX','operator_macro':'mathrm','single_token_arguments':'explicit braces','relation_spacing':'Protect less-than and greater-than signs from HTML parsing'},
   'formatting':'Preserve mathematical expressions; use fenced math, external equation labels, upright operator names, and explicit single-token macro arguments.'})
 output['maintenance/READING_TRANSFORMS.json']=(json.dumps(ledger,indent=2,sort_keys=True)+'\n').encode()
 return output

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');a=ap.parse_args()
 failures=[]
 for name,data in expected().items():
  p=ROOT/name
  if a.check:
   if not p.exists() or p.read_bytes()!=data:failures.append(name)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 if failures:raise SystemExit('Reading mismatch: '+', '.join(failures))
 print(('Checked' if a.check else 'Generated')+' four scientific reading pages and their transform ledger.')
if __name__=='__main__':main()
