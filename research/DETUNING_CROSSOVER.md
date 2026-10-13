# Detuning crossover of the locally observed dimer velocity

## 1. Same model, and a dimensionless distance from resonance

Keep the Hamiltonian, local preparation, and unconditional same-site detector
of the [author account](AUTHOR_ACCOUNT.md). Fix $J>0$ and $1/2<z<1$ throughout.
Approach the rest-binding resonance from the stronger-attraction side and set

$$
\delta=J\left(\frac1{U_c}-\frac1U\right)>0,\qquad
\rho=\delta^{1/(1-z)},\qquad U=U_\delta\downarrow U_c. \tag{D1}
$$

Both $\delta$ and $\rho$ are dimensionless in lattice units. Define

$$
e_\rho(k)=\frac{E_d(\rho k;U_\delta)}{J\rho^z},\qquad
V_\rho(k)=e_\rho'(k)=\frac{\delta}{J}E_d'(\rho k;U_\delta),
\quad 0\le k\le\pi/\rho.
$$

The statements below concern the **limiting coincidence-velocity measure**.
The infinite lattice and long-time limit at each fixed $U_\delta$ precede
$\delta\downarrow0$. Both source/detector overlap factors are retained.
Simultaneous time and detuning limits are controlled in the separate
[observation-time theorem](OBSERVATION_TIME.md).

## 2. Crossover theorem

Put

$$
a_z(k,x)=|x+k/2|^z+|x-k/2|^z,
$$
$$
G_z(k,e)=\int_{\mathbb R}\frac{dx}{2\pi}
\left[\frac1{a_z(k,x)-e}-\frac1{2|x|^z}\right],\qquad e<k^z.
$$

At each $k\ge0$ there is a unique solution $e_z(k)<k^z$ of

$$
G_z(k,e_z(k))=-1. \tag{D2}
$$

Define its positive normalization integral and velocity by

$$
D_z(k)=\int_{\mathbb R}\frac{dx}{2\pi}
\frac1{[a_z(k,x)-e_z(k)]^2},\qquad V_z(k)=e_z'(k).
$$

