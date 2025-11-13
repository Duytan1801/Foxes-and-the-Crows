# Chapter IV: Landen's Transformation

Lines: 1553-2266

\Chapter{IV}{Landen's Transformation}

%[Illustration]
\begin{wrapfigure}[6]{l}{2in}
  \vspace{-\baselineskip}
  \Input[2in]{036a}
  \vspace{\baselineskip}
  \Pagelabel{30}%
\end{wrapfigure}
\First{Let} $AB$~be the diameter of a circle,
with the centre at~$O$, the radius $AO = r$,
and $C$~a fixed point situated upon~$OB$,
and $OC = k_{0}r$. Denote the angle~$PBC$
by~$\phi$, and the angle~$PCO$ by~$\phi_{1}$. Let
$P'$~be a point indefinitely near to~$P$.

Then
\[
\frac{PP'}{PC} = \frac{\sin PCP'}{\sin PP'C} = \frac{\sin PCP'}{\cos OP'C}.
\]

But $PP' = 2r\, d\phi$, and $\sin PCP' = PCP' = d \phi_{1}$;
therefore
\[
\frac{2r\, d\phi}{PC} = \frac{d \phi_{1}}{\cos OP'C}.
\]

But
\begin{align}
\overline{PC}^{2}
  &= r^{2} + r^{2}k_{0}^{2} + 2r^{2}k_{0} \cos 2 \phi \\\\
  &= (r + rk_{0})^{2} \cos^{2} \phi + (r - rk_{0})^{2} \sin^{2} \phi;
\end{align}
\NegMathSkip
\begin{DPalign}
\lintertext{also}
r^{2} \cos^{2} OP'C
  &= r^{2} - r^{2} \sin^{2} OP'C \\\\
  &= r^{2} - r^{2}k_{0}^{2} \sin^{2} \phi_{1}.
\end{DPalign}

Therefore %[** PP: Next two equations aligned in original]
\[
\frac{2\, d\phi}{\sqrt{(r + rk_{0})^{2} \cos^{2} \phi + \DPtypo{(r - rk_{0})}{(r - rk_{0})^{2}} \sin^{2} \phi}}
  = \frac{d \phi_{1}}{\sqrt{r^{2} - r^{2}k_{0}^{2} \sin^{2} \phi_{1}}},
\]
which can be written
\[
\frac{2}{r + rk_{0}}\,
  \frac{d \phi}{\sqrt{1 - \dfrac{4k_{0}r^{2}}{(r + rk_{0})^{2}} \sin^{2} \phi}}
  = \frac{1}{r}\, \frac{d \phi_{1}}{\sqrt{1 - k_{0}^{2} \sin^{2} \phi_{1}}},
\]
%% -----File: 037.png---Folio 31-------

Putting
\[
\Tag{(1)}
\frac{4k_{0}r^{2}}{(r + rk_{0})^{2}} = \frac{4k_{0}}{(1 + k_{0})^{2}} = k^{2},
\]
we have
\[
\Tag{(2)}
\int_{0}^{\phi} \frac{d \phi}{\sqrt{1 - k^{2} \sin^{2} \phi}}
  = \frac{1 + k_{0}}{2}
    \int_{0}^{\phi_{1}} \frac{d \phi_{1}}{\sqrt{1 - k_{0}^{2} \sin^{2} \phi_{1}}};
\]
no constant being added because $\phi$ and~$\phi_{1}$ vanish simultaneously;
$\phi$ and~$\phi_{1}$ being connected by the equation
\[
\Tag{(3)}
\frac{\sin OPC}{\sin OCP}
  = \frac{\sin (2 \phi - \phi_{1})}{\sin \phi_{1}}
  = \frac{rk_{0}}{r}
  = k_{0}.
\]

From the value of~$k^{2}$ we have
\[
\Tag{(4)}
1 - k^{2} = k'^{2} = \frac{(1 - k_{0})^{2}}{(1 + k_{0})^{2}},
\]
and therefore
\[
\Tag{(5)}
k_{0} = \frac{1 - k'}{1 + k'}.
\]
$k'$~is called the *complementary modulus*, and is evidently the
minimum value of~$\Delta \phi$, the value of~$\Delta \phi$ when~$\phi = 90°$:
\[
\sqrt{1 - k^{2}} = k'.
\]

From \Eqref{eq.}{}{(1)} we evidently have $k > k_{0}$, for, putting \Eqref{eq.}{}{(1)}
in the form
\[
\frac{k^{2}}{k_{0}^{2}} = \frac{4}{k_{0} + 2k_{0}^{2} + k_{0}^{3}},
\]
we see that if $k_{0} = 1$, then $k = k_{0}$, but as $k_{0} < 1$, always, as is
evident from the figure, $k$~must be greater than~$k_{0}$.

It is also evident, from the figure, that~$\phi_{1} > \phi$. Or it may
be deduced directly from \Eqref{eq.}{}{(3)}.

Since $k < 1$, we can write
\[
k = \sin \theta, \qquad k' = \sqrt{1 - k^{2}} = \cos \theta.
\]
%% -----File: 038.png---Folio 32-------

Substituting in \Eqref{eq.}{}{(5)}, we have
\[
k_{0} = \frac{1 - k'}{1 + k'} = \tan^2 \tfrac{1}{2} \theta,
\]
and we can write
\[
k_{0} = \sin \theta_{0}, \qquad k_{1}' = \sqrt{1 - k_{0}^2} = \cos \theta_{0}.
\]

From \Eqref{eq.}{}{(5)} we have
\[
1 + k_{0} = \frac{2}{1 + k'}.
\]

Substituting the value of~$k_{0}$ in that for~$k_{1}'$, we get
\[
k_{1}' = \frac{2\sqrt{k'}}{1 + k'}.
\]

We also have
\begin{DPalign} %[** aligning next group]
2 \phi - \phi_{1} & = \phi - (\phi_{1} - \phi) \\\\
\phi_{1} & = \phi + (\phi_{1} - \phi), \\\\
\lintertext{and, \Eqref{eq.}{}{(3)},}
\sn (2\phi - \phi_{1}) &= k_{0} \sin \phi_{1},
\end{DPalign}
becomes
\begin{multline*} %[** PP: Moving = to second line]
\sin \phi \cos (\phi_{1} - \phi) - \cos \phi \sin (\phi_{1} - \phi) \\\\
= k_{0} \sin \phi \cos (\phi_{1} - \phi) + k_{0} \cos \phi \sin (\phi_{1} - \phi),
\end{multline*}
or
\[
\tan \phi - \tan (\phi_{1} - \phi)
  = k_{0} \tan \phi + k_{0} \tan (\phi_{1} - \phi),
\]
or
\begin{align}
\tan (\phi_{1} - \phi)
  &= \frac{1 - k_{0}}{1 + k_{0}} \tan \phi \\\\
  &= k' \tan \phi.
\end{align}

Collecting these results, we have
\begin{align}
\Tag{(6)}
k &= \frac{2\sqrt{k_{0}}}{1 + k_{0}} = \sin \theta; \\\\
\Tag{(7)}
k_{0}
  &= \frac{1 - k'}{1 + k'}
   = \sin \theta_{0}
   = \tan^{2} \tfrac{1}{2} \theta;
\end{align}
%% -----File: 039.png---Folio 33-------
\begin{align}
\Tag{(8)}
k_{1}' &= \frac{2\sqrt{k'}}{1 + k'} = \cos \theta_{0}; \\\\
\Tag{(9)}
k' &= \frac{1 - k_{0}}{1 + k_{0}} = \cos \theta; \\\\
\Tag{(10)}
1 + k_{0} &= \frac{2}{1 + k'}
   = \frac{2\sqrt{k_{0}}}{k}
   = \frac{k_{1}'}{\sqrt{k'}}
   = \frac{1}{\cos^{2} \frac{1}{2} \theta};
\end{align}
\begin{align}
\Tag{(11)}
\sin (2 \phi - \phi_{1}) &= k_{0} \sin \phi_{1}; \\\\
\Tag{(12)}
\tan (\phi_{1} - \phi) &= k' \tan \phi;
\end{align}
\begin{align}
\Tag{(13)}
\int_{0}^{\phi} \frac{d \phi}{\Delta (k, \phi)}
  &= \frac{1 + k_{0}}{2} \int_{0}^{\phi_{1}} \frac{d \phi_{1}}{\Delta (k_{0}, \phi_{1})}; \\\\
\Tag{(14)}
k &= \sqrt{1 - k'^{2}}, \quad k' = \sqrt{1 - k^{2}}.
\end{align}

Upon examination it will easily appear that $k$ and~$k_{0}$, and $\theta$
and~$\theta_{0}$, are the first two terms of a decreasing series of moduli
and angles; $k'$~and~$k_{1}'$, and $\phi$~and~$\phi_{1}$, of an increasing series;
the law connecting the different terms of the series being deduced
from \Eqref{eqs.}{}{(6)} to~\Eqref{}{}{(12)}.

By repeated applications of these equations we would get
the following series of moduli and amplitudes:
\[
\renewcommand{\arraystretch}{\SMSTR}%
\begin{array}{l*{2}{>{\qquad}l}}
k_{0n} = 0_{(n = \infty)} & k_{n}' = 1_{(n = \infty)} & \phi_{n} \\\\
\PadTo{k_{00}}{\vdots} & \PadTo{k'_n}{\vdots} & \PadTo{\phi_n}{\vdots} \\\\
k_{00} & k_{2}' & \phi_{2} \\\\
k_{0}  & k_{1}' & \phi_{1} \\\\
k & k' & \phi
\end{array}
\]

The upper limit of the one series of moduli is~$1$, and the
lower limit of the other series is~$0$, as is indicated. $k$~and~$k'$,
%% -----File: 040.png---Folio 34-------
which are bound by the relation $k^{2} + k'^{2} = 1$, are called the
*primitives* of the series.

\begin{Remark}
It will be noticed that the successive terms of a decreasing series
are indicated by the sub-accents $0, 00, 03, 04, \ldots 0n$; and the successive terms
of an increasing series by the sub-accents $1, 2, 3, \ldots n$.
\end{Remark}

Again, by application of these equations, we can form a new
series running up from~$k$, viz., $k_{1}, k_{2}, k_{3}, \ldots k_{n} = 1_{(n = \infty)}$; and
also a new series running down from~$k'$, viz., $k_{0}', k'_{00}, \ldots \DPtypo{k_{0n}}{k_{0n}'} =
0_{(n = \infty)}$. So also with~$\phi$.

Collecting these series, we have
\[
\renewcommand{\arraystretch}{\SMSTR}%
\begin{array}{l@{}*{2}{p{1in}l}}
k_{0n} \rlap{$ = 0$} && k_{n}' \rlap{$ = 1$} && \phi_{n} \\\\
\PadTo{k_{00}}{\vdots} && \PadTo{k'_n}{\vdots} && \PadTo{\phi_n}{\vdots} \\\\
k_{02} && k_{2}' && \phi_{2} \\\\
k_{0}  && k_{1}' && \phi_{1} \\\\
k      & \Dots{1} & k' & \Dots{1} & \phi \\\\
k_{1}  && k_{0}' && \phi_{0} \\\\
k_{2}  && k'_{00}&& \phi_{00} \\\\
\PadTo{k_{00}}{\vdots} && \PadTo{k'_n}{\vdots} && \PadTo{\phi_n}{\vdots} \\\\
k_{n} \rlap{$ = 1$} &&  k'_{0n} \rlap{$ = 0$} && \phi_{0n}=0
\end{array}
\]

\begin{Remark}
In practice it will be found that generally $n$ will not need to be very
large in order to reach the limiting values of the terms, often only two or three
terms being needed.
\end{Remark}

Applying \Eqref{eqs.}{}{(7)}, \Eqref{}{}{(12)},~\Eqref{}{}{(13)}, and~\Eqref{}{}{(14)} repeatedly, we get
\[
\Tag[14sub1]{(14_{1})}
\left\{\begin{array}{ll}
k=\sin \theta, & k' = \cos \theta; \\\\
k_{0} = \dfrac{1-k'}{1+k'} = \tan^{2} \frac{1}{2} \theta = \sin \theta_{0}, \qquad & k_{1}' = \cos \theta_{0}; \\\\
k_{00} = \tan^{2} \frac{1}{2} \theta_{0} = \sin \theta_{00}, & k_{2}' = \cos \theta_{00}; \\\\
k_{03} = \tan^{2} \frac{1}{2} \theta_{00} = \sin \theta_{03}, & k_{3}' = \cos \theta_{03}; \\\\
\Dots{2} \\\\
k_{0n} = \tan^{2} \frac{1}{2} \theta_{0(n-1)} = \sin \theta_{0n}, & k_{n}' = \cos \theta_{0n}.
\end{array}\right.
\]
%% -----File: 041.png---Folio 35-------
\begin{align}
\Tag[14sub2]{(14_2)}
&\left\{
\begin{array}{l}
\tan (\phi_{1} - \phi) = k' \tan \phi;\\
\tan (\phi_{2} - \phi_{1}) = k_{1}' \tan \phi_{1};\\
\tan (\phi_{3} - \phi_{2}) = k_{2}' \tan \phi_{2};\\
\Dots{1} \\\\
\tan (\phi_{n} - \phi_{n - 1}) = k'_{(n - 1)} \tan \phi_{n - 1}.
\end{array} \right. \\\\
%
\Tag[14sub3]{(14_3)}
&\left\{
\begin{array}{r@{}l}
F(k, \phi) &{}= \dfrac{1 + k_{0}}{2} F(k_{0}, \phi_{1});\\
F(k_{0}, \phi_{1}) &{}= \dfrac{1 + k_{00}}{2} F(k_{00}, \phi_{2});\\
F(k_{00}, \phi_{2}) &{}= \dfrac{1 + k_{03}}{2} F(k_{03}, \phi_{3});\\
\Dots{2} \\\\
F(k_{0(n - 1)}, \phi_{n - 1}) &{}= \dfrac{1 + k_{0n}}{2} F(k_{0n}, \phi_{n}).
\end{array} \right.
\end{align}

Multiplying these latter equations together, member by
member, we have
\[
\Tag{(15)}
F(k, \phi) = (1 + k_{0})(1 + k_{00}) \dotsm (1 + k_{0n})
  \frac{F(k_{0n}, \phi_{n})}{2^{n}};
\]
$k_{0}$,~$k_{00}$,~etc., and $\phi_{1}$,~$\phi_{2}$,~etc., being determined from the preceding
equations.

From \Eqref{eqs.}{}{(9)} and~\Eqref{}{}{(10)} we get
\[
1 + k_{0}  = \frac{1}{\cos^{2} \frac{1}{2} \theta},\qquad
1 + k_{00} = \frac{1}{\cos^{2} \frac{1}{2} \theta_{0}},\quad \text{etc.}
\]

Substituting these in \Eqref{eq.}{}{(15)}, we get
\[
\Tag{(16)}
F(k, \phi)
  = \frac{1}{\cos^{2} \dfrac{\theta}{2}
             \cos^{2} \dfrac{\theta_{0}}{2} \dotsm
             \cos^{2} \dfrac{\theta_{0n}}{2}}
  · \frac{F(k_{0n}, \phi_{n})}{2^{n}}.
\]
%% -----File: 042.png---Folio 36-------

From \Eqref{eqs.}{}{(15)} and~\Eqref{}{}{(10)} we get
\[
F(k, \phi)
  = \sqrt{\frac{k_{1}' k_{2}' k_{3}' \dotsm k_{n}'^{2}}{k'}}
    · \frac{F(k_{0n}, \phi_{n})}{2^{n}}.
\]
And this with \Eqref{equations}{}{(8)} and~\Eqref{}{}{(9)} gives
\[
\Tag{(17)}
F(k, \phi)
  = \sqrt{\frac{\cos \theta_{0} \cos \theta_{00} \dotsm \cos^{2} \theta_{0n}}{\cos \theta}}
    · \frac{F(k_{0n}, \phi_{n})}{2^{n}}.
\]

Applying \Eqref{equation}{}{(13)} to $(k_{1}, \phi_{0})$, $(k_{2}, \phi_{00})$,~etc., we get
\[
F(k_{1}, \phi_{0}) = \frac{1 + k}{2} F(k, \phi),\ \text{etc.};
\]
but since, \Eqref{eq.}{}{(10)},
\[
\frac{1 + k}{2} = \frac{1}{1 + k_{0}'},\ \text{etc.},
\]
these become
\[
\begin{array}{r@{}l}
F(k, \phi)
  &{} = (1 + k_{0}') F(k_{1}, \phi_{0}); \\\\
F(k_{1}, \phi_{0})
  &{} = (1 + k'_{00}) F(k_{2}, \phi_{00}); \\\\
\Dots{2} \\\\
\llap{$F(k_{n-1}, \phi_{0(n-1)})$}
  &{} = (1 + k'_{0n}) F(k_{\DPtypo{00}{n}}, \phi_{0n});
\end{array}
\]
whence
\[
\Tag{(18)}
F(k, \phi) = (1 + k_{0}')(1 + k'_{00}) \dotsm (1 + k'_{0n})F(k_{n}, \phi_{0n}),
\]
in which $k_{0}'$, $k_{00}'$,~etc., $k_{1}$, $k_{2}$,~etc., $\phi_{0}$, $\phi_{00}$,~etc., are determined
as follows:
\begin{DPalign}
\lintertext{\indent Let}
k &= \sin \theta, \\\\
k_{1} & = \sin \theta_{1}.
\end{DPalign}
From \Eqref{eq.}{}{(10)},
\[
k_{1} = \frac{2\sqrt{k}}{1 + k} \quad \text{or}\quad
\sin \theta_{1} = \frac{2\sqrt{\sin \theta}}{1 + \sin \theta}.
\]
%% -----File: 043.png---Folio 37-------

Solving this equation for~$\sin \theta$, we get
\[
\sin \theta = \tan^{2} \tfrac{1}{2} \theta_{1}.
\]

Hence we can write
\begin{align}
\Tag[18sub1]{(18_{1})}
&\left\{\begin{array}{l}
k = \sin \theta = \tan^{2} \frac{1}{2} \theta_{1}; \\\\
k_{1} = \sin \theta_{1} = \tan^{2} \frac{1}{2} \theta_{2}; \\\\
\Dots{1} \\\\
k_{n} = \sin \theta_{n}.
\end{array}\right. \\\\
\intertext{\indent From \Eqref{equation}{}{(12)} we get}
\Tag[18sub2]{(18_{2})}
&\left\{\begin{array}{l}
\sin (2\phi_{0} - \phi) = k \sin \phi;\footnotemark \\\\
\sin (2\phi_{00} - \phi_{0}) = k_{1} \sin \phi_{0}; \\\\
\Dots{1} \\\\
\rlap{$\sin (2\phi_{0n} - \phi_{0(n-1)}) = k_{n-1} \sin \phi_{0(n-1)}$.}
\end{array}\right.
\end{align}
\footnotetext{When $\sin \phi = 1$ nearly, $\phi$~is best determined as follows: From \Eqref{eq.}{}{(12)}
  we have
  \begin{align}
  \tan (\phi - \phi_{0})
    &= k_{0}' \tan \phi_{0} \\\\
    &= k_{0}' \tan \phi\ \text{nearly};
  \intertext{whence}
  \phi - \phi_{0}
    &= Rk_{0}' \tan \phi\ \text{nearly},
  \end{align}
  $R$~being the radian in seconds, viz.\ $206264''.806$, and $\log R = 5.3144251$.

  Substituting the approximate value of~$\phi_{0}$, we can get a new approximation.

  \textit{Example}.\qquad\qquad $\phi_{0} = 82°\ 30'$\qquad\qquad\qquad $k'_{00} = \log^{-1} 5.8757219$
  \[
  \begin{array}{l<{\qquad\qquad}@{}r@{}>{\qquad}c}
  \tan 82°\ 30' & 10.8805709 & \\\\
  k'_{00}   &     5.8757219 & \\\\
  R     &           5.3144251 & \\\\
  \cline{2-2}
  &                  2.0707179  & 117''.684 = 1'.9614
  \end{array}
  \]
  \begin{DPalign}
  \phi_{0} - \phi_{00} & = 1'.9614 \\\\
  \phi_{00} & = 82°\ 28'.0386   \rintertext{1st approximation.}
  \end{DPalign}

  This value gives
  \begin{DPalign}
  \phi_{0} - \phi_{00} &= 117''.1675 = 1'.95279\\
  \therefore \phi_{00} &= 82°\ 28'.04721
  \rintertext{2d~approximation.}\\
  \intertext{\indent This value gives}
  \phi_{0} - \phi_{00} &= 117''.1698 = 1'.95283\\
             \phi_{00} &= 82°\ 28'.04717
  \rintertext{3d~approximation.}
  \end{DPalign}
}
%% -----File: 044.png---Folio 38-------

To determine $k'_{0}$, $k'_{00}$,~etc., we have
\[
\Tag[18sub3]{(18_3)}
\left\{
\begin{aligned}
k' &= \sin \eta,   & k &= \cos \eta;\\
k'_{0}  &= \frac{1 - k}{1 + k} = \tan^{2} \tfrac{1}{2} \eta = \sin \eta_{0},
               & k_{1} &= \cos \eta_{0};\\
k'_{00} &= \tan^{2} \tfrac{1}{2} \eta_{0} = \sin \eta_{00},
               & k_{2} &= \cos \eta_{00};\\
        & \quad \PadTo[l]{\tan^{2} \tfrac{1}{2} \eta_{0}}{\quad\text{etc.}}
          \phantom{{}={}}
          \PadTo{\sin \eta_{00}}{\quad\text{etc.}} &
        & \PadTo{\cos \eta_{00}}{\text{etc.}}
\end{aligned}
\right.
\]

Or, since $1 + k'_0 = \dfrac{1}{\cos^2 \frac{1}{2} \eta}$,\quad $1 + k'_{00} = \dfrac{1}{\cos^2 \frac{1}{2} \eta_0}$, \text{etc.},
we can put \Eqref{eq.}{}{(18)} in the following form:
\[
\Tag{(19)}
F(k, \phi)
  = \frac{1}{\cos^{2} \frac{1}{2}\eta\,
             \cos^{2} \frac{1}{2}\eta_{0} \dotsm
             \cos^{2} \frac{1}{2}\eta_{0n}}\, F(k_{n}, \phi_{0n}).
\]

From \Eqref{equation}{}{(13)} we have
\begin{align}
\Tag[19st]{(19)^*}
F(k_1, \phi_0) &= \frac{1 + k}{2} F(k, \phi), \\\\
\intertext{whence}
F(k, \phi) &= \frac{2}{1 + k} F(k_1, \phi_0).
\end{align}

By repeated applications this gives, after combining,
\begin{align}
F(k, \phi)
  &= \frac{2}{1 + k}
   · \frac{2}{1 + k_{1}} \dotsm
     \frac{2}{1 + k_{n - 1}} · F(k_{n}, \phi_{0n}) \\\\
%% -----File: 045.png---Folio 39-------
  &= \frac{k_{1}}{\sqrt{k}} ·
     \frac{k_{2}}{\sqrt{k_{1}}} \dotsm
     \frac{k_{n}}{\sqrt{k_{n-1}}} · F(k_{n}, \phi_{0n});
\end{align}
\NegMathSkip
\[
\Tag{(20)}
F(k, \phi) = \sqrt{\frac{k_{1} k_{2} \dotsm k_{n}^{2}}{k}} · F(k_{n}, \phi_{0n});
\]
$k_{1}$,~$k_{2}$,~etc., being determined by repeated applications of
\[
k_{1} = \frac{2\sqrt{k}}{1 + k},
\]
or by \Eqref[18sub1]{equations}{}{(18_{1})}.

In \Eqref[19st]{equation}{}{(19)^*} let us change $k_{1}$~and~$\phi_{0}$ into $k'$~and~$\phi$ respectively,
so that the first member may have for its complete
function
\[
K' = F(k', \phi).
\]

Upon examination of \Eqref[19st]{eq.}{}{(19)^*} we see that the modulus in
the second member must be the one next less than the one in
the first member, that is,~$k_{0}'$; and likewise that the amplitude
must be the one next greater than the amplitude in the first
member, viz.,~$\phi_{1}$; hence we get
\[
F(k', \phi) = \frac{1 + k_{0}'}{2}\, F(k_{0}', \phi_{1}).
\]

Indicating the complete functions by $K'$~and~$K_{0}'$, we have,
since $\phi = \dfrac{\pi}{2}$ when $\phi_{1} = \pi$ (see \Chapref{Chap.}{V}),
\[
K' = (1 + k_{0}')K_{0}';
\]
and in the same manner,
\[
\begin{array}{r@{}l}
K_{0}' &{}= (1+k_{00}') K_{00}', \\\\
K_{00}' &{}= (1+k_{03}') K_{03}', \\\\
\Dots{2} \\\\
\llap{$K_{0(n-1)}'$} &{}= (1 + k_{0n}')K_{0n}';
\end{array}
\]
%% -----File: 046.png---Folio 40-------
whence
\[
K' = (1 + k_{0}')(1 + k_{00}') \dotsm (1+k_{0n}')K_{0n}'.
\]

Since
\begin{DPgather*}
K_{0n}' = \int_{0}^{\frac{\pi}{2}} d \phi = \frac{\pi}{2},
\rintertext{($n =$ limit,)}
\end{DPgather*}
we have
\[
\Tag[20st]{(20)^*}
(1 + k_{0}')(1 + k_{00}') \dotsm (1 + k_{0n}') = \frac{2K'}{\pi}.
\]

From \Eqref[19st]{eq.}{}{(19)^*} we have, since [\Eqref{eq.}{IV}{(10)}, Chap\DPtypo{}{.}~IV]
\begin{gather*}
\frac{1 + k}{2} = \frac{1}{1 + k_{0}'}, \\\\
(1 + k_{0}') \int_{0}^{\phi_{0}} \frac{d \phi_{0}}{\Delta (\phi_{0}, k_{1})}
  = \int_{0}^{\phi} \frac{d \phi}{\Delta (\phi_{1}, k)};
\end{gather*}
whence also, since for $\phi_{0} = \dfrac{\pi}{2}$, $\phi = \pi$,
\[
\begin{array}{r@{}l}
(1 + k_{0}')K_{1}  &{}= 2K, \\\\
(1 + k_{00}')K_{2} &{}= 2K_{1}, \\\\
\Dots{2} \\\\
(1 + k_{0n}')K_{n} &{}= \rlap{$2K_{n-1}$,}
\end{array}
\]
and
\[
(1 + k_{0}')(1 + k_{00}') \dotsm (1 + k_{0n}')K_{n} = 2^{n}K;
\]
or
\begin{DPalign}
\frac{K_{n}}{2^{n}}
  &= \frac{K}{(1 + k_{0}')(1 + k_{00}') \dotsm}
\rintertext{($n = \infty$)} \\\\
\Tag{(21)}
  & = \frac{\pi}{2K_{1}} K.
\end{DPalign}
%% -----File: 047.png---Folio 41-------

Let us find the limiting value of $F(k_{0n}, \phi_{n})$ in \Eqref{eq.}{}{(15)}. In
the equation $\tan (\phi_{n} - \phi_{n-1}) = k_{n-1} \tan \phi_{n-1}$, we see that when
$k_{n-1}$~reaches the limit~$1$, then $\phi_{n} - \phi_{n-1} = \phi_{n-1}$ or $\phi_{n} = 2\phi_{n-1}$.
Therefore
\begin{align}
\frac{\phi_{n}}{2^{n}}
  &= \frac{2\phi_{n - 1}}{2^{n}}
   = \frac{\phi_{n-1}}{2^{n - 1}}; \\\\
%
\frac{\phi_{n+1}}{2^{n+1}}
  &= \frac{2\phi_{n}}{2^{n+1}}
   = \frac{\phi_{n}}{2^{n}}
   = \frac{\phi_{n-1}}{2^{n}}; \\\\
%
\frac{\phi_{n+m}}{2^{n+m}}
  &= \frac{\phi_{n - 1}}{2^{n}}
   = \text{constant, whatever $m$ may be}.
\end{align}
Therefore \Eqref{eq.}{}{(15)} becomes
\[
\Tag[21st]{(21)^*}
F(k, \phi) = (1 + k_{0})(1 + k_{00}) \dotsm (1 + k_{0n}) \frac{\phi_{n}}{2^{n}},
\]
$n$~being whatever number will carry $k_{0}$ and~$\dfrac{\phi_{1}}{2}$ to their limiting
values.

In the same way, \Eqref{eqs.}{}{(16)} and~\Eqref{}{}{(17)} become
\begin{align}
\Tag{(22)}
F(k, \phi)
  &= \frac{1}{\cos^{2} \dfrac{\theta}{2}
              \cos^{2} \dfrac{\theta_{0}}{2} \dotsm
              \cos^{2} \dfrac{\theta_{0n}}{2}} · \frac{\phi_{n}}{2^{n}} \\\\
\Tag{(23)}
  &= \sqrt{\frac{\cos \theta_{0} \cos \theta_{00} \dotsm \cos^{2} \theta_{0n}}{\cos \theta}}
   · \frac{\phi_{n}}{2^{n}},
\end{align}
$n - 1$ being the number which makes $k_{n-1}' = 1$.

In these last three \DPtypo{equation}{equations} $k_{0}$,~$k_{00}$ are determined by \Eqref[14sub1]{eqs.}{}{(14_{1})};
$\phi_{1}$,~$\phi_{2}$,~etc., by \Eqref[14sub2]{eqs.}{}{(14_{2})}\footnotemark;
\footnotetext{Taking for~$\phi_{1} - \phi$, etc., not always the least angle given by the tables,
  but that which is nearest to~$\phi$.}%
$\theta$,~$\theta_{0}$,~etc., by \Eqref[14sub1]{eqs.}{}{(14_{1})}; and
$k'$,~$k_{1}'$, $\DPtypo{k_{2}}{k_{2}'}$,~etc., for use in \Eqref[14sub2]{eq.}{}{(14_{2})} by \Eqref[14sub1]{eqs.}{}{(14_{1})}.
%% -----File: 048.png---Folio 42-------

\Section{BISECTED AMPLITUDES.}

We have identically
\begin{DPalign}
u &= 2 · \frac{u}{2}
   = 2 \raisebox{-1ex}{\scalebox{2}{$\displaystyle\int$}} \frac{d \am \dfrac{u}{2}}{\sqrt{1 - k^{2} \sn^{2} \dfrac{u}{2}}}; \\\\
\frac{u}{2}
  &= 2 · \frac{u}{4}
   = 2F\left(k, \am \frac{u}{4}\right); \\\\
  & \quad \text {etc.} \\\\
\intertext{\indent Therefore}
u &= F(k, \am u) = 2^{n} F\left(k, \am \frac{u}{n}\right) \\\\
  &= 2^{n} · \am \frac{u}{n},
\rintertext{($n =$ limit,)}
\end{DPalign}
$\am \dfrac{u}{n}$ being determined by repeated applications of \Eqref{eq.}{II}{(12)} of
Chap.~II, as follows:
\begin{align}
\sn^{2} \frac{u}{2}
  &= \frac{1 - \cn u}{1 + \dn u}
   = \frac{2 \sin^{2} \frac{1}{2} \am u}{1 + \dn u}; \\\\
%
\Tag{(24)}
\sn \frac{u}{2}
  &= \frac{\sin \frac{1}{2} \am u}{\sqrt{\dfrac{1 + \cos \beta}{2}}}
   = \frac{\sin \dfrac{\am u}{2}}{\cos \frac{1}{2} \beta};
\end{align}
$\beta$ being an angle determined by the equation
\[
\Tag{(25)}
\cos \beta = \dn u = \sqrt{1 - k^{2} \sn^{2} u},
\]
and $n$ being the number which makes
\[
2^{n} \am \frac{u}{n} = \text{constant}.
\]
$\am \dfrac{u}{n}$ is found by repeated applications of \Eqref{eq.}{}{(24)}.
%% -----File: 049.png---Folio 43-------

Indicating the amplitudes as follows:
\[
\begin{array}{r@{}l}
\am u &{}= \phi, \\\\
\am \dfrac{u}{2} &{}= \phi_{02}, \\\\[2pt]
\am \dfrac{u}{4} &{}= \phi_{04}, \\\\[2pt]
\am \dfrac{u}{8} &{}= \phi_{08}, \\\\[2pt]
\Dots{2} \\\\
%[** PP: Em-dash present in high-res scan, retaining]
\llap{$\am \dfrac{u}{2^{n}}$} &{}= \rlap{$\phi_{02^{n}},\text{---}$} \\\\
\Tag{(26)}
\llap{$F(k, \phi)$} &{} = \rlap{$2^{n} \phi_{02^{n}}$;}
\end{array}
\]
$n$~being the limiting value.

In \Eqref{eq.}{}{(18)}, when $k_{n}$~reaches its limit~$1$, we have
\[
F(k_{n}, \phi_{0n})
  = \int_{0}^{\phi} \frac{d \phi_{0n}}{\cos \phi_{0n}}
  = \log_{\epsilon} \tan (45^{\circ} + \tfrac{1}{2} \phi_{0n}),
\]
and \Eqref{eqs.}{}{(18)} and~\Eqref{}{}{(19)} become
\begin{align}
\Tag{(27)}
F(k, \phi)
  &= (1 + k_{0}')(1 + k_{00}') \dotsm (1 + k_{0n}')
     \log_{\epsilon} \tan (45° + \tfrac{1}{2} \phi_{0n}) \\\\
  &= \frac{1}{\cos^{2} \frac{1}{2} \eta\,
              \cos^{2} \frac{1}{2} \eta_{0} \dotsm
              \cos^{2} \frac{1}{2} \eta_{0n}}
     \log_{\epsilon} \tan (45° + \tfrac{1}{2} \phi_{0n}) \\\\
\Tag{(28)}
  &= \frac{1}{\cos^{2} \frac{1}{2} \eta\,
              \cos^{2} \frac{1}{2} \eta_{0} \dotsm
              \cos^{2} \frac{1}{2} \eta_{0n}}
   · \frac{1}{M} \log \tan (45° + \tfrac{1}{2} \phi_{0n});
\end{align}
$n$~being the number which renders $k_{n} = 1$.

\Eqref{Eq.}{}{(20)} becomes
%% -----File: 050.png---Folio 44-------
\begin{align}%[** PP: Realigning first line on =]
\Tag{(29)}
F(k, \phi)
  &= \sqrt{\frac{k_{1} k_{2} \dotsm k_{n}^{2}}{k}}
   · \log_{\epsilon} \tan (45° + \tfrac{1}{2} \phi_{0n}) \\\\
%
  &= \sqrt{\frac{k_{1}k_{2} \dotsm k_{n}^{2}}{k}}
   · \frac{1}{M} \log \tan (45° + \tfrac{1}{2} \phi_{0n}) \\\\
%
  &= \sqrt{\frac{\cos \eta_{0} \cos \eta_{00} \dotsm \cos^{2} \eta_{0n}}{\cos \eta}}
   · \frac{1}{M} \log \tan (45° + \tfrac{1}{2} \phi_{0n}).
\end{align}

In these equations $k'_{0}$,~$k'_{00}$,~etc., are determined by \Eqref[18sub3]{eqs.}{}{(18_3)};
$\eta$,~$\eta_{0}$,~etc., by \Eqref[18sub3]{eqs.}{}{(18_3)}; $\phi_{0}$,~$\phi_{00}$,~etc., by \Eqref[18sub2]{eqs.}{}{(18_2)}; $k_{1}$,~$k_{2}$,~etc., by \Eqref[18sub1]{eqs.}{}{(18_1)}.

Substituting in \Eqref{eq.}{}{(27)} from \Eqref[20st]{eq.}{}{(20)^*}, we have
\begin{align}
F(k, \phi)
  &= \frac{2K'}{\pi} \log_{\epsilon} \tan (45° + \tfrac{1}{2} \phi_{0n})\\
\Tag{(30)}
  &= \frac{2K'}{\pi M} \log \tan (45° + \tfrac{1}{2} \phi_{0n}).
\end{align}
%% -----File: 051.png---Folio 45-------


