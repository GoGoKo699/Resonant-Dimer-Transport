# Finite-time relative accuracy for the coincidence tail

## 1. Scope and fixed-time event

Keep the infinite-lattice Hamiltonian, onsite source, and unconditional position
measurement in the [author account](AUTHOR_ACCOUNT.md). Fix $J>0$,
$1/2<z<1$, and $U>U_c$. Write $E(P)=E_d(P;U)$ and $Z(P)=Z(P;U)$.
All momentum norms below use $dP/(2\pi)$. Set

```math
\begin{aligned}
\delta&=J(U_c^{-1}-U^{-1}),\qquad a=\delta/J,\\
p_t(s)&=\sum_{|aj/t| > s}C_j(t),\\
q(s)&=\int\frac{dP}{2\pi}Z(P)^2\mathbf{1}_{\{|aE'(P)| > s\}}.
\end{aligned}
```

**(F1)**

For a fractional-cutoff event take $s=\theta a v_{\max}(U)$, $0<\theta<1$.
Then $q(s)>0$. No time averaging, momentum filtering, change of initial state,
or smoothing of the actual detector is used in the conclusions.

This note gives a nonasymptotic error bound and a sufficient observation time
in terms of **static spectral quantities**, whose finiteness is proved below.
The prescription requires valid bounds on those quantities. The
[joint observation-time theorem](OBSERVATION_TIME.md) controls their detuning
dependence.

## 2. Quantities entering the bound

Let $w_{P,U}(E)$ be the continuous part of the contact spectral density,
extended by zero outside the scattering band:

```math
w_{P,U}(E)=\frac{\rho_{0,P}(E)}{|1-U I_P(E+i0)|^2},\qquad
b_P(t)=\int_{\mathbb{R}}e^{-itE}w_{P,U}(E)\,dE.
```

Its mass is $1-Z(P)$, as established in the [transport proof](TRANSPORT_PROOF.md).
For an auxiliary momentum margin $0<r<\pi/2$, define

```math
\mathcal K_r=\{P:r\le |P|\le\pi-r\},\qquad
m_r=\int_{\mathcal K_r^c}\frac{dP}{2\pi}(1-Z(P))^2\le\frac{2r}{\pi},
```
```math
\begin{aligned}
L_r^2&=\int_{\mathcal K_r}\frac{dP}{2\pi}
\left[\mathrm{TV}_{\mathbb{R}}(w_{P,U})\right]^2,
\\
e_t(r)&=\sqrt{m_r+L_r^2/t^2}.
\end{aligned}
```

**(F2)**

Here total variation is with respect to **energy**, including the extension
by zero; it has inverse-energy units. The margin $r$ is solely a proof
parameter. Every momentum is still present in the physical state.

For an auxiliary scaled-velocity margin $0<h<s/2$, put

```math
W=\int\frac{dP}{2\pi}Z(P)^2,\quad
S(s,h)=\int\frac{dP}{2\pi}Z(P)^2
\mathbf{1}_{\{\,\big||aE'(P)|-s\big|\le 2h\,\}},
```
```math
\begin{aligned}
A(h)&=\frac{\sqrt W}{\pi}
\left[\frac{9a\|Z'\|_2}{h}
+\frac{27a^2\|E''Z\|_2}{2h^2}\right],
\\
d_t(s,h)&=S(s,h)+A(h)/t.
\end{aligned}
```

**(F3)**

The quantities $m_r,L_r,S,A$ have no oscillatory observation-time integral.
For this model, $L_r<\infty$, $E\in C^2$ on the momentum circle,
$Z\in C^1$, and $S(s,h)\to0$ as $h\downarrow0$ at every $s>0$.
Sections 5--6 prove the regularity statements rather than presuming them
from rank one or from an energy asymptotic.

## 3. Nonasymptotic theorem and sufficient time

For every $t>0$ and the admissible margins above,

```math
\boxed{|p_t(s)-q(s)|\le
 d_t(s,h)+2\sqrt{q(s)+d_t(s,h)}\,e_t(r)+e_t(r)^2.}
```

