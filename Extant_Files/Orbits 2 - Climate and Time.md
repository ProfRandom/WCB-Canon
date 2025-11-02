---
title: ""
---

# 📖 Season-Length Estimation Methods
This process assumes that you have already determined the duration of your planet's orbit around its star (its *sidereal chronum*, $C$).

## Obliquity azimuth ($\phi$)
The *obliquity azimuth* of your planet's obliquity is determined by the point in its orbit when the northern hemisphere is tilted directly away from the star. If your planet's northern hemisphere is tilted away from the star when it is at the closest point in its orbit (its *periastron*), then its obliquity azimuth is $\phi = 0$.

| $\phi$ | Orientation                                                                              |
| -----: | ---------------------------------------------------------------------------------------- |
|      0 | Northern hemisphere tilted directly away from star at periastron                         |
|     90 | Northern hemisphere tilted directly away one-fourth orbit *after* periastron             |
|    180 | Northern hemisphere tilted directly away one-half orbit after periastron (at *apastron*) |
|    270 | Northern hemisphere tilted directly away three-fourths orbit after periastron            |

## 1. Sinusoidal Approximation (Fast vs. Slow Half)
Here is a quick, algebra-only method that captures the *main effect of eccentricity* on seasons:

$$
\Delta t \;\approx\; \dfrac{C}{4} + \left(\dfrac{2e}{\pi} C \times \sin \nu\right)
$$
Where:  
- $C$ = year length (chronum, in diurns or days)  
- $e$ = orbital eccentricity  
- $\nu$ = central true anomaly of the season (0° = perihelion, 180° = aphelion)  

### Step 1 — Seasonal Baseline Length
Equal quarter of the chronum:

$$
\dfrac{C}{4}
$$
### Step 2 — Correction Factor
This is a dimensionless ratio determined by eccentricity:

$$
\dfrac{2e}{\pi}
$$
To get the actual correction in diurns, it is multiplied by the full length of the chronum ($C$) in the main equation.

### Step 3 — Seasonal Adjustment
True anomaly of each season midpoint is tied to the obliquity azimuth $\phi$:

$$
\begin{aligned}
&\nu = (\phi + 90n) \bmod 360 \\[1em]
&\begin{cases}
n = 0 &\text{spring equinox} \\
n = 1 &\text{summer solstice} \\
n = 2 &\text{autumn equinox} \\
n = 3 &\text{winter solstice}
\end{cases}
\end{aligned}
$$
#### Worked Example: Earth (Sinusoidal Approximation, Sidereal Chronum)
Given:  
- $\phi = 0$  
- $C = 365.2564$ d (sidereal year)  
- $e = 0.0167$  

**Step 1 — Baseline**

$$
\frac{C}{4} = \frac{365.2564}{4} = 91.31
$$
**Step 2 — Correction Factor**

$$
\frac{2e}{\pi} C = \frac{2 \times 0.0167}{\pi} \times 365.2564 = 3.88
$$
**Step 3 — Seasonal Adjustments (Earth)**
True anomalies from $\phi = 0$:

