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

$$
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J>0,\quad \frac12<z<1.
$$

They attract only when their positions coincide, with potential
$-U\delta_{x_a,x_b}$. The hopping is the standard fractional discrete Laplacian
[5], not an exact power law at all lattice separations. The Hamiltonian is
bounded, translation invariant, and time independent.

Prepare $|0,0\rangle$ and measure both positions after evolution. Define

$$
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
$$

Every initially prepared pair is a trial. Events with unequal final positions
are not discarded from the normalization. There is no initial band projection,
energy filtering, or momentum selection. On a coincidence, the pair's center
coordinate is $X=j$.

The rest-binding threshold is

$$
U_c=2^{1+z}J\sqrt\pi\,
\frac{\Gamma(1-z/2)}{\Gamma((1-z)/2)}.
$$

At $U=U_c$, the formal rest state is not square integrable. Binding at nonzero
momentum means a normalizable **relative-coordinate** eigenstate below the
continuum at that conserved total momentum. It need not have negative energy
relative to the global two-particle minimum.

## Main transport statement

Let $E_d(P;U)$ be the bound energy and let
$Z(P;U)=|\psi_{P,U}(0)|^2$ be the contact probability in its normalized relative
state. For $U\ge U_c$ and every bounded continuous $f$,

$$
\boxed{\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int_{-\pi}^{\pi}\frac{dP}{2\pi}\,
 Z(P;U)^2 f(\partial_P E_d(P;U)).}\tag{1}
$$

At resonance the isolated $P=0$ fiber may be assigned arbitrary values in this
integral; it has zero momentum measure. This is weak convergence of the
unnormalized coincidence-velocity measure, not a claim about all position
moments or finite-time vanishing outside a cone.

At $U=U_c$, suppress the coupling argument. Define

$$
b_z(x)=|x+1/2|^z+|x-1/2|^z,\qquad
F_z(e)=\int_{\mathbb R}\frac{dx}{2\pi}
\left[\frac1{b_z(x)-e}-\frac1{2|x|^z}\right].
$$

There is a unique $c_z\in(0,1)$ with $F_z(c_z)=0$. The microscopic spectral
analysis gives

$$
E_d(P)\sim Jc_z|P|^z,\quad
E'_d(P)\sim Jzc_z\operatorname{sgn}(P)|P|^{z-1},\quad
Z(P)\sim B_z|P|^{2z-1},\quad
B_z=\frac{J^2}{U_c^2F'_z(c_z)}.
$$

For continuity points $v>0$, write

$$
Q(v)=\lim_{t\to\infty}\Pr(x_a=x_b,\ |X|>vt).
$$

Equation (1) and the spectral asymptotics imply

$$
\boxed{Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}.}\tag{2}
$$

The order is the infinite lattice, long time at fixed $v$, and then large
$v/J$. In contrast, for each fixed $U>U_c$, the dimer has a negative rest
energy and a finite quadratic curvature. The full bound branch has a positive
minimum gap and

$$
v_{\max}(U)=\sup_P|\partial_P E_d(P;U)|<\infty,
\qquad Q_U(v)=0\quad(v>v_{\max}(U)).\tag{3}
$$

Equation (3) concerns the limiting measure only. Long-range hopping still
permits finite-time spatial tails.

## Why the local measurement matters

The normalized source in each total-momentum fiber is the constant relative-
momentum function. Its contact survival amplitude decomposes as

$$
c_P(t)=Z(P)e^{-itE_d(P)}+b_P(t).
$$

The explicit rank-one contact spectral measure has one bound atom and an
integrable continuous density. Its possible exceptional continuum energies
are finite in number and carry no normalizable source-coupled eigenvector.
Thus $b_P(t)\to0$ almost everywhere in $P$. Set

$$
A^d_j(t)=\int\frac{dP}{2\pi}Z(P)e^{iPj-itE_d(P)},\qquad
\eta(t)^2=\int\frac{dP}{2\pi}|b_P(t)|^2.
$$

Dominated convergence gives $\eta(t)\to0$. Parseval and Cauchy–Schwarz yield

$$
\sum_j\left|C_j(t)-|A^d_j(t)|^2\right|
\le2\sqrt{W_c}\eta(t)+\eta(t)^2,\qquad
W_c=\int\frac{dP}{2\pi}Z(P)^2.\tag{4}
$$

This removes the continuum from the **coincidence observable**, not from the
full state. In particular, the projected bound component is initially
nonlocal; it must not be substituted for the actual local preparation.

The characteristic function of the pole contribution is a momentum integral
with a shift of order $1/t$. Translation continuity of $Z$ in $L^2$ and the
separately established derivative of $E_d$ give (1). No differentiation of an
uncontrolled little-o remainder or stationary-phase approximation at the cusp
is required.

