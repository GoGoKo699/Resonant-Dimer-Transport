# Binding resonance and the transport seen by a local pair source

## Physical question

Does binding turn particles with a singular low-momentum velocity into a
composite excitation with a finite velocity cutoff? In the model studied here,
the answer depends on the distance from the rest-binding threshold. A bound
branch at every nonzero total momentum is not, by itself, a statement about
what a local preparation and position measurement can observe. The relevant
question is whether its fast part remains visible after both preparation and
detection probabilities are included.

The result is a sharp contrast in one fixed measurement. Exactly at resonance,
the persistent coincidence signal has an unbounded, algebraically decaying
velocity distribution. At every fixed stronger attraction its limiting
velocity support is bounded. The fastest states have vanishing local overlap
and a diverging internal size. Binding therefore does not impose a finite
velocity cutoff at resonance, but the result does not imply efficient
transport of a compact molecule.

## Model and observable

There is one particle of each of two distinguishable species on the infinite
one-dimensional lattice. In units of lattice spacing and Planck's constant
equal to one, both particles have dispersion

```math
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J > 0,\quad \frac12 < z < 1.
```

They attract only when their positions coincide, with potential
$`-U\delta_{x_a,x_b}`$. The hopping is the standard fractional discrete Laplacian
[5], not an exact power law at all lattice separations. The Hamiltonian is
bounded, translation invariant, and time independent.

Prepare $`|0,0\rangle`$ and measure both positions after evolution. Define

```math
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
```

Every initially prepared pair is a trial. Events with unequal final positions
are not discarded from the normalization. There is no initial band projection,
energy filtering, or momentum selection. On a coincidence, the pair's center
coordinate is $`X=j`$.

The rest-binding threshold is

```math
U_c=2^{1+z}J\sqrt\pi\,
\frac{\Gamma(1-z/2)}{\Gamma((1-z)/2)}.
```

At $`U=U_c`$, the formal rest state is not square integrable. Binding at nonzero
momentum means a normalizable **relative-coordinate** eigenstate below the
continuum at that conserved total momentum. It need not have negative energy
relative to the global two-particle minimum.

## Main transport statement

Let $`E_d(P;U)`$ be the bound energy and let
$`Z(P;U)=|\psi_{P,U}(0)|^2`$ be the contact probability in its normalized relative
state. For $`U\ge U_c`$ and every bounded continuous $`f`$,

```math
\boxed{\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int_{-\pi}^{\pi}\frac{dP}{2\pi}\,
 Z(P;U)^2 f(\partial_P E_d(P;U)).}
```

**(1)**

At resonance the isolated $`P=0`$ fiber may be assigned arbitrary values in this
integral; it has zero momentum measure. This is weak convergence of the
unnormalized coincidence-velocity measure, not a claim about all position
moments or finite-time vanishing outside a cone.

At $`U=U_c`$, suppress the coupling argument. Define

```math
b_z(x)=|x+1/2|^z+|x-1/2|^z,\qquad
F_z(e)=\int_{\mathbb{R}}\frac{dx}{2\pi}
\left[\frac1{b_z(x)-e}-\frac1{2|x|^z}\right].
```

There is a unique $`c_z\in(0,1)`$ with $`F_z(c_z)=0`$. The microscopic spectral
analysis gives

```math
E_d(P)\sim Jc_z|P|^z,\quad
E'_d(P)\sim Jzc_z\mathrm{sgn}(P)|P|^{z-1},\quad
Z(P)\sim B_z|P|^{2z-1},\quad
B_z=\frac{J^2}{U_c^2F'_z(c_z)}.
```

For continuity points $`v>0`$, write

```math
Q(v)=\lim_{t\to\infty}\Pr(x_a=x_b,\ |X| > vt).
```

Equation (1) and the spectral asymptotics imply

```math
\boxed{Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}.}
```

**(2)**

The order is the infinite lattice, long time at fixed $`v`$, and then large
$`v/J`$. In contrast, for each fixed $`U>U_c`$, the dimer has a negative rest
energy and a finite quadratic curvature. The full bound branch has a positive
minimum gap and

