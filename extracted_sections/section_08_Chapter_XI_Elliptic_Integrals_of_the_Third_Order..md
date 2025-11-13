# Chapter XI: Elliptic Integrals of the Third Order.

Lines: 4106-5301

\Chapter{XI}{Elliptic Integrals of the Third Order.}

\First{The} Elliptic Integral of the third order is
\[
\Tag{(1)}
\Pi (n, k, \phi) = \int_{0}^{\phi} \frac{d\phi}{(1 + n \sin^{2} \phi)\, \Delta \phi}.
\]

Put
\[
\Tag{(2)}
\Pi (\phi) + \Pi (\psi) = S;
\]
whence we have immediately
\[
\Tag{(3)}
dS = \frac{d\phi}{(1 + n \sin^{2} \phi)\, \Delta \phi}
   + \frac{d\psi}{(1 + n \sin^{2} \psi)\, \Delta \psi}.
\]
But, \Eqref{eq.}{II}{(2)}, Chap.~II,
\[
\Tag{(4)}
\frac{d\phi}{\Delta \phi} + \frac{d\psi}{\Delta \psi} = 0;
\]
whence
\begin{align}
dS &= \left(\frac{1}{1 + n \sin^{2} \phi} - \frac{1}{1 + n \sin^{2} \psi}\right) \frac{d\phi}{\Delta \phi} \\\\
\Tag{(5)}
   &= \frac{n (\sin^{2} \psi - \sin^{2} \phi)}
           {(1 + n \sin^{2} \phi)(1 + n \sin^{2} \psi)} · \frac{d\phi}{\Delta \phi}.
\end{align}

From \Eqref{equation}{X}{(8)}, Chap.~X, we get by differentiation, since
$\sigma$ (or~$\mu$) is constant,
\begin{align}
\Delta \phi · d \phi + \Delta \psi · d\psi
  &= k^{2} \sin \sigma\, d(\sin \phi \sin \psi),
\intertext{or, from \Eqref{equation}{}{(3)},}
(\sin^{2} \psi - \sin^{2} \phi)\, \frac{d\phi}{\Delta \phi}
  &= \sin \sigma\, d(\sin \phi \sin \psi).
\end{align}
%% -----File: 097.png---Folio 91-------
This, introduced into \Eqref{equation}{}{(5)}, gives
\[
dS = \frac{n \sin \sigma\, d (\sin \phi \sin \psi)}
          {1 + n (\sin^{2} \phi + \sin^{2} \psi) + n^{2} \sin^{2} \phi \sin^{2} \psi}.
\]

Put
\[
\sin \phi \sin \psi = q, \quad \sin^{2} \phi + \sin^{2} \psi = p;
\]
whence
\[
\Tag{(6)}
dS = \frac{n \sin \sigma\, dq}{1 + np + n^{2}p^{2}}.
\]

From \Eqref{equation}{II}{(5)}, Chap.~II, we have
\[
\cos \sigma = \cos\phi \cos\psi - \sin\phi \sin\psi\, \Delta\sigma,
\]
from which we easily get
\begin{align}
(\cos \sigma + q \Delta \sigma)^{2}
  &= \cos^{2} \phi \cos^{2} \psi\DPtypo{)}{} \\\\
  &= (1 - \sin^{2} \phi)(1 - \sin^{2} \psi) \\\\
  &= 1 - p + q^{2},
\end{align}
and thence
\begin{align}
p &= 1 + q^{2} - (\cos \sigma + q\, \Delta \sigma)^{2} \\\\
  &= \sin^{2} \sigma - 2 \cos \sigma \Delta \sigma q + k^{2} \sin^{2} \sigma · q^{2}.
\end{align}

This, substituted in \Eqref{eq.}{}{(6)}, gives
\begin{align}
dS &= \frac{n \sin \sigma\, dq}
           {1 + n \sin^{2} \sigma - 2n \cos \sigma \Delta \sigma q + n(n + k^{2} \sin^{2} \sigma) q^{2}} \\\\
  &= \frac{n \sin \sigma\, dq}{A - 2Bq +Cq^{2}},
\end{align}
where
\begin{align}
A &= 1 + n \sin^{2} \sigma, \\\\
B &= n \cos \sigma\, \Delta \sigma, \\\\
C &= nk^{2} \sin^{2} \sigma + n^{2}.
\end{align}
%% -----File: 098.png---Folio 92-------

From this we get
\[
S = n \sin \sigma \int \frac{dq}{A - 2Bq + Cq^{2}} + \text{Const.}
\]

In order to determine the constant of integration we must
observe that for $\phi = 0$, $\psi = \sigma$ and~$q = 0$; whence
\begin{align}
\Pi \sigma &= n \sin \sigma \int_{q=0} \frac{dq}{A - 2Bq + Cq^{2}} + \text{Const.};
\intertext{whence}
S &= \Pi \sigma + n \sin \sigma \int_{0}^{q} \frac{dq}{A - 2Bq + Cq^{2}},
\intertext{or}
\Tag{(7)}
\Pi \phi + \Pi \psi &= \Pi \sigma + n \sin \sigma \int_{0}^{q} \frac{dq}{A - 2Bq + Cq^{2}}.
\end{align}

But we have
\begin{align}
dS &= \frac{CM\, dq}{AC - B^{2} + (Cq - B)^{2}} \\\\
  &= \frac{CM}{AC - B^{2}} · \frac{dq}{1 + \left(\dfrac{Cq - B}{\sqrt{AC - B^{2}}}\right)^{2}} \\\\
  &= \frac{M}{\sqrt{AC-B^{2}}}
   · \frac{\dfrac{C\, dq}{\sqrt{AC - B^{2}}}}
          {1 + \left(\dfrac{Cq - B}{\sqrt{AC - B^{2}}}\right)^{2}}
\end{align}
where $M = n \sin \sigma$.

The integral of the second member is
\[
\frac{M}{\sqrt{AC - B^{2}}} \tan^{-1} \frac{Cq - B}{\sqrt{AC - B^{2}}};
\]
%% -----File: 099.png---Folio 93-------
whence
\[
\int_{0}^{q} dS = S_{1}
  = \frac{M}{\sqrt{AC - B^{2}}}
    \left[\tan^{-1} \frac{Cq - B}{\sqrt{AC - B^{2}}}
        + \tan^{-1} \frac{B}{\sqrt{AC - B^{2}}}\right];
\]
or, since
\begin{gather*}
\tan^{-1} x + \tan^{-1} y = \tan^{-1} \frac{x + y}{1 - xy}, \\\\
S_{1} = \frac{M}{\sqrt{AC - B^{2}}} \tan^{-1} \frac{q\sqrt{AC - B^{2}}}{A - Bq}.
\end{gather*}

Substituting the values of $A$,~$B$,~$C$ and~$M$, we have
\begin{align}
AC - B^{2}
  &= n(1 + n - \Delta^{2} \sigma)(1 + n \sin^{2} \sigma) - n^{2} \cos^{2} \sigma\, \Delta^{2} \sigma \\\\
  &= n(1 + n - \Delta^{2} \sigma + n(1 + n) \sin^{2} \sigma - n\, \Delta^{2} \sigma) \\\\
  &= n(1 + n)(1 - \Delta^{2} \sigma + n \sin^{2} \sigma) \\\\
  &= n(1 + n)(k^{2} + n) \sin^{2} \sigma;
\end{align}
and putting
\[
\frac{(1 + n)(k^{2} + n)}{n} = \Omega,
\]
we have
\[
\sqrt{AC - B^{2}} = n \sqrt{\Omega} \sin \sigma.
\]
Substituting these values in \Eqref{eq.}{}{(7)}, we have
\begin{gather*}
\Pi (n, k, \phi) + \Pi (n, k, \psi) - \Pi (n, k, \sigma) = S_{1} \\\\
= \frac{1}{\sqrt{\Omega}}
  \tan^{-1} \frac{n\sqrt{\Omega} \sin \phi \sin \psi \sin \sigma}
                 {1 + n \sin^{2} \sigma - n \sin \phi \sin \psi \cos \sigma\, \Delta \sigma}.
\end{gather*}
%% -----File: 100.png---Folio 94-------


\Chapter[Numerical Calculations. q.]{XII}{Numerical Calculations. $q$.}

\Section{CALCULATION OF THE VALUE OF~$q$.}

\First{From} \Eqref{eq.}{IX}{(7)}, Chap.~IX, we have
\[
\dn u = \sqrt{k'}\, \frac{\Theta (u + K)}{\Theta (u)};
\]
whence, \Eqref{eq.}{IV}{(9)}, Chap.~IV, \Eqref{eqs.}{IX}{(27)} and~\Eqref{}{IX}{(39)}, Chap.~IX,
\begin{align}
\Tag{(1)}
\sqrt{\cos \theta}
  &= \frac{1 - 2q + 2q^{4} - 2q^{9} + 2q^{16} - \dotsb}
          {1 + 2q + 2q^{4} + 2q^{9} + 2q^{16} + \dotsb} \\\\
  &= 1 - 4q + 8q^{2} - 16q^{3} + 32q^{4} - 56q^{5} + \dotsb.
\end{align}

The first five terms of this series can be represented by
\[
\sqrt{\cos \theta} = \frac{1 - 2q}{1 + 2q}.
\]
From this we get
\[
\Tag{(2)}
q = \frac{1}{2} · \frac{1 - \sqrt{\cos \theta}}{1 + \sqrt{\cos \theta}},
\]
which is exact up to the term containing~$q^{5}$.

Or we can deduce a more exact formula as follows: From
\Eqref{eq.}{}{(1)},
\begin{align}
\frac{1 + \sqrt{\cos \theta}}{1 - \sqrt{\cos \theta}}
  &= \frac{\sqrt{1 + \tan^{2} \frac{1}{2} \theta}
         + \sqrt{1 - \tan^{2} \frac{1}{2} \theta}}
          {\sqrt{1 + \tan^{2} \frac{1}{2} \theta}
         - \sqrt{1 - \tan^{2} \frac{1}{2} \theta}} \\\\
  &= \frac{ 1 + 2q^{4} + 2q^{16} + \dotsb}
          {2q + 2q^{9} + 2q^{25} + \dotsb};
\end{align}
%% -----File: 101.png---Folio 95-------
whence, by the method of indeterminate coefficients,
\begin{align}
\Tag{(3)}
q &= \tfrac{1}{4}  \tan^{2} \frac{\theta}{2}
   + \tfrac{1}{16} \tan^{\DPtypo{2}{6}} \frac{\theta}{2}
   + \tfrac{\DPtypo{57}{17}}{512} \tan^{10} \frac{\theta}{2}
   + \tfrac{45}{2048} \tan^{14} \frac{\theta}{2} + \dotsb, \\\\
\intertext{or}
\log q %[** PP: Re-breaking]
  &= 2 \log \tan \frac{\theta}{2} - \log 4 \\\\
  &\qquad
   + \log \Bigl(1 + \tfrac{1}{4} \tan^{4} \frac{\theta}{2}
   + \tfrac{17}{128} \tan^{8} \frac{\theta}{2}
   + \tfrac{45}{512} \tan^{12} \frac{\theta}{2} \dotsb\Bigr) \\\\
\Tag{(4)}
  &= 2 \log \tan \frac{\theta}{2} - \log 4 \\\\
  &\qquad
   + M\Bigl(\tfrac{1}{4} \tan^{4} \frac{\theta}{2}
   + \tfrac{13}{128} \tan^{8} \frac{\theta}{2}
   + \tfrac{23}{384} \tan^{12} \frac{\theta}{2} + \dotsb\Bigr),
\end{align}
$M$~being the modulus of the common system of logarithms.

Put
\[
\Tag{(5)}%[** PP: Re-breaking]
\log q = 2 \log \tan \frac{\theta}{2}
  + 9.397940 + a \tan^{4} \frac{\theta}{2}
  + b \tan^{8} \frac{\theta}{2}
  + c \tan^{12} \frac{\theta}{2} + \dotsb,
\]
in which
\begin{align}
\log a &= 9.0357243; \\\\
\log b &= 8.64452; \\\\
\log c &= 8.41518; \\\\
\log d &= 8.25283.
\end{align}

\Example. Let $k' = \cos 10°\ 23'\ 46''$. To find~$q$.
\[
\begin{array}[t]{r@{}c@{}l@{}}
4 \log \tan \dfrac{\theta}{2}
       &{}={}& 5.835 \\\\
\log a &{}={}& 9.036 \\\\
\cline{3-3}
            && 4.871 \\\\
&& \\\\
a \tan^{4} \dfrac{\theta}{2}
       &{}={}& \rlap{$0.0000074$}
\end{array}
\qquad\qquad
\begin{array}[t]{r@{}c@{}l@{}}
2 \log \tan \dfrac{\theta}{2}
       &{}={}& 7.9176842 \\\\
       &     & 9.3979400 \\\\
       &     & \PadTo[r]{9.3979400}{74} \\\\
\cline{3-3}
\log q &{}={}& 7.3156316
\end{array}
\]
%% -----File: 102.png---Folio 96-------

When $\theta$ approaches~$90°$, $\tan \dfrac{\theta}{2}$~differs little from unity, and
the series in \Eqref{eq.}{}{(5)} is not very converging, but $q$~can be calculated
by means of \Eqref{eq.}{VII}{(6)}, Chap.~VII, viz.,
\[
q = e^{-\frac{\pi K'}{K}}, \qquad q' = e^{-\frac{\pi K}{K'}}.
\]

By comparing these equations with \Eqref{eqs.}{IV}{(6)} and~\Eqref{}{IV}{(9)}, Chap.~IV,
we see that if
\begin{align}
q &= f(k) = f(\theta),
\intertext{then}
q' &= f(k') = f(90° - \theta).
\end{align}

Therefore, having $\theta$, we can from its complement, $90° - \theta$,
find~$q'$ by \Eqref{eq.}{}{(5)}, and thence~$q$ by the following process. We
have
\[
\frac{1}{q}  = e^{\frac{\pi K'}{K}}, \qquad
\frac{1}{q'} = e^{\frac{\pi K}{K'}};
\]
whence
\begin{align}
\log \frac{1}{q} \log \frac{1}{q'} = M^{2}\pi^{2} &= 1.8615228, \\\\
\Tag{(6)}
\log \log \frac{1}{q} + \log \log \frac{1}{q'} &= 0.2698684,
\end{align}
by which we can deduce $q$ from~$q'$.

\Example. Let $\theta = 79°\ 36'\ 14''$. To find~$q$.
\[
90° - \theta = 10°\ 23'\ 46''.
\]

By \Eqref{eq.}{}{(5)} we get
\begin{gather*}
\log q' = 7.3156316, \qquad \log \frac{1}{q'} = 2.6843684, \\\\
\text{and} \quad \log \log \frac{1}{q'} = .4288421;
\end{gather*}
%% -----File: 103.png---Folio 97-------
and by \Eqref{eq.}{}{(6)},
\begin{align}
\log \log \frac{1}{q} &= 9.8410263;
\intertext{whence}
\log q &= 1.3065321.
\end{align}

When $k' = k = \cos 45° = \frac{1}{2} \sqrt{2}$, \Eqref{eq.}{}{(6)} becomes
\begin{DPalign}
\Tag{(7)}
\log \frac{1}{q}
  &= M \pi = 1.3643763;
\rintertext{($k = k'$;)} \\\\
\intertext{whence}
\log q &= 2.6356237, \\\\
q &= 0.0432138.
\rintertext{($k = k'$.)}
\end{DPalign}

\Example. Given $\theta = 10°\ 23'\ 46''$. Find~$q$. \\\\
\null\hfill\textit{Ans.} $\log q = 7.3156316$.

\Example. Given $\theta = 82°\ 45'$. Find~$q$. \\\\
\null\hfill\textit{Ans.} $\log q = 9.37919$.
%% -----File: 104.png---Folio 98-------


\Chapter[Numerical Calculations. K.]{XIII}{Numerical Calculations. $K$.}

\Section{CALCULATION OF THE VALUE OF $K$.}

\First{We} have already found from \Eqref{eq.}{IX}{(37)}, Chap.~IX,
\[
\Tag{(1)}
\Theta (0) = \sqrt{\frac{2k'K}{\pi}},
\]
and from \Eqref{eq.}{IX}{(40)}, same chapter,
\[
\Tag{(2)}
\Theta (K) = \frac{\Theta (0)}{\sqrt{k'}} = \sqrt{\frac{2K}{\pi}}.
\]

But, \Eqref{eqs.}{IX}{(38)} and~\Eqref{}{IX}{(27)}, Chap.~IX,
\begin{align}
\Theta (K) &= 1 + 2q + 2q^{4} + 2q^{9} + 2q^{16} + \dotsb, \\\\
\Theta (0) &= 1 - 2q + 2q^{4} - 2q^{9} + 2q^{16} - \dotsb;
\end{align}
whence, \Eqref{eq.}{}{(2)},
\[
\Tag{(3)}
K = \frac{\pi}{2} (1 + 2q + 2q^{4} + 2q^{9} + \dotsb)^{2}.
\]

By adding \Eqref{eqs.}{}{(1)}~and~\Eqref{}{}{(2)} we get
\[
\Theta (0) + \Theta (K) = \sqrt{\frac{2K}{\pi}} (1 + \sqrt{k'});
\]
whence
\begin{align}
K &= \frac{\pi}{2} \left(\frac{\Theta (0) + \Theta (K)}{1 + \sqrt{k'}}\right)^{2} \\\\
  &= \frac{\pi}{2} \left[\frac{2(1 + 2q^{4} + 2q^{16} + \dotsb)}{1 + \sqrt{k'}}\right]^{2} \\\\
%% -----File: 105.png---Folio 99-------
\Tag{(4)}
  &= \frac{\pi}{2} \left(\frac{2}{1 + \sqrt{k'}}\right)^{2}
     (1 + 2q^{4} + 2q^{16} + \dotsb)^{2}.
\end{align}

\Example. Let $k = \sin \theta = \sin 19°\ 30'$. Required~$K$.

*First Method.*\quad By \Eqref{eq.}{}{(3)}.

By \Eqref{eq.}{XII}{(5)}, Chap.~XII, we find $\log q = 8.6356236$. Applying
\Eqref{eq.}{}{(3)}, using only two terms of the series, we have
\[
\begin{array}{r@{}l@{}}
1 + 2q &{} = 1.0147662 \\\\
\PadTo[r]{1+2q}{\log (1 + 2q)} &{} = 0.0063660 \\\\
\PadTo[r]{1+2q}{2 \log (1 + 2q)} &{} = 0.0127320 \\\\
\log \dfrac{\pi}{2} &{} = 0.1961199 \\\\
\cline{1-2}
\log K &{} = 0.2088519 \\\\
K &{} = 1.615101
\end{array}
\]

*Second Method.*\quad By \Eqref{eq.}{}{(4)}.

\Eqref{Equation}{}{(4)} may be written, neglecting~$q^{4}$,
\[
K = \frac{\pi}{2} \left(\frac{1 + \sqrt{\cos \theta}}{2}\right)^{-2};
\]
whence
\begin{align}
\log \cos \theta & = 9.9743466, \\\\
\log \sqrt{\cos \theta} & = 9.9871733, \\\\
1 + \sqrt{\cos \theta} & = 1.9708973, \\\\
\frac{1 + \sqrt{\cos \theta}}{2} & = 0.98544865;
\intertext{and}
\log K & = 0.2088519, \\\\
K & = 1.615101,
\end{align}
the same result as above.
%% -----File: 106.png---Folio 100-------

*Third Method.*\quad By \Eqref{eq.}{V}{(7)}, Chap.~V.
\[
\begin{array}{r@{}c@{}l<{\quad}|>{\quad}r@{}c@{}l}
\theta &{}={} & 19°\ 30' &
  \theta_{0} &{}={}& 1°\ 41'\ 31''.1 \\\\
\frac{1}{2} \theta &{}={}& 9°\ 45' &
  \frac{1}{2} \theta_{0} &{}={}& 0°\ 50'\ 45''.5 \\\\
\log \tan \frac{1}{2} \theta &{}={}& 9.235103 & & & \\\\
\log \cos \frac{1}{2} \theta &{}={}& 9.993681 &
  \log \cos \frac{1}{2} \theta_{0}  &{}={}& 9.999953 \\\\
\begin{array}{r}
\log \tan^{2} \frac{1}{2} \theta \\\\ \log \sin \theta_{0}\end{array}\biggr\} & = & 8.470206 & & & \\\\
\theta_{0} & = & 1°\ 41'\ 31''.1 & & &
\end{array}
\]
\[
\begin{array}{r@{}c@{}l@{}}
\log \cos^{2} \tfrac{1}{2} \theta     &{}={}& 9.987362 \\\\
\log \cos^{2} \tfrac{1}{2} \theta_{0} &{}={}& 9.999906 \\\\
\cline{3-3}
                                      &     & 9.987268 \\\\
\log \dfrac{\pi}{2}                   &{}={}& 0.196120 \\\\
\cline{3-3}
\log K                                &{}={}& 0.208852
\end{array}
\]

$\theta_{00}$~is not calculated, as it is evident that its cosine will be~$1$.

\Example. Given $k = \sin 75°$. Find~$K$.

By \Eqref{eq.}{V}{(7)}, Chap.~V.

From \Eqref[14sub1]{eqs.}{IV}{(14_{1})}, Chap.~IV, we find
\settowidth{\TmpLen}{$\tan^{2} \tfrac{1}{2} \theta_{00}$}%
\begin{align}
k &= \sin\theta = \sin 75°  & \log &= 9.9849438 \\\\
\PadTo[l]{k_{00}}{k_{0}} &= \biggl\{
  \begin{aligned}
    \makebox[\TmpLen][l]{$\tan^{2} \tfrac{1}{2} \theta$}
      &= \tan^{2} 37°\ 30' \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{0}$}
      &= \sinP 36°\ \Z4'\ 16''.47\Z
  \end{aligned}\biggr\} & & \PadTo{{}={}}{} 9.7699610 \\\\
%
k_{00} &= \biggl\{
  \begin{aligned}
    \makebox[\TmpLen][l]{$\tan^{2} \tfrac{1}{2} \theta_{0}$}
      &= \tan^{2} 18°\ \Z2'\ \Z8''.235 \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{00}$}
      &= \sinP \Z6°\ \Z5'\ \Z9''.38
  \end{aligned}\biggr\} & &  \PadTo{{}={}}{} 9.0253880 \\\\
%
k_{03} &= \biggl\{
  \begin{aligned}
    \makebox[\TmpLen][l]{$\tan^{2} \tfrac{1}{2} \theta_{00}$}
      &= \tan^{2} \Z3°\ \Z2'\ 34''.69\Z \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{03}$}
      &= \PadTo[l]{\tan^2  18°}{\sin}\ \Z9'\ 42''.90
  \end{aligned}\biggr\} & &  \PadTo{{}={}}{} 7.4511672
\end{align}
%% -----File: 107.png---Folio 101-------
\[
\begin{array}{l@{\,}c@{\,}l@{\,}r@{\ }lcc<{\quad}@{}c@{}}
 &&&&&   \log  &  2 \log  &  \ac 2 \log \\\\
\cos \frac{1}{2} \theta
  &=& \cos & 37° & 30'      & 9.8994667 & 9.7989334 & 0.2010666 \\\\
\cos \frac{1}{2} \theta_{0}
  &=& \cos & 18° & 2'.13725 & 9.9781184 & 9.9562368 & 0.0437632 \\\\
\cos \frac{1}{2} \theta_{02}
  &=& \cos &  3° & 2'.57817 & 9.9993873 & 9.9987746 & 0.0012254 \\\\
\cos \frac{1}{2} \theta_{03}
  &=& \cos &     & 4'.8575  & 9.9999995 & 9.9999990 & 0.0000010 \\\\
\cline{8-8}
& & & & & & &                                         0.2460562 \\\\
\multicolumn{1}{c}{\dfrac{\pi}{2}} & & & & & & \dfrac{\pi}{2} & \Z.1961199 \\\\
\cline{8-8}
& & & & & \multicolumn{3}{r@{}}{%
  \log K = \PadTo[r]{2.768064\quad \text{\textit{Ans.}}}{0.4421761}} \\\\
& & & & & \multicolumn{3}{r@{}}{%
       K = 2.768064\quad \text{\textit{Ans.}}}
\end{array}
\]

\Example. Given $k = \sin 45°$. Find~$K$.

Method of \Eqref{eq.}{V}{(7)}, Chap.~V.

From \Eqref[14sub1]{eqs.}{IV}{(14_{1})}, Chap.~IV, we have
\settowidth{\TmpLen}{$\tan^{2} \tfrac{1}{2} \theta_{00}$}%
\begin{align}
& & \PadTo{9.2344486}{\log} \\\\
\PadTo[l]{k_{00}}{k_{0}} &= \biggl\{
  \begin{aligned}
    \makebox[\TmpLen][l]{$\tan^{2} \frac{1}{2} \theta$}
    &= \tan^{2} 22°\ 30' \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{0}$}
    &= \sinP \Z9°\ 52'.75683
  \end{aligned}\biggr\} &  9.2344486 \\\\
%
k_{00} &= \biggl\{
  \begin{aligned}
    \makebox[\TmpLen][l]{$\tan^{2} \tfrac{1}{2} \theta_{0}$}
    &= \tan^{2} \Z4°\ 56'.37841 \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{00}$}
    &= \PadTo[l]{\tan^2 22°}{\sin}\ 25'.679
  \end{aligned}\biggr\} & 7.8733009 \\\\
%
k_{03} &= \biggl\{
  \begin{aligned}
    \tan^{2} \tfrac{1}{2} \theta_{00}
    &= \PadTo[l]{\tan^2 22°}{\tan^{2}}\ 12'.3395\Z \\\\
    \makebox[\TmpLen][l]{$\sin \theta_{03}$}
    &= \PadTo[l]{\tan^2 22°}{\sin}\ \Z0'.05
  \end{aligned}\biggr\} & 5.1445523
\end{align}
\[
\begin{array}{l@{}r@{}l@{}}
\ac \log \cos^{2} \frac{1}{2} \theta     &&  0.0687694 \\\\
\ac \log \cos^{2} \frac{1}{2} \theta_{0}  && 0.0032320 \\\\
\ac \log \cos^{2} \frac{1}{2} \theta_{00} && 0.0000060 \\\\
\multicolumn{1}{c}{\log \dfrac{\pi}{2}}  && 0.1961199 \\\\
\cline{3-3}
  & \log K = {}& 0.2681273 \\\\
  & K = {}& 1.8540747 \rlap{\quad\text{\textit{Ans.}}}
\end{array}
\]

\Example. Given $\theta = 63°\ 30'$. Find~$K$. \\\\
\null\hfill\textit{Ans.} $\log K = 0.3539686$.

\Example. Given $\theta = 34°\ 30'$. Find~$K$. \\\\
\null\hfill\textit{Ans.} $K = 1.72627$.
%% -----File: 108.png---Folio 102-------


\Chapter[Numerical Calculations. u.]{XIV}{Numerical Calculations. $u$}

\Section{CALCULATION OF THE VALUE OF~$u$.}

\First{When} $\theta° =  \sin^{-1}k < 45°$.

\Example. Let $\phi = 30°$, $k = \sin 45°$. Find~$u$.

*First Method.* \Eqref{Eq.}{IV}{(23)}, Chap.~IV, and \Eqref[14sub1]{eqs.}{IV}{(14_{1})}, \Eqref[14sub2]{}{IV}{(14_{2})},~\Eqref[14sub3]{}{IV}{(14_{3})},
Chap.~IV\@.

By \Eqref[14sub1]{equations}{IV}{(14_{1})},
\begin{align}
\frac{\theta}{2} &= 22°~30'; \\\\
\log \tan \frac{\theta}{2} &= 9.6172243; \\\\
\log \tan^{2} \frac{\theta}{2} &= 9.2344486 = \log k_{0} = \log \sin \theta_{0}; \\\\
\theta_{0} &= 9°~52'~45''.41; \\\\
\log \tan \frac{\theta_{0}}{2} &= 8.9366506; \\\\
\log \tan^{2} \frac{\theta_{0}}{2} &= 7.8733012 = \log k_{00} = \log \sin \theta_{00}; \\\\
\theta_{00} &= 0°~25'~40''.7; \\\\
\log \tan^{2} \frac{\theta_{00}}{2} &= 5.144552 = \log k_{03}.
\end{align}
%% -----File: 109.png---Folio 103-------

By \Eqref[14sub2]{equations}{IV}{(14_{2})},
\[
\begin{array}{@{}r@{}l@{}}
\phi &{}= 30° \\\\
\log \tan \phi &{}= 9.761439 \\\\
\log \cos \theta &{}= 9.849485 \\\\
\cline{1-2}
\llap{$\log \tan (\phi_{1} - \phi)$} &{}= 9.610924 \\\\
\phi_{1} - \phi &{}= \rlap{$22°\ 12'\ 27''.56$} \\\\
\phi_{1} &{}= \rlap{$52°\ 12'\ 27''.56$} \\\\
\end{array}
\]
%
\[
\begin{array}{@{}r@{}l@{}}
\log \tan \phi_{1} &{}= 0.110438 \\\\
\log \cos \theta_{0} &{}= 9.993512 \\\\
\cline{1-2}
\llap{$\log \tan (\phi_{2} - \phi_{1})$} &{}= 0.103949 \\\\
\phi_{2} - \phi_{1} &{}= \rlap{$51°\ 47'\ 32''.59$} \\\\
\end{array}
\]
%
\[
\begin{array}{@{}r@{}l@{}}
\phi_{2} &{}= \rlap{$104°\ 0'\ 0''.15$} \\\\
\log \tan \phi_{2} &{}= 0.603228 \\\\
\log \cos \theta_{00} &{}= 9.999988 \\\\
\cline{1-2}
%
\llap{$\log \tan (\phi_{3} - \phi_{2})$} &{}= 0.603216 \\\\
\phi_{3} - \phi_{2} &{}= \rlap{$104°\ 0'\ 1''.5$} \\\\
& \\\\
%
\phi_{3} &{}= \rlap{$208°\ 0'\ 1''.65$}
\end{array}
\]

Since $\dfrac{\phi_{2}}{4} = 26°\ 0'\ 0''.04$ and $\dfrac{\phi_{3}}{8} = 26°\ 0'\ 0''.21$,
we need not calculate~$\phi_{4}$.
\[
\frac{\phi_{3}}{8} = 93600''.21.
\]

Reducing this to radians, we have
\[
\log \frac{\phi_{3}}{8} = 9.656852.
\]
%% -----File: 110.png---Folio 104-------

Substituting in \Eqref{eq.}{IV}{(23)}, Chap.~IV, we have, since $\cos \theta_{03} = 1$,
\[
\begin{array}{@{}r@{}c@{}l@{}}
\llap{$\ac$} \log \cos \theta &{}={}& 0.150515 \\\\
\log \cos \theta_{0}  &{}={}& 9.993512 \\\\
\log \cos \theta_{00} &{}={}& 9.999988 \\\\
\cline{1-3}
%
&& 0.144014 \\\\
&& 0.072007
  \rlap{${} = \log\sqrt{\dfrac{\cos \theta_{0} \cos \theta_{00}}{\cos \theta}}$} \\\\
\log \dfrac{\phi_{3}}{8} &{}={}& 9.656852 \\\\
\cline{3-3}
%
\log u &{}={}& 9.728859 \\\\
u &{}={}& 0.535623\rlap{,\quad\text{\textit{Ans.}}}
\end{array}
\]

When $\theta = \sin^{-1} k > 45°$. %[** PP: Scan unclear]

\Example. Given $k = \sin 75°$, $\tan \phi = \sqrt{\dfrac{2}{\sqrt{3}}}$. To find~$F(k, \phi)$.

*First Method. Bisected Amplitudes.*

By \Eqref{equations}{IV}{(24)} and~\Eqref{}{IV}{(25)}, Chap.~IV, we get
\begin{align}
\PadTo[l]{\phi_{\frac{1}{32}}}{\phi}
  &= 47°\ \Z3'\ 30''.91,                   &       & \\\\
%
\PadTo[l]{\phi_{\frac{1}{32}}}{\phi_{\frac{1}{2}}}
  &= 25°\ 36'\ \Z5''.64, &
\PadTo[l]{\beta_{04}}{\beta} &= 45°; \\\\
%
\PadTo[l]{\phi_{\frac{1}{32}}}{\phi_{\frac{1}{4}}}
  &= 13°\ \Z6'\ 30''.98, &
\PadTo[l]{\beta_{04}}{\beta_{0}}  &= 24°\ 40'\ 10''.94; \\\\
%
\PadTo[l]{\phi_{\frac{1}{32}}}{\phi_{\frac{1}{8}}}
  &= \Z6°\ 35'\ 40''.74, &
\beta_{00} &= 12°\ 39'\ 15''.83; \\\\
%
\PadTo[l]{\phi_{\frac{1}{32}}}{\phi_{\frac{1}{16}}}
  &= \Z3°\ 18'\ \Z8''.75, &
\beta_{03} &= \Z6°\ 22'\ \Z8''.40; \\\\
%
\phi_{\frac{1}{32}} &= \Z1°\ 39'\ \Z7''.43, &
\beta_{04} &= {}
\end{align}

Substituting in \Eqref{equation}{IV}{(26)}, Chap.~IV, we have
\begin{align}
F(k, \phi)
  &= 32 × 1°\ 39'\ 7''.43 \\\\
  &= 52°\ 51'\ 58''.03 \\\\
  &= 0.9226878.\quad \text{\textit{Ans.}}
\end{align}
%% -----File: 111.png---Folio 105-------

*Second Method.* \Eqref{Equation}{IV}{(29)}, Chap.~IV.

From \Eqref[18sub3]{equations}{IV}{(18_{3})}, Chap.~IV, we have
\[
\begin{array}{r@{}l@{}l@{\;}c}
&&& \log \\\\
k       &{}= \cos \eta &\begin{aligned}{}= \cosP 15°\ \Z0'\ \Z0''.00\end{aligned} & 9.9849438 \\\\
k'      &{}= \sin \eta &\begin{aligned}{}= \sinP 15°\ \Z0'\ \Z0''.00\end{aligned} & 9.4129962 \\\\
k_{0}'  &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \eta \\\\
           &\sin \eta_{0}
         \end{aligned} &
         \begin{aligned}
           {}= \tan^{2} \Z7°\ 30'\ \Z0''.00 \\\\
           {}= \sinP    \Z0°\ 59'\ 35''.25
         \end{aligned}\;\biggr\} &
         8.2388582 \\\\
k_{1}   &{}= \cos \eta_{0} &\begin{aligned}{}= \cosP \Z0°\ 59'\ 35''.25\end{aligned} & 9.9999348 \\\\
k'_{00} &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \eta_{0} \\\\
           &\sin \eta_{00}
         \end{aligned}&
         \begin{aligned}
           {}= \tan^{2} \Z0°\ 29'\ 47''.62 \\\\
           {}= \sinP \Z0°\ \Z0'\ 15''.49
         \end{aligned}\;\biggr\} &
         5.8757219 \\\\
k_{2} &{}= \cos \eta_{00} &\begin{aligned}{}= \cosP \Z0°\ \Z0'\ 15''.49\end{aligned} &  0.0000000 \\\\
k'_{03} &{}= \left(\tfrac{1}{2} k'_{00}\right)^{2} && 1.1493838
\end{array}
\]

From \Eqref[18sub2]{equations}{IV}{(18_{2})}, Chap.~IV, we get
\begin{align}
\phi &= 47°\ 3'\ 30''.95; \\\\
2 \phi_{0} - \phi &= 45°; \\\\
\phi_{0} &= 46°\ 1'\ 45''.475; \\\\
\phi_{02} &= 46°\ 1'\ 29''.41; \\\\
\phi_{03} &= 46°\ 1'\ 29''.41; \\\\
45° + \tfrac{1}{2} \phi_{3} &= 68°\ 0'\ 44''.705.
\end{align}

Substituting these values in \Eqref{eq.}{IV}{(29)}, Chap.~IV, we get
\begin{align}
F(k, \phi)
  &= \sqrt{\frac{k_{1}}{k}} · \frac{1}{M} · \log \tan 68°\ 0'\ 44''.705 \\\\
  &= 0.9226877.\quad\text{\textit{Ans.}}
\end{align}

*Third Method.* \Eqref{Equation}{IV}{\DPtypo{(23)^*}{(23)}}, Chap.~IV\@.
%% -----File: 112.png---Folio 106-------

From \Eqref[14sub1]{equations}{IV}{(14_{1})}, Chap.~IV, we have
\[
\begin{array}{r@{}l@{}l@{\;}c}
&&& \log \\\\ % [** Moving to prev. line, cf. prev. page]
k       &{}= \sin \theta &\begin{aligned}{}= \sinP 75°\ \Z0'\ \Z0''\phantom{.00}\end{aligned}  & 9.9849438 \\\\
k'      &{}= \cos \theta &\begin{aligned}{}= \cosP 75°\phantom{\ 00'\ 00''.00}\end{aligned}  & 9.4129962 \\\\
k_{0}   &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta \\\\
           &\sin \theta_{0}
         \end{aligned} &
         \begin{aligned}
           &{}= \tan^{2} 37°\ 30' \\\\
           &{}= \sinP 36°\ \Z4'\ 16''.47
         \end{aligned}\;\biggr\} &
         9.7699610 \\\\
k_{1}'  &{}= \cos \theta_{0} && 9.9075648 \\\\
k_{02}  &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta_{0} \\\\
           &\sin \theta_{00}
         \end{aligned} &
         \begin{aligned}
           &{}= \tan^{2} 18°\ \Z2'\ 8''.235 \\\\
           &{}= \sinP \Z6°\ \Z5'\ 9''.38
       \end{aligned}\;\biggr\} &
       9.0253880 \\\\
k_{2}'  &{}= \cos \theta_{00} && 9.9975452 \\\\
k_{03}  &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta_{00} \\\\
           &\sin \theta_{03}
         \end{aligned} &
         \begin{aligned}
           &{}= \tan^{2} \Z3°\ \Z2'\ 34''.69 \\\\
           &{}= \sinP \phantom{00°}\ \Z9'\ 42''.90
       \end{aligned}\;\biggr\} &
       7.4511672 \\\\
k'_{3} &{}= \cos \theta_{03} && 9.9999982 \\\\
k_{04} &{}= \left(\tfrac{1}{2} k_{03}\right)^{2} && 4.3002761 \\\\
k_{4}' &{}={} && 0.0000000
\end{array}
\]

From \Eqref[14sub2]{equations}{IV}{(14_{2})}, Chap.~IV, we have
\begin{align}
\phi &= \Z47°\ \Z3'\ 30''.94; \\\\
\phi_{1} &= \Z62°\ 36'\ \Z3''.10; \\\\
\phi_{2} &= 119°\ 55'\ 47''.67; \\\\
\phi_{3} &= 240°\ \Z0'\ \Z0''.19; \\\\
\phi_{4} &= 480°\ \Z0'\ \Z0''.
\end{align}
Therefore the limit of $\phi$, $\dfrac{\phi_{1}}{2}$, $\dfrac{\phi_{2}}{4}$, or~$\dfrac{\phi_{n}}{2^{n}}$ is $30° = \dfrac{\pi}{6}$.

Substituting these values in \Eqref{eq.}{IV}{\DPtypo{(23)^*}{(23)}}, Chap.~IV, we have
\begin{align}
F(k, \phi)
  &= \sqrt{\frac{k_{1}' k_{2}' k_{3}' k_{4}'}{k'}} · \frac{\pi}{6} \\\\
  &= 0.9226874.\quad\text{\textit{Ans.}}
\end{align}

\Example. Given $\phi = 30°$, $k = \sin 89°$. Find~$u$.

Method of \Eqref{eq.}{IV}{(28)}, Chap.~IV\@.
%% -----File: 113.png---Folio 107-------

From \Eqref[18sub1]{eqs.}{IV}{(18_{1})} we find
\[
k_{1} = \sin \theta_{1}\quad \text{and}\quad
\tan^{2} \tfrac{1}{2} \theta_{1} = k = \sin \theta,
\]
from which we find that $k_{1} = 1$ as far as seven decimal places.

From \Eqref[18sub2]{eqs.}{IV}{(18_{2})} we have
\[
\begin{array}{r@{}c@{}l@{}}
\sin \phi &{}={}& 9.6989700 \\\\
k &{}={}& 9.9999338 \\\\
\cline{3-3}
%
\sin (2 \phi_{0} - \phi) &{}={}& 9.6989038 \\\\
2 \phi_{0} - \phi &{}={}& \rlap{$29°\ 59'.69733$} \\\\
2 \phi_{0} &{}={}& \rlap{$59°\ 59'.69733$} \\\\
45° + \tfrac{1}{2} \phi_{0}\footnotemark &{}={}& \rlap{$59°\ 59'.92433$} \\\\
\log \left(45° + \tfrac{1}{2} \phi_{0}\right) &{}={}& 0.2385385
\end{array}
\]
\footnotetext{Since $k_{1} = 1$, $\phi_{00} = \phi_{0}$, and we need not carry the calculation further.}%

From \Eqref[18sub3]{eqs.}{IV}{(18_{3})}, Chap.~IV, we have
\[
k = \cos \eta = \cos 1°,\qquad \tfrac{1}{2} \eta = 30'.
\]

Substituting in \Eqref{eq.}{IV}{(28)}, Chap.~IV, we have
\[
\begin{array}{r@{}c@{}l@{}}
\ac \log \cos \tfrac{1}{2} \eta && 0.0000330 \\\\
\log \log \left(45° + \tfrac{1}{2} \phi_{0}\right) && 9.3775585 \\\\
\ac \log M && 0.3622157 \\\\
\cline{3-3}
%
\log F(k, \phi) &{}={}& 9.7398072 \\\\
F(k, \phi) &{}={}& 0.549297\PadTo[l]{0}{.}\rlap{\quad\text{\textit{Ans.}}}
\end{array}
\]

\Example. Given $\phi = 79°$, $k = 0.25882$. Find~$u$. \\\\
\null\hfill\textit{Ans.} $u = 0.39947$.

\Example. Given $\phi = 37°$, $k = 0.86603$. Find~$u$. \\\\
\null\hfill\textit{Ans.} $u = 0.68141$.
%% -----File: 114.png---Folio 108-------


\Chapter[Numerical Calculations. phi.]{XV}{Numerical Calculations. $\phi$.}

\Example. Given $u = 1.368407$, $\theta = 38°$. Find~$\phi$.

*First Method.* From \Eqref{eqs.}{IX}{(46)} \Eqref[41st]{and}{IX}{(41)^*}, Chap.~IX, we have
\begin{align}
u &= x \Theta^{2}(K), \\\\
\Delta \phi &= \sqrt{k'} \frac{\Theta_{1}(x)}{\Theta (x)}.
\end{align}

From \Eqref{equations}{XII}{(5)}, Chap.~XII, and~\Eqref{}{IX}{(38)}, Chap.~IX, we
have
\[
\begin{array}{r@{}c@{}l@{}}
\log q &{}={}& 8.4734187 \\\\
\log \Theta^{2}(K) &{}={}& 0.0501955 \\\\
\log u &{}={}& 0.1362153 \\\\
\cline{3-3}
%
\log x &{}={}& 0.0860198 \\\\
x &{}={}& \rlap{$69°\ 50'\ 46''.12$}
\end{array}
\]

From \Eqref{equations}{IX}{(23)} and~\Eqref{}{IX}{(24)}, Chap.~IX, we get
\[
\begin{array}{r@{}c@{}l@{}}
\log \Theta_{1}(x) &{}={}& 9.9798368 \\\\
\log \Theta (x) &{}={}& 0.0192687 \\\\
\cline{3-3}
%
&& 9.9605681 \\\\
\log \sqrt{k'} &{}={}& 9.9482661 \\\\
\cline{3-3}
%
\log \Delta \phi &{}={}& 9.9088342 \rlap{${} = \log \sin \lambda$}
\end{array}
\]

But
\begin{align}
k^{2} \sin^{2} \phi &= 1 - \Delta^{2} \phi, \\\\
k \sin \phi &= \cos \lambda;
\end{align}
%% -----File: 115.png---Folio 109-------
whence
\[
\begin{array}{r@{}c@{}l@{}}
\log \cos \lambda &{}={}& 9.7675483 \\\\
\log k &{}={}& 9.7893420 \\\\
\cline{3-3}
%
\log \sin \phi &{}={}& 9.9782063 \\\\
\phi &{}={}& \rlap{$72°$.\quad\text{\textit{Ans.}}}
\end{array}
\]

*Second Method.* From \Eqref{eq.}{VI}{(1)}, Chap.~VI\@.

From \Eqref[14sub1]{eqs.}{IV}{(14_{1})} Chap.~IV, we find
\[
\begin{array}{r@{}l@{}l@{\;}c}
&&& \log \\\\ %[** log on its own line, as on 113]
\PadTo[l]{k_{00}}{k_{0}}   &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta\\
           &\sin \theta_{0}
         \end{aligned} &
         \begin{aligned}
           {}= \tan^{2} 19°\phantom{\ 48'.54569} \\\\
           {}= \sinP \Z6°\ 48'.54569
         \end{aligned}\;\biggr\} &
         9.0739438 \\\\
        & \phantom{{}={}}\quad \begin{aligned}\cos \theta_{0}\end{aligned} && 9.9969260 \\\\
%
k_{00}  &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta_{0} \\\\
           &\sin \theta_{00}
         \end{aligned} &
         \begin{aligned}
           {}= \tan^{2} \Z3°\ 24'.2784\Z \\\\
           {}= \DPtypo{\phantom{\sinP}}{\sinP} \phantom{00°}\ 12'.16659
         \end{aligned}\;\biggr\} &
         7.5488952 \\\\
        &\phantom{{}={}}\quad \begin{aligned}\cos \theta_{00}\end{aligned} &&9.9999974 \\\\
%
k_{03}  &{}= \biggl\{\begin{aligned}
           &\tan^{2} \tfrac{1}{2} \theta_{00} \\\\
           &\sin \theta_{03}
         \end{aligned} &
         \begin{aligned}
           {}= \tan^{2} \phantom{00°}\ \Z6'.08329 \\\\
           {}
         \end{aligned}\;\biggr\} &
         4.4957316 \\\\
        &\phantom{{}={}}\quad \begin{aligned}\cos \theta_{03}\end{aligned} &&0.0000000
\end{array}
\]

Substituting these values in \Eqref{eq.}{VI}{(1)}, Chap.~VI, we have
\[
\begin{array}{r<{\quad}@{}l@{}}
\log \cos \theta_{0}  & 9.9969260 \\\\
\log \cos \theta_{00} & 9.9999974 \\\\
\cline{2-2}
%
& 9.9969234 \\\\
\log \sqrt{\cos \theta_{0} \cos \theta_{00}} & 9.9984617 \\\\
\ac \log \PadTo{\cos \theta_{0}}{\text{``}}
         \PadTo{\cos \theta_{00}}{\text{``}} & 0.0015383 \\\\
\log u & \Z.1362153 \\\\
\log \sqrt{\cos \theta} & 9.9482660 \\\\
\log 2^{3} & \Z.9030900\rlap{\footnotemark} \\\\
\ac \log \sqrt{\cos \theta_{0} \cos \theta_{00}} & 0.0015383 \\\\
\cline{2-2}
%
& 0.9891096 \\\\
& 2.2418773 \\\\
\cline{2-2}
%
\log \phi_{3}\addtocounter{footnote}{-1}\footnotemark & 2.7472323 \\\\
\phi_{3} & \rlap{$558°\ 46'.140$}
\end{array}
\]
\footnotetext{$n$~is taken equal to~$3$, because $\cos\DPtypo{}{\theta}_{03} = 1$.}
%% -----File: 116.png---Folio 110-------

Whence, by \Eqref{equations}{VI}{\DPtypo{(1)^*}{(1)}} of Chap.~VI, we get
\[
\begin{array}{r@{}c@{}l@{}}%[** PP: Re-aligning first group]
k_{03} \log &{}={}& 4.4957316 \\\\
\sin \phi_{3} && 9.5075232_{n} \\\\
\cline{3-3}
%
\sin (2 \phi_{2} - \phi_{3}) && 4\DPtypo{\,}{.}0032548_{n} \\\\
2 \phi_{2} - \phi_{3} &{}={}& -0'.00346 \\\\
\phi_{2} &{}={}& \rlap{$279°\ 23'.06827$}
\end{array}
\]
%
\[
\begin{array}{r@{}c@{}l@{}}
k_{00} \log &{}={}& 7.5488952 \\\\
\sin \phi_{2} && 9.9941484_{n} \\\\
\cline{3-3}
\sin (2 \phi_{1} - \phi_{2}) && 7.5430436_{n} \\\\
2 \phi_{1} - \phi_{2} &{}={}& -12'.0039 \\\\
\phi_{1} &{}={}& \rlap{$139°\ 35'.5321$}
\end{array}
\]
%
\[
\begin{array}{r@{}c@{}l@{}}
k_{0} \log &{}={}& 9.0739438 \\\\
\sin \phi_{1} && 9.8117249 \\\\
\cline{3-3}
\sin (2 \phi - \phi_{1}) && 8.8856687 \\\\
2 \phi - \phi_{1} &{}={}& \rlap{$\Z4°\ 24'.467$} \\\\
\phi &{}={}& \rlap{$71°\ 59'.9999$} \\\\
     &{}={}& \rlap{$72°$.\quad\text{\textit{Ans.}}}
\end{array}
\]

\Example. Given $u = 2.41569$, $\theta = 80°$. Find~$\phi$. \\\\
\null\hfill\textit{Ans.} $\phi = 82°$.

\Example. Given $u = 1.62530$, $k = \frac{1}{2}$. Find~$\phi$. \\\\
\null\hfill\textit{Ans.} $\phi = 87°$.
%% -----File: 117.png---Folio 111-------


\Chapter[Numerical Calculations. E(k, phi).]{XVI}
{Numerical Calculations. $E(k, \phi)$.}

*First Method.* By Chap.~X, \Eqref{eqs.}{X}{(15)},~\Eqref{}{X}{(16)}, and~\Eqref{}{X}{(17)}.

\Example. Given $k = 0.9327$, $\phi = 80°$. Find $E(k, \phi)$.

By \Eqref{eq.}{X}{(15)}, Chap.~X,
\[
\begin{array}{l@{}c@{}l<{\qquad\qquad}l@{}c@{}l}
\phi              &{}={}&  80°;   &
    \gamma              &{}={}& 67°\ 44'.\Z; \\\\
\phi_{\frac{1}{2}}  &{}={}&  50° 43'.6, &
    \gamma_{\frac{1}{2}}  &{}={}& 46°\ 40'.4; \\\\
\phi_{\frac{1}{4}}  &{}={}&  27° 48'.5, &
    \gamma_{\frac{1}{4}}  &{}={}& 26°\ \Z0'.1; \\\\
\phi_{\frac{1}{8}}  &{}={}&  14° 16'.7, &
    \gamma_{\frac{1}{8}}  &{}={}& 13°\ 24'.0; \\\\
\phi_{\frac{1}{16}} &{}={}& \Z7° 11'.3, &
    \gamma_{\frac{1}{16}} &{}={}& \Z6°\ 45'.2; \\\\
\phi_{\frac{1}{32}} &{}={}& \Z3° 36'.0, &
    \llap{$\log \sin{}$} \gamma_{\frac{1}{32}} &{}={}& 8.77094; \\\\
\phi_{\frac{1}{32}} &{}={}& 0.062831.   && \\\\
\llap{$\therefore$ } \phi^{5}_{\frac{1}{32}} &{}<{}& 0.0000001. &&
\end{array}
\]
Whence, by \Eqref{eq.}{X}{(17)},
\[
\begin{array}{r@{}c@{}l@{}}
E(k, \phi_{\frac{1}{32}}) &{}={}& 0.06279\rlap{$4$} \\\\
\PadTo[l]{\sin \phi_{\frac{1}{16}}}{\sin \phi}
  \PadTo[l]{\sin^{2} \gamma_{\frac{1}{32}}}{\sin^{2} \gamma_{\frac{1}{2}}} &{}={}& 0.52116 \\\\
2\, \PadTo[l]{\sin \phi_{\frac{1}{16}}}{\sin \phi_{\frac{1}{2}}}
  \PadTo[l]{\sin^{2} \gamma_{\frac{1}{32}}}{\sin^{2} \gamma_{\frac{1}{4}}} &{}={}& 0.29757 \\\\
4\, \PadTo[l]{\sin \phi_{\frac{1}{16}}}{\sin \phi_{\frac{1}{4}}}
  \PadTo[l]{\sin^{2} \gamma_{\frac{1}{32}}}{\sin^{2} \gamma_{\frac{1}{8}}} &{}={}& 0.10023 \\\\
8\, \PadTo[l]{\sin \phi_{\frac{1}{16}}}{\sin \phi_{\frac{1}{8}}}
  \sin^{2} \gamma_{\frac{1}{16}} &{}={}& 0.02728 \\\\
16 \sin \phi_{\frac{1}{16}} \sin^{2} \gamma_{\frac{1}{32}} &{}={}& 0.00697 \\\\
\cline{3-3}
&& 0.95321
\end{array}
\]
Hence, by \Eqref{eq.}{X}{(16)},
\begin{align}
E(k, \phi)
  &= 32E(k, \phi_{\frac{1}{32}}) - 0.95321 \\\\
  &= 2.0094 - 0.9532 = 1.0562.
\end{align}
%% -----File: 118.png---Folio 112-------

*Second Method.* By Chap.~X, \Eqref{eq.}{X}{(26)}.

\Example. Given $k = \sin 75°$, $\tan \phi = \sqrt{\dfrac{2}{\sqrt{3}}}$. Find~$E(k, \phi)$.

From \Eqref[14sub1]{eqs.}{IV}{(14_{1})}, Chap.~IV, we have
\begin{align}%XXXX
k  &= \sin \theta = \sin 75°\ 0'\ 0'' & \log ={}& 9.9849438 \\\\
k' &= \cos \theta = \cos 75°                 && 9.4129962 \\\\
k_{0}
   &= \biggl\{
\begin{aligned}
  \tan^{2} \tfrac{1}{2} \theta &= \tan^{2} 37°\ 30' \\\\
  \PadTo[l]{\tan^2 \tfrac{1}{2} \theta}{\sin \theta_{0}} &= \PadTo[l]{\tan^2}{\sin}\ 36°\ \Z4'\ 16''.47
\end{aligned}
\biggr\} && 9.7699610 \\\\
k_{1}' &= \cos \theta_{0} && 9.9075648 \\\\
k_{02} &= \biggl\{
\begin{aligned}
  \tan^{2} \tfrac{1}{2} \theta_{0} &= \tan^{2} 18°\ \Z2'\ \Z8''.235 \\\\
  \PadTo[l]{\tan^2 \tfrac{1}{2} \theta_{0}}{\sin \theta_{00}} &= \PadTo[l]{\tan^2}{\sin}\ \Z6°\ \Z5'\ \Z9''.38
\end{aligned}
\biggr\} && 9.0253880 \\\\
k_{2}' &= \cos \theta_{00} && 9.9975452 \\\\
k_{03} &= \biggl\{
\begin{aligned}
  \tan^{2} \tfrac{1}{2} \theta_{00} &= \tan^{2} \Z3°\ \Z2'\ 34''.69 \\\\
  \PadTo[l]{\tan^2 \tfrac{1}{2} \theta_{00}}{\sin \theta_{03}} &= \PadTo[l]{\tan^2 22°}{\sin}\ \Z9'\ 42''.90
\end{aligned}
\biggr\} && 7.4511672 \\\\
k_{3}' &= \cos \theta_{03} && 9.9999982 \\\\
k_{04} &= \left(\tfrac{1}{2}k_{03}\right)^{2} && 4.3002761 \\\\
k_{4}' &={} && 0.0000000
\end{align}

From \Eqref[14sub2]{eqs.}{IV}{(14_{2})}, Chap.~IV, we have
\begin{align}
\phi &= \Z47°\ \Z3'\ 30''.94; \\\\
\phi_{1} &= \Z62°\ 36'\ \Z3''.10; \\\\
\phi_{2} &= 119°\ 55'\ 47''.67; \\\\
\phi_{3} &= 240°\ \Z0'\ \Z0''.19.
\end{align}
%% -----File: 119.png---Folio 113-------

Applying \Eqref{eq.}{X}{(26)}, Chap.~X, we have
\[
\begin{array}{rr@{}l@{}c<{\qquad}@{}c@{}}
k^{2} & \log  ={}& 9.9698876 && \\\\
\ac 2 & & 9.6989700 && \\\\
\cline{3-3}
                 & & 9.6688576 && .4665064
\end{array}
\]
\[
\begin{array}{rr@{}l@{}c<{\qquad}@{}c@{}}
k_{0} & \phantom{\log  ={}} & 9.7699610 && \\\\
\ac 2 & & 9.6989700 && \\\\
\cline{3-3}
                 & & 9.1377886 && .1373373
\end{array}
\]
\[
\begin{array}{rr@{}l@{}c<{\qquad}@{}c@{}}
k_{00}& \phantom{\log  ={}} & 9.0253880 && \\\\
\ac 2 & & 9.6989700 && \\\\
\cline{3-3}
                 & & 7.8621466 && .0072802
\end{array}
\]
\[
\begin{array}{rr@{}l@{}c<{\qquad}@{}c@{}}
k_{03}& \phantom{\log  ={}} & 7.4511672 && \\\\
\ac 2 & & 9.6989700 && \\\\
\cline{3-3}
                 & & 5.0132838 && .0000103 \\\\
\cline{5-5}
                 & &           && .6111342
\end{array}
\]
\[
1 - .6111342 = 0.3888658.
\]

From \Eqref{eq.}{IV}{\DPtypo{(23)^*}{(23)}}, Chap.~IV, we find $F(k, \phi) = 0.9226874$.

Hence
\[
\begin{array}{r@{}l@{}c@{}} %[** PP: Re-aligning first equation]
F(k, \phi)
  \left[1 - \dfrac{k^{2}}{2} \left(1 + \dfrac{k_{0}}{2} + \dotsb\right)\right]
  &{}=& 0.3588016 \\\\[4pt]
\dfrac{k \sqrt{k_{0}}}{2} \sin \phi_{1}
  &{}=& 0.3290186 \\\\[4pt]
\dfrac{k \sqrt{k_{0}k_{00}}}{4} \sin \phi_{2}
  &{}=& 0.0522872 \\\\[4pt]
\dfrac{k \sqrt{k_{0}k_{02}k_{03}}}{8} \sin \phi_{3}
  &{}= -& 0.0013888 \\\\[4pt]
\dfrac{k \sqrt{k_{0} \dotsm k_{04}}}{16} \sin \phi_{4}
  &{}=& 0.0000010 \\\\[4pt]
\cline{3-3}
  && 0.3799180
\end{array}
\]
%% -----File: 120.png---Folio 114-------
Whence
\[
E(k, \phi) = 0.3588016 + 0.3799180 = 0.7387196.\quad\textit{Ans.}
\]

\Example. Given $k = \sin 75°$. Find~$E\left(k, \dfrac{\pi}{2}\right)$.

From Example~2, Chap.~XIII, we find
\[
\begin{array}{r@{}c@{}l@{}}
\log F\left(k, \dfrac{\pi}{2}\right) &{}={}& 0.4421761 \\\\
\log 0.3888658 &{}={}& 1.5897998 \\\\
\cline{3-3}
\log E \left(k, \dfrac{\pi}{2}\right) &{}={}& 0.0319759 \\\\
E\left(k, \frac{\pi}{2}\right) &{}={}& 1.076405\rlap{.\quad\text{\textit{Ans.}}}
\end{array}
\]

\Example. Given $k = \sin 30°$, $\phi = 81°$. Find~$E(k, \phi)$. \\\\
\null\hfill\textit{Ans.} $E(k, \phi) = 1.33124$.

\Example. Find~$E(\sin 80°, 55°)$. \\\\
\null\hfill\textit{Ans.} $0.82417$.

\Example. Find~$E\left(\sin 27°, \dfrac{\pi}{2}\right)$. \\\\
\null\hfill\textit{Ans.} $1.48642$.

\Example. Find~$E(\sin 19°, 27°)$. \\\\
\null\hfill\textit{Ans.} $0.46946$.
%% -----File: 121.png---Folio 115-------