The two factors of $Z$ have different physical roles: excitation by the local
source and coincidence detection of the resulting relative state. Consequently,

$$
W_b=\int\frac{dP}{2\pi}Z(P),\qquad
\lim_{t\to\infty}\sum_j C_j(t)=W_c<W_b.
$$

The asymptotic coincidence mass is not the probability of occupying the bound
sector. Replacing $Z^2$ by $Z$ changes both the observable and its tail exponent.

## Probability and preparation cost

For $z=3/4$, the model calculations give

$$
Q(v)\sim1.9347109013\times10^{-4}(J/v)^8.
$$

Direct quadrature of the limiting measure gives the following absolute event
probabilities per prepared pair, without conditioning on a final coincidence:

| $v/J$ | $Q(v)$ |
|---:|---:|
| 1 | $2.2546710613\times10^{-4}$ |
| 2 | $7.8608836356\times10^{-7}$ |
| 3 | $3.0007475914\times10^{-8}$ |

These are the preserved model diagnostics, not experimentally established
rates or certified numerical intervals. Equation (4) currently supplies no
uniform observation time that resolves these rare events with small relative
error.

For a relative source restricted to $|r|\le R$, the exact best squared overlap
with a selected bound eigenstate is

$$
M_R(P)=\sum_{|r|\le R}|\psi_P(r)|^2.
$$

The normalized restricted eigenfunction attains it. The scaled momentum
wavefunction converges strongly to

$$
h_z(x)=\frac1{\sqrt{F'_z(c_z)}[b_z(x)-c_z]}.
$$

With $\phi_z$ its inverse Fourier transform, the corresponding lattice
probability profile satisfies

$$
PR(P)\to a\quad\Longrightarrow\quad
M_{R(P)}(P)\to\int_{-a}^{a}|\phi_z(y)|^2dy.
$$

For any fixed target overlap $0<q<1$, the minimum relative radius therefore
obeys

$$
R_q(P)=\Theta(|P|^{-1}),\qquad
R_q(v)=\Theta((v/J)^{1/(1-z)}).\tag{5}
$$

At $z=3/4$ the latter grows as the fourth power of velocity. This is a
fiberwise support optimum, applicable to narrow normalizable momentum wave
packets, not a state-loading procedure or a preparation-time bound. Enlarging
only the center-of-mass envelope does not remove the internal size requirement.

The limiting velocity measure is tight. For every $L(t)/t\to\infty$,
$\sum_{|j|>L(t)}C_j(t)\to0$. Thus unbounded velocity support does not mean a
nonvanishing superballistic coincidence fraction.

## Relationship to established work

Sun, Feng, and Zhang [1] provide the finite-total-momentum contact scattering
framework. At their resonance, matching kinetic units and rescaling relative
momentum yields $T(J|P|^ze,P)^{-1}=|P|^{1-z}F_z(e)/(2J)$. The pole equation is
therefore inherited; the factor of two does not change its zero. The physical
statement assessed here connects that pole and its residue to a specified,
unconditioned lattice position measurement.

Kranzl and collaborators [2] already prepare nearby magnons and observe
bound-pair propagation with finite group velocity in their selected
long-range Heisenberg regime. Their interaction and branch differ from the
attractive contact resonance here. Albeverio and collaborators [3] establish
motion-induced binding under three-dimensional lattice hypotheses.
Domínguez-Castro [4] treats mobile distinguishable particles with power-law
hopping and onsite interaction, including disappearance of attractive rest
dimers. These works preclude novelty claims for motion-induced binding,
local pair detection, or the basic two-species scattering model.

The remaining contribution is the microscopic, source-resolved resonance
contrast, with its probability and internal-size accounting. The strongest
objection is that this can be viewed as a precise consequence of existing
two-body resonance theory using familiar spectral tools. Merely adding more
coefficients or presenting the support projection as a separate mechanism
would not answer that objection. The comparison is targeted, not exhaustive
priority clearance.

## Proof route and endpoint convention

The [proof map](PROOF_MAP.md) connects (1)–(5) to the complete spectral,
transport, and wavefunction arguments. The lattice threshold is always
$T_P=\epsilon_z(P)$, not $J|P|^z$. The [endpoint lemma](THRESHOLD_ENDPOINT.md)
proves the exact-threshold scaling needed for the weaker-attraction threshold
coefficient. The resonant root has $c_z<1$ and is unaffected by that endpoint
correction. The [verification guide](../REPRODUCIBILITY.md) separates finite
checks from these analytical limits.

## Primary references

[1] N. Sun, L. Feng, and P. Zhang, *Efimov effect in long-range quantum spin
chains*, Communications Physics **9**, 146 (2026), doi:10.1038/s42005-026-02580-0.
Published two-magnon Eqs. (6)–(8); preprint v1 Eqs. (5)–(7).
https://www.nature.com/articles/s42005-026-02580-0

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