```math
v_{\max}(U)=\sup_P|\partial_P E_d(P;U)| < \infty,
\qquad Q_U(v)=0\quad(v > v_{\max}(U)).
```

**(3)**

Equation (3) concerns the limiting measure only. Long-range hopping still
permits finite-time spatial tails.

## How the finite cutoff approaches resonance

The [detuning crossover theorem](DETUNING_CROSSOVER.md) makes the contrast
quantitative without changing the model or detector. Define
$`\delta=J(U_c^{-1}-U^{-1})>0`$ and $`\rho=\delta^{1/(1-z)}`$. A dimensionless
continuum pole profile $`e_z(k)`$ is fixed by

```math
\int_{\mathbb{R}}\frac{dx}{2\pi}
\left[\frac1{|x+k/2|^z+|x-k/2|^z-e_z(k)}-\frac1{2|x|^z}\right]=-1.
```

Uniform microscopic scaling, together with estimates excluding very small
and very large scaled momentum, proves

```math
v_{\max}(U)=\frac{J}{\delta}[K_z+o(1)],\qquad
K_z=\max_{k\ge0}|e_z'(k)| > 0,\qquad |P_{\max}(U)|=\Theta(\rho).
```

Thus the maximum velocity diverges inversely with $`U-U_c`$ for every fixed
$`z`$ in the model's window. The exponent is independent of $`z`$; the coefficient
and the maximizing momentum scale are not. Uniqueness of the maximizing
momentum is unnecessary. The local-source probability in the same scaling
window has a controlled crossover, giving for any fixed $`0<\theta<1`$

```math
Q_U(\theta v_{\max}(U))=\Theta(\delta^{(4z-1)/(1-z)}).
```

For $`z=3/4`$, numerical profile evaluation gives $`K_z\simeq0.1051707`$.
The cutoff therefore rises as $`\delta^{-1}`$, while the probability above a
fixed fraction of it falls as $`\delta^8`$. This is a changing, increasingly
fast event, not the total coincidence probability. The full crossover matches
the resonant tail in its own subsequent small-scaled-velocity limit.

The pole profile and dimensional prediction follow from the same inherited
finite-momentum scattering framework [1]. The additional work is control of
the lattice derivative, global rather than local maximization, and the two
source/detector weights. Long time is taken at fixed detuning before approaching
resonance. The detuning result alone does not supply an observation time;
the separate joint time–detuning estimate below addresses deterministic readout.

