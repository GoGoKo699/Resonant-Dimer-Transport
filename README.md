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
That theorem takes long time at each fixed detuning first. The finite-time
extension below gives a separate sufficient joint-limit condition, not an
experimental visibility guarantee.

## Finite-time resolution

A conservative joint-limit theorem now controls the original sharp coincidence
event at deterministic finite times. For fixed $0<\theta<1$, define

$$
p_\delta(t;\theta)=\Pr_U(x_a=x_b,\ |X|>\theta v_{\max}(U)t).
$$

The [finite-time proof](research/FINITE_TIME.md) shows that

$$
Jt_\delta\,\delta^{M_z}\to\infty
\quad\Longrightarrow\quad
\frac{p_\delta(t_\delta;\theta)}{Q_U(\theta v_{\max}(U))}\to1,
\qquad M_z=\frac{(4z-1)(10-z)}{4(1-z)(2z-1)}.
$$

At $z=3/4$, $M_z=37$. This is a **sufficient, nonoptimized bound**, not a
necessary waiting time, a physical relaxation exponent, or an experimentally
useful operating window. It follows from a uniform continuum estimate and a
sharp-event Fourier bound; no time averaging or change of source/detector is
introduced. The result controls error relative to the shrinking probability,
while retaining the infinite-lattice assumption.

## Reading route

| Document | Purpose |
|---|---|
| [Author account](research/AUTHOR_ACCOUNT.md) | Background, precise claims, physical interpretation, and closest predecessors. |
| [Theorem](research/THEOREM.md) | Model, local observation, limiting velocity law, and preparation-size result. |
| [Proof map](research/PROOF_MAP.md) | Dependencies and complete spectral and transport proofs. |
| [Spectral foundation](research/SPECTRAL_PROOF.md) | Rest threshold, moving pole, differentiated velocity, and residue. |
| [Finite-time resolution](research/FINITE_TIME.md) | Deterministic relative-error joint limit and explicit conservative error bounds. |
| [Detuning crossover](research/DETUNING_CROSSOVER.md) | Global inverse-detuning velocity cutoff and its source-weighted probability law. |
| [Threshold endpoint](research/THRESHOLD_ENDPOINT.md) | Correct lattice-edge scaling and the domain of the continuum approximation. |
| [Transport proof](research/TRANSPORT_PROOF.md) | Continuum separation, two overlap factors, and unconditional measurement law. |
| [Contribution assessment](research/CONTRIBUTION.md) | Closest predecessors and the precise claim remaining after attribution. |
| [Reproducibility](REPRODUCIBILITY.md) | Twenty-nine scientific groups, source integrity, and preserved-report comparisons. |

The finite-momentum scattering framework, motion-induced lattice binding, fractional lattice operator, nearby-pair detection, and spectral pushforward methods have explicit predecessors. The assessed contribution is their microscopic, source-resolved resonance contrast, not a new scattering mechanism or general optimization principle.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[MIT license](LICENSE).
