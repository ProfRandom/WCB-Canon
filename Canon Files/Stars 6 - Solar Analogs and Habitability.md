---
title: ""
---

## Abstract 
**Major Topics:** 
- Reconstructs the vague astronomical notion of “Sun-like stars” into a clear, mathematically grounded **WCB classification hierarchy** tied to orbital habitability rather than surface resemblance. 
- Defines nested stellar categories by **ontozonal boundaries** and **perannual orbit ranges (𝒫):** 
 - **Solar Analogs:** stars whose perannual orbits span ⟨0.500 ∧ 4.850⟩ AU — the full Parahabitable Zone (H₀–H₅) — corresponding to spectral types F2–K9. 
 - **Solar Cognates:** perannual orbits within ⟨0.750 ∧ 1.770⟩ AU — the Habitable Zone (H₁–H₄) — spectral types F7.6–K1.1. 
 - **Solar Twins:** perannual orbits within ⟨0.950 ∧ 1.385⟩ AU — the Hospitable Zone (H₂–H₃) — spectral types G1.0–G7.7. 
 - All Twins ⊂ Cognates ⊂ Analogs. 
- Links **stellar luminosity (L)** to **perannual orbit (𝒫)** via $𝒫 = L^{1/11.4}$, allowing direct determination of spectral type for any orbit located on a thermozone boundary (H₀–H₅). 
- Derives a **generalized scaling relation** between luminosity and the thermozone factor (λ): 
 - $L = \sqrt[-0.4123]{λ}$ and $K = 5800(λ^{-0.3191})$ 
 - These enable forward and inverse calculations of stellar temperature or orbital distance. 
- Introduces the **Orbital Habitability Index (OHI)** — a continuous scalar (0.00–1.00) quantifying relative habitability as a function of distance from the **nucleal orbit (𝒩 = √L)**: 
 - Intranucleal: $H_I = 2R − 1$ (for R ≤ 1) 
 - Extranucleal: $H_I = −0.26R + 1.26$ (for R > 1) 
 - Index peaks at 1.00 when 𝒫 = 𝒩, declining to 0.00 at H₀ and H₅. 
- Establishes the **Thermal Axis for Perannual Orbits**, mapping stellar temperature and spectral class across all habitability zones (H₀–H₅). 
- Provides a practical framework for evaluating the “Sun-likeness” of a star directly from its habitability potential, not merely its photometric similarity. 

**Key Terms & Symbols:** 
- **Solar Analog / Cognate / Twin:** nested WCB categories of Sun-like stars based on ontozonal position. 
- **𝒫 (Perannual Orbit):** period-equivalent orbital distance. 
- **𝒩 (Nucleal Orbit):** irradiance-equivalent orbital distance. 
- **H₀–H₅ (Thermozones):** reference corridors of orbital habitability. 
- **λ (Scaling Factor):** ratio of 𝒫 to 𝒩. 
- **OHI (Orbital Habitability Index):** 0–1 scalar quantifying orbital habitability. 

**Cross-Check Notes:** 
- Builds directly upon *Stars 1 — Fundamental Orbits* (definitions of 𝒩 and 𝒫) and *Stars 2 — Spectral Frameworks* (luminosity–temperature relations). 
- Introduces new glossary terms: Solar Analog, Solar Cognate, Solar Twin, and OHI. 
- Serves as the conceptual and computational bridge between **stellar classification** and **habitability analysis**, forming the gateway to *Stars 5 — System Architecture* and *Planemons 2 — Habitability.*

# Solar Analogs, Cognates, and Twins

The published literature often speaks of *solar analog* stars, but tends to be distressingly vague about exactly what the term means. Generally speaking, it means *a star very much like the Sun*.

> **Keppy**: And that doesn't help at all — that could mean *any* star, really.

You're right; so, for our purposes we have our own definitions, based on *orbits* and the animozones. But, first, a survey of existing terminology.

## Existing Definitions
A *Sun-like star* is a broad term used to describe stars that share characteristics with our own Sun. Astronomers often categorize them into a hierarchy based on their *physical* similarity to the Sun. They all need to be main-sequence stars**, actively fusing hydrogen into helium in their core, like our Sun. Otherwise:

**Solar-type Stars:** This is the broadest category. These stars are broadly similar to the Sun in mass and evolutionary state. Key characteristics include: 
 - **Spectral type:** Typically F8V (6300 K) to K2V (4700 K) — more on this below.
 
**Solar Analogs:** These stars are more similar to the Sun than general solar-type stars, conforming to stricter criteria:
- **Temperature:** Within approximately 500 Kelvin (K) of the Sun's temperature (which is about 5800 K) — between 5300 K (G7V) and 6300 K (F8V). 
**Solar Twins:** This is the most restrictive category, for stars that are nearly identical to the Sun. The idea is that they are virtually indistinguishable from our Sun in as many ways as possible:
- **Temperature:**
	- Within a very narrow range, typically ±10 K of the Sun's temperature — 5790 K (G2.1V) to 5810 K (G1.9V).
	- Some definitions are even stricter, within ±5 K — 5795 K (G2.05V) to 5805 K (G1.95V).
- **Age**:
	- **4.3 – 4.7 Gyr** (The Sun's age ±200 Ma)
 - Sometimes as tight as **±100 Ma**, i.e., **4.4 – 4.6  Gyr**

## A Proposed, Clearer System
For thesiastic purposes, our classifications relate directly to the *habitability potential of orbiting planemos*, rather than just their parent stars’ physical resemblance to the Sun.

**Solar Analogs**:
- Stars whose *perannual orbits* fall within ⟨0.500 ∧ 4.850⟩ AU, spanning from the Inner Parahabitable Zone to the Outer Parahabitable Zone (H₀ – H₅), spectral types F2 – K9.
**Solar Cognates**:
- Stars whose *perannual orbits* fall within ⟨0.750 ∧ 1.770⟩ AU, spanning from the Inner Habitable Zone to the Outer Habitable Zone (H₁ – H₄), spectral types F7.62 – K1.11.
**Solar Twins**:
- Stars whose *perannual orbits* fall within ⟨0.950 ∧ 1.385⟩ AU, spanning the Hospitable Zone (H₂ – H₃), spectral types G1.04 – G7.73.
*Thus*:
- All *Solar Twins* are also *Solar Cognates* and *Solar Analogs*.
- All *Solar Cognates* are also *Solar Analogs*.
- *Solar Analogs* encompass the *Solar Cognate* and *Solar Twin* categories.

> **NOTE**:
> - This perannual-orbit-based requirement is largely arbitrary, predicated on the thesiastic idea that a planemon that is least different from Earth would have an orbital period the same as Earth's.

##### Nested Ontozonal Categories of Sun-like Stars

### Calculating The Spectral Types
Previously, in [[M002 - Stars — 06 Relating the Nucleal and Perannual Orbits ✓]], we established that the *distance* of the perannual orbit can be approximated by:

$$
\mathcal{P} = \sqrt[3]{M}
$$
… and in [[M002 - Stars — 07 Fine-tuning Stellar Parameters ✓]], we established the relationship:

$$
L = M^{3.8}
$$
… which lets us calculate that:

$$
\mathcal{P} = \sqrt[3]{\sqrt[3.8]{L}} = \sqrt[11.4]{L}
$$
In [[M002 - Stars — 04 Thermozone Orbits ✓]], we established that the thermozone limits are calculated by applying fixed scaling factors to the **nucleal orbit distance** ($\mathcal{N}$), which is calculated from the square-root of the luminosity:

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
\mathcal{P} = \sqrt[11.4]{L} \quad \text{equal to} \quad \mathcal{P} = 0.500\sqrt{L}
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
\mathcal{S} &= \dfrac{\kappa - K}{þ}
\end{aligned}
$$
Where:
- K = the star's surface temperature in Kelvin
- κ = the *upper bound* temperature of the relevant spectral class
- þ = the thermal interval constant for the relevant spectral class
- $\mathcal{S}$ = the spectral *type* number

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
\mathcal{S} = \dfrac{\kappa - K}{þ} = \dfrac{7500 - 7235.97}{150} = \dfrac{264.03}{150} = 1.76
$$
So the spectral type of a star with a perannual orbit at 0.500 AU is F 1.76 ✓.

### The Other End Of The Range
This means that we can set:

$$
\mathcal{P} = \sqrt[11.4]{L} \quad \text{equal to} \quad \mathcal{P} = 4.850\sqrt{L}
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
\mathcal{S} = \dfrac{\kappa - K}{þ} = \dfrac{5000 - 3503.85}{150} = \dfrac{1496.185}{150} = 9.975
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

The OHI provides a scalar measure (0.00–1.00) of the *relative biological viability* of a planemon orbit based on its distance from the nucleal orbit $\mathcal{N} = \sqrt{L}$​. It assumes a peak habitability of 1.00 (100%) at 1.000N, declining linearly in each direction.

$$
H_I =
\begin{cases}
 \quad 2\dfrac{D}{\mathcal{N}} - 1 & \text{if } {D} ≤ {\mathcal{N}} \quad \text{(intranucleal)} \\[1em]
 -0.26\dfrac{D}{\mathcal{N}} + 1.26 & \text{if } {D} > {\mathcal{N}} \quad \text{(extranucleal)}
\end{cases}
\text{Where } R = \dfrac{D}{\mathcal{N}}: \quad H_I =
\begin{cases}
 \quad 2R - 1 & \text{if } R ≤ 1 \quad \text{(intranucleal)} \\
 -0.26R + 1.26 & \text{if } R > 1 \quad \text{(extranucleal)}
\end{cases}
$$

Where:
- $H_I$ = the numeric value of the orbit's habitability index
- *$D$* = the orbit's distance in AU
- $\mathcal{N}$ = the nucleal orbit's distance in AU

Values of *D* < 0.500$\mathcal{N}$ and > 4.850$\mathcal{N}$ return *negative numbers* for $H_I$, indicating that the orbit is not hospitable, habitable, or parahabitable for Earth-type lifeforms.

| Orbit<br>Type | Orbit<br>Distance | Habitability<br>Index |
| :-----------: | :----------------: | :-------------------: |
| Intranucleal | 0.500$\mathcal{N}$ | 0.00 |
| Intranucleal | 0.750$\mathcal{N}$ | 0.50 |
| Intranucleal | 0.950$\mathcal{N}$ | 0.90 |
| Nucleal | 1.000$\mathcal{N}$ | 1.00 |
| Extranucleal | 1.385$\mathcal{N}$ | 0.90 |
| Extranucleal | 1.770$\mathcal{N}$ | 0.80 |
| Extranucleal | 4.850$\mathcal{N}$ | 0.00 |

