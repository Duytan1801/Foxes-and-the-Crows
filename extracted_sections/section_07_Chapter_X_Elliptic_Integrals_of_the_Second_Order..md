# Chapter X: Elliptic Integrals of the Second Order.

Lines: 3677-4105

\Chapter{X}{Elliptic Integrals of the Second Order.}

\First{From} Chap.~I, \Eqref{equation}{I}{(19)}, we have
\[
E(k, \phi) = \int_{0}^{\phi} \sqrt{1 - k^{2} \sin^{2} \phi} · d\phi
  = \int_{0}^{\phi} \Delta \phi · d\phi.
\]

From this we have
\[
E(\phi) + E(\psi)
  = \int_{0}^{\phi} \Delta \phi · d\phi + \int_{0}^{\psi} \Delta \phi · d\phi.
\]

Put
\[
\Tag{(1)}
E\phi + E\psi = S.
\]

Differentiating, we get
\[
\Tag{(2)}
\Delta \phi · d\phi + \Delta \psi · d\psi = dS.
\]
But we have, Chap.~II, \Eqref{equation}{II}{(2)},
\[
\frac{d\phi}{\Delta \phi} + \frac{d\psi}{\Delta \psi} = 0,
\]
or
\[
\Tag{(3)}
\Delta \psi · d\phi + \Delta \phi · d\psi = 0.
\]

Adding equations \Eqref{}{}{(2)}~and~\Eqref{}{}{(3)}, we get
\[
\Tag{(4)}
(\Delta \phi + \Delta \psi)(d\phi + d\psi) = dS.
\]
%% -----File: 088.png---Folio 82-------

