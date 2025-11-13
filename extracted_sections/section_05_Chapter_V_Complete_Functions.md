# Chapter V: Complete Functions

Lines: 2267-2452

\Chapter{V}{Complete Functions}

\First{Indicate} by~$K$ the complete integral
\[
\Tag{(1)}
K = \int_{0}^{\frac{\pi}{2}} \frac{d\phi}{\sqrt{1 - k^{2} \sin^{2} \phi}},
\]
and by~$K_{0}$ the complete integral
\[
\Tag{(2)}
K_{0} = \int_{0}^{\frac{\pi}{2}} \frac{d\phi_{1}}{\sqrt{1 - k_{0}^{2} \sin^{2} \phi_{1}}};
\]
and in a similar manner $K_{00}$,~$K_{03}$,~etc.

From \Eqref{eq.}{IV}{(12)}, Chap.~IV, we have
\begin{align}
\tan (\phi_{1} - \phi)
  &= k' \tan \phi \\\\
  &= \frac{\tan \phi_{1} - \tan \phi}{1 + \tan \phi_{1} \tan \phi}, \\\\
\intertext{whence}
\tan \phi_{1}
  &= \frac{(1 + k') \tan \phi}{1 - k' \tan^{2} \phi} \\\\
  &= \frac{1 + k'}{\dfrac{1}{\tan \phi} - k' \tan \phi}.
\end{align}
%% -----File: 052.png---Folio 46-------

From this equation we see that when $\phi = \dfrac{\pi}{2}$, $\phi_{1} = \pi$. This
same result might also have been deduced from \hyperref[page:30]{Fig.~1}, Chap.~IV,
or from the equation
\[
\Tag{(3)}
\phi_{1} = 2 \phi - k_{0} \sin 2\phi + \tfrac{1}{2} k_{0}^{2} \sin 4\phi - \text{etc.},
\]
this last being the well-known trigonometrical formula
\begin{gather*}
\tan x = n \tan y, \\\\
x = y - \frac{1 - n}{1 + n}\, \sin 2y
      + \frac{1}{2} \left(\frac{1 - n}{1 + n}\right)^{2} \sin 4y
      - \frac{1}{3} \left(\frac{1 - n}{1 + n}\right)^{3} \sin 6y + \text{etc.}
\end{gather*}
\begin{DPalign}
\lintertext{Since}
\int_{0}^{\frac{\pi}{2}} \frac{d \phi_{1}}{\Delta (k_{0}\DPtypo{}{,} \phi_{1})}
  &= K_{0},\ \text{we must have} \\\\
\int_{0}^{\pi} \frac{d\phi_{1}}{\Delta (k_{0}\DPtypo{}{,} \phi_{1})}
  &= 2K_{0}.
\end{DPalign}

These values substituted in \Eqref{eq.}{IV}{(13)}, Chap.~IV, give successively
\[
\begin{array}{r@{}l}
\Tag{(4)}
K &{}= (1 + k_{0})K_{0}, \\\\
K_{0} &{}= (1 + k_{00})K_{00}, \\\\
\Dots{2} \\\\
\llap{$K_{0(n - 1)}$} &{}= (1 + k_{0n})K_{0n};
\end{array}
\]
whence
\[
\Tag{(5)}
K = (1 + k_{0})(1 + k_{00}) \dotsm (1 + k_{0n})K_{0n}.
\]

Since the limit of~$k_{0n}$ is~$0$, $K_{0n}$~becomes
\[
K_{0n} = \int_{0}^{\frac{\pi}{2}} d \phi = \frac{\pi}{2},
\]
%% -----File: 053.png---Folio 47-------
and we have
\begin{align}
\Tag{(6)}
K &= \frac{\pi}{2} (1 + k_{0})(1 + k_{00}) \dotsm \\\\
\Tag{(7)}
  &= \frac{\tfrac{1}{2} \pi}{\cos^{2} \tfrac{1}{2}\theta
                             \cos^{2} \tfrac{1}{2}\theta_{0} \dotsm
                             \cos^{2} \tfrac{1}{2}\theta_{0n}};
\end{align}
$k_{1}$,~$k_{0}$,~etc., and $\theta_{1}$,~$\theta_{0}$,~etc., being found by \Eqref[14sub1]{eqs.}{IV}{(14_{1})} of Chap.~IV\@.

From the formulæ in these two chapters we can compute
the values of~$u$ for all values of $\phi$~and~$k$ and arrange them in
tables. These are Legendre's Tables of Elliptic Integrals.
%% -----File: 054.png---Folio 48-------


\Chapter[Evaluation for phi.]{VI}{Evaluation for $\phi$.}

\Section{TO FIND~$\phi$, $u$~AND~$k$ BEING GIVEN.}

\DPtypo{From}{\First{From}} \Eqref{eqs.}{IV}{(21)} and~\Eqref{}{IV}{(23)}, Chap.~IV, we have ($n$~having the
value which makes $\cos \theta_{0n} = 1$)
\[
\Tag{(1)}
\phi_{n}
  = \frac{2^{n}u}{(1 + k_{0})(1 + k_{00}) \dotsm (1 + k_{0n})}
  = \frac{2^{n}u \sqrt{\cos \theta}}{\sqrt{\cos \theta_{0} \dotsm \cos^{2} \theta_{0n}}},
\]
from which $\phi_{n}$~can be calculated, $k_{0},~k_{00}$,~etc., being found by
means of \Eqref[14sub1]{equations}{IV}{(14_1)}, Chap.~IV\@.

Then, having $\phi_{n}$, $k_{0}$,~$k_{00}$,~etc., we can find~$\phi$ by means of
the following equations:
\[
\begin{array}{r@{}l}
\sin (2\phi_{n - 1} - \phi_{n}) &= k_{0n} \sin \phi_{n},\\
\sin (2\phi_{n - 2} - \phi_{n - 1}) &= k_{0(n - 1)} \sin \phi_{n - 1},\\
\Dots{2} \\\\
\sin (2\phi - \phi_{1}) &= k_{0} \sin \phi_{1};\\
\end{array}
\]
whence we can get the angle~$\phi$.

When $k > \sqrt{\frac{1}{2}}$ the following formulæ will generally be found
to work more rapidly:

From \Eqref{eq.}{IV}{(29)}, Chap.~IV, we have
\[
\Tag{(2)}
\log \tan (45° + \tfrac{1}{2} \phi_{0n})
  = \frac{uM}{\sqrt{\dfrac{k_{1}k_{2} \dotsm k_{n}^{2}}{k}}},
\]
%% -----File: 055.png---Folio 49-------
from which we can get~$\phi_{0n}$; $k_{1}$,~$k_{2}$,~etc., being calculated from
\Eqref[18sub1]{eqs.}{IV}{(18_{1})}, Chap.~IV, and $\phi$~being calculated from the following
equations:
\[
\begin{array}{r@{}l}
\tan (\phi_{0(n - 1)} - \phi_{0n})
  &= k_{n} \tan \phi_{0n}, \\\\
%
\Dots{2} \\\\
%
\tan (\phi_{0} - \phi_{00})
  &= k_{2} \tan \phi_{02}, \\\\
%
\tan (\phi - \phi_{0})
  &= k \tan \phi_{0};
\end{array}
\]
whence we get~$\phi$.

This gives a method of solving the equation
\[
F\psi = n\, F\phi,
\]
where $n$~and~$\phi$ and the moduli are known, and $\psi$~is the
required quantity. $n$~and~$\phi$ give~$F\psi$, and then $\psi$~can be determined
by the foregoing methods.

When $k = 1$ *nearly*, \Eqref{equation}{}{(2)} takes a special form,---

\primo. When~$\tan \phi$ is very much less than~$\dfrac{1}{k'}$. In this case
\begin{align}
F(k, \phi)
  &= \int \frac{d\phi}{\sqrt{\cos^{2}\phi + k'^{2} \sin^{2} \phi}}
   = \int \frac{d\phi}{\sqrt{(1 + k'^{2} \tan^{2} \phi) \cos^{2} \phi}} \\\\
  &= \int \frac{d\phi}{\cos \phi}
   = \log \tan (45° + \tfrac{1}{2} \phi);
\end{align}
whence we can find~$\phi$.

\secundo. When~$\tan \phi$ and~$\dfrac{1}{k'}$ approach somewhat the same value,
and $k' \tan \phi$~cannot be neglected, $F(k, \phi)$~must be transposed
into another where $k'$~shall be much smaller, so that $k' \tan \phi$~can
be neglected.
%% -----File: 056.png---Folio 50-------

These methods for finding~$\phi$ apply only when $\phi < \dfrac{\pi}{2}$, that
is, $u < K$. In the opposite case ($u > K$) put
\[
u = 2nK ± \nu,
\]
the upper or the lower sign being taken according as $K$~is continued
in~$u$ an even or an odd number of times. In either case
$\nu < K$, and we can find~$\nu$ by the preceding methods.

Having found~$\nu$, we have from \Eqref{eq.}{III}{(5)}, Chap.~III,
\begin{align}
\am u
  &= \am (2nK ± \nu)\\
  &= n \pi ± \am \nu.
\end{align}
%% -----File: 057.png---Folio 51-------


