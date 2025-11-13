# Chapter II: Elliptic Functions.

Lines: 833-1186

\Chapter{II}{Elliptic Functions.}

\begin{DPgather*}
\lintertext{\indent\First{Let}}
u = \int_0^\phi \frac{d\phi}{\sqrt{1 - k^2 \sin^2 \phi}}.
\end{DPgather*}

$\phi$\footnotemark~is called the *amplitude* corresponding to the *argument*~$u$,
and is written
\footnotetext{Legendre.}
\[
\phi = \am (u, k) = \am u.
\]

The quantity~$k$ is called the *modulus*, and the expression
$\sqrt{1 - k^2 \sin^2 \phi}$ is written\footnotemark[1]
\[
\sqrt{1 - k^2 \sin^2 \phi} = \Delta \am u = \Delta \phi,
\]
and is called the *delta function* of the amplitude of~$u$, or \emph{delta
of~$\phi$}, or simply *delta*~$\phi$.

$u$~can be written
\[
u = F(k, \phi).
\]

The following abbreviations are used:
\begin{align}
\sin \phi &= \sin \am u = \sn\footnotemark u; \\\\
\cos \phi &= \cos \am u = \cn\footnotemark[2] u; \\\\
\Delta \phi &= \Delta \am u = \dn\footnotemark[2] u = \Delta u; \\\\
\tan \phi &= \tan \am u = \tn u.
\end{align}
\footnotetext{\textit{Gudermann}, in his ``Theorie der Modularfunctionen'': Crelle's Journal,
  Bd.~18.}%

Let $\phi$ and~$\psi$ be any two arbitrary angles, and put
\begin{align}
\phi &= \am u;\\
\psi &= \am \nu.\\
\end{align}
%% -----File: 023.png---Folio 17-------

%[Illustration]
\begin{wrapfigure}{r}{1.25in}
  \Input[1in]{023a}
\end{wrapfigure}
In the spherical triangle~$ABC$ we have from
Trigonometry, $\DPtypo{c}{\mu}$~and~$C$ being constant,
\[
\frac{d\phi}{\cos B} + \frac{d\psi}{\cos A} = 0.
\]

Since $C$~and~$\DPtypo{c}{\mu}$ are constant, denoting by~$k$ an arbitrary constant,
we have
\[
\Tag{(1)}
\frac{\sin C}{\sin \mu} = k.
\]

But
\[
\sin A
  = \sin\psi \frac{\sin B}{\sin \phi}
  = \sin\psi \frac{\sin C}{\sin \mu}
  = k \sin\psi.
\]

Whence
\[
\cos A
  = \sqrt{1 - \sin^{2}A}
  = \sqrt{1 - k^{2} \sin^{2} \psi}.
\]

In the same manner
\[
\cos B
  = \sqrt{1 - \sin^{2}B}
  = \sqrt{1 - k^{2} \sin^{2} \phi}.
\]

Substituting these values, we get
\[
\Tag{(2)}
\frac{d\phi}{\sqrt{1 - k^{2} \sin^{2} \phi}} +
\frac{d\psi}{\sqrt{1 - k^{2} \sin^{2} \psi}} = 0.
\]

Integrating this, there results
\[
\Tag{(3)}
\int_0^\phi \frac{d\phi}{\sqrt{1 - \DPtypo{k_2}{k^2} \sin^{2}\phi}} +
\int_0^\psi \frac{d\psi}{\sqrt{1 - k^2 \sin^2\psi}} = \text{const}.
\]

When $\phi = 0$, we have $\psi = \mu$, and therefore the constant
must be of the form
\[
\int_0^\mu \frac{d\phi}{\sqrt{1 - k^2 \sin^2 \phi}},
\]
%% -----File: 024.png---Folio 18-------
whence
\[
\Tag{(4)}
\int_0^\phi \frac{d \phi}{\sqrt{1 - k^2 \sin^2 \phi}} +
\int_0^\psi \frac{d \psi}{\sqrt{1 - k^2 \sin^2 \psi}} =
\int_0^\mu  \frac{d \phi}{\sqrt{1 - k^2 \sin^2 \phi}},
\]
or
\[
u + \nu = m;
\]
and evidently the amplitudes $\phi$,~$\psi$, and~$\mu$ can be considered as
the three sides of a spherical triangle, and the relations between
the sides of this spherical triangle will be the same as those
between $\phi$,~$\psi$, and~$\mu$.

%[Illustration]
\begin{wrapfigure}{l}{1.125in}
  \Input{024a}
\end{wrapfigure}
But the sides of this triangle have imposed upon them the
condition
\[
\frac{\sin C}{\sin \mu} = k;
\]
and since $k < 1$, we must have $\mu > C$, which requires that one
of the angles of the triangle shall be obtuse and the other two
acute.

