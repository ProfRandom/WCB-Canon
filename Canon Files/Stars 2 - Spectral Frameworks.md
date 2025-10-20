---
title: ""
---

## Abstract  
**Major Topics:**  
- Establishes the **WCB Stellar Framework** — a unified, linearized model for stellar temperature, luminosity, and class that supports both astrophysical realism and worldbuilding clarity.  
- Defines the **spectral classification sequence** (O, B, A, F, G, K, M + L, T, Y) in a **continuous temperature scale**, smoothing irregularities in the traditional OBAFGKM system.  
- Introduces the **spectral-type index (𝓢)** and the **thermal interval constant (þ)**, enabling decimal interpolation (e.g., F3.65, G9.19) without creating new classes.  
- Derives the governing relations among:  
  - **Spectral parameters:** $K = κ − 𝓢 þ$ and $T = K / 5800$  
  - **Class constants:** $þ = (high − low)/10$ K per subclass  
- Expands the framework to the **five core stellar parameters** — temperature (T/K), mass (M), radius (R), luminosity (L), and lifetime (Q) — with **temperature as the primary** and **radius as the secondary** controlling variable.  
- Applies the **Stefan–Boltzmann Law** ($L = 4πR^2σT^4$ → $L = R^2 T^4$ in solar units) and the **blackbody approximation** (ϵ ≈ 1) to model stellar irradiance and flux.  
- Provides complete **parameter-derivation chains** allowing any variable (T, M, R, L, Q) to seed the others, simplifying habitability and orbit modeling.  
- Introduces **refined calibration exponents** for main-sequence stars:  
  - $M = T^{2.0}$ $L = T^{7.6}$ $L = M^{3.8}$  
  - Exact recommended values: 7.5778 and 3.7889.  
- Adds **direct luminosity conversions** among all parameters, enhancing computational speed and consistency across worldbuilding modules.  
- Includes tabulated spectral-class data (O–M, plus brown-dwarf LTY classes) in both Kelvin and solar-relative units.  

**Key Terms & Symbols:**  
- **Spectral Class / Type (𝓢)** — continuous classification by surface temperature.  
- **þ (thorn)** — Thermal Interval Constant, subclass temperature step.  
- **κ (kappa)** — upper-bound temperature of class.  
- **K, T** — absolute and solar-relative temperature.  
- **M, R, L, Q** — stellar mass, radius, luminosity, and lifetime (⊙ units).  
- **ϵ, σ** — emissivity and Stefan–Boltzmann constant.  
- **Calibrated Exponents:** 7.5778 (for T ↔ L), 3.7889 (for M ↔ L).  

**Cross-Check Notes:**  
- Consolidates prior *Stars 2–3* material: spectral classification, parametric equations, and exponent calibration.  
- Supplies the **quantitative foundation** for *Stars 1 — Fundamental Orbits* and all subsequent habitability modeling.  
- Harmonizes stellar and planetary notation (upper- vs. lower-case).  
- Connects forward to *Stars 6 — Reference Tables* for numeric lookup and to *Planemons 2 — Habitability* for irradiance-based design.

# Stars and Spectral Classes: The Fusion-Fueled Continuum

First: The spectral class system used throughout this guide — the sequence **O, B, A, F, G, K, M** — is historically rooted in the observational astronomy of the late 19th and early 20th centuries. Its peculiar alphabetical order reflects the evolution of stellar classification from empirical cataloging to physical understanding.

> For readers curious about its origins — including the critical work of **Annie Jump Cannon**, **Cecilia Payne-Gaposchkin**, and the less brilliant men who received most of the credit — see **[[Sidebar: The Spectral System and the Women Who Built It]]**.

Second: The spectral classes used in WCB are based on a **linearized temperature model**. This approach smooths over the irregularities of the traditional system to support clean interpolation, symbolic clarity, and consistent orbital modeling.

> If you're curious about the limitations of the classical OBAFGKM system — and why we’ve chosen to “straighten the curve” — see **[[Sidebar Module: *Mind the Gap — The Shortcomings of the Traditional Spectral Scale*]]**.

## Spectral Class Table
Here are the spectral classes we'll be working with.

