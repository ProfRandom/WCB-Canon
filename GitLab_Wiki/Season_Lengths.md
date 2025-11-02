📖 Season-Length Estimation Methods
This process assumes that you have already determined the duration of your planet's orbit around its star (its *sidereal chronum*, $C$).
## Obliquity azimuth ($\phi$)
The *obliquity azimuth* of your planet's obliquity is determined by the point in its orbit when the northern hemisphere is tilted directly away from the star. If your planet's northern hemisphere is tilted away from the star when it is at the closest point in its orbit (its *periastron*), then its obliquity azimuth is $\phi = 0$.

| $\phi$ | Orientation                                                                              |
| -----: | ---------------------------------------------------------------------------------------- |
|      0 | Northern hemisphere tilted directly away from star at periastron                         |
|     90 | Northern hemisphere tilted directly away one-fourth orbit *after* periastron             |
|    180 | Northern hemisphere tilted directly away one-half orbit after periastron (at *apastron*) |
|    270 | Northern hemisphere tilted directly away three-fourths orbit after periastron            |

---
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
\begin{align}
&\nu = (\phi + 90n) \bmod 360 \\[1em]
&\begin{cases}
n = 0 &\text{spring equinox} \\
n = 1 &\text{summer solstice} \\
n = 2 &\text{autumn equinox} \\
n = 3 &\text{winter solstice}
\end{cases}
\end{align}
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
$$
$$
\begin{cases}
n = 0 & \nu = 270^\circ & \text{spring equinox} \\
n = 1 & \nu = 0^\circ & \text{summer solstice} \\
n = 2 & \nu = 90^\circ   & \text{autumn equinox} \\
n = 3 & \nu = 180^\circ  & \text{winter solstice}
\end{cases}
$$
**Step 4 — Apply the Formula**

$$
\Delta t \;\approx\; \frac{C}{4} + \left(\frac{2e}{\pi} C \times \sin\nu\right)
$$
$$
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
   - Errors are usually small if $e \leq 0.1$ (a few diurns at most for Earth-like orbits).  

2. **Apply the generalized fudge factor.**  
   - To break the “paired seasons” pattern and create four distinct values, redistribute part of the correction term.  
   - Use the rule:

$$
     f = 10e
$$

- Subtract $f \times \left(\tfrac{2e}{\pi}C\right)$ from the long seasons (those with $\sin\nu = +1$).  
- Add the same amount to the short seasons (those with $\sin\nu = -1$).  
- Baseline seasons (where $\sin\nu = 0$) remain unchanged.  

**Why this works:**  
- The fudge stays tied to orbital eccentricity, so it scales correctly for different worlds.  
- The method remains **SANC** — *Simple, Approximate, Notationally Clear* — while avoiding arbitrary “just make something up” adjustments.

---

📖 **WCB Note:**  
The sinusoidal shortcut is SANC — Simple, Approximate, Notationally Clear. It always gives you a consistent set of season lengths that add to the right year.

If you’re working with a mildly eccentric orbit ($e \lesssim 0.03$), you may want to apply the fudge factor $f=10e$ to nudge the values closer to reality and give you four distinct seasons.

If you’re working with a strongly eccentric orbit, leave the fudge aside — the uneven seasons it predicts are already the truth of the geometry.

Ultimately, whether you ‘fudge’ is up to you as the worldbuilder: do you want clean numbers, or do you want raw extremes? Both choices are defensible.

---
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
$$
$$
\begin{cases}
n = 0 & \nu = 0^\circ & \text{spring equinox} \\
n = 1 & \nu = 90^\circ & \text{summer solstice} \\
n = 2 & \nu = 180^\circ   & \text{autumn equinox} \\
n = 3 & \nu = 270^\circ  & \text{winter solstice}
\end{cases}
$$
**Step 4 — Apply the Formula**

$$
\Delta t \;\approx\; \frac{C}{4} + \left(\frac{2e}{\pi} C \times \sin\nu\right)
$$

$$
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
\begin{align}
&\nu = (\phi + 90n) \bmod 360 \\[1em]
&\begin{cases}
n = 0; \;\text{spring equinox} \\
n = 1; \;\text{summer solstice} \\
n = 2; \;\text{autumn equinox} \\
n = 3; \;\text{winter solstice} \\
\end{cases}
\end{align}
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
\begin{align}
&M_\text{spring} \\
&M_\text{summer} \\
&M_\text{autumn} \\
&M_\text{winter} 
\end{align}
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

---

### Step 5 — Scale to Year Length

Multiply each fraction by the chronum ($C$) to convert fractions into diurns:

$$
\begin{gather}
\Delta t_\text{spring} = f_\text{spring}\,C, \\
\Delta t_\text{summer} = f_\text{summer}\,C, \\
\Delta t_\text{autumn} = f_\text{autumn}\,C, \\
\Delta t_\text{winter} = f_\text{winter}\,C
\end{gather}
$$

#### Worked Example: Earth (Kepler’s Method, Sidereal Year)
Given:  
- $\phi = 0^\circ$  
- $C = 365.2564$ days (sidereal year)  
- $e = 0.0167$  

**Step 1 — True Anomalies**
Seasonal markers from $\phi = 0^\circ$:  

$$
\nu = (\phi + 90n) \bmod 360
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
\begin{align}
&F_\text{spring} \approx 0.2553, \\[.5em]
&F_\text{summer} \approx 0.2553, \\[.5em]
&F_\text{autumn} \approx 0.2447 \\[0.5em]
&F_\text{winter} \approx 0.2447, \\[.5em]
\end{align}
$$
**Step 5 — Scale to chronum length**
Multiply each fraction by $C$ to get season lengths in diurns:  

$$
\begin{gather}
\Delta t = F \times C \\[1em]
\begin{cases}
\Delta t_\text{spring} &\approx 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{summer} &\approx 0.2553 \times 365.2564 = 93.3 \\
\Delta t_\text{autumn} &≈ 0.2447 \times 365.2564 = 89.4 \\
\Delta t_\text{winter} &≈ 0.2447 \times 365.2564 = 89.4
\end{cases}
\end{gather}
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
\begin{gather}
&\nu = (\phi + 90n) \bmod 360 \\[1em]
&\begin{cases}
n &= 0 & \nu = 0^\circ & \text{spring equinox} \\
n &= 1 & \nu = 90^\circ & \text{summer solstice} \\
n &= 2 & \nu = 180^\circ & \text{autumn equinox} \\
n &= 3 & \nu = 270^\circ & \text{winter solstice}
\end{cases}
\end{gather}
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
\begin{align}
&F_\text{spring} \approx 0.2180, \\
&F_\text{summer} \approx 0.2537, \\
&F_\text{autumn} \approx 0.2820, \\
&F_\text{winter} \approx 0.2463
\end{align}
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