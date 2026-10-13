# A sufficient joint time–detuning regime

## 1. Statement for the unchanged position measurement

Fix $1/2<z<1$, $J>0$, and a fraction $0<\theta<1$. The Hamiltonian,
onsite pair source, and unconditional same-site position detector are those
in [the author account](AUTHOR_ACCOUNT.md). Set

```math
\delta=J(U_c^{-1}-U^{-1}),\qquad \rho=\delta^{1/(1-z)},\qquad U=U_\delta > U_c,
```
```math
p_{\delta,t}=\sum_{|j| > \theta v_{\max}(U_\delta)t} C_j(t),\qquad
q_\delta=Q_{U_\delta}(\theta v_{\max}(U_\delta)).
```

The [detuning theorem](DETUNING_CROSSOVER.md) establishes
$q_\delta\sim C_{z,\theta}\delta^{\alpha_z}$, with
$C_{z,\theta}>0$ and $\alpha_z=(4z-1)/(1-z)$. The time-dependent
quantity here includes the full scattering state and its interference with
the bound branch. There is no time averaging or filtering of the source.

Define

```math
\nu_z=\begin{cases}
(3z-\tfrac12)/(1-z),&\tfrac12 < z < \tfrac34,\\
7,&z=\tfrac34,\\
(5z-2)/(1-z),&\tfrac34 < z < 1,
\end{cases}
\qquad
\ell_z(\delta)=\begin{cases}\sqrt{\log(2/\delta)},&z=\tfrac34,\\1,&z\ne\tfrac34.
\end{cases}
```

**(O1)**

**Sufficient-time theorem.** For every $0<\varepsilon\le1$ there are
$\delta_0>0$ and $C<\infty$, depending on $z,\theta,\varepsilon$ but
not on $J,\delta,t$, such that

```math
\boxed{0 < \delta < \delta_0,\quad
Jt\ge C\delta^{-\nu_z}\ell_z(\delta)
\quad\Longrightarrow\quad
|p_{\delta,t}-q_\delta|\le\varepsilon q_\delta.}
```

**(O2)**

Equivalently, along any joint limit with $\delta\downarrow0$ and
$Jt\delta^{\nu_z}/\ell_z(\delta)\to\infty$,

```math
\boxed{p_{\delta,t}=C_{z,\theta}\delta^{\alpha_z}[1+o(1)].}
```

**(O3)**

For $z=3/4$, a sufficient regime is
$Jt\gg\delta^{-7}\sqrt{\log(2/\delta)}$, while the event probability is
of order $\delta^8$. The bound is sufficient for the relative accuracy in
(O2). The change of exponent and logarithm in (O1) arise from the band norms
in this proof.

## 2. Uniform continuum estimate

The [boundary resolvent appendix](BOUNDARY_RESOLVENT.md) supplies the
signed cusp power integral, full analytic Morse coefficient, and regular
principal-value derivative formulas used below.

Let $w_{P,U}(\omega)$ be the continuous contact density extended by zero,
as in [the finite-time certificate](FINITE_TIME_CERTIFICATE.md). If
$U_c\le U\le U_1$, with a fixed dimensionless ratio $U_1/J<\infty$, then
there is $C_0<\infty$, depending only on $z,U_1/J$, such that

```math
\mathrm{TV}_{\omega}(w_{P,U})
\le\frac{C_0}{J}(1+|P|^{z-1})\quad(0 < |P|\le\pi).
```

**(O4)**

In particular,

```math
\mathcal L_U^2:=\int\frac{dP}{2\pi}
 [\mathrm{TV}_{\omega}(w_{P,U})]^2
\le\frac{C_0^2}{J^2}
\left[1+\frac{2\pi^{z-1}}z+\frac{\pi^{2z-2}}{2z-1}\right].
```

**(O5)**

Thus the full contact-continuum remainder satisfies

```math
\boxed{\eta_U(t)\le\mathcal L_U/t\le C_1/(Jt).}
```

**(O6)**

The uniformity is in $U\in[U_c,U_1]$. It is **not** a uniform bound on
each fiber's variation. The right side of (O4) diverges at $P=0$; its square
is integrable precisely because $z>1/2$. At $P=0,U=U_c$ the density need
not be of bounded variation, but this single fiber has zero momentum measure.
No momentum margin or excluded probability remains in (O6).

