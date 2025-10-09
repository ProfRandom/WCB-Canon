---
title: ""
---

## Abstract  
**Major Topics:**  
- Defines the **stellar spectral classification system** (O, B, A, F, G, K, M; plus L, T, Y) in a **linearized temperature model** for WCB use.  
- Spectral Classes are set by **surface temperature ranges** ($T_{\text{eff}}$ in Kelvin).  
- Each Class is subdivided into **Spectral Types** (0–9), numbered backwards (0 = hottest).  
- Establishes formulas for interconversion between:  
  - Spectral Type (𝓢),  
  - Surface temperature in Kelvin (K),  
  - Relative solar temperature (T),  
  - High-class temperature bound (κ),  
  - Thermal interval constant (þ).  
- Introduces **thermal interval constants** (þ) for each Class, computed as (high – low)/10.  
- Provides worked examples for:  
  - The Sun (G2, 5800K, T=1.0),  
  - Essem (F3.65, 6952.5K, T=1.199),  
  - Essel (G9.192, 5081K, T=0.876).  
- Includes expanded **parameter tables by spectral class**: Kelvin ranges, T⊙, R⊙, L⊙, M⊙, and Q⊙.  

**Key Terms & Symbols:**  
- **Spectral Class** — O, B, A, F, G, K, M (+ L, T, Y).  
- **Spectral Type** — subclass 0–9 (backwards numbering).  
- **K** — effective surface temperature in Kelvin.  
- **T** — temperature relative to Sun (⊙ = 5800K ⇒ T = 1.0).  
- **κ (kappa)** — high temperature bound of class.  
- **þ (thorn)** — thermal interval constant = (high – low)/10.  
- **𝓢** — spectral type number.  

**Cross-Check Notes:**  
- Provides **linearized model** vs. traditional classification irregularities.  
- Supports interpolation (decimal values, e.g. G2.3, G2.9) without creating new types.  
- Forms the **baseline module** for stellar characterization in WCB.  
- Connects stellar parameters (L⊙, R⊙, M⊙, Q⊙) to habitability modeling.  

___
___



# Stars and Spectral Classes: The Fusion-Fueled Continuum

First: The spectral class system used throughout this guide — the sequence **O, B, A, F, G, K, M** — is historically rooted in the observational astronomy of the late 19th and early 20th centuries. Its peculiar alphabetical order reflects the evolution of stellar classification from empirical cataloging to physical understanding.

> For readers curious about its origins — including the critical work of **Annie Jump Cannon**, **Cecilia Payne-Gaposchkin**, and the less brilliant men who received most of the credit — see **[[Sidebar: The Spectral System and the Women Who Built It]]**.

Second: The spectral classes used in WCB are based on a **linearized temperature model**. This approach smooths over the irregularities of the traditional system to support clean interpolation, symbolic clarity, and consistent orbital modeling.

> If you're curious about the limitations of the classical OBAFGKM system — and why we’ve chosen to “straighten the curve” — see **[[Sidebar Module: _Mind the Gap — The Shortcomings of the Traditional Spectral Scale_]]**.

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
> 	- **T** = temperature _relative to the Sun_ (i.e., ⊙ = 5800K ⇒ T = 1.0)
### Spectral *Type*
Each spectral class is subdivided into 10 **spectral types**, numbered **0** (hottest) to **9** (coolest).

> **Hippy**: Wait, that's  – 

Yes, it runs _backwards_. No, we’re not happy about it, either (don't shoot the messenger).

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
\begin{align}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\ \\
\kappa & = \mathcal{S} þ + K \\ \\
K &= \kappa - \mathcal{S} þ \\ \\
þ &= \dfrac{\kappa - K}{\mathcal{S}} \\
\end{align}
$$

Where:
- K = the star's surface temperature in Kelvin
- κ = the _upper bound_ temperature of the relevant spectral class
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
\begin{align}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\
\mathcal{S} &= \dfrac{6000 - 5800}{100} \\
\mathcal{S} &= \dfrac{200}{100} \\
\mathcal{S} &= 2\;✓
\end{align}
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
\begin{align}
K &= \kappa - \mathcal{S} þ \\
K &= 6000 - (2)(100) \\
K &= 6000 - 200 \\
K &= 5800\;✓
\end{align}
$$
The surface temperature of the Sun is *5800K*.

### Converting Between Absolute Kelvin (K) And Solar Relative (T)
Nothing could be simpler:
$$
\begin{align}
T &= \dfrac{K}{5800} \\ \\
K &= 5800T
\end{align}
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
\begin{align}
K &= \kappa - \mathcal{S} þ \\
K &= 7500 - (3.65)(150) \\
K &= 7500 - 547.5 \\
K &= 6952.5\;✓
\end{align}
$$
What is Essem's relative surface temperature?
$$
\begin{align}
T = \dfrac{K}{5800} \\ \\
T = \dfrac{6952.5}{5800} \\ \\
T = 1.199\;✓
\end{align}
$$
Essem's relative temperature is *T = 1.199*⊙.

**Working The Other Direction**

Let us say that Essem has a near neighbor, Essel, and we know that its relative temperature is T = 0.876⊙.  What is its spectral type?

First, convert T to K by:
$$ K = 5800T = (5800)(0.876) = 5080.8\;✓ $$
Looking at our table we see that this value falls in spectral class G:

| Spectral<br>Class | <center>Low<br>Temp.<br>(Kelvin)</center> | <center>High<br>Temp.<br>(Kelvin)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ----------------------------------------: | -----------------------------------------: | ------------------------------------------------------: |
|         G         |                                      5000 |                                       6000 |                                                     100 |

… which gives us all the other information we need:
- G-class high temperature is κ = 6000
- G-class thermal interval constant is þ = 100

The spectral type is:
$$
\begin{align}
\mathcal{S} &= \dfrac{\kappa - K}{þ} \\ \\
\mathcal{S} &= \dfrac{6000 - 5080.8}{100} \\ \\
\mathcal{S} &= \dfrac{919.2}{100} \\ \\
\mathcal{S} &= 9.192\;✓
\end{align}
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

## Abstract  
**Major Topics:**  
- Defines the **five core stellar parameters**:  
  - Temperature (K, T)  
  - Mass (M)  
  - Radius (R)  
  - Luminosity (L)  
  - Lifetime (Q)  
- Establishes **parameter precedence**: temperature (T/K) is primary, radius (R) is secondary.  
- Provides **equations of state** for main-sequence stars, allowing any parameter to be derived from another.  
- Introduces the **blackbody approximation**, with emissivity (ϵ) correction.  
- Explains the **Stefan–Boltzmann Law** and its solar-relative simplification ($L = R^2T^4$).  
- Presents dependency chains for deriving all parameters starting from T, M, R, L, or Q.  
- Emphasizes practical use in **worldbuilding calculations** (habitability, orbits, irradiance).  

**Key Terms & Symbols:**  
- **K** — Stellar surface temperature in Kelvin.  
- **T** — Temperature relative to solar (T = K/5800).  
- **M** — Stellar mass (⊙).  
- **R** — Stellar radius (⊙).  
- **L** — Stellar luminosity (⊙).  
- **Q** — Stellar lifetime (⊙ units).  
- **ϵ (epsilon)** — Emissivity, fraction of ideal blackbody radiation (0–1).  
- **σ (Stefan–Boltzmann constant)** = $5.670374419 × 10^{-8} W·m^{-2}·K^{-4}$.  

**Cross-Check Notes:**  
- Direct analog to planemo parameter system (m, r, ρ, g, vₑ).  
- Stars: **T primary, R secondary**.  
- Planemos: **m primary, ρ secondary**.  
- Provides unified framework for comparing stellar and planetary parameters.  

___
___



# Stellar Parametrics
In *Spectral Classes*, we covered spectral classes and spectral types and their association to the surface temperatures of stars.  Stars, like planemos, have a basic set of parameters that describe them:
- **Temperature** — How hot is the surface?
	- Absolute measure: Kelvin (K)
	- Relative measure: Solar units (T)
- **Mass** — How much material is there? (M)
- **Luminosity** — How bright is it? (L)
- **Radius** — How big is it? (R)
- **Lifetime** — How long does it shine? ($\mathcal{Q}$)
	- Chiefly relevant to _Main Sequence_ stars, particularly stars that are **Solar Cognates** (more on this below.)

> Notes:
> 1. Where we use lower-case letters for the parameters of planemos, we use upper-case letters for stars, so it's easy to tell them apart.
> 2. While **mass** (*m*) is the primary parameter for planemos, with **density** (*ρ*) secondary, for stars **Temperature** (*T*) is the primary parameter, and **radius** (*R*) is secondary.
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
	- planemos, dust clouds, and even stars aren’t _perfect_ blackbodies.
	- Real objects have an **emissivity** ϵ between 0 and 1:
$$ F = \varepsilon \sigma T^4$$
- But stars are close enough that the **blackbody approximation works very well**.

> **Hippy**: Sorry you asked, Keplarius?

Yes, that's a bit technical and complicated, but it's also extremely _important_ to what comes next.

Here are the promised equations:

|   Temperature<br>(T)   |      Mass<br>(M)       |      Radius<br>(R)      |            Lifetime<br>(Q)            |
| :--------------------: | :--------------------: | :---------------------: | :-----------------------------------: |
|   $T=\sqrt[1.98]{M}$   |   $M=\sqrt[0.9]{R}$    |       $R=M^{0.9}$       |        $\mathcal{Q}=M^{-2.5}$         |
|   $T=\sqrt[1.8]{R}$    |      $M=T^{1.98}$      |       $R=T^{1.8}$       | $\mathcal{Q} \approx \sqrt[-0.36]{R}$ |
| $T=\mathcal{Q}^{-0.2}$ | $M=\mathcal{Q}^{-0.4}$ | $R=\mathcal{Q}^{-0.36}$ |         $\mathcal{Q}=T^{-5}$          |

> > **NOTE**:
> > All of the above equations are _approximations_; stars are a much more variable set of objects (after all, they're mostly gas and plasma, so fluid dynamics plays a major role in their characteristics).  These equations work **best _in general_ for main sequence stars** of all classes.

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
\begin{align}
L &= R^2T^4, \qquad \text{with derivations of} \\ \\
R &= \dfrac{\sqrt{L}}{T^2}, \qquad
T = \sqrt[4]{\dfrac{L}{R^2}}
\end{align}
$$
## Parameter Calculation Precedence
The above being the case, there is a "best" order for calculating stellar parameters when starting from any given parameter (though it is always best start with *K* or *T* whenever possible).
> All parameters (except K) are expressed in Solar-relative units; that is, T = 1⊙ for 5800 K, R = 1⊙ for the solar radius, etc.
#### Starting with Temperature (*T*) or (*K*)
**Primary dependency chain**: T/K → R → L → M → Q
$$
\begin{gather}
T = \dfrac{K}{5800} \quad or \quad K = 5800T \\
R = T^{1.8} \\
L = R^2T^4 \\
M = T^{1.98} \quad or \quad M = \sqrt[0.9]{R} \\
\mathcal{Q} = T^{-5} \quad or \quad \mathcal{Q} = M^{-2.5}
\end{gather}
$$
#### Starting with Mass (*M*)
**Primary dependency chain**: M → T/K → R → L → Q
$$
\begin{gather}
T = \sqrt[1.98]{M} \\
K = 5800T \\
R = T^{1.8} \quad or \quad R = M^{0.9} \\
L = R^2T^4 \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting with Radius (*R*)
**Primary dependency chain**: R → T → K → L → M → 𝒬
$$
\begin{gather}
T = \sqrt[1.8]{R} \\
K = 5800T \\
L = R^2T^4 \\
M = T^{1.98} \\
\mathcal{Q} = T^{-5} \quad or \quad \mathcal{Q} = M^{-2.5}
\end{gather}
$$
#### Starting With Luminosity (*L*)
**Primary dependency chain**: L → T → K → R → M → Q
$$
\begin{gather}
T = \sqrt[7.6]{L} \\
K = 5800T \\
R = T^{1.8} \\
M = T^{1.98} \\
Q = T^{-5} \quad or \quad Q = M^{-2.5}
\end{gather}
$$
#### Starting with Lifetime (*𝒬*)
\**As soon as you assume you'd never want to do this, you'll find a case for doing it.*\*
**Primary dependency chain**: 𝒬 → T → K → R → L → M
$$
\begin{gather}
T=\mathcal{Q}^{-0.2} \\
K = 5800T \\
R=\mathcal{Q}^{-0.36} \\
L = R^2T^4 \\
M = \sqrt[3]{L}
\end{gather}
$$      

 
## Abstract  
**Major Topics:**  
- Defines the **Nucleal Orbit (𝒩)** — orbital distance at which a planemo receives the same stellar irradiance as Earth does at 1 AU.  
- Formula: 𝒩 = √L (where L = stellar luminosity in ⊙ units).  
- Anchors the **habitable zone (HZ)** around a star as ranges proportional to 𝒩.  
- Distinguishes between:  
  - **Habitable Zone** — wider corridor (⟨0.750 ∧ 1.770⟩𝒩).  
  - **Hospitable Zone** — narrower “middle lane” (⟨0.950 ∧ 1.385⟩𝒩).  
- Defines **parahabitable, habitable, hospitable, xenotic** orbital spans as structured “Ontozones.”  
- Introduces the **Frost Line (ϝ)** at 4.850𝒩, beyond which water cannot remain liquid.  
- Specifies notation for inner and outer orbital regimes:  
  - $Z_{IX}$, $Z_{IP}$, $Z_{IH}$, $Z_H$, $Z_{OH}$, $Z_{OP}$, $Z_{OX}$.  

**Key Terms & Symbols:**  
- **𝒩 (Nucleal Orbit)** — central reference orbit for irradiance equivalence.  
- **ϝ (Frost Line)** — outer limit for liquid water (~4.850𝒩).  
- **Ontozones** — structured orbital bands around stars.  
- **Zone Notation:**  
  - $Z_{IX}$ — Inner Xenotic Zone (<0.500𝒩).  
  - $Z_{IP}$ — Inner Parahabitable Zone (0.500–0.750𝒩).  
  - $Z_{IH}$ — Inner Habitable Zone (0.750–0.950𝒩).  
  - $Z_H$ — Hospitable Zone (0.950–1.385𝒩).  
  - $Z_{OH}$ — Outer Habitable Zone (1.385–1.770𝒩).  
  - $Z_{OP}$ — Outer Parahabitable Zone (1.770–4.850𝒩).  
  - $Z_{OX}$ — Outer Xenotic Zone (≥4.850𝒩).  

**Cross-Check Notes:**  
- Builds directly on **Habitable Zone Limits (H₀–H₅)** from v1.219.  
- Adds layered refinement: narrower **Hospitable Zone** within the wider HZ.  
- Introduces **Ontozones** and **zone notation system** for systematic classification.  
___
___



## The Nucleal Orbit
The average distance from Earth to the Sun — about $1.496 \times 10^8$ km — is defined as one **astronomical unit (AU)**. Due to Earth’s slightly elliptical orbit, this distance varies by approximately ±2.5 million km between Earth's closest approach to and farthest distance from the Sun.

So, for all practical (and thesiastic) purposes, the Earth's orbital distance (*a*) is a = 1.0AU.  In fact *a* is the commonly used symbol for _any_ orbital distance when it is expressed in Astronomical Units.

For our purposes, I have revived an old word from the dusty backroom shelves of English — *nucleal* — and given it new life:

> **Nucleal Orbit** ($\mathcal{N}$): the orbital distance from any given star at which a planemo receives the same stellar irradiance as Earth receives from the Sun at 1 AU.

… and given it the utterly unimaginative symbol, $\mathcal{N}$.

The important thing to note here is that *$\mathcal{N}$ is not constant*, but varies from star to star, and it is calculated by:
$$
\mathcal{N} = \sqrt{L}
$$
Where:
- *L* = the Luminosity of the star in relative units

Obviously for the Sun:
$$
\mathcal{N} = \sqrt{L} = \sqrt{1} = 1
$$
> **Keppy**: So for a dimmer star N shifts closer to the star?

> **Hippy**: And for a brighter star, it shifts farther out from the star.

Correct on both counts.  And once we know _$\mathcal{N}$_, we can express the **habitable zone** (details coming!) as a proportional range around it.  For instance, for a star of half the Sun's luminosity $L = 0.5⊙$:
$$
\mathcal{N} = \sqrt{L} = \sqrt{0.5} = 0.7071\;AU
$$
### The Nucleal Orbit and the Habitable Zone
A quick survey of the existing literature reveals a commonly held definition for the **habitable zone** as:
$$
\langle0.950 \wedge 1.385\rangle \mathcal{N}
$$
… or, in other words: between 95% of the nucleal orbit distance to 1.385 times (138.5%) the nucleal orbit distance.  In the case of our hypothetical $L = 0.5⊙$ star and its $\mathcal{N}$ nucleal orbit, the range of its habitable zone calculates to:
$$
\begin{gather}
\mathcal{N} = 0.7071\; AU \\
\text{Inner Edge} = 0.950 \mathcal{N} = (0.950)(0.7071) = 0.6717\; AU \\
\text{Outer Edge} = 1.385 \mathcal{N} = (1.385)(0.7071) = 0.9793\; AU
\end{gather}
$$
> **Keppy**: So ... the *outer edge* of this star's habitable zone is *closer to its star* than *Earth orbits from the Sun*.....

Exactly.  But, this region is only a part of a total star system.
### The Ontozones – Two Habitable Zones
To start with, some scientist posit a wider, more "optimistic habitable zone" region, covering:
$$
\langle0.750 \wedge 1.770\rangle \mathcal{N}
$$
For our purposes, we call this *wider spread* the actual **habitable zone** and we call the narrower span the **hospitable zone**, so that the *hospitable zone* comprises a middle lane between the extremes of the *habitable zone*:
$$
\dfrac{1.385 - 0.95}{1.77 - 0.75} = \dfrac{0.435}{1.02} = 0.4265\;AU
$$
… about 42.65% of it, in fact.

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
It has also been suggested that "desert" planemos (think Dune, Tattooine) might orbit in the zone between ⟨0.500 ∧ 0.750⟩N and we might call this the "desert planemo zone", which would be, by definition, **parahabitable** to **habitable** (but mostly the former).

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
### The Frost Line (ϝ)
Research indicates that beyond a distance of about $a = 4.850\;AU$ in our Solar system, water cannot remain liquid due to insufficient irradiance from the Sun.  This distance is sometimes termed the "Frost Line" or "Ice Line", and an orbital distance of $a = 4.850N$ is the value we set for this outer limit.

For instance:
- Mars' orbit in our own Solar system is $a = 1.524\;AU$, well within the $1.770N$ limit
- The asteroid belt is ≈ ⟨2.2 ∧ 3.2⟩AU, beyond $1.77\mathcal{N}$, but still within the $4.850\;AU$ ϝ limit.  This region in our Solar system does not host a sizeable planemo (and likely never did), but if one were to exist there, it would probably be parahabitable due to the orbital distance from the Sun.

This gives us another range of orbits we can add to our accounting:

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Parahabitable              |

Jupiter's orbit is at $a = 5.204\;AU$, well _beyond_ the $4.850\;AU$ limit, and things just get colder from there, so we can specify that if any kind of "life" does exist in this region it is likely to be extremophile by Earth standards, which WCB denotes as "***xenotic***".

|         Orbital Range         | <center>Ontozones</center> |
| :---------------------------: | -------------------------- |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$  | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$  | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$  | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$  | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$N | Parahabitable              |
|     4.850$\mathcal{N}$ →      | Xenotic                    |
Similarly, any "life" that might come to be on a body orbiting closer than 0.500N would also be xenotic:

|        Orbital Range         | <center>Ontozones</center> |
| :--------------------------: | -------------------------- |
|     ← 0.500$\mathcal{N}$     | Xenotic                    |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Parahabitable              |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Habitable Zone             |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Parahabitable              |
|     4.850$\mathcal{N}$ →     | Xenotic                    |
Finally, we differentiate between inner and outer zones, and define notations for each:

|        Orbital Range         | <center>Ontozones</center> | Notation |
| :--------------------------: | -------------------------- | -------- |
|     ← 0.500$\mathcal{N}$     | Inner Xenotic Zone         | $Z_{IX}$ |
| ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Inner Parahabitable Zone   | $Z_{IP}$ |
| ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Inner Habitable Zone       | $Z_{IH}$ |
| ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            | $Z_{H}$  |
| ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Outer Habitable Zone       | $Z_{OH}$ |
| ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Outer Parahabitable Zone   | $Z_{OP}$ |
|     4.850$\mathcal{N}$ →     | Outer Xenotic Zone         | $Z_{OX}$ |
This gives us a full inventory of orbital limits for any star system we choose to devise.

## Abstract  
**Major Topics:**  
- Introduction of **thermozones** as orbital bands derived from multiples of the Nucleal Orbit (𝒩).  
- Mapping of thermozones to **Ontozones** (habitability categories): xenotic, parahabitable, habitable, hospitable.  
- Distinct naming scheme rooted in **Latin/Greek etymologies**:  
  - *Igniozone, Calorozone, Heliozone, Solarazone, Hiberozone, Brumazone, Cryozone*.  
- **Thermozone Limit Notation (H₀…H₅):** standardized subscripts marking orbital cutoffs (0.5𝒩 through 4.85𝒩).  
- Relationship of 𝒩 to Solarazone: always lies 11.49% inward from its inner edge.  
- Provides a consistent, mnemonic framework for discussing orbital corridors across any star system.  

**Key Terms & Symbols:**  
- **Thermozone names:** Igniozone, Calorozone, Heliozone, Solarazone, Hiberozone, Brumazone, Cryozone.  
- **Notation:** $Z_{..}$ for ontozones, H₀–H₅ for thermozone limits.  
- **Nucleal Orbit (𝒩):** always located inside Solarazone.  
- **Ontozones:** Inner/Outer Xenotic, Parahabitable, Habitable, Hospitable.  

**Cross-Check Notes:**  
- Several **new glossary terms** staged: thermozone names, *Thermozone Limit Notation (H₀–H₅)*.  
- Builds directly on **Nucleal Orbit (𝒩)** (from Stars 03).  
- Provides the **didactic bridge** between raw stellar flux math and corridor naming for worldbuilders.  


# Star System Thermozones
We've already introduced the term Habitable Zone before, sometimes also prosaically referred to as "The Goldilocks Zone".

> **Hippy**: Silliness!

Well....  Scientists _do_ try to keep things accessible for those not familiar with the official lingo.

Anyway, broadly speaking, this is the range of orbital distances around a given star in which an orbiting planemo might reasonably be expected to retain liquid water and a reasonably dense atmospheric envelope. In the previous section, we defined the *parahabitable*, *habitable*, and *hospitable* zones as occupying this region.

> **Keppy**: But this is based on ... what?

I'm glad you asked; it's based on how much energy (irradiance) the planemo receives from its star compared to how much insolation the Earth receives from the Sun (you may remember this concept from our discussion of the _nucleal orbit_.  And _that_ gives us our standard candle (if you'll pardon the pun).
## Naming The Zones And Labeling Their Limits

### The Thermozones
For ease of remembering these zones and their ontosomic characteristics we use the **thermozone** naming system:

| Thermozone |        Orbital Range         | <center>Ontozones</center> | Notation |                        |
| :--------- | :--------------------------: | -------------------------- | -------- | ---------------------- |
| Igniozone  |     ← 0.500$\mathcal{N}$     | Inner Xenotic Zone         | $Z_{IX}$ | "Desert planemo Zone"  |
| Calorozone | ⟨0.500 ∧ 0.750⟩$\mathcal{N}$ | Inner Parahabitable Zone   | $Z_{IP}$ |                        |
| Heliozone  | ⟨0.750 ∧ 0.950⟩$\mathcal{N}$ | Inner Habitable Zone       | $Z_{IH}$ |                        |
| Solarazone | ⟨0.950 ∧ 1.385⟩$\mathcal{N}$ | Hospitable Zone            | $Z_{H}$  |                        |
| Hiberozone | ⟨1.385 ∧ 1.770⟩$\mathcal{N}$ | Outer Habitable Zone       | $Z_{OH}$ |                        |
| Brumazone  | ⟨1.770 ∧ 4.850⟩$\mathcal{N}$ | Outer Parahabitable Zone   | $Z_{OP}$ |                        |
| Cryozone   |     4.850$\mathcal{N}$ →     | Outer Xenotic Zone         | $Z_{OX}$ | "Glacier planemo Zone" |
These names are derived from:
- **Igniozone**: Latin *ignis*, "fire"
- **Calorozone**: Latin *calor*, "hot, heat"
- **Heliozone**: Greek *Helios*, an early name of the Sun god
	- Planemos in this region might be somewhat Earth-like in environment, but generally warmer\*
- **Solarazone**: Latin *solar*, from *Sol*, a title of the Sun god
	- Planemos in this region are likely to be very Earth-like in their environment\*
- **Hiberozone**: Latin *hiberno*, "cold"
- **Brumazone**: Latin *bruma*, "winter"
- **Cryozone**: Greek *kryo*, "cold"

\* Assuming they are otherwise Earth-like in size and composition.
#### Thermozone Limit Notation
For ease of reference, the limiting orbital distances of the thermozones are denoted by an *H* accompanied by a subscript:

| Notation |  Orbital Distance  |
| :------: | :----------------: |
| H₀       | 0.500$\mathcal{N}$ |
| H₁       | 0.750$\mathcal{N}$ |
| H₂       | 0.950$\mathcal{N}$ |
| H₃       | 1.385$\mathcal{N}$ |
| H₄       | 1.770$\mathcal{N}$ |
| H₅       | 4.850$\mathcal{N}$ |
Adding these to our earlier table:

| <center>Thermozone</center> | <center>Zone<br>Limits</center> | <center>Orbital<br>Range</center><br> | <center>Ontozones</center> | Notation |                       |
| --------------------------- | :-----------------------------: | :-----------------------------------: | -------------------------- | -------- | --------------------- |
| Igniozone                   |              ← H₀               |         ← 0.500$\mathcal{N}$          | Inner Xenotic Zone         | $Z_{IX}$ | "Desert planemo Zone" |
| Calorozone                  |            ⟨H₀ ∧ H₁⟩            |     ⟨0.500 ∧ 0.750⟩$\mathcal{N}$      | Inner Parahabitable Zone   | $Z_{IP}$ |                       |
| Heliozone                   |            ⟨H₁ ∧ H₂⟩            |     ⟨0.750 ∧ 0.950⟩$\mathcal{N}$      | Inner Habitable Zone       | $Z_{IH}$ |                       |
| Solarazone                  |            ⟨H₂ ∧ H₃⟩            |     ⟨0.950 ∧ 1.385⟩$\mathcal{N}$      | Hospitable Zone            | $Z_{H}$  |                       |
| Hiberozone                  |            ⟨H₃ ∧ H₄⟩            |     ⟨1.385 ∧ 1.770⟩$\mathcal{N}$      | Outer Habitable Zone       | $Z_{OH}$ |                       |
| Brumazone                   |            ⟨H₄ ∧ H₅⟩            |     ⟨1.770 ∧ 4.850⟩$\mathcal{N}$      | Outer Parahabitable Zone   | $Z_{OP}$ |                       |
| Cryozone                    |              H₅ →               |         4.850$\mathcal{N}$ →          | Outer Xenotic Zone         | $Z_{OX}$ | "Glaci planemo Zone"  |
This gives us a very robust way of discussing orbital distances in any star system.

Note that the *nucleal orbit*, being always $\mathcal{N} = 1.0N$, always falls within the Solarazone.  In fact, it always falls at 11.49% _into_ the Solarazone from its inner edge.


## Abstract  
**Major Topics:**  
- Definition of the **Perannual Orbit (𝒫):** the orbital distance in a star system where a planemo completes exactly one Earth sidereal year (365.256363 ephemeris days).  
- Distinction between **sidereal year** (fixed stars, used for 𝒫) and **tropical year** (surface experience of seasons).  
- Calculation of orbital period using Kepler’s Third Law in Solar-relative units:  
  - $P = \sqrt{\dfrac{a^3}{M+m}}$  
  - $a = \sqrt[3]{P^2 (M+m)}$  
  - $M+m = \dfrac{a^3}{P^2}$  
- Effect of planemo mass (*m*) on orbital period (generally negligible but measurable; e.g., Earth’s mass shifts orbital period by ~47 seconds).  
- 𝒫 compared with the **Nucleal Orbit (𝒩):**  
  - Can be **intranucleal** (inside 𝒩) or **extranucleal** (outside 𝒩).  
  - Only coincides with 𝒩 when $M = 1⊙$ (and $m = 1⨁$ ideally).  
- Unlike 𝒩 (irradiance-based), 𝒫 depends on **mass**, making it a **temporal reference** rather than a thermal one.  
- Final simplification: for the perannual orbit distance,  
  - $\mathcal{P} = \sqrt[3]{M+m}$ (including planemo mass).  
  - $\mathcal{P} = \sqrt[3]{M}$ (ignoring planemo mass).  

**Key Terms & Symbols:**  
- **Perannual Orbit (𝒫):** distance where orbital period = 1 Earth sidereal year.  
- **Sidereal Year:** 365.256363 ephemeris days; fixed-star frame reference.  
- **Intranucleal / Extranucleal:** perannual orbit lies inside or outside the nucleal orbit.  
- **Symbols:**  
  - $P$ = orbital period (in sidereal years).  
  - $a$ = semi-major axis (AU).  
  - $M$ = stellar mass (⊙).  
  - $m$ = planemo mass (⊙).  
  - 𝒫 = perannual orbital distance.  
  - 𝒩 = nucleal orbit.  

**Cross-Check Notes:**  
- **New glossary entries needed:** Perannual Orbit (𝒫), Intranucleal, Extranucleal.  
- Reinforces dual anchor system in WCB: 𝒩 (thermal/irradiance-based) vs. 𝒫 (temporal/mass-based).  
- Links forward to *M002 — Stars 06: Relating the Nucleal and Perannual Orbits*.  
---

## The Perannual Orbit
There is one remaining essential star system orbit, which I have called the **perannual** orbit.  The word comes from the Latin *per annum*, meaning "per year" or "each year", and the name reflects that this is the orbit in any star system which has an orbital period (*P*) of exactly one Earth year.
##### IMPORTANT
> "One Earth Year" in this case is the duration of Earth's complete orbit around the Sun relative to the larger reference frame of the "fixed" stars; thus this is called the **sidereal year**, from the Latin *sidus*, "star".  This is measured and denoted in terms of **ephemeris days** — which are *defined* to be exactly 86400 _seconds_ in duration. Thus, the sidereal year (and, consequently, the perannual year) has a duration of:
$$\
\begin{gather}
365.256363004 \quad \text{Ephemeris Days} \\
or \\
365^d\;6^h\;9^m\; 9.763545^s
\end{gather}
$$
> This is _not_ a "year" as experienced by inhabitants on the surface of a planemo on this orbit (that is called the **tropical year**, which is in part dependent upon the _rotational period_ of the planemo, itself); this is the **sidereal year**.
> 
> Please see [[Units and Measures of Time ✓]] for a more in-depth discussion of this topic.

We denote the perannual year as $\mathcal{P}$, and its location in the star system _is not constant_ (the same as the *nucleal orbit* ($\mathcal{N}$) but is _determined_ by the mass of the star(s), and – to a small but measurable degree – by the mass of the planemo.

Please see [[M002 - Stars — 06 Relating the Nucleal and Perannual Orbits ✓]] for an in-depth exploration of this relationship.

The perannual orbit is determined not by the luminosity of the star(s) in the system but by **mass**, mostly of the stars(s), but the mass of the planemo can become a calculatory relevant factor if it is a significant fraction of the mass of the star(s).

The perannual orbit is an *orbital distance*, but it is predicated on the **period** of that orbit — how long it takes the planemo to complete one entire orbit (measured in Earth years).  **ANY** planemo orbital period is calculated (in relative terms) by:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M+m}} \\
	a &= \sqrt[3]{P^2 (M+m)} \\
	M + m &= \dfrac{a^3}{P^2} \qquad \text{Believe it or not, this has its uses}
\end{align}
$$
Where:
- *P* = the planemo's orbital period in Earth sidereal years
- *a* = the measure of the semi-major axis of the planemo's orbit
- *M* = the mass of the star(s) in Solar masses
- *m* = the mass of the planemo (also expressed in _Solar_) masses

In many cases (such as that of Earth), *m* is such a small number that it can be ignored without drastically altering the value of *P*.  In the case of Earth:

- $M = 1⊙$
- $m = 0.000003003$⊙ ($3.003 \times 10^{-6}$) — three *millionths* of the Sun's mass
- $a = 1\;AU$

Calculating with **only** the Sun's mass:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M}} = \sqrt{\dfrac{1^3}{1}} = \sqrt{\dfrac{1}{1}} = \sqrt{1} = 1\;\text{years}		
\end{align}
$$
Calculating with **both** masses:
$$
\begin{align}
	P &= \sqrt{\dfrac{a^3}{M + m}} \\
	 &= \sqrt{\dfrac{1^3}{1 + 0.000003003}} \\
	 &= \sqrt{\dfrac{1}{1.000003003}} \\
	 &= \sqrt{0.999997} \\
	 P &= 0.9999985\;\text{years}		
\end{align}
$$
… a difference of about 47.384 _seconds_.

> 🔍 **Takeaways**:
> >The *perannual orbit* defines the location in any star system where a planemo would complete one sidereal Earth year.
> >It may be closer-in than the nucleal orbit (**intranucleal**) or farther out than the nucleal orbit (**extranucleal**).
> >If it is ever _the same as the nucleal orbit_, then the star(s)' mass(es) must be $M = 1⊙$, and — ideally — the planemo's mass must be $m = 1⨁$.
> >Unlike the *nucleal orbit* (which depends on *stellar irradiance*), the perannual orbit *depends only the mass of the system* — and serves as a *temporal* rather than *thermal* reference point.

As shown above, the *distance* of any orbit can be calculated from the period and the masses via:
$$
a = \sqrt[3]{P^2 (M+m)}
$$
… but if we already know that $P = 1$, it drops out of the equation:
$$
a = \sqrt[3]{M+m}
$$
… such that the distance of the orbit is simply the cube-root of the sum of the masses.

For clarity, we denote the _distance_ of the perannual orbit with a $\mathcal{P}$ (for _perannual_), so our equation becomes:
$$
\begin{align}
\mathcal{P} &= \sqrt[3]{M+m} &&\text{When taking into account both masses} \\
\mathcal{P} &= \sqrt[3]{M} &&\text{When using only the central mass} \\
\end{align}
$$

## Abstract  
**Major Topics:**  
- Relationship between the **Nucleal Orbit (𝒩)** and the **Perannual Orbit (𝒫)**.  
- Both are **orbital environs**, not strict limiting distances — they describe contextual properties of a star system.  
- Restatement of definitions:  
  - 𝒩 = $\sqrt{L}$ (AU), where *L* = stellar luminosity (⊙).  
  - 𝒫 = $\sqrt[3]{M+m}$ (AU), or $\sqrt[3]{M}$ if planemo mass *m* is disregarded.  
- Mass–luminosity link: $M = \sqrt[3]{L}$ → allows cross-approximation between 𝒩 and 𝒫.  
- Approximation formulas:  
  - $\mathcal{P} \approx \sqrt[6]{L}$ (perannual from luminosity).  
  - $\mathcal{N} \approx \sqrt{M^3}$ (nucleal from mass).  
  - Cross-relations:  
    - $\mathcal{P} \approx \sqrt[3]{\mathcal{N}}$  
    - $\mathcal{N} \approx \mathcal{P}^3$  
- Caution: these relations are **approximations**; robust calculation of 𝒩 and 𝒫 is recommended for precision:contentReference[oaicite:0]{index=0}.  

**Key Terms & Symbols:**  
- **𝒩 (Nucleal Orbit):** irradiance-based orbital benchmark.  
- **𝒫 (Perannual Orbit):** period-based orbital benchmark.  
- **Approximation relations:** linking 𝒩 and 𝒫 through stellar mass–luminosity scaling.  

**Cross-Check Notes:**  
- No new glossary entries beyond 𝒩 and 𝒫 (already staged in prior files).  
- This section functions as a **bridge note**, unifying the thermal and temporal anchors in WCB orbital design.  
- Emphasizes **approximation vs. precision**: usable shortcuts exist, but exact calculation is preferable.  
---
---



We have explored both [[M002 - Stars — 03 The Nucleal Orbit ✓|The Nucleal Orbit]] and [[M002 - Stars — 05 The Perannual Orbit ✓|The Perannual Orbit]].  These two are not *limiting distances*, but **orbital environs** which both describe and contribute to the ontosomic nature of planemos.

As a quick review:
- **Nucleal Orbit**: that orbit (expressed in AU) at which a planemo receives from its star(s) the same radiant flux as Earth receives from the Sun at one Astronomical Unit distance, calculated by: 
 $$
	\mathcal{N} = \sqrt{L}
$$

Where *L* = Luminosity of the star(s) as expressed in Solar units, ⊙

- **Perannual Orbit**: that orbit (expressed in AU) which has an orbital period of exactly one sidereal Earth year, calculated by:
$$
\mathcal{P} = \sqrt[3]{M+m}
$$
If we disregard the mass of the planemo *m*:
$$
\mathcal{P} = \sqrt[3]{M}
$$
And we saw in [[M002 - Stars — 02 Parameters ✓]] that through relationship:
$$
M = \sqrt[3]{L}
$$
This means that:
- The perannual orbit can be *approximated* directly from the luminosity by:
$$
\mathcal{P} \approx \sqrt[3]{\sqrt[3]{L}} \approx \sqrt[6]{L}
$$
- The nucleal orbit can be *approximated* directly from the mass by:
$$
\mathcal{N} \approx \sqrt{M^3}
$$
And, by extension either can be *approximated* from the other by:
$$
\begin{align}
\mathcal{P} &\approx \sqrt[6]{mathcal{N}^2} \approx \sqrt[3]{\mathcal{N}} \\
\mathcal{N} &\approx \mathcal{P}^3
\end{align}
$$
**REMEMBER**
- Both $\mathcal{N}$ and $\mathcal{P}$ are measured in astronomical units, not time!
- These last four equations are **approximations**; in most cases they'll be "accurate enough", but calculating$\mathcal{N}$ and $\mathcal{P}$ robustly is always advised.

## Abstract  
**Major Topics:**  
- Review of the **Standard Stellar Parameter Equations** linking temperature (T), mass (M), radius (R), lifetime (Q), and luminosity (L).  
- Recognition that while the standard exponents work well for most **Main Sequence** stars, observed stellar data show that slight adjustments produce a closer fit.  
- **Refinements introduced:**  
  - Exponent for $T ↔︎ M$ increased from 1.98 → 2.0.  
  - Addition of direct calculation routes to/from **luminosity (L)**, simplifying downstream math (especially for *Stars 08: Sun-Like Stars*).  
  - For higher precision, recommended exact values:  
    - $7.6 ≈ 7.5778$  
    - $3.8 ≈ 3.7889$:contentReference[oaicite:0]{index=0}.  
- Emphasis: WCB prioritizes **plausible world construction** over strict theoretical purity, so these adjusted exponents serve the design goals better.  

**Key Terms & Symbols:**  
- **Standard Stellar Parameter Equations:** Baseline power-law relations for T, M, R, Q, and L.  
- **Modified Parameters:** Slightly adjusted exponents improving fit across observed data.  
- **Direct Luminosity Relations:** New formulas linking L with other parameters for simplified application.  

**Cross-Check Notes:**  
- No **new glossary entries** introduced; the adjustments are refinements to existing equations.  
- Functions as a **supportive methods note** — improves accuracy and usability of WCB stellar modeling.  
- Directly prepares for *Stars 08: Sun-Like Stars*, where these refined forms are applied.  
---
---


# Stars — 2.07 Fine-tuning Stellar Parameters
## Standard Parameter Equations
The Standard Parameter Equations (see [[M002 - Stars — 02 Parameters ✓]]):

| Temperature<br>(T) |    Mass<br>(M)    | Radius<br>(R) |       Lifetime<br>(Q)       |
| :----------------: | :---------------: | :-----------: | :-------------------------: |
| $T=\sqrt[1.98]{M}$ | $M=\sqrt[0.9]{R}$ |  $R=M^{0.9}$  |        $Q=M^{-2.5}$         |
| $T=\sqrt[1.8]{R}$  |   $M=T^{1.98}$    |  $R=T^{1.8}$  | $Q \approx \sqrt[-0.36]{R}$ |
|    $T=Q^{-0.2}$    |   $M=Q^{-0.4}$    | $R=Q^{-0.36}$ |         $Q=T^{-5}$          |
… _generally_ work well for most **Main Sequence** stars, but a survey of known stars in the Solar neighborhood —

> **Hippy**: "Wha–"

… *which is too complex and extensive to detail here* — suggests that *modest* adjustments to a couple of key exponents yield parameter equations that better reflect observed stellar characteristics. Since worldmaking prioritizes plausible-world construction over strict theoretical purity, these revised values offer better performance across the mass range of interest.
### Modified Parameters Table# Main Sequence Stellar Equations of State

| Temperature<br>(T)  |    Mass<br>(M)    |        Radius<br>(R)        |       Lifetime<br>(Q)       | <center>Luminosity<br>(L)</center><br> |
| :-----------------: | :---------------: | :-------------------------: | :-------------------------: | :------------------------------------: |
|    $T=\sqrt{M}$     | $M=\sqrt[0.9]{R}$ |         $R=M^{0.9}$         |        $Q=M^{-2.5}$         |              $L=M^{3.8}$               |
|  $T=\sqrt[1.8]{R}$  |      $M=T^2$      |         $R=T^{1.8}$         | $Q \approx \sqrt[-0.36]{R}$ |       $L \approx R^{4.\bar{2}}$        |
|    $T=Q^{-0.2}$     |   $M=Q^{-0.4}$    |        $R=Q^{-0.36}$        |         $Q=T^{-5}$          |             $L = T^{7.6}$              |
| $T = \sqrt[7.6]{L}$ | $M=\sqrt[3.8]{L}$ | $R\approx\sqrt[4.\bar2]{L}$ |        $Q=L^{-1.52}$        |          $L=\sqrt[-1.52]{Q}$           |

**Notes**:
- The parameter relationship that changed from the previous table was $T ↔︎ M$, where the exponent increased slightly from $1.98$ to $2.0$
- The **major change** is the addition of direct calculation for the parameters to-and-from luminosity; these are included for the purpose of simplifying much of the math related to [[M002 - Stars — 08 `Sun-Like` Stars ✓]].
- **For *greatest accuracy***:
	- The exponent $7.6$ can be more precisely specified as $7.5778$
	- The exponent $3.8$ can be more precisely specified as $3.7889$

## Abstract  
**Major Topics:**  
- Critique of vague astronomical usage of “Sun-like star” and proposal of a **clearer WCB classification system** grounded in orbital habitability.  
- Definitions nested by **Ontozone boundaries** and **perannual orbits (𝒫):**  
  - **Solar Analogs:** perannual orbits spanning 0.500–4.850 AU (Inner → Outer Parahabitable Zone, H₀–H₅); spectral types F2–K9.  
  - **Solar Cognates:** perannual orbits spanning 0.750–1.770 AU (Inner → Outer Habitable Zone, H₁–H₄); spectral types F7.62–K1.11.  
  - **Solar Twins:** perannual orbits spanning 0.950–1.385 AU (Hospitable Zone, H₂–H₃); spectral types G1.04–G7.73.  
- Hierarchical logic: all Twins ⊂ Cognates ⊂ Analogs:contentReference[oaicite:0]{index=0}.  
- Mathematical framework for deriving stellar parameters:  
  - Cross-relations between luminosity, perannual orbit (𝒫), and thermozone limits (H₀–H₅).  
  - Generalized equation for stellar luminosity given thermozone factor (λ).  
  - Direct temperature relation: $K = 5800(\lambda^{-0.3191})$.  
- Thermal Axis for Perannual Orbits: diagram showing stellar temperature vs. spectral type for H₀–H₅.  
- **Orbital Habitability Index (OHI):** scalar (0.00–1.00) quantifying relative habitability based on distance from the nucleal orbit (𝒩).  
  - Piecewise function distinguishes intranucleal vs. extranucleal cases.  
  - Index peaks at 1.00 for D = 𝒩, declines linearly to 0.00 at H₀ and H₅.  
  - Illustrated via habitability atlas plate.  

**Key Terms & Symbols:**  
- **Solar Analog, Solar Cognate, Solar Twin:** nested categories of Sun-like stars based on ontozone/perannual placement.  
- **𝒫 (Perannual Orbit):** temporal anchor.  
- **𝒩 (Nucleal Orbit):** thermal anchor.  
- **Thermozones (H₀–H₅):** reference corridors.  
- **λ (Scaling Factor):** ratio linking perannual orbit to nucleal orbit.  
- **OHI (Orbital Habitability Index):** 0.00–1.00 habitability scalar.  

**Cross-Check Notes:**  
- **New glossary entries needed:** Solar Analog, Solar Cognate, Solar Twin, Orbital Habitability Index (OHI).  
- All other symbols and terms already staged in prior files (𝒩, 𝒫, thermozones, H₀–H₅, λ).  
- This section bridges stellar classification with **habitability indices**, anchoring “Sun-like” terminology directly to WCB orbital framework.  
---
---


# Solar Analogs, Cognates, and Twins

The published literature often speaks of "solar analog" stars, but tends to be distressingly vague about exactly what the term means.  Generally speaking, it means "a star very much like the Sun".

> **Keppy**: And that doesn't help at all — that could mean _any_ star, really.

You're right; so, for our purposes we have our own definitions, based on *orbits* and the ontozones.  But, first, a survey of existing terminology.
## Existing Definitions
A "Sun-like star" is a broad term used to describe stars that share characteristics with our own Sun. Astronomers often categorize them into a hierarchy based on their *physical* similarity to the Sun.  They all need to be main-sequence stars**, actively fusing hydrogen into helium in their core, like our Sun. Otherwise:

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
For thesiastic purposes, our classifications relate directly to the _habitability potential of orbiting planemos_, rather than just their parent stars’ physical resemblance to the Sun.

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
> - This perannual-orbit-based requirement is largely arbitrary, predicated on the thesiastic idea that a planemo that is least different from Earth would have an orbital period the same as Earth's.
##### Nested Ontozonal Categories of Sun-like Stars

![[Solar Types Diagram|300]]
### Calculating The Spectral Types
Previously, in [[M002 - Stars — 06 Relating the Nucleal and Perannual Orbits ✓]], we established that the _distance_ of the perannual orbit can be approximated by:
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
In  [[M002 - Stars — 04 Thermozone Orbits ✓]], we established that the thermozone limits are calculated by applying fixed scaling factors to the **nucleal orbit distance** ($\mathcal{N}$), which is calculated from the square-root of the luminosity:

| Limiting<br>Orbit |   Calculation   |
| :---------------: | :-------------: |
|       $H_0$       | $0.500\sqrt{L}$ |
|       $H_1$       | $0.750\sqrt{L}$ |
|       $H_2$       | $0.950\sqrt{L}$ |
|       $H_3$       | $1.385\sqrt{L}$ |
|       $H_4$       | $1.770\sqrt{L}$ |
|       $H_5$       | $4.850\sqrt{L}$ |
This means that we can set:
$$
\mathcal{P} = \sqrt[11.4]{L} \quad \text{equal to} \quad \mathcal{P} = 0.500\sqrt{L}
$$
… and solve for L:
$$
\begin{align}
\sqrt[11.4]{L} &= 0.500\sqrt{L} \\
0.500 &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} -{\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
0.500 &= L^{-0.4123} \\
L &= \sqrt[-0.4123]{0.500} \\
&= 5.372\; ✓
\end{align}
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
\begin{align}
\mathcal{S} &= \dfrac{\kappa - K}{þ}
\end{align}
$$
Where:
- K = the star's surface temperature in Kelvin
- κ = the _upper bound_ temperature of the relevant spectral class
- þ = the thermal interval constant for the relevant spectral class
- $\mathcal{S}$ = the spectral *type* number

Taken from the table:

| Spectral<br>Class | <center>High<br>Temp.<br>(K)</center> | <center>Thermal<br>Interval<br>Constant<br>(þ)</center> |
| :---------------: | ------------------------------------: | ------------------------------------------------------: |
|         O         |                                 55000 |                                                    3000 |
|         B         |                                 25000 |                                                    1500 |
|         A         |                                 10000 |                                                     250 |
|         F         |                                  7500 |                                                     150 |
|         G         |                                  6000 |                                                     100 |
|         K         |                                  5000 |                                                     150 |
|         M         |                                  3500 |                                                     110 |
|         L         |                                  2400 |                                                     110 |
|         T         |                                  1300 |                                                      70 |
|         Y         |                                   600 |                                                      30 |
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
\begin{align}
\sqrt[11.4]{L} &= 4.850\sqrt{L} \\
4.850 &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} -{\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
4.850 &= L^{-0.4123} \\
L &= \sqrt[-0.4123]{4.850} \\
&= 0.022\; ✓
\end{align}
$$
Converting luminosity to temperature:
$$
T = \sqrt[7.6]{L} = \sqrt[7.6]{0.022} = 0.605\;\odot
$$
In [[M002 - Stars — 02 Parameters ✓]], we established the following relationship between solar-unit temperature (*T*) and Kelvin temperature (*K*)
$$
K = 5800T
$$
So, our star has a Kelvin temperature of:
$$
K = 5800T = 5800(0.605) = 3503.85\;K
$$
… which is a K-Class star with a $\kappa = 5000 \text{  and  } þ = 150$, from which we can calculate the spectral type by:
$$
\mathcal{S} = \dfrac{\kappa - K}{þ} = \dfrac{5000 - 3503.85}{150} = \dfrac{1496.185}{150} = 9.975
$$
So the spectral type of a star with a perannual orbit at $4.850$ AU is K9.975 ✓.

This means that the range of spectral types which host _perannual orbits within the **parahabitable** zone_ is F1.76 – K9.932, which we can round for convenience to F2 – K9.

**Why K9 and not M0**
The exact math yields **F1.76 – K9.97**. For presentation, we **round inward** at both ends of the range to **F2 – K9** so that all perannual orbits calculated for stars within this range lies **strictly** inside the parahabitable band, avoiding knife‑edge cases at the hot and cold limits. (This convention absorbs small uncertainties in stellar parameters and subclass mapping.)

## Generalizing The Equation
This logic can be extended for any Hₓ value:
By generalizing the scaling factor **λ**, we can calculate the relative stellar luminosity for **any** perannual orbit distance:
$$
\begin{align}
\sqrt[11.4]{L} &= \lambda\sqrt{L} \\
\lambda &= \dfrac{\sqrt[11.4]{L}}{\sqrt{L}} \\
&= L^{\frac{1}{11.4} - {\frac{1}{2}}} \\
&= L^{\frac{2}{22.8}-\frac{11.4}{22.8}} = L^{-\frac{9.4}{22.8}} \\
\lambda &= L^{-0.4123} \\
\therefore L &= \sqrt[-0.4123]{\lambda} \; ✓
\end{align}
$$
# A Final Determination
Substituting all of the $H_x$ values in for λ:

| Limiting<br>Orbit | Scaling<br>Factor<br>(λ) |         Calculation         | <center>Luminosity<br>(L)</center><br> | Spectral<br>Type | <center>Ontozone</center> |
| :---------------: | :----------------------: | :-------------------------: | -------------------------------------: | :--------------: | ------------------------- |
|       $H_0$       |          0.500           | $L = \sqrt[-0.4123]{0.500}$ |                                  5.372 |      F1.760      | Parahabitable             |
|       $H_1$       |          0.750           | $L = \sqrt[-0.4123]{0.750}$ |                                  2.009 |      F7.615      | Habitable                 |
|       $H_2$       |          0.950           | $L = \sqrt[-0.4123]{0.950}$ |                                  1.132 |      G1.043      | Hospitable                |
|       $H_3$       |          1.385           | $L = \sqrt[-0.4123]{1.385}$ |                                  0.454 |      G7.726      | Hospitable                |
|       $H_4$       |          1.770           | $L = \sqrt[-0.4123]{1.770}$ |                                  0.250 |      K1.108      | Habitable                 |
|       $H_5$       |          4.850           | $L = \sqrt[-0.4123]{4.850}$ |                                  0.022 |      K9.972      | Parahabitable             |
> **Keppy**: Seems like a lot of calculating and converting...

Well, without going into the gory details, you can calculate the relative or Kelvin temperature directly by:
$$\begin{gather}
K =5800(\lambda^{-0.3191}) \\[1em]
T = \lambda^{-0.3191}
\end{gather}
$$
… which will allow you to calculate the spectral type for any perannual orbit at any orbital distance, and the reverse calculations are:
$$
\begin{gather}
\lambda = \sqrt[-0.3191]{\dfrac{K}{5800}} \\[1em]
\lambda = \sqrt[-0.3191]{T}
\end{gather}
$$      
… which will give you the orbital distance of the perannual orbit for a star of any given Kelvin temperature (*K*) or relative temperature (*T*), since $T=\frac{K}{5800}$.
#### Thermal Axis for Perannual Orbits
This diagram shows the stellar surface temperatures (*K*) and corresponding spectral types required for a star’s _perannual orbit_ to fall on each thermozone boundary $H_0$​ through $H_5$​. The core equation relates perannual distance scaling factor λ to stellar temperature *K*.

![[Ontozones and Spectral Types|650]]

### Orbital Habitability Index (OHI)
The Orbital Habitability Index (OHI) is a measure of how likely a planemo is to be habitable based on its orbit, with the nucleal orbit assumed to be 100% habitable and orbits closer-in and farther-out becoming progressively less habitable.  It is calculated using one of two equations, depending on whether the orbit in question is *intranucleal* or *extranucleal*:

The OHI provides a scalar measure (0.00–1.00) of the _relative biological viability_ of a planemo orbit based on its distance from the nucleal orbit $\mathcal{N} = \sqrt{L}$​. It assumes a peak habitability of 1.00 (100%) at 1.000N, declining linearly in each direction.

$$
H_I =
\begin{cases}
  \quad 2\dfrac{D}{\mathcal{N}} - 1 & \text{if } {D} \leq {\mathcal{N}} \quad \text{(intranucleal)} \\[1em]
  -0.26\dfrac{D}{\mathcal{N}} + 1.26 & \text{if } {D} \gt {\mathcal{N}} \quad \text{(extranucleal)}
\end{cases}
$$

$$
\text{Where } R = \dfrac{D}{\mathcal{N}}: \quad H_I =
\begin{cases}
  \quad 2R - 1 & \text{if } R \leq 1 \quad \text{(intranucleal)} \\
  -0.26R + 1.26 & \text{if } R \gt 1 \quad \text{(extranucleal)}
\end{cases}
$$

Where:
- $H_I$ = the numeric value of the orbit's habitability index
- *D* = the orbit's distance in AU
- $\mathcal{N}$ = the nucleal orbit's distance in AU

Values of *D* < 0.500$\mathcal{N}$ and > 4.850$\mathcal{N}$ return *negative numbers* for $H_I$, indicating that the orbit is not hospitable, habitable, or parahabitable for Earth-type lifeforms.


![[Orbital Habitability Index Graph.png|400]]

| Orbit<br>Type | Orbit<br>Distance  | Habitability<br>Index |
| :-----------: | :----------------: | :-------------------: |
| Intranucleal  | 0.500$\mathcal{N}$ |         0.00          |
| Intranucleal  | 0.750$\mathcal{N}$ |         0.50          |
| Intranucleal  | 0.950$\mathcal{N}$ |         0.90          |
|    Nucleal    | 1.000$\mathcal{N}$ |         1.00          |
| Extranucleal  | 1.385$\mathcal{N}$ |         0.90          |
| Extranucleal  | 1.770$\mathcal{N}$ |         0.80          |
| Extranucleal  | 4.850$\mathcal{N}$ |         0.00          |
#### Habitability Axis Plate

![[Habitability Atlas Plate.png]]

## Abstract  
**Major Topics:**  
- Extension from nucleal (𝒩) and perannual (𝒫) orbits to **full orbital system design**.  
- Empirical analysis of the Solar System: orbital distances, eccentricities, ontozone placement, gaps, and intervals.  
- Definition of **orbital intervals** (ratio of successive orbital distances):  
  - Solar System ranges: 1.38–2.00 AU, μ ≈ 1.74 AU, σ ≈ 0.205.  
  - WCB **conservative range:** ⟨1.400 ∧ 2.000⟩ AU.  
  - WCB **medial range:** ⟨1.200 ∧ 3.500⟩ AU.  
  - WCB **optimistic range:** ⟨1.000 ∧ 5.000⟩ AU.  
- Introduction of **intrabasal** and **extrabasal orbit generation processes**:  
  - **Intrabasal:** generate inward orbits from a base radius (divide by randomized interval).  
  - **Extrabasal:** generate outward orbits from a base radius (multiply by randomized interval).  
- Application strategies:  
  - Start at nucleal/perannual orbit → expand inward/outward.  
  - Start at innermost or outermost safe orbit → generate outward/inward.  
  - Always check results against 𝒩 or 𝒫 to maintain coherent interval spacing.  
- Worked example:  
  - Starting from 𝒩 = 0.834 AU.  
  - Generated inward to 0.101 AU, outward to 33.357 AU.  
  - Produced 11 candidate orbital positions spanning inner rocky to distant icy regions.  

**Key Terms & Symbols:**  
- **Orbital Interval (I):** ratio of successive orbital distances, $I = O_n / O_{n-1}$.  
- **Orbital Gap (G):** difference of successive orbital distances, $G = O_n - O_{n-1}$.  
- **Intrabasal Orbit Calculation:** inward generation by division.  
- **Extrabasal Orbit Calculation:** outward generation by multiplication.  
- **Basal Orbit (B):** chosen anchor orbit (e.g., 𝒩 or 𝒫).  
- **Ω (Omega):** cutoff distance (innermost safe orbit or outer system limit).  

**Cross-Check Notes:**  
- **New glossary entries needed:** Orbital Interval, Orbital Gap, Intrabasal Orbit Calculation, Extrabasal Orbit Calculation, Basal Orbit, Ω (system cutoff).  
- Builds on previous anchors (𝒩, 𝒫, thermozones) to enable **statistically grounded system generation**.  
- Provides WCB’s baseline method for populating star systems with planemo orbits.  
---
---


# Fleshing Out A Star System

We've established spectral classes and types, thermozones, ontozones, habitability indices, and the two critical orbital distances, *nucleal* ($\mathcal{N}$) and *perannual* ($\mathcal{P}$).

But planemos don't orbit only at these discreet distances  – they're all over the place.  Here's a breakdown of our own Solar system's planemo orbit data:

| <center>planemo</center> | <center>α<br>(AU)</center> | <center>ϵ</center> | Ontozone    |
| ----------------------- | -------------------------: | ------------------ | ----------- |
| Mercury                 |                      0.387 | 0.2056             | Igniozone   |
| Venus                   |                      0.723 | 0.0068             | Calorozone  |
| Earth                   |                      1.000 | 0.0167             | Solarazone  |
| Mars                    |                      1.524 | 0.0934             | Hiberozone  |
| *Asteroids*             |     *⟨2.2 ∧ 3.2⟩; μ = 2.7* | *μ = 0.15*         | *Brumazone* |
| Jupiter                 |                      5.204 | 0.0489             | Cryozone    |
| Saturn                  |                      9.583 | 0.0565             | Cryozone    |
| Uranus                  |                     19.191 | 0.0472             | Cryozone    |
| Neptune                 |                     30.070 | 0.0087             | Cryozone    |
## Orbital Parameters
Ignoring the asteroid belt for the moment and inserting Ceres as the largest member of the belt:

| <center>planemo</center> | <center>α<br>(AU)</center> | <center>ϵ</center> | <center>Gap¹<br>(AU)</center> | <center>Interval²<br>(AU)</center> |
| ----------------------- | -------------------------: | -----------------: | ----------------------------: | ---------------------------------: |
| Mercury                 |                      0.387 |             0.2056 |                               |                                    |
| Venus                   |                      0.723 |             0.0067 |                        0.3362 |                             1.8686 |
| Earth                   |                      1.000 |             0.0167 |                        0.2767 |                             1.3825 |
| Mars                    |                      1.524 |             0.0934 |                        0.5237 |                             1.5237 |
| Ceres                   |                      2.700 |             0.1500 |                        0.1763 |                             1.7720 |
| Jupiter                 |                      5.204 |             0.0489 |                        2.5038 |                             1.9273 |
| Saturn                  |                      9.583 |             0.0565 |                        4.3788 |                             1.8415 |
| Uranus                  |                     19.191 |            0.04727 |                        9.6087 |                             2.0027 |
| Neptune                 |                     30.070 |             0.0088 |                       10.8787 |                             1.5669 |
>Notes:
>1. The orbital **gap** is calculated by subtracting the planemo's orbital distance from the next closer-in planemo's orbital distance
>   $$G = O_n - O_{n-1}$$>2. The orbital **interval** is calculated by dividing the planemo's orbital distance by the next closer-in planemo's orbital distance:
>   $$I = \dfrac{O_n}{O_{n-1}}$$

What we are concerned with is the *orbital intervals*
- The minimum interval is between Venus and Earth: $I = 1.3825\;AU$
- The maximum interval is between Uranus and Neptune: $I = 2.0027\;AU$
- The average interval is $I \approx 1.74\;AU$
- The median interval is $I \approx 1.81\;AU$
- The standard deviation is $\sigma = 0.2051$

This supports defining a **WCB-conservative orbital interval range** of  ⟨1.400  ∧  2.000⟩  AU by rounding up the minimum and rounding down the maximum.

However, a cursory survey of the Exoplanet Catalog seems to reveal a range of ⟨1.000 ∧ 5.000⟩ AU for planetary orbital intervals.  We'll define this as our optimistic orbital interval range, and, for completeness, average the two ranges at ⟨1.200 ∧ 3.500⟩ AU.

**Orbital interval ranges**

| Inner | Outer | Description  |
| ----: | ----: | ------------ |
|   1.4 |     2 | Conservative |
|   1.2 |   3.5 | Medial       |
|     1 |     5 | Optimistic   |
## Calculating Other Orbits
This brings us to methods of calculating other orbits in a star system.  In practice, any method the worldmakerchooses is _valid_, including just putting planemos where "it feels right"; however, even using this method _should_ ideally take into account the above statistics and try to avoid an orbital interval between a given planemo and its nearest neighbor of $< 1.500\;AU$ or $> 2.000\;AU$.

### Starting From A Known Orbit
Most of the time, you'll have pre-established a particular orbit  — usually either the *nucleal* or the *perannual* orbit, and want to arrange other planemos in the system relative to that orbit. Notating this orbit as the **base** orbit, we can set up two processes for calculating orbits inferior to (closer-in than) and superior to (farther-out than) that orbit.

**Intrabasal Orbit Calculation Process**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i-1} = \frac{r_i}{⟨⟨ \text{min} ∧ \text{max} ⟩⟩}
\quad \text{while } r_{i-1} \geq \Omega
$$
**Extrabasal Orbit Calculation Process**
$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i+1} = r_i \cdot ⟨⟨ \text{min} ∧ \text{max} ⟩⟩
\quad \text{while } r_{i+1} \leq \Omega
$$
Where:
- *B* = basal orbital radius (e.g. the nucleal orbit $\mathcal{N}$)
- *Ω* = orbital distance cuttoff (minimum or maximum allowed orbit based on the star system constraints)

### Usage Strategy
*Assuming the medial orbital interval range* $I \in ⟨⟨1.200 ∧ 3.500⟩⟩\;AU$:
The **intrabasal** and **extrabasal** forms can be used independently depending on your desired anchoring strategy:

> **Inward-Only Generation**  
  If you begin at the **basal orbit** (innermost, nucleal, perannual, etc.), use the **intrabasal** form to expand inward via divisive steps:
$$
  r_0 = B;\; \Omega = «▢»:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨1.200 ∧ 3.500⟩⟩}, \text{ while } r_{i-1} \geq \Omega
$$
Where:
- *Ω* = the minimum safe orbital distance  —  usually taken to be $a = 0.100\;AU$.

> **Outward-Only Generation**  
  If you begin at an **innermost orbit** (e.g. a thermal, Roche, or design constraint), use the **intrabasal** form to expand outward via multiplicative steps:
$$
  r_0 = B;\; \Omega = «▢»:
  \quad r_{i+1} = r_i \cdot ⟨⟨1.200 ∧ 3.500⟩⟩, \text{ while } r_{i+1} \leq \Omega
$$
Where:
- *Ω* = the farthest orbit desired for a planemo in the system — based on whatever criterion desired, but physically limited to the Hill Sphere radius of the central mass.

> Applying these methods can fully define a system.
> - If one wanted to start with the innermost safe orbit; e.g. $B = 0.100\;AU$, then one would use only the extrabasal process to calculate orbits outward.
> - Conversely if one wanted to start with the most distant orbit, then one would use only the intrabasal process to calculate orbits inward.

>> **IMPORTANT**
>> *If not starting from the perannual or nucleal orbit, always check randomized orbits against either (or both) to ensure proper interval gaps fall to either side of that orbit, and adjust accordingly!*

## Worked Example
Let us say we've identified our nucleal orbit ($\mathcal{N}$) as $\mathcal{N} = 0.834\;AU$, and we want to calculate orbits interior-to and exterior-to that orbit, and we've chosen $a = 0.100\;AU$ as our innermost safe orbit.
### Working Inward
$$
  r_0 = 0.834;\; \Omega = 0.100:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨1.200 ∧ 3.500⟩⟩}, \text{ while } r_{i-1} \geq 0.100
$$
$$
\begin{align}
r_{i-1} &= \dfrac{0.834} {1.723} = 0.482\;AU \qquad 1.732 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.482} {1.616} = 0.298\;AU \qquad 1.616 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.298} {1.573} = 0.190\;AU \qquad 1.573 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.190} {1.884} = 0.101\;AU \qquad 1.884 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i-1} &= \dfrac{0.101} {1.963} = 0.051\;AU \qquad 1.963 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU}\;✘ \\[1em]
\end{align}
$$
We stop at the fourth randomized orbit, because the next orbit randomly generated fails the $r ≥ 0.100\;AU$ test.
We now have a system of five orbits:

|  Orbit  | Distance |
| :-----: | :------: |
|    1    | 0.101    |
|    2    | 0.190    |
|    3    | 0.298    |
|    4    | 0.482    |
| 5 (*N*) | 0.834    |
We could stop here and have a fully legitimate star system, but let's say we want extranucleal orbits, as well.  Again, beginning with the nucleal orbit $B = 0.834\;AU$, and setting an outermost orbit of $\Omega = 35.0\;AU$:
$$
  r_0 = 0.834;\; \Omega = 35.0:
  \quad r_{i+1} = r_i \cdot ⟨⟨1.200 ∧ 3.500⟩⟩, \text{ while } r_{i+1} \leq 35.0