The same crossover also fixes the rest contact residue and effective mass.
The [explicit rest coefficients](DETUNING_CROSSOVER.md#explicit-rest-residue-and-curvature)
give $`Z(0;U_\delta)\asymp\rho^{2z-1}`$ and
$`m_d(U_\delta)\asymp J^{-1}\rho^{2-z}`$, where
$`m_d=1/E_d''(0)`$ and $`\rho=\delta^{1/(1-z)}`$.
The vanishing mass describes the divergent rest curvature as resonance is
approached; the rest velocity is still zero at each fixed positive detuning.
This coefficient calculation uses the exact lattice curvature integral and
is separate from the global maximum-velocity statement.

## Why the local measurement matters

The normalized source in each total-momentum fiber is the constant relative-
momentum function. Its contact survival amplitude decomposes as

```math
c_P(t)=Z(P)e^{-itE_d(P)}+b_P(t).
```

The explicit rank-one contact spectral measure has one bound atom and an
integrable continuous density. Its possible exceptional continuum energies
are finite in number and carry no normalizable source-coupled eigenvector.
Thus $`b_P(t)\to0`$ almost everywhere in $`P`$. Set

```math
A^d_j(t)=\int\frac{dP}{2\pi}Z(P)e^{iPj-itE_d(P)},\qquad
\eta(t)^2=\int\frac{dP}{2\pi}|b_P(t)|^2.
```

Dominated convergence gives $`\eta(t)\to0`$. Parseval and Cauchy–Schwarz yield

```math
\sum_j\left|C_j(t)-|A^d_j(t)|^2\right|
\le2\sqrt{W_c}\eta(t)+\eta(t)^2,\qquad
W_c=\int\frac{dP}{2\pi}Z(P)^2.
```

**(4)**

This removes the continuum from the **coincidence observable**, not from the
full state. In particular, the projected bound component is initially
nonlocal; it must not be substituted for the actual local preparation.

The characteristic function of the pole contribution is a momentum integral
with a shift of order $`1/t`$. Translation continuity of $`Z`$ in $`L^2`$ and the
separately established derivative of $`E_d`$ give (1). No differentiation of an
uncontrolled little-o remainder or stationary-phase approximation at the cusp
is required.

The two factors of $`Z`$ have different physical roles: excitation by the local
source and coincidence detection of the resulting relative state. Consequently,

```math
W_b=\int\frac{dP}{2\pi}Z(P),\qquad
\lim_{t\to\infty}\sum_j C_j(t)=W_c < W_b.
```

The asymptotic coincidence mass is not the probability of occupying the bound
sector. Replacing $`Z^2`$ by $`Z`$ changes both the observable and its tail exponent.

## Probability and preparation cost

For $`z=3/4`$, the model calculations give

```math
Q(v)\sim1.9347109013\times10^{-4}(J/v)^8.
```

Direct quadrature of the limiting measure gives the following absolute event
probabilities per prepared pair, without conditioning on a final coincidence:

| $`v/J`$ | $`Q(v)`$ |
|---:|---:|
| 1 | $`2.2546710613\times10^{-4}`$ |
| 2 | $`7.8608836356\times10^{-7}`$ |
| 3 | $`3.0007475914\times10^{-8}`$ |

These values are quadrature diagnostics of the limiting lattice measure.
The finite-time and joint-regime estimates below control the relative error
of deterministic observations.

For a relative source restricted to $`|r|\le R`$, the exact best squared overlap
with a selected bound eigenstate is

```math
M_R(P)=\sum_{|r|\le R}|\psi_P(r)|^2.
```

The normalized restricted eigenfunction attains it. The scaled momentum
wavefunction converges strongly to

```math
h_z(x)=\frac1{\sqrt{F'_z(c_z)}[b_z(x)-c_z]}.
```

With $`\phi_z`$ its inverse Fourier transform, the corresponding lattice
probability profile satisfies

```math
PR(P)\to a\quad\Longrightarrow\quad
M_{R(P)}(P)\to\int_{-a}^{a}|\phi_z(y)|^2dy.
```

For any fixed target overlap $`0<q<1`$, the minimum relative radius therefore
obeys

```math
R_q(P)=\Theta(|P|^{-1}),\qquad
R_q(v)=\Theta((v/J)^{1/(1-z)}).
```

**(5)**

At $`z=3/4`$ the latter grows as the fourth power of velocity. This is a
fiberwise support optimum, applicable to narrow normalizable momentum wave
packets, not a state-loading procedure or a preparation-time bound. Enlarging
only the center-of-mass envelope does not remove the internal size requirement.

The limiting velocity measure is tight. For every $`L(t)/t\to\infty`$,
$`\sum_{|j|>L(t)}C_j(t)\to0`$. Thus unbounded velocity support does not mean a
nonvanishing superballistic coincidence fraction.

## Finite-time error control and a joint observation regime

The sharp event can also be bounded at a deterministic time. Put
$`a=\delta/J`$, $`p_t(s)=\Pr(x_a=x_b,|aX/t|>s)`$, and let $`q(s)`$ denote
its limiting probability. If $`d_t`$ bounds the band-to-velocity event error
and $`e_t`$ bounds the continuum contact-amplitude norm, then

```math
|p_t(s)-q(s)|\le d_t+2\sqrt{q(s)+d_t}\,e_t+e_t^2.
```

The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) gives
$`d_t=S(s,h)+A(h)/t`$ in terms of a narrow velocity-shell mass and explicit
band-derivative norms. Its smoothing is confined to the proof; neither the
actual sharp detector nor the local preparation is changed. For a rare
probability $`q`$, continuum amplitude error small relative to $`\sqrt q`$
suffices, provided $`d_t=o(q)`$.