### 2.1 Quotient calculus

It suffices to set $J=1$ in the proof. Write $u_c=U_c/J$ and use the same
letters for dimensionless energies and couplings. The exact rank-one formula is

```math
w(\omega)=\frac{1}{\pi U^2}
\frac{\mathrm{Im}I_P(\omega+i0)}
{[\mathrm{Re}I_P(\omega+i0)-1/U]^2+
 [\mathrm{Im}I_P(\omega+i0)]^2}.
```

For $v>0$ put $\Phi(u,v)=v/(u^2+v^2)$. The following elementary estimates
will be used without trying to bound the real part away from zero:

```math
|\partial_u\Phi|\le C v^{-2},\quad
|\partial_v\Phi|\le v^{-2},\quad
|\partial_u\Phi(u,v)|\le C(1+u^2)^{-3/2}
\quad(c\le v\le C').
```

**(O7)**

The last bound is integrable over $u\in\mathbb{R}$. Consequently a monotone
real-part passage through zero with imaginary part bounded above and below
has uniformly bounded quotient variation, independently of its steepness or
of an additive constant in its real part. Similarly, if $v$ is monotone and
$v\ge c$, its contribution is bounded by $\int_c^\infty v^{-2}dv$.

### 2.2 Small momentum and energies of order $P^z$

Take $P>0$ small. On the half-circle the three critical energies are

```math
T_P=\epsilon(P),\quad m_P=2\epsilon(P/2),\quad M_P=2\epsilon(\pi-P/2).
```

The first is a cusp minimum, the second a smooth local maximum, and the third
the global maximum. Their exact values, not the leading continuum
approximations, are used at endpoints. For scaled energy $e=\omega/P^z$ set

```math
F_P(e)=P^{z-1}[I_P(P^z e+i0)-I_0(0)],\qquad
\lambda=\delta/P^{1-z}\ge0.
```

Then

```math
w(P^z e)=\frac{P^{z-1}}{\pi U^2}
\Phi(\lambda+\mathrm{Re}F_P(e),\mathrm{Im}F_P(e)).
```

**(O8)**

On any fixed scaled-energy interval containing the two lower critical values,
the quotient in (O8) has variation bounded uniformly in small $P$ and **all**
$\lambda\ge0$. Here are the estimates at the only singular locations.

At $e=t_P:=T_P/P^z$, put $y=e-t_P$ and $\beta=(1-z)/z\in(0,1)$.
The inverse cusp branches give $v=\mathrm{Im}F_P=O(y^\beta)$ and
$|v'|+|u'|\le C y^{\beta-1}$. The exact-threshold lemma gives
$\mathrm{Re}F_P(t_P)\to F_z(1)>0$. Shrink a fixed neighborhood so that
$\lambda+u\ge c+\lambda$. The derivative of (O8)'s quotient is then bounded
by $C y^{\beta-1}$, uniformly in $\lambda$. The value tends to zero at
this lower endpoint.

At $e=\mu_P:=m_P/P^z$, the scaled dispersion has a uniformly
nondegenerate maximum. A local Morse coordinate and the two on-shell outer
roots give the following normal forms, with coefficients bounded above and
away from zero independently of small $P$:

```math
\begin{array}{c|cc}
 & u=\mathrm{Re}F_P & v=\mathrm{Im}F_P\\ \hline
e=\mu_P-y & O(1),\quad u'=O(1)
 & c_Py^{-1/2}+O(1),\quad \partial_yv=-\tfrac12c_Py^{-3/2}+O(y^{-1/2})\\
e=\mu_P+y & -c_Py^{-1/2}+O(1),\quad
 \partial_yu=\tfrac12c_Py^{-3/2}+O(y^{-1/2})
 & d_P+O(y),\quad v'=O(1).
\end{array}
```

**(O9)**

On the lower side, $v$ is monotone for a sufficiently small fixed
neighborhood, so (O7) controls its unbounded range and the bounded derivative
of $u$. On the upper side, $u$ is monotone and $c\le v\le C$; the integrable
bound in $u+\lambda$ controls the real-part passage even for arbitrarily
large $\lambda$. The bounded $v'$ controls the other term. Both quotient
limits are zero at the critical energy. Away from these neighborhoods the
imaginary part is bounded below, and both derivatives are bounded; (O7)
again applies uniformly in $\lambda$.