Here $D_z(k)$ is a normalization function, not the Fourier coefficient called
$D_z$ in the [small-window calculation](THEOREM.md#small-scaled-windows).
On every finite $k$ interval,

$$
e_\rho\longrightarrow e_z\quad\hbox{in }C^1,
\qquad
\frac{U_\delta^2}{J^2}\rho^{1-2z}Z(\rho k;U_\delta)
\longrightarrow D_z(k)^{-1}\quad\hbox{uniformly}. \tag{D3}
$$

The continuous function $|V_z|$ tends to zero at both $k=0$ and $k=\infty$
and is not identically zero. Thus

$$
K_z:=\max_{k\ge0}|V_z(k)|\in(0,\infty)
$$

exists and is attained at positive finite momenta. Since $Z(P;U)>0$
on every bound fiber and the velocity is continuous, the spectral maximum
is also the endpoint of the support seen by the coincidence detector.
Crucially, the local convergence in (D3) controls the **global** lattice maximum:

$$
\boxed{v_{\max}(U)=\frac{J}{\delta}[K_z+o(1)]
=\frac{U U_c}{U-U_c}[K_z+o(1)].} \tag{D4}
$$

Every maximizing momentum satisfies

$$
\boxed{|P_{\max}(U)|=\Theta(\rho)
=\Theta(\delta^{1/(1-z)}).} \tag{D5}
$$

More precisely, the distance of $|P_{\max}|/\rho$ to
$\mathcal K_z=\operatorname{argmax}_{k\ge0}|V_z(k)|$ tends to zero. Neither
uniqueness of a maximizer nor monotonicity of the velocity is assumed.
The inverse power of $U-U_c$ in (D4) is one for every fixed exponent in the
declared window; the coefficient and momentum exponent do depend on $z$.
There is no uniform claim as $z$ approaches either endpoint of its window.

For the actual local-source measurement, define as before

$$
Q_U(v)=\lim_{t\to\infty}\Pr_U(x_a=x_b,\ |X|>vt),\qquad
\alpha_z=\frac{4z-1}{1-z}.
$$

For each fixed $s>0$, the corresponding probability crossover is

$$
\boxed{\delta^{-\alpha_z}Q_{U_\delta}(Js/\delta)
\longrightarrow\left(\frac J{U_c}\right)^4\mathcal H_z(s),}\tag{D6}
$$
$$
\mathcal H_z(s)=\frac1\pi\int_0^\infty
\frac{\mathbf1_{\{|V_z(k)|>s\}}}{D_z(k)^2}\,dk.
$$

This function is finite and continuous for $s>0$, positive for $0<s<K_z$,
and zero for $s\ge K_z$. Consequently, for any fixed $0<\theta<1$,

$$
Q_U(\theta v_{\max}(U))\sim
\left(\frac J{U_c}\right)^4\mathcal H_z(\theta K_z)
\delta^{\alpha_z}. \tag{D7}
$$

Approaching resonance therefore sends the speed cutoff to infinity while
making the absolute coincidence probability near any fixed fraction of that
cutoff vanish. This is an increasingly fast moving event, not the total
coincidence probability. The cutoff and its observable weight are parts of one result,
not competing descriptions of transport.

## 3. Continuum profile and its endpoint behavior

For $k>0$, change variables $x=ky$ in (D2):

$$
G_z(k,e)=k^{1-z}F_z(e/k^z),\qquad
F_z(e_z(k)/k^z)=-k^{z-1}. \tag{D8}
$$

The function $F_z$ is strictly increasing for $e<1$, with
$F_z(c_z)=0$ and $F_z(1)>0$. Its derivative is strictly positive. At large
negative energy the change of variable $x=|e|^{1/z}y$ gives
$F_z(e)\sim-A_z(-e)^{\beta_z}$, where

$$
\beta_z=\frac{1-z}{z}\in(0,1),\qquad
A_z=\frac{2^{-1/z}}{z\sin(\pi\beta_z)}>0.
$$

These properties prove unique solvability of (D8). At $k=0$ a beta integral
is exact:

$$
G_z(0,-a)=-A_z a^{\beta_z},\qquad
e_z(0)=-a_z^*,\quad a_z^*=A_z^{-1/\beta_z}. \tag{D9}
$$

For example, substitute $x=(a/2)^{1/z}t$ and then $u=t^z$. The remaining
integral is $\int_0^\infty u^{\beta_z-1}/(1+u)\,du
=\pi/\sin(\pi\beta_z)$. This also proves the small-detuning rest-energy law
$E_d(0;U_\delta)\sim-Ja_z^*\rho^z$ once (D3) is established.

The negative rest energy permits the autocorrelation proof from the spectral
foundation to be applied on the real line. For $h_t(x)=e^{-t|x|^z}$ one has
$h_t\in H^1(\mathbb R)$ because $2z-2>-1$. Apply the autocorrelation expansion
to the convergent difference $G_z(k,e)-G_z(0,e)$, not to either divergent
unsubtracted continuum integral. Integration with $e^{te}$ for $e<0$ is
justified by $\|h_t'\|_2^2=O(t^{1/z})$. Implicit differentiation then gives

$$
e_z(k)=-a_z^*+C_z^* k^2+o(k^2),\qquad
V_z(k)=2C_z^* k+o(k), \tag{D10}
$$
$$
C_z^*=
\frac{\displaystyle\int\frac{dx}{2\pi}
 \frac{z^2|x|^{2z-2}}{(2|x|^z+a_z^*)^3}}
 {\displaystyle\int\frac{dx}{2\pi}
 \frac1{(2|x|^z+a_z^*)^2}}>0.
$$

The differentiated autocorrelation, not differentiation of the little-o
term alone, proves the velocity expansion.

### Explicit rest residue and curvature

The quadratic endpoint in (D10) has a closed coefficient. Writing
$a=a_z^*$ and $\beta=\beta_z$, one has

$$
D_z(0)=\frac\beta a,\qquad
C_z^*=z\,2^{2/z-3}a^{1-2/z}>0. \tag{R1}
$$

The first identity follows by differentiating the exact rest loop
$G_z(0,-a)=-A_z a^\beta$ and using $A_z a^\beta=1$.
For the second, the denominator and numerator in (D10), respectively,
are

$$
\frac{2^{-1/z}a^{1/z-2}}{\pi z}
 \operatorname B(1/z,2-1/z),\qquad
\frac{z\,2^{1/z-2}a^{-1-1/z}}\pi
 \operatorname B(2-1/z,1+1/z).
$$

These follow from $u=2|x|^z/a$. The beta-function ratio in the quotient is
$1/(2z)$, which proves (R1). Both integrals converge because $z>1/2$.

Let $C(U)$ denote the exact lattice rest curvature, defined by
$E_d(P;U)=E_d(0;U)+C(U)P^2+o(P^2)$ in the
[spectral foundation, Section 5](SPECTRAL_PROOF.md#5-why-a-dimer-away-from-resonance-is-different).
Then the same microscopic branch obeys

$$
Z(0;U_\delta)\sim
 \left(\frac J{U_c}\right)^2\frac{a_z^*}{\beta_z}\rho^{2z-1},
\qquad
C(U_\delta)\sim J C_z^*\rho^{z-2}. \tag{R2}
$$

The residue limit is (D3) at $k=0$ together with (R1).
The curvature limit requires a separate argument; $C^1$ convergence in
(D3) alone would not imply it. Put
$g_\delta=-E_d(0;U_\delta)>0$. The exact cusp-safe rest identity is

$$
C(U_\delta)=
\frac{\displaystyle\int\frac{dq}{2\pi}
 [\epsilon_z'(q)]^2/[2\epsilon_z(q)+g_\delta]^3}
 {\displaystyle\int\frac{dq}{2\pi}
 1/[2\epsilon_z(q)+g_\delta]^2}.
$$

By (D3) and (D9), $g_\delta/(J\rho^z)\to a_z^*$.
Scale $q=\rho x$ in both integrals. The numerator divided by
$J^{-1}\rho^{-z-1}$ converges to the numerator in (D10), and the
denominator divided by $J^{-2}\rho^{1-2z}$ converges to $D_z(0)$.
To justify convergence on the expanding Brillouin zone, use the chord
bounds $\epsilon_z(q)\ge cJ|q|^z$ and
$|\epsilon_z'(q)|\le CJ|q|^{z-1}$ for $|q|\le\pi$.
For sufficiently small $\delta$, the respective scaled integrands,
extended by zero beyond $|x|\le\pi/\rho$, are bounded by fixed multiples of

$$
\frac{|x|^{2z-2}}{(1+|x|^z)^3},\qquad
\frac1{(1+|x|^z)^2}.
$$

The first has integrable powers $2z-2>-1$ at the origin and $-z-2$ at
infinity; the second is integrable at infinity because $2z>1$.
Pointwise convergence away from $x=0$ and dominated convergence prove
the two limits, hence (R2). No second derivative of the cusp dispersion
has been integrated, and no asymptotic remainder has been differentiated.

In lattice units, the corresponding rest effective mass is

$$
m_d(U_\delta):=\frac1{E_d''(0;U_\delta)}
 \sim\frac{\rho^{2-z}}{2J C_z^*}
 =\frac{\delta^{(2-z)/(1-z)}}{2J C_z^*}. \tag{R3}
$$

The finite quadratic curvature at each fixed stronger attraction therefore
diverges on approaching resonance. Its rest velocity still vanishes.
This is a local band-curvature statement; the global cutoff and its
coincidence weight remain the separate conclusions (D4) and (D6).

At the other endpoint, (D8) yields $e_z(k)/k^z\to c_z$. With
$y=e_z(k)/k^z$, exact implicit differentiation gives

$$
V_z(k)=k^{z-1}\left[zy-(1-z)\frac{F_z(y)}{F_z'(y)}\right],\qquad
D_z(k)=k^{1-2z}F_z'(y). \tag{D11}
$$

Thus $V_z(k)\sim zc_z k^{z-1}$ and
$D_z(k)\sim F_z'(c_z)k^{1-2z}$ as $k\to\infty$.
This proves the asserted endpoints, positivity of $K_z$, and compactness of
$\mathcal K_z$. On $k>0$, $F_z$ and its inverse are real analytic below the
threshold, so $V_z$ is real analytic and nonconstant. In particular every
positive level set $\{|V_z|=s\}$ is finite on the compact region where it
can occur. It has Lebesgue measure zero, even at $s=K_z$.

## 4. Uniform lattice scaling, including the derivative

Use the exact scaled lattice integral

$$
G_{\rho,z}(k,e)=\frac{J}{\rho^{1-z}}
 [I_{\rho k}(J\rho^z e)-I_0(0)].
$$

The pole equation is exactly $G_{\rho,z}(k,e_\rho(k))=-1$. For bounded $k$
and bounded $e$ separated by a positive distance from $k^z$, this function,
its $e$ derivative, and its $k$ derivative converge uniformly to those of
$G_z$. Here is the necessary local/tail argument.

On $|q|\le M\rho$, put $q=\rho x$. The scaled chord dispersions converge
to $|x\pm k/2|^z$. A positive spectral gap bounds their resolvent denominators
away from zero. The rest subtraction is dominated by $|x|^{-z}$ at the
origin. For the $k$ derivative, the moving cusp factors have order
$|x\pm k/2|^{z-1}$; their integrals over intervals of length $\ell$ are
uniformly $O(\ell^z)$. Exclude such small intervals, use uniform smooth
convergence on the remainder, and then send $\ell\to0$. This proves uniform
local derivative convergence rather than assuming a pointwise majorant
independent of the moving singularities.

For $M\rho\le|q|\le q_0$, with $M$ larger than twice the bounded $k$ range,
the symmetric shift and energy bounds give

$$
\left|\frac1{A_{\rho k}(q)-J\rho^z e}-\frac1{2\epsilon_z(q)}\right|
\le \frac CJ\left(\rho^z|q|^{-2z}+\rho^2|q|^{-z-2}\right).
$$

After scaling and integration the bound is
$C(M^{1-2z}+M^{-1-z})$. For $\partial_eG_{\rho,z}$ the tail bound is
$CM^{1-2z}$. For $\partial_kG_{\rho,z}$ use
$|\partial_PA_P(q)|\le CJ|P||q|^{z-2}$, yielding $CM^{-1-z}$.
All bounds vanish as $M\to\infty$. The fixed outer region $|q|\ge q_0$
contributes $O(\rho^{2z-1}+\rho^{1+z})$ to the function, $O(\rho^{2z-1})$
to its $e$ derivative, and $O(\rho^{1+z})$ to its $k$ derivative. Periodicity
handles the Brillouin-zone boundary without an additional cusp.

The continuum pole curve on any compact $k$ interval has a positive minimum
gap $k^z-e_z(k)$. Bracket it by two small fixed energy offsets, apply the
uniform convergence just proved, and use $\partial_eG_z>0$, bounded below
on that compact tube. This proves uniform root convergence. The exact identity
$e_\rho'=-\partial_kG_{\rho,z}/\partial_eG_{\rho,z}$ proves the $C^1$ part
of (D3). Finally,

$$
\partial_eG_{\rho,z}(k,e_\rho(k))
=J^2\rho^{2z-1}I'_{\rho k}(E_d),
$$

combined with $Z=(U_\delta^2 I')^{-1}$ proves the residue statement.
This analysis always stays strictly below the exact lattice threshold; it
does not reintroduce the endpoint substitution corrected in
[the endpoint lemma](THRESHOLD_ENDPOINT.md).

## 5. Why another momentum scale cannot dominate the cutoff

Compact convergence alone cannot establish (D4). Two additional estimates
exclude maximizers escaping to either endpoint of the scaled momentum axis.
All constants in this section may depend on the fixed $z$ but not on small
$\rho$.

### Very small momentum

Choose $k_0>0$ sufficiently small. By (D3) and (D9), for $0\le k\le k_0$,
the lattice root obeys $-CJ\rho^z\le E_d\le-cJ\rho^z<0$. For such energies,
put $h_t(q)=e^{-t\epsilon_z(q)}$ on the momentum circle. The derivative of
its autocorrelation satisfies

$$
|\partial_P\langle h_t(\cdot+P/2),h_t(\cdot-P/2)\rangle|
\le |P|\|h_t'\|_2^2.
$$

For example, the Fourier series bound is $|\sin(nP)|\le |nP|$.
The Laplace representation of the resolvent consequently gives

$$
|\partial_P I_P(E)|\le
2|P|\int\frac{dq}{2\pi}\frac{[\epsilon_z'(q)]^2}{[2\epsilon_z(q)-E]^3}
\le\frac C J |P|\rho^{-z-1}.
$$

The last integral is finite because $2z-2>-1$ and follows by scaling $q=\rho x$.
On $|q|\le\rho$ the energy and shift bounds give
$I'_P(E_d)\ge cJ^{-2}\rho^{1-2z}$. Therefore

$$
|V_\rho(k)|=\frac\delta J|E_d'(\rho k)|\le Ck
\quad(0\le k\le k_0). \tag{D12}
$$

### Large scaled momentum

For $k\ge1$ and $P=\rho k\le p_0$, divide the exact pole equation by
$P^{1-z}/J$. Its right side is $-\delta/P^{1-z}=-k^{z-1}\in[-1,0]$.
Choose fixed $e_-<e_+<1$ such that $F_z(e_-)<-2$ and $F_z(e_+)>0$.
Uniform fixed-energy-ratio lattice convergence, with sufficiently small fixed
$p_0$, traps every such root in

$$
e_-\le E_d(P;U_\delta)/(JP^z)\le e_+.
$$

This gives a denominator gap of order $JP^z$. The region $|q|\le2P$ yields
$I'_P\ge cJ^{-2}P^{1-2z}$. Split the absolute derivative numerator at $2P$
and $q_0$. Near the two cusps, integrate their powers $|q\pm P/2|^{z-1}$;
outside, use $|\partial_PA_P|\le CJP|q|^{z-2}$. The result is

$$
\int\frac{dq}{2\pi}\frac{|\partial_PA_P(q)|}{[A_P(q)-E_d]^2}
\le C J^{-1}P^{-z},\qquad
|V_\rho(k)|\le C k^{z-1}. \tag{D13}
$$

On the remaining compact physical momenta $p_0\le P\le\pi$, the resonant
branch already has a positive minimum gap. Increasing $U$ lowers its energy;
for $U$ in a bounded neighborhood of $U_c$ the denominator normalization is
also uniformly bounded below. Integrability of $\epsilon_z'$ therefore gives
$|E_d'(P;U)|\le CJ$ and $|V_\rho|\le C\delta$ there. Combining the regions,

$$
\limsup_{\rho\downarrow0}\sup_{k\ge R}|V_\rho(k)|
\le C R^{z-1}\longrightarrow0\quad(R\to\infty). \tag{D14}
$$

Equations (D12) and (D14), together with $K_z>0$, trap all maximizers in a
fixed compact interval inside $(0,\infty)$. Uniform convergence on that interval
proves (D4), (D5), and convergence to the complete maximizing set. No sampled
velocity plot is used as a global maximization proof.

## 6. Probability crossover and recovery of the resonant tail

The already proved local-quench theorem gives

$$
Q_{U_\delta}(Js/\delta)
=\frac\rho\pi\int_0^{\pi/\rho}
Z(\rho k;U_\delta)^2\mathbf1_{\{|V_\rho(k)|>s\}}\,dk.
$$

For fixed $s>0$, (D12)–(D14) confine the superlevel region to a fixed compact
interval away from zero for all sufficiently small $\rho$. Apply the uniform
residue limit (D3), the velocity limit, and the zero-measure level-set fact
following (D11). Since $\rho^{4z-1}=\delta^{\alpha_z}$, dominated convergence
proves (D6), including at $s=K_z$. It also proves continuity of
$\mathcal H_z$ on $(0,\infty)$. Positivity below $K_z$ follows from an open
interval around a point where $|V_z|>s$. The moving-threshold limit in (D7)
follows by squeezing $\theta\delta v_{\max}/J$ between nearby fixed thresholds.

At small positive $s$, use the large-$k$ asymptotics (D11) to squeeze the
superlevel set and integrate $D_z(k)^{-2}\sim k^{4z-2}/F_z'(c_z)^2$. This gives

$$
\mathcal H_z(s)\sim
\frac1{\pi(4z-1)F_z'(c_z)^2}
\left(\frac{zc_z}{s}\right)^{\alpha_z}\quad(s\downarrow0). \tag{D15}
$$

After multiplying by $(J/U_c)^4$, this is exactly the coefficient of the
resonant coincidence tail. The comparison is first
$\delta\downarrow0$ at fixed $s$, then $s\downarrow0$; it is not a uniform
interchange with either finite time or arbitrary simultaneous limits.

## 7. Interpretation, computation, and attribution

For $z=3/4$, numerical evaluation of the continuum profile gives
$K_z\simeq0.1051707$, with a located maximum near $k=28.5002$. These are
quadrature/optimization diagnostics, not interval-certified constants or a
proof that the maximizing set is a singleton. Thus the leading cutoff is
$v_{\max}\simeq0.1051707J/\delta$. The peak momentum scale is $\delta^4$,
and the coincidence probability at any fixed fractional cutoff is of order
$\delta^8$. The shrinking weight prevents an interpretation as a finite-weight
superballistic front. Better tuning raises the available speed, not the
probability of efficiently launching a compact molecule at that speed.

The existing finite-momentum contact scattering framework already predicts
the continuum equation (D2) and its homogeneity. In particular Sun, Feng,
and Zhang give both the arbitrary-momentum $T$-matrix and the detuned rest
pole: *Efimov effect in long-range quantum spin chains*, Communications
Physics **9**, 146 (2026), published Eqs. (6)–(8); the readable v1 preprint
uses Eqs. (5)–(7). The factor of two in their $T$-matrix convention does not
change its zeros. The beta coefficient in (D9), the momentum scale, and the
inverse-detuning dimensional prediction are not separate inventions here.

The additional analytical content is uniform microscopic derivative control,
exclusion of competing momentum scales in the global maximum, and the
unconditional source/detector-weighted probability crossover. It quantifies
the tuning dependence of the same resonance contrast within the contact
scattering framework.

Primary source: https://www.nature.com/articles/s42005-026-02580-0

Readable preprint: https://arxiv.org/html/2502.20759v1

`tools/detuning.py` uses the scalar pole and resolvent
implementations. `tools/check_detuning.py` checks continuum derivatives against
an additional quadrature, rest scaling, lattice profile/residue convergence,
maximization diagnostics, and a source-weighted fast-velocity interval. The
proofs, not finite grids or a fitted exponent, establish (D3)–(D7).

`tools/check_rest_crossover.py` independently integrates the rest
normalization and curvature numerator, checks the lattice residue/curvature
limits at three fixed exponents, and compares the rest curvature with a
separate small-momentum velocity calculation. The [reproduction guide](../REPRODUCIBILITY.md#rest-residue-and-curvature-checks)
records its finite-quadrature scope; (R2) rests on the separate lattice
dominated-convergence proof above.

[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)
