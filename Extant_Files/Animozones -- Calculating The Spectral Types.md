---
title: ""
---



##### Nested Ontozonal Categories of Sun-like Stars

### Calculating The Spectral Types
Previously, in [[M002 - Stars — 06 Relating the Nucleal and Perannual Orbits ✓]], we established that the *distance* of the perannual orbit can be approximated by:

$$
P = \sqrt[3]{M}
$$
… and in [[M002 - Stars — 07 Fine-tuning Stellar Parameters ✓]], we established the relationship:

$$
L = M^{3.8}
$$
… which lets us calculate that:

$$
P = \sqrt[3]{\sqrt[3.8]{L}} = \sqrt[11.4]{L}
$$
In [[M002 - Stars — 04 Thermozone Orbits ✓]], we established that the thermozone limits are calculated by applying fixed scaling factors to the **nucleal orbit distance** ($N$), which is calculated from the square-root of the luminosity:

| Limiting<br>Orbit | Calculation |
| :---------------: | :-------------: |
| $H_0$ | $0.500\sqrt{L}$ |
| $H_1$ | $0.750\sqrt{L}$ |
| $H_2$ | $0.950\sqrt{L}$ |
| $H_3$ | $1.385\sqrt{L}$ |
| $H_4$ | $1.770\sqrt{L}$ |
| $H_5$ | $4.850\sqrt{L}$ |

This means that we can set:

$$
P = \sqrt[11.4]{L} \quad \text{equal to} \quad P = 0.500\sqrt{L}
$$
… and solve for L:

$$
\begin{aligned}
\sqrt[11.4]{L} &= 0.500\sqrt{L} \\
0.500 &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} -{\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
0.500 &= L^{-0.4123} \\
L &= \sqrt[-0.4123]{0.500} \\
&= 5.372\; ✓
\end{aligned}
$$
Converting luminosity to temperature:

$$
T = \sqrt[7.6]{L} = \sqrt[7.6]{5.372} = 1.248\;\odot
$$
In [[M002 - Stars — 02 Parameters ✓]], we established the following relationship between solar-unit temperature (*T*) and Kelvin temperature (*K*)

$$
K = 5800T
$$
So, our star has a Kelvin temperature of:

$$
K = 5800T = 5800(1.248) = 7235.97\;K
$$

… and we can calculate the spectral class and type:

$$
\begin{aligned}
S &= \dfrac{\kappa - K}{þ}
\end{aligned}
$$
Where:
- K = the star's surface temperature in Kelvin
- κ = the *upper bound* temperature of the relevant spectral class
- þ = the thermal interval constant for the relevant spectral class
- $S$ = the spectral *type* number

Taken from the table:

| Spectral<br>Class | <center>High<br>Temp.<br>(K)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ------------------------------------: | ------------------------------------------------------: |
| O | 55000 | 3000 |
| B | 25000 | 1500 |
| A | 10000 | 250 |
| F | 7500 | 150 |
| G | 6000 | 100 |
| K | 5000 | 150 |
| M | 3500 | 110 |
| L | 2400 | 110 |
| T | 1300 | 70 |
| Y | 600 | 30 |

Our Kelvin temperature is $7235.97\;K$ which is an F-type star, so
- κ = 7500
- þ = 150

$$
S = \dfrac{\kappa - K}{þ} = \dfrac{7500 - 7235.97}{150} = \dfrac{264.03}{150} = 1.76
$$
So the spectral type of a star with a perannual orbit at 0.500 AU is F 1.76 ✓.

### The Other End Of The Range
This means that we can set:

$$
P = \sqrt[11.4]{L} \quad \text{equal to} \quad P = 4.850\sqrt{L}
$$
… and solve for L:

$$
\begin{aligned}
\sqrt[11.4]{L} &= 4.850\sqrt{L} \\
4.850 &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} -{\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
4.850 &= L^{-0.4123} \\
L &= \sqrt[-0.4123]{4.850} \\
&= 0.022\; ✓
\end{aligned}
$$
Converting luminosity to temperature:

$$
T = \sqrt[7.6]{L} = \sqrt[7.6]{0.022} = 0.605\;\odot
$$
We have established the following relationship between solar-unit temperature (*T*) and Kelvin temperature (*K*)

$$
K = 5800T
$$
So, our star has a Kelvin temperature of:

$$
K = 5800T = 5800(0.605) = 3503.85\;K
$$
… which is a K-Class star with a $\kappa = 5000 \text{ and } þ = 150$, from which we can calculate the spectral type by:

$$
S = \dfrac{\kappa - K}{þ} = \dfrac{5000 - 3503.85}{150} = \dfrac{1496.185}{150} = 9.975
$$
So the spectral type of a star with a perannual orbit at $4.850$ AU is K9.975 ✓.

This means that the range of spectral types which host *perannual orbits within the **parahabitable** zone* is F1.76 – K9.932, which we can round for convenience to F2 – K9.

**Why K9 and not M0**
The exact math yields **F1.76 – K9.97**. For presentation, we **round inward** at both ends of the range to **F2 – K9** so that all perannual orbits calculated for stars within this range lies **strictly** inside the parahabitable band, avoiding knife‑edge cases at the hot and cold limits. (This convention absorbs small uncertainties in stellar parameters and subclass mapping.)

## Generalizing The Equation
This logic can be extended for any Hₓ value:
By generalizing the scaling factor **λ**, we can calculate the relative stellar luminosity for **any** perannual orbit distance:

$$
\begin{aligned}
\sqrt[11.4]{L} &= \lambda\sqrt{L} \\
\lambda &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} - {\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
\lambda &= L^{-0.4123} \\
\therefore L &= \sqrt[-0.4123]{\lambda} \; ✓
\end{aligned}
$$
# A Final Determination
Substituting all of the $H_x$ values in for λ:

| Limiting<br>Orbit | Scaling<br>Factor<br>(λ) | Calculation | <center>Luminosity<br>(L)</center><br> | Spectral<br>Type | <center>Animozone</center> |
| :---------------: | :----------------------: | :-------------------------: | -------------------------------------: | :--------------: | ------------------------- |
| $H_0$ | 0.500 | $L = \sqrt[-0.4123]{0.500}$ | 5.372 | F1.760 | Parahabitable |
| $H_1$ | 0.750 | $L = \sqrt[-0.4123]{0.750}$ | 2.009 | F7.615 | Habitable |
| $H_2$ | 0.950 | $L = \sqrt[-0.4123]{0.950}$ | 1.132 | G1.043 | Hospitable |
| $H_3$ | 1.385 | $L = \sqrt[-0.4123]{1.385}$ | 0.454 | G7.726 | Hospitable |
| $H_4$ | 1.770 | $L = \sqrt[-0.4123]{1.770}$ | 0.250 | K1.108 | Habitable |
| $H_5$ | 4.850 | $L = \sqrt[-0.4123]{4.850}$ | 0.022 | K9.972 | Parahabitable |

> **Keppy**: Seems like a lot of calculating and converting...

Well, without going into the gory details, you can calculate the relative or Kelvin temperature directly by:

$$
\begin{aligned}
K =5800(\lambda^{-0.3191}) \\[1em]
T = \lambda^{-0.3191}
\end{aligned}
$$

… which will allow you to calculate the spectral type for any perannual orbit at any orbital distance, and the reverse calculations are:

$$
\begin{aligned}
\lambda = \sqrt[-0.3191]{\dfrac{K}{5800}} \\[1em]
\lambda = \sqrt[-0.3191]{T}
\end{aligned}
$$
… which will give you the orbital distance of the perannual orbit for a star of any given Kelvin temperature (*K*) or relative temperature (*T*), since $T=\frac{K}{5800}$.

#### Thermal Axis for Perannual Orbits
This diagram shows the stellar surface temperatures (*K*) and corresponding spectral types required for a star’s *perannual orbit* to fall on each thermozone boundary $H_0$​ through $H_5$​. The core equation relates perannual distance scaling factor λ to stellar temperature *K*.

### Orbital Habitability Index (OHI)
The Orbital Habitability Index (OHI) is a measure of how likely a planemon is to be habitable based on its orbit, with the nucleal orbit assumed to be 100% habitable and orbits closer-in and farther-out becoming progressively less habitable. It is calculated using one of two equations, depending on whether the orbit in question is *intranucleal* or *extranucleal*:

The OHI provides a scalar measure (0.00–1.00) of the *relative biological viability* of a planemon orbit based on its distance from the nucleal orbit $N = \sqrt{L}$​. It assumes a peak habitability of 1.00 (100%) at 1.000N, declining linearly in each direction.

$$
H_I =
\begin{cases}
 \quad 2\dfrac{D}{N} - 1 & \text{if } {D} ≤ {N} \quad \text{(intranucleal)} \\[1em]
 -0.26\dfrac{D}{N} + 1.26 & \text{if } {D} > {N} \quad \text{(extranucleal)}
\end{cases}
\text{Where } R = \dfrac{D}{N}: \quad H_I =
\begin{cases}
 \quad 2R - 1 & \text{if } R ≤ 1 \quad \text{(intranucleal)} \\
 -0.26R + 1.26 & \text{if } R > 1 \quad \text{(extranucleal)}
\end{cases}
$$

Where:
- $H_I$ = the numeric value of the orbit's habitability index
- *$D$* = the orbit's distance in AU
- $N$ = the nucleal orbit's distance in AU

Values of *D* < 0.500$N$ and > 4.850$N$ return *negative numbers* for $H_I$, indicating that the orbit is not hospitable, habitable, or parahabitable for Earth-type lifeforms.

| Orbit<br>Type | Orbit<br>Distance | Habitability<br>Index |
| :-----------: | :---------------: | :-------------------: |
| Intranucleal |     0.500$N$      | 0.00 |
| Intranucleal |     0.750$N$      | 0.50 |
| Intranucleal |     0.950$N$      | 0.90 |
| Nucleal |     1.000$N$      | 1.00 |
| Extranucleal |     1.385$N$      | 0.90 |
| Extranucleal |     1.770$N$      | 0.80 |
| Extranucleal |     4.850$N$      | 0.00 |