For clarity, the uniform normal forms are obtained by scaling $q=Px$ before
choosing fixed neighborhoods of $x=0,\pm1/2$ and of the simple outer roots.
The inner maximum has curvature tending to
$-2z(1-z)2^{2-z}\ne0$; its inverse branch has a convergent square-root
expansion. The Cauchy transform of that branch has a purely imaginary leading
inverse square root below the maximum and a negative real one above it.
The remaining on-shell branch is smooth and has nonzero density at the
maximum. Subtracting its value in the principal-value integral makes the
regular pieces and their derivatives bounded. The subtracted high-momentum
tail is uniformly bounded with its first energy derivative, since $2z>1$.
At the minimum, inverting $|x-1/2|^z+O(|x-1/2|)$ instead gives the power
$\beta$ and the derivative stated above. This supplies the uniform estimates
used in (O9), rather than deducing them from compactness of a degenerating
unscaled fiber.

Variation is invariant under an increasing change of the energy variable.
It follows from (O8) that the entire region $T_P\le\omega\le R P^z$,
for sufficiently large fixed $R$, contributes at most $C P^{z-1}$.

### 2.3 Intermediate and fixed nonzero energies

Choose $R$ large and a fixed small $\omega_0>0$. In
$R P^z\le\omega\le\omega_0$ the local maximum and cusp energies lie well
below the on-shell energy. Rescale $q=\omega^{1/z}x$; now
$k=P/\omega^{1/z}\le R^{-1/z}$. The on-shell roots are simple and stay
away from the two cusps, uniformly in this range. The free density and
subtracted boundary loop obey

```math
c\omega^\beta\le\mathrm{Im}I_P(\omega+i0)\le C\omega^\beta,
\quad |\mathrm{Re}I_P(\omega+i0)-I_0(0)|\le C\omega^\beta,
\quad |\partial_\omega I_P(\omega+i0)|\le C\omega^{\beta-1}.
```

**(O10)**

One direct justification is to split the scaled integral into small fixed
neighborhoods of its simple roots and the complement. On each root
neighborhood change to the dispersion value, subtract the value and first
Taylor polynomial of the inverse-branch density, and differentiate the
resulting regular principal-value formula. All coefficients are bounded
because the roots and their slopes remain separated from zero. The cusps
are off shell and have a denominator bounded away from zero in these units.
The large-$x$ subtracted integral has tail $O(|x|^{-2z})$, and its energy
derivative has the same integrable tail. The outer fixed lattice region adds
$O(\omega+P^2)$ to the loop difference and $O(1)$ to its derivative, both
within (O10). Taking $R$ large and $\omega_0$ small gives the lower bound on
the density from its nonzero rest continuum limit. This argument applies to
the boundary values; it does not replace a principal value by an ordinary
integral across an on-shell pole.

Since $I_0(0)-1/U=\delta$, (O10) implies

```math
|I_P(\omega+i0)-1/U|\ge c(\delta+\omega^\beta),\qquad
|w'(\omega)|\le
\frac{C\omega^{\beta-1}}{(\delta+\omega^\beta)^2}.
```

**(O11)**

For the first inequality, if $\delta$ is larger than twice the upper bound
on the real correction, use the real part; otherwise use the lower bound
on the imaginary part. Integrating the second inequality yields at most
$C/(\delta+P^{1-z})\le C P^{z-1}$.

For $\omega\ge\omega_0$ and small $P$, only the global smooth maximum
remains as a critical energy. Its curvature is uniformly nonzero. The usual
Morse coordinate now has bounded unscaled coefficients, while the free
density is bounded below off its neighborhood. The same quotient calculation
therefore gives a bounded variation contribution uniformly in $U\in[u_c,U_1]$.
Joining the energy pieces, including their boundary values, proves (O4)
near zero momentum.

### 2.4 Coalescing upper maxima near $P=\pi$

Only the coalescence $m_P\uparrow M_P$ still needs a uniform estimate.
The two curvatures remain bounded above and below by nonzero constants,
and the cusp threshold stays a fixed distance below them. Let
$d=M_P-m_P\downarrow0$. Choose disjoint neighborhoods of the two maxima,
with a fixed symmetric radius in their Morse coordinates. In each one,
$A_P(q)=M_\sigma-t^2$, where $M_-=m_P$ and $M_+=M_P$.
The even part of the coordinate Jacobian is analytic in $t^2$, uniformly
in $P$ near $\pi$. Dividing that analytic function by $t^2+\zeta$ before
integrating gives the exact local decomposition

