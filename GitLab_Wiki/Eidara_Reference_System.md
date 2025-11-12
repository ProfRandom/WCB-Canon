---
title: "Meta 6 — The Eidara Reference System"
summary: Defines the canonical WCB example system used for demonstrations of Ontic, Metric, and Descriptive principles.
domain: meta
category: reference
tags: [eidara, reference, system, habitable, example]
vocabulary: [Eidara, Eidaran, Fusamon, Duramon, Monon, Animote]
updated: 2025-11-01
status: canonical
version: 1.0
related: [Ontics, Metrics, Morphotics, Conformics, Animotics, Milieutics]
contributors: [M. Conrad, GPT-5]
source: ""
---

# The Eikon-Eidara Reference System

## Building From The Planemon

### Constants
- $\chi_\oplus = 365.256363004$ days
- $M_\odot = 333000 m\oplus$

## Process

We begin with two known parameters for the planemon:

$$
\begin{aligned}
	m &= 1.05\oplus \\[0.5ex]
  \therefore m_\odot &= \frac{m}{333000} = 3.153 \times 10^{-6}\odot \\[0.5ex]
  r &= 1.02\oplus \\[0.5ex]
   &\text{And one known parameter for its orbital axis:} \\[0.5ex]
  D &= 1.1\; \text{AU}
\end{aligned}
$$
 —  and one known parameter for its orbital axis:

$$
\begin{aligned}
  D &= 1.1\; \text{AU}
\end{aligned}
$$
 
- **This is also specified to be the system *nucleal orbit axis*** ($N$).

The other three parameters are calculated from these two:

$$
\begin{aligned}
	\rho &= \frac{m}{r^3} = 0.989 \\
	g &= \frac{m}{r^2} = 1.009 \\
	v_e &= \sqrt{\frac{m}{r}} = 1.015
\end{aligned}
$$
We cannot calculate the orbital period (Chronum; $\chi$) for Eidara by without knowing the mass of the star, because:

$$
	P = \sqrt{\frac{D^3}{\mathbf{M} + m\odot}}
$$
 — and we cannot calculate the mass of the star by rearranging this equation, because that requires that we know $P$ which is the very quantity we're seeking.

 However, there is one stellar parameter that we *can* calculate directly from what information we already have:

$$
 	L = N^2
$$
 —  and since we've already specified that the planemon's orbital axis *is* the nucleal orbit axis:

$$
 	L = N^2 = 1.1^2 = 1.21\; \odot
$$
 — and once we know the star's luminosity, we can calculate its mass:

$$
\begin{aligned}
	M &= \sqrt[3.7889]{1.21} = 1.051 \\
\end{aligned}
$$
Using this mass, we can now calculate an orbital period ($P$) for the planemon:

$$
\begin{aligned}
	\chi &= \sqrt{\frac{D^3}{M + m\odot}} \\
    &= \sqrt{\frac{1.1^3}{1.051 + 3.153 \times 10^{-6}}} \\
    &= \sqrt{\frac{1.331}{1.051003153}} \\
    &= \sqrt{1.2664} \\
  \chi &= 1.125  
\end{aligned}
$$
 — which is:

$$
	\chi_d = \chi \times \chi_\oplus = 1.125 \times 365.256363004 = 411.041\; \text{days}
$$
We can calculate the rest of the star's parameters from the luminosity: 

$$
\begin{aligned}
  T &= \sqrt[7.5778]{L} = \sqrt[7.5778]{1.21} = 1.025 \\
  R &= \sqrt[4.\overline{2}]{L} = \sqrt[4.\overline{2}]{1.21} = 1.046 \\
  Q &= L^{-1.52} = 1.21^{-1.52} = 0.749 \times 10^{10} = 7.49\; \text{Ga}
\end{aligned}
$$
We can *approximate* the perannual orbit for Eikon by:

$$
	A_\approx = \sqrt[3]{M} = \sqrt[3]{1.051} = 1.017\; \text{AU}
$$
 — it is technically more accurate to calculate it from the orbital period ($\chi$) and the summed masses ($M + m\odot$).  In this case we're looking for the orbital axis of an orbit with $\chi = 1$, so we can leave that parameter out:

$$
 \begin{aligned}
 	A &= \sqrt[3]{M + m\odot} \\
  	&= \sqrt[3]{1.051 + 3.153 \times 10^{-6}} \\
  A &= \sqrt[3]{1.051003153} = 1.017\; \text{AU}
\end{aligned} 
$$
 The two results come out the same because the mass of the planemon contributes so little to the equation that it can safely be ignored.

Taking the two equations out to absurd numbers of decimal places:

$$
\begin{array}{clc}
  A &= \sqrt[3]{1.051003153} &= 1.01671994\; \text{AU} \\
  A &= \sqrt[3]{1.051} &= 1.01671892\; \text{AU}
\end{array}
$$

 — a difference of $0.00000102$ AU, or about $152.11$ km
 
## Results
From this process we arrive at the following known parameters:

### Eidara
- Specified Parameters
  - $m = 1.05\oplus$; $m_\odot = 3.153 \times 10^{-6}$
  - $r = 1.02\oplus$
- Calculated Parameters
  - $\rho = 0.989\oplus$
  - $g = 1.009\oplus$
  - $v_e = 1.015\oplus$
- Specified Orbit (= to nucleal orbit)
  - $D = N = 1.1$ AU
- Calculated Orbital Period (Chrona; $\chi$, $\chi_{trop}$)
    - $\chi = 1.125$ years
    - $\chi_d = 410.9134$ days
    - $\chi_{trop}$ = 410.8987 days (22ᵐ 57.55ˢ shorter)
- Obliquity: $\varepsilon = 27^\circ$
- Tempostat: Primary Equinox
- Chronex of the Tempostat: $\zeta = 35^\circ$
- Orbital Eccentricity:
  - $e = 0.050$
- Precession Span:
  - $Ϣ = 28994$ years
- Sectals:
  - Kepler:
    - $S_0 = 101.8317$ d (Primary Equinox)
    - $S_1 = 107.4456$ d (Secondary Solstice)
    - $S_2 = 103.4658$ d (Primary Equinox)
    - $S_3 = 98.1706$ d (Primary Solstice)
  - Sinusoidal:
    - $S_0 = 110.2306$ d (Primary Equinox)
    - $S_1 = 113.4427$ d (Secondary Solstice)
    - $S_2 = 95.2261$ d (Primary Equinox)
    - $S_3 = 92.0140$ d (Primary Solstice)
  - Moons: 2
    - Eis:
      - Sidereal period: $11.72$ d
    - Eisen:
      - Sidereal period: $24.36$ d

### Eikon
- Calculated Parameters
  - $L = 1.21\odot$ → Used to calculate $\chi$ for Eidara
  - $K = 5916.551$ K
  - $S = \text{G}0.834$
  - $T = 1.025\odot$
  - $M = 1.051\odot$
  - $R = 1.046\odot$
  - $Q = 0.749\odot; 7.49$ Ga
  - $A = 1.017$ AU
- Basal Orbital Configuration:
  - Nucleal: $1.1$ AU
  - Perannual: $1.017$ AU
- Thermozones:
  - $H_0 = 0.524$ AU
  - $H_1 = 0.787$ AU
  - $H_2 = 0.996$ AU
    - ($A = 1.017$ AU)
    - ($N = 1.1$ AU)
  - $H_3 = 1.453$ AU
  - $H_4 = 1.856$ AU
  - $H_5 = 5.087$ AU
- System Orbits:
  1. $0.130$ AU — Igniozone
  2. $0.207$ AU — Igniozone
  3. $0.361$ AU — Igniozone
  4. $0.615$ AU — Calorozone
  5. $1.017$ (A) AU — Solarazone
  6. $1.100$ (N) AU — Solarazone
  7. $1.817$ AU — Hiberozone
  8. $3.024$ AU — Brumazone
      Main Micromon Belt
       - Inner Edge: 3.657 (est)
       - Outer Edge: 4.848 (est)
  9. $5.953$ AU — Cryozone
  10. $11.665$ AU — Cryozone
  11. $17.474$ AU — Cryozone