|  Spectral<br>Class  | Low Temp. (K) | High Temp. (K) |
| :-----------------: | ------------: | -------------: |
|          O          |         25000 |          55000 |
|          B          |         10000 |          25000 |
|          A          |          7500 |          10000 |
|          F          |          6000 |           7500 |
|          G          |          5000 |           6000 |
|          K          |          3500 |           5000 |
|          M          |          2400 |           3500 |
| Brown<br>↓ Dwarfs ↓ |               |                |
|          L          |          1300 |           2400 |
|          T          |           600 |           1300 |
|          Y          |           300 |            600 |

> Notes:
> - Spectral Classes L, T, and Y are "special cases" which are covered in detail in another module ⟨⟨ insert module name here ⟩⟩
> - Each range reflects a star's **surface temperature**, typically noted as $T_{\text{eff}}$ in astronomical literature.
> - In WCB:
> 	- **K** = temperature in Kelvin 
> 	- **T** = temperature *relative to the Sun* (i.e., ⊙ = 5800K ⇒ T = 1.0)
### Spectral *Type*
Each spectral class is subdivided into 10 **spectral types**, numbered **0** (hottest) to **9** (coolest).

> **Hippy**: Wait, that's  – 

Yes, it runs *backwards*. No, we’re not happy about it, either (don't shoot the messenger).

For example:  
- The Sun, at **5800K**, is classified as a **G2** star —  
	- Spectral **Class**: G  
	- Spectral **Type**: 2

> #### Note on Spectral Type Precision in WCB
> In this system, a **spectral type** is defined by its **numerical position** within a spectral class.  For example:
> - **G2**, **G2.3**, and **G2.9** are all **Type 2** 
> - The decimal simply adds interpolation precision — it does **not** define a new type.
> - Therefore, **Type 2** refers to the full range ⟨2.0 ∧ 2.999···⟩ within class *G*.

This allows for relatively simple mathematical treatment of the relationship between spectral type (T) and surface temperature (K).

$$
\begin{aligned}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\ \\
\kappa & = \mathcal{S} þ + K \\ \\
K &= \kappa - \mathcal{S} þ \\ \\
þ &= \dfrac{\kappa - K}{\mathcal{S}} \\
\end{aligned}
$$

Where:
- K = the star's surface temperature in Kelvin
- κ = the *upper bound* temperature of the relevant spectral class
- þ = the thermal interval constant for the relevant spectral class
- $\mathcal{S}$ = the spectral *type* number

#### The Thermal Interval Constant (þ)
Where does þ come from?
For a given spectral class þ can be calculated by:

$$
þ = \dfrac{high\;temp - low\;temp}{10}
$$

Here is the above table with these constants added:


| Spectral<br>Class | <center>Low<br>Temp.<br>(Kelvin)</center> | <center>High<br>Temp.<br>(Kelvin)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ----------------------------------------: | -----------------------------------------: | ------------------------------------------------------: |
|         O         |                                     25000 |                                      55000 |                                                    3000 |
|         B         |                                     10000 |                                      25000 |                                                    1500 |
|         A         |                                      7500 |                                      10000 |                                                     250 |
|         F         |                                      6000 |                                       7500 |                                                     150 |
|         G         |                                      5000 |                                       6000 |                                                     100 |
|         K         |                                      3500 |                                       5000 |                                                     150 |
|         M         |                                      2400 |                                       3500 |                                                     110 |
|         L         |                                      1300 |                                       2400 |                                                     110 |
|         T         |                                       600 |                                       1300 |                                                      70 |
|         Y         |                                       300 |                                        600 |                                                      30 |
|                   |                                           |                                            |                                                         |
|                   |                                           |                                            |                                                         |

#### Example
Let's run the numbers for the Sun
- Known surface temperature: 5800K
- Checking the table, 5800K falls between 5000K and 6000K, so the Sun is spectral class G
- The high temperature (κ) for spectral class G is κ 6000K
- The thermal interval constant (þ) for spectral class G is þ = 100
- What is the Sun's spectral type ($\mathcal{S}$)
Running the numbers:

$$
\begin{aligned}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\
\mathcal{S} &= \dfrac{6000 - 5800}{100} \\
\mathcal{S} &= \dfrac{200}{100} \\
\mathcal{S} &= 2\;✓
\end{aligned}
$$
The Sun is spectral type *G2*.

**Reversing the process:**
- The known spectral class of the Sun is G
- The known spectral type of the Sun is $\mathcal{S}$ = 2
- The high temperature (κ) for spectral class G is κ 6000K
- The thermal interval constant (þ) for spectral class G is þ = 100
- What is the Sun's Kelvin temperature (K)
Running the numbers:

$$
\begin{aligned}
K &= \kappa - \mathcal{S} þ \\
K &= 6000 - (2)(100) \\
K &= 6000 - 200 \\
K &= 5800\;✓
\end{aligned}
$$
The surface temperature of the Sun is *5800K*.

### Converting Between Absolute Kelvin (K) And Solar Relative (T)
Nothing could be simpler:

$$
\begin{aligned}
T &= \dfrac{K}{5800} \\ \\
K &= 5800T
\end{aligned}
$$
For instance: the Sun's surface temperature is K = 5800:

$$
T = \dfrac{K}{5800} = \dfrac{5800}{5800} = 1\;✓
$$
Conversely, the Sun's relative temperature is T = 1.0:

$$
K = 5800 T = (5800)(1) = 5800\;✓
$$
### Fictional Examples
Let's say we have a star called Essem that we want to be spectral type *F3.65*.  What is its Kelvin temperature?
- The surface temperature for spectral class F is K ∈ ⟨6000 ∧ 7500⟩.
- The thermal interval constant for spectral class F is þ = 150.
Working through the equation:

$$
\begin{aligned}
K &= \kappa - \mathcal{S} þ \\
K &= 7500 - (3.65)(150) \\
K &= 7500 - 547.5 \\
K &= 6952.5\;✓
\end{aligned}
$$
What is Essem's relative surface temperature?

$$
\begin{aligned}
T = \dfrac{K}{5800} \\ \\
T = \dfrac{6952.5}{5800} \\ \\
T = 1.199\;✓
\end{aligned}
$$
Essem's relative temperature is *T = 1.199*⊙.

**Working The Other Direction**

Let us say that Essem has a near neighbor, Essel, and we know that its relative temperature is T = 0.876⊙.  What is its spectral type?

First, convert T to K by:

$$
K = 5800T = (5800)(0.876) = 5080.8\;✓
$$
Looking at our table we see that this value falls in spectral class G:

| Spectral<br>Class | <center>Low<br>Temp.<br>(Kelvin)</center> | <center>High<br>Temp.<br>(Kelvin)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ----------------------------------------: | -----------------------------------------: | ------------------------------------------------------: |
|         G         |                                      5000 |                                       6000 |                                                     100 |

… which gives us all the other information we need:
- G-class high temperature is κ = 6000
- G-class thermal interval constant is þ = 100

The spectral type is:

$$
\begin{aligned}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\ \\
\mathcal{S} &= \dfrac{6000 - 5080.8}{100} \\ \\
\mathcal{S} &= \dfrac{919.2}{100} \\ \\
\mathcal{S} &= 9.192\;✓
\end{aligned}
$$
Essel's spectral type is *G9.192*.
### Parameter Ranges By Spectral Class

# Parameter Ranges by Spectral Class

|        | SC →       | <center>O</center> | <center>B</center> | <center>A</center> | <center>F</center> | <center>G</center> | <center>K</center> | <center>M</center> |
| ------ | ---------- | -----------------: | -----------------: | -----------------: | -----------------: | -----------------: | -----------------: | -----------------: |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |              55000 |              25000 |              10000 |               7500 |               6000 |               5000 |               3500 |
| Kelvin | Mean       |              40000 |              17500 |               8750 |               6750 |               5500 |               4250 |               2950 |
|        | Low        |              25000 |              10000 |               7500 |               6000 |               5000 |               3500 |               2400 |
|        | TIC¹ (*þ*) |               3000 |               1500 |                250 |                150 |                100 |                150 |                110 |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |             9.4828 |             4.3103 |             1.7241 |             1.2931 |             1.0345 |             0.8621 |             0.6034 |
| T⊙     | Mean       |             6.8966 |             3.0172 |             1.5086 |             1.1638 |             0.9483 |             0.7328 |             0.5086 |
|        | Low        |             4.3103 |             1.7241 |             1.2931 |             1.0345 |             0.8621 |             0.6034 |             0.4138 |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |            17.0690 |             7.7586 |             3.1034 |             2.3276 |             1.8621 |             1.5517 |             1.0862 |
| R⊙     | Mean       |            12.4138 |             5.4310 |             2.7155 |             2.0948 |             1.7069 |             1.3190 |             0.9155 |
|        | Low        |             7.7586 |             3.1034 |             2.3276 |             1.8621 |             1.5517 |             1.0862 |             0.7448 |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |            2.356 M |           20.779 k |            85.1093 |            15.1476 |             3.9709 |             1.3298 |             0.1565 |
| L⊙     | Mean       |          348.608 k |            2.445 k |            38.1967 |             8.0501 |             2.3559 |             0.5015 |             0.0561 |
|        | Low        |           20.779 k |             85.109 |            15.1476 |             3.9709 |             1.3298 |             0.1565 |             0.0163 |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |            18.7759 |             8.5345 |             3.4138 |             2.5603 |             2.0483 |             1.7069 |             1.1948 |
| M⊙     | Mean       |            13.6552 |             5.9741 |             2.9871 |             2.3043 |             1.8776 |             1.4509 |             1.0071 |
|        | Low        |             8.5345 |             3.4138 |             2.5603 |             2.0483 |             1.7069 |             1.1948 |             0.8193 |
|        |            |                    |                    |                    |                    |                    |                    |                    |
|        | High       |          64.10E-06 |           4.00E-03 |             0.1280 |             0.4684 |             1.3041 |             4.7336 |            29.3785 |
| Q⊙     | Mean       |           0.67E-03 |          65.64E-03 |             0.2766 |             0.8441 |             2.1003 |            12.4968 |            82.4297 |
|        | Low        |           0.69E-06 |          35.57E-06 |           3.47E-03 |             0.0146 |             0.0447 |             0.1112 |             0.6614 |

¹ Thermal Interval Constant
# Stellar Parametrics
In *Spectral Classes*, we covered spectral classes and spectral types and their association to the surface temperatures of stars.  Stars, like planemons, have a basic set of parameters that describe them:
- **Temperature** — How hot is the surface?
	- Absolute measure: Kelvin (K)
	- Relative measure: Solar units (T)
- **Mass** — How much material is there? (M)
- **Luminosity** — How bright is it? (L)
- **Radius** — How big is it? (R)
- **Lifetime** — How long does it shine? ($\mathcal{Q}$)
	- Chiefly relevant to *Main Sequence* stars, particularly stars that are **Solar Cognates** (more on this below.)

> Notes:
> 1. Where we use lower-case letters for the parameters of planemons, we use upper-case letters for stars, so it's easy to tell them apart.
> 2. While **mass** (*m*) is the primary parameter for planemons, with **density** (*ρ*) secondary, for stars **Temperature** (*T*) is the primary parameter, and **radius** (*R*) is secondary.
> 	- While luminosity is **technically derived** from a star's temperature and radius (see *the Stefan-Boltzmann Law*, below), it plays a **central role** in modeling stellar systems — particularly when calculating orbit distances, habitable zones, and irradiance. In practice, it’s often treated as the secondary parameter after termperature for thesisastics.

## Equations of State
A regularized set of empirical relationships can be used to estimate any stellar parameter from the others — assuming a Main Sequence **blackbody**-like star (see [[Sidebar — What Is The Main Sequence]]).

> **Keppy**: And a **blackbod**y is...?

Excellent question!  A **blackbody** is an **idealized physical object** that:
1. **Absorbs all** incoming electromagnetic radiation — no reflection, no transmission.
2. **Emits radiation** purely based on its temperature — not its material, shape, or color.
3. Emits a **perfectly smooth, continuous spectrum** (a "thermal spectrum").

In short:
> A blackbody is the theoretical gold standard for radiant heat emission — a perfect radiator and absorber.

#### Why "Blackbody" Matters Here
Most stars (especially Main Sequence stars) behave **approximately like blackbodies**, meaning their energy output can be modeled using **temperature alone**. This makes them excellent candidates for:
- **Temperature-based modeling**
- **Color-temperature mapping** (blue = hotter, red = cooler)
- **Spectrum-based classification** (like spectral classes O–M)
- Real-World Deviation
	- planemons, dust clouds, and even stars aren’t *perfect* blackbodies.
	- Real objects have an **emissivity** ϵ between 0 and 1:

$$ F = \varepsilon \sigma T^4$$
- But stars are close enough that the **blackbody approximation works very well**.

> **Hippy**: Sorry you asked, Keplarius?

Yes, that's a bit technical and complicated, but it's also extremely *important* to what comes next.

Here are the promised equations:

$$
\begin{array}{c|c|c|c}
\text{Temperature} &\text{Mass} &\text{Radius} &\text{Lifetime} \\[0.1em]
\text{(T)} &\text{(M)} &\text{(R)} & \text{($\mathcal{Q}$)} \\[0.5em] 
\hline\\[-2pt]
T=\sqrt[1.98]{M} & M=\sqrt[0.9]{R} & R=M^{0.9} & \mathcal{Q}=M^{-2.5} \\[0.5em]
T=\sqrt[1.8]{R} & M=T^{1.98} & R=T^{1.8} & \mathcal{Q} \approx \sqrt[-0.36]{R} \\[0.5em]
T=\mathcal{Q}^{-0.2} & M=\mathcal{Q}^{-0.4} & R=\mathcal{Q}^{-0.36} & \mathcal{Q}=T^{-5}
\end{array}
$$
> > **NOTE**:
> > All of the above equations are *approximations*; stars are a much more variable set of objects (after all, they're mostly gas and plasma, so fluid dynamics plays a major role in their characteristics).  These equations work **best *in general* for main sequence stars** of all classes.

> **Keppy**: You said Luminosity was the second most important parameter for stars, but it doesn't appear in the table...?

Well spotted, Keppy!  There's a reason.
### The Stefan-Boltzmann Law
The Stefan-Boltzmann Law is a formulation that relates the **luminosity** of any luminous object to its **temperature** and **surface area**:

$$
L = 4 \pi R^2 \sigma T^4
$$
Where:
- $4 \pi R^2$  = the surface area of the body
- $T$ = is the temperature of the body in Kelvin
- $σ$ = the Stefan-Boltzmann constant
	- $\sigma = 5.670374419 \times 10^{-8} W m^{-2}K^{-4}$
		- **Watts** per square meter per Kelvin to the fourth power 1 K⁴
		- It tells you how much **radiant energy per second** (i.e., power) is emitted by a **1 square meter** portion of a **perfect blackbody** at **1 K⁴**.

And this is why we needed the quick aside into the term "blackbody" earlier.

In worldmaking terms, we can simplify the Stefan-Boltzmann equation to:

$$
\dfrac{L_s}{L_{Sun}} = \left(\dfrac{R_s}{R_{Sun}}\right)^2 \left(\dfrac{K_s}{K_{Sun}}\right)^4
$$
Where:
- $L_S$ = the absolute luminosity of the star
- $L_{Sun}$ = the absolute luminosity of the Sun
- $R_S$ = the absolute radius of the star
- $R_{Sun}$ = the absolute radius of the Sun
- $K_S$ = the Kelvin temperature of the star
- $K_{Sun}$ = the Kelvin temperature of the Sun

Because the form $\dfrac{X_s}{X_{Sun}}$ is the standard for converting a parameter to solar units, and $T = \dfrac{K_s}{K_{Sun}}$, this equation becomes:

$$
\begin{aligned}
L &= R^2T^4, \qquad \text{with derivations of} \\ \\
R &= \dfrac{\sqrt{L}}{T^2}, \qquad
T = \sqrt[4]{\dfrac{L}{R^2}}
\end{aligned}
$$
## Parameter Calculation Precedence
The above being the case, there is a "best" order for calculating stellar parameters when starting from any given parameter (though it is always best start with *K* or *T* whenever possible).

> All parameters (except K) are expressed in Solar-relative units; that is, T = 1⊙ for 5800 K, R = 1⊙ for the solar radius, etc.

#### Starting with Temperature (*T*) or (*K*)
**Primary dependency chain**: T/K → R → L → M → Q

$$
\begin{aligned}
T &= \dfrac{K}{5800} \quad or \quad K = 5800T \\
R &= T^{1.8} \\
L &= R^2T^4 \\
M &= T^{1.98} \quad or \quad M = \sqrt[0.9]{R} \\
\mathcal{Q} &= T^{-5} \quad or \quad \mathcal{Q} = M^{-2.5}
\end{aligned}
$$
#### Starting with Mass (*M*)
**Primary dependency chain**: M → T/K → R → L → Q

$$
\begin{aligned}
T &= \sqrt[1.98]{M} \\
K &= 5800T \\
R &= T^{1.8} \quad or \quad R = M^{0.9} \\
L &= R^2T^4 \\
Q &= T^{-5} \quad or \quad Q = M^{-2.5}
\end{aligned}
$$
#### Starting with Radius (*R*)
**Primary dependency chain**: R → T → K → L → M → 𝒬

$$
\begin{aligned}
T &= \sqrt[1.8]{R} \\
K &= 5800T \\
L &= R^2T^4 \\
M &= T^{1.98} \\
\mathcal{Q} &= T^{-5} \quad or \quad \mathcal{Q} = M^{-2.5}
\end{aligned}
$$
#### Starting With Luminosity (*L*)
**Primary dependency chain**: L → T → K → R → M → Q

$$
\begin{aligned}
T &= \sqrt[7.6]{L} \\
K &= 5800T \\
R &= T^{1.8} \\
M &= T^{1.98} \\
\mathcal{Q} &= T^{-5} \quad or \quad \mathcal{Q} = M^{-2.5}
\end{aligned}
$$
#### Starting with Lifetime (𝒬)
**As soon as you assume you'd never want to do this, you'll find a case for doing it.**
**Primary dependency chain**: 𝒬 → T → K → R → L → M

$$
\begin{aligned}
T &= \mathcal{Q}^{-0.2} \\
K &= 5800 T \\
R &= \mathcal{Q}^{-0.36} \\
L &= R^2 T^4 \\
M &= \sqrt[3]{L}
\end{aligned}
$$
# Fine-tuning Stellar Parameters
## Standard Parameter Equations
The Standard Parameter Equations:

$$
\begin{array}{c|c|c|c}
\text{Temperature} &\text{Mass} &\text{Radius} &\text{Lifetime} \\[0.1em]
\text{(T)} &\text{(M)} &\text{(R)} & \text{($\mathcal{Q}$)} \\[0.5em] 
\hline\\[-2pt]
T=\sqrt[1.98]{M} & M=\sqrt[0.9]{R} & R=M^{0.9} & \mathcal{Q}=M^{-2.5} \\[0.5em]
T=\sqrt[1.8]{R} & M=T^{1.98} & R=T^{1.8} & \mathcal{Q} \approx \sqrt[-0.36]{R} \\[0.5em]
T=\mathcal{Q}^{-0.2} & M=\mathcal{Q}^{-0.4} & R=\mathcal{Q}^{-0.36} & \mathcal{Q}=T^{-5}
\end{array}
$$
… *generally* work well for most **Main Sequence** stars, but a survey of known stars in the Solar neighborhood —

> **Hippy**: "Wha–"

… *which is too complex and extensive to detail here* — suggests that *modest* adjustments to a couple of key exponents yield parameter equations that better reflect observed stellar characteristics. Since worldmaking prioritizes plausible-world construction over strict theoretical purity, these revised values offer better performance across the mass range of interest.

### Modified Parameters Table# Main Sequence Stellar Equations of State
$$
\begin{array}{c|c|c|c|c}
\text{Temperature} &\text{Mass} &\text{Radius} &\text{Lifetime} & \text{Lifetime} \\[0.1em]
\text{(T)} &\text{(M)} &\text{(R)} & \text{($\mathcal{Q}$)} &\text{(L)} \\[0.5em] 
\hline\\[-2pt]
T=\sqrt{M} & M=\sqrt[0.9]{R} & R=M^{0.9} & \mathcal{Q}=M^{-2.5} & L - M^{3.8} \\[0.5em]
T=\sqrt[1.8]{R} & M=T^{1.98} & R=T^{1.8} & \mathcal{Q} \approx \sqrt[-0.36]{R} & L \approx R^{4.\bar{2}} \\[0.5em]
T=\mathcal{Q}^{-0.2} & M=\mathcal{Q}^{-0.4} & R=\mathcal{Q}^{-0.36} & \mathcal{Q}=T^{-5} & L = T^{7/6} \\[0.5em]
T= \sqrt[7.6]{L} & M = \sqrt[3.8]{L} & R \approx \sqrt[4.\bar{2}]{L} & \mathcal{Q} = L^{-1.52} & L = \sqrt[-1.52]{\mathcal{Q}}
\end{array}
$$
**Notes**:
- The parameter relationship that changed from the previous table was $T ↔︎ M$, where the exponent increased slightly from $1.98$ to $2.0$
- The **major change** is the addition of direct calculation for the parameters to-and-from luminosity; these are included for the purpose of simplifying much of the math related to [[M002 - Stars — 08 `Sun-Like` Stars ✓]].
- **For *greatest accuracy***:
	- The exponent $7.6$ can be more precisely specified as $7.5778$
	- The exponent $3.8$ can be more precisely specified as $3.7889$