```math
I_P(\omega+i0)=R_P(\omega)
-\sum_{\sigma\in\{-,+\}}
\frac{H_{P,\sigma}(\omega-M_\sigma)}
     {\sqrt{\omega-M_\sigma+i0}}.
```

Here the square root has its cut on the negative real axis and is positive
above the maximum. The functions $H_{P,\sigma}$ are real analytic, satisfy
$c\le H_{P,\sigma}\le C$, and have uniformly bounded first derivatives on
one fixed interval around zero. The remaining function $R_P$ is real with
uniformly bounded value and first derivative in this energy neighborhood.
Indeed the finite Morse-coordinate endpoint terms are analytic after the
displayed singularity is subtracted, and the rest of the momentum circle
has energy a fixed distance below both maxima. This decomposition retains
the full analytic coefficient: subtracting only its constant term would
leave square-root remainders whose derivatives are unbounded.

Between the maxima, write
$\omega=m_P+dy$, $0<y<1$. The leading boundary loop has real and
imaginary parts

```math
-c_-/\sqrt{dy},\qquad c_+/\sqrt{d(1-y)},
```

respectively, with positive bounded coefficients. To control the full
quotient, set $s=\omega-m_P$, $r=M_P-\omega=d-s$ and

```math
u=R_P(\omega)-1/U-H_{P,-}(s)/\sqrt s,\qquad
v=H_{P,+}(-r)/\sqrt r.
```

For sufficiently small $d$, uniformly in $U\in[u_c,U_1]$,

```math
|u|\asymp s^{-1/2},\quad v\asymp r^{-1/2},\quad
|u'|\le Cs^{-3/2},\quad |v'|\le Cr^{-3/2},\quad
u^2+v^2\ge c\left(s^{-1}+r^{-1}\right)=\frac{cd}{sr}.
```

The bounded real remainder cannot cancel the first singular term here.
Direct quotient differentiation now gives

```math
\left|\frac{d}{d\omega}\frac{v}{u^2+v^2}\right|
\le C\left[\frac{r^{3/2}}{d^2}+\frac{s}{d\sqrt r}\right],\qquad
\int_0^d\left[\frac{(d-s)^{3/2}}{d^2}
                 +\frac{s}{d\sqrt{d-s}}\right]ds
=\frac{26}{15}\sqrt d.
```

Thus the full gap contributes $O(\sqrt d)$ variation; its endpoint values
are zero. This also recovers the bounded-variation leading profile.
For example its leading profile is proportional to

```math
\frac{y\sqrt{1-y}}{c_-^2(1-y)+c_+^2y},
```

whose derivative has integrable endpoint singularities uniformly in the
allowed coefficients. Below both maxima, put $x=m_P-\omega>0$. The exact
decomposition instead gives

```math
u=R_P(\omega)-1/U,\qquad
v=\frac{H_{P,-}(-x)}{\sqrt x}
  +\frac{H_{P,+}(-x-d)}{\sqrt{x+d}}.
```

For $x,d$ in fixed sufficiently small neighborhoods, the positive leading
terms in $dv/d\omega$ dominate the bounded derivatives of $H_{P,\sigma}$.
Consequently $v$ is monotone, $v\ge c$, and $|u'|\le C$.
Equation (O7) bounds the $u'$ contribution by a fixed multiple of the
interval length and the $v'$ contribution by
$\int_c^\infty v^{-2}dv$. The quotient tends to zero at $x=0$.
These bounds also apply directly at $d=0$, when the two positive singular
coefficients add. Above $M_P$
the density is zero. All other energy regions are uniform regular/cusp
regions with a nonzero contact denominator. This proves a uniform bound near
$\pi$, including the equal-maxima fiber. Compact intervening momenta use
the separated-critical-value proof in the finite-time certificate. Restoring
$J$ proves (O4), and Stieltjes integration by parts followed by the momentum
$L^2$ integral proves (O5)--(O6).

## 3. Sharper band norms

