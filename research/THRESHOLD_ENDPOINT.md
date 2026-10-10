# The exact lattice threshold in the scaling limit

## Statement and domain

Fix $J>0$ and $1/2<z<1$. Write

$$
\epsilon_z(k)=J|2\sin(k/2)|^z,\qquad
A_P(q)=\epsilon_z(q+P/2)+\epsilon_z(q-P/2),\qquad
T_P=\epsilon_z(P).
$$

The contact integral at its lower spectral edge is an improper, absolutely
convergent integral:

$$
I_P(T_P)=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac{1}{A_P(q)-T_P},\qquad P\ne0.
$$

The endpoint scaling law is

$$
\boxed{I_P(T_P)-I_0(0)=\frac{|P|^{1-z}}{J}\,[F_z(1)+o(1)]}\tag{E1}
$$

as $P\to0$, where

$$
F_z(1)=\int_{\mathbb R}\frac{dx}{2\pi}
\left[\frac{1}{|x+1/2|^z+|x-1/2|^z-1}-\frac{1}{2|x|^z}\right].
$$

In contrast, the fixed-energy-ratio expansion in Section 4 of the
[spectral proof](SPECTRAL_PROOF.md), Eq. (8), uses $E=J|P|^z e$ with
**fixed $e<1$**. It must not be evaluated at $e=1$ on the lattice:

$$
T_P=J|P|^z\left[1-\frac{zP^2}{24}+O(P^4)\right]<J|P|^z.
$$

For sufficiently small nonzero $P$, the latter energy is inside the continuum.
It does not define the real below-band integral used in the pole equation.
A principal-value prescription would be a different object. Although the
energy difference is small, continuity of a resolvent across its spectrum
cannot be assumed.

## Proof of the endpoint limit

By evenness, take $P>0$. The known strict subadditivity of $\epsilon_z$ gives
$A_P(q)\ge T_P$, with equality only at $q=\pm P/2$ modulo $2\pi$.
We control these zeros before taking any limit.

Near $q=P/2$, put $q=P(1/2+s)$. For a sufficiently small fixed $a>0$ and
$|s|\le a$, chord bounds and the mean-value theorem away from zero give

$$
\epsilon_z(Ps)\ge cJP^z|s|^z,\qquad
|\epsilon_z(P(1+s))-\epsilon_z(P)|\le CJP^z|s|.
$$

The constants can be chosen uniformly for small $P$. Since $z<1$, choose $a$
so that $Ca^{1-z}\le c/2$. Then

$$
A_P(P(1/2+s))-T_P\ge \frac c2 JP^z|s|^z.\tag{E2}
$$

The other cusp has the same bound. This both proves integrability at the
lattice threshold and supplies a uniform integrable majorant proportional
to $|s|^{-z}$ after rescaling.

For fixed $M$, use $q=Px$ on $|q|\le MP$. The scaled denominator converges to
$|x+1/2|^z+|x-1/2|^z-1$. Away from its two zeros, this limit is strictly
positive on compact sets. At the zeros, (E2) supplies domination. The
subtracted rest integrand is bounded by a constant times $|x|^{-z}$ near
$x=0$, also integrable. Dominated convergence therefore yields the desired
limiting integral on $[-M,M]$.

For the remaining region, first choose $M$ sufficiently large and fix small
$q_0>0$. On $MP\le|q|\le q_0$, the symmetric Taylor difference obeys

$$
|A_P(q)-2\epsilon_z(q)|\le CJP^2|q|^{z-2}.
$$

Also $T_P\le JP^z$ and both $A_P(q)-T_P$ and $2\epsilon_z(q)$ are bounded
below by $cJ|q|^z$. Consequently,

$$
\left|\frac1{A_P(q)-T_P}-\frac1{2\epsilon_z(q)}\right|
\le\frac CJ\left(P^z|q|^{-2z}+P^2|q|^{-z-2}\right).\tag{E3}
$$

After integration and multiplication by $J/P^{1-z}$, this region contributes
at most $C(M^{1-2z}+M^{-1-z})$. It tends to zero as $M\to\infty$, because
$2z>1$. The compact region $q_0\le|q|\le\pi$ contributes
$O(P^{2z-1}+P^{1+z})$ in the same normalization and hence vanishes as
$P\to0$. The tails of the limiting subtracted integral satisfy the same
integrable power bounds. Taking $P\to0$ first and then $M\to\infty$ proves
(E1).

## Consequence for the moving binding threshold

Define $U_c(P)=I_P(T_P)^{-1}$ and $U_c=I_0(0)^{-1}$. Then

$$
\boxed{\frac1{U_c(P)}-\frac1{U_c}
=\frac{|P|^{1-z}}J\,[F_z(1)+o(1)].}\tag{E4}
$$

Thus the threshold-shift formula in the spectral proof remains valid. Its
endpoint justification is (E1), not substitution of $e=1$ into the
fixed-$e<1$ lattice resolvent. The strict inequality $F_z(1)>0$ follows from
the subadditivity argument already given for the continuum integral.

## Scope of the correction and checks

The preserved pilot's sentence extending its fixed-$e$ lattice argument to
$e=1$ used the wrong lattice energy. The archive is unchanged. The generated
spectral page replaces that sentence with the exact-threshold convention
and a link to this proof; the literal replacement is recorded in the reading
transform ledger. This is a correction to proof prose, not merely formatting.

The pole lies at $e\to c_z<1$, so its existence, differentiated velocity,
residue, local-coincidence tail, and preparation-size conclusions are
unaffected. The weaker-attraction threshold coefficient is justified by
(E4). No uniform finite-time transport rate is inferred.

`tools/check_endpoint.py` adds three regression groups: exclusion of the
above-edge substitution; comparison of two threshold quadratures; and
convergence to the endpoint coefficient with an exact energy-unit check.
It explicitly reuses the preserved scalar solver for one representation.
The second quadrature uses an algebraic endpoint weight and a stable
trigonometric difference. These are finite diagnostics, not interval
certificates; the limit rests on (E2)–(E3).
