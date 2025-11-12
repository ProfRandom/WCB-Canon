# Micromon Belt Placement and Extents

## Placing The Belt and Identifying Its Dimensions

$$
\begin{aligned}
a_i &= &&\text{Inner orbit distance} \\
a_o &= &&\text{Outer orbit distance} \\[0.5em]
m_i &= &&\text{Mass of inner body in Terrans} \\
m_o &= &&\text{Mass of outer body in Terrans} \\[0.5em]
M_* & = 333000M⊙ \qquad &&\text{Mass of star in Terrans} \\[0.5em]
a_c &= \frac{a_i + a_o}{2} \qquad &&\text{Average of the two orbits} \\[0.5em]
\Delta a &= a_o - a_i \qquad &&\text{Difference between the two orbits} \\[0.5em]
a_\Delta &= \frac{\Delta a}{2} \qquad &&\text{Midrange of the two orbits} \\[0.5em] 
a_s &= a_c + a_\Delta \left(\frac{m_o - m_i}{m_o + m_i}\right) \qquad &&\text{Asymmetric central orbit} \\[0.5em]
m_\mu &= \frac{m_i + m_o}{M_*} \qquad &&\text{Dimensionless systemic mass ratio} \\[0.5em]
\beta &= 1 - (C \times \sqrt[3]{m_\mu}) \qquad &&\text{Where C} \in \{1, 2, 3\} \\
&&&\text{Belt width scaler} \\[0.5em]
W_{belt} &= \Delta a \times \beta \qquad &&\text{Belt width calculation}\\[0.5em]
w_i &= \frac{m_i}{m_i + m_o} \qquad w_o = \frac{m_o}{m_i + m_o} \quad &&\text{Belt inner and outer edge adjustments} \\[0.5em]
W_i &= W_{belt} \times w_i \qquad W_o = W_{belt} \times w_o \quad && \text{Belt inner and outer edge offset calculations}\\[0.5em]
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
a_x &= \sqrt[3]{P_x^2 \, M\odot}, \quad P_x = P_i \times k \\[1em]
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
a_x &= \sqrt[3]{P_x^2 \, M\odot}, \quad P_x = \frac{P_o}{k} \\[1em]
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
a_x &= \sqrt[3]{\Big((P_i \times k)^2 \, M\odot\Big)} \\[0.5em]
 \text{Where: } k &\in \{1.67, 2.00, 2.25, 2.33, 2.50, 2.67, 3.00, 3.50, 4.00, 5.00\}
\end{aligned}
$$
##### Outer Orbit Resonances
$$
\begin{aligned}
a_x &= \sqrt[3]{\left(\frac{P_o}{k}\right)^2 M\odot} \\[0.5em]
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
g_i &= a \times \sqrt{\frac{m_i}{333000M⊙}} \\[1em]
g_o &= a \times \sqrt{\frac{m_o}{333000M⊙}} \\[1em]
g_{quad} &= \sqrt{g_i^2 + g_o^2}
\end{aligned}
$$
Both methods are algebraically equivalent: the $g_{quad}$ form expands ***exactly*** into the $g_w$ expression:

$$
g_{quad} = \sqrt{g_i^2 + g_o^2} = \sqrt{\left(a^2 \frac{m_i}{M_*}\right) + \left(a^2 \frac{m_o}{M_*}\right)} = a \times \sqrt{\frac{m_i + m_o}{M_*}} = g_w \; \checkmark
$$
# Harmonic Periods

*Harmonic periods* are crucial for understanding how a planet's rotational and orbital cycles synchronize.  The harmonic period $H$ is the time interval over which the two independent motions align in their periodicity.

$$
H = \dfrac{P_1 \times P_2}{|P_1 - P_2|}
$$
Where:
- $P_1$ = length of the solar day
- $P_2$ = length of the sidereal day
- $H$ = harmonic period

> Yes, this is actually the same equation as the synodic period.

## Example
Using Earth's solar day and sidereal day:

$$
\begin{array}{l l}
P_1 = 86400^s &\text{solar day}\\
P_2 = 86164.090531^s &\text{sidereal day}
\end{array}
\begin{aligned}
\begin{split}
H &= \dfrac{P_1 \times P_2}{|P_1 - P_2|} \\[0.5em]
&= \dfrac{86400 \times 86164.090531}{|86400 - 86164.090531|} \\[0.5em]
&= \dfrac{7444577422}{235.9094692} \\[0.5em]
H &= 31556924.9854376^s\; \checkmark
\end{split}
\end{aligned}
$$
… we find that the harmonic period between the solar day and the sidereal day is approximately the length of the *tropical year*, differing from the official value of $31556925.216^s$ by an excess of only $0.2306^s$.

Similarly, calculating the harmonic period between Earth's solar day and the *stellar day*:

$$
\begin{array}{l l}
P_1 = 86400^s &\text{solar day}\\
P_2 = 86164.0989^s &\text{stellar day}
\end{array}
\begin{aligned}
\begin{split}
H &= \dfrac{P_1 \times P_2}{|P_1 - P_2|} \\[0.5em]
&= \dfrac{86400 \times 86164.0989}{|86400 - 86164.0989|} \\[0.5em]
&= \dfrac{7444578145}{235.901096} \\[0.5em]
H &= 31558048.1047344^s\; \checkmark
\end{split}
\end{aligned}
$$
… a difference of only $101.65737^s$ longer than the official length of the *sidereal year*: $31558149.7635456^s$.

# Orbit Randomization Notation
This symbolic system defines how to procedurally generate a sequence of orbital radii using randomized multiplicative (or divisive) steps from a baseline (**basal**) value. It distinguishes between **intrabasal** (moving inward) and **extrabasal** (moving outward) orbit generation.

The notation is fully symbolic and compatible with WCB's randomization and range assignment grammar.

**Intrabasal**

$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i-1} = \frac{r_i}{⟨⟨ \text{min} ∧ \text{max} ⟩⟩}
\quad \text{while } r_i ≥ \Omega
$$

**Extrabasal**

$$
r_i = B;\; \Omega = \text{«▢»}: \qquad
r_{i+1} = r_i \cdot ⟨⟨ \text{min} ∧ \text{max} ⟩⟩
\quad \text{while } r_i ≤ \Omega
$$
Where:
- B = basal orbital radius (e.g. the nucleal orbit $N$)
- Ω = orbital distance cuttoff (minimum or maximum allowed orbit based on the star system constraints)

## 🔄 Usage Strategy

The **intrabasal** and **extrabasal** forms can be used independently depending on your desired anchoring strategy:

- 🧭 **Outward-Only Generation**  
  If you begin at the **innermost permissible orbit** (e.g. a thermal, Roche, or design constraint), use the **extrabasal** form to expand outward via multiplicative steps:

$$
  r_0 = «inner limit»;\; L = «system edge»:
  \quad r_{i+1} = r_i \cdot ⟨⟨min ∧ max⟩⟩, \text{ while } r_{i+1} ≤ L
$$
- 🧭 **Outward-Only Generation**  
  If you begin at the **outermost permissible orbit** (e.g. a thermal or design constraint), use the **extrabasal** form to expand outward via multiplicative steps:

$$
  r_0 = «inner limit»;\; L = «system edge»:
  \quad r_{i-1} = \dfrac{r_i} {⟨⟨min ∧ max⟩⟩}, \text{ while } r_{i+1} ≤ L
$$

> Either method can fully define a system — or both can be combined with a central anchor (e.g. nucleal orbit) to scaffold a bidirectional structure.

