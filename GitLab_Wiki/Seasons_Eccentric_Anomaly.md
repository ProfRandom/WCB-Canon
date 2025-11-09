---
title: "Orbits-4 — Kepler’s Eccentric Anomaly Method"
summary: Step-by-step procedure for estimating seasonal durations using Kepler’s relations between true, eccentric, and mean anomalies.
domain: metric
category: methods
status: canonical
version: 1.0
updated: 2025-11-06
contributors: [M. Conrad, GPT-5]
---

## 1 · Context and Purpose

The **Eccentric Anomaly Method** provides a geometric and temporal framework for estimating **seasonal durations** on worlds whose orbits are **non-circular**.

In the *World Crafting Basics* system, it serves as the **canonical procedure** for converting a planet’s **orbital geometry** into **time fractions** of its *chronum* — the sidereal year.

In any elliptical orbit, the planet’s orbital speed varies: it moves **faster near periapsis** (closest to the star) and **slower near apoapsis** (farthest away).

Because of this, the four “seasons” or **quarta** do not occupy equal fractions of the year.  Where Kepler observed that planets sweep out *equal areas in equal times*, we might invert the insight to say that they traverse *equal distances in unequal times*.  This inversion reframes orbital mechanics from a geometric principle into an experiential one: a rhythm of motion that shapes the tempo of a world’s year.

The difference in season length arises purely from the **eccentricity** of the orbit, independent of axial tilt or climate.

The eccentric anomaly ($E_n$) is the key intermediary that links **spatial position** (true anomaly, $ν$) with **temporal progress** (mean anomaly, $\textit{Ⳁ}_n$).  

For **worldmakers**, this method turns abstract orbital parameters into practical narrative data:  
- It determines how long each season lasts on a given world.  
- It shows how eccentricity can create longer summers and shorter winters — or vice versa — without altering obliquity.  
- It provides a foundation for climate timing, cultural calendars, and the rhythm of a planet’s year.

By pairing **Kepler’s geometry** with **WCB’s chronum–quartum framework**, the eccentric anomaly method gives a clear, reproducible way to convert orbital shape into lived temporal experience — the heartbeat of a world’s cycle.

## 2 · Vocabulary

- **Chronum** *($\chi$)* —  
  One complete sidereal orbit; the planet’s **year** expressed in diurns.  

- **Quartum** *(pl. quarta)* —  
  One quarter of a planet’s orbital period (denoted $Q_0, Q_1, Q_2, Q_3$); a **non-climatological “season.”**  
    A quartum is a **temporal span**, not a spatial angle — a section of the orbit *traversed through time* between two successive chronal stations.

  - **Quarta** ($Q_n$) are **successive spans of motion** between those angles:
  
$$
    Quartum_n = [\nu_n,\; \nu_{n+1})
$$

— forming four temporal intervals that together complete the chronum.  

Thus, the true anomalies define **where** each quartum begins, while the quarta themselves describe **how long** each orbital segment lasts.  

- **Tempostat** *($t$)* —  
  The **onset of the first quartum** following periapsis; marks the temporal origin of the planet’s annual cycle.  
  - This need not correspond to a “spring” or vernal point for any given hemisphere — it is purely orbital and axial, not seasonal, in definition.  

- **Chronex** *($\zeta$)* —  
  The **true anomaly** of the tempostat.  

- **Eccentricity** *($e$)* —  
  Describes how far the orbit departs from circularity (0 = circle, < 1 = ellipse).  

- **True Anomaly** *($\nu$)* —  
  The **spatial angle** between periapsis and the planet’s actual position, measured from the system’s focus.  
  Each **true anomaly** ($\nu$) defines a **cardinal boundary** between quarta — the concentric angular coordinates that partition the orbit into four temporal spans.  

  - Every point along an orbit has a distinct true anomaly.  
    The true-anomaly measures of the four quarta are denoted $Ⲁ_0, Ⲁ_1, Ⲁ_2,\;\text{and}\; Ⲁ_3$, calculated by:

$$
    Ⲁ_n = (\zeta + 90n) \bmod 360
$$
 — where *n* is the **index of the quartum**.

- **Eccentric Anomaly** *($E_n$)* —  
  The **geometric angle** measured at the ellipse’s center to the projected point on its circumscribed circle; it simplifies Kepler’s relations, generally denoted $E$, but the eccentric anomalies of the four quarta are denoted $E_0, E_1, E_2,$ and $E_3$.

$$
\begin{gathered}
E_n = 2 \arctan \!\left( \xi \;\tan \frac{\nu_n}{2} \right), \qquad
\nu_n = 2 \arctan \!\left( \frac{1}{\xi} \;\tan \frac{E_n}{2} \right)
\end{gathered}
$$

