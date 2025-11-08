📖 Season-Length Estimation Methods
This process assumes that you have already determined the duration of your planet's orbit around its star (its *sidereal chronum*, $\chi$).
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
\Delta t \;\approx\; \dfrac{\chi}{4} + \left(\dfrac{2e}{\pi} \chi \times \sin \nu\right)
$$
Where:  
- $\chi$ = year length (chronum, in diurns or days)  
- $e$ = orbital eccentricity  
- $\nu$ = central true anomaly of the season (0° = perihelion, 180° = aphelion)  

### Step 1 — Seasonal Baseline Length
Equal quarter of the chronum:

$$
\dfrac{\chi}{4}
$$
### Step 2 — Correction Factor
This is a dimensionless ratio determined by eccentricity:

$$
\dfrac{2e}{\pi}
$$
To get the actual correction in diurns, it is multiplied by the full length of the chronum ($\chi$) in the main equation.

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
- $\chi = 365.2564$ d (sidereal year)  
- $e = 0.0167$  

**Step 1 — Baseline**

$$
\frac{\chi}{4} = \frac{365.2564}{4} = 91.31
$$
**Step 2 — Correction Factor**

$$
\frac{2e}{\pi} \chi = \frac{2 \times 0.0167}{\pi} \times 365.2564 = 3.88
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
\Delta t \;\approx\; \frac{\chi}{4} + \left(\frac{2e}{\pi} \chi \times \sin\nu\right)
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
   - The approximation will always add up to the correct year length ($\chi$).  
   - Errors are usually small if $e \leq 0.1$ (a few diurns at most for Earth-like orbits).  

2. **Apply the generalized fudge factor.**  
   - To break the “paired seasons” pattern and create four distinct values, redistribute part of the correction term.  
   - Use the rule:

$$
     f = 10e
$$

- Subtract $f \times \left(\tfrac{2e}{\pi}\chi\right)$ from the long seasons (those with $\sin\nu = +1$).  
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