The global gap $\epsilon(P)-E_d(P;U)\ge -E_d(0;U)>0$ and the cusp-safe
second-derivative identity are proved in the finite-time certificate.
For small detuning they imply the following sharper bounds, uniformly on
$0\le P\le\pi$:

```math
Z(P)\le C(P+\rho)^{2z-1},\quad
|Z'(P)|\le C(P+\rho)^{2z-2},\quad
|E''(P)|\le CJ(P+\rho)^{z-2}.
```

**(O12)**

To verify the powers rather than differentiate an asymptotic remainder,
use the exact uncentered resolvent $D=\epsilon(k)+\epsilon(P-k)-E(P)$.
For $P\le\rho$, compact crossover control gives a gap $cJ\rho^z$ on
$|k|\le C\rho$, and $D\ge cJ|k|^z$ outside this region. For
$\rho\le P\le p_0$, the energy-ratio bracket from the detuning proof gives
the same estimates with $P$ in place of $\rho$. Set $b=\max(P,\rho)$.
Splitting at $|k|=Cb$ gives

```math
I_E\ge cJ^{-2}b^{1-2z},\quad
|I_P|\le CJ^{-1}b^{-z},\quad
|I_{PE}|\le CJ^{-2}b^{-2z},\quad
I_{EE}\le CJ^{-3}b^{1-3z},\quad
|I_{PP}|\le CJ^{-1}b^{-z-1}.
```

**(O13)**

For the last bound use $I_{PP}=2\int \epsilon'(k)\epsilon'(P-k)D^{-3}
dk/(2\pi)$, not an absolute integral of $\epsilon''$. In the local scaled
region the product is uniformly integrable even when the two cusps merge,
by Cauchy--Schwarz and $2z-2>-1$. The outer tail is bounded by
$C J^{-1}|k|^{-z-2}$. The other estimates follow from the same splitting
with one first derivative or none. Exact implicit differentiation and
$Z=(U^2I_E)^{-1}$ then give (O12). Momenta $P\ge p_0$ have a uniform gap
already at $U_c$ and obey bounded versions of all derivatives; this completes
the global bound.

Integrating the squares in (O12) gives

```math
\|Z'\|_2\le C\begin{cases}
\rho^{2z-3/2},&z < 3/4,\\
\sqrt{\log(2/\rho)},&z=3/4,\\
1,&z > 3/4,
\end{cases}
```
```math
J^{-1}\|E''Z\|_2\le C\begin{cases}
\rho^{3z-5/2},&z < 5/6,\\
\sqrt{\log(2/\rho)},&z=5/6,\\
1,&z > 5/6.
\end{cases}
```

**(O14)**

For a fixed auxiliary velocity margin $h>0$, the coefficient $A(h)$ in
(F3) consequently satisfies

```math
A(h)\le\frac{C_h}{J}\begin{cases}
\rho^{z-1/2},&z < 3/4,\\
\rho^{1/4}\sqrt{\log(2/\rho)},&z=3/4,\\
\rho^{1-z},&z > 3/4.
\end{cases}
```

**(O15)**

The logarithm at $5/6$ in the second norm is subleading to the first term
of $A(h)$. It introduces no additional case in (O15).

## 4. Closing the sharp-event relative-error bound

Take $s_\delta=\theta\delta v_{\max}(U_\delta)/J\to\theta K_z$.
Continuity and positivity of the detuning probability profile imply that,
for each fixed accuracy, one can choose **one fixed $h>0$**, independent of
small $\delta$, such that

```math
S(s_\delta,h)\le\varepsilon q_\delta/6.
```

Indeed divide this shell by $\rho^{4z-1}$, use compact velocity and residue
convergence, and squeeze the two moving boundaries by fixed nearby levels.
The limiting shell tends to zero with $h$; every positive level set has
zero measure. This also covers a level with a multiple momentum preimage.

In (F4) replace the margin-based continuum budget by $C_1/(Jt)$ from (O6).
It is sufficient to require

```math
t\ge \frac{6A(h)}{\varepsilon q_\delta},\qquad
Jt\ge\frac{12C_1}{\varepsilon\sqrt{q_\delta}}.
```

**(O16)**

The first requirement, using $q_\delta\asymp\rho^{4z-1}$ and (O15),
is $Jt\ge C\rho^{-3z+1/2}$ below $3/4$,
$Jt\ge C\rho^{-7/4}\sqrt{\log(2/\rho)}$ at $3/4$, and
$Jt\ge C\rho^{-5z+2}$ above it. The second requires only
$Jt\ge C\rho^{-2z+1/2}$ and is weaker in every case. Conversion from
$\rho$ to $\delta$ proves (O2). Since each fixed accuracy can be chosen
arbitrarily small, it also proves the joint limit (O3).

## 5. A narrow continuum peak that the variation proof must allow

A useful check on Section 2 is that a fiberwise variation bound uniform in
$P$ would be false. At **fixed $U>U_c$** and $P\downarrow0$, define

```math
a_z=z(1-z)2^{2-z},\quad b_z(x)=|x+1/2|^z+|x-1/2|^z,
```

and let $x_z>1/2$ be the unique solution of $b_z(x_z)=2^{1-z}$;
write $d_z=b_z'(x_z)>0$. Just above $m_P=2\epsilon(P/2)$, the real
loop has an inverse-square-root term from the closed inner branch:

```math
I_P(m_P+\Delta+i0)
=I_0(0)-\frac{1}{2\sqrt{(-\epsilon''(P/2))\Delta}}
+O(P^{1-z}/J)+i\frac{P^{1-z}}{Jd_z}[1+o(1)].
```

**(O17)**

This expansion is uniform when $\Delta$ is within fixed positive multiples
of $J P^{2-z}/\delta^2$; the imaginary part has a relative error, while
the displayed real remainder is an absolute one. It follows from the same
Morse coordinate as (O9); the regular subtracted loop is $O(P^{1-z}/J)$.
There is a unique real-denominator zero $\omega_*(P)$ in this neighborhood,
with

```math
\omega_*-m_P\sim\frac{J P^{2-z}}{4a_z\delta^2},\qquad
\Gamma_P:=\frac{\mathrm{Im}I_P(\omega_*+i0)}
{\partial_\omega\mathrm{Re}I_P(\omega_*+i0)}
\sim\frac{J P^{3-2z}}{2a_zd_z\delta^3}.
```

**(O18)**

After centering on the **exact** zero and scaling by $\Gamma_P$,

```math
\frac{w_{P,U}(\omega_*+\Gamma_P x)}{w_{P,U}(\omega_*)}
\longrightarrow\frac1{1+x^2},\qquad
w_{P,U}(\omega_*)\sim\frac{Jd_z}{\pi U^2}P^{z-1},
```

**(O19)**

uniformly for bounded $x$. Its spectral weight on a fixed number of widths
is of order $P^{2-z}/\delta^3$, so its diverging height is consistent with
vanishing mass. The leading shift alone cannot be used as the center of the
Lorentz profile: its subleading error can be as large as a width.

This is a resonance in the **continuous density**, not an extra bound-state
atom. An inverse linewidth is not by itself a proof that the full unfiltered
contact amplitude decays exponentially at that rate. Also, the regime here
is $P^{1-z}/\delta\to0$ at fixed detuning; it must not be substituted for
the $P\asymp\rho$ cutoff region without a separate uniform argument.
The peak explains why bounding the real contact denominator away from zero
would fail. Section 2 instead controls its variation through the monotone
real-part crossing and the nonzero outer-channel density.

## 6. Attribution and verification boundary

The finite-momentum contact loop is inherited from the two-body framework
of Sun, Feng, and Zhang, *Efimov effect in long-range quantum spin chains*,
Communications Physics **9**, 146 (2026), published Eq. (6). Rank-one spectral
densities, threshold/Morse expansions, Fourier integration by parts, and
Duhamel/smoothing estimates are established ingredients. The addition proved
here is the uniform microscopic variation estimate and its combination with
sharp band-norm scaling to establish a simultaneous rare-event time–detuning
regime. The sufficient exponent is not promoted to a new universality class.

Primary sources: https://www.nature.com/articles/s42005-026-02580-0 ;
https://arxiv.org/abs/1904.09833

`tools/check_observation_time.py` tests quotient-variation controls, actual
lattice continuum peak scaling with an explicit principal-value calculation,
band-norm power accounting and relative-error arithmetic, with an additional
check for control characters in active Markdown. The analytical proof
establishes (O1)--(O3); the checks exercise its identities and error accounting.

[Proof map](PROOF_MAP.md) · [Finite-time certificate](FINITE_TIME_CERTIFICATE.md)