In the figure, let $C$~be an acute angle of the triangle~$ABC$,
and $PQ$~the equatorial great circle of which $C$~is the pole.

%[Illustration]
\ifthenelse{\boolean{ForPrinting}}{%
  \begin{wrapfigure}[11]{r}{2.125in}
    \vspace{-1.5\baselineskip}
    \hfill\Input[2in]{025a}
    \vspace{1.5\baselineskip}
  \end{wrapfigure}
}{%
  \begin{wrapfigure}{r}{2.125in}
    \hfill\Input[2in]{025a}
  \end{wrapfigure}
}
The arc~$PQ$ will be the measure of the angle~$C$.

Let $AG$~and~$AH$ be the arcs of two great
circles perpendicular respectively to $CQ$ and~$CP$.
They will of course be shorter than~$PQ$.
Hence $AB = \mu$ must intersect~$CQ$ in points
between $CG$ and~$HQ$, since $\mu > (C=PQ)$. In
any case either $A$~or~$B$ will be obtuse according
as $B$~falls between $QH$ or~$CG$ respectively; and
the other angle will be acute.

In the case where $C$~is an obtuse angle, it will be easily seen
that the angle at~$A$ must be acute, since the great circle~$AD$,
perpendicular to~$CP$, intersects~$PQ$ in~$D$, $PD$~being a quadrant.
The same remarks apply to the angle~$B$. Hence, in either
%% -----File: 025.png---Folio 19-------
case, one of the angles of the triangle is
obtuse and the other two are acute, as
a result of the condition
\[
\frac{\sin C }{\sin \mu} = k < 1.
\]

From Trigonometry we have
\[
\cos \mu = \cos \phi \cos \psi + \sin \phi \sin \psi \cos C;
\]
and since the angle~$C$ is obtuse,
\[
\cos C = - \sqrt{1- \sin^2C} = -\sqrt{1 - k^2 \sin^2 \mu},
\]
and
\[
\Tag{(5)}
\cos \mu = \cos \phi \cos \psi - \sin \phi \sin \psi \sqrt{1 - k^2 \sin^2 \mu},
\]
the relation sought.

