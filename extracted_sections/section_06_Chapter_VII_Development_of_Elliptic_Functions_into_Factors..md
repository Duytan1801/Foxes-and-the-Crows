# Chapter VII: Development of Elliptic Functions into Factors.

Lines: 2453-3676

\Chapter{VII}{Development of Elliptic Functions into Factors.}
\SetRunningHeads{Development into Factors}

From \Eqref{eq.}{IV}{(12)}, Chap.~IV, we readily get
\begin{align}
\sin (2\phi_{0} - \phi)
  &= k \sin \phi;\\
%
\sin \phi
  &= \frac{\sin 2 \phi_{0}}{\sqrt{1 + k^{2} + 2k \cos 2\phi_0}}\\
  &= \frac{\sin 2 \phi_{0}}{\sqrt{(1 + k)\DPtypo{}{^2} - 4k \sin^{2} \phi_0}}\\
  &= \frac{1 + k_{0}'}{2} · \frac{\sin 2 \phi_{0}}{\sqrt{1 - k_{1}^{2} \sin^{2} \phi_{0}}}\\
\end{align}
$\Bigl(\text{since } \dfrac{4k}{1 + k} = k_{1} \text{ and } 1 + k = \dfrac{2}{1 + k_{0}'}, \text{\Eqref{eqs.}{IV}{(6)} and~\Eqref{}{IV}{(10)}, Chap.~IV}\Bigr)$;
and thence
\[
\Tag{(1)}
\sin \phi = \frac{(1 + k_{0}') \sin \phi_{0} \cos \phi_{0}}{\Delta (\phi_{0}, k_{1})}.
\]

From \Eqref{eq.}{IV}{(13)}, Chap.~IV, we have
\[
\int_{0}^{\phi_{0}} \frac{d \phi_{0}}{\Delta (\phi_{0}, k_{1})}
  = \frac{1 + k}{2} \int_{0}^{\phi} \frac{d\phi}{\Delta (\phi, k)};
\]
and from \Eqref{eq.}{V}{(4)}, Chap.~V, passing up the scale of moduli
one step,
\[
1 + k = \frac{K_{1}}{K},
\]
%% -----File: 058.png---Folio 52-------
whence %[** PP: Next several displays aligned on = in original]
\[
F(\phi_{0}, k_{1}) = \frac{K_{1}}{2K} F(\phi, k).
\]

Put
\[
F(\phi_{0}, k_{1}) = u_{1}\quad \text{and} \quad F(\phi, k) = u,
\]
whence
\[
u_{1} = \frac{K_{1}}{2K} u.
\]

Furthermore,
\begin{align}
\phi &= \am (u, k);\\
\phi_{1} = \am (u_{1}, k_{1}) &= \am \left( \frac{K_{1}}{2K} u, k_{1} \right).
\end{align}

Substituting these values in \Eqref{eq.}{}{(1)}, we have
\[
\sn (u, k)
  = (1 + k'_{0})
    \frac{\sn \left( \dfrac{K_{1}}{2K} u, k_{1} \right)
          \cn \left( \dfrac{K_{1}}{2K} u, k_{1} \right)}
         {\dn \left( \dfrac{K_{1}}{2K} u, k_{1} \right)}.
\]

But from \Eqref{eq.}{III}{(11)}, Chap.~III, we have
\begin{align}
\frac{\cn (v, k_{1})}{\dn (v, k_{1})} &= \sn (v + K_{1}, k_{1}), \\\\
\intertext{or}
\frac{\cn \left( \dfrac{K_{1}}{2K} u, k_{1} \right)}
     {\dn \left( \dfrac{K_{1}}{2K} u, k_{1} \right)}
  &=  \sn \left( \frac{K_{1}u}{2K} + K_{1}, k_{1} \right) \\\\
  &=  \sn \left( \dfrac{K_{1}}{2K} (u + \DPtypo{K_{1}}{2K}), k_{1} \right);
\end{align}
%% -----File: 059.png---Folio 53-------
whence
\begin{DPalign}
\Tag{(2)}
\sn (u, k)
  &= (1 + k_{0}') \sn \frac{K_{1}u}{2K}
     \sn \left[\frac{K_{1}}{2K} (u + 2K)\right].\footnotemark \\\\
& \rintertext{\llap{(Mod.${}= k_{1}$.)}}
\end{DPalign}
\footnotetext{The analogous formula in Trigonometry is
  \[
  \sin \phi = \DPtypo{\tfrac{1}{2}}{2} \sin \tfrac{1}{2} \phi\,
              \sin \tfrac{1}{2} (\phi + \pi).
  \]}

From this equation, evidently, we have generally
\begin{DPgather*}
\Tag[2st]{(2)^*}
\sn (\nu, k_{n})
  = (1 + k'_{0(n + 1)}) \sn \frac{K_{n + 1}}{2K_{n}} \nu
    \sn \left[\frac{K_{n + 1}}{2K_{n}} (\nu + 2K_{n})\right]. \\\\
\rintertext{\llap{(Mod.${}= k_{n + 1}$.)}}
\end{DPgather*}

Applying this general formula to the two factors of \Eqref{eq.}{}{(2)},
we have
\begin{DPalign}
\sn \left(\frac{K_{1}u}{2K}, k_{1}\right)
  &= (1 + k'_{00}) \sn \frac{K_{2}}{2K_{1}} · \frac{K_{1}u}{2K}
      · \sn \left[\frac{K_{2}}{2K_{1}} \left(\frac{K_{1}u}{2K} + 2K_{1}\right)\right] \\\\
& \rintertext{\llap{(Mod.\ $k_{2}$)}} \\\\
  &= (1 + k'_{00}) \sn \frac{K_{2}u}{2^{2}K} \sn \frac{K_{2}}{2^{2}K} (u + 4K);
\rintertext{\llap{(Mod.\ $k_{2}$;)}}
\end{DPalign}
\begin{DPgather*}
\Tag{(3)}
\sn \left[\frac{K_{1}}{2K} (u + 2K), k_{1}\right]
  = (1 + k'_{00}) \sn \frac{K_{2}}{2^{2}K} (u + 2K) \\\\
  · \sn \frac{K_{2}}{2K_{1}} \left[\frac{K_{1}}{2K} (u + 2K) + 2K_{1}\right].
\rintertext{(Mod.\ $k_{2}$.)}
\end{DPgather*}

The last argument in this equation is equal to
\[
\frac{K_{2}}{2^{2}K} (u + 6K);
\]
and since, \Eqref{eq.}{III}{(7)}, Chap.~III,
\[
\sn (u, k_{2}) = \sn (2K_{2} - u, k_{2}),
\]
%% -----File: 060.png---Folio 54-------
we can put in place of this,
\[
2K_{2} - \frac{K_{2}}{2^{2}K} (u + 6K\DPtypo{}{)} = \frac{K_{2}}{2^{2}K} (2K - u);
\]
whence \Eqref{eq.}{}{(3)} becomes
\begin{DPgather*}%[** PP: Re-breaking]
\sn \left[\frac{K_{1}}{2K} (u + 2K), k_{1}\right]
  = (1 + k'_{00}) \sn \frac{K_{2}}{2^{2}K} (2K + u)
    · \sn \frac{K_{2}}{2^{2}K} (2K - u). \\\\
\rintertext{\llap{(Mod.\ $k_{2}$.)}}
\end{DPgather*}

Substituting these values in \Eqref{eq.}{}{(2)}, we have
\begin{DPalign}%[** PP: Aligning on equals sign]
\Tag{(4)}
\sn (u, k)
  &= (1+k'_{0})(1 + k'_{00})^{2} \sn \frac{K_{2}u}{2^{2}K} \\\\
  &\quad
  · \sn \frac{K_{2}}{2^{2}K} (2K ± u) \sn \frac{K_{2}}{2^{2}K} (4K+u),
\rintertext{(Mod.\ $k_{2}$,)}
\end{DPalign}
in which the double sign indicates two separate factors which
are to be multiplied together.

By the application of the general \Eqref[2st]{equation}{}{(2)^*} we find that
the arguments in the second member of \Eqref{eq.}{}{(4)} will each give
rise to two new arguments, as follows:
\[
\frac{K_{2}u}{2^{2}K}\quad \text{gives}\quad \frac{K_{3}u}{2^{3}K},
\]
and
\begin{gather*}
\frac{K_{3}}{2K_{2}} \left(\frac{K_{2}u}{2^{2}K} + 2K_{2}\right)
  = \frac{K_{3}}{2^{3}K} (u + 8K); \\\\
\frac{K_{2}}{2^{2}K} (2K ± u)\quad \text{gives}\quad
\frac{K_{3}}{2^{3}K} (2K ± u),
\end{gather*}
%% -----File: 061.png---Folio 55-------
and
\begin{gather*}
\Tag{(a)}
\frac{K_{3}}{2K_{2}} \left[\frac{K_{2}}{2^{2}K} (2K ± u) + 2K_{2}\right]
  = \frac{K_{3}}{2^{3}K} (10K ± u), \\\\
\frac{K_{2}}{2^{2}K} (4K + u) \quad \text{gives} \quad \frac{K_{3}}{2^{3}K} (4K + u),
\intertext{and}
\Tag{(b)}
\frac{K_{3}}{2K_{2}} \left[\frac{K_{2}}{2^{2}K} (4K + u) + 2K_{2}\right]
  = \frac{K_{3}}{2^{3}K} (12K + u).
\end{gather*}

Subtracting~\Eqno{(a)} and~\Eqno{(b)} from~$2K_{3}$, by which the sine of the
amplitudes will not be changed [\Eqref{eq.}{III}{(7)}, Chap.~III], and since
our new modulus is~$k_{3}$, we have for the expressions \Eqno{(a)}~and~\Eqno{(b)},
\begin{gather*}
\Tag[apr]{(a')}
\frac{K_{3}}{2^{3}K} (6K \mp u); \\\\
\Tag[bpr]{(b')}
\frac{K_{3}}{2^{3}K} (4K - u).
\end{gather*}

Substituting these values in \Eqref{eq.}{}{(4)}, and remembering the
factor $(1 + k'_{03})$ introduced by each application of \Eqref[2st]{eq.}{}{(2)^*}, we
have
\begin{DPalign}%[** PP: Align on equal signs, remove extraneous semicolons]
\sn (u, k)
  &= (1 + k'_{0})(1 + k'_{00})^{2}(1 + k'_{03})^{4}
     \sn \frac{K_{3}u}{2^{3}K}\DPtypo{;}{} \\\\
  &\quad·
     \sn \frac{K_{3}}{2^{3}K} (2K ± u)
     \sn \frac{K_{3}}{2^{3}K} (4K ± u)\DPtypo{;}{} \\\\
  &\quad·
     \sn \frac{K_{3}}{2^{3}K} (6K ± u)
     \sn \frac{K_{3}}{2^{3}K} (8K + u).
\rintertext{(Mod.\ $k_{3}$.)}
\end{DPalign}
%% -----File: 062.png---Folio 56-------

From this the law governing the arguments is clear, and we
can write for the general equation
\begin{DPalign}
\Tag{(5)}
\sn (u, k)
  &= (1 + k_{0}')(1 + k'_{00})^{2}(1 + k'_{03})^{4} \dotsm (1 + k'_{0n})^{2^{n-1}} \\\\
  &\quad· \sn \frac{K_{n}u}{2^{n}K}
          \sn \frac{K_{n}}{2^{n}K} (2K ± u) \\\\
  &\quad· \sn \frac{K_{n}}{2^{n}K} (4K ± u)
          \sn \frac{K_{n}}{2^{n}K} (6K ± u) \\\\
  &\quad \dotsm \sn \frac{K_{n}}{2^{n}K} \Bigl[(2^{n} - 2)K ± u\Bigr] \\\\
  &\quad· \sn \frac{K_{n}}{2^{n}K} (2^{n}K + u).
\rintertext{\llap{(Mod.\ $k_{n}$.)}}
\end{DPalign}

Indicate the continued product of the binomial factors by~$A'$,
and we have
\[
A' = (1 + k_{0}')(1 + k'_{00})^{2}(1 + k'_{03})^{4}(1 + k'_{04})^{8} \dotsm.
\]

Since the limit of~$k'_{0}$, $k'_{00}$,~etc., is zero, it is evident that
these factors converge toward the value unity. It can be shown
that the functional factors also converge toward the value
unity. Thus the argument of the last factor can be written
\[
K_{n} + \frac{K_{n}u}{2^{n}K}.
\]

From \Eqref{eq.}{III}{(11)}, Chap.~III, we get then
\begin{DPgather*}
\sn \left(K_{n} + \frac{K_{n}u}{2^{n}K}\right)
  = \frac{\cn \dfrac{K_{n}u}{2^{n}K}}
         {\dn \dfrac{K_{n}u}{2^{n}K}}.
\rintertext{(Mod.\ $k_{n}$.)}
\end{DPgather*}

But since $k_{n}$ at its limit is equal to unity, $\cn = \dn$; whence
the last factor of \Eqref{eq.}{}{(5)} is unity.
%% -----File: 063.png---Folio 57-------

From \Eqref{eq.}{IV}{(21)}, Chap.~IV, we have
\[
\operatorname{limit} \frac{K_{n}}{2^{n}K} = \frac{2 \pi}{2 K'}.
\]

Therefore for $n = \infty$, \Eqref{eq.}{}{(5)} becomes
\begin{DPalign}%[** PP: Align on equals sign]
\sn (u, k)
  &= A'   \sn \frac{\pi u}{2K'} \sn \frac{\pi}{2K'} (2K ± u) \\\\
  &\quad· \sn \frac{\pi}{2K'}(4K ± u) \sn \frac{\pi}{2K'}(6K ± u), \ldots
\rintertext{(Mod.\ $1$,)} \\\\
\intertext{or}
\Tag{(6)}
\sn (u, k)
  &= A' \sn \frac{\pi u}{2K'} \left[{\textstyle\prod\limits_{1}^{\infty}} h\right]
        \sn \frac{\pi}{2K'} (2hK ± u),
\rintertext{\llap{(Mod.\ $1$,)}}
\end{DPalign}
where the sign~$\Prod$ indicates the continued product in the same
manner as $\sum$~indicates the continued sum.

When~$k = 1$, $\displaystyle\int_{0}^{\phi} F(\phi, k)\DPtypo{}{\,d\phi}$ becomes
\[
\nu = \int_{0}^{\phi} \frac{d \phi}{\cos \phi}
  = \tfrac{1}{2} \DPtypo{\log^e}{\log_\epsilon} \frac{1 + \sin \phi}{1 - \sin \phi};
\]
whence
\[
e^{2\nu} = \frac{1 + \sin \phi}{1 - \sin \phi},
\]
and
\[
\sin \phi = \frac{e^{2\nu} - 1}{e^{2\nu} + 1}
  = \frac{e^{\nu} - e^{-\nu}}{e^{\nu} + e^{-\nu}}
  = \sn (\nu, 1).
\]
%% -----File: 064.png---Folio 58-------

Hence in \Eqref{equation}{}{(6)}
\begin{align}
\sin \frac{\pi u}{2K'}
  &= \frac{e^{\frac{\pi u}{2K'}} - e^{-\frac{\pi u}{2K'}}}
          {e^{\frac{\pi u}{2K'}} + e^{-\frac{\pi u}{2K'}}}; \\\\
\sn \frac{\pi}{2K'}(2hK ± u)
  &= \frac{e^{ \frac{h\pi K}{K'}} e^{±\frac{\pi u}{2K'}}
         - e^{-\frac{h\pi K}{K'}} e^{\mp\frac{\pi u}{2K'}}}
          {e^{ \frac{h\pi K}{K'}} e^{±\frac{\pi u}{2K'}}
         + e^{-\frac{h\pi K}{K'}} e^{\mp\frac{\pi u}{2K'}}}.
\end{align}

Put
\[
\Tag[6st]{(6)^*}
q = e^{-\frac{\pi K'}{K}}, \quad q' = e^{-\frac{\pi K}{K'}},
\]
and the last expression becomes
\begin{align}
\sn \frac{\pi}{2K'} & (2hK ± u)
  = \frac{q'^{-h} e^{±\frac{\pi u}{2K'}} - q'^{h} e^{\mp\frac{\pi u}{2K'}}}
         {q'^{-h} e^{±\frac{\pi u}{2K'}} + q'^{h} e^{\mp\frac{\pi u}{2K'}}}; \\\\
%
\sn \frac{\pi}{2K'} & (2hK + u) \sn \frac{\pi}{2K'}(2hK - u) \\\\
 &= \frac{q'^{-h} e^{ \frac{\pi u}{2K'}} - q'^{h} e^{-\frac{\pi u}{2K'}}}
         {q'^{-h} e^{ \frac{\pi u}{2K'}} + q'^{h} e^{-\frac{\pi u}{2K'}}}
  · \frac{q'^{-h} e^{-\frac{\pi u}{2K'}} - q'^{h} e^{ \frac{\pi u}{2K'}}}
         {q'^{-h} e^{-\frac{\pi u}{2K'}} + q'^{h} e^{ \frac{\pi u}{2K'}}} \\\\
%
 &= \frac{q'^{-2h} + q'^{2h} - \left(e^{\frac{\pi u}{K'}} + e^{-\frac{\pi u}{K'}}\right)}
         {q'^{-2h} + q'^{2h} + \left(e^{\frac{\pi u}{K'}} + e^{-\frac{\pi u}{K'}}\right)}.
\end{align}

From plane trigonometry we have the equations
\[
\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} = -i \tan ix, \quad e^{x} + e^{-x} = 2 \cos ix;
\]
%% -----File: 065.png---Folio 59-------
where $i = \sqrt{-1}$: which gives
\begin{DPalign}
\sn \frac{\pi u}{2K'}
  &= -i \tan \frac{\pi i u}{2K'};
\rintertext{\llap{(Mod.\ $1$;)}} \\\\
%
\sn \frac{\pi}{2K'} & (2hK + u) \sn \frac{\pi}{2K'}(2hK - u) \\\\
  &= \frac{q'^{-2h} + q'^{2h} - 2 \cos \dfrac{\pi iu}{K'}}
          {q'^{-2h} + q'^{2h} + 2 \cos \dfrac{\pi iu}{K'}} \\\\
%
%[** PP: No equation label in orig., but text refers specifically to (7).]
\DPtypo{}{\Tag{(7)}}
  &= \frac{1 - 2q'^{2h} \cos \dfrac{\pi iu}{K'} + q'^{4h}}
          {1 + 2q'^{2h} \cos \dfrac{\pi iu}{K'} + q'^{4h}}.
\end{DPalign}

From \Eqref{eq.}{III}{(10)}, Chap.~III, we have
\[
\sn (u, k) = -i \tn (iu, k').
\]

Substituting these values in eq.~(6), we have
\[
\tn (iu, k') = A' \tan \frac{\pi iu}{2K'} \Prod
  \frac{1 - 2q'^{2h} \cos \dfrac{\pi iu}{K'} + q'^{4h}}
       {1 + 2q'^{2h} \cos \dfrac{\pi iu}{K'} + q'^{4h}}.
\]

Now in place of the series of moduli $k'$,~$k_{0}'$ and the corresponding
complete integral~$K'$, we are at liberty to substitute
the parallel series of moduli $k$,~$k_{0}$ and the corresponding complete
integral~$K$; calling the new integral~$u$, we have
\begin{align}
\Tag{(8)}
\tn (u, k)
  &= A \tan \frac{\pi u}{2K} \DPtypo{\{\textstyle\prod}{\Prod}
     \frac{1 - 2q^{2h} \cos \dfrac{\pi u}{K} + q^{4h}}
          {1 + 2q^{2h} \cos \dfrac{\pi u}{K} + q^{4h}} \\\\
%% -----File: 066.png---Folio 60-------
  &= A \tan \frac{\pi u}{2K}
     \frac{1 - 2q^{2} \cos \dfrac{\pi u}{K} + q^{4}}
          {1 + 2q^{2} \cos \dfrac{\pi u}{K} + q^{4}} \\\\
%[** PP: Adding {} to the right of &s to coax · into math mode]
  &\PadTo[r]{{}= A \tan \dfrac{\pi u}{2K}}{{}·{}}
   \frac{1 - 2q^{4} \cos \dfrac{\pi u}{K} + q^{8}}
        {1 + 2q^{4} \cos \dfrac{\pi u}{K} + q^{8}} \\\\
  &\PadTo[r]{{}= A \tan \dfrac{\pi u}{2K}}{{}·{}}
   \frac{1 - 2q^{6} \cos \dfrac{\pi u}{K} + q^{12}}
        {1 + 2q^{6} \cos \dfrac{\pi u}{K} + q^{12}} \dotsm,
\end{align}
where
\[
\Tag{(9)}
A = (1 + k_{0})(1 + k_{00})^{2}(1 + k_{03})^{4}(1 + k_{04})^{8} \dotsm
\]

Now in \Eqref{equation}{}{(6)} put $u+K$~for~$u$, and we have, since
[\Eqref{eq.}{III}{(11)}, Chap.~III] $\sn (u+K)= \dfrac{\cn u}{\dn u}$,
\begin{DPalign}%[** PP: Re-breaking]
\frac{\cn u}{\dn u}
  &= A' \sn \frac{\pi (u+K)}{2K'} \\\\
  &\quad \Prod \sn \frac{\pi}{2K'} [(2h+1)K+u]
             · \sn \frac{\pi}{2K'} [(2h-1)K-u]. \\\\
&\rintertext{\llap{(Mod.\ $1$.)}}
\end{DPalign}
Now from $2h-1$ and~$2h+1$ we have the following series of
numbers respectively:
\[
\begin{array}{l@{\qquad}*{6}{@{\quad}r}}
2h-1: & 1, & 3, & 5, & 7, & 9, & \text{etc.} \\\\
2h+1: &    & 3, & 5, & 7, & 9, & \text{etc.}
\end{array}
\]

It will be observed that the factor outside of the sign~$\Prod$,
viz., $\sin \am \dfrac{\pi (u + K)}{2K'}$, would, if placed under the sign~$\Prod$, supply
%% -----File: 067.png---Folio 61-------
the missing first term of the second series. Hence, placing this
factor within the sign, we have
\begin{DPalign}%[** PP: Re-breaking]
\Tag{(10)}
\frac{\cn u}{\dn u}
  &= A'\Prod \sn \frac{\pi}{2K'} \left[(2h-1)K + u\right]
           · \sn \frac{\pi}{2K'} \left[(2h-1)K - u\right]. \\\\
  & \rintertext{\llap{(Mod.\ $1$.)}}
\end{DPalign}

Comparing this with \Eqref{equation}{}{(7)}, we see that the factors
herein differ from those in \Eqref{equation}{}{(7)} only in having $2h-1$
in place of~$2h$; hence we have
\begin{DPgather*}
\sn \frac{\pi}{2K'} [(2h-1)K + u]
\sn \frac{\pi}{2K'} [(2h-1)K - u] \\\\
  = \frac{1 - 2q'^{2h-1} \cos \dfrac{\pi iu}{K'} + q'^{4h-2}}
         {1 + 2q'^{2h-1} \cos \dfrac{\pi iu}{K'} + q'^{4h-2}}.
\rintertext{(Mod.\ $1$.)}
\end{DPgather*}

From \Eqref{eqs.}{III}{(10)}, Chap.~III, we have
\[
\frac{\cn (u, k)}{\dn (u, k)} = \frac{1}{\dn(iu, k')};
\]
whence \Eqref{eq.}{}{(10)} becomes
\[
\Tag{(11)}
\frac{1}{\dn(iu, k')}
  = A'\Prod \frac{1 - 2q'^{2h-1} \cos \dfrac{\pi iu}{K'} + q'^{4h-2}}
                 {1 + 2q'^{2h-1} \cos \dfrac{\pi iu}{K'} + q'^{4h-2}};
\]
and when in place of~$iu$, $k'$, $K'$, $q'$,~$A'$, we substitute~$u$, $k$, $K$,
$q$ and~$A$, and invert the equation, we have
\[
\Tag{(12)}
\dn (u, k)
  = \frac{1}{A} \Prod \frac{1 + 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}
                           {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}.
\]
%% -----File: 068.png---Folio 62-------

Bearing in mind the remarkable property (Chap.~III, \Pageref{p.}{29})
that the functions $\sn u$~and~$\dn u$ approach infinity for the same
value of~$u$, we see that both these functions, except as to the
factor independent of~$u$, must have the same denominator.
Furthermore, since $\sn u$~and~$\tn u$ disappear for the same value
of~$u$, they must, except for the independent factor, have the
same numerator. Hence, indicating by~$B$ a new quantity,
dependent upon~$k$ but independent of~$u$, we have
\[
\Tag{(13)}
\sn (u, k) = B \sin \frac{\pi u}{2K} \Prod
  \frac{1 - 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}};
\]
and since
\[
\cn u = \frac{\sn u}{\tn u},
\]
we also have, from \Eqref{eqs.}{}{(8)} and~\Eqref{}{}{(13)},
\[
\Tag{(14)}
\cn (u, k) = \frac{B}{A} \cos \frac{\pi u}{2K} \Prod
  \frac{1 + 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}.
\]
Collecting these results, we have the following equations:
\begin{align}
\Tag{(15)}
\sn (u, k)
  &= B \sin \frac{\pi u}{2K} \Prod
  \frac{1 - 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}, \\\\
\Tag{(16)}
\cn (u, k)
  &= \frac{B}{A} \cos \frac{\pi u}{2K} \Prod
  \frac{1 + 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}, \\\\
%% -----File: 069.png---Folio 63-------
\Tag{(17)}
\dn (u, k) &= \frac{1}{A} \Prod
  \frac{1 + 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}.
\end{align}

To ascertain the values of $A$ and~$B$, we proceed as follows:

In \Eqref{eq.}{}{(17)} we make~$u = 0$, whence, by \Eqref{eq.}{II}{(13)}, Chap.~II,
we have
\begin{align}
1 &= \frac{1}{A} \Prod \left(\frac{1 + q^{2h-1}}{1 - q^{2h-1}}\right)^{2}; \\\\
\intertext{whence}
\Tag{(18)}
\frac{1}{A} &= \Prod \left(\frac{1 - q^{2h-1}}{1 + q^{2h-1}}\right)^{2}. \\\\
\intertext{\indent In \Eqref{equation}{}{(17)}, making~$u=K$, we get, by \Eqref{equation}{III}{(1)},
Chap.~III,}
k' &= \frac{1}{A} \Prod \left(\frac{1 - q^{2h-1}}{1 + q^{2h-1}}\right)^{2}
    = \frac{1}{A^{2}}; \\\\
\Tag{(19)}
\therefore \frac{1}{A} &= \sqrt{k'}.
\end{align}
We have identically
\begin{align}
1 &= B \frac{1}{B} = B \frac{\dfrac{1}{A}}{\dfrac{B}{A}}
   = B \frac{\sqrt{k'}}{\dfrac{B}{A}}; \\\\
\intertext{whence}
\frac{B}{A} & = B \sqrt{k'}.
\end{align}

To calculate~$B$, put~$e^{\frac{i\pi u}{2K}} = \nu$; if we change $\dfrac{\pi u}{2K}$ into
%% -----File: 070.png---Folio 64-------
$\dfrac{\pi u}{2K} + \dfrac{i\pi K'}{2K}$, $\nu$~will change into~$\nu \sqrt{q}$, and $\sn u$ will become, by
\Eqref{eq.}{III}{(14)}, Chap.~III,
\[
\sn (u+iK') = \frac{1}{k \sn u}.
\]

Now, replacing $\sin \dfrac{\pi u}{2K}$ and $\cos \dfrac{\pi u}{K}$ by their exponential values,
and observing that
\[
1 - 2q^{n} \cos \frac{\pi u}{K} + q^{2n} = (1 - q^{n}\nu^{2})(1 - q^{n}\nu^{-2}),
\]
we have
\[
\sn u = \frac{B}{2} · \frac{\nu - \nu^{-1} }{\sqrt{-1}}
      · \frac{\Prod (1 - q^{2h}  \nu^{2})(1 - q^{2h}  \nu^{-2})}
             {\Prod (1 - q^{2h-1}\nu^{2})(1 - q^{2h-1}\nu^{-2})}.
\]

Changing $u$ into~$u + iK'$, and consequently $\nu$~into~$\nu \sqrt{q}$, we
have
\[
\frac{1}{k \sn u}
  = \frac{B}{2} · \frac{\nu \sqrt{q} - \nu^{-1} \sqrt{q^{-1}}}{\sqrt{-1}}
  · \frac{\Prod (1 - q^{2h+1}\nu^{2})(1 - q^{2h-1}\nu^{-2})}
         {\Prod (1 - q^{2h}  \nu^{2})(1 - q^{2h-2}\nu^{\DPtypo{2}{-2}})}.
\]

Multiplying these equations together, member by member,
and observing that
\begin{align}
\nu \sqrt{q} - \nu^{-1} \sqrt{q^{-1}}
  &= \frac{1 - q\nu^{2}}{-\nu \sqrt{q}}, \\\\
\nu - \nu^{-1}
  &= \nu(1 - \nu^{-2}),
\end{align}
we get
\begin{align}
\frac{1}{k}
  &= \frac{B^{2}}{4}
  · \frac{1 - q\nu^{2}}{\nu \sqrt{q}}
  · \nu(1 - \nu^{-2})
  · \frac{\Prod(1 - q^{2h+1}\nu^{2})(1 - q^{2h}  \nu^{-2})}
         {\Prod(1 - q^{2h-1}\nu^{2})(1 - q^{2h-2}\nu^{-2})} \\\\
%% -----File: 071.png---Folio 65-------
  &= \frac{B^{2}}{4 \sqrt{q}} (1 - q\nu^{2})\nu(1 - \nu^{-2})
     \frac{(1 - q^{3}\nu^{2})(1 - q^{5}\nu^{2}) \dotsm}
          {(1 - q    \nu^{2})(1 - q^{3}\nu^{2}) \dotsm} \\\\
  &\PadTo[r]{{}=\dfrac{B^{2}}{4 \sqrt{q}} (1 - q\nu^{2})\nu(1 - \nu^{-2})}{{}·{}}
     \frac{(1 - q^{2}\nu^{-2})(1 - q^{4}\nu^{-2}) \dotsm}
          {(1 -      \nu^{-2})(1 - q^{2}\nu^{-2}) \dotsm} \\\\
  &= \frac{B^{2}}{4} · \frac{1}{\sqrt{q}}.
\end{align}
\begin{align}
\therefore B &= \frac{2 \sqrt[4]{q}}{\sqrt{k}}; \\\\
\intertext{whence}
\frac{B}{A} &= 2 \sqrt[4]{q} \sqrt{\frac{k'}{k}}.
\end{align}

Substituting these values in \Eqref{eqs.}{}{(15)},~\Eqref{}{}{(16)}, and~\Eqref{}{}{(17)}, we
have
\begin{align}
\Tag{(20)}
\sn (u, k) &= \frac{2 \sqrt[4]{q}}{\sqrt{k}} \sin \frac{\pi u}{2K} \Prod
  \frac{1 - 2q^{2h} \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}; \\\\
%
\Tag{(21)}
\cn (u, k) &= \frac{2 \sqrt{k'} \sqrt[4]{q}}{\sqrt{k}} \cos \frac{\pi u}{2K} \Prod
  \frac{1 + 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}; \\\\
%
\Tag{(22)}
\dn (u, k) &= \sqrt{k'} \Prod
  \frac{1 + 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}.
\end{align}
%% -----File: 072.png---Folio 66-------


\Chapter[The Theta Function.]{VIII}{The $\Theta$ Function.}

\First{We} will indicate the denominator in \Eqref{eq.}{VII}{(20)}, Chap.~VII, by~$\phi (u)$,
thus:
\[
\Tag{(1)}
\phi (u) = \Prod(1 - 2q^{2h - 1} \cos \frac{\pi u}{K} + q^{4h - 2}).
\]
We will now develop this into a series consisting of the cosines
of the multiples of $\dfrac{\pi u}{K}$. Put $\dfrac{\pi u}{2K} = x$, whence
\begin{align}
2 \cos \frac{\pi u}{K} &= (e^{2ix} + e^{-2ix});\\
\intertext{but}
1 - 2q^{2h - 1} \cos \frac{\pi u}{K} + q^{4h - 2}
  &= (1 - q^{2h - 1}e^{2ix})(1 - q^{2h - 1}e^{-2ix}),
\end{align}
and therefore
\begin{align}
\Tag{(2)}
\phi (u)
  &= (1 - qe^{2ix})(1 - q^{3}e^{2ix})(1 - q^{5}e^{2ix}) \dotsm \\\\
  &\PadTo{{}={}}{}
     (1 - qe^{-2ix})(1 - q^{3}e^{-2ix})(1 - q^{5}e^{-2ix}) \dotsm
\end{align}

Putting now $u + 2iK'$ instead of~$u$, we have
\begin{align}
x_{1} &= \frac{\pi(u + 2iK')}{2K} = x + \frac{\pi iK'}{K},\\
2ix_{1} &= 2ix - \frac{2 \pi K'}{K};
\end{align}
%% -----File: 073.png---Folio 67-------
and
\begin{align}
e^{2ix_{1}} &= q^{2}e^{2ix}, \\\\
e^{-2ix_{1}} &= \frac{1}{q^{2}} e^{-2ix}.
\end{align}
From these we have
\begin{align}
\phi (u + 2iK') = - \frac{1}{q} e^{-2ix}
  & (1 - qe^{2ix}) (1 - q^{3}e^{2ix}) \dotsm \\\\
  & (1 - qe^{-2ix})(1 - q^{3}e^{-2ix}) \dotsm;
\end{align}
whence
\begin{align}
\phi (u + 2iK') &= -\frac{1}{q} e^{-2ix} \phi (u), \\\\
\intertext{or}
\Tag{(3)}
\phi (u + 2iK') &= -q^{-1} e^{-\frac{\pi iu}{K}} \phi (u).
\end{align}

Now put
\[
\Tag{(4)}
\phi (u) = A + B \cos \frac{\pi u}{K}
  + C \cos \frac{2\pi u}{K}
  + D \cos \frac{3\pi u}{K} + \text{etc.}
\]

Since
\[
\cos \frac{\pi u}{K} = \tfrac{1}{2} \left(e^{2ix} + e^{-2ix}\right),
\]
this becomes
\begin{align}
\Tag{(5)}
\phi (u) = A & + \tfrac{1}{2} Be^{2ix}  + \tfrac{1}{2} Ce^{4ix}  + \tfrac{1}{2} De^{6ix}  + \dotsb \\\\
             & + \tfrac{1}{2} Be^{-2ix} + \tfrac{1}{2} Ce^{-4ix} + \tfrac{1}{2} De^{-6ix} + \dotsb;
\end{align}
whence
\begin{align}
\Tag{(6)}
-\frac{1}{q} e^{-2ix} \phi (u) =
  & -\frac{A}{q}  e^{-2ix} - \frac{B}{2q} - \frac{C}{2q} e^{2ix} - \frac{D}{2q} e^{4ix} - \dotsb \\\\
  & -\frac{B}{2q} e^{-4ix} - \frac{C}{2q} e^{-6ix} - \frac{D}{2q} e^{-8ix} - \dotsb\DPtypo{}{.}
\end{align}
%% -----File: 074.png---Folio 68-------

Now in \Eqref{equation}{}{(5)} put $u + 2iK'$ in place of~$u$, remembering
that $e^{2ix}$~and~$e^{-2ix}$ are thereby changed respectively into
$q^{2}e^{2ix}$~and~$q^{-2}e^{-2ix}$, and we have
\begin{align}
\Tag{(7)}
\phi (u + 2iK') = A
  & + \frac{Bq^{2}}{2} e^{2ix}  + \frac{Cq^{4}}{2} e^{4ix}  + \frac{Dq^{6}}{2} e^{6ix} + \dotsb \\\\
  & + \frac{B}{2q^{2}} e^{-2ix} + \frac{C}{2q^{4}} e^{-4ix} + \dotsb.
\end{align}

Since \Eqref{equations}{}{(6)} and~\Eqref{}{}{(7)} are equal, we have
\[
\begin{array}{r@{}lcr@{}l}
-\dfrac{B}{2q} &{}= A, &\qquad\qquad& B &= -2qA; \\\\
-\dfrac{C}{2q} &{}= \dfrac{Bq^{2}}{2}, && C &= +2q^{4}A; \\\\
-\dfrac{D}{2q} &{}= \dfrac{Cq^{4}}{2}, && D &= -2q^{9}A; \\\\
\Dots{2} && \Dots{2} \\\\
\end{array}
\]
whence
\[
\Tag{(8)}
\left\{
\begin{aligned} %[** PP: Retain small parentheses]
&\Prod (1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}) \\\\
&\begin{aligned}
  {} = A(1 - 2q \cos \dfrac{\pi u}{K}
    &+ 2q^{4} \cos \dfrac{2\pi u}{K} - 2q^{9} \cos \dfrac{3\pi u}{K} \\\\
    &+ 2q^{16} \cos \dfrac{4\pi u}{K} - \ldots).
  \end{aligned}
\end{aligned}
\right.
\]

The series in the second member has been designated by
Jacobi and subsequent writers by~$\Theta (u)$, thus:
\[
\Tag{(9)}
\Theta (u) = 1 - 2q \cos \frac{\pi u}{K} + 2q^{4} \cos \frac{2\pi u}{K} - \dotsb
\]
%% -----File: 075.png---Folio 69-------


\Chapter[The Theta and Eta Functions.]{IX}{The $\Theta$ and $\Eta$ Functions.}

\First{In} \Eqref{equation}{VII}{(20)}, Chap.~VII, viz.,
\[
\sn (u, k) = \frac{2 \sqrt[4]{q}}{\sqrt{k}} \sin \frac{\pi u}{2K}
  \Prod \frac{1 - 2q^{2h}   \cos \dfrac{\DPtypo{u \pi}{\pi u}}{K} + q^{4h}}
             {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}},
\]
the numerator and the denominator have been considered separately
by Jacobi, who gave them a special notation and developed
from them a theory second only in importance to the
elliptic functions themselves.

Put [see \Eqref{equation}{VIII}{(8)}, Chap.~VIII]
\begin{gather*}
\Tag{(1)}
\Theta (u) = \frac{1}{A} \Prod (1 - 2q^{2h-1} \cos \frac{\pi u}{K} + q^{4h-2}). \\\\
\Tag{(2)}
\Eta (u) = 2 \frac{1}{A} \sqrt[4]{q} \sin \frac{\pi u}{2K}
  \Prod \left(1 - 2q^{2h} \cos \frac{\pi u}{K} + q^{4h}\right);
\end{gather*}
$A$ being a constant whose value is to be determined later.
From these we have
\[
\Tag{(3)}
\sn (u, k) = \frac{1}{\sqrt{k}} · \frac{\Eta (u)}{\Theta (u)}.
\]
%% -----File: 076.png---Folio 70-------

The functions $\sn u$~and~$\cn u$ can also be expressed in terms
of the new functions; thus we have
\[
\Tag{(4)}
\cn (u, k) = \sqrt{\frac{k'}{k}} · 2 \sqrt[4]{q} \cos \frac{\pi u}{2K}
  \Prod \frac{1 + 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
             {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}};
\]
or, since $\sin x = \cos \left(x + \dfrac{\pi}{2}\right)$ and $\cos x = -\DPtypo{\cos}{\sin} \left(x + \dfrac{\pi}{2}\right)$,
and putting $u = \dfrac{2Kx}{\pi}$,
\begin{align}
\cn \left(\frac{2Kx}{\pi}, k\right)
  &= \sqrt{\frac{k'}{k}}
     \frac{\Eta   \left[\dfrac{2K}{\pi} \left(x + \dfrac{\pi}{2}\right)\right]}
          {\Theta \left(\dfrac{2Kx}{\pi}\right)} \\\\
  &= \sqrt{\frac{k'}{k}}
     \frac{\Eta   \left[\dfrac{2Kx}{\pi} + K\right]}
          {\Theta \left(\dfrac{2Kx}{\pi}\right)}.
\end{align}

Replacing $\dfrac{2Kx}{\pi}$ by its value,~$u$, we have
\[
\Tag{(5)}
\cn (u, k) = \sqrt{\frac{k'}{k}}\, \frac{\Eta (u + K)}{\Theta (u)}.
\]

Furthermore,
\[
\Tag{(6)}
\dn (u, k) = \sqrt{k'} \Prod
  \frac{1 + 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}
       {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}
\]
%% -----File: 077.png---Folio 71-------
gives in the same manner
\begin{align}
\dn \frac{2Kx}{\pi}
  &= \sqrt{k'}\,
     \frac{\Theta \left[\dfrac{2K}{\pi} \left(x + \dfrac{\pi}{2}\right)\right]}
          {\Theta \left(\dfrac{2Kx}{\pi}\right)},
\intertext{or}
\Tag{(7)}
\dn (u, k)
  &= \sqrt{k'}\, \frac{\Theta (u + K)}{\Theta (u)}.
\end{align}

If we put
\begin{align}
\Tag{(8)}
\Eta (u + K)   &= \Eta_{1}(u), \\\\
\Tag{(9)}
\Theta (u + K) &= \Theta_{1}(u),
\end{align}
the three elliptic functions can be expressed by the following
formulas:
\begin{align}
\Tag{(10)}
\sn (u, k) &= \frac{1}{\sqrt{k}} · \frac{\Eta (u)}{\Theta (u)}; \\\\
\Tag{(11)}
\cn (u, k) &= \sqrt{\frac{k'}{k}} · \frac{\Eta_{1}(u)}{\Theta (u)}; \\\\
\Tag{(12)}
\dn (u, k) &= \sqrt{k'} \frac{\Theta_{1} (u)}{\Theta (u)}.
\end{align}

These functions $\Theta$~and~$\Eta$ can be expressed in terms of
each other. By definition,
\[
\Eta (u) = 2C \sqrt[4]{q} \sin \frac{\pi u}{2K}
  \Prod \left(1 - 2q^{2h} \cos \frac{\pi u}{K} + q^{4h}\right);
\]
%% -----File: 078.png---Folio 72-------
but
\begin{align}
1 - 2q^{h} \cos \frac{\pi u}{K} + q^{2h}
  &= \Bigl(1 - q^{h}e^{ \frac{\pi u \sqrt{-1}}{K}}\Bigr)
     \Bigl(1 - q^{h}e^{-\frac{\pi u \sqrt{-1}}{K}}\Bigr) \\\\
\sin \frac{\pi u}{2K}
  &= \frac{e^{\frac{\pi iu}{2K}} - e^{-\frac{\pi iu}{2K}}}{2 \sqrt{-1}} \\\\
  &= e^{\frac{-\pi iu}{2K}} \frac{1 - e^{\frac{\pi iu}{K}}}{2} \sqrt{-1},
\end{align}
and consequently
\[
\Tag{(13)}
\Eta(u) = C \sqrt[4]{q} e^{-\frac{\pi iu}{2K}}
  \sqrt{-1} \Bigl(1 - e^{\frac{\pi iu}{K}}\Bigr)
            \Bigl(1 - q^{2}e^{-\frac{\pi iu}{K}}\Bigr)
            \Bigl(1 - q^{2}e^{ \frac{\pi iu}{K}}\Bigr) \dotsm.
\]

Now, changing $u$ into~$u + iK'$, and remembering that
$e^{-\frac{\pi K'}{K}} = q$, we have
\begin{multline*} %[** PP: Re-breaking]
\Tag{(14)}
\Eta(u + iK')
  = Cq^{-\frac{1}{4}}e^{\DPtypo{\frac{-\pi iu}{2K}}{-\frac{\pi iu}{2K}}}
  \sqrt{-1}\Bigl(1 - qe^{ \frac{\pi iu}{K}}\Bigr)
           \Bigl(1 - qe^{-\frac{\pi iu}{K}}\Bigr) \\\\
           \Bigl(1 - q^{3}e^{ \frac{\pi iu}{K}}\Bigr)
           \Bigl(1 - q^{3}e^{-\frac{\pi iu}{K}}\Bigr) \dotsm;
\end{multline*}
and reuniting the factors two by two, this becomes
\begin{multline*} %[** PP: Re-breaking]
\Tag{(15)}
\Eta(u + iK')
  = C \sqrt{-1} q^{-\frac{1}{4}}e^{-\frac{\pi iu}{2K}} \\\\
    \left(1 - 2q \cos \frac{\pi u}{K} + q^{2}\right)
    \left(1 - 2q^{3} \cos \frac{\pi u}{K} + q^{6}\right) \dotsm;
\end{multline*}
and finally, according to \Eqref{equation}{}{(1)},
\[
\Tag{(16)}
\Eta (u + iK') = \sqrt{-1} q^{-\frac{1}{4}} e^{-\frac{\pi iu}{2K}} \Theta (u).
\]
%% -----File: 079.png---Folio 73-------

In the same manner, we can get
\[
\Tag{(17)}
\Theta (u + iK') = \sqrt{-1} q^{-\frac{1}{4}}e^{-\frac{\pi iu}{2K}} \Eta (u).
\]

Substituting $u+2K$ for~$u$ in \Eqref{equations}{}{(1)} and~\Eqref{}{}{(2)}, we get
\begin{align}
\Tag{(18)}
\Theta (u + 2K) &= \Theta (u), \\\\
\Tag{(19)}
\Eta (u + 2K) &= -\Eta (u),
\end{align}
since $\cos \dfrac{\pi}{K} (u + 2K) = \cos \dfrac{\pi u}{K}$ and $\sin \dfrac{\pi}{2K} (u + 2K) = -\sin \dfrac{\pi u}{2K}$.

The comparison of these four equations with \Eqref{equations}{}{(10)},~\Eqref{}{}{(11)},
and~\Eqref{}{}{(12)} shows the periodicity of the elliptic functions.
For example, comparing \Eqref{eqs.}{}{(10)} and~\Eqref{}{}{(16)} and~\Eqref{}{}{(17)}, we
see that changing~$u$ into $u+iK'$ simply multiplies the numerator
and denominator of the second member of \Eqref{eq.}{}{(10)} by
the same number, and does not change their ratio.

The addition of~$2K$ changes the sign of the function, but
not its value.

We will define $\Theta_{1}$ and~$\Eta_{1}$ as follows:
\begin{align}
\Tag{(20)}
\Theta_{1}(x) &= \Theta (x + K); \\\\
\Tag{(21)}
\Eta_{1}(x) &= \Eta (x + K).
\end{align}
Hence we get, from \Eqref{equation}{}{(17)},
\begin{DPalign}
\Theta_{1}(x + iK')
  &= \Theta (x + iK' + K) = \Theta (x + K + iK') \\\\
  &= i\Eta (x + K)e^{-\frac{i\pi}{4K} (2x + 2K + iK')} \\\\
  &= i\Eta_{1}(x)e^{-\frac{i\pi}{4K} (2x + iK')} (-\sqrt{-1}), \\\\
\lintertext{since}
e^{-\frac{i\pi}{2}}
  &= \cos \frac{\pi}{2} - \sqrt{-1} \sin \frac{\pi}{2} = -\sqrt{-1};
\end{DPalign}
%% -----File: 080.png---Folio 74-------
whence
\[
\Tag{(22)}
\Theta_{1}(x + iK') = \Eta_{1}(x)e^{-\frac{i\pi}{4K}(2x + iK')}.
\]
In a similar manner we get
\[
\Tag[22st]{(22)^*}
\Eta_{1}(x + iK') = \Theta_{1}(x)e^{-\frac{i\pi}{4K}(2x + iK')}.
\]

In \Eqref{eq.}{VIII}{(9)}, Chap.~VIII, put $u = \dfrac{2Kz}{\pi}$, and we get
\[
\Tag{(23)}
\Theta \left(\frac{2Kz}{\pi}\right) = 1 - 2q \cos 2z + 2q^{4} \cos 4z - \dotsb.
\]

Now, in this equation, changing~$z$ into $z + \dfrac{\pi}{2}$, and observing
\Eqref{eq.}{}{(20)}, we get
\[
\Tag{(24)}
\Theta_{1} \left(\frac{2Kz}{\pi}\right) = 1 + 2q \cos 2z + 2q^{4} \cos 4z + \dotsb.
\]

Applying \Eqref{eq.}{}{(22)} to this, we have
\begin{align}
&\begin{aligned}
\Eta_{1} \left(\frac{2Kz}{\pi}\right) %[** Explicit sizing of () required?]
  &= \Theta_{1}\left(\frac{2K}{\pi} \Bigl(z + \frac{\pi iK'}{2K}\Bigr)\right) e^{\frac{\pi i}{4K}\left(\frac{4Kz}{\pi} + iK'\right)} \\\\
  &= \Theta_{1}\left(\frac{2K}{\pi} \Bigl(z + \frac{\pi iK'}{2K}\Bigr)\right) e^{iz}q^{\frac{1}{4}}
\end{aligned} \\\\
%
  &= e^{iz}q^{\frac{1}{4}}
     \left[1 + 2q     \cos 2\Bigl(z + \frac{\pi iK'}{2K}\Bigr)
             + 2q^{4} \cos 4\Bigl(z + \frac{\pi iK'}{2K}\Bigr) + \dotsb\right] \\\\
  &= e^{iz}q^{\frac{1}{4}}
     \biggl[1 + q   \Bigl(e^{2i\bigl(z + \frac{\pi iK'}{2K}\bigr)}
                      + e^{-2i\bigl(z + \frac{\pi iK'}{2K}\bigr)}\Bigr) \\\\
  & \PadTo{{}=e^{iz}q^{\frac{1}{4}} \biggl[1}{}
           {} + q^{4} \Bigl(e^{4i\bigl(z + \frac{\pi iK'}{2K}\bigr)}
    + e^{-4i\bigl(z + \frac{\pi iK'}{2K}\bigr)}\Bigr) + \dotsb\biggr] \\\\
%% -----File: 081.png---Folio 75-------
  &= e^{iz} q^{\frac{1}{4}}
     \left[1 + q(qe^{2iz} + q^{-1}e^{-2iz})
             + q^{4}(q^{2}e^{4iz} + q^{-2}e^{-4iz}) + \dotsb \right] \\\\
%[** PP: Not breaking next two lines]
  &= e^{iz}q^{\frac{1}{4}}
     \left[1 + q^{2}e^{2iz} + q^{6}e^{4iz} + \dotsb
           + e^{-2iz} + q^{2}e^{-4iz} + \dotsb \right] \\\\
  &= q^{\frac{1}{4}} \left[e^{iz} + q^{2}e^{3iz} + q^{6}e^{5iz} + \dotsb
  + e^{-iz} + q^{2}e^{-3iz} + q^{6}e^{-5iz} + \dotsb \right] \\\\
  &= 2q^{\frac{1}{4}} \left[\cos z + q^{2} \cos 3z + q^{6} \cos 5z + \dotsb\right];
\end{align}
whence
\[
\Tag{(25)}
\Eta_{1} \left( \frac{2Kz}{\pi} \right)
  = 2 \sqrt[4]{q} \cos z
  + 2 \sqrt[4]{q^{9}} \cos 3z
  + 2 \sqrt[4]{q^{25}} \cos 5z + \dotsb
\]

In this equation, changing~$z$ into $z - \dfrac{\pi}{2}$, and applying \Eqref{eq.}{}{(21)},
we get
\begin{align}
\Tag{(26)}
\Eta \left( \frac{2Kz}{\pi} \right)
  &= 2 \sqrt[4]{q} \sin z
   - 2 \sqrt[4]{q^{9}} \sin 3z
   + 2 \sqrt[4]{q^{25}} \sin 5z - \dotsb, \\\\
\intertext{since}
\Eta_{1} \left( \frac{2Kz}{\pi} \right)
  &= \Eta \left( \frac{2Kz}{\pi} + K \right).
\end{align}

We will now determine the constant~$A$ of \Eqref{eq.}{VIII}{(8)}, Chap.~VIII,
and \Eqref{eqs.}{}{(1)} and~\Eqref{}{}{(2)} of this chapter. Denote~$A$ by~$f(q)$,
and we have
\[
\Tag[26st]{(26)^*}
\Prod(1 - 2q^{2h - 1} \cos \frac{\pi u}{K} + q^{4h - 2}) = f(q)\Theta (u).
\]

Substituting herein $u = 0$ and $u = \dfrac{K}{2}$, we have
\begin{align}
\Prod(1 - q^{2h - 1})^{2} &= f(q) \Theta (0);\\
\Prod(1 + q^{4h - 2}) &= f(q) \Theta \left( \frac{K}{2} \right).
\end{align}
%% -----File: 082.png---Folio 76-------

From \Eqref{eq.}{VIII}{(9)}, Chap.~VIII, we get
\begin{align}
\Tag{(27)}
\Theta (0)
  &= 1 - 2q + 2q^{4} - 2q^{9} + 2q^{16} - \dotsb; \\\\
\Tag{(28)}
\Theta \left( \frac{K}{2} \right)
  &= 1 - 2q^{4} + 2q^{16} - 2q^{36} + 2q^{64} - \dotsb;
\end{align}
from which we see that $\Theta (0)$ is changed into $\Theta \left( \dfrac{K}{2} \right)$ when we
put $q^{4}$~in place of~$q$.

Whence
\[
\Prod(1 - q^{8h - 4})^{2} = f(q^{4})\Theta \left( \frac{K}{2} \right);
\]
and therefore
\begin{align}
\frac{f(q)}{f(q^{4})}
  &= \Prod \frac{1 + q^{4h - 2}}{(1 - q^{8h - 4})^{2}}\\
\Tag{(29)}
  &= \Prod \frac{1}{(1 - q^{8h - 4})(1 - q^{4h - 2})}.
\end{align}

Now, the expressions $4h - 2$, $8h - 4$, and~$8h$ give the
following series of numbers:
\begin{center}
\small
\begin{tabular}{l<{\qquad}*{18}{@{\,}c@{\,}}}
$4h - 2$, &2,&  &6,&  &10,&   &14,&   &18,&   &22,&   &26,&   &30,&   &34;&   \\\\
$8h - 4$, &  &4,&  &  &   &12,&   &   &   &20,&   &   &   &28,&   &   &   &36;\\
$8h$,     &  &  &  &8,&   &   &   &16,&   &   &   &24,&   &   &   &32.&   &
\end{tabular}
\end{center}
Hence, the three expressions taken together contain all the
even numbers, and
\[
\Prod(1 - q^{8h - 4})(1 - q^{4h - 2})(1 - q^{8h}) = \Prod(1 - q^{2h}).
\]
Therefore, multiplying \Eqref{eq.}{}{(29)} by
\begin{gather*}
\Prod \frac{1 - q^{8h}}{1 - q^{8h}},\\
\intertext{we have}
\frac{f(q)}{f(q^{4})} = \Prod \frac{1 - q^{8h}}{1 - q^{2h}}.
\end{gather*}
%% -----File: 083.png---Folio 77-------

Now in this equation, by successive substitutions of~$q^{4}$ for~$q$,
we get
\[
\begin{array}{r@{}l}
\dfrac{f(q^{4})}{f(q^{16})}   &{}= \Prod \dfrac{1 - q^{32h} }{1 - q^{8h}}; \\\\
\dfrac{f(q^{16})}{f(q^{64})}  &{}= \Prod \dfrac{1 - q^{128h}}{1 - q^{32h}}; \\\\
\dfrac{f(q^{64})}{f(q^{256})} &{}= \Prod \dfrac{1 - q^{512h}}{1 - q^{128h}}; \\\\
\Dots{2} \\\\
\end{array}
\]

Now $q$ being less than~$1$, $q^{n}$~tends towards the limit~$0$ as $n$~increases,
and consequently $1-q^{n}$ tends towards the limit~$1$.
Also, from \Eqref{eq.}{VIII}{(8)}, Chap.~VIII, we see that $f(0) = 1$. Hence,
multiplying the above equations together member by member,
we have
\begin{align}
\Tag{(30)}
f(q) &= \Prod \frac{1}{1-q^{2h}}, \\\\
\intertext{or}
\Tag{(31)}
A &= \frac{1}{(1 - q^{2})(1 - q^{4})(1 - q^{6}) \dotsm}.
\end{align}

Substituting this value in \Eqref{equation}{VIII}{(8)}, Chap.~VIII, we have,
after making $u = 0$,
\begin{align}
(1 - q)^{2}(1 - q^{3})^{2}(1 - q^{5})^{2} \dotsm
  &= \frac{1- 2q + 2q^{4} - 2q^{9} + \dotsb}
          {(1 - q^{2})(1 - q^{4})(1 - q^{6}) \dotsm} \\\\
  &= \frac{\Theta (0)}{(1 - q^{2})(1 - q^{4})(1 - q^{6}) \dotsm}.
\end{align}

(See \Eqref{equation}{VIII}{(9)}, Chap.~VIII.)

Transposing one of the series of products from the left-hand
member, we get
\[
(1 - q)(1 - q^{3}) \dotsm
  = \frac{\Theta (0)}{(1 - q)(1 - q^{2})(1 - q^{3})(1 - q^{4}) \dotsm}.
\]
%% -----File: 084.png---Folio 78-------

Introducing on both sides of the equation the factors $1 - q^{2}$,
$1 - q^{4}$, $1 - q^{6}$,~etc., we get
\begin{align}
(1 - q) &(1 - q^{2})(1 - q^{3})(1 - q^{4}) \dotsm \\\\
  &= \Theta (0) \frac{1 - q^{2}}{1 - q}
              · \frac{1 - q^{4}}{1 - q^{2}}
              · \frac{1 - q^{6}}{1 - q^{3}}
              · \frac{1 - q^{8}}{1 - q^{4}} \dotsm \\\\
  &= \Theta (0) (1 + q)(1 + q^{2})(1 + q^{3}) \dotsm;
\intertext{whence}
\Tag{(32)}
\Theta (0)
  &= \frac{(1 - q)(1 - q^{2})(1 - q^{3})\DPtypo{}{\dotsm}}
          {(1 + q)(1 + q^{2})(1 + q^{3})\DPtypo{}{\dotsm}}.
\end{align}

Resuming \Eqref{equation}{VII}{(20)}, Chap.~VII, and dividing both
members of the equation by~$u$, we have
\[
\frac{\sn u}{u}
  = \frac{2 \sqrt[4]{q}}{\sqrt{k}}\,
    \frac{\sin \dfrac{\pi u}{2K}}{u}
    \Prod \frac{1 - 2q^{2h}   \cos \dfrac{\pi u}{K} + q^{4h}}
               {1 - 2q^{2h-1} \cos \dfrac{\pi u}{K} + q^{4h-2}}.
\]
This, for~$u = 0$, since the limiting value of $\dfrac{\sn u}{u}$ for~$u = 0$ is~$1$,
and of $\dfrac{\sin \dfrac{\pi u}{2K}}{u}$ for~$x=0$ is~$\dfrac{\pi}{2K}$, becomes
\begin{align}
1 &= \frac{\sqrt[4]{q}}{\sqrt{k}} · \frac{\pi}{K}
   · \frac{(1 - q^{2})^{2}(1 - q^{4})^{2}(1 - q^{6})^{2} \dotsm}
          {(1 - q)^{2}(1 - q^{3})^{2}(1 - q^{5})^{2} \dotsm},
\intertext{or}
\Tag{(33)}
\frac{\sqrt{k} K}{\pi \sqrt[4]{q}}
  &= \left[\frac{(1 - q^{2})(1 - q^{4})(1 - q^{6}) \dotsm}
                {(1 - q)(1 - q^{3})(1 - q^{5}) \dotsm}\right]^{2}.
\end{align}

Further, from \Eqref{equation}{VII}{(21)}, Chap.~VII, for~$u=0$, we have
\[
\Tag{(34)}
\frac{\sqrt{k}}{2\sqrt{k'} \sqrt[4]{q}}
  = \left[\frac{(1 + q^{2})(1 + q^{4})(1 + q^{6}) \dotsm}
               {(1 - q)(1 - q^{3})(1 - q^{5}) \dotsm}\right]^{2}.
\]
%% -----File: 085.png---Folio 79-------

The quotient of these two equations gives
\[
\Tag{(35)}
\frac{2\sqrt{k'}K}{\pi}
  = \left[\frac{(1 - q^{2})(1 - q^{4})(1 - q^{6}) \dotsm}
               {(1 + q^{2})(1 + q^{4})(1 + q^{6}) \dotsm}\right]^{2};
\]
or, substituting the value of~$\sqrt{k'}$ from \Eqref{eqs.}{VII}{(18)} and~\Eqref{}{VII}{(19)}, Chap.~VII,
\[
\Tag{(36)}
\frac{2k'K}{\pi}
  = \left[\frac{(1 - q)(1 - q^{2})(1 - q^{3}) \dotsm}
               {(1 + q)(1 + q^{2})(1 + q^{3}) \dotsm}\right]^{2}.
\]

Comparing this with \Eqref{equation}{}{(32)}, we easily get
\[
\Tag{(37)}
\Theta (0) = \sqrt{\frac{2k'K}{\pi}}.
\]

From \Eqref{equation}{VIII}{(9)}, Chap.~VIII, making~$u=K$, we get
\[
\Tag{(38)}
\Theta (K) = 1 + 2q + 2q^{4} + 2q^{9} + 2q^{16} + \dotsb.
\]

Making $z=0$ in \Eqref{equation}{IX}{(24)}, Chap.~IX, we have
\[
\Tag{(39)}
\Theta_{1} (0) = 1 + 2q + 2q^{4} + 2q^{9} + \dotsb.
\]

This might also have been derived from \Eqref{eq.}{}{(38)} by observing
that
\[
\DPtypo{\Theta_{1}}{\Theta} (0 + K) = \Theta_{1}(0) = \Theta (K).
\]
Knowing $\Theta (0)$, it is easy to deduce $\Theta (K)$~and~$\Eta (K)$.

From \Eqref{equation}{}{(7)} we have
\[
\dn u = \sqrt{k'}\, \frac{\Theta (u + K)}{\Theta (u)}.
\]

Making $u=0$, we have, since $\dn (0) = 1$,
\[
\Tag{(40)}
\Theta (K) = \frac{\Theta (0)}{\sqrt{k'}}.
\]
%% -----File: 086.png---Folio 80-------

From \Eqref{equation}{}{(5)} we get, in the same manner,
\[
\Tag{(41)}
\Eta (K) = \sqrt{\frac{k'}{k}}\, \Theta (0).
\]

From \Eqref{eq.}{IX}{(12)}, Chap.~IX, we have
\[
\Tag[41st]{(41)^*}
\dn u
   = \sqrt{1 - k^{2} \sin^{2} \phi}
   = \sqrt{k'}\, \frac{\Theta_{1}(u)}{\Theta (u)};
\]
and putting $x = \dfrac{\pi u}{2K}$, we have
\[
\Tag{(42)}
\frac{\dn u}{\sqrt{k'}}
  = \frac{1 + 2q \cos 2x + 2q^{4} \cos 4x + 2q^{9} \cos 6x + \dotsb}
         {1 - 2q \cos 2x + 2q^{4} \cos 4x - 2q^{9} \cos 6x + \dotsb}.
\]

Putting
\[
\Tag[42st]{(42)^*}
\frac{\dn u}{\sqrt{k'}} = \cot \gamma,
\]
we have
\[
\frac{\cot \gamma - 1}{\cot \gamma + 1}
  = \tan (45° - \gamma)
  = 2q \frac{\cos2x + q^{8}(4 \cos^{3} 2x - 3 \cos 2x) + \dotsb}
            {1 + q^{4}(4 \cos^{2} 2x - 2)};
\]
whence
\begin{multline*}
\Tag{(43)}
\cos 2x = \frac{\tan (45° - \gamma) [1 + q^{4}(4 \cos^{2}2x - 2)]}{2q} \\\\
  - q^{8}(4 \cos^{3}2x - 3\cos2x) - \dotsb,
\end{multline*}
and approximately,
\[
\Tag{(44)}
\cos 2x = \frac{\tan (45° - \gamma)}{2q}.
\]

From \Eqref{equations}{IX}{(37)} and~\Eqref{}{IX}{(40)}, Chap.~IX, we have
\begin{align}
\Tag{(45)}
x &= \frac{u}{\Theta^{2}(K)}; \\\\
\intertext{whence}
\Tag{(46)}
u &= x\Theta^{2}(K).
\end{align}
%% -----File: 087.png---Folio 81-------