**(F4)**

This controls the sharp position event at a specified time. The bound is
valid whether or not its right side is small; it can be capped by one.

There is an explicit sufficient-time prescription. Fix a relative accuracy
$0<\varepsilon\le1$ and write $q=q(s)>0$. Choose

```math
0 < r\le\frac{\pi\varepsilon^2q}{288},\qquad
0 < h < s/2\ \text{such that}\ S(s,h)\le\frac{\varepsilon q}{6}.
```

**(F5)**

Such choices exist. Then

```math
\boxed{
T=\max\left\{\frac{6A(h)}{\varepsilon q},
             \frac{12L_r}{\varepsilon\sqrt q}\right\}
\quad\Longrightarrow\quad
\frac{|p_t(s)-q|}{q}\le\varepsilon\quad\text{for every }t\ge T.
}
```

**(F6)**

The assertion is for each fixed stronger attraction and fixed fractional
cutoff. To instantiate a numerical certificate, $q$, the shell mass, the
variation integral, and the band norms must be enclosed with rigorous bounds.
Uncertified quadrature estimates inserted in (F6) are not automatically a
certified observation time. Conservative upper and lower enclosures can be inserted directly in (F4);
the square-root term requires an upper bound on its argument. The algebraic
helper does not certify spectral inputs or turn numerical estimates into
rigorous enclosures.

**Accuracy accounting.** Under (F5)--(F6), $d_t\le\varepsilon q/3$ and
$e_t\le\sqrt{m_r}+L_r/t\le\varepsilon\sqrt q/6$. Therefore the right side
of (F4), divided by $q$, is at most

```math
\varepsilon\left[\frac13+\frac13\sqrt{1+\varepsilon/3}
+\frac{\varepsilon}{36}\right] < \varepsilon.
```

**(F7)**

## 4. Proof of the finite-time bound

### 4.1 Continuum decay with a momentum margin

For a compactly supported bounded-variation density, Stieltjes integration by
parts gives $|\int e^{-itE}w(E)dE|\le\mathrm{TV}(w)/t$.
Apply this for $P\in\mathcal K_r$. On the complement retain the exact mass
bound $|b_P(t)|\le1-Z(P)$. The Parseval error in the contact-amplitude vector
then obeys

```math
\eta_U(t)^2:=\int\frac{dP}{2\pi}|b_P(t)|^2
\le m_r+L_r^2/t^2.
```

**(F8)**

The bound does not assert a uniform variation norm at $P=0$ or $P=\pi$;
the excluded momentum measure is kept explicitly. Removing those regions
from the physical preparation would be a different operation.

### 4.2 Quantitative band-to-velocity approximation

Let

```math
A_j^d(t)=\int\frac{dP}{2\pi}Z(P)e^{iPj-itE(P)},\qquad
p_t^d(s)=\sum_{|aj/t| > s}|A_j^d(t)|^2.
```