The [joint observation-time theorem](OBSERVATION_TIME.md) establishes

```math
\eta_U(t)\le\frac{C}{Jt}
```

uniformly for couplings in a fixed interval $`U_c\le U\le U_1`$. The uniformity
holds after the total-momentum integral. Individual-fiber spectral variation
can diverge like $`|P|^{z-1}`$; its square remains integrable for $`z>1/2`$.
The proof treats the lower cusp, a narrow continuum resonance above an
internal local maximum, and the coalescing upper maxima separately.

Together with cusp-safe estimates for $`Z'`$ and $`E''Z`$, this yields a
sufficient joint limit for the unchanged event
$`p_{\delta,t}=\Pr(x_a=x_b,|X|>\theta v_{\max}(U_\delta)t)`$.
For any fixed $`0<\theta<1`$, at $`z=3/4`$,

```math
\boxed{Jt\delta^7/\sqrt{\log(2/\delta)}\to\infty
\quad\Longrightarrow\quad
p_{\delta,t}=C_{3/4,\theta}\delta^8[1+o(1)].}
```

For other fixed $`z`$, the explicit sufficient exponent is given in Eq. (O1)
of that theorem. For each fixed relative accuracy, the corresponding bound
holds at every sufficiently late deterministic time, with constants
independent of small detuning.

This is a sufficient waiting-time regime for the stated relative accuracy.
The exponent and the logarithm at $`z=3/4`$ come from the band norms used in
the estimate.

## Relationship to established work

Sun, Feng, and Zhang [1], published Eqs. (6)–(8), supply the
finite-momentum contact loop. Matching kinetic units and rescaling relative
momentum in the renormalized continuum theory at resonance gives

```math
T(J|P|^ze,P)^{-1}=\frac{|P|^{1-z}}{2J}F_z(e).
```

The pole equation is inherited. Its homogeneity predicts the pole and residue
powers and the detuning scales; these are not separate mechanisms. Their
Supplementary Note 1 matches the microscopic spin model to its low-energy
scattering parameter.

That matching does not identify their auxiliary dimer residue with our
normalized onsite probability $`Z`$. Their spin model forbids two magnons on
one site; Supplementary Note 1, Eqs. (S2)–(S5), enforces this constraint by
taking an onsite repulsion to infinity and introduces separate onsite and
nearest-neighbor auxiliary fields. The factor $`1/2`$ in their loop is a
scattering-amplitude convention: it leaves the pole equation unchanged but
affects the propagator residue. In the present contact lattice model the
normalized source and detector coefficient is fixed separately by the exact
rank-one eigenfunction. Indeed, the scaled continuum wavefunction is square
integrable for $`z>1/2`$, while its formal point value involves an ultraviolet
divergence for $`z<1`$. A bare continuum contact value cannot replace the
microscopic $`B_z`$. The inherited powers and the lattice source/detector
normalization are therefore distinct pieces of the calculation.

The public author response accompanying [1], Eqs. (R5)–(R7), also proposes
evolution from two magnons at finite separation and a resonance diagnostic
based on single-site magnon-density scaling while varying that separation.
It explicitly identifies the growing bound-state size as a detection
difficulty. This is a stated research proposal, distinct from an established
same-site transport theorem.

| Claim or ingredient | Predecessor content | Content established here |
|---|---|---|
| Moving pole and residue | The finite-momentum loop [1] supplies the pole equation and scaling predictions. | Exact fractional-lattice binding and independently controlled energy, velocity, and contact-residue asymptotics. |
| Detuning scales | Homogeneity of that loop predicts $`\lvert E_0\rvert\propto\delta^{z/(1-z)}`$, $`P\sim\delta^{1/(1-z)}`$, and $`v\sim J/\delta`$. | Uniform lattice derivatives, exclusion of competing momentum scales, the global cutoff, and its unconditional coincidence weight. |
| Local pair propagation | Macrì et al. [6] evolve adjacent spins and resolve slow bound and weak unbound components; Kranzl et al. [2] measure nearby-pair propagation. The response to [1] proposes a resonance-dependent local-density diagnostic. | The fixed onsite source and same-site detector give the $`Z^2`$ velocity law, with continuum contact contributions controlled. |
| Deterministic rare-event readout | Spectral variation, Fourier smoothing, and Duhamel bounds are established methods. | Uniform integrated continuum control and a sufficient joint time–detuning regime for the unchanged sharp event. |

