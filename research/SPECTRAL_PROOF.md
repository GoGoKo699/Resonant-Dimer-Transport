# Spectral foundation of the resonant dimer

## 1. A fully specified microscopic model

Use two distinguishable particles, one of each species, on the infinite lattice Z. Lattice spacing and hbar are one. Both have the dispersion

```math
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J > 0,\quad \tfrac12 < z < 1.
```

They interact only on the same site, with attractive potential -U delta_(x_a,x_b), U>0. The complete Hamiltonian is bounded and self-adjoint in the two-particle sector. The Hamiltonian is time independent and translation invariant.

The single-particle operator is the established fractional power J(-Delta)^(z/2) of the discrete Laplacian [CRSTV]. Its hopping at nonzero integer separation r is positive in the convention H=diagonal - sum_r t_r translation_r:

```math
t_r=\frac{J\Gamma(1+z)\sin(\pi z/2)}{\pi}
\frac{\Gamma(|r|-z/2)}{\Gamma(|r|+1+z/2)}
\sim \frac{J\Gamma(1+z)\sin(\pi z/2)}{\pi |r|^{1+z}}.
```

The gamma-function kernel fixes the microscopic short-distance hopping; its long-distance power is J/|r|^(1+z) times the stated coefficient.

Total crystal momentum P is conserved. In a P fiber the relative-momentum Hamiltonian acts in L^2([-pi,pi],dq/(2pi)) as

```math
h_P=A_P-U|1\rangle\langle1|,\quad
A_P(q)=\epsilon_z(q+P/2)+\epsilon_z(q-P/2),
```

where |1> is the constant normalized function. A below-continuum eigenvalue satisfies the exact rank-one equation

```math
\frac1U=I_P(E),\qquad I_P(E)=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac1{A_P(q)-E}.
```

**(1)**

Its relative wave function is proportional to (A_P-E)^(-1). For fixed P and E below the band it is normalizable. A momentum eigenstate is not a normalizable center-of-mass state on the entire infinite lattice; one may form wave packets from the fibers. Binding here means relative-coordinate localization below the scattering continuum **at the conserved P**, not a negative energy relative to the global two-particle minimum.

## 2. The continuum edge and the rest threshold

The chord identity and 0<z<1 give

```math
|1-e^{i(p+q)}|^z\le (|1-e^{ip}|+|1-e^{iq}|)^z
\le |1-e^{ip}|^z+|1-e^{iq}|^z.
```

Therefore epsilon_z is subadditive on the momentum circle and

```math
E_{\rm th}(P)=\min_q A_P(q)=\epsilon_z(P).
```

**(2)**

The two threshold configurations put the individual momenta at 0 and P. Equal sharing P/2,P/2 has higher energy. The subadditivity is strict away from configurations involving a zero momentum.

At P=0 the threshold integral is finite because z<1. Its beta integral gives

```math
U_c=2^{1+z}J\sqrt\pi\,
\frac{\Gamma(1-z/2)}{\Gamma((1-z)/2)},\qquad I_0(0)=U_c^{-1}.
```

**(3)**

For U<Uc there is no rest bound state. For U>Uc there is exactly one negative rest eigenvalue. At U=Uc the formal zero-energy solution is proportional to 1/(2epsilon_z(q)), hence behaves as |q|^(-z). It is integrable but not square integrable for z>1/2. Thus the threshold is a resonance, not a normalizable zero-energy dimer.

The parameter window is not arbitrary: z<1 permits a nonzero rest binding threshold, while z>1/2 makes the threshold solution nonnormalizable and the renormalized finite-energy difference ultraviolet convergent. These roles also occur in the two-body resonance analysis of [SFZ].

## 3. Exact bound state for every nonzero momentum at U=Uc

For a,b>0,

```math
\frac1{a+b}\le\frac14\left(\frac1a+\frac1b\right).
```

Apply this pointwise to the two shifted dispersions and use translation invariance of the integral. For P not zero modulo 2pi the inequality is strict on a set of positive measure, so

```math
I_P(0) < I_0(0).
```

**(4)**

For the other endpoint, use uncentered momentum p=q+P/2. Subadditivity gives

```math
0 < \epsilon_z(p)+\epsilon_z(P-p)-\epsilon_z(P)\le2\epsilon_z(p)
```

almost everywhere, with strict inequality on a set of positive measure. The zeros of the denominator are integrable cusps of order |p|^z or |p-P|^z. Thus

```math
I_P(E_{\rm th}(P)) > I_0(0).
```

**(5)**

Since I_P(E) is continuous and strictly increasing below the edge, (4)–(5) bracket exactly one eigenvalue at U=Uc:

```math
\boxed{0 < E_d(P) < \epsilon_z(P)\quad\text{for every}\quad P\ne0.}
```

**(6)**

This establishes an infinite-lattice relative-coordinate eigenstate separated from the continuum at its conserved total momentum.

The general phenomenon that motion changes the internal binding problem on a lattice is inherited from [ALMM]. Their displayed theorem uses a three-dimensional lattice and twice-differentiable dispersions with a nondegenerate minimum. Those assumptions are not satisfied by the one-dimensional cusp here. This distinguishes theorem scope, not ownership of the physical mechanism.

## 4. Universal fractional dispersion

Define, for e<=1,

```math
F_z(e)=\int_{\mathbb{R}}\frac{dx}{2\pi}
\left[\frac1{|x+1/2|^z+|x-1/2|^z-e}-\frac1{2|x|^z}\right].
```

**(7)**

At e=1 the threshold singularities remain integrable. At infinity the difference is O(|x|^(-2z)) plus O(|x|^(-z-2)); z>1/2 ensures convergence. The subtraction at x=0 is integrable because z<1.

A useful sign proof does not require numerical root finding. At e=0, replace the subtraction in the integral by one quarter of the sum of its two shifted versions. The integral of the change tends to zero under symmetric large cutoffs. The integrand becomes

```math
\frac1{a+b}-\frac14\left(\frac1a+\frac1b\right)
=-\frac{(a-b)^2}{4ab(a+b)},
```

with a=|x+1/2|^z and b=|x-1/2|^z. Hence F_z(0)<0. At e=1, shift to p=x+1/2 and use |1-p|^z<=1+|p|^z. The resulting integrand relative to 1/(2|p|^z) is strictly positive almost everywhere. Hence F_z(1)>0. Also

```math
F'_z(e)=\int_{\mathbb{R}}\frac{dx}{2\pi}
\frac1{(|x+1/2|^z+|x-1/2|^z-e)^2} > 0\quad(e < 1).
```

There is a unique c_z in (0,1) with F_z(c_z)=0.

### Controlled passage from the lattice to (7)

For e in a compact subset below 1,

```math
I_P(J|P|^z e)-I_0(0)
=\frac{|P|^{1-z}}J[F_z(e)+o(1)].
```

**(8)**

Here is an explicit convergence argument. On |q|<=M|P| scale q=|P|x and use epsilon_z(q)=J|q|^z[1+O(q^2)]. For fixed M the subtraction is dominated near x=0 by |x|^(-z); the positive gap 1-e controls the other denominator. In the intermediate tail M|P|<=|q|<=q0, with M>=2, symmetric Taylor expansion of the shifted dispersion bounds the difference by

```math
\frac C J\left(|P|^z|q|^{-2z}+P^2|q|^{-z-2}\right).
```

After division by |P|^(1-z)/J, its integral is bounded by C[M^(1-2z)+M^(-1-z)]. The part |q|>=q0 is O(|P|^z+P^2) before division and vanishes because 2z>1. First take P to zero at fixed M, then M to infinity. Constants may depend on z and the compact e interval. At the endpoint use the exact lattice energy $E=E_{\rm th}(P)=\epsilon_z(P)$, not $E=J|P|^z$. The latter is above the lattice edge, so Eq. (8) cannot be extended by substituting e=1. The [exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint expansion with coefficient F_z(1), using uniform cusp domination and the same tail splitting.

Monotonicity and two fixed energies bracketing c_z transfer (8) to the exact eigenvalue:

```math
\boxed{E_d(P)=c_zJ|P|^z+o(|P|^z),\quad
\frac{E_{\rm th}(P)-E_d(P)}{E_{\rm th}(P)}\to1-c_z > 0.}
```

**(9)**

Thus the binding is of the **same low-energy order** as the continuum edge, not a higher-order lattice correction to a free center-of-mass motion.

Numerical values, not interval certificates:

| z | c_z | limiting relative binding 1-c_z |
|---:|---:|---:|
| 0.60 | 0.2558876112 | 0.7441123888 |
| 0.75 | 0.6340774020 | 0.3659225980 |
| 0.90 | 0.9045901716 | 0.0954098284 |

The exact lattice calculation at z=0.75 gives E_d(P)/(J P^z) = 0.6454158452, 0.6378187108, 0.6352643638 at P=0.1,0.01,0.001, approaching c_z. These are below-band pole calculations, not fitted dispersion exponents.

### Group velocity: a separate differentiated estimate

A leading expansion with an unspecified little-o remainder is not enough on its own to differentiate (9). Implicit differentiation of (1) instead gives

```math
E'_d(P)=\frac{\int dq/(2\pi)\,\partial_PA_P(q)/(A_P(q)-E_d(P))^2}
{\int dq/(2\pi)\,1/(A_P(q)-E_d(P))^2}.
```

**(10)**

The numerator's cusps have integrable powers |q+-P/2|^(z-1). Scale q=Px for P>0. Put B_z(x)=|x+1/2|^z+|x-1/2|^z and b_z(x)=zB_z(x)-xB'_z(x). The numerator is J^(-1)P^(-z)[N_z(c_z)+o(1)], where N_z(e)=integral b_z/(B_z-e)^2. Its scaled tail is O(M^(-1-z)); the denominator is J^(-2)P^(1-2z)[F'_z(c_z)+o(1)]. Both statements follow from the same splitting as above and dominated convergence at the moving cusps.

Integration by parts with the subtracted integrand in (7) gives

```math
N_z(e)=zeF'_z(e)-(1-z)F_z(e).
```

The boundary term vanishes because it is O(|x|^(1-2z)) plus O(|x|^(-1-z)). At the root this is zc_zF'_z(c_z). Hence

```math
\boxed{E'_d(P)\sim zc_zJ P^{z-1}\quad(P\downarrow0).}
```

**(11)**

It is a diverging **spectral group velocity**. Its local-source coincidence weight is derived in [the transport proof](TRANSPORT_PROOF.md).

## 5. Why a dimer away from resonance is different

Fix U>Uc, so that E0=E_d(0)<0. Then

```math
E_d(P)=E_0+C(U)P^2+o(P^2),\qquad
C(U)=\frac{\int dq/(2\pi)\,[\epsilon'_z(q)]^2/[2\epsilon_z(q)-E_0]^3}
{\int dq/(2\pi)\,1/[2\epsilon_z(q)-E_0]^2} > 0.
```

**(12)**

The coefficient is finite because epsilon'_z(q)^2 is integrable for z>1/2. The effective mass is 1/[2C(U)]. This holds for the same fractional single-particle kinetics, not by replacing it with a quadratic approximation.

A clean proof controls the cusp instead of formally inserting a nonintegrable second derivative. For E<0 use

```math
I_P(E)=\int_0^\infty ds\,e^{sE}\langle h_s(\cdot+P/2),h_s(\cdot-P/2)\rangle,
\quad h_s(q)=e^{-s\epsilon_z(q)}.
```

Each h_s is in the periodic Sobolev space H^1. Its autocorrelation equals ||h_s||^2-P^2||h'_s||^2/2+o(P^2), and the difference is bounded by P^2||h'_s||^2/2. Integrating in s is justified by E<0 and gives
I_P(E)=I_0(E)-P^2 integral epsilon'^2/(2epsilon-E)^3+o(P^2).
The implicit function relation proves (12). The differentiated autocorrelation argument also gives E'_d(P)=2C(U)P+o(P).

The resonance is therefore singular: the finite-mass description at fixed U>Uc does not extend to U=Uc. The constants in (12) are not uniform as E0 approaches zero.

## 6. Spectral weight and preparation accounting

Normalize the below-band relative wave function. The overlap with a normalized onsite pair in a fixed-momentum fiber is

```math
Z(P)=|\psi_P(0)|^2=\frac1{U_c^2 I'_P(E_d(P))}.
```

The same scaling used in (10) gives

```math
\boxed{Z(P)\sim\frac{J^2}{U_c^2F'_z(c_z)}|P|^{2z-1}\longrightarrow0.}
```

**(13)**

At z=0.75 the coefficient is 0.6816851254..., so Z(P) is asymptotic to that constant times sqrt(|P|). This is the spectral weight of the discrete line seen by onsite pair creation; it is not the fraction of every possible prepared pair that binds.

In a finite-volume regularization the normalized operator creating the probe is L^(-1/2) sum_x exp(iPx) a_x^dagger b_x^dagger. Its vacuum spectral measure has a line of weight Z(P) at E_d(P), plus a continuum. The infinite-volume limit defines the fiber quantity. Both the gap and its contact weight decrease toward P=0. Consequently, increasingly small momenta demand spectral resolution and have decreasing overlap with this local pair source.

Total momentum is conserved in this translation-invariant problem. Bound wavefunctions in a long-range hopping model need not decay exponentially.

## 7. A hard-core, nearest-neighbor control

The contact example is not the only interaction supporting the low-momentum pole. As a specified control, keep the same fractional kinetic energy, forbid double occupancy, and put an attraction -V at relative separations +-1. Consider identical bosons, so the even relative-coordinate sector is the physical one. This is the two-magnon structure of a long-range XY chain with a nearest-neighbor longitudinal attraction, though our short-distance hopping kernel differs from [SFZ]'s pure power.

Define g_r(E,P)=integral cos(rq)/(A_P-E). Eliminating the forbidden site by a Schur complement gives the even nearest-neighbor resolvent

```math
I_{\rm hc}=g_0+g_2-2g_1^2/g_0,\qquad V^{-1}=I_{\rm hc}.
```

**(14)**

At rest zero energy,

```math
g_0=U_c^{-1},\quad a:=g_1/g_0=\frac z{2-z},\quad
b:=g_2/g_0=\frac{z(2+z)}{(2-z)(4-z)},
\quad V_c=[g_0(1+b-2a^2)]^{-1}.
```

**(15)**

The threshold vector has numerator proportional to cos(q)-a; since 1-a>0, it is again a nonnormalizable resonance, not a threshold eigenstate. Each fixed-r g_r has the same leading change as g_0 in (8), because cos(rq)=1+O(q^2) in the singular region. Taylor expansion of (14) gives

```math
I_{\rm hc}(J|P|^ze,P)-I_{\rm hc}(0,0)
=2(1-a)^2\frac{|P|^{1-z}}J[F_z(e)+o(1)].
```

**(16)**

The prefactor is strictly positive. Thus at V=Vc there is a below-band even eigenvalue for all sufficiently small nonzero P with **the same c_z**. The assertion is local in momentum; no all-P hard-core theorem is claimed. Monotonicity follows directly from the resolvent of the projected kinetic operator below its spectrum. No other even below-band state can occur because the remaining attractive interaction has rank one there.

For z=.75, Vc/J=1.4411355579.... The ratios E_hc/(J P^z) are 0.5949493530,0.6195852551,0.6293576619 at P=.1,.01,.001, approaching c_z from the other side of the contact result. This is a microscopic control, not proof of universality for arbitrary interactions or every spin apparatus.

## 8. Weaker attraction and the near-resonance momentum window

For the contact model define Uc(P)=1/I_P(E_th(P)). Equations (5) and (8) imply

```math
U_c(P) < U_c\ (P\ne0),\qquad
\frac1{U_c(P)}-\frac1{U_c}
=\frac{|P|^{1-z}}J[F_z(1)+o(1)].
```

**(17)**

In a joint weak-detuning limit, set h=J(U^(-1)-Uc^(-1))/|P|^(1-z)>=0. Away from its threshold endpoint the universal bound equation is F_z(e)=h. It has a solution below continuum exactly for 0<=h<F_z(1); for h>F_z(1) no such pole occurs in that scaling window. At equality the pole meets the continuum. This does not prove global monotonicity in P or a unique critical momentum throughout the Brillouin zone.

A finite control with z=.75 and U=.7Uc has no below-band contact state at P=.0001, but has one at P=.1. The momentum-dependent availability of binding itself is not a new general observation [ALMM, K23].

## 9. Relationship to established work

### [SFZ] Finite-momentum pole equation

The 2026 published text of Sun, Feng and Zhang [SFZ], Eqs. (6),(8), gives the arbitrary-total-momentum contact T-matrix and its resonance subtraction. The v1 preprint numbers the same formulas (5),(7). Their scattering parameter denoted P is **not our total momentum P**.

At their resonance, set their total momentum k=P, energy E=u|P|^z e, and their kinetic coefficient u=J. Subtract their zero-energy, zero-momentum integral and send the dimensionless cutoff to infinity. Their result becomes

```math
T(E,P)^{-1}=\frac{|P|^{1-z}}{2J}F_z(e).
```

Thus (7) is an **exact specialization of their effective theory**. The factor 1/2 changes T normalization, while the pole equation is unchanged. Sections 3–6 establish the root between 0 and 1, its below-fixed-momentum-continuum interpretation, lattice convergence, differentiated velocity, and normalized contact weight.

### [ALMM] Motion-induced lattice binding

Their Theorem 5.4 assumes the smooth three-dimensional setting and guarantees nonempty below-band discrete spectrum for every nonzero total momentum when the rest fiber has a threshold eigenvalue or resonance. They explicitly explain that changing momentum, not adding attractive potential, can create binding. Section 3 supplies the explicit calculation for the fractional cusp outside those smooth hypotheses.

### [K23] Momentum-selective magnon binding

Kranzl et al. report broad low-momentum spectral weight, a sharp high-momentum bound feature, and finite group velocity for the bound branch they study. Their dominant state is a repulsively bound high-energy branch of a long-range anisotropic Heisenberg model, with long-range longitudinal coupling as well. Our attractive, resonance-tuned branch, exponent window, and short-range interaction differ. Their spectroscopy establishes finite velocity for the specified branch and provides context for the resonance contrast in this contact model.

### Other model ingredients

[DC23] treats two species with equal power-law hopping and onsite interaction, supplies a total-momentum scattering equation, and examines the disappearance of attractive rest dimers. [CRSTV] supplies the fractional lattice kinetic operator and exact kernel. These model ingredients remain attributed to the respective sources.

The spectral result is a controlled resonance-to-bound-pair dispersion contrast in the exact lattice model, with a fractional moving pole and vanishing local spectral weight. Its scattering framework and motion-induced binding mechanism remain attributed above. The [transport proof](TRANSPORT_PROOF.md) carries the normalized local overlaps into the observed probability law.


## Primary sources

[ALMM] S. Albeverio, S. N. Lakaev, K. A. Makarov and Z. I. Muminov, *The Threshold effects for the two-particle Hamiltonians on lattices*, arXiv:math-ph/0501013. Introduction, Hypotheses 3.1 and 5.1, and Theorem 5.4/proof. https://arxiv.org/pdf/math-ph/0501013

[SFZ] N. Sun, L. Feng and P. Zhang, *Efimov effect in long-range quantum spin chains*, Communications Physics 9,146 (2026); arXiv:2502.20759. Published two-magnon section and arbitrary-momentum T-matrix; preprint v1 provides the indicated alternative equation numbering. https://www.nature.com/articles/s42005-026-02580-0 ; https://arxiv.org/html/2502.20759v1

[K23] F. Kranzl et al., *Observation of magnon bound states in the long-range, anisotropic Heisenberg model*, Physical Review X 13,031017 (2023); arXiv:2212.03899. Section III and Appendices E–F: bound-branch sign, velocity behavior, and preparation. https://arxiv.org/pdf/2212.03899

[DC23] G. A. Dominguez-Castro, *Bose Polaron in a One-Dimensional Lattice with Power-Law Hopping*, Atoms 11,110 (2023). Two-body construction, Eqs. (8)–(10), and zero-momentum analysis. https://www.mdpi.com/2218-2004/11/8/110

[CRSTV] O. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea and J. L. Varona, *Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications*, arXiv:1608.08913v2. Theorem 1.1, kernel (1.7), and power-law bounds (1.8). Our z equals twice their fractional power s, with mesh h=1. https://arxiv.org/pdf/1608.08913

Primary sources are linked under their own publication and distribution terms.

---

[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)
