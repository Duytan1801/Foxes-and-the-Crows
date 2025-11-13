# Chapter I: Elliptic Integrals.

Lines: 337-832

\Chapter{I}{Elliptic Integrals.}

\First{The} integration of irrational expressions of the form
\begin{gather*}
X\, dx \sqrt{A + Bx + Cx^{2}},\\
\intertext{or}
\frac{X\, dx}{\sqrt{A + Bx + Cx^{2}}},
\end{gather*}
$X$ being a rational function of~$x$, is fully illustrated in most elementary
works on Integral Calculus, and shown to depend upon
the transcendentals known as logarithms and circular functions,
which can be calculated by the proper logarithmic and trigonometric
tables.

When, however, we undertake to integrate irrational expressions
containing higher powers of~$x$ than the square, we meet
with insurmountable difficulties. This arises from the fact that
the integral sought depends upon a new set of transcendentals,
to which has been given the name of *elliptic functions*, and
whose characteristics we will learn hereafter.

The name of Elliptic Integrals has been given to the simple
integral forms to which can be reduced all integrals of the form
\[
\Tag{(1)}
V = \int F(X, R)\, dx,
\]
where $F(X, R)$ designates a rational function of $x$~and~$R$, and
$R$~represents a radical of the form
\[
R = \sqrt{Ax^{4} + Bx^{3} + Cx^{2} + Dx + E},
\]
%% -----File: 011.png---Folio 5-------
where $A$,~$B$,~$C$, $D$,~$E$ indicate constant coefficients.

We will show presently that all cases of \Eqref{Eq.}{}{(1)} can be
reduced to the three typical forms
\[
\Tag{(2)}
\begin{aligned}
&\int_{0}^{x} \frac{dx}{\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}}, \\\\
&\int_{0}^{x} \frac{x^{2}\, dx}{\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}},\\
&\int_{0}^{x} \frac{dx}{(x^{2} + a) \sqrt{(1 - x^{2})(1 - k^{2}x^{2})}},
\end{aligned}
\]
which are called elliptic integrals of the first, second, and third
order.

Why they are called *Elliptic* Integrals we will learn further
on. The transcendental functions which depend upon these
integrals, and which will be discussed in \Chapref{Chapter}{IV}, are called *Elliptic Functions*.

The most general form of \Eqref{Eq.}{}{(1)} is
\[
\Tag{(3)}
V = \int \frac{A + BR}{C + DR}\, dx;
\]
where $A$,~$B$,~$C$, and~$D$ stand for rational integral functions of~$x$.

$\dfrac{A + BR}{C + DR}$ can be written
\begin{align}
\frac{A + BR}{C + DR}
  &= \frac{AC - BDR^{2}}{C^{2} - D^{2}R^{2}}
   - \frac{(AD - CB)R^{2}}{C^{2} - D^{2}R^{2}} · \frac{1}{R}\\
  &= N - \frac{P}{R};
\end{align}
%% -----File: 012.png---Folio 6-------
$N$~and~$P$ being rational integral functions of~$x$. Whence \Eqref{Eq.}{}{(3)}
becomes
\[
\Tag{(4)}
V = \int N\, dx - \int \frac{P\, dx}{R}.
\]

\Eqref{Eq.}{}{(4)} shows that the most general form of~$V$ can be made
to depend upon the expressions
\[
\Tag{(5)}
V' = \int \frac{P\, dx}{R},
\]
and
\[
\int N\, dx.
\]

This last form is rational, and needs no discussion here.

We can write
\begin{align}
P &= \frac{G_{0} + G_{1}x + G_{2}x^{2} + \dotsb}
          {H_{0} + H_{1}x + H_{2}x^{2} + \dotsb} \\\\
  &= \frac{G_{0} + G_{2}x^{2} + G_{4}x^{4} + \dotsb + (G_{1} + G_{3}x^{2} + \dotsb)x}
          {H_{0} + H_{2}x^{2} + H_{4}x^{4} + \dotsb + (H_{1} + H_{3}x^{2} + \dotsb)x}.
\end{align}
Multiplying both numerator and denominator by
\[
H_{0} + H_{2}x^{2} + H_{4}x^{4} + \dotsb - (H_{1} + H_{3}x^{2} + H_{5}x^{4} + \dotsb)x,
\]
we have a new \DPtypo{numerator}{denominator} which contains only powers of~$x^{2}$.
The result takes the following form:
\begin{align}
P &= \frac{M_{0} + M_{2}x^{2} + M_{4}x^{4} + \dotsb
        + (M_{1} + M_{3}x^{2} + M_{5}x^{4} + \dotsb)x}
          {N_{0} + N_{2}x^{2} + N_{4}x^{4} + N_{6}x^{6} + \dotsb} \\\\
  &= \Phi(x^{2}) + \Psi(x^{2})·x.
\end{align}

\Eqref{Equation}{}{(5)} thus becomes
\[
\Tag{(6)}
V' = \int \frac{\Phi(x^{2})\, dx}{R} + \int \frac{\Psi(x^{2}) · x · dx}{R}.
\]
%% -----File: 013.png---Folio 7-------

We shall see presently that $R$ can always be assumed to be
of the form
\[
\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}.
\]

Therefore, putting $x^{2} = z$, the second integral in \Eqref{Eq.}{}{(6)}
takes the form
\[
\frac{1}{2} \int \frac{\Psi(z) · dz}{\sqrt{(1 - z)(1 - k^{2}z)}},
\]
which can be integrated by the well-known methods of Integral
Calculus, resulting in logarithmic and circular transcendentals.

There remains, therefore, only the form
\[
\int \frac{\Phi(x^{2})\, dx}{R}
\]
to be determined.

We will now show that $R$ can always be assumed to be in
the form
\[
\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}.
\]
We have
\begin{align}
R &= \sqrt{Ax^{4} + Bx^{3} + Cx^{2} + Dx + E} \\\\
  &= \sqrt{G(x - a)(x - b)(x - c)(x - d)},
\end{align}
$a$,~$b$,~$c$, and~$d$ being the roots of the polynomial of the fourth
degree, and $G$~any number, real or imaginary, depending upon
the coefficients in the given polynomial.

Substituting in \Eqref{equation}{}{(1)}
\begin{align}
x &= \frac{p + qy}{1 + y}, \\\\
\intertext{we have}
\Tag{(7)}
V &= \int \phi(y, \rho)\, dy,
\end{align}
%% -----File: 014.png---Folio 8-------
$\rho$~designating the radical
\[
\rho = \sqrt{G[p - a + (q - a)y]
              [p - b + (q - b)y]
              [p - c + (q - c)y]\DPtypo{}{\dotsm}} \DPtypo{\dotsm}{\;}.
\]

In order that the odd powers of~$y$ under the radical may
disappear we must have their coefficients equal to zero; i.e.,
\begin{align}
(p - a)(q - b) + (p - b)(q - a) &= 0, \\\\
(p - c)(q - d) + (p - d)(q - c) &= 0;
\end{align}
whence
\begin{align}
2pq - (p + q)(a + b) + 2ab &= 0, \\\\
2pq - (p + q)(c + d) + 2cd &= 0,
\end{align}
and
\[
\Tag{(8)}
\left\{
\begin{aligned}
pq    &= \frac{ab(c + d) - cd(a + b)}{a + b - (c + d)}, \\\\
p + q &= \frac{2ab - 2cd}{a + b - (c + d)}.
\end{aligned}
\right.
\]
\Eqref{Equation}{}{(8)} shows that $p$ and~$q$ are real quantities, whether
the roots $a$,~$b$,~$c$, and~$d$ are real or imaginary; $a$,~$b$, and $c$,~$d$ being
the conjugate pairs.

Hence \Eqref{equation}{}{(1)} can always be reduced to the form of
\Eqref{equation}{}{(7)}, which contains only the second and fourth powers
of the variable.

This transformation seems to fail when $a + b - (c + d) = 0$;
but in that case we have
\[
R = \sqrt{G[x^{2} - (a + b)x + ab][x^{2} - (a + b)x + cd]},
\]
and substituting
\[
x = y - \frac{a + b}{2}
\]
will cause the odd powers of~$y$ to disappear as before.

If the radical should have the form
\[
\sqrt{G(x - a)(x - b)(x - c)},
\]
%% -----File: 015.png---Folio 9-------
placing $x = y^{2} + a$, we get
\begin{align}
V    &= \int \phi(y, \rho)\, dy, \\\\
\rho &= \sqrt{G(y^{2} + a - b)(y^{2} + a - c)},
\end{align}
$\phi$~designating a rational function of $y$~and~$\rho$.

Thus all integrals of the form contained in \Eqref{equation}{}{(1)}, in
which $R$~stands for a quadratic surd of the third or fourth
degree, can be reduced to the form
\[
\Tag{(9)}
V = \int \phi(x, R)\, dx,
\]
$R$~designating a radical of the form
\[
\sqrt{G(1 + mx^{2})(1 + nx^{2})},
\]
$m$~and~$n$ designating constants.

It is evident that if we put
\[
x' = x\sqrt{-m},\quad k^{2} = -\frac{n}{m},
\]
we can reduce the radical to the form
\[
\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}.
\]

We shall see later on that the quantity~$k^{2}$, to which has
been given the name *modulus*, can always be considered real
and less than unity.

Combining these results with \Eqref{equation}{}{(6)}, we see that the
integration of \Eqref{equation}{}{(1)} depends finally upon the integration
of the expression
\[
\Tag{(10)}
V'' = \int \frac{\phi(x^{2})\, dx}{\sqrt{(1 - x^{2})(1 - k^{2}x^{2})}}
  = \int \frac{\phi(x^{2})\, dx}{R}.
\]
%% -----File: 016.png---Folio 10-------

The most general form of~$\phi(x^{2})$ is
\begin{align}
\phi(x^{2})
  &= \frac{M_{0} + M_{2}x^{2} + M_{4}x^{4} + \dotsb}
          {N_{0} + N_{2}x^{2} + N_{4}x^{4} + \dotsb} \\\\
  &= P_{0} + P_{2}x^{2} + P_{4}x^{4} + P_{6}x^{\DPtypo{2}{6}} + \dotsb \\\\
  &+ \sum \frac{L}{(x^{2} + a)^{n}}. %[** PP: Textstyle sums in original]
\end{align}

Hence
\[
\Tag{(11)}
V'' = \sum P \int \frac{x^{2m}\, dx}{R}
    + \sum L \int \frac{dx}{(x^{2} + a)^{n}\, R}.
\]

But $\displaystyle\int \frac{x^{2m}\, dx}{R}$ depends upon $\displaystyle\int \frac{dx}{R}$ and $\displaystyle\int \frac{x^{2}\, dx}{R}$, which can
be shown as follows:

Differentiating $Rx^{2m-3}$, we have
\begin{align}
d[x^{2m-3}R]
  &= d\left[x^{2m-3} \sqrt{\alpha + \beta x^{2} + \gamma x^{4}}\right] \\\\
  &= (2m - 3)x^{2m-4}\, dx \sqrt{\alpha + \beta x^{2} + \gamma x^{4}}
%\end{aligned} \\\\
   + \frac{x^{2m-3}(\beta x + 2\gamma x^{3})\, dx}
          {\sqrt{\alpha + \beta x^{2} + \gamma x^{4}}}.
\end{align}
Integrating and collecting, we get
\begin{align}
Rx^{2m-3}
  &= \begin{aligned}[t]
       (2m - 3)\alpha \int \frac{x^{2m-4}\, dx}{R}
    &+ (2m - 2)\beta  \int \frac{x^{2m-2}\, dx}{R} \\\\
    &+ (2m - 1)\gamma \int \frac{x^{2m}\, dx}{R}
    \end{aligned} \\\\
%
\Tag{(12)}
  &= \alpha' \int \frac{x^{2m-4}\, dx}{R}
   + \beta'  \int \frac{x^{2m-2}\, dx}{R}
   + \gamma' \int \frac{x^{2m}\, dx}{R}.
\end{align}
%% -----File: 017.png---Folio 11-------
Whence we get, by taking $m=2$,
\[
\Tag{(13)}
Rx = \alpha \int \frac{dx}{R}
   + \beta  \int \frac{x^{2}\, dx}{R}
   + \gamma \int \frac{x^{4}\, dx}{R},
\]
which shows that the general expression $\displaystyle\int \frac{x^{2m}\, dx}{R}$ can be found
by successive calculations, when we are able to integrate the
expressions
\[
\int \frac{dx}{R}\quad \text{and}\quad \int \frac{x^{2}\, dx}{R},
\]
the first and second of \Eqref{equation}{}{(2)}.

We will now consider the second class of terms in \Eqref{eq.}{}{(11)},
viz., $\dfrac{L\, dx}{(x^{2} + a)^{n}\, R}$.

This second term is as follows:
\begin{align}
\Tag{(14)}
\sum \int \frac{L}{(x^{2} + a)^{n}\, R}
   = \int \frac{A\, dx}{(x^{2} + a)^{n}\, R}
  &+ \int \frac{B\, dx}{(x^{2} + a)^{n-1}\, R} \\\\
  &+ \int \frac{C\, dx}{(x^{2} + a)^{n-2}\, R} + \dotsb
\end{align}

Each of these terms can be shown to depend ultimately
upon terms of the form
\[
\frac{x^{2}\, dx}{R},\quad \frac{dx}{R},\quad \text{and}\quad \frac{dx}{(x^{2} + a)\, R}.
\]

The two former will be recognized as the two ultimate forms
already discussed, the first and second of \Eqref{equation}{}{(2)}. The
third is the third one of \Eqref{equation}{}{(2)}.

This dependence of \Eqref{equation}{}{(14)} can be shown as follows:
%% -----File: 018.png---Folio 12-------

We have
\begin{align}
d\left[\frac{xR}{(x^{2} + a)^{n-1}}\right]
  &= \frac{(x^{2} + a)^{n-1} (x\, dR + R\, dx) - 2x^{2} R(n + 1)(x^{2} + a)^{n-2}\, dx}
          {(x^{2} + a)^{2n-2}} \\\\
  &= \frac{(x^{2} + a)(x\, dR + R\, dx) - 2x^{2} R(n - 1)\, dx}{(x^{2} + a)^{n}}.
\end{align}

Substituting the value of
\[
R  = \sqrt{\alpha + \beta x^{2} + \gamma x^{4}}\quad\text{and}\quad
dR = (\beta x + 2 \gamma x^{3})\, \frac{dx}{R},
\]
we get
\Pagelabel{12}%
\begin{gather*}
\begin{aligned}
&d\left[\frac{xR}{(x^{2} + a)^{n-1}}\right] \\\\ %[** PP: Moving = to next line]
%
&= \frac{(x^{2} + a)(\beta x^{2} + 2 \gamma x^{4} + \alpha + \beta x^{2} + \gamma x^{4})
      - 2x^{2}(n-1)(\alpha + \beta x^{2} + \gamma x^{4})}
     {(x^{2} + a)^{n}} · \frac{dx}{R}
\end{aligned} \\\\
%
\begin{aligned}
&= \frac{\left\{\begin{aligned}
        \bigl(3\gamma - 2(n-1)\gamma\bigr) x^6
      &+ \bigl(2\beta + 3a\gamma - 2(n-1)\beta\bigr) x^4 \\\\
      &+ \bigl(2a\beta + \alpha - 2(n-1)\alpha\bigr) x^2
       + a\alpha\end{aligned}\right\}}
  {(x^{2} + a)^{n}} · \frac{dx}{R} \\\\
%
&= \frac{-(2n - 5)\gamma x^6
      + \bigl(\DPnote{[**A]} - (2n - 4)\beta + 3a\gamma\bigr) x^4
      + \bigl(\DPnote{[**B]} - (2n - 3)\alpha + \DPnote{[**C]} 2a\beta\bigr) x^2
      + a\alpha}
  {(x^{2} + a)^{n}} · \frac{dx}{R};
\end{aligned}
\end{gather*}
%[** PP: This display has been completely re-set. Minor modifications
% were required to maintain algebraic correctness:
% **A & **B: (+ inserted, matching ) immediately precedes x^4, x^2 resp.;
% **C: - typo corrected to +]
or, by substituting in the numerator $x^{2} = z - a$,
\[
= \frac{\left\{\begin{aligned}&- (2n - 5)\gamma z^3 \\\\
        &+ \bigl((2n - 5) 3a\gamma - (2n - 4)\beta + 3a\gamma\bigr) z^2 \\\\
        &+ \bigl(\DPnote{[**D]} - (2n - 5) 3a^2\gamma + (2n - 4) 2a\beta - 6a^2\gamma
                - (2n - 3)\alpha + 2a\beta\bigr) z \\\\
        &+ \bigl((2n - 5)a^3\gamma - (2n - 4) a^2\beta + 3a^3\gamma
                + (2n - 3)a\alpha - 2a^2\beta + a\alpha\bigr)\end{aligned}\right\}}{(x^{2} + a)^{n}} · \frac{dx}{R};
\]
%[**D: (+ inserted, matching ) immediately precedes z]}
%% -----File: 019.png---Folio 13-------
or, after resubstituting $z = x^2 + a$, and integrating,
\begin{align}
\Tag{(15)}
\frac{xR}{(x^2 + a)^{n - 1}}
  &= -(2n - 5)\gamma \int \frac{dx}{(x^2 + a)^{n - 3} R} \\\\
  &\quad -(2n - 4)(\beta - 3a \gamma) \int \frac{dx}{(x^2 + a)^{n - 2} R}\\
  &\quad -(2n - 3)(3 a^2 \gamma - 2a \beta + \alpha) \int \frac{dx}{(x^2 + a)^{n - 1} R}\\
  &\quad +(2n - 2)(a^3 \gamma - a^2 \beta + a \alpha) \int \frac{dx}{(x^2 + a)^n R}.
\end{align}
\begin{align}
= \alpha_{1}  \int \frac{dx}{(x^2 + a)^{n - 3}R}
 + \beta_{1}  \int \frac{dx}{(x^2 + a)^{n - 2}R}
&+ \gamma_{1} \int \frac{dx}{(x^2 + a)^{n - 1}R}\\
&+ \delta_{1} \int \frac{dx}{(x^2 + a)^n R}.
\end{align}
Making $n = 2$, we have
\begin{align}
\Tag{(16)}
\frac{xR}{(x^2 + a)^{\DPtypo{-1}{1}}}
  = \alpha_{1} \int \frac{(x^2 + a)\, dx}{R}
   + \beta_{1} \int \frac{dx}{R}
 &+ \gamma_{1} \int \frac{dx}{(x^2 + a)R} \\\\
 &+ \delta_{1} \int \frac{dx}{(x^2 + a)^2 R}.
\end{align}

\Eqref{Equation}{}{(16)} shows that
\[
\int \frac{dx}{(x^2 + a)^2 R}
\]
depends upon the three forms
\[
\int \frac{x^2\, dx}{R},\quad
\int \frac{dx}{R},\quad \text{and}\quad
\int \frac{dx}{(x^2 + a)R},
\]
%% -----File: 020.png---Folio 14-------
the three types of \Eqref{equation}{}{(2)}, and \Eqref{equation}{}{(15)} shows that
the general form
\[
\int \frac{dx}{(x^2 + a)^n R}
\]
depends ultimately upon the same three types.

We have now discussed every form which the general \Eqref{equation}{}{(1)}
can assume, and shown that they all depend ultimately
upon one or more of the three types contained in \Eqref{equation}{}{(2)}.

These three types are called the three Elliptic Integrals of
the first, second, and third kind, respectively.

Legendre puts $x = \sin \phi$, and reduces the three integrals
to the following forms:
\begin{align}%[** PP: Aligning next three lines]
\Tag{(17)}
F(k, \phi) &=  \int_{0}^{\phi} \frac{d \phi}{\sqrt{1 - k^2 \sin^2 \phi}}; \\\\
&\quad \llap{$\dfrac{1}{k^2}$}
               \int_{0}^{\phi} \frac{d \phi}{\sqrt{1 - k^2 \sin^2 \phi}}
     - \frac{1}{k^2} \int_{0}^{\phi} \sqrt{1 - k^2 \sin^{2} \phi} · d \phi; \\\\
\Tag{(18)}
\varPi(n, k, \phi)
  &= \int_{0}^{\phi} \frac{d \phi}{(1 - n \sin^2 \phi) \sqrt{1 - k^2 \sin^2 \phi}};
\end{align}
the first being Legendre's integral of the first kind; the form
\[
\Tag{(19)}
E(k, \phi) = \int_{0}^{\phi} \sqrt{1 - k^2 \sin^2 \phi} · d \phi
\]
being the integral of the second kind; and the third one being
the integral of the third kind.

The form of the integral of the second kind shows why they
are called Elliptic Integrals, the arc of an elliptic quadrant
being equal to
\[
a \int_{0}^{\frac{\pi}{2}} \sqrt{1 - e^2 \sin^2 \phi} · d\phi,
\]
$\phi$ being the complement of the eccentric angle.
%% -----File: 021.png---Folio 15-------

By easy substitutions, we get from \Eqref{Eqs.}{}{(17)},~\Eqref{}{}{(18)}, and~\Eqref{}{}{(19)}
the following solutions:
\setlength{\TmpLen}{1.5ex}%
\begin{align}
\int_{0}^{\phi} \frac{\sin^2 \phi}{\Delta}\, d\phi
  &= \frac{F - E}{k^2}; \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{\cos^2 \phi}{\Delta}\, d\phi
  &= \frac{E - (1 - k^2)F}{k^2}; \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{\tan^2 \phi}{\Delta}\, d\phi
  &= \frac{\Delta \tan \phi - E}{1 - k^2}; \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{\sec^2 \phi}{\Delta}\, d\phi
  &= \frac{\Delta \tan \phi + (1 - k^2)F - E}{1 - k^2}; \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{1}{\Delta^3}\, d\phi
  &= \frac{1}{1 - k^2} \left(E - \frac{k^2 \sin\phi \cos\phi}{\Delta} \right); \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{\sin^2 \phi}{\Delta^3}\, d\phi
  &= \frac{1}{1 - k^2} \left( \frac{E - (1 - k^2)F}{k^2}
                            - \frac{\sin\phi \cos\phi}{\Delta} \right); \\\\[\TmpLen]
%
\int_{0}^{\phi} \frac{\cos^2 \phi}{\Delta^3}\, d\phi
  &= \frac{F - E}{k^2} + \frac{\sin\phi \cos\phi}{\Delta}.
\end{align}
%% -----File: 022.png---Folio 16-------


