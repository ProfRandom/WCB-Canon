# Quartal-Length Estimation Methods (Sinusoidal)
This process assumes that you have already determined the duration of your planet's orbit around its star (its *sidereal chronum*, $\chi$).

## Chronex of the Tempostat

**Station (Chronal)** *($\varsigma_n$)* —
A **geometric orientation event** in which a planet’s rotational axis attains one of four characteristic alignments relative to its star, *as viewed from above the planet’s right-hand-rule north pole*. 
- Each **station** ($\varsigma_n$) corresponds to an **axial alignment angle** ($Ⲁ_n$) separated by 90° in orbital longitude, marking a **temporal node** that bounds successive quarta within a chromum.

- **Quartum** *(pl. quarta)* —  
  One quarter of a planet’s orbital period (denoted $Q_0, Q_1, Q_2, Q_3$); a **non-climatological “quartal.”**  
    A quartum is a **temporal span**, not a spatial angle — a section of the orbit *traversed through time* between two successive chronal stations.

**Tempostat** —
The **onset event** of the first quartum following periapsis; marks the temporal origin of the planet’s annual cycle.
* Defined by its **chronex (ζ)** — the true anomaly of the planet at the moment the first axial station occurs post-periapsis.
* The tempostat is an *event*, not a variable; it establishes the chromum’s temporal phase reference.
* It need not correspond to any surface season or cultural new year — it is purely orbital and axial in definition.

- **Chronex** *($\zeta$)* —  
  The **true anomaly** of the tempostat.  

## 1. Sinusoidal Approximation (Fast vs. Slow Half)
Here is a quick, algebra-only method that captures the *main effect of eccentricity* on quarta:

$$
Q \;\approx\; \dfrac{\chi}{4} + \left(\dfrac{2\!\;\chi\!\;e}{\pi} \times \sin \zeta\right)
$$
Where:  
- $\chi$ = year length (chronum, in diurns or days)  
- $e$ = orbital eccentricity  
- $\zeta$ = true anomaly of the tempostat  

## Quartal Adjustment
True anomaly of each **quartal onset** is determined from the **chronex** (ζ):

$$
\begin{aligned}
&Ⲁ_n = (\zeta + 90n) \bmod 360 \\[1em]
&\begin{cases}
n = 1 & Q_0 \\
n = 0 & Q_1 \\
n = 3 & Q_2 \\
n = 2 & Q_3 \\
\end{cases}
\end{aligned}
$$
**NOTE: *The n-values here are out of numerical order so that the Earth's seasons come out listed in order of:***
- Spring
- Summer
- Autumn
- Winter

For fictional worlds, using an order of n = {0, 1, 2, 3}  will still produce usable results — which surface season they apply to is a matter of crafter's-choice.

#### Worked Example: Earth (Sinusoidal Approximation, Sidereal Chronum)
Given:  
- $\zeta = 77$  
- $\chi = 365.2564$ d (sidereal year)  
- $e = 0.0167$  

**Step 3 — Quartal Adjustments**
True anomalies from $\zeta = 0$:

$$
Ⲁ_n = (\zeta + 90n) \bmod 360
$$
$$
\begin{cases}
n = 1 & Ⲁ_1 = 167^\circ & \quad Q_0 \\
n = 2 & Ⲁ_2 = 77^\circ & \quad Q_1 \\
n = 3 & Ⲁ_3 = 347^\circ & \quad Q_2 \\
n = 0 & Ⲁ_0 = 357^\circ & \quad Q_3
\end{cases}
$$

**Step 4 — Apply the Formula**

$$
Q_n \;\approx\; \frac{\chi}{4} + \left(\frac{2\!\;\chi\!\;e}{\pi} \times \sin Ⲁ_n \right)
$$
$$
\begin{cases}
n=1;\;Ⲁ_1 = 167^\circ;\;\sinⲀ_1 = 0.2250 & Q_0 \approx 92.18 \\
n=2;\;Ⲁ_2 = 257^\circ;\;\sinⲀ_2 = 0.9744 & Q_1 \approx 87.53 \\
n=3;\;Ⲁ_3 = 347^\circ;\;\sinⲀ_3 = -0.225 & Q_2 \approx 90.44 \\
n=0;\;Ⲁ_0 = 77^\circ;\;\sinⲀ_0 = -0.9744 & Q_3 \approx 95.09
\end{cases}
$$

**Result:**  
- $Q_0$ ≈ 92.18 d  
- $Q_1$ ≈ 95.09 d  
- $Q_2$ ≈ 90.44 d  
- $Q_3$ ≈ 87.53 d  
(Total = 365.24219 d)

**Conclusion**

The observed lengths of Earth's quartals are approximately:
- $Q_0$ ≈ 92.771 d  
- $Q_1$ ≈ 93.641 d  
- $Q_2$ ≈ 89.834 d  
- $Q_3$ ≈ 88.994 d
- (Total = 365.2400 d)
    - The difference in the totals here is due to the fact that the process is returning fractions of the *sidereal year*, but the observed values are fractions of the *tropical year*.

Discrepancies:

- $Q_0$ ≈ -0.59 d  
- $Q_1$ ≈ 1.49 d  
- $Q_2$ ≈ 0.60 d  
- $Q_3$ ≈ -1.47 d 

### ⚠️ **Symmetry Note — When ζ mod 90° = 0**

The sinusoidal tempostatic equation:

$$
Q_n \;\approx\; \frac{χ}{4} + \frac{2\!\,\chi\!\;e}{\pi} \sinⲀ_n
$$

produces two identical quartal durations whenever the **tempostat chronex ζ** lies at a 90° multiple — that is, when $ζ \bmod 360° = 0°, 90°, 180°, 270°$.

This arises directly from the sine function’s symmetry:

$$
\sin(ζ + 180°) = −\sin ζ.
$$

As a result, **Q₀** and **Q₂** (the first and third quarta) mirror one another in duration, yielding *paired quarta*.  

In any real planetary system where ζ ≠ 0° (mod 90°), this degeneracy breaks naturally and all four quarta become distinct.  
No correction or “fudge factor” is required.

> **Note:** This pairing is *not* a failure of the method.  
> It reflects the actual temporal geometry a world would experience if its tempostat chronex ζ were perfectly aligned with a symmetry point of its orbit.  
> Such a planet would, in fact, exhibit two matching quartal spans during each chromum.
