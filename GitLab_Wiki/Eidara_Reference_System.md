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
- $\chi_{\oplus-trop} = 365.21219$ days
- $M_\odot = 333000 m\oplus$

### The Star Eikon
- Calculated Parameters
  - $L = 1.21\odot$ → Used to calculate $\chi$ for Eidara
  - $K = 5916.551$ K
  - $S = \text{G}0.834$
  - $T = 1.025\odot$
  - $M = 1.051\odot$
  - $R = 1.046\odot$
    - Apparent diameter: $0.508$° $\left(\frac{0.508}{0.533} = 0.9531 \right)$
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
  1. $0.130$ AU — Igniozone — Telluric/Xenotic – Baked and blasted rock (P = $16.6$d)
    m: 0.35; r: 0.55; d: 1.60
    Metal-rich cinder
  2. $0.207$ AU — Igniozone — Telluric – Lava (P = $33.5$d)
    m: 0.60; r: 0.75; d: 1.42
  3. $0.361$ AU — Igniozone — Telluric – ??? (P = $75.9$d)
    m: 0.85; r: 0.95; 1.00
  4. $0.615$ AU — Calorozone  — Argeic (P = $173$d)
  5. $1.017$ (A) AU — Solarazone — EMPTY (P = $365.2564$d)
  6. $1.100$ (N) AU — Solarazone — ***GAEAN*** (P = $410.9$d)
     *This is Eidara's orbit*
  7. $1.817$ AU — Hiberozone — Geotic – Cool Oceanic (P = $879.4$d; $2.401$y)
  8. $3.024$ AU — Brumazone — Argeic (P = $1889.8$d; $5.172$y)
      Main Micromon Belt
       - Inner Edge: 3.657 (est)
       - Outer Edge: 4.848 (est)
  9. $5.953$ AU — Cryozone — Xenotic – Ice Giant (P = $14.13$y)
  10. $11.665$ AU — Cryozone — Xenotic – Gas Giant (P = $38.93$y)
  11. $17.474$ AU — Cryozone — Xenotic – Gas Giant (P = $69.28$y)



  - Moons: 2
    - 
    - 
    - Synodic Period: $22.587$ days; $20.09$ diurns
      - $18.19$ synodia/chronum
    - Synodial Epoch:
      - Aggregate: $7137.48$ days; $6344.427$ diurns
        - $19.54$ years; 17.369 chrona
      - Epochal interval ($\Psi$): $316$ synodia
      - Quarter synodial epoch: $4.89$ years; $4.347$ chrona
      - Quarter epochal interval: $79$ synodoi





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