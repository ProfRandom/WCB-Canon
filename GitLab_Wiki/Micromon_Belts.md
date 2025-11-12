# Micromon Belt Placement and Extents

## Placing The Belt and Identifying Its Dimensions

$$
\begin{aligned}
a_i &= &&\text{Inner orbit distance} \\
a_o &= &&\text{Outer orbit distance} \$$0.5ex]
m_i &= &&\text{Mass of inner body in Terrans} \\
m_o &= &&\text{Mass of outer body in Terrans} \$$0.5ex]
M_* & = 333000M⊙ \qquad &&\text{Mass of star in Terrans} \$$0.5ex]
a_c &= \frac{a_i + a_o}{2} \qquad &&\text{Average of the two orbits} \$$0.5ex]
\Delta a &= a_o - a_i \qquad &&\text{Difference between the two orbits} \$$0.5ex]
a_\Delta &= \frac{\Delta a}{2} \qquad &&\text{Midrange of the two orbits} \$$0.5ex] 
a_s &= a_c + a_\Delta \left(\frac{m_o - m_i}{m_o + m_i}\right) \qquad &&\text{Asymmetric central orbit} \$$0.5ex]
m_\mu &= \frac{m_i + m_o}{M_*} \qquad &&\text{Dimensionless systemic mass ratio} \$$0.5ex]
\beta &= 1 - (C \times \sqrt[3]{m_\mu}) \qquad &&\text{Where C} \in \{1, 2, 3\} \\
&&&\text{Belt width scaler} \$$0.5ex]
W_{belt} &= \Delta a \times \beta \qquad &&\text{Belt width calculation}\$$0.5ex]
w_i &= \frac{m_i}{m_i + m_o} \qquad w_o = \frac{m_o}{m_i + m_o} \quad &&\text{Belt inner and outer edge adjustments} \$$0.5ex]
W_i &= W_{belt} \times w_i \qquad W_o = W_{belt} \times w_o \quad && \text{Belt inner and outer edge offset calculations}\$$0.5ex]
B_i &= a_s - W_i \qquad B_o = a_s + W_o \qquad &&\text{Belt inner and outer edge calculations}
\end{aligned}
$$

## Calculating Resonant Orbits

### Vocabulary Notes
- Perturber: An orbiting object acting to perturb the orbit of other, less massive nearby objects.
- Perturbant: The body exerting perturbing influence.
- Resonant: Any of the resonances that result from the influence of the perturbant.
- Tresonance: A resonance tending to trap orbiting bodies within a narrow orbital region.
- Gresonance: A resonance tending to exclude orbiting bodies from a narrow orbital region.

When mapping resonant gap orbits, use the bracketing orbits as **perturbers**. For each perturber, resonances can be found by scaling the orbital period with small integer ratios and converting back to distance with Kepler’s Third Law ($P^2 \propto a^3$).

1. When both perturbers have equal mass ($m_i = m_o$) calculate resonance orbits only from the mass and orbital distance of the outer perturber.
2. When the perturbers have differenting masses:
	- If their mass ratio ≤ 10:1, calculate resonance orbits for both inner and outer perturbers and pairwise-average them.
	- If their mass ratio > 10:1, calculate resonance orbits using only the mass and orbital distance of the more massive perturber (regardless of location).

### Inner Orbit Resonances
Using the **inner perturber** with period $P_i$.  

$$
\begin{aligned}
a_x &= \sqrt[3]{P_x^2 \, M\odot}, \quad P_x = P_i \times k \$$1ex]
\text{Where: } k &\in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
\end{aligned}
$$
Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M\odot$ = stellar mass (in solar units)  
- $k$ = resonance scaler (see below for details)  

***Keep only values where $a_x > B_i$ (beyond the inner orbit).***  

### Outer Orbit Resonances
Using from the **outer perturber** with period $P_o$.  

$$
\begin{aligned}
a_x &= \sqrt[3]{P_x^2 \, M\odot}, \quad P_x = \frac{P_o}{k} \$$1ex]
\text{Where: } k &\in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
\end{aligned}
$$
Where:
- $P_x$ = resonant period  
- $a_x$ = resonant distance (AU)  
- $M\odot$ = stellar mass (in solar units)  
- $k$ = resonance scaler  

