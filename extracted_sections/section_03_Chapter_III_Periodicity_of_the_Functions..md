# Chapter III: Periodicity of the Functions.

Lines: 1187-1552

\Chapter{III}{Periodicity of the Functions.}

\First{When} the elliptic integral
\[
\int_{0}^{\phi} \frac{d \phi}{\sqrt{1 - k^{2} \sin^{2} \phi}}
\]
has for its amplitude~$\dfrac{\pi}{2}$, it is called, following the notation of
Legendre, the *complete* function, and is indicated by~$K$, thus:
\[
K = \int_{0}^{\frac{\pi}{2}} \frac{d \phi}{\sqrt{1-k^{2} \sin^{2} \phi}}.
\]

When~$k$ becomes the complementary modulus,~$k'$, (see \Eqref{eq.}{IV}{\DPtypo{4}{(4)}},
Chap.\ IV,) the corresponding complete function is indicated by~$K'$,
thus:
\[
K' = \int_{0}^{\frac{\pi}{2}} \frac{d \phi}{\sqrt{1-k'^{2} \sin^{2} \phi}}.
\]

From these, evidently,
\[
\am (K, k) = \frac{\pi}{2},\qquad \am (K', k') = \frac{\pi}{2}.
\]
\[
\Tag{(1)}
\left\{
\begin{aligned}
\sn (K, k) &= 1; \\\\
\cn (K, k) &= 0; \\\\
\dn (K, k) &= k'.
\end{aligned}
\right.
\]
%% -----File: 029.png---Folio 23-------

From \Eqref{eqs.}{II}{(7)},~\Eqref{}{II}{(8)}, and~\Eqref{}{II}{(9)}, Chap.~II, we have, by the substitution
of the values of~$\sn (K) = 1$, $\cn (K) = 0$, $\dn (K) = k'$,
\[
\Tag{(2)}
\left\{
\begin{aligned}
\sn 2K &= 0; \\\\
\cn 2K &= -1; \\\\
\dn 2K &= 1.
\end{aligned}
\right.
\]

These equations, by means of \Eqref{}{II}{(1)},~\Eqref{}{II}{(2)}, and~\Eqref{}{II}{(3)} of Chap.~II,
give
\[
\Tag{(3)}
\left\{
\begin{aligned}
\sn (u+2K) &= - \sn u; \\\\
\cn (u+2K) &= -\cn u; \\\\
\dn (u+2K) &= \dn u;
\end{aligned}
\right.
\]
and these, by changing $u$ into~$u+2K$, give
\[
\Tag{(4)}
\left\{
\begin{aligned}
\sn (u+4K) &= \sn u; \\\\
\cn (u+4K) &= \cn u; \\\\
\dn (u+4K) &= \dn u.
\end{aligned}
\right.
\]

From these equations it is seen that the elliptic functions
$\sn$,~$\cn$,~$\dn$, are periodic functions having for their period~$4K$.
Unlike the period of trigonometric functions, this period is not
a fixed one, but depends upon the value of~$k$, the modulus.

From the Integral Calculus we have
\begin{align}
\int_{0}^{n \frac{\pi}{2}} \frac{d \phi}{\Delta \phi}
  &= \int_{0}^{\frac{\pi}{2}} \frac{d \phi}{\Delta \phi}
   + \int_{\frac{\pi}{2}}^{\pi} \frac{d \phi}{\Delta \phi}
   + \int_{\pi}^{\frac{3\pi}{2}} \frac{d \phi}{\Delta \phi} + \cdots
   + \int_{(n-1)\frac{\pi}{2}}^{n \frac{\pi}{2}} \frac{d \phi}{\Delta \phi} \\\\
  &= n \int_{0}^{\frac{\pi}{2}} \frac{d \phi}{\Delta \phi}
   = nK;
\end{align}
from which we see that
\begin{DPalign}
n \frac{\pi}{2} &= \am (nK); \\\\
%% -----File: 030.png---Folio 24-------
\intertext{or, since $\dfrac{\pi}{2} = \am K$,}
\am (nK) &= n · \am K, \\\\
\intertext{and}
n \pi &= \am (2nK), \\\\
\lintertext{and also}
n \pi &= 2n \am K.
\end{DPalign}
In the case of an Elliptic Integral with the arbitrary angle~$\alpha$,
we can put
\[
\DPtypo{d}{\alpha} = n \pi ± \beta,
\]
where $\beta$ is an angle between $0$~and~$\dfrac{\pi}{2}$, the upper or the lower
sign being taken according as $\dfrac{\pi}{2}$ is contained in~$\alpha$ an even or
an uneven number of times.

In the first case we have
\[
\int_0^{n\pi+\beta} \frac{d \phi}{\Delta \phi}
  = \int_0^{n\pi} \frac{d \phi}{\Delta \phi}
  + \int_{n\pi}^{n\pi+\beta} \frac{d \phi}{\Delta \phi};
\]
or, putting $\phi_{1} = \DPtypo{}{\phi} - n \pi$,
\[
\int_0^{n\pi+\beta} \frac{d \phi}{\Delta \phi}
  = 2nK + \int_0^\beta \frac{d \phi_{1}}{\Delta \phi_{1}}.
\]

In the second case
\[
\int_0^{n\pi-\beta} \frac{d \phi}{\Delta \phi}
  = \int_0^{n\pi} \frac{d \phi}{\Delta \phi}
  - \int_{n\pi-\beta}^{n\pi} \frac{d \phi}{\Delta \phi};
\]
or, putting $\phi_{1} = n \pi - \phi$,
\[
\int_0^{n\pi-\beta} \frac{d \phi}{\Delta \phi}
  = 2nK - \int_0^\beta \frac{d \phi_{1}}{\Delta \phi_{1}};
\]
%% -----File: 031.png---Folio 25-------
or in either case,
\[
\int_0^{n\pi±\beta} \frac{d \phi}{ \Delta \phi}
  = 2nK ± \int_0^\beta \frac{d \phi_{1} }{ \Delta \phi_{1}}.
\]

Thus we see that the Integral with the general amplitude~$\alpha$
can be made to depend upon the complete integral~$K$ and
an Integral whose amplitude lies between $0$~and~$\dfrac{\pi}{2}$.

Put now
\[
\int_0^\beta \frac{d \phi_{1} }{ \Delta \phi_1} = u,\qquad \beta = \am u.
\]

This gives
\begin{DPalign}
\int_0^{n\pi±\beta} \frac{d \phi }{ \Delta \phi} &= 2nK ± u,\\
\lintertext{or}
\am (2nK ± u)
  &= n \pi ± \beta\\
\Tag{(5)}
  &= n\pi ± \am u\\
\Tag{(6)}
  &= 2n · \am K ± \am u;\\
\lintertext{or, since}
\am (-z)
  &= -\am z,\\
\am (u ± 2nK)
  &= \am u ± n \pi\\
  &= \am u ± 2n · \am K.\\
\end{DPalign}

Taking the sine and cosine of both sides, we have
\begin{align}
\sn (u + 2nK) &= ± \sn u;\\
\cn (u + 2nK) &= ± \cn u;
\end{align}
the upper or the lower sign being taken according as $n$~is even
or odd. By giving the proper values to~$n$ we can get the same
results as in \Eqref{equations}{}{(3)} and~\Eqref{}{}{(4)}.

Putting $n = 1$ in \Eqref{eq.}{}{(5)}, we have
\begin{align}
\sn (2K - u)
  &= \sin \pi \cn u - \cos \pi \sn u\\
\Tag{(7)}
  &= \sn u.
\end{align}
%% -----File: 032.png---Folio 26-------

Elliptic functions also have an imaginary period. In order
to show this we will, in the integral
\[
\int_0^\phi \frac{d \phi}{\Delta \phi},
\]
assume the amplitude as imaginary. Put
\[
\sin \phi = i \tan \psi.
\]
From this we get
\[
\Tag{(8)}
\left\{
\begin{aligned}
\cos \phi
  &= \frac{1}{\cos \psi}; \\\\
\Delta \phi
  &= \frac{\sqrt{1 - k'^{2} \sin^{2} \psi}}{\cos \psi}
   = \frac{\Delta (\psi, k')}{\cos \psi}; \\\\
d \phi
  &= i \frac{d \psi}{\cos \psi}.
\end{aligned}
\right.
\]
From these, since $\phi$~and~$\psi$ vanish simultaneously, we easily get
\begin{align}
\int_0^\phi \frac{d \phi}{\Delta \phi}
  &= i \int_0^\psi \frac{d \psi}{\Delta (\psi, k')}. \\\\
\intertext{Put}
\int_0^\psi \frac{d \psi}{\Delta (\psi, k')} &= u \quad \text{and} \quad
\psi = \am (u, k'), \\\\
\intertext{whence}
\int_0^\phi \frac{d \phi}{\Delta \phi} &= iu \quad \text{and} \quad
\phi = \am (iu);
\end{align}
and these substituted in \Eqref{Eq.}{}{(8)} give
\[
\Tag{(9)}
\left\{
\begin{aligned}
\sn iu &= i \tn (u, k'); \\\\
\cn iu &= \frac{1}{\cn (u, k')}; \\\\
\dn iu &= \frac{\dn (u, k')}{\cn (u, k')}.
\end{aligned}
\right.
\]
%% -----File: 033.png---Folio 27-------
By assuming
\[
\int_0^\psi \frac{d \psi}{\Delta (\psi, k')} = iu \quad \text{and}\quad
\int_0^\phi \frac{d \phi}{\Delta \phi} = -u,
\]
we get
\begin{align}
\sn (-u) &= i \tn (iu, k'), \\\\
\cn (-u) &= \frac{1}{\cn(iu, k')}, \\\\
\dn (-u) &= \frac{\dn (iu, k')}{\cn (iu, k')};
\end{align}
or, from \Eqref{eq.}{II}{(14)}, Chap.~II,
\[
\Tag{(10)}
\left\{
\begin{aligned}
\sn u &= -i \tn (iu, k'); \\\\
\cn u &= \frac{1}{\cn (iu, k')}; \\\\
\dn u &= \frac{\dn (iu, k')}{\cn (iu, k')}.
\end{aligned}
\right.
\]

From \Eqref{eqs.}{II}{(7)}, Chap.~II, making $\nu = K$, we get, since
$\sn K = 1$, $\cn K = 0$, $\dn K = k'$,
\[
\Tag{(11)}
\left\{
\begin{aligned}%[** PP: Moved \mp out of numerator in second equation]
\sn (u ± K) &= ± \frac{\cn u \dn u}{1 - k^{2} \sn^{2} u} = ± \dfrac{\cn u}{\dn u}; \\\\
\cn (u ± K) &= \mp \frac{\sn u \dn uk'}{\dn^{2} u} = \mp \frac{k' \sn u}{\dn u}; \\\\
\dn (u ± K) &= + \frac{k'}{\dn u}.
\end{aligned}
\right.
\]

In these equations, changing $u$ into~$iu$, we get, by means of
\Eqref{eqs.}{}{(9)},
\[
\Tag{(12)}
\left\{
\begin{aligned}
\sn (iu ± K) &= ± \frac{1}{\dn (u, k')}; \\\\
\cn (iu ± K) &= \mp \frac{ik' \sn (u, k')}{\dn (u, k')}; \\\\
\dn (iu ± K) &= + \frac{k' \cn (u, k')}{\dn (u, k')}.
\end{aligned}
\right.
\]
%% -----File: 034.png---Folio 28-------

Putting now in \Eqref{eqs.}{}{(9)} $u ± K'$ instead of~$u$, and making use
of \Eqref{eqs.}{}{(10)}, and interchanging $k$~and~$k'$, we have
\[
\Tag{(13)}
\left\{
\begin{aligned}
\sn (iu ± iK') &= - \frac{i \cn (u, k')}{k \sn (u, k')}; \\\\
\cn (iu ± iK') &= \mp \frac{\dn (u, k')}{k \sn (u, k')}; \\\\
\dn (iu ± iK') &= \mp \frac{1}{\sn (u, k')}.
\end{aligned}
\right.
\]

Substituting in these~$-iu$ in place of~$u$, we get, by
means of \Eqref{eqs.}{II}{(9)} and \Eqref{eqs.}{II}{(14)} of Chap.~II,
\[
\Tag{(14)}
\left\{
\begin{aligned}
\sn (u ± iK') &= \frac{1}{k \sn u}; \\\\
\cn (u ± iK') &= \mp \frac{i \dn u}{k \sn u}; \\\\
\dn (u ± iK') &= \mp i \cot \am u.
\end{aligned}
\right.
\]

In these equations, putting $u + K$ in place of~$u$, we get
\[
\Tag{(15)}
\left\{
\begin{aligned}
\sn (u + K ± iK') &= + \frac{\dn u}{k \cn u}; \\\\
\cn (u + K ± iK') &= \mp \frac{ik'}{k \cn u}; \\\\
\dn (u + K ± iK') &= ± ik' \tn u.
\end{aligned}
\right.
\]
Whence for $u = 0$ we get
\[
\Tag{(16)}
\left\{
\begin{aligned}
\sn (K ± iK') &= \frac{1}{k}; \\\\
\cn (K ± iK') &= \mp \frac{ik'}{k}; \\\\
\dn (K ± iK') &= 0.
\end{aligned}
\right.
\]
%% -----File: 035.png---Folio 29-------

If in \Eqref{eqs.}{}{(14)} we put $u = 0$, we see that as $u$~approaches
zero, the expressions
\Pagelabel{29}
\[
\sn (± iK'), \quad \cn (± iK'), \quad \dn (± iK')
\]
approach infinity.

We see from what has preceded that Elliptic Functions
have two periods, one a real period, and one an imaginary
period.

In the former characteristic they resemble Trigonometric
Functions, and in the latter Logarithmic Functions.

On account of these two periods they are often called
Doubly Periodic Functions. Some authors make this double
periodicity the starting-point of their investigations. This
method of investigation gives some very beautiful results and
processes, but not of a kind adapted for an elementary work.

It will be noticed that the Elliptic Functions $\sn u$,~$\cn u$, and~$\dn u$
have a very close analogy to trigonometric functions, in
which, however, the independent variable~$u$ is not an angle, as
it is in the case of trigonometric functions.

Like Trigonometric Functions, these Elliptic Functions can
be arranged in tables. These tables, however, require a double
argument, viz., $u$~and~$k$. In \Chapref{Chap.}{IX} these functions are developed
into series, from which their values may be computed
and tables formed.

No complete tables have yet been published, though they
are in process of computation.
%% -----File: 036.png---Folio 30-------