In the momentum representation, position is $X=i\partial_P$ on its periodic
Sobolev domain. Its exact band Heisenberg evolution is
$e^{itE}Xe^{-itE}=X+tE'$. Thus the scaled-position characteristic function
in the pole contribution is the expectation of
$\exp[i\xi(aE'+aX/t)]$ in the vector $Z$. The limiting one is the expectation
of $\exp(i\xi aE')$ in the same vector. Duhamel on that vector gives

```math
|\widehat\mu_t^d(\xi)-\widehat\mu_\infty^d(\xi)|
\le\frac{\sqrt W}{t}
\left[a|\xi|\|Z'\|_2+\frac{a^2\xi^2}{2}\|E''Z\|_2\right].
```

**(F9)**

Indeed, $\|X e^{iu aE'}Z\|_2\le\|Z'\|_2+|u|a\|E''Z\|_2$;
unitarity controls the other factor in the Duhamel integral. The identity
can first be proved for smooth functions and then passed to the stated
regularity. It does not require bounded position or differentiation of a
little-o remainder.

To turn (F9) into a sharp-event bound, let $\kappa_h$ be the convolution of
three uniform probability densities on $[-h/3,h/3]$. It is nonnegative,
supported on $[-h,h]$, and has Fourier transform
$[\mathrm{sinc}(h\xi/3)]^3$, with $\mathrm{sinc}u=\sin u/u$.
For $R>0$ set $f_{R,h}=\mathbf{1}_{[-R,R]}*\kappa_h$. Then

```math
f_{s-h,h}\le\mathbf{1}_{[-s,s]}\le f_{s+h,h},
\quad
|\widehat f_{R,h}(\xi)|\le\frac2{|\xi|}
\min\{1,(3/(h|\xi|))^3\}.
```

The two elementary integral bounds are

```math
\int_{\mathbb{R}}\min\{1,(3/(h|\xi|))^3\}d\xi=9/h,
```
```math
\int_{\mathbb{R}}|\xi|\min\{1,(3/(h|\xi|))^3\}d\xi=27/h^2.
```

Fourier inversion and (F9) show that the two band measures differ by at most
$A(h)/t$ on either smoothed function. The limiting expectations of these
functions differ from the sharp-event mass only in the shell of (F3).
Both band measures have total mass $W$, so taking complements proves

```math
|p_t^d(s)-q(s)|\le d_t(s,h).
```

**(F10)**

The smoothed functions are upper and lower estimates, not a replacement of
the specified position detector. Equality at a lattice threshold is also
covered by the pointwise sandwich.

### 4.3 Event-local amplitude error

Let $\Pi_t$ select precisely the contact sites in (F1), and put
$R(t)=A(t)-A^d(t)$. The triangle inequality gives the stronger amplitude form

```math
\big|\sqrt{p_t(s)}-\sqrt{p_t^d(s)}\big|
\le\|\Pi_tR(t)\|_2\le\eta_U(t).
```

Consequently,

```math
|p_t(s)-p_t^d(s)|\le2\sqrt{p_t^d(s)}\eta_U(t)+\eta_U(t)^2.
```

Use $p_t^d\le q+d_t$, (F8), and (F10) to obtain (F4). In particular,
relative accuracy of a rare event requires continuum amplitude error small
relative to $\sqrt q$, **not** $q$. The whole-distribution estimate
$2\sqrt W\eta+\eta^2$ is still correct, but unnecessarily expensive for
this one event. This improvement is elementary projection geometry, not a
new dynamical mechanism.

## 5. Band regularity and explicit conservative norm bounds

Write the fiber in the uncentered variable $k$ as
$A(P,k)=\epsilon(k)+\epsilon(P-k)$. Subadditivity gives
$A(P,k)-\epsilon(P)\le2\epsilon(k)$. The min--max principle, with the
unchanged contact attraction, implies

```math
E(P)-\epsilon(P)\le E(0) < 0.
```

Hence $g=-E(0)>0$ is a **global lower bound** on the below-band gap. Also
$E(P)\ge-U$, and with $M=2^{z+1}J$ and $L=M+U$,

```math
g\le A(P,k)-E(P)\le L,\qquad I_E\ge L^{-2}.
```

**(F11)**

Let $u=\epsilon'$, $l_1=\|u\|_1$, $l_2=\|u\|_2^2$. The exponent window
ensures $u\in L^2$. In the normalization used here,

```math
l_1=2^zJ/\pi,\qquad
l_2=\frac{J^2z^2 2^{2z-2}}\pi
\mathrm{B}(z-1/2,3/2).
```

For $D=A(P,k)-E$ and $E$ strictly below the fiber threshold,

```math
I_P=-\int\frac{dk}{2\pi}\frac{u(P-k)}{D^2},\quad
I_{PE}=-2\int\frac{dk}{2\pi}\frac{u(P-k)}{D^3},\quad
I_{EE}=2\int\frac{dk}{2\pi}\frac1{D^3},
```
```math
\boxed{I_{PP}=2\int\frac{dk}{2\pi}\frac{u(k)u(P-k)}{D^3}.}
```

**(F12)**

For smooth dispersion, (F12) follows by integrating the second derivative
once by parts; the apparent $u(P-k)^2$ terms cancel. For the cusp dispersion,
mollify periodically, preserve a positive denominator gap, and pass to the
limit. Products of the translated first derivatives converge in $L^1$ by
$L^2$ translation continuity and Cauchy--Schwarz. Thus these are continuous
second partial derivatives even at $P=0$. No nonintegrable $\epsilon''$ is
inserted into the integral. Implicit differentiation gives $E\in C^2$ and

```math
E'=-I_P/I_E,\qquad
E''=-\frac{I_{PP}+2I_{PE}E'+I_{EE}(E')^2}{I_E}.
```

The derivative of $Z=(U^2 I_E(P,E(P)))^{-1}$ is continuous as well.
For a fully explicit, deliberately conservative upper envelope, set

```math
v_* = L^2l_1/g^2,\quad
M_2=\frac{2L^2}{g^3}(l_2+2l_1v_*+v_*^2),\quad
Z_1=\frac{2L^4}{U^2g^3}(l_1+v_*).
```

Then $\|Z'\|_2\le Z_1$, $\|E''Z\|_2\le M_2\sqrt W$, and these
bounds can replace the norms in (F3). They are not sharp detuning estimates.

For completeness, $E$ is real analytic on $0<P<\pi$: locally split the
relative-momentum integral into neighborhoods of the two separated cusps,
center each such neighborhood on its cusp, and use analytic parameter
dependence of the other dispersion factor and the positive resolvent gap.
On the remaining arcs there is no cusp. Fixed local integration radii give
uniform analytic extensions in the parameters; boundary pieces are regular.
The analytic implicit theorem applies because $I_E>0$.
The velocity is not constant on this interval: it is continuous with
$E'(0)=E'(\pi)=0$, whereas $E(P)>E(0)$ for $P\ne0$. The latter strict
inequality follows at $E(0)<0$ from the Laplace autocorrelation formula and
strict Cauchy--Schwarz for a nontrivial translate of $e^{-t\epsilon}$.
Every positive velocity level set therefore has zero measure. It is contained
away from the endpoints and is finite there by analyticity. This proves the
vanishing shell-mass assertion used in (F5), including a critical velocity
level with a multiple preimage.

## 6. Finite spectral variation away from coalescing momenta

The local Cauchy-transform and boundary-derivative calculations are given
explicitly in the [boundary resolvent appendix](BOUNDARY_RESOLVENT.md).

It remains to justify the variation norm in (F2). For
$r\le P\le\pi-r$, the relative dispersion has a cusp minimum at $P/2$
and nondegenerate smooth maxima at $0$ and $\pi$ on the half-circle.
Their energies are

```math
T=\epsilon(P),\qquad m=2\epsilon(P/2),\qquad
M_P=2\epsilon(\pi-P/2),\qquad T < m < M_P.
```

All three values remain separated on this compact momentum interval.
Away from them, the inverse branches and the free density are smooth, the
free density is positive inside the band, and hence the rank-one denominator
has nonzero imaginary part. Only the three exceptional energies require
estimates. Put $\beta=(1-z)/z\in(0,1)$.

At the cusp, each local branch is
$A-T=J|u|^z+O(u)$ with differentiated remainder. Inverting on either side gives
$\rho_0(T+y)=c_P y^\beta[1+O(y^\lambda)]$ for some $\lambda>0$, with
termwise first-derivative bounds, uniformly on compact momentum intervals.
For example, one can take $\lambda=\beta$ using the expansion in
$y^{(1-z)/z}$ of the inverse of $J|u|^z+O(u)$.
The Cauchy integral of this local density satisfies

```math
I_P(T+y+i0)=I_P(T)+O(y^\beta),\qquad
\partial_y I_P(T+y+i0)=O(y^{\beta-1}).
```

These estimates follow by subtracting the edge value, scaling the local
Cauchy integral by $u=yv$, and splitting at $u=2y$; the explicit leading
power integral and its derivative have orders $y^\beta$ and
$y^{\beta-1}$. Higher-power terms can carry logarithms at integer exponents,
which are lower order than these bounds. The real part is interpreted as a
principal value **inside the band**, as required for the spectral density;
this is not the invalid below-band endpoint substitution.
Since $I_P(T)>1/U_c\ge1/U$, the edge denominator stays nonzero uniformly on
the compact momentum interval. Consequently

```math
w(T+y)=O(y^\beta),\qquad w'(T+y)=O(y^{\beta-1}).
```

**(F13)**

At either smooth maximum the Morse expansion gives a free-density term
$c_P y^{-1/2}[1+O(y)]$ on its lower-energy side. Its Cauchy transform has a
nonzero inverse-square-root imaginary term on that side, and an
inverse-square-root real term on the upper-energy side. The remaining
branch at the interior maximum contributes a smooth density. Inserting these
expansions in the exact rank-one quotient gives

```math
\begin{array}{c|cc}
 & w & |w'|\\ \hline
E=m-y & O(y^{1/2}) & O(y^{-1/2})\\
E=m+y & O(y) & O(1)\\
E=M_P-y & O(y^{1/2}) & O(y^{-1/2})
\end{array}
```

**(F14)**

The square-root Cauchy expansion can equivalently be obtained by changing
to the Morse coordinate before integration. Its nonzero coefficient is
bounded away from zero on the compact momentum set. All denominators away
from these local neighborhoods are bounded away from zero by continuity and
positive free density. The bounds (F13)--(F14) are integrable for $w'$,
and $w$ extends continuously by zero through the exceptional values where
required. Thus the extended density is absolutely continuous with finite
variation. The bounds are uniform for $P\in\mathcal K_r$ at fixed $U$
(and for $U$ in a fixed compact subset of $[U_c,\infty)$). This proves
$L_r<\infty$ and completes the proof of (F4)--(F6).

## 7. Interpretation and verification

Equations (F2)--(F6) separate the static ingredients of the finite-time error
estimate. The bound holds for **every sufficiently late deterministic time**,
not just a selected subsequence or a time-averaged detector. The continuum
amplitude tolerance is correctly matched to the square root of the rare
probability. The source, detector, and unconditional normalization are unchanged.

The [joint observation-time theorem](OBSERVATION_TIME.md) removes the
auxiliary momentum margin through an integrable variation envelope and
controls band-norm detuning dependence. It supplies a sufficient polynomial
regime. Neither that estimate nor (F6) is a necessary or optimal law
$T=\Theta(\delta^{-\nu})$. At $z=3/4$, $q\asymp\delta^8$ makes a
continuum tolerance $o(\delta^4)$ sufficient once the band error is
$o(\delta^8)$; it does not determine the time needed to reach those errors.

The Aronszajn--Krein density formula is inherited; see Frymark and Liaw,
*Spectral Analysis, Model Theory and Applications of Finite-Rank Perturbations*,
arXiv:1904.09833. Integration by parts for bounded-variation Fourier transforms,
Duhamel comparison, and Fourier smoothing are established methods, derived
here in the required normalization. Cheng, Huang, and Zheng,
*Dispersive estimates for the Schrödinger equation with finite rank
perturbations*, arXiv:2209.08965, study the ordinary continuum Laplacian under
spectral assumptions; their stated setting does not supply a uniform estimate
for this moving fractional-lattice fiber. No decay exponent from that result
is imported here. The finite-momentum scattering attribution is
in [the detuning theorem](DETUNING_CROSSOVER.md).

Primary records: https://arxiv.org/abs/1904.09833 ;
https://arxiv.org/abs/2209.08965

`tools/check_finite_time.py` checks the event-local inequality, the Fourier
sandwich and constants, an independently specified smooth band, actual dimer
second-derivative identities, an exact continuous-density benchmark, and
actual dimer density samples on both sides of its interior critical energy.
The benchmark and smooth band test the analytical estimates; they are not a
simulation of the rare dimer event or a numerical certificate for $L_r$.
The sufficient-time arithmetic requires valid upper bounds as input and
cannot establish their validity by itself.

[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)