***Keep only values where $a_x < B_o$ (inside the outer orbit).***  

#### Combined Equation Forms:

##### Inner Orbit Resonances
$$
\begin{aligned}
a_x &= \sqrt[3]{\Big((P_i \times k)^2 \, M\odot\Big)} \$$0.5ex]
 \text{Where: } k &\in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
\end{aligned}
$$
##### Outer Orbit Resonances
$$
\begin{aligned}
a_x &= \sqrt[3]{\left(\frac{P_o}{k}\right)^2 M\odot} \$$0.5ex]
 \text{Where: } k &\in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
 \end{aligned}
$$
### Details: Resonance Scalers
*Sorted in order of frequency*

#### Gap Resonances (Gresonances)

|  Notes   | Perturbant | Resonant |  Ratio  | Order | Frequency<br>$\tfrac{\text{Perturbant}}{\text{Resonant}}$ |
| :------: | :--------: | :------: | :-----: | :---: | :-------------------------------------------------------: |
|    4     |     5      |    3     |   5:3   |   2   |                           1.67                            |
| **3, 4** |   **2**    |  **1**   | **2:1** | **1** |                         **2.00**                          |
|          |     9      |    4     |   9:4   |   5   |                           2.25                            |
|    4     |     7      |    3     |   7:3   |   4   |                           2.33                            |
|    4     |     5      |    2     |   5:2   |   3   |                           2.50                            |
|          |     8      |    3     |   8:3   |   5   |                           2.67                            |
|    4     |     3      |    1     |   3:1   |   2   |                           3.00                            |
|          |     7      |    2     |   7:2   |   5   |                           3.50                            |
|    4     |     4      |    1     |   4:1   |   3   |                           4.00                            |
|          |     5      |    1     |   5:1   |   4   |                           5.00                            |

#### Trap Resonances (Tresonances)

| Notes | Perturbant | Resonant | Ratio | Order | Frequency<br>$\tfrac{\text{Perturbant}}{\text{Resonant}}$ |
| :---: | :--------: | :------: | :---: | :---: | :-------------------------------------------------------: |
|   4   | 4          | 3        | 4:3   | 1     |                           1.33                            |
|   4   | 3          | 2        | 3:2   | 1     |                           1.50                            |
|       | 5          | 4        | 5:4   | 1     |                           1.25                            |
|       | 6          | 5        | 6:5   | 1     |                           1.20                            |
|       | 7          | 6        | 7:6   | 1     |                           1.17                            |

> **Notes:**
> 1. The higher the resonant order, the weaker the resonance.
> 2. It is worth noting that all gap resonances have frequencies > 1.50 and all trap resonances have frequencies ≤ 1.50.
> 3. Resonance 2:1 is the only first-order gap resonance, though it can, under certain circumstances, behave as a trap resonance.
> 4. These resonance ratios are all observed in the Solar System micromon belt, though the framework is generalizable to other systems.

>**Usage:**
>Preferentially choose resonance ratios with order 1 or 2 whenever possible: resonances of order 1 or 2 will have the strongest dynamical signatures (clear gaps or stable traps). Higher orders may be used sparingly to add fine structure, but their effects will be much weaker.

# Width of Gaps
## Justification
For a resonance gap in an micromon belt to be significant, it should be ≥ 0.1% of the orbital radius of the gap, itself.

$$
\begin{aligned}
\frac{m_p}{M_*} ≥ 10^{-6} \\
\therefore m_p ≥ \frac{M_*}{10^6}
\end{aligned}
$$
Where:
- $m_{p}$ = the mass of the perturber in Terrans
- $M_*$ = the mass of the star in Terrans $= 333000$ × the mass of the star in solar units ($M_\odot$)

### Example:

Given: $M_{*} = 333000 M_{⨁} = 333000$ (for the Sun):

$$
m_p ≥ \frac{333000}{10^6} = 0.333 m_{⨁}
$$
**Meaning:**
- A body must be **at least 0.333 Earth masses** (~⅓⨁) to carve a **recognizable Kirkwood gap** in a main-belt analogue.
- **Below this** (midimons, small planemons), the “gap width” is so narrow it doesn’t register as a true Kirkwood void.

## Calculating Gap Widths
For each resonant orbit calculated above, calculate a gap width by:

$$
g_w = a \times \sqrt{\frac{m_i + m_o}{333000M⊙}} \qquad \text{Preferred method}
$$
or

$$
\begin{aligned}
g_i &= a \times \sqrt{\frac{m_i}{333000M⊙}} \$$1ex]
g_o &= a \times \sqrt{\frac{m_o}{333000M⊙}} \$$1ex]
g_{quad} &= \sqrt{g_i^2 + g_o^2}
\end{aligned}
$$
Both methods are algebraically equivalent: the $g_{quad}$ form expands ***exactly*** into the $g_w$ expression:

$$
g_{quad} = \sqrt{g_i^2 + g_o^2} = \sqrt{\left(a^2 \frac{m_i}{M_*}\right) + \left(a^2 \frac{m_o}{M_*}\right)} = a \times \sqrt{\frac{m_i + m_o}{M_*}} = g_w \; \checkmark
$$
# Estimating When Perturber Masses Are Unknown
## Micromon Belt Placement — Massless Geometric Approximation

When planetary masses are unknown or uncertain, belt placement can be estimated purely from orbital geometry.  
This approach assumes that stable belts tend to occupy the middle of wide orbital gaps, where non-resonant orbits persist.

### 1. Parameters
$$
\begin{aligned}
&\textbf{Symbol} && \textbf{Meaning} \\
&a_i && \text{Inner perturber orbit (AU)} \\
&a_o && \text{Outer perterber orbit (AU)} \\
&a_c && \text{Logarithmic (geometric) midpoint between $a_i$ and $a_o$} \\
&W_{belt} && \text{Total belt width} \\
&b_i,\;b_o && \text{Inner and Outer belt edges} \\
&k_b && \text{Belt width fraction (0.30.5 typical)}
\end{aligned}
$$
### 2. Core Relations

$$
\begin{aligned}
a_c &= \sqrt{a_i a_o} &&\text{Central orbit (geometric mean)} \\[0.5ex]
\Delta a &= a_o - a_i &&\text{Orbital gap width} \\[0.5ex]
W_{belt} &= k_b \times \Delta a &&\text{Belt width fraction (30–50 \% of gap)} \\[0.5ex]
B_i &= a_c - \frac{W_{belt}}{2} \\[1ex]
B_o &= a_c + \frac{W_{belt}}{2} &&\text{Inner / outer edges}
\end{aligned}
$$

*Optional refinement:* bias toward one side by adding a small asymmetry factor

$$
\delta = \frac{a_o / a_c - a_c / a_i}{a_o / a_i} \\

B_i = a_c - \frac{W_{belt}}{2}(1+\delta), \qquad B_o = a_c + \frac{W_{belt}}{2}(1-\delta)
$$

### 3. Example — Eikon System

$$
\begin{aligned}
a_i &= 3.024\ \text{AU}, \quad a_o = 5.953\ \text{AU} \\
a_c &= \sqrt{1.817\times5.953} = 4.243\ \text{AU} \\
\Delta a &= 2.929\ \text{AU} \\
&\text{For $k_b = 0.4$} \\
W_{belt} &= 0.4 \cdot 2.929 = 1.171\ \text{AU} \\  
B_i &= 4.242 - 0.586 = 3.657\ \text{AU} \\
B_o &= 4.242 + 0.586 = 4.828\ \text{AU}
\end{aligned}
$$

**Result:**  
A stable **Main Micromon Belt** extending from **≈ 3.7 AU to 4.8 AU**,  
centered near 3.3 AU with a total width of ≈ 1.6 AU.

### 4. Interpretation

This method yields dynamically reasonable belts without requiring planetary mass estimates.  
Use $k_b$ to tune the belt’s compactness:

- $k_b = 0.3$: narrow, resonance-bound belt  
- $k_b = 0.4$: Solar-analog main belt  
- $k_b = 0.5$: broad debris-rich belt  

When perturber masses become known, the geometric model can be refined by substituting the full mass-based method.


