📖 Season-Length Estimation Methods
This process assumes that you have already determined the duration of your planet's orbit around its star (its *sidereal chronum*, $C$).

# Eccentric Anomaly Conversion (Kepler's Method)

This more precise method uses full orbital geometry to determine **season lengths** and **solar flux variations** throughout the year.

## Eccentric Anomaly (E)

The **eccentric anomaly**, $E$, is an angular coordinate that describes a body’s position along an **elliptical orbit** in a way that keeps Kepler’s equation simple.

Imagine a circle drawn around the ellipse with the same center and major axis. If you project the planet’s position *up* to that circle by a line drawn perpendicular to the major axis, the angle at the center of the ellipse between that line and the direction of periastron is the **eccentric anomaly**.

In other words:

- The *true anomaly* ($ν$) is the angle measured **at the focus** — from periastron to the planet itself.  
- The *eccentric anomaly* ($E$) is measured **at the center** — from periastron to the projected point on the reference circle.  
- The *mean anomaly* ($M$) increases uniformly with time and connects to $E4 through Kepler’s Equation:

$$
M = E - e\,\sin E
$$

The eccentric anomaly acts as the mathematical bridge between the **uniform time variable** ($M$) and the **actual orbital position** ($ν$). 
It allows us to calculate how much of the orbital period has elapsed at any given geometric position — even when the orbit is not circular.


## Obliquity Azimuth (φ)

The *obliquity azimuth* defines the orbital longitude where the planet’s northern hemisphere is tilted directly away from its star.  
If this occurs at **periastron**, then φ = 0°.

$$
\begin{array}{l r l}
\phi = &0^\circ & \text{Northern hemisphere tilted directly \textit{away} from the star at periastron.} \\
\phi = &90^\circ & \text{Tilted away at one-fourth orbit \textit{after} periastron.} \\
\phi = &180^\circ & \text{Tilted away at one-half orbit \textit{after} periastron (apastron).} \\
\phi = &270^\circ & \text{Tilted away at three-fourths orbit \textit{after} periastron.}
\end{array}
$$

The value of φ may be any angle from 0° to 359°, depending on the planet’s **axial precession**.

The Obliquity Azimuth ($\phi$) therefore acts as a **phase offset** between the orbit’s eccentric anomaly and the planet’s seasonal cycle, determining whether perihelion aligns with summer or winter in each hemisphere.

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
\begin{aligned}
E &= 2 \arctan \!\left( \sqrt{\dfrac{1-e}{1+e}} \;\tan \dfrac{\nu}{2} \right) \\[1em]
\nu &= 2 \arctan \!\left( \sqrt{\dfrac{1+e}{1-e}} \;\tan \dfrac{E}{2} \right)
\end{aligned}
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