# Local-source transport proof

## 1. Model, source, and detector

Two distinguishable particles on the infinite lattice have

```math
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad 1/2 < z < 1,
```

and onsite attraction $`-U\delta_{x_a,x_b}`$. Set $`U=U_c`$, with the exact value in [the spectral foundation](SPECTRAL_PROOF.md). Prepare

```math
|\Psi_0\rangle=|0,0\rangle.
```

At time $`t`$ measure both positions after unitary evolution from this onsite source. Define the **unconditional** same-site probability

```math
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
```

**(1)**

All trials, including those with unequal final positions, are part of the normalization. On a coincidence the center coordinate $`X=(x_a+x_b)/2`$ is exactly $`j`$. The detector resolves the lattice positions of both distinguishable particles.

The [spectral foundation](SPECTRAL_PROOF.md) proves a unique relative-coordinate bound state $`\psi_P`$ at each total momentum $`P\ne0`$, with

```math
E_d(P)\sim c_zJ|P|^z,\quad E'_d(P)\sim zc_zJ\,\mathrm{sgn}(P)|P|^{z-1},
\quad Z(P)=|\psi_P(0)|^2\sim B_z|P|^{2z-1},
```

**(2)**

where $`B_z=J^2/[U_c^2F'_z(c_z)]`$. These spectral facts are the inputs to the preparation and propagation derivations below.

## 2. A contact measurement separates the bound branch from the continuum

In a total-momentum fiber, let $`|1\rangle`$ be the normalized constant relative-momentum function, $`h_P=A_P-U|1\rangle\langle1|`$, and

```math
c_P(t)=\langle1|e^{-ith_P}|1\rangle.
```

The physical amplitude in (1) is the exact Fourier coefficient

```math
A_j(t)=\int_{-\pi}^{\pi}\frac{dP}{2\pi}e^{iPj}c_P(t).
```

**(3)**

The source spectral measure has one bound atom, of weight $`Z(P)`$, and an integrable continuum density:

```math
c_P(t)=Z(P)e^{-itE_d(P)}+b_P(t),\qquad b_P(t)\longrightarrow0 \quad(t\to\infty).
```

**(4)**

### Why the continuum claim holds here

With $`I_P(w)=\langle1|(A_P-w)^{-1}|1\rangle`$, the exact rank-one identity is

```math
\langle1|(h_P-w)^{-1}|1\rangle=\frac{I_P(w)}{1-U I_P(w)}.
```

**(5)**

This is the standard Aronszajn--Krein formula, with coupling $`\gamma=-U`$. Its pole weight and absolutely continuous density are the standard formulas recorded in [FL, Sec. 3.2, Proposition 3.5]:

```math
Z(P)=\frac1{U^2I'_P(E_d(P))},\qquad
w_P(E)=\frac{\rho_{0,P}(E)}{|1-U I_P(E+i0)|^2}.
```

**(6)**

For the explicit $`A_P`$, the pushforward of $`dq/(2\pi)`$ under $`A_P`$ has a positive density at every regular interior energy. For $`0<P<\pi`$, strict concavity of $`\epsilon`$ on $`(0,\pi)`$ shows that $`A_P(q)`$ strictly decreases on $`(0,P/2)`$ and strictly increases on $`(P/2,\pi)`$. Its only half-circle critical points are the lower cusp at $`P/2`$ and the smooth maxima at $`0`$ and $`\pi`$; the $`P=\pi`$ case merges their energy values without creating a flat interval. $`A_P`$ is analytic on the remaining arcs, so it has only finitely many exceptional energy values. Therefore (5) gives an absolutely continuous measure away from those exceptional energies. Its positive imaginary part excludes an embedded pole at a regular interior energy. At a smooth band extremum the free density diverges, rather than satisfying the pole condition; at the lower cusp edge, the spectral foundation gives $`I_P(E_{th})>1/U_c`$, also excluding a pole. A singular continuous measure cannot be supported on the remaining finite exceptional set. Above the band the attractive rank-one perturbation has no eigenvalue. The spectral foundation gives the unique eigenvalue below it. These facts establish the stated atom-plus-density decomposition for almost every $`P`$. The rest threshold at $`P=0`$ has no normalizable eigenvector and in any case is a zero-measure momentum fiber.

It would be incorrect to infer absence of singular continuous spectrum for an arbitrary rank-one perturbation solely from its rank. Here it follows from the explicit regularity and threshold properties. Since the continuum density has total mass $`1-Z(P)`$, Riemann--Lebesgue gives (4) and $`|b_P(t)|\le1-Z(P)\le1`$.

### The continuum vanishes in the entire coincidence distribution

Define the pole contribution

```math
A^d_j(t)=\int\frac{dP}{2\pi}e^{iPj-itE_d(P)}Z(P).
```

Dominated convergence and Parseval imply $`\sum_j|A_j-A^d_j|^2\to0`$. Consequently,

```math
\boxed{\sum_j\left|C_j(t)-|A^d_j(t)|^2\right|\longrightarrow0.}
```

**(7)**

Indeed, the sum is at most $`2\|A^d\|_2\|A-A^d\|_2+\|A-A^d\|_2^2`$. This removes the continuum and its interference in absolute probability, without preparing a projected state. The bound component alone is initially nonlocal; it is not asserted to be the actual preparation.

The limiting total coincidence probability and the conserved total bound-sector weight are different:

```math
\boxed{W_c=\lim_{t\to\infty}\sum_j C_j(t)=\int\frac{dP}{2\pi}Z(P)^2,\qquad
W_b=\int\frac{dP}{2\pi}Z(P).}
```

**(8)**

Both are positive, and $`0<W_c<W_b<1`$. At $`z=3/4`$, numerical quadrature gives $`W_c=0.5466750044\ldots`$, $`W_b=0.7067744300\ldots`$. The difference includes bound configurations whose constituents are on different sites. $`W_c`$ is not the dimer formation probability.

The result takes the infinite lattice before long time. A finite ring's scattering levels recur; extending its dynamics indefinitely does not establish (7).

## 3. Exact preparation-resolved ballistic velocity law

For any bounded continuous test function $`f`$,

```math
\boxed{\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int_{-\pi}^{\pi}\frac{dP}{2\pi}Z(P)^2 f(E'_d(P)).}
```

**(9)**

This is a finite positive measure of mass $`W_c`$. Dividing by $`W_c`$ gives the probability distribution conditional on a final coincidence, but none of the absolute probabilities reported here performs that division.

**Proof.** It suffices first to consider the pole contribution. Its characteristic function is

```math
\sum_j e^{i\xi j/t}|A^d_j(t)|^2
=\int\frac{dP}{2\pi}Z(P)Z(P+\xi/t)
 e^{it[E_d(P+\xi/t)-E_d(P)]}.
```

The phase tends to $`e^{i\xi E'_d(P)}`$ at almost every $`P`$. The translation of $`Z`$ converges in $`L^2`$ and $`Z`$ is bounded by one, giving dominated/translation convergence of the integral. The total mass is constant. The continuity theorem for characteristic functions gives weak convergence of the normalized pole measure. Equation (7) then gives (9) for the actual local preparation. No stationary-phase differentiation of an unspecified remainder is used; $`E'_d`$ is established separately in the spectral foundation.

In particular, at continuity points $`v>0`$,

```math
Q(v):=\lim_{t\to\infty}\Pr(x_a=x_b,\ |X| > vt)
=\int_{|E'_d(P)| > v}\frac{dP}{2\pi}Z(P)^2.
```

**(10)**

This is a directly defined position-counting event. No energy resolution or band projection is supplied to the detector.

## 4. The fast tail survives, with two powers of the local overlap

Because $`E'_d`$ diverges only near zero and $`Z(P)>0`$ at every nonzero momentum, $`Q(v)>0`$ at arbitrarily large finite $`v`$. The small-$`P`$ asymptotics (2) give

```math
\boxed{Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}\quad(v/J\to\infty).}
```

**(11)**

The measure integrates both propagation directions. One factor $`Z`$ is the local source's probability of exciting the bound state; a second factor $`Z`$ is its same-site detection probability. Replacing $`Z^2`$ by $`Z`$ would answer a different, spectrally projected question and give the wrong physical tail for (1).

No global monotonicity of $`E'_d`$ is needed for (11). On a compact momentum region away from zero the velocity is bounded. In the remaining interval, the ratio $`|E'_d(P)|/[zc_zJ|P|^{z-1}]`$ tends to one. Squeezing its superlevel set between the corresponding small intervals and integrating $`Z^2`$ proves (11).

At $`z=3/4`$,

```math
\boxed{Q(v)\sim1.9347109013\times10^{-4}(J/v)^8.}
```

**(12)**

Numerical evaluation of the limiting ray measure gives:

| $`v/J`$ | Near-zero cutoff $`P`$ | $`Q(v)`$, per initially prepared pair |
|---:|---:|---:|
| 1 | 0.0558640157 | 2.2546710613e-4 |
| 2 | 0.00326925834 | 7.8608836356e-7 |
| 3 | 0.000637751873 | 3.0007475914e-8 |

These are quadrature diagnostics, not interval certificates. The tabulation uses the numerically single crossing of $`E'_d=v`$, checked over the remaining Brillouin zone. The asymptotic theorem does not depend on assuming that numerical monotonicity as an analytical input.

**Order of limits:** $`t`$ tends to infinity at fixed $`v`$ first; then $`v/J`$ tends to infinity. The exponent belongs to this limiting velocity measure. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [joint observation-time theorem](OBSERVATION_TIME.md) control the sharp event at deterministic times under their stated conditions.

### No finite-weight superballistic coincidence front

Equation (9), together with convergence of the total coincidence mass, implies tightness of the conditional velocity distributions. Hence, for every $`L(t)/t`$ tending to infinity,

```math
\boxed{\sum_{|j| > L(t)}C_j(t)\longrightarrow0.}
```

**(13)**

Thus unbounded velocity support and a nonvanishing fraction moving faster than every linear scale are different statements. The present local source has the former, not the latter. Fixed nonextreme quantiles of its late-time coincidence distribution scale linearly with time. The limiting velocity measure has a finite second moment because the exponent in (11) exceeds two, but weak convergence alone does not justify convergence of the exact unbounded spatial second moment; no such step is used here.

## 5. Fixed stronger binding restores bounded velocity support

For every fixed $`U>U_c`$, the unique branch is below the continuum for all $`P`$. At $`P=0`$ it has $`E_0<0`$ and the spectral expansion $`E_d(P)=E_0+C(U)P^2+o(P^2)`$, with the separately justified derivative $`2C(U)P+o(P)`$. The branch remains separated from its continuum by a positive minimum gap on the compact momentum circle. Away from zero the differentiated resolvent is finite and continuous. Therefore

```math
v_{\max}(U):=\sup_P|E'_d(P)| < \infty.
```

The same local-source spectral argument yields

```math
\lim_{t\to\infty}\Pr(x_a=x_b,\ |X| > vt)=0\qquad(v > v_{\max}(U)).
```

**(14)**

At $`U=U_c`$, (10)--(11) instead have unbounded support. This is the measurable version of the resonance-to-finite-mass contrast, for the same particles, hopping, preparation and detector. Neither statement sets all finite-time long-range hopping tails to zero.

For $`U=0`$ there is no atom in the contact spectral measure. The same Riemann--Lebesgue argument gives $`\sum_j C_j(t)\to0`$. Fast independent particles therefore do not produce a persistent coincidence tail in this late-time observable. At finite times they can coincide, and their scattering component remains in the full wavefunction.

## 6. The fastest dimers are also spatially large

Normalize the bound relative wavefunction by

```math
\psi_P(q)=\frac{1}{\sqrt{I'_P(E_d(P))}[A_P(q)-E_d(P)]}.
```

Plancherel applied to its $`q`$ derivative gives its exact relative root-mean-square separation. Scaling $`q=Px`$ yields

```math
\boxed{\left(\sum_r r^2|\psi_P(r)|^2\right)^{1/2}
\sim \frac{L_z}{|P|},\qquad
L_z^2=\frac{\int_{\mathbb{R}} \frac{dx}{2\pi}
\frac{[b'_z(x)]^2}{[b_z(x)-c_z]^4}}{F'_z(c_z)}.}
```

**(15)**

Here $`b_z(x)=|x+1/2|^z+|x-1/2|^z`$; the lower-case function is distinct from the scalar residue coefficient $`B_z`$ in (2).

Near the two derivative cusps, the numerator behaves as $`|x\mp1/2|^{2z-2}`$, which is integrable for $`z>1/2`$; its tail is $`O(|x|^{-2z-2})`$. The lattice scaled numerator and denominator converge by the local/tail splitting in the spectral foundation. This independently controls the unbounded relative moment rather than inferring it from norm convergence. At $`z=3/4`$, $`L_z=2.6911243485\ldots`$.

For a fixed finite relative support $`|r|\le R`$, the exact best overlap of any normalized source vector supported there with $`\psi_P`$ is

```math
M_R(P)=\sum_{|r|\le R}|\psi_P(r)|^2.
```

Cauchy--Schwarz gives the upper bound and the normalized truncated bound vector attains it. The resolvent Fourier coefficients give

```math
\boxed{M_R(P)\sim S_R B_z|P|^{2z-1},\qquad
S_R=\sum_{|r|\le R}a_r^2,\quad a_r=U_c g_r(0,0).}
```

**(16)**

Thus even optimized finite-range relative preparation loses overlap with an ever-smaller-momentum dimer. A broad center-of-mass envelope alone does not eliminate this internal-state restriction. More formally, any normalized pair preparation confined to this relative support and total momentum $`[p,2p]`$ has bound-sector weight at most $`\sup_{P\in[p,2p]}M_R(P)\to0`$. This statement fixes $`R`$; no uniform claim for an arbitrarily growing preparation support is imported from (16).

Allowing a detector to count any fixed finite set of relative separations changes the limiting measure in (9) to

```math
\int\frac{dP}{2\pi}Z(P)M_R(P)f(E'_d(P)).
```

The same proof uses the finitely many mixed contact/relative spectral measures. Their continuous parts decay and the discrete coefficient is $`\sqrt Z\,\psi_P(r)`$. By (16), its large-$`v`$ tail has the **same exponent** as (11), multiplied by $`S_R`$. The effect is not an artefact of demanding exactly zero final separation. The explicit numerical table remains the same-site detector $`R=0`$.

## 7. Attribution and contribution boundaries

The contact scattering framework, local-pair measurement, and spectral identities have the following predecessors.

- **Sun, Feng and Zhang (2026):** the arbitrary-momentum contact T-matrix and its resonance subtraction supply the continuum pole equation. The propagation law here combines the normalized lattice contact residue with the specified source and detector through spectral/Fourier arguments. https://www.nature.com/articles/s42005-026-02580-0
- **Kranzl et al. (2023; arXiv v2):** Secs. III--IV explicitly prepare two neighboring magnons and measure one- and two-magnon position projectors to distinguish propagation. They also explicitly discuss accidental unbound-neighbor coincidences and finite-system participation corrections. Thus using nearby-pair detection to isolate bound transport is established. Their repulsive, hard-core, long-range longitudinal-interaction model and selected regime have finite bound-state velocity and differ from the attractive contact resonance here. Their data are not reanalyzed or contradicted. https://arxiv.org/pdf/2212.03899
- **Fukuhara et al. (2013):** local two-spin preparation and position correlations separate free and bound motion in the short-range Heisenberg chain. This is a direct predecessor for the local-pair observable. https://arxiv.org/pdf/1305.6598
- **Albeverio, Lakaev, Makarov and Muminov (2005):** Theorem 5.4 gives the general lattice motion-induced binding precedent under its stated smooth three-dimensional hypotheses. The nonzero-momentum mechanism is inherited. https://arxiv.org/pdf/math-ph/0501013
- **[FL] Frymark and Liaw, Spectral Analysis, Model Theory and Applications of Finite-Rank Perturbations (2019):** Sec. 3.2, Theorem 3.3 and Proposition 3.5 summarize the standard Aronszajn--Krein formula, point masses and continuous densities used in (5)--(6). These mathematical ingredients are not new. https://arxiv.org/pdf/1904.09833

The [author account](AUTHOR_ACCOUNT.md#relationship-to-established-work) compares the models and observables in detail.

---

[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)