Substituting $\cos \mu$ from \Eqref{eq.}{II}{(5)}, in \Eqref[5st]{eq.}{II}{(5)^*}, Chap.~II, we get
\[
\Tag{(5)}
\left\{
\begin{aligned}
\Delta\phi
  &= \frac{\sin\phi \cos\psi\, \Delta\mu + \cos\phi \sin\psi}{\sin\mu}, \\\\
\Delta\psi
  &= \frac{\sin\psi \cos\phi\, \Delta\mu + \cos\psi \sin\phi}{\sin\mu};
\end{aligned}
\right.
\]
whence
\[
\Tag{(6)}
\Delta \phi ± \Delta \psi = \frac{\Delta \mu ± 1}{\sin \mu} \sin (\phi ± \psi).
\]

Substituting in \Eqref{equation}{}{(4)}, we have
\begin{align}
dS &= \frac{\Delta \mu + 1}{\sin \mu} \sin (\phi + \psi)\,d(\phi + \psi) \\\\
\Tag{(7)}
   &= - \frac{\Delta \mu + 1}{\sin \mu}\,d \cos (\phi + \psi).
\end{align}
Integrating equation~\Eqref{}{}{(7)}, we have
\[
E\phi + E\psi = \frac{\Delta \mu + 1}{\sin \mu} \left[C - \cos (\phi + \psi)\right].
\]

The constant of integration,~$C$, is determined by making
$\phi = 0$; in this case $\psi = \mu$, $E\phi = 0$, $E\psi = E\mu$, and $S = E\mu$;
whence
\[
E\mu = \frac{\Delta \mu + 1}{\sin \mu} (C - \cos \mu),
\]
and by subtraction,
\[
E\phi + E\psi - E\mu
  = \frac{\Delta \mu + 1}{\sin \mu}
    (\cos \mu - \cos \phi \cos \psi + \sin \phi \sin \psi).
\]
But, Chap.~II, \Eqref{eq.}{II}{(5)},
\[
\cos\mu - \cos\phi \cos\psi = - \sin\phi \sin\psi\, \Delta\mu;
\]
%% -----File: 089.png---Folio 83-------
whence
\[
E\phi + E\psi - E\mu = \frac{1 - \Delta^{2}\mu}{\sin \mu} \sin \phi \sin \psi
\]
whence
\[
\Tag{(8)}
E\phi + E\psi = E\mu + k^{2} \sin\phi \sin\psi \sin\mu.
\]

When $\phi = \psi$, we have
\begin{align}
\Tag{(9)}
E\mu &= 2E\phi - k^{2} \sin^{2} \phi \sin\mu. \\\\
\intertext{But in that case}
\Tag{(10)}
\cos \mu &= \cos^{2} \phi - \sin^{2} \phi\, \Delta \mu; \\\\
\intertext{whence}
\Tag{(11)}
\sin \phi &= \sqrt{\frac{1 - \cos \mu}{1 + \Delta \mu}}.
\end{align}

Let $\phi$, $\phi_{\frac{1}{2}}$, $\phi_{\frac{1}{4}}$,~etc., be such values as will satisfy the equations
\begin{align}
\Tag{(12)}
E\phi
  &= 2E\phi_{\frac{1}{2}} - k^{2} \sin^{2} \phi_{\frac{1}{2}} \sin \phi,\\
E\phi_{\frac{1}{2}}
  &= 2E\phi_{\frac{1}{4}} - k^{2} \sin^{2} \phi_{\frac{1}{4}} \sin \phi_{\frac{1}{2}},\\
  &\PadTo{= 2E\phi_{\frac{1}{4}}}{\text{etc.}}
   \PadTo{ - k^{2} \sin^{2} \phi_{\frac{1}{4}} \sin \phi_{\frac{1}{2}}}{\text{etc.}}
\end{align}

Assume an auxiliary angle~$\gamma$, such that
\[
\Tag{(13)}
\sin\gamma = k \sin\phi;
\]
whence
\[
\Delta\phi = \cos\gamma,
\]
and Chap.~IV, \Eqref{eq.}{IV}{(24)},
\[
\Tag{(14)}
\sin\phi_{\frac{1}{2}}
  = \frac{\sin \frac{1}{2}\phi}{\cos \frac{1}{2}\gamma}.
\]
%% -----File: 090.png---Folio 84-------

Applying eqs.\ \Eqref{}{}{(13)}~and~\Eqref{}{}{(14)} successively, we get
\[
\Tag{(15)}
\left\{
\begin{array}{r@{}l}
\sin \phi_{\frac{1}{2}}
  &{}= \dfrac{\sin \frac{1}{2} \phi}{\cos \frac{1}{2} \gamma},\quad
       \sin \gamma_{\frac{1}{2}} = k \sin \phi_{\frac{1}{2}}; \\\\
\sin \phi_{\frac{1}{4}}
  &{}= \dfrac{\sin \frac{1}{2} \phi_{\frac{1}{2}}}
             {\cos \frac{1}{2} \gamma_{\frac{1}{2}}},\quad
       \sin \gamma_{\frac{1}{4}} = k \sin \phi_{\frac{1}{4}}; \\\\
\Dots{2} \\\\
\sin \phi_{\frac{1}{2^{n}}}
  &{}= \dfrac{\sin \frac{1}{2} \phi_{\frac{1}{2^{n - 1}}}}
             {\cos \frac{1}{2} \gamma_{\frac{1}{2^{n - 1}}}};
\end{array}
\right.
\]
whence
\begin{align}%[** PP: Unbalanced parentheses in original]
\Tag{(16)}
E \phi &= 2^{n} E \phi_{\frac{1}{2^{n}}}
  - \Bigl(\sin \phi \sin^{2} \gamma_{\frac{1}{2}}
      + 2 \sin \phi_{\frac{1}{2}} \sin^{2} \gamma_{\frac{1}{4}} \\\\
  &+ 2^{2} \sin \phi_{\frac{1}{4}} \sin^{2} \gamma_{\frac{1}{8}} + \dotsb
    2^{n-1} \sin \phi_{\frac{1}{2^{n}}} \sin^{2} \gamma_{\frac{1}{2^{n - 1}}} \Bigr)
\end{align}

%[** PP: Modernizing factorial notation]
To find the limiting value, $E \phi_{\frac{1}{n}}$, we have, by the Binomial
Theorem, since $\sin \phi = 1 - \dfrac{\phi^{3}}{3!} + \dfrac{\phi^{5}}{5!} -{}$ etc.,
\begin{align}
\Delta \phi
  &= (1 - k^{2} \sin^{2} \phi)^{\frac{1}{2}}\\
  &= 1 - \frac{k^{2}}{2} \left( \phi - \frac{\phi^{3}}{6} \right)^{2}
%[** PP: Fourth power in next line missing in original]
       - \frac{k^{4}}{8} \left( \phi - \frac{\phi^{3}}{6} \right)^{4} + \dotsb\\
  &= 1 - \frac{k^{2}}{2} \phi^{2}
       + \left( \frac{k^{2}}{6} - \frac{k^{4}}{8} \right) \phi^{4}.
%[** PP: Series truncated to polynomial, presumably 4th power approximation]
\end{align}
Whence
\begin{align}
E k \phi_{\frac{1}{2^{n}}}
  &= \int_{0}^{\phi_{n}} \Delta \phi_{\frac{1}{2^{n}}}\, d\phi\\
\Tag{(17)}
  &= \phi_{\frac{1}{2^{n}}} - \frac{k^{2}}{6} \phi^{3}_{\frac{1}{2^{n}}}
     + \frac{k^{2}(4 - 3k^{2})}{120} \phi^{5}_{\frac{1}{2^{n}}}.
\end{align}
%% -----File: 091.png---Folio 85-------

Substituting in \Eqref{eq.}{}{(16)} the numerical values derived from
\Eqref{equations}{}{(15)} and~\Eqref{}{}{(17)}, we are enabled to determine the value
of~$E\phi$.

Landen's Transformation can also be applied to Elliptic
Integrals of this class.

From \Eqref{eq.}{IV}{(11)}, Chap.~IV, we get, by easy transformation,
\[
\Tag{(18)}
\sin^{2} 2\phi = \sin^{2} \phi_{1} (1 + k_{0} + 2k_{0} \cos 2\phi).
\]
From this we easily get
\begin{align}
2k_{0} \cos 2\phi \sin^{2} \phi_{1}
  &= \sin^{2} 2\phi - \sin^{2} \phi_{1} - k_{0}^{2} \sin^{2} \phi_{1} \\\\
  &= 1 - \cos^{2} 2\phi - \sin^{2} \phi_{1} - k_{0}^{2} \sin^{2} \phi_{1} \\\\
  &= \Delta^{2}k_{0}\phi_{1} - \sin^{2}\phi_{1} - \cos^{2}2\phi;
\end{align}
whence
\[
\cos^{2} 2\phi + 2k_{0} \sin^{2}\phi_{1} \cos 2\phi
  = \Delta^{2}k_{0}\phi_{1} - \sin^{2}\phi_{1};
\]
and from this,
\begin{align}
\cos 2\phi
  &= -k_{0} \sin^{2} \phi_{1}
     ± \sqrt{\Delta^{2}k_{0}\phi_{1} - \sin^{2} \phi_{1}
             + k_{0}^{2} \sin^{4} \phi_{1}} \\\\
\Tag{(19)}
  &= \cos \phi_{1} \Delta k_{0}\phi_{1} - k_{0} \sin^{2} \phi_{1};
\end{align}
whence, also,
\begin{align}
1 - \cos^{2} 2\phi
  &= 1 - \cos^{2} \phi_{1}\, \Delta^{2}\phi_{1}
       + 2k \sin^{2}\phi_{1} \cos \phi_{1}\, \Delta k_{0}\phi_{1}
       - k_{0}^{2} \sin^{4} \phi_{1} \\\\
  &= \sin^{2} \phi_{1}
     (1 + k_{0}^{2} \cos^{2} \phi_{1}
       + 2k_{0} \cos \phi_{1}\, \Delta k_{0}\phi_{1}
       - k_{0}^{2} \sin^{2} \phi_{1})
\end{align}
and
\[
\Tag{(20)}
\sin 2\phi = \sin \phi_{1} (\Delta k_{0}\phi_{1} + k_{0} \cos \phi_{1}).
\]

Differentiating \Eqref{equation}{}{(19)}, we get
\[
2 \sin 2\phi \frac{d\phi}{d\phi_{1}}
  = \sin \phi_{1}
    \frac{(k_{0} \cos \phi_{1} + \Delta k_{0}\phi_{1})^{2}}
         {\Delta k_{0} \phi_{1}}.
\]
Dividing this by \Eqref{equation}{}{(20)}, we have
\[
\frac{2d\phi}{d\phi_{1}}
  = \frac{k_{0} \cos \phi_{1} + \Delta k_{0}\phi_{1}}{\Delta k_{0}\phi_{1}}.
\]
%% -----File: 092.png---Folio 86-------
But from~\Eqref{}{}{(19)}, and \Eqref{eq.}{IV}{(6)}, Chap.~IV,
\begin{align}
k^{2} \sin^{2} \phi
  &= \frac{k^{2}(1 - \cos 2\phi)}{2} \\\\
  &= \frac{2k_{0}}{(1 + k_{0})^{2}}
     \{1 + k_{0} \sin^{2} \phi_{1} - \cos \phi_{1} \Delta k_{0} \phi_{1}\};
\intertext{whence}
\Delta k\, \phi
  &= \frac{\Delta k_{0}\phi_{1} + k_{0} \cos \phi_{1}}{1 + k_{0}},
\intertext{and}
2\Delta k\, \phi · \frac{d\phi}{d\phi_{1}}
  &= \frac{(k_{0} \cos \phi_{1} + \Delta k_{0}\, \phi_{1})^{2}}
          {(1 + k_{0}) \Delta k_{0}\, \phi_{1}},
\intertext{and}
d\phi\, \Delta k\, \phi
  &= \frac{d\phi_{1}}{\Delta k_{0} \phi_{1}}
   · \frac{(k_{0} \cos \phi_{1} + \Delta k_{0}\, \phi_{1})^{2}}{2(1 + k_{0})}.
\end{align}
This gives immediately, by integration,
\begin{align}
Ek\phi
  &= \frac{1}{2(1+k_{0})}
     \int \frac{d\phi_{1}}{\Delta k_{0}\, \phi_{1}}
          \{k_{0} \cos \phi_{1} + \Delta k_{0} \phi_{1}\}^{2} \\\\
  &=\frac{1}{2(1+k_{0})}
     \int \frac{d\phi_{1}}{\Delta k_{0}\, \phi_{1}}
          \{2\Delta^{2}k_{0}\, \phi_{1}
          + 2k_{0} \cos \phi_{1} \Delta k_{0}\phi_{1}
          - k_{1}'^{2}\} \\\\
\Tag{(21)}
  &= \frac{Ek_{0}\phi_{1}}{1+k_{0}}
   + \frac{k_{0} \sin \phi_{1}}{1+k_{0}}
   - \tfrac{1}{2} (1 - k_{0})Fk_{0}\phi_{1}.
\end{align}

Thus the value of~$Ek\phi$ is made to depend upon~$Ek_{0}\phi_{1}$
(containing a smaller modulus and a larger amplitude), and
upon the integral of the first class,~$Fk_{0}\phi_{1}$; $k_{0}$,~$\phi_{1}$,~etc., being
determined by the \Eqref{formulæ}{IV}{(6)} to~\Eqref{}{IV}{(12)} of Chap.~IV.

By successive applications of \Eqref{equation}{}{(21)}, $Ek\phi$~may be
made to depend ultimately upon~$Ek_{0n}\phi_{n}$, where $k_{0n}$~approximates
to zero and $Ek_{0n}\phi_{n}$ to~$\phi_{n}$.

Or, by reversing, it may be made to depend upon~$Ek_{n}\phi_{0n}$,
where $k_{n}$~approximates to unity and $Ek_{n}\phi_{0n}$ to~$-\cos \phi_{0n}$.
%% -----File: 093.png---Folio 87-------

To facilitate this, assume
\[
Gk\phi = Ek\phi - Fk\phi.
\]
Subtracting from \Eqref{equation}{}{(21)} the equation
\[
Fk\phi = \frac{1 + k_{0}}{2} Fk_{0}\phi_{1}
  \text{ (see \Eqref{eq.}{IV}{(13)}, Chap.~IV)},
\]
we have
\[
Gk\phi = \frac{1}{1 + k_{0}}
  (Gk_{0}\phi_{1} + k_{0} \sin \phi_{1} - k_{0}\, Fk_{0}\, \phi_{1}).
\]
Repeated applications of this give
\[
\begin{array}{r@{}l}
Gk_{0}\phi_{1}
  &{}= \dfrac{1}{1 + k_{00}}
     (Gk_{00}\phi_{2} + k_{00} \sin \phi_{2} - k_{00}\, Fk_{00}\, \phi_{2}),\\
\Dots{2} \\\\
\llap{$Gk_{0(n - 1)}\phi_{n - 1}$}
  &{}= \dfrac{1}{1 + k_{0n}} \rlap{$(Gk_{0n}\phi_{n}
       + k_{0n} \sin \phi_{n} - k_{0n}\, Fk_{0n}\, \phi_{n})$.}
\end{array}
\]
Whence
\[
\Tag{(22)}
Gk\phi = \sum_{n}^{1} %[** PP: \textstyle sum in original]
  \Biggl\{ \frac{k_{0n}(\sin \phi_{n} - Fk_{0n}\phi_{n})}
                {\Prodlim(1 + k_{0n})} \Biggr\}
  + \frac{Gk_{0n}\, \phi_{n}}{\Prodlim(1 + k_{0n})}.
\]
But since (compare \Eqref{eq.}{IV}{(13)}, Chap.~IV)
\[%[** PP: Next two displays aligned in original]
Fk\phi = \frac{Fk_{0n}\, \phi_{n}\Prodlim(1 + k_{0n})}{2^{n}},
\]
or
\[
\Tag{(23)}
\frac{Fk_{0n}\, \phi_{n}}{\Prodlim (1 + k_{0n})}
  = \frac{2^{n} Fk\, \phi}{\Prodlim(1 + k_{0n})^{2}};
\]
%% -----File: 094.png---Folio 88-------
and since, also, (compare \Eqref{eq.}{IV}{(6)}, Chap.~IV,)
\[
\frac{k^{2}_{0(n-1)}}{k_{0n}} = \frac{2^{2}}{(1 + k_{0n})^{2}},
\]
we have
\begin{align}
\Tag{(24)}
\frac{2^{n}k_{0n}}{\Prodlim(1 + k_{0n})^{2}}
  &= \frac{k_{0n}}{2^{n}} \Prodlim \frac{k^{2}_{0(n-1)}}{k_{0n}} \\\\
  &= \frac{k_{0n}}{2^{n}} \Prodlim \frac{k_{0(n-1)}}{k_{0n}} \Prodlim k_{0(n-1)} \\\\
  &= \frac{k_{0n}}{2^{n}} · \frac{k}{k_{0}} · \frac{k_{0}}{k_{00}} \dotsm \frac{k_{0(n-1)}}{k_{0n}} · k\Prodlim[2] k_{0(n-1)} \\\\
  &= \frac{k^{2}}{2^{n}} \Prodlim[2] k_{0(n-1)}.
\end{align}

Substituting these values in \Eqref{equation}{}{(22)}, and neglecting
the term containing $Gk_{0n}\phi_{n}$ since, carried to its limiting
value,
\begin{DPalign}
Gk_{0n}\phi_{n}
  &= Ek_{0n}\phi_{n} - Fk_{0n}\phi_{n} \\\\
  &= \phi_{n} - \phi_{n} = 0,
\rintertext{\llap{($n =$ limiting value,)}}
\end{DPalign}
we have
\begin{gather*}
\Tag{(25)}
Gk\phi = \sum_{n}^{1} \Biggl\{ \frac{k\sqrt{k_{0n}} \sin \phi_{n}
  \Prodlim[2] \sqrt{k_{0(n-1)}} - k^{2} \Prodlim[2] k_{0(n-1)}}{2^{n}}
  \Biggr\} \\\\
  \begin{aligned}
  &= k \left[\frac{\sqrt{k_{0}}}{2} \sin \phi_{1}
           + \frac{\sqrt{k_{0}k_{00}}}{2^{2}} \sin \phi_{2}
           + \frac{\sqrt{k_{0}k_{00}k_{03}}}{2^{3}} \sin \phi_{3} + \dotsb\right] \\\\
  & \quad - \frac{k^{2}}{2} \left[1 + \frac{k_{0}}{2} + \frac{k_{0}k_{00}}{2^{2}} + \frac{k_{0}k_{00}k_{03}}{2^{3}} + \dotsb\right];
\end{aligned}
\end{gather*}
whence
\begin{gather*}
\Tag{(26)}
Ek\phi = Fk\phi \left[1 - \frac{k^{2}}{2}
  \left(1 + \frac{k_{0}}{2} + \frac{k_{0}k_{00}}{2^{2}} + \dotsb\right)\right] \\\\
  + k \left[\frac{\sqrt{k_{0}}}{2} \sin \phi_{1}
    + \frac{\sqrt{k_{0}k_{00}}}{2^{2}} \sin \phi_{2}
    + \frac{\sqrt{k_{0}k_{00}k_{03}}}{2^{3}} \sin \phi_{3} + \dotsb\right].
\end{gather*}
%% -----File: 095.png---Folio 89-------

From \Eqref{eq.}{V}{(3)}, Chap.~V, we see that when $\phi = \dfrac{\pi}{2}$,
\[
\phi_{n} = 2^{n-1} \pi.
\]

Substituting these values in \Eqref{equation}{}{(26)}, we have for a
complete Elliptic Integral of the second class,
\begin{multline*}
\Tag{(27)}
E \left(k, \frac{\pi}{2}\right) = \\\\
F \left(k, \frac{\pi}{2}\right)
  \left[1 - \frac{k^{2}}{2}
    \left(1 + \frac{k_{0}}{2}
            + \frac{k_{0}k_{00}}{2^{2}}
            + \frac{k_{0}k_{00}k_{03}}{2^{3}} + \dotsb\right)\right].
\end{multline*}

In a similar manner we could have found the formula for
$E (k, \phi)$ in terms of an increasing modulus, viz.,
\begin{align}
\Tag{(28)}
E (k, \phi)
  &= F (k, \phi)
     \biggl[1 + k\biggl(1 + \frac{2}{k_{1}} + \frac{2^{2}}{k_{1}k_{2}}
                          + \frac{2^{3}}{k_{1}k_{2}k_{3}} + \dotsb \\\\
  &{} + \frac{2^{n-2}}{k_{1}k_{2} \dotsm k_{n-2}}
    - \frac{2^{n-1}}{k_{1}k_{2} \dotsm k_{n-1}}\biggr)\biggr] \\\\
  &{} - k \biggl[\sin \phi
        + \frac{2}{\sqrt{k}} \sin \phi_{1}
        + \frac{2^{2}}{\sqrt{kk_{1}}} \sin \phi_{2} + \dotsb \\\\
  &{} + \frac{2^{n-1}}{\sqrt{kk_{1} \dotsm k_{n-2}}} \sin \phi_{n-1}
      - \frac{2^{n}}{\sqrt{kk_{1} \dotsm k_{n-1}}} \sin \phi_{n}\biggr].
\end{align}
%% -----File: 096.png---Folio 90-------