$$
$$
\begin{align}
r_{i+1} &= 0.834(1.829) = 1.525\;AU \qquad 1.829 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 1.525(1.969) = 3.003\;AU \qquad 1.969 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 3.003(1.578) = 4.739\;AU \qquad 1.578 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 4.739(1.547) = 7.332\;AU \qquad 1.547 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 7.332(1.552) = 11.379\;AU \qquad 1.552 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 11.379(1.608) = 18.298\;AU \qquad 1.608 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 18.298(1.823) = 33.357\;AU \qquad 1.823 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \\[1em]
r_{i+1} &= 33.357(1.778) = 59.309\;AU \qquad 1.778 := \text{Randomized interval between ⟨⟨1.200 ∧ 3.500⟩⟩ AU} \; ✘ \\[1em]
\end{align}
$$
We stop at the seventh iteration, as the next value exceeds $\Omega = 35.0\;AU$.

This expands our system to 11 orbits:

|  Orbit  | Distance |
| :-----: | :------: |
|    1    |  0.101   |
|    2    |  0.190   |
|    3    |  0.298   |
|    4    |  0.482   |
| 5 (*N*) |  0.834   |
|    6    |  1.525   |
|    7    |  3.003   |
|    8    |  4.739   |
|    9    |  11.379  |
|   10    |  18.298  |
|   11    |  33.357  |
… and we can proceed to design planemos for each orbit, or eliminate some orbits and install asteroid belts, or adjust orbital intervals to suit our needs.... the sky's the limit.

> **Hippy**: Oh, ha-ha...

C'mon, you had to know I'd use that pun at _some point_ didn't you?

With this method, a worldmaker can quickly generate a full planemo system that is physically plausible, statistically grounded, and symbolically consistent with WCB cosmology.

[[Asteroid Belts and Resonance Gaps — working out]]

## Abstract  
**Major Topics:**  
- Demonstrates integration of **thermozones (H₀–H₅)**, **ontozones**, and **orbital generation rules** into a coherent stellar system design.  
- Stepwise calculation:  
  - Thermozone limits derived from the nucleal orbit ($𝒩 = 0.834$ AU).  
  - Placement of generated orbits into both thermozone and ontozone categories.  
- Worked example tables:  
  - Case with both nucleal (𝒩) and perannual (𝒫) orbits → reveals interval violation ($I = 1.162$ < minimum 1.5).  
  - Case with **perannual planemo only** → valid intervals maintained (1.574–1.927 AU).  
- Demonstrates **design trade-offs**: some orbital anchors (𝒩 vs. 𝒫) may be mutually exclusive depending on stellar mass/luminosity.  
- Stellar parameter recalculation (luminosity, temperature, spectral type, subclass index) validates the system’s spectral class (G4.701).  
- Orbital habitability evaluation:  
  - Perannual orbit receives ~74.1% of nucleal flux.  
  - Corresponding Orbital Habitability Index (OHI) = 0.958 (95.8% of nucleal).  
- Emphasis: WCB design enforces **minimum orbital spacing (I ≥ 1.5)** as a hard rule, while maximum spacing (I ≤ 2.0) is treated as flexible.  

**Key Terms & Symbols:**  
- **Δ (Delta):** factor expressing relative distance offset between perannual and nucleal orbits.  
- **F (Flux):** relative stellar irradiance at a given orbital distance, normalized to 1.0 at 𝒩.  
- **OHI (Orbital Habitability Index):** previously defined, applied here in practice.  

**Cross-Check Notes:**  
- **New glossary entries needed:** Δ (distance ratio), F (stellar flux).  
- Reinforces prior entries: thermozones, ontozones, 𝒩, 𝒫, orbital intervals.  
- Serves as a practical example of reconciling WCB rules with real stellar constraints.  
---
---


# Calculating the Thermozones
Since we know our nucleal orbit is $\mathcal{N} = 0.834\;AU$, we can calculate the thermozone limits:
$$
\begin{align}
H_0 = 0.500\mathcal{N} &= 0.500(0.834) = 0.417\;AU \\
H_1 = 0.750\mathcal{N} &= 0.750(0.834) = 0.626\;AU \\
H_2 = 0.950\mathcal{N} &= 0.950(0.834) = 0.792\;AU \\
H_3 = 1.385\mathcal{N} &= 1.385(0.834) = 1.115\;AU \\
H_4 = 1.770\mathcal{N} &= 1.770(0.834) = 1.476\;AU \\
H_5 = 4.850\mathcal{N} &= 4.850(0.834) = 4.045\;AU \quad \text{Frost Line} \\
\end{align}
$$
And we can add these to our orbits table from above and determine the thermozones and ontozones of the orbits:

|       Orbit        | Distance | <center>Thermozone</center> | <center>Ontozone</center> |
| :----------------: | :------: | --------------------------- | ------------------------- |
|         1          |  0.101   | Igniozone                   | Xenotic                   |
|         2          |  0.190   | Igniozone                   | Xenotic                   |
|         3          |  0.298   | Ignoizone                   | Xenotic                   |
|       $H_0$        |  0.417   |                             |                           |
|         4          |  0.482   | Calorozone                  | Inner Parahabitable       |
|       $H_1$        |  0.626   |                             |                           |
|       $H_2$        |  0.792   |                             |                           |
| 5 (*$\mathcal{N}$) |  0.834   | Solarazone                  | Hospitable                |
|       $H_3$        |  1.115   |                             |                           |
|       $H_4$        |  1.476   |                             |                           |
|         6          |  1.525   | Brumazone                   | Outer Parahabitable       |
|         7          |  3.003   | Brumazone                   | Outer Parahabitable       |
|       $H_5$        |  4.045   |                             |                           |
|         8          |  4.739   | Cryozone                    | Xenotic                   |
|         9          |  11.379  | Cryozone                    | Xenotic                   |
|         10         |  18.298  | Cryozone                    | Xenotic                   |
|         11         |  33.357  | Cryozone                    | Xenotic                   |
And, we can calculate the perannual orbital distance and the star's spectral type by:
**Perannual Orbit**
$$
\begin{align}
L &= \mathcal{N}^2 = 0.834^2 = 0.696 \\
M &= \sqrt[3.8]{L} = \sqrt[3.8]{0.696} = 0.909 \\
A &= \sqrt[3]{0.909} = 0.969\;AU\;✓
\end{align}
$$
The perannual orbit in this system is at $A = 0.969\;AU$.

**Spectral Type**
$$
\begin{align}
L &= 0.696 \\
T &= \sqrt[7.6]{L} = \sqrt[7.6]{0.696} = 0.953\odot \\
K &= 5800T = 5800(0.953) = 5529.92 \quad \text{Spectral Class G: κ = 6000; þ = 100} \\[2em]
\mathcal{S} &= \dfrac{\kappa - K}{100} = \dfrac{6000 - 5529.92}{100} = \dfrac{470.08}{100} = 4.701\\
\end{align}
$$
The spectral type of our star is $G4.701$.

> **Hippy**: Uh..... that perannual orbit distance....

Excellent catch!

> **Keppy**: What....?

Check this out: we already know that our nucleal orbit is at $\mathcal{N} = 0.834\;AU$.  *If* we put planemo on the perannual orbit at $A = 0.969\;AU$ the interval between the nucleal orbit and the perannual orbit is only:
$$
I = \dfrac{0.969}{0.834} = 1.162\;AU\;✓
$$
… which is less than our specified minimum $I > 1.500\;AU$.

> **Keppy**: Which means....

> **Hippy**: Either we don't have a planemo on the nucleal orbit, *or* we don't have a planemo on the perannual orbit; those orbits are fixed by the stellar parameters  – neither can be shifte.

EXACTLY!  This is the power  — but also the limitation — of our system.  Some things we can tweak as we please; other things we have to work with, or work around.

In this case, we're forced to choose between a planemo with Earth's stellar flux, or a planemo with Earth's orbital period, but we can't have both.

> **Keppy**: What if we drop the nucleal planemo and go with the parahabitable planemo?

Excellent thought... let's work that through.  Here's a modified orbit table taking that into account:

|       Orbit       | Distance | <center>Thermozone</center> | <center>Ontozone</center> | Interval |
| :---------------: | :------: | --------------------------- | ------------------------- | -------- |
|         1         |  0.101   | Igniozone                   | Xenotic                   |          |
|         2         |  0.190   | Igniozone                   | Xenotic                   | 1.884    |
|         3         |  0.298   | Ignoizone                   | Xenotic                   | 1.573    |
|       $H_0$       |  0.417   |                             |                           |          |
|         4         |  0.482   | Calorozone                  | Inner Parahabitable       | 1.616    |
|       $H_1$       |  0.626   |                             |                           |          |
|       $H_2$       |  0.792   |                             |                           |          |
| 5 ($\mathcal{A}$) |  0.969   | Solarazone                  | Hospitable                | »1.927«  |
|       $H_3$       |  1.115   |                             |                           |          |
|       $H_4$       |  1.476   |                             |                           |          |
|         6         |  1.525   | Brumazone                   | Outer Parahabitable       | »1.574«  |
|         7         |  3.003   | Brumazone                   | Outer Parahabitable       |          |
|       $H_5$       |  4.045   |                             |                           |          |
|         8         |  4.739   | Cryozone                    | Xenotic                   | 1.552    |
|         9         |  11.379  | Cryozone                    | Xenotic                   | 1.608    |
|        10         |  18.298  | Cryozone                    | Xenotic                   | 1.823    |
|        11         |  33.357  | Cryozone                    | Xenotic                   | 1.778    |
The interval between the perannual orbit and the next closer-in orbit is:
$$
I = \dfrac{0.969}{0.482} = 1.927\;AU
$$
… _just_ within our $I = 2.000\;AU$ maximum, and the interval to the next orbit out is:
$$
I = \dfrac{1.525}{0.969} = 1.574\;AU
$$
… which, again, is _just_ within our specified minimum $I = 1.500\;AU$, so, yes we can drop the nucleal planemo and go with the perannual planemo, instead.

> **Hippy**: I am compelled to point out that the maximum interval is not nearly as absolute as the minimum interval...

Good point!  Planemos can certainly have wider intervals between their orbits than $I = 2.000\;AU$  – we just never want them to have an interval *less-than* $I = 1.500\;AU$.

> **Keppy**: But the perannual planemo is farther out than the nucleal orbit, so won't it get less stellar flux?

Well spotted!  And we can calculate that!  Since $A = 0.969\;AU$ and $N = 0.834\;AU$, and we know that the stellar flux at *N* = 1.0, we can calculate that *A* is:
$$
\Delta = \dfrac{0.969}{0.834} = 1.162
$$
… the perannual orbit is $1.162 \times$ farther out than the nucleal orbit, and since intensity decreases with the square of the distance:
$$
F = \dfrac{1}{\Delta^2}
$$
… we can calculate that the perannual planemo receives:
$$
F = \dfrac{1}{1.162^2}= \dfrac{1}{1.350} = 0.741
$$
… about 74.1% of the stellar flux as the nucleal orbit does... but that's still:
$$
\begin{gather}
H_I = -0.26\dfrac{D}{\mathcal{N}} + 1.26 = -0.26\dfrac{0.969}{0.834} + 1.26 = -0.26(1.162) + 1.26 = -0.302 + 1.26 = 0.958
\end{gather}
$$
… an orbital habitability index of 95.8% that of the nucleal orbit.  Slightly cooler, but not drastically so.


## Parameter Ranges by Spectral Class

**Abstract:**  
This file presents a tabulated set of **stellar parameters by spectral class (O–M)**, with high, mean, and low values given for each. Parameters included are:  

- **Effective temperature (K)**  
- **Thermal Interval Constant (þ)** — the step size in Kelvin that defines subclass increments  
- **Temperature (T⊙)** relative to the Sun  
- **Radius (R⊙)** relative to the Sun  
- **Luminosity (L⊙)** relative to the Sun  
- **Mass (M⊙)** relative to the Sun  
- **Frequency (Q⊙)** relative to the Sun  

The table serves as a **ready reference for stellar design** in worldbuilding, allowing thesiasts to quickly identify plausible ranges of physical values across the standard stellar sequence. It systematizes how subclass divisions are calculated (using the TIC, þ) and provides both absolute and relative values for major stellar quantities.  

**Canon Links:**  
- Connects to **Spectral Classes, Types, and Parameters** (M002 Stars series).  
- Uses the **Thermal Interval Constant (þ) [neo]** as defined elsewhere in WCB.  
- Values support calculations in **Habitable Zones**, **Fundamental Orbits**, and related stellar-orbital frameworks.  

**Lexical Tags:**  
- **[sci]** Spectral Classes, Tempera
---
---