The models and measurements in [2,6] differ from the attractive contact
resonance here. In particular, the finite-velocity branch observed in [2]
is not a theorem that every bound pair regularizes a singular velocity.
Albeverio and collaborators [3] establish motion-induced binding under
three-dimensional lattice hypotheses. Domínguez-Castro [4] treats mobile
distinguishable particles with power-law hopping and onsite interaction,
including disappearance of attractive rest dimers.

The contribution assessed here is the microscopic, source-resolved resonance
contrast with its probability, internal-size, and deterministic-time
accounting. The two-body framework, local-pair dynamics, resonance diagnosis
by local quenches, and qualitative size divergence remain inherited. The
preparation result here quantifies optimal relative-support overlap. This
comparison identifies the additional claims and their proof obligations; it
is not exhaustive priority clearance.

## Proof route and endpoint convention

The [proof map](PROOF_MAP.md) connects (1)–(5) to the complete spectral,
transport, and wavefunction arguments. The lattice threshold is always
$`T_P=\epsilon_z(P)`$, not $`J|P|^z`$. The [endpoint lemma](THRESHOLD_ENDPOINT.md)
proves the exact-threshold scaling needed for the weaker-attraction threshold
coefficient. The resonant root has $`c_z<1`$ and is unaffected by that endpoint
correction. The [verification guide](../REPRODUCIBILITY.md) separates finite
checks from these analytical limits.

## Primary references

[1] N. Sun, L. Feng, and P. Zhang, *Efimov effect in long-range quantum spin
chains*, Communications Physics **9**, 146 (2026), doi:10.1038/s42005-026-02580-0.
Published two-magnon Eqs. (6)–(8); Supplementary Note 1, Eqs. (S5)–(S13);
preprint v1 Eqs. (5)–(7). The linked public peer-review file contains the
author response, Eqs. (R5)–(R7), pp. 6–7.
https://www.nature.com/articles/s42005-026-02580-0

[Public author response](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42005-026-02580-0/MediaObjects/42005_2026_2580_MOESM2_ESM.pdf).

[2] F. Kranzl et al., *Observation of magnon bound states in the long-range,
anisotropic Heisenberg model*, Physical Review X **13**, 031017 (2023),
doi:10.1103/PhysRevX.13.031017. Preparation and propagation in Sections III–IV.
https://arxiv.org/html/2212.03899v2

[3] S. Albeverio, S. N. Lakaev, K. A. Makarov, and Z. I. Muminov,
*The Threshold effects for the two-particle Hamiltonians on lattices*,
arXiv:math-ph/0501013. The three-dimensional motion-induced-binding result.
https://arxiv.org/abs/math-ph/0501013

[4] G. A. Domínguez-Castro, *Bose Polaron in a One-Dimensional Lattice with
Power-Law Hopping*, Atoms **11**, 110 (2023), doi:10.3390/atoms11080110.
Section 4 concerns the exact two-body problem; the later many-body polaron
approximation is not used here.
https://www.mdpi.com/2218-2004/11/8/110

[5] O. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea, and J. L. Varona,
*Nonlocal discrete diffusion equations and the fractional discrete Laplacian,
regularity and applications*, arXiv:1608.08913. Fractional lattice operator
and kernel, as recorded in the spectral foundation.
https://arxiv.org/abs/1608.08913

[6] T. Macrì, L. Lepori, G. Pagano, M. Lewenstein, and L. Barbiero,
*Bound state dynamics in the long-range spin-1/2 XXZ model*,
Physical Review B **104**, 214309 (2021), doi:10.1103/PhysRevB.104.214309.
Section IV and Figure 3: dynamics from two neighboring spins.
https://arxiv.org/html/2110.01760v1