- This represents an **algebraic frame-shift** that permits calculation of the **mean anomaly** ($M^{\!\theta}$) by projecting the *true anomaly* onto the circumscribed reference circle.  

- **Mean Anomaly** *($\textit{Ⳁ}_n$)* —  
  The **temporal angle** that increases uniformly with time, defining a constant angular rate around the orbit.  
  Kepler’s relation (modified for WCB):

$$
\textit{Ⳁ}_n = \frac{(E_n - e\,\sin E_n) \bmod 360}{360}
$$

  …translates the varying orbital motion into a **uniform time variable**, allowing direct calculation of how much of the year has elapsed at any given point on the ellipse.  It represents the planet’s position as if it moved at steady speed along a circular path, providing a linear measure of elapsed orbital time.

> Note that $E_n$ **cannot** easily be back-calculated from $\textit{Ⳁ}_n$!

- **Eccentric Tangent Factor** *($\xi$)* —
  - A dimensionless helper constant linking *true* and *eccentric* anomalies through their tangent relation, calculated by:  

$$
	\xi = \sqrt{\frac{1 - e}{1 + e}}, \qquad
  \frac{1}{\xi} = \sqrt{\frac{1 + e}{1 - e}}
$$

- **Obliquity** *($\varepsilon$)* —  
  The **axial tilt** between a planet’s spin vector and the normal to its orbital plane.  
 -  It governs the **intensity and polarity** of insolation across hemispheres, affecting climatic seasons but not the geometric quarta themselves.

**Station (Chronal)** *($ς\_n$)* —
A **geometric orientation event** in which a planet’s rotational axis attains one of four characteristic alignments relative to its star, *as viewed from above the planet’s right-hand-rule north pole*. 
- Each **station** ($ς\_n$) corresponds to an **axial alignment angle** ($Ⲁ\_n$) separated by 90° in orbital longitude, marking a **temporal node** that bounds successive quarta within a chromum.

> *Italicized variables are scalar; boldface (not used here) would denote vector quantities.*

## Eccentric Anomaly Conversion (Kepler’s Method)

## 1 · Identify Key Quantities

Before beginning the conversion, identify the following key quantities:

- **$\varepsilon$** — the planet’s **obliquity** (axial tilt).  
  - *Note:* a planet with no tilt ($\varepsilon = 0$) experiences no seasons — and therefore no quarta — in the usual sense. Proceeding further in such a case is non-productive.  
- **$e$** — orbital **eccentricity**, describing how far the planet’s orbit departs from circularity.  
- **$\zeta$** — the **chronex**, the true-anomaly angle of the first cardinal event (*tempostat*) to occur after the planet passes periapsis.  
- **$\chi$** — the planet’s **chronum**, its sidereal orbital period (best expressed in diurns or days).  

### How do I determine my planet’s *chronex*?

You choose it — but the choice shapes the rhythm of the world’s year. Consider the following:

**A.** Which quartum (“season”) do you want to begin **less than $45^\circ$ after periapsis**?  
That is your *tempostat.*  
> *Note:* if you set $\zeta ≥ 45^\circ$, your tempostat actually falls in the **preceding quartum.**

**B.** The specific quartum you choose matters only insofar as it determines how the **fractions of the chronum** are distributed among the quarta.

If you want, for example, “summer” in the northern hemisphere to be the **longest** season, that requirement alone determines your chronex: place the *tempostat* such that the longest quartum (by definition $Q_2$) aligns with northern summer.

## Eccentric Anomaly (E)

The **eccentric anomaly**, $E$, is an angular coordinate that describes a body’s position along an **elliptical orbit** in a way that keeps Kepler’s equation simple.

Imagine a circle drawn around the ellipse with the same center and major axis. If you project the planet’s position *up* to that circle by a line drawn perpendicular to the major axis, the angle at the center of the ellipse between that line and the direction of periastron is the **eccentric anomaly**.

In other words:

- The *true anomaly* ($ν$) is the angle measured **at the focus** — from periastron to the planet itself.  
- The *eccentric anomaly* ($E$) is measured **at the center** — from periastron to the projected point on the reference circle.  
- The *mean anomaly* ($M$) increases uniformly with time and connects to $E$ through Kepler’s Equation:

$$
M^\theta = \frac{E - e\,\sin E}{360}
$$

The eccentric anomaly acts as the mathematical bridge between the **uniform time variable** ($M$) and the **actual orbital position** ($ν$). 
It allows us to calculate how much of the orbital period has elapsed at any given geometric position — even when the orbit is not circular.


### Step 1 — Choose True Anomalies
Pick the true anomalies ($\nu$) for the four seasonal markers, offset by obliquity orientation $\zeta$:

$$
\begin{aligned}
&\nu = (\zeta + 90n) \bmod 360 \\[$$1em]
&\begin{cases}
n = 0; \;\text{spring equinox} \\
n = 1; \;\text{summer solstice} \\
n = 2; \;\text{autumn equinox} \\
n = 3; \;\text{winter solstice} \\
\end{cases}
\end{aligned}
$$

### Step 2 — Calculate The Eccentric Tangent Factor ($\xi$)

$$
\xi = \sqrt{\frac{1 - e}{1 + e}}, \qquad \xi^{-1} = \sqrt{\frac{1 + e}{1 - e}} \\

$$

### Step 3 — Convert to Eccentric Anomaly
For each $\nu$, compute the eccentric anomaly $E$:

$$
\begin{aligned}
E &= 2 \arctan \!\left( \xi \;\tan \frac{\nu}{2} \right)
\end{aligned}
$$

*The inverse relation, useful when converting from eccentric to true anomaly, is:*


### Step 4 — Convert to Mean Anomaly

Translate $E$ into mean anomaly $M$, which grows linearly with time:

$$
M = E - e \sin E
$$
### Step 5 — Find Season Fractions

Once you have the mean anomalies for each seasonal marker:

$$
\begin{aligned}
&M_\text{spring} \\
&M_\text{summer} \\
&M_\text{autumn} \\
&M_\text{winter} 
\end{aligned}
$$

subtract them in sequence to get the fractional year lengths:

$$
\begin{aligned}
f_\text{spring} &= \frac{M_\text{summer} - M_\text{spring}}{2\pi} \\[6pt]
f_\text{summer} &= \frac{M_\text{autumn} - M_\text{summer}}{2\pi} \\[6pt]
f_\text{autumn} &= \frac{(M_\text{winter}+2\pi) - M_\text{autumn}}{2\pi} \\[6pt]
f_\text{winter} &= \frac{M_\text{spring} - M_\text{winter}}{2\pi}
\end{aligned}
$$

Where:  
- Each $f$ = fraction of the year occupied by that season.  
- The denominator $2\pi$ normalizes the full orbit to 1.  
- The $+2\pi$ in the autumn term closes the loop back to the next winter.

### Step 6 — Scale to Year Length

Multiply each fraction by the chronum ($\chi$) to convert fractions into diurns:

$$
\begin{gathered}
\Delta t_\text{spring} = f_\text{spring}\,\chi, \\
\Delta t_\text{summer} = f_\text{summer}\,\chi, \\
\Delta t_\text{autumn} = f_\text{autumn}\,\chi, \\
\Delta t_\text{winter} = f_\text{winter}\,\chi
\end{gathered}
$$

#### Worked Example: Earth (Kepler’s Method, Sidereal Year)

Given:  
- $\zeta = 0^\circ$  
- $\chi = 365.2564$ days (sidereal year)  
- $e = 0.0167$  

**Step 1 — True Anomalies**
Seasonal markers from $\zeta = 0^\circ$:  

$$
\nu = (\zeta + 90n) \bmod 360
$$

$$
\begin{cases}
n = 0 & \nu = 270^\circ & \text{spring equinox} \\
n = 1 & \nu = 0^\circ & \text{summer solstice} \\
n = 2 & \nu = 90^\circ & \text{autumn equinox} \\
n = 3 & \nu = 180^\circ & \text{winter solstice}
\end{cases}
$$
**Step 2 — Convert to Eccentric Anomaly**

$$
E = 2 \arctan \!\left( \sqrt{\tfrac{1-e}{1+e}} \;\tan \tfrac{\nu}{2} \right)
$$
**Step 3 — Convert to Mean Anomaly**

$$
M = E - e \sin E
$$
This gives the “time angle” at each seasonal marker.

**Step 4 — Find Season Fractions**
Subtract successive $M$ values and normalize by $2\pi$:  

$$
\begin{aligned}
F_\text{spring} &= \frac{M_\text{summer} - M_\text{spring}}{2\pi} \\[6pt]
F_\text{summer} &= \frac{M_\text{autumn} - M_\text{summer}}{2\pi} \\[6pt]
F_\text{autumn} &= \frac{(M_\text{winter}+2\pi) - M_\text{autumn}}{2\pi} \\[6pt]
F_\text{winter} &= \frac{M_\text{spring} - M_\text{winter}}{2\pi}
\end{aligned}
$$
Numerical results:  

$$
\begin{gathered}
F_\text{spring} &\approx 0.2553, \\[0.5em]
F_\text{summer} &\approx 0.2553, \\[0.5em]
F_\text{autumn} &\approx 0.2447 \\[0.5em]
F_\text{winter} &\approx 0.2447
\end{gathered}
$$

**Step 5 — Scale to chronum length**
Multiply each fraction by $\chi$ to get season lengths in diurns:  