The spherical triangle likewise gives the following relations
between the sides:
\[
\Tag[5st]{(5)^*}
\left\{
\begin{aligned}
\cos \phi &= \cos \mu \cos \psi + \sin \mu \sin \psi \sqrt{1 - k^2 \sin^2 \phi}; \\\\
\cos \psi &= \cos \mu \cos \phi + \sin \mu \sin \phi \sqrt{1 - k^2 \sin^2 \psi}.
\end{aligned}
\right.
\]

These give, by eliminating $\cos \mu$,
\[
\sin \mu = \frac{\cos^2 \psi - \cos^2 \phi}
                {\sin \phi \cos \psi \Delta \psi - \sin \psi \cos \phi \Delta \phi};
\]
which, after multiplying by the sum of the terms in the denominator
and substituting $\cos^2 = 1 - \sin^2$, can be written
\[
\sin \mu
  = \frac{(\sin^2 \phi - \sin^2 \psi)
          (\sin \phi \cos \psi \Delta \psi + \sin \psi \cos \phi \Delta \phi \DPtypo{}{)}}
         { \sin^2 \phi \cos^2 \psi \Delta^2 \psi - \sin^2 \psi \cos^2 \phi \Delta^2 \phi}.
\]

Since the denominator can be written
\begin{gather*}
(\sin^2 \phi - \sin^2 \psi)(1 - k^2 \sin^2 \phi \sin^2 \psi), \\\\
\Tag{(6)}
\sin \mu = \frac{\sin \phi \cos \psi \Delta \psi
               + \sin \psi \cos \phi \Delta \phi}
                {1 - k^2 \sin^2 \phi \sin^2 \psi}.
\end{gather*}

In a similar manner we get
\[
\Tag[6st]{(6)^*}
\left\{
\begin{aligned}
\cos \mu   &= \frac{\cos \phi \cos \psi - \sin \phi \sin \psi \Delta \phi \Delta \psi}
                   {1 - k^2 \sin^2 \phi \sin^2 \psi}; \\\\
%
\Delta \mu &= \frac{\Delta \phi \Delta \psi - k^2 \sin \phi \sin \psi \cos \phi \cos \psi}
                   {1 - k^2 \sin^2 \phi \sin^2 \psi}.
\end{aligned}
\right.
\]
%% -----File: 026.png---Folio 20-------

These equations can also be written as follows:
\[
\Tag{(7)}
\left\{
\makebox[\linewidth-40pt][l]{$\begin{aligned}
\sin \am (u±\nu)
  &= \frac{\sin \am u \cos \am \nu \Delta \am \nu
         ± \sin \am \nu \cos \am u \Delta \am u}
          {1 - k^{2} \sin^{2} \am u \sin^{2} \am \nu}; \\\\
%
\cos \am (u±\nu)
  &= \frac{\cos \am u \cos \am \nu
       \mp \sin \am u \sin \am \nu \Delta \am u \Delta \am \nu}
          {1 - k^{2} \sin^{2} \am u \sin^{2} \am \nu}; \\\\
%
\Delta \am (u±\nu)
  &= \frac{\Delta \am u \Delta \am \nu
       \mp k^{2} \sin \am u \sin \am \nu \cos \am u \cos \am \nu}
          {1 - k^{2} \sin^{2} \am u \sin^{2} \am \nu};
\end{aligned}$}
\right.
\]
or
\[
\Tag{(8)}
\left\{
\begin{aligned}
\sn (u±\nu)
  &= \frac{\sn u \cn \nu \dn \nu ± \sn \nu \cn u \dn u}
          {1 - k^{2} \sn^{2} u \sn^{2} \nu}; \\\\
%
\cn (u±\nu)
  &= \frac{\cn u \cn \nu \mp \sn u \sn \nu \dn u \dn \nu}
          {1 - k^{2} \sn^{2} u \sn ^{2} \nu}; \\\\
%
\dn (u±\nu)
  &= \frac{\dn u \dn \nu \mp k^{2} \sn u \sn \nu \cn u \cn \nu}
          {1 - k^{2} \sn^{2} u \sn^{2} \nu}.
\end{aligned}
\right.
\]

Making $u = \nu$, we get from the upper sign
\[
\Tag{(9)}
\left\{
\begin{aligned}
\sn 2u &= \frac{2 \sn u \cn u \dn u}{1 - k^{2} \sn^{4} u}; \\\\
\cn 2u &= \frac{\cn^{2}u - \sn^{2}u \dn^{2}u}{1 - k^{2} \sn^{4}u}
        = \frac{1 - 2\sn^{2}u + k^{2}\sn^{4}u}{1 - k^{2}\sn^{4}u}; \\\\
\dn 2u &= \frac{\dn^{2}u - k^{2}\sn^{2}u \cn^{2}u}{1 - k^{2}\sn^{4}u}
        = \frac{1 - 2k^{2}\sn^{2}u + k^{2}\sn^{4}u}{1 - k^{2}\sn^{4}u}.
\end{aligned}
\right.
\]

From these
\[
\Tag{(10)}
\left\{
\begin{aligned}
1 - \cn 2u &= \frac{2 \cn^{2} u \dn^{2} u}{1 - k^{2} \sn^{4} u}; \\\\
1 + \cn 2u &= \frac{2 \cn^{2} u}{1 - k^{2} \sn^{4} u}; \\\\
1 - \dn \PadTo[l]{2u}{u}  &= \frac{2k^{2} \sn^{2} u \cn^{2} u}{1 - k^{2} \sn^{4} u}; \\\\
1 + \dn \PadTo[l]{2u}{u}  &= \frac{2 \dn^{2} u}{1 - k^{2} \sn^{4} u};
\end{aligned}
\right.
\]
%% -----File: 027.png---Folio 21-------
and therefore
\[
\Tag{(11)}
\left\{
\begin{aligned}
\sn^{2} u &= \frac{1 - \cn 2u}{1 + \dn 2u}; \\\\
\cn^{2} u &= \frac{\dn 2u + \cn 2u}{1 + \dn 2u}; \\\\
\dn^{2} u &= \frac{1 - k^{2} + \dn 2u + k^{2}\cn 2u}{1 +\dn 2u};
\end{aligned}
\right.
\]
and by analogy
\[
\Tag{(12)}
\left\{
\begin{aligned}
\sn \dfrac{u}{2} &= \sqrt{\frac{1 - \cn u}{1 + \dn u}}; \\\\
\cn \dfrac{u}{2} &= \sqrt{\frac{\cn u + \dn u}{1 + \dn u}}; \\\\
\dn \dfrac{u}{2} &= \sqrt{\frac{1 - k^{2} + \dn u + k^{2} \cn u}{1 + \dn u}}.
\end{aligned}
\right.
\]

In \Eqref{equations}{}{(7)} making $u = \nu$, and taking the lower sign,
we have
\[
\Tag{(13)}
\left\{
\begin{aligned}
\sn 0 &= 0; \\\\
\cn 0 &= 1; \\\\
\dn 0 &= 1.
\end{aligned}
\right.
\]

Likewise, we get by making $u = 0$,
\[
\Tag{(14)}
\left\{
\begin{aligned}
\sn (-u) &= -\sn u; \\\\
\cn (-u) &= +\cn u; \\\\
\dn (-u) &= \dn u.
\end{aligned}
\right.
\]
%% -----File: 028.png---Folio 22-------


