# Resonant-Dimer-Transport

**What does a local source actually detect when a bound pair has a singular velocity?**

Two distinguishable particles hop on a one-dimensional lattice with a fractional kinetic energy and attract on the same site. At the rest-binding threshold, the persistent same-site coincidence signal has an algebraically unbounded velocity distribution. At any fixed stronger attraction, the same measurement has bounded limiting velocity support.

The result includes the probability cost of local creation and detection, the scattering continuum, and the spatial extent needed to prepare fast dimers with fixed overlap. It is not a claim of efficient superballistic transport.

## Physical task

The single-particle dispersion is

$$
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J>0,\quad \tfrac12<z<1.
$$

The interaction is $-U\delta_{x_a,x_b}$. Prepare $|0,0\rangle$, evolve, and measure both positions. The unconditional same-site probability is

$$
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
$$

Trials with unequal final positions remain part of the normalization. No initial projection onto a bound band or final energy filtering is supplied.

## Main result

Let $E_d(P)$ be the below-continuum dimer energy and $Z(P)$ its onsite overlap probability. For every bounded continuous test function $f$,

$$
\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int_{-\pi}^{\pi}\frac{dP}{2\pi}\,Z(P)^2 f(E'_d(P)).
$$

At resonance, $E'_d(P)$ diverges near zero momentum while $Z(P)$ vanishes. Both source and detector overlaps matter. The resulting high-velocity coincidence tail is

$$
Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}.
$$

For $z=3/4$ it is proportional to $(J/v)^8$: the tail persists but is rare. The limit takes the infinite lattice first, then long time at fixed velocity, and finally high velocity. It is not a fixed-time arrival guarantee or a strict light cone.

A fixed capture probability in a selected fast eigenstate requires relative source radius of order

$$
R_{\min}(v)=\Theta\!\left((v/J)^{1/(1-z)}\right).
$$

This is optimal wavefunction support, not a loading protocol. The fastest bound states are spatially large rather than compact molecules.

## Approach to resonance

The finite cutoff has a controlled divergence. With the dimensionless detuning
$\delta=J(U_c^{-1}-U^{-1})>0$,

$$
v_{\max}(U)\sim K_z\frac{J}{\delta},\qquad
|P_{\max}(U)|=\Theta(\delta^{1/(1-z)}).
$$

For any fixed $0<\theta<1$, the unconditional coincidence probability above
$\theta v_{\max}(U)$ is of order $\delta^{(4z-1)/(1-z)}$. At $z=3/4$, better
tuning raises the cutoff as $\delta^{-1}$ while its near-cutoff weight falls
as $\delta^8$. The [detuning theorem](research/DETUNING_CROSSOVER.md) proves the
global maximum, its momentum scale, and the full probability crossover.
Long time is taken at each fixed detuning first; this is not a finite-time
visibility guarantee.

![Absolute coincidence tails and the probability near the velocity cutoff](figures/coincidence_tail.svg)

For $z=3/4$, the lattice calculation compares resonance with three positive
detunings. Dashed lines mark the located velocity cutoffs. The right panel
shows the absolute probability above $90\%$ of each cutoff: the larger cutoff
comes with a rarer event. These are limiting probabilities per prepared pair.
[Data and reproduction](REPRODUCIBILITY.md#coincidence-tail-figure) include
crossing, quadrature, and source-overlap checks.

## Finite-time accuracy

The [finite-time certificate](research/FINITE_TIME_CERTIFICATE.md) bounds the
error of the same sharp coincidence event at a deterministic observation time.
It combines static spectral variation, band-derivative norms, and a narrow
velocity-shell mass. An event with limiting probability $q$ requires continuum
amplitude error small relative to $\sqrt q$, rather than $q$. A sufficient
time is explicit in these static quantities.

The [joint observation-time theorem](research/OBSERVATION_TIME.md) bounds the
full continuum contact amplitude by $C/(Jt)$ uniformly near resonance after
integration over total momentum. Together with sharper band norms, it gives
a sufficient simultaneous time–detuning regime. At $z=3/4$,

$$
Jt\delta^7/\sqrt{\log(2/\delta)}\longrightarrow\infty
\quad\Longrightarrow\quad
p_{\delta,t}\sim C_{3/4,\theta}\delta^8,
$$

where $p_{\delta,t}$ is the actual coincidence probability beyond
$\theta v_{\max}(U_\delta)t$, for a fixed $0<\theta<1$. The general
fixed-$z$ statement is in that theorem. This is a sufficient upper-bound
regime, not a necessary or optimal time scale. Its prefactor has not been
interval-evaluated, so no numerical experimental observation window is asserted.

## Reading route

| Document | Purpose |
|---|---|
| [Results index](research/RESULTS.md) | All established results, their proof locations, and interpretation boundaries. |
| [Author account](research/AUTHOR_ACCOUNT.md) | Background, precise claims, physical interpretation, and closest predecessors. |
| [Theorem](research/THEOREM.md) | Model, local observation, limiting velocity law, and preparation-size result. |
| [Proof map](research/PROOF_MAP.md) | Dependencies and complete spectral and transport proofs. |
| [Spectral foundation](research/SPECTRAL_PROOF.md) | Rest threshold, moving pole, differentiated velocity, and residue. |
| [Detuning crossover](research/DETUNING_CROSSOVER.md) | Global inverse-detuning velocity cutoff and its source-weighted probability law. |
| [Finite-time certificate](research/FINITE_TIME_CERTIFICATE.md) | Deterministic-time relative-error bound and its static spectral budgets. |
| [Joint observation time](research/OBSERVATION_TIME.md) | Uniform integrated continuum decay and a sufficient simultaneous time–detuning regime. |
| [Boundary resolvent](research/BOUNDARY_RESOLVENT.md) | Cusp, smooth-maximum, and principal-value calculations supporting the continuum estimates. |
| [Threshold endpoint](research/THRESHOLD_ENDPOINT.md) | Correct lattice-edge scaling and the domain of the continuum approximation. |
| [Transport proof](research/TRANSPORT_PROOF.md) | Continuum separation, two overlap factors, and unconditional measurement law. |
| [Contribution assessment](research/CONTRIBUTION.md) | Closest predecessors and the precise claim remaining after attribution. |
| [Reproducibility](REPRODUCIBILITY.md) | Thirty-three scientific groups, source integrity, and report comparisons. |

The finite-momentum scattering framework, motion-induced lattice binding, fractional lattice operator, nearby-pair detection, and spectral pushforward methods have explicit predecessors. The assessed contribution is their microscopic, source-resolved resonance contrast, not a new scattering mechanism or general optimization principle.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[MIT license](LICENSE).