$$
\nu = (\phi + 90n) \bmod 360
\left\{
\begin{array}{rlll}
n = 0 & \nu = 270^\circ & & \text{spring equinox}\\
n = 1 & \nu = 0^\circ   & & \text{summer solstice}\\
n = 2 & \nu = 90^\circ  & & \text{autumn equinox}\\
n = 3 & \nu = 180^\circ & & \text{winter solstice}
\end{array}
\right.
$$

**Step 4 — Apply the Formula**

$$
\Delta t \;\approx\; \frac{C}{4} + \left(\frac{2e}{\pi} C \times \sin\nu\right)
\begin{cases}
n=0;\;\nu=270^\circ;\;\sin\nu=1 & \Delta t_\text{spring} \approx 91.31 + 3.88 = 95.20 \\
n=1;\;\nu=0^\circ;\;\sin\nu=0 & \Delta t_\text{summer} \approx 91.31 \\
n=2;\;\nu=90^\circ;\;\sin\nu=-1 & \Delta t_\text{autumn} \approx 91.31 - 3.88 = 87.43 \\
n=3;\;\nu=180^\circ;\;\sin\nu=0 & \Delta t_\text{winter} \approx 91.31
\end{cases}
$$
**Result:**  
- Spring ≈ 95.2 d  
- Summer ≈ 91.3 d  
- Autumn ≈ 87.4 d  
- Winter ≈ 91.3 d  
(Total = 365.2564 d)

**Conclusion**
The observed lengths of Earth's seasons are approximately:
- Spring ≈ 92.8 d  
- Summer ≈ 93.6 d  
- Autumn ≈ 89.9 d  
- Winter ≈ 89.0 d 
**Errors:**  
- Spring: +2.4 d  
- Summer: –2.3 d  
- Autumn: –2.5 d  
- Winter: +2.3 d
The method captures the *overall pattern* (a longer spring, a shorter autumn) but forces **two seasons to pair**, which Earth does not actually do because its obliquity azimuth $\phi$ is offset from 0° by about 13°.
**Advice**

When using the sinusoidal method, you have two options:

1. **Accept the values as returned.**  
   - This keeps the math simple and transparent.  
   - The approximation will always add up to the correct year length ($C$).  
   - Errors are usually small if $e ≤ 0.1$ (a few diurns at most for Earth-like orbits).  

2. **Apply the generalized fudge factor.**  
   - To break the “paired seasons” pattern and create four distinct values, redistribute part of the correction term.  
   - Use the rule:   $$
     f = 10e
     $$
- Subtract $f \times \left(\tfrac{2e}{\pi}C\right)$ from the long seasons (those with $\sin\nu = +1$).  
- Add the same amount to the short seasons (those with $\sin\nu = -1$).  
- Baseline seasons (where $\sin\nu = 0$) remain unchanged.  

**Why this works:**  
- The fudge stays tied to orbital eccentricity, so it scales correctly for different worlds.  
- The method remains **SANC** — *Simple, Approximate, Notationally Clear* — while avoiding arbitrary “just make something up” adjustments.

📖 **WCB Note:**  
The sinusoidal shortcut is SANC — Simple, Approximate, Notationally Clear. It always gives you a consistent set of season lengths that add to the right year.
If you’re working with a mildly eccentric orbit ($e \lesssim 0.03$), you may want to apply the fudge factor $f=10e$ to nudge the values closer to reality and give you four distinct seasons.
If you’re working with a strongly eccentric orbit, leave the fudge aside — the uneven seasons it predicts are already the truth of the geometry.
Ultimately, whether you ‘fudge’ is up to you as the worldbuilder: do you want clean numbers, or do you want raw extremes? Both choices are defensible.

#### Worked Example: Rosetta (Sinusoidal Approximation, Sidereal Chronum)
Given:  
- $\phi = 180^\circ$  
- $C = 492$ diurns (sidereal chronum)  
- $e = 0.05$  
**Step 1 — Baseline**

$$
\frac{C}{4} = \frac{492}{4} = 123.0
$$
**Step 2 — Correction Factor**

$$
\frac{2e}{\pi} C = \frac{2 \times 0.05}{\pi} \times 492 = 15.66
$$
**Step 3 — Seasonal Adjustments (Rosetta)**
True anomalies from $\phi = 180^\circ$:

$$
\nu = (\phi + 90n) \bmod 360
\left\{
\begin{array}{rlll}
n = 0 & \nu = 0^\circ   & & \text{spring equinox} \\
n = 1 & \nu = 90^\circ  & & \text{summer solstice} \\
n = 2 & \nu = 180^\circ & & \text{autumn equinox} \\
n = 3 & \nu = 270^\circ & & \text{winter solstice}
\end{array}
\right.
$$

**Step 4 — Apply the Formula**

$$
\Delta t \;\approx\; \frac{C}{4} + \left(\frac{2e}{\pi} C \times \sin\nu\right)
\begin{cases}
n=0;\;\nu=0^\circ;\;\sin\nu=-1 & \Delta t_\text{spring} \approx 123.0 - 15.66 = 107.3 \\
n=1;\;\nu=90^\circ;\;\sin\nu=0 & \Delta t_\text{summer} \approx 123.0 \\
n=2;\;\nu=180^\circ;\;\sin\nu=1 & \Delta t_\text{autumn} \approx 123.0 + 15.66 = 138.7 \\
n=3;\;\nu=270^\circ;\;\sin\nu=0 & \Delta t_\text{winter} \approx 123.0 \\
\end{cases}
$$
**Result:**  
- Spring ≈ 107.3 diurns  
- Summer ≈ 123.0 diurns  
- Autumn ≈ 138.7 diurns  
- Winter ≈ 123.0 diurns
(Total = 492 diurns)

**Conclusion**
The sinusoidal approximation predicts for Rosetta:
- Two baseline seasons (winter, summer ≈ 123 diurns)  
- One shorter season (spring ≈ 107 diurns)  
- One longer season (autumn ≈ 139 diurns)
- The difference between the longest and shortest seasons is **over 31 diurns** — nearly a whole “weke” longer or shorter than the baseline!
- This is much more dramatic than Earth’s ±2–3 day distortions, because Rosetta’s orbital eccentricity ($e=0.05$) is about **3× larger than Earth’s**.
**Advice**
- You can **accept these values directly**, which already tell the story of a planet with noticeably uneven seasons.  
- Or you can **tweak them** slightly (redistributing a fraction of the correction term) to break the symmetry of the paired seasons and produce four distinct values, closer to what the Kepler method would return.  
- Either way, the results remain *SANC* — Simple, Approximate, Notationally Clear — while giving Rosettan cultures a real seasonal asymmetry to reckon with.

## 2. Kepler’s Exact Method (Eccentric Anomaly Conversion)
This more precise method uses full orbital geometry to derive season lengths.
**Key features:**  
- Produces **true season lengths**, including asymmetries between all four.  
- If periastron lines up with a solstice or equinox, still produces pairs (but corrected vs. sinusoidal).  
- If periastron is offset, yields **four distinct season lengths** (like Earth’s 93/94/90/89-day split).  
- Requires a calculator, but no iteration — just `arctan` and `sin`.

### Step 1 — Choose True Anomalies
Pick the true anomalies ($\nu$) for the four seasonal markers, offset by obliquity azimuth $\phi$:

$$
\begin{aligned}
&\nu = (\phi + 90n) \bmod 360 \\[1em]
&\begin{cases}
n = 0; \;\text{spring equinox} \\
n = 1; \;\text{summer solstice} \\
n = 2; \;\text{autumn equinox} \\
n = 3; \;\text{winter solstice} \\
\end{cases}
\end{aligned}
$$
### Step 2 — Convert to Eccentric Anomaly
For each $\nu$, compute the eccentric anomaly $E$:

$$
E = 2 \arctan \!\left( \sqrt{\dfrac{1-e}{1+e}} \;\tan \dfrac{\nu}{2} \right)
$$
### Step 3 — Convert to Mean Anomaly
Translate $E$ into mean anomaly $M$, which grows linearly with time:

$$
M = E - e \sin E
$$
### Step 4 — Find Season Fractions

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
f_\text{winter} &= \frac{M_\text{spring} - M_\text{winter}}{2\pi} \\[6pt]
\end{aligned}
$$

Where:  
- Each $f$ = fraction of the year occupied by that season.  
- The denominator $2\pi$ normalizes the full orbit to 1.  
- The $+2\pi$ in the autumn term closes the loop back to the next winter.

### Step 5 — Scale to Year Length

Multiply each fraction by the chronum ($C$) to convert fractions into diurns:

$$
\begin{aligned}
&\Delta t_\text{spring} = f_\text{spring}\,C, \\
&\Delta t_\text{summer} = f_\text{summer}\,C, \\
&\Delta t_\text{autumn} = f_\text{autumn}\,C, \\
&\Delta t_\text{winter} = f_\text{winter}\,C
\end{aligned}
$$
#### Worked Example: Earth (Kepler’s Method, Sidereal Year)
Given:  
- $\phi = 0^\circ$  
- $C = 365.2564$ days (sidereal year)  
- $e = 0.0167$  

**Step 1 — True Anomalies**
Seasonal markers from $\phi = 0^\circ$:  

$$
\begin{aligned}
\nu &= (\phi + 90n) \bmod 360 \;
\left\{
\begin{array}{rlcll}
n = 0 & \nu = 0^\circ   & & \text{spring equinox} \\
n = 1 & \nu = 90^\circ  & & \text{summer solstice} \\
n = 2 & \nu = 180^\circ & & \text{autumn equinox} \\
n = 3 & \nu = 270^\circ & & \text{winter solstice}
\end{array}
\right.
\end{aligned}
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
\begin{aligned}
&F_\text{spring} \approx 0.2553, \\[.5em]
&F_\text{summer} \approx 0.2553, \\[.5em]
&F_\text{autumn} \approx 0.2447 \\[0.5em]
&F_\text{winter} \approx 0.2447, \\[.5em]
\end{aligned}
$$
**Step 5 — Scale to chronum length**
Multiply each fraction by $C$ to get season lengths in diurns:  

$$
\Delta t = F \times C \quad
\left\{
\begin{array}{lll}
\Delta t_\text{spring} & \approx & 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{summer} & \approx & 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{autumn} & \approx & 0.2447 \times 365.2564 = 89.4 \\
\Delta t_\text{winter} & \approx & 0.2447 \times 365.2564 = 89.4
\end{array}
\right.
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
- $\phi = 180^\circ$  
- $C = 492$ diurns (sidereal chronum)  
- $e = 0.05$  

**Step 1 — True Anomalies**
Seasonal markers from $\phi = 180^\circ$:  

$$
\begin{aligned}
\nu &= (\phi + 90n) \bmod 360 \\[1em]
&\left\{
\begin{array}{rlll}
n = 0 & \nu = 0^\circ   & & \text{spring equinox} \\
n = 1 & \nu = 90^\circ  & & \text{summer solstice} \\
n = 2 & \nu = 180^\circ & & \text{autumn equinox} \\
n = 3 & \nu = 270^\circ & & \text{winter solstice}
\end{array}
\right.
\end{aligned}
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
Multiply each fraction by $C$:  

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

# Workflow for Calculating Azimuthal Intersections
#### **Step 1: Input**
- **Obliquity ($\varepsilon_x$)**: The planet’s axial tilt.
- **Latitude ($\lambda$)**: Observer’s *latitude*, degrees north or south of the equator.
- **Fraction of the apical chronum ($C_f$)**: Time since the summer solstice, as a fraction of the chronum.

#### **Step 2: Calculate Star’s Declination**
Over the course of the apical chronum, a star’s declination shifts north and south of the celestial equator in a sinusoidal pattern. This north–south swing is what causes the east–west drift of the star’s rising and setting azimems along the horizon.

$$
\delta = \epsilon \cos(2 \pi C_f)
$$
#### **Step 3: Calculate Maximum and Minimum Altitudes**
1. **Maximum Altitude ($h_\text{max}$):**

   $$
   h_\text{max} = 90^\circ - |\lambda - \delta|
   $$

2. **Minimum Altitude ($h_\text{min}$):**

   $$
   h_\text{min} = 90^\circ - |\lambda + \delta|
   $$

#### **Step 4: Condition Check**
- **If $h_\text{max} > 0^\circ$ and $h_\text{min} < 0^\circ$:**
    - The star's path intersects the horizon. **Proceed to Step 5**.
- **Otherwise Stop:**
    - If $h_\text{min} > 0^\circ$: The star never dips below the horizon (continuous daylight).
    - If $h_\text{max} ≤ 0^\circ$: The star never rises above the horizon (continuous night).

#### **Step 5: Calculate Center Offset ($altitudem$)**
If the condition in Step 4 is satisfied:

$$
\text{altitudem} = 90^\circ - \frac{|\lambda - \delta| + |\lambda + \delta|}{2}
$$
#### **Step 6: Calculate the Azimuthal Angle and Azimems**
For the star’s path intersections with the horizon ($y = 0^\circ$):

$$
\begin{aligned}
Z = \text{ Azimuthem } \cdot \sqrt{1 - \left(\frac{\text{Altitudem}}{\text{Obliquem}}\right)^2} \\
Z_e = +Z \quad\text{;}\quad Z_w = -Z
\end{aligned}
$$
...where:
- $Azimuthem$ = the great-circle line that connects due east to due west through the observer’s position (passing through the zenith and nadir). Its angular measure is always $180^\circ$.
- $Altitudem$ = the altitude of the ellipse's center relative to the horizon.
- $Obliquem$ = half the angular measure of the planet's obliquity $\left(\dfrac{\varepsilon_x}{2}\right)$
- $Z$ = the azimuthal angle magnitude between due north and the horizon-intersection of either the rising or setting of a star's path
	- $Z_e$ = the east *Azimem*; the angle from due north along the eastern horizon line at which the star's path intersects the eastern horizon.
	- $Z_w$ = the west *Azimem*; the angle from due north along the western horizon line at which the star's path intersects the western horizon.

### **Key Considerations**
- **No Intersections (Skip Step 5 and 6)**:
    - If $h_\text{min} > 0^\circ$: The star’s path lies entirely above the horizon.
    - If $h_\text{max} ≤ 0^\circ$: The star’s path lies entirely below the horizon.

# Obliquity — Planetary Orientation

## Current Obliquity (Axial tilt) ($\varepsilon$) 
Obliquity is the **instantaneous angle** between a planemon’s rotational axis and the perpendicular to its orbital plane.  An up arrow $\uparrow$ or down arrow $\downarrow$ may be appended after the angular measure to indicate whether the obliquity is increasing or decreasing.   

For Earth:  

$$
\varepsilon = 23.5^\circ\downarrow
$$
## Obliquity Envelope ($\mathcal{E}_\varepsilon$) 
$$
\mathcal{E}_\varepsilon =
\begin{bmatrix}
\varepsilon_{min} \\
\varepsilon_{mean} \\
\varepsilon_{max}
\end{bmatrix}
$$
Where:  
- $\varepsilon_x$ = current tilt angle  
- $\varepsilon_{min}$ = minimum obliquity 
- $\varepsilon_{mean}$ = mean obliquity  
- $\varepsilon_{max}$ = maximum obliquity 

Example (Earth):  

$$
\mathcal{E}_\varepsilon = 
\begin{bmatrix}
22.1^\circ \\
23.3^\circ \\
24.5^\circ
\end{bmatrix}
$$
## Obliquity Scope ($\Delta\varepsilon$)
$$
\Delta\varepsilon = \varepsilon_{max} - \varepsilon_{min}
$$
For Earth:

$$
\Delta\varepsilon = 24.5^\circ - 22.1^\circ = 2.5^\circ
$$
## Obliquity Cycle ($T_\varepsilon$) 
The time interval between two maxima (or minima) of obliquity.  

For Earth:  

$$
T_\varepsilon \approx 41{,}000 \text{ years}
$$
## Obliquity  Tempo ($\dot{\varepsilon}$) 
Rate of obliquity change per year:  

$$
\dot{\varepsilon} = \dfrac{\varepsilon_{max} - \varepsilon_{min}}{T_\varepsilon}
$$
For Earth:  

$$
\dot{\varepsilon} = \frac{24.5 - 22.1}{41000} ≈ 0.0000585^\circ/\text{yr} \;=\; 0.00585^\circ/\text{kyr}
$$
## Obliquity Phase ($\phi_\varepsilon$) 
The ratio of the current obliquity to its maximum value, expressed as a percentage, with an arrow showing whether the trend is increasing $\uparrow$ or decreasing $\downarrow$:

$$
\phi_\varepsilon = \dfrac{\varepsilon}{\varepsilon_{max}}\times 100 \; (\uparrow,\downarrow)
$$
For Earth:  

$$
\phi_\varepsilon = \dfrac{23.5}{24.5}\times 100 \approx 95.9\text{\%}\;\downarrow
$$
## Obliquity Azimuth ($\zeta_{n}$) 
The angular orientation of a planemon’s axial tilt relative to its orbit.  Defined as the angle between periapsis (the line of apsides) and the projection of the planet’s north pole on the orbital plane.  
- $\zeta_{0}$ =  (“periaptic zero”): northern solstice occurs at periastron.  
- $\zeta_{90}$ = northern solstice has precessed 90° forward along the orbit.  
- $\zeta_{180}$ =  northern solstice occurs at apastron.  
- $\zeta_{270}$=  northern solstice has precessed 270° forward along the orbit.  
- $\zeta_{n}$ advances anti-clockwise with respect to the orbit, so solstices and equinoxes **precess relative to periastron/apastron**.

- The **obliquity azimuth** precesses around the orbit, shifting the alignment of solstices and equinoxes with periastron and apastron. The **calendar seasons** remain fixed relative to equinoxes/solstices, but their **orbital context** changes over the precessional cycle.
- This precession occurs for all planets with nonzero obliquity ($\varepsilon \neq 0$).  
- The cycle is independent of tilt magnitude: even an $\varepsilon = 90^\circ$ planet precesses in the same way, with solstices tied to periastron/apastron alignment.

**Canonical Cases for $\zeta_n$​**
- $e \neq 0, \varepsilon = 0$
    - The orbit has a defined **periastron**.
    - There is no axial tilt, so no solstices or equinoxes exist.
    - By convention, $\zeta_0$​ may still be defined as the direction of periastron, but it carries **no physical seasonal meaning**.
- $e \neq 0, \varepsilon \neq 0$
    - The orbit has a defined periastron.
    - The planet has tilt, so solstices and equinoxes exist.
    - $\zeta_n$​ is measured from periastron, describing the orbital longitude where the **north pole is tilted directly away from the star**.
        - $\zeta_0$​: that event coincides with periastron.
        - Other $\zeta_n$​: the event occurs $n^\circ$ along the orbit from periastron.
- $e=0, \varepsilon \neq 0$
    - Orbit is a perfect circle: no physical periastron exists.
    - Solstices/equinoxes still exist because of axial tilt.
    - In this case, **a 0° reference direction must be chosen arbitrarily** (often set by convention, e.g. “perihelion by definition”), and $\zeta_n$​ is measured relative to that.
- $e=0, \varepsilon = 0$
    - No tilt, no closest approach.
    - Neither solstices/equinoxes nor apsidal points exist.
    - $\zeta_n$​ is undefined, unless an **arbitrary 0° longitude** is adopted purely for bookkeeping.

## Obliquity Azimuth Precession Cycle ($\Gamma$) 
The length of time it takes the obliquity azimuth ($\zeta_{n}$) to precess through $360^\circ$.
- Defined such that $\zeta_{0}$ occurs when the planet’s north pole is tilted **away** from the star at periastron.  
- At $\zeta_{180}$, the north pole is tilted **toward** the star at periastron.
- For Earth: $\Gamma ≈ 27000$ y.

Thus, for Earth in ~13,000 years, northern summer will occur near December–February if the current Gregorian framework remains in use unchanged.  

> **Note:** $\Gamma$ is undefined for $\varepsilon = 0$, since there is no obliquity to precess. In practice, some frameworks may assign $\Gamma = 0$ for bookkeeping, but this has no physical meaning.

## Earth’s Current Seasons 
| Season | Start        | End          | Length (days) | Why length differs                  |     |
| ------ | ------------ | ------------ | ------------- | ----------------------------------- | --- |
| Spring | Mar Equinox  | Jun Solstice | 92.75         | Earth slows toward apastron         |     |
| Summer | Jun Solstice | Sep Equinox  | 93.65         | Earth slowest near apastron         |     |
| Autumn | Sep Equinox  | Dec Solstice | 89.85         | Earth accelerates toward periastron |     |
| Winter | Dec Solstice | Mar Equinox  | 88.99         | Earth fastest near periastron       |     |

# Retrograde Motion

> **Keppy**: Wait… isn’t retrograde motion an orbital thing?  

Not always: planemons can also **rotate** in a retrograde sense — spinning "backwards" compared to their orbital direction.  And remember what is "up" in a star system is *purely a matter of convention*; ignoring direction of orbital motion, we could just as easily say that Venus is the only prograde planemon in the Solar System.

#### 🧭 How to Know:

- Axial tilt (ε) is the angle between the planemon’s spin axis and the perpendicular to its orbital plane.
- If **ε ∈ ⟨0° ∧ 90°⟩**, the rotation is **prograde** — the planemon spins the same direction as it orbits.
- If **ε ∈ ⟨90° ∧ 180°⟩**, the rotation is **retrograde** — the planemon spins the *opposite* direction from its orbit.

> And here's the twist:  
> What we call “prograde” or “retrograde” is just a matter of **convention**.
> 
> We define “up” in the Solar System based on Earth’s north pole and orbital direction.  
> But that's completely arbitrary.  
> If we flipped the system and redefined "north" as "south," **Venus would become the *only* prograde planemon**, and all the others would be retrograde.

#### 🪐 Example: Venus

- Axial tilt: **177.4°**
- Spins incredibly slowly and **retrograde**
- A full Venus day (sidereal) is ~243 Earth days
- But because of its retrograde spin, a **solar day** (sunrise to sunrise) lasts ~117 Earth days — and the Sun rises in the **west**!

#### 🌀 Why This Matters

- ε > 90° radically changes **day/night direction**, **sun path across the sky**, and even **cultural orientation** ("sun rises in the west").
- High obliquity + retrograde spin = **wildly different** seasonal or diurnal patterns.
- For worldbuilders: this is a prime lever to make a world *feel* subtly alien while remaining physically plausible.

#### 🧭 **How It Works**

- A planemon’s **axial tilt (ε)** is defined as the angle between its rotational axis and the perpendicular to its orbital plane.
- **ε ∈ ⟨0° ∧ 90°⟩** → **prograde rotation**  
    (spin direction aligns with orbital motion)
- **ε ∈ ⟨90° ∧ 180°⟩** → **retrograde rotation**  
    (spin direction opposes orbital motion)

So:

- **Earth**: ε ≈ 23.44° → prograde
- **Venus**: ε ≈ **177.4°** → retrograde
    - It’s tipped almost completely upside down — a rotation that is both *slow* and *backwards*
- **Uranus**: ε ≈ **97.8°** → technically retrograde
    - Lies nearly on its side; its axial pole dips below the orbital plane

#### 📌 **Retrograde Rotation at a Glance**

|**Axial Tilt (ε)**|**Rotation Type**|**Example**|
|---|---|---|
|0°|Perfectly prograde|Theoretical ideal|
|23.4°|Prograde|Earth|
|90°|Sideways / ambiguous|Theoretical (unstable)|
|97.8°|Retrograde|Uranus|
|177.4°|Retrograde|Venus|
|180°|Perfectly retrograde|Theoretical limit|

#### 🪐 **Why It Matters**

- ε > 90° affects **day-night patterns**, **sunrise/sunset direction**, and even **seasonal progression**.
- Can produce a “**solar reversal**” — the Sun appears to rise in the west and set in the east.
- Combined with slow rotation, it may completely upend expectations about **day length**, **thermal cycling**, and **climatic intuition**.

<!-- ### Types of “Day”

An **ephemeris day** (**mean solar day**) is a unit of time used in astronomy and celestial mechanics defined as exactly 24 hours (86400 SI seconds).

Contrast this with an **apparent solar day (tropical day)**, is the time it takes for the Sun to appear in the same position in the sky, from one noontime to the next, and can be either as short as 23ʰ 59ᵐ 38ˢ (23.9938889ʰ) or as long as 24ʰ 30ˢ (24.5ʰ).  Long or short days occur in succession, so the difference builds up until mean time is ahead of apparent time by about 14 minutes near February 6, and behind apparent time by about 16 minutes near November 3.

A **sidereal day** is a unit of time used in astronomy and celestial mechanics. It is defined as the length of time it takes for the Earth to make one complete rotation on its axis with respect to the *fixed stars*, and is defined as:

·         86164.09053083288 SI seconds
·         23ʰ 56ᵐ 4.09053083288ˢ (23.93447192ʰ)
·         0.99726956632908ᵈ

A **stellar day** is Earth's rotation period relative to the International Celestial Reference Frame, defined by the International Earth Rotation and Reference Systems Service (IERS), as:

·         86164.098903691 SI seconds
·         23ʰ 56ᵐ 4.098903691ˢ (23.93446959ʰ)
·         0.99726966323716ᵈ

A sidereal day is 99.9999902827% of a stellar day.  The sidereal day is slightly shorter than the solar day due to the Earth's orbital motion around the Sun.  The synodic period between them is slightly over 28000 calendar years.

The **synodic period** between the ***ephemeris day*** and the ***sidereal day*** calculates to almost exactly the **tropical year**.

… which calculates to only 0.265295200 seconds (1.00000000840688 times) longer than the actual value of 31556925.2507328ˢ.

The **synodic period** between the **_ephemeris day_** and the **_stellar day_** calculates to very nearly the **sidereal year**.

… which calculates to only 101.65737 seconds (1.000003221 times) longer than the actual value of 31558149.7635456ˢ. -->

# Planning A Detailed Atmosphere

## Why Go Deeper Than The Basic Geotic Model?

You don’t *have to* go beyond the basic Geotic model — unless, of course, your players or readers are the kind who pull out calculators and gleefully point out why your planemon’s air shouldn’t work.

If you’re the kind of worldcrafter who likes knowing how things *actually work* (or just wants to stay one step ahead of the smart alecks), this Sidebar Module walks you through the fundamentals of atmospheric plausibility.

We're sticking to **generally habitable atmospheres** here — ones that humans or near-humans could plausibly breathe. But the core principles apply no matter how exotic you want to get.

- **Average atmospheric pressure (atm)**
	- Range: atm ∈ ⟨0.5 ∧ 2.0⟩
	-  Supports oxygen respiration and liquid water without requiring pressure suits or extreme acclimatization
- **Atmospheric Scale Height (H)**
	- H ∈ ⟨6 ∧ 12⟩ km
	- Governs pressure drop with altitude
	- Affects breathing, mountain height, and high-altitude flight
	- See below for details
- **Average atmospheric composition**
	- Oxygen
		- Range: O₂ ∈ ⟨15% ∧ 30%⟩
			-  > 30% even damp fuel ignites more easily, and spontaneous combustion becomes a risk
			-  < 15% requires acclimation or enhanced lung capacity (for any creature not evolved in the environment)
		 - Needed for aerobic respiration
	 - Buffer Gas
		-  Range:  ∈ ⟨70% ∧ 85%⟩
		- The chemically inert or low-reactivity bulk gas that fills out the atmosphere around oxygen
		- Defines overall *atmospheric* density, scale height, sound propagation, and temperature response
		- Nitrogen (N₂) and Argon (Ar) are your only reliable options
			- Other candidates (neon, helium, etc.) are too rare, too light, or too toxic
	- Trace Gases
		-  < 1%
		-  H₂O vapor, O₃, CH₄
		-  CO₂ ideally should comprise < 0.04%
		-  Required for climate regulation (greenhouse effect), UV shielding, biodynamics

## More About Scale Height

As related above, the atmospheric scale height (H)
	- Governs pressure drop with altitude
	- Affects breathing, mountain height, and high-altitude flight

However, the value of H varies with the composition of the atmosphere because the ***molecular mass*** is different for each component gas and is not a constant.

> **Hippy**: You need to calculate H based on how much O₂, buffer gas, etc. your atmosphere has.

Exactly!  So, how do you do that?

### Calculating Scale Height

Scale height (H) depends on:
- **T** = average temperature of the atmosphere (in Kelvin)
- **M** = mean molar mass of the gas mixture (in kg/mol)
- **g** = surface gravity (in m/s²)
- **R** = universal gas constant ≈ 8.314 J/mol·K

... related in the equation:

$$
H = \dfrac{R T}{M g}
$$
#### First

Find the mean molecular (molar) mass M.  Each gas in the atmosphere contributes to the average molar mass based on its ***mole fraction***:

$$
M = \sum{x_i M_i}
$$
> **Keppy**: *DON'T PANIC*!  That Σ might *look* like calculus, but it's not... all it's saying is that we sum up the molar masses of all the gasses present

Yes, in the above equation:
- $x_i$ is the **mole fraction** of each atmospheric gas (in Earth's case, that's 0.78 for N₂; 0.21 for O₂)
- $M_i$ is the molar mass of the gas in question.

Let's use Earth's atmosphere as an example:
- Atmosphere = 78% N₂, 21% O₂, 1% Ar  (using kg/mol):  
- $M_{N_2} = 0.028014$  
- $M_{O_2} = 0.031998$
- $M_{Ar} = 0.039948$
	- We lump argon in with the trace gasses in Earth's case

$$
M = (0.78 \times 0.028014) + (0.21 \times 0.031998) + (0.01 \times 0.039948) = 0.02896 \text{ kg/mol}​
$$

> **Keppy**: Where did 0.028014, and the other numbers come from?

Well spotted!

Each gas has a known molar mass — the mass of one ***mole*** of its molecules — and it's typically expressed in grams per mole (g/mol). Since we’re working in SI units, we convert those to kilograms per mole (kg/mol) by dividing by 1000.  And we look those numbers up in an appropriate (and reliable) source.  Here are a few for reference:

| Gas            | Chemical Formula | Molar Mass (g/mol) | Molar Mass (kg/mol) |
|----------------|------------------|--------------------|---------------------|
| Nitrogen       | N₂               | 28.014             | 0.028014            |
| Oxygen         | O₂               | 31.998             | 0.031998            |
| Argon          | Ar               | 39.948             | 0.039948            |
| Carbon Dioxide | CO₂              | 44.01              | 0.044010            |
| Water vapor    | H₂O (gas)        | 18.015             | 0.018015            |
| Methane        | CH₄              | 16.043             | 0.016043            |
| Helium         | He               | 4.003              | 0.004003            |

> **Hippy**: And you use these values in your atmosphere recipe to get your average molar mass.

Exactly! Once you've built your mix — say, 75% N₂ and 25% O₂ — just multiply each molar mass by its fraction and sum the results.

> **Keppy**: Seems like that equation could get lengthy and complex.

You are *not* wrong about that.  Getting warm and friendly with a spreadsheet or a programmable calculator is very good advice for the serious worldcrafter, for sure.

#### Second

Now that we have our value for M, we plug it into our other *known* values for R (8.314), T (288), and g (9.8) and get:

$$
H=\dfrac{R T}{M g} = \dfrac{8.314 \times 288}{0.02896 \times 9.8} = \dfrac{2395.6}{0.2838} = 8.44\text{ km},
$$

... which is usually rounded up to H = 8.5 km for convenience, but you can use the more exact value if you prefer.

> **Hippy**: T = 288 K is for Earth.  How does one determine it for a 'crafted planemon?

Ah — excellent question.  

The **average surface temperature** T depends on factors like:
- The **luminosity and spectral class** of the central star(s)
- The **orbital distance** of the planemon
- The planemon’s **albedo** (reflectivity)
- And any **greenhouse effects** caused by atmospheric composition    

That starts to pull us into stellar physics and orbital modeling, which is covered in:

> 🔗 **Module XY.Z — Building Your Star and Setting Your Orbit**

There, you'll find methods for estimating a planemon's **equilibrium temperature** and adjusting it for greenhouse gases to get a realistic T for your atmosphere model.

For now, if you're working with a roughly Earthlike setup, using:

$$
T ∈ \langle260 \wedge 320\rangle K,
$$
or roughly ⟨-13° ∧ 47°⟩C  will keep your numbers in a plausible range.

Here's some context for that range:

> - 260K (-13°C; 8.6°F)
> 	- Close to the freezing point of seawater
> 	- Sustained habitability without deep-cold adaptation is still possible
> - 273K (0°C; 32°F)
> 	- Freezing point of water
> 	- Important psychological and ecological threshold
> - 288K (15°C; 59°F)
> 	- Earth's average
> 	- Serves as benchmark for climate comfort and live-rich biomes
> - 310K (37°C; 98.6°F)
> 	- Human core temperature
> 	- Upper limit for comfort under heavy exertion
> - 320K (47°C; 116.6°F)
> 	- At or above this, heat stress becomes deadly without rapid evaporative cooling or climate control.

> ❗️ Important note: IF you *choose* a surface temperature for your world, be sure to note it down, because it will help *determine* your star's parameters later!

> **Keppy**: So, back to atmospheric composition: If you used argon instead of nitrogen as your buffer gas, the air would be heavier and H would shrink?

Exactly. More mass = more gravity per mole = thinner vertical spread = smaller H.

> **Keppy**: And in this case, we're just ignoring the trace gasses altogether?

 Mostly, yes — and here’s why:

Trace gases like CO₂, CH₄, and H₂O vapor are typically present in such **small quantities** (fractions of a percent) that they **barely shift the weighted average** of molar mass.

Let’s say your atmosphere is:
- 78% N₂ (0.028014 kg/mol)
- 21% O₂ (0.031998 kg/mol)
- 1% CO₂ (0.04401 kg/mol)

$$
M = (0.78 \times 0.028014) + (0.21 \times 0.031998) + (0.01 \times 0.04401) = 0.02899 \text{ kg/mol}​
$$

That’s a difference of only **+0.00003** compared to Earth-normal — **Less than a tenth of a percent.**  So, unless you’re at CO₂ levels high enough to make the air toxic or unbreathable, it’s safe to treat the trace gasses as negligible in the **H** calculation.

> **Hippy**: So just include the big players — buffer gas and oxygen — and don’t sweat the tenths of a percent?

Bingo. You can always do a full weighted sum if you really want to be *precise*, but for 99% of cases, O₂ and the buffer gas dominate the molar mass *for Geotic worlds*.

#### Third: Pressure vs. Altitude Approximation

For Earth:

$$
P(h) = P_0 \times 0.37^{\frac{h}{H}}
$$

Where:
- h = altitude in kilometers
- H = 8.5 (or 8.44) km

> **Keppy**: What is P₀, and how do we know its value?

Precisely the question I'd ask at this point!

P₀​ is the **surface pressure** of the planemon — that is, the pressure at **zero altitude**. On Earth, that value is defined as:
- 1 atm
- 101325 Pa*
- 101.325 kPa

\* Named for Blaise Pascal; there's not space here to go into this in detail, but it's a fascinating read if you want to look it up!

For any world you create, P₀​ is one of your **starting parameters**. You either:
- **Choose it** (e.g., 1.2 atm, or 0.65 atm), or
- **Derive it** from known gas composition, temperature, and gravity (which gets more advanced)

So, let's say you've chosen P₀ = 0.9 atm for your planemon, then at one scale height above the planemon's surface, the atmospheric pressure calculates to:

$$
P(H) = 0.9 \times 0.37 = 0.333\text{ atm}
$$
> **Hippy**: Which raises the question of where 0.37 comes from?

Excellent question. That 0.37 isn’t arbitrary — it’s actually derived from a **fundamental mathematical constant**: Euler’s number, e (≈ 2.71828).

The **pressure–altitude relationship** is an ***exponential decay*** equation. In its most general form:

$$
P(h) = P_0 \times e^{\frac{-h}{H}}
$$
... which means that at an altitude of exactly one scale height (where *h* = *H*):

$$
P(H) = P_0 \times e^{-1} = P_0 \times 0.3679 
$$
> **Keppy**: Ah!  I see... and P₀ is just whatever multiple of Earth's surface pressure in atm you've chosen for your world!

> **Hippy**: I always frown at "chosen"; is there any way to at least *approximate* an appropriate P₀ for your planemon based on how you decided to compose its atmosphere?

Well.... yes.... sort of.

You *can* approximate $P_0$​ from first principles — and it's especially useful if you've already defined your atmosphere’s:
- **Gas composition** (molar mix)
- **Surface gravity** (g)
- **Average temperature** (T)

... and rearranging the ***ideal gas law*** for planemon atmospheres:

$$
P_0 = \dfrac{\rho R T}{M}
$$
But this requires knowing ρ, the **near-surface air density** — which in turn depends on pressure and composition, so we go a different route.

Instead, for an atmosphere in hydrostatic equilibrium, you can approximate:

$$
P_0 ≈ \dfrac{g M N}{A}
$$
Where:
- g = surface gravity
- M = average molar mass (kg/mol)
- N = total moles of atmosphere
- A = surface area of the planemon

But this, too, gets messy without knowing how much gas the planemon *started with*, which is based on accretion, outgassing, escape velocity, etc.

So while you *can* try to derive it from theory — and I can help you do that — you’re usually safe choosing a $P_0$ based on:
- Your world’s **gravity** (g)
- Its **escape velocity** (vₑ)
- Its **molar mass and buffer gas makeup** (M – which we learned how to calculate above.)

Here's a "pressure plausibility chart" based on gravity and atmosphere type to give you an other "rule of thumb" to work from:

### 🌍 Pressure Plausibility Chart

*Rule-of-thumb surface pressures based on gravity and buffer gas makeup (M)*

| **Gravity**<br>(g in g⨁) | **Likely Pressure<br>Range (atm)** | **Notes**                                                                               |
| :------------------------: | :----------------------------------: | --------------------------------------------------------------------------------------- |
| 0.5                      |            ⟨0.2 ∧ 0.6⟩             | Light gravity;<br>thinner atmosphere unless<br>retained via cold temps or high mass gas |
| 0.75                     |            ⟨0.4 ∧ 0.9⟩             | On the thin side but potentially<br>breathable; requires attention to O₂ %              |
| 1.0                      |            ⟨0.8 ∧ 1.2⟩             | Earth-normal, depending on<br>mix of gases and water vapor                              |
| 1.25                     |            ⟨1.0 ∧ 1.5⟩             | Denser air; easier to retain<br>light gases like H₂O, CH₄                               |
| 1.5                      |            ⟨1.2 ∧ 2.0⟩             | Heavy air; pressure at sea level<br>could approach adaptation limits                    |

This assumes (!) an Earth-like atmosphere:
- Mean molar mass ≈ ⟨0.028 ∧ 0.032⟩ kg/mol
- Normal temperature (~288 K)
- Terrestrial radius (~1⨁)

You'll need to shift values worlds with high CO₂, significant greenhouse buildup, or non-volatile-rich origins, but the above should be well within bounds for *Geotic worlds*.