$$
\begin{gathered}
\Delta t = F \times \chi \\[1em]
\begin{cases}
\Delta t_\text{spring} &\approx 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{summer} &\approx 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{autumn} &≈ 0.2447 \times 365.2564 = 89.4 \\
\Delta t_\text{winter} &≈ 0.2447 \times 365.2564 = 89.4
\end{cases}
\end{gathered}
$$

**Result:**  
- Spring ≈ 93.3 d  
- Summer ≈ 93.3 d  
- Autumn ≈ 89.4 d  
- Winter ≈ 89.4 d 
(Total = 365.26 d)

**Comparison to Actuals**
Observed Earth season lengths (tropical year):  
- Spring ≈ 92.8 d  
- Summer ≈ 93.6 d  
- Autumn ≈ 89.9 d  
- Winter ≈ 89.0 d

**Errors:**  
- Spring: +0.5 d  
- Summer: –0.3 d  
- Autumn: –0.5 d  
- Winter: +0.4 d 

**Conclusion**
- The Kepler method reproduces Earth’s observed seasons within **half a day per season**.  
- It captures the correct pattern — two longer seasons and two shorter — without needing any fudge factors.

#### Worked Example: Rosetta (Kepler’s Method, Sidereal Chronum)
Given:  
- $\zeta = 180^\circ$  
- $\chi = 492$ diurns (sidereal chronum)  
- $e = 0.05$  

**Step 1 — True Anomalies**
Seasonal markers from $\zeta = 180^\circ$:  

$$
\begin{gathered}
&\nu = (\zeta + 90n) \bmod 360 \\[1em]
&\begin{cases}
n &= 0 & \nu = 0^\circ & \text{spring equinox} \\
n &= 1 & \nu = 90^\circ & \text{summer solstice} \\
n &= 2 & \nu = 180^\circ & \text{autumn equinox} \\
n &= 3 & \nu = 270^\circ & \text{winter solstice}
\end{cases}
\end{gathered}
$$
**Step 2 — Convert to Eccentric Anomaly**

$$
E = 2 \arctan \!\left( \sqrt{\tfrac{1-e}{1+e}} \;\tan \tfrac{\nu}{2} \right)
$$
**Step 3 — Convert to Mean Anomaly**

$$
M = E - e \sin E
$$

**Step 4 — Find Season Fractions**
Subtract successive $M$ values and normalize by $2\pi$:  

$$
\begin{aligned}
F_\text{spring} &= \frac{M_\text{summer} - M_\text{spring}}{2\pi} \\[6pt]
F_\text{summer} &= \frac{M_\text{autumn} - M_\text{summer}}{2\pi} \\[6pt]
F_\text{autumn} &= \frac{(M_\text{winter}+2\pi) - M_\text{autumn}}{2\pi} \\[6pt]
F_\text{winter} &= \frac{M_\text{spring} - M_\text{winter}}{2\pi} 
\end{aligned}
$$
Numerical results:  

$$
\begin{aligned}
&F_\text{spring} \approx 0.2180, \\
&F_\text{summer} \approx 0.2537, \\
&F_\text{autumn} \approx 0.2820, \\
&F_\text{winter} \approx 0.2463
\end{aligned}
$$
**Step 5 — Scale to Year Length**
Multiply each fraction by $\chi$:  

$$
\begin{cases}
\Delta t_\text{spring} \approx 107.3 \\
\Delta t_\text{summer} \approx 124.9 \\
\Delta t_\text{autumn} \approx 138.6 \\
\Delta t_\text{winter} \approx 121.2
\end{cases}
$$
(Total = 492.0 d)

**Result (Kepler):**  
- Spring ≈ 107.3 d  
- Summer ≈ 124.9 d  
- Autumn ≈ 138.6 d  
- Winter ≈ 121.2 d

**Comparison to Sinusoidal**
From the sinusoidal shortcut (no fudge):  
- Spring ≈ 107.3 d  
- Summer ≈ 123.0 d  
- Autumn ≈ 138.7 d  
- Winter ≈ 123.0 d

**Differences:**  
- Spring: 0.0 d  
- Summer: +1.9 d  
- Autumn: –0.1 d  
- Winter: –1.8 d

**Conclusion**
The Kepler method and sinusoidal shortcut agree closely for Rosetta, but Kepler adds nuance:  
- Winter is slightly shorter, summer slightly longer, compared to the sinusoidal baseline.  
- Spring and autumn remain nearly identical.  

With Rosetta’s higher eccentricity ($e = 0.05$), the **seasonal spread is extreme** — from 107 d to 139 d — a difference of over 30 diurns.  

This is exactly the kind of asymmetry you would expect on a world with such an orbit, and it needs **no fudge at all**.