---
title: ""
---

## Abstract  
**Major Topics:**  
- Introduces the **fundamental geometry and parameters of binary star systems**.  
- Defines **primary** ($M_P$) and **secondary** ($M_S$) bodies, their relationship to the **barycenter** (ḅ), and how mass ratio determines orbital extent.  
- Derives nine key **dimensional parameters** of binary motion: minimum, average, and maximum separations for the total system ($T$), the primary ($P$), and the secondary ($S$).  
- Establishes core formulas linking:  
  - barycentric distances ($P_\bullet$, $S_\bullet$) to total separation ($T_\bullet$),  
  - orbital **eccentricity** ($e$) to maximum/minimum/average positions, and  
  - constant proportionalities between stellar **mass ratios** and **orbital distances**.  
- Introduces the **Crux Metric** ($\acute{e}$) — the eccentricity at which unequal-mass orbits become tangentially adjoined.  
- Explains **relative-orbit simplification**, where the more massive body is treated as stationary when $M_P \gg M_S$.  
- Defines **barycentric motion** equivalence: the barycenter’s “orbit” mirrors that of the primary, scaled by mass ratio.  
- Summarizes **constant equalities** that remain invariant across all binary configurations.  
- Incorporates **observational context** for multiplicity among solar-type stars (Duquennoy & Mayor 1991; Raghavan et al. 2010).  
- Develops an **empirical model of companion-mass trends** (Moe & Di Stefano 2017; Li et al. 2022) showing that primary spectral class constrains secondary mass range.  
- Provides a **stochastic formulation** for secondary mass selection:  
  $$M_2 = M_1 \times ⟨⟨a ∧ b⟩⟩^{k}$$  
  with optional bias exponent $k$ to emulate observed distributions.  
- Discusses **orbital-eccentricity limits** ensuring physical separation ($T_{min} ≥ 0.10$ AU).  
- Outlines the **period–eccentricity relation** and its physical origin in **tidal circularization**, linking orbital period to eccentricity damping timescales.  
- Summarizes observed regimes (short-, intermediate-, and long-period binaries) and anomalies driven by third-body interactions or post-transfer effects.  

**Key Terms & Symbols:**  
- **$M_P$, $M_S$** — primary and secondary masses.  
- **$\mathcal{A}$** — average separation of binary components.  
- **$T_{min}$, $T_{max}$** — minimum and maximum stellar separations.  
- **$P_\bullet$, $S_\bullet$** — barycentric distances of primary and secondary.  
- **$e$** — orbital eccentricity.  
- **$\acute{e}$** — *Crux Metric*, eccentricity where orbits adjoin tangentially.  
- **$\bar{e}$** — limiting eccentricity ensuring $T_{min} ≥ 0.10$ AU.  
- **$k$** — weighting exponent for stochastic mass pairing.  
- **$\mu$** — binary mass ratio = $M_2 / (M_1 + M_2)$.  
- **$P_{circ}$** — circularization period threshold (~10 days for solar-type systems).  

**Cross-Check Notes:**  
- Complements **Stars 1 — Basics** by applying stellar parameters to multi-body configurations.  
- Establishes a quantitative basis for subsequent sections on **Roche geometry**, **Hill spheres**, and **orbital stability zones**.  
- Provides canonical formulae and constants for world-building applications involving binary or multiple stellar systems.  

___




This section focuses on binary systems in general. While higher-multiplicity arrangements are common and fascinating, they introduce significant mathematical and physical complexity beyond the current scope of this guide.
# The Basics
Binary systems consist of two bodies bound in a mutual gravitational relationship, each tracing an orbital path around a shared center of mass known as the **barycenter** (_ḅ_). This point, ||shown as a black X in the figure||, _always_ lies along the line connecting the centers of the two bodies and is not a massive object itself, but a calculated position determined by the masses and separation of the components.

When the two objects are of unequal masses ($M_2 < M_1$), the more massive object (the **primary body**) orbits on an elliptical path, on average closer to the barycenter, while the **secondary body** traces a *larger* elliptical path on average farther from the barycenter. Both orbits share the same eccentricity ($e$), and are synchronized in period, preserving the balance of angular momentum.  They differ only in extent.

A binary system is described by a total of nine dimensions:

- $T_{min}$ ,  $\mathcal{A}$ ,  $T_{max}$ :  The minimum, average, and maximum separations of the two bodies from one another
- $P_{min}$ ,  $P_{avg}$ ,  $P_{max}$: The minimum, average, and maximum separations of the **primary** body ($P$) from the **barycenter** (*ḅ*)
- $S_{min}$ ,  $S_{avg}$ ,  $S_{max}$ :  The minimum, average, and maximum separations of the **secondary** body ($S$) from the **barycenter** (*ḅ*)

… as well as the masses of the two bodies:
- $M_1$: the primary mass ($P$)
- $M_2$: the secondary mass ($S$)

… and the eccentricity of their orbits:
- $e$: a dimensionless value that describes the deviation of the orbital paths from perfectly circular; $e = 0$ means the orbit is a circle

These are related through a series of equations, which may seem daunting at first, but are quite straightforward once they are understood.
### Primary Dimensions
$$
\begin{align}
P_{avg} &= \mathcal{A} \times\dfrac{M_S}{M_P+M_S} \qquad &&\text{Primary average distance}\\[1em]
P_{min} &= P_{avg}(1 - e) \qquad &&\text{Primary minimum distance} \\[1em]
P_{max} &= P_{avg}(1 + e) \qquad &&\text{Primary maximum distance} 
\end{align}
$$
### Secondary Dimensions
$$
\begin{align}
S_{avg} &= \mathcal{A} \times\dfrac{M_P}{M_P+M_S} \qquad &&\text{Secondary average distance}\\[1em]
S_{min} &= S_{avg}(1 - e) \qquad &&\text{Secondary minimum distance} \\[1em]
S_{max} &= S_{avg}(1 + e) \qquad &&\text{Secondary maximum distance}
\end{align}
$$
### Total (Overall) Dimensions
$$
\begin{gather}
T_{min} = \mathcal{A}(1 - e)
= P_{min} + S_{min} = T_{max}\left(\dfrac{1 - e}{1 + e}\right) \\
T_{max} = \mathcal{A}(1 + e)
= P_{max} + S_{max} = T_{min}\left(\dfrac{1 + e}{1 - e}\right) \\
\mathcal{A} = \dfrac{T_{min}}{1 - e}
= \dfrac{T_{max}}{1 + e}
= P_{avg} + S_{avg}\\[0.5em]
\end{gather}
$$
### Eccentricity Relationships
> In the equations below a subscript dot $_{\bullet}$ means *any two matching parameters*; e.g.  $Max_{\bullet} - Min_{\bullet}$ means any maximum value minus any minimum value of the same parameter, such as $P_{max} - P_{min}$.
#### System Eccentricity
$$
\begin{align}
e &= \dfrac{Max_\bullet - Min_{\bullet}}{Max_\bullet + Min_{\bullet}}
\;\;=\;\; \left[1 - \dfrac{Min_{\bullet}}{Avg_{\bullet}}\right]
\;\;=\;\; \left[\dfrac{Max_{\bullet}}{Avg_{\bullet}} - 1\right] \\[1em]
&= \left(P_{max} \times \dfrac{M_P + M_S}{\mathcal{A} \times M_S}\right) - 1
\quad = \quad 1 - \left(P_{min} \times \dfrac{M_P + M_S}{\mathcal{A} \times M_S}\right) \\[1em]
&= \left(S_{max} \times \dfrac{M_P + M_S}{\mathcal{A} \times M_P}\right) - 1
\quad = \quad 1 - \left(S_{min} \times \dfrac{M_P + M_S}{\mathcal{A} \times M_P}\right) \\[1em]
\end{align}
$$
#### The Crux Metric ($\acute{e}$)
> The circle $_{\circ}$ subscript is used to indicate expressions in which all terms share the **same positional magnitude** (e.g., max, min, or average), regardless of parameter type.
$$
\begin{align}
\acute{e} = \dfrac{M_P - M_S}{M_P + M_S}
= \dfrac{|S_{\circ} - P_{\circ}|}{S_{\circ} + P_{\circ}} 
= \dfrac{|S_{\circ} - P_{\circ}|}{T_{\circ}}
\end{align}
$$
- $é$ (e-prime) is the system eccentricity value at which the orbits of the stars become *_adjoined tangential_* $(e \gt 0; M_P \neq M_S)$
- For a mass ratio of $^{M_S}/_{M_P} = 0.8$, the system requires $\acute{e} \geq 0.8519$ for the primary and secondary orbits to adjoin tangentially (see below).

---

# Relative Orbit of the Secondary
There are times (such as when the Secondary is less massive than the Primary — typically $\frac{M_1}{M_2} \gtrsim 80$, the approximate star/brown dwarf mass dividing line, but it works for sub-stellamon bodies as well — it is convenient to treat the Primary as stationary and the Secondary as following the relative orbit alone.  Therefore,
$$
\begin{gather}
R_{min} = T_{min} \\[0.5em]
R_{avg} = \mathcal{A} \\[0.5em]
R_{max} = T_{max} \\
\end{gather}
$$
For instance, in the case of the Earth-Sun system:
$$
\begin{align}
\mathcal{A} &= 1.0 AU \\[0.5em]
P_{avg} &= \mathcal{A} \times\dfrac{M_S}{M_P+M_S} \\[1em]
&= 1.0 \times \frac{1}{333000+1} \\[1em]
&= 1.0 \times \frac{1}{333001} = 3.009299 \times 10^{-6} AU \\[1.5em]
1 \text{ AU } &= 1.496 \times 10^6 \text{ km} \\
\therefore P_{avg} &= 3.009299 \times 10^{-6} \times 1.496 \times 10^8 ≈ 449 \text{ km}  
\end{align}
$$

Considering that the Sun’s radius is $696{,}340$ km, a wobble of only $≈ 450$ km ($\approx 0.065\%$) is justifiably negligible, so the math works out well enough by just treating the Sun as stationary and the Earth as orbiting it.
# Barycentrics
Similarly to the Relative Orbit of the Secondary, when dealing with a system where $M_S ≈ M_P$, it becomes more convenient to think of the masses as stationary and their barycenter "orbiting" between them. **|graphic to be added|**
$$
\begin{align}
B_{min} &=   \frac{\mathcal{a}(1 - e)\; M_S}{M_P + M_S} 
= \frac{T_{min}\; M_S}{M_P + M_S} = B_{avg}(1 - e) = \mathbf{P_{min}} \\[2em]
B_{avg} &= \frac{\mathcal{a}\; M_S}{M_P + M_S} = \mathbf{P_{avg}} \\[2em]
B_{max} &= \frac{\mathcal{a}(1 + e)\; M_S}{M_P + M_S} 
= \frac{T_{max}\; M_S}{M_P + M_S} = B_{avg}(1 + e) = \mathbf{P_{max}}
\end{align}
$$
Where:
- $\mathcal{a}$ = the average separation between the Primary in and the Secondary expressed in terms of the radius of the Primary
- $M_P$ = the mass of the Primary
- $M_S$ = the mass of the Secondary
- $e$ = the eccentricity of the system

If the mass of the Secondary ($M_S$) is expressed in terms of the mass of the Primary ($M_P$) the equations become:
$$
\begin{align}
M_0 &= \frac{M_S}{M_P} \\[1em]
B_{min} &= \frac{\mathcal{a}(1 - e)\; M_0}{M_0 + 1} 
= \frac{T_{min}\; M_0}{M_0 + 1} = B_{avg}(1 - e) = \mathbf{P_{min}} \\[2em]
B_{avg} &= \frac{\mathcal{a}\; M_0}{M_0 + 1} = \mathbf{P_{avg}} \\[2em]
B_{max} &= \frac{\mathcal{a}(1 + e)\; M_0}{M_0 + 1} 
= \frac{T_{max}\; M_0}{M_0 + 1} = B_{avg}(1 + e) = \mathbf{P_{max}}
\end{align}
$$
Note that in both sets of equations, the math works out such that the dimensions of the barycenter's "orbit" *precisely match* those of the Primary's orbit; this is incredibly convenient, as it allows us to directly compare the geometry of the barycenter's orbit to the physical dimensions of the Primary, in particular the Primary's radius ($R_P$) — more on this below.

# Constant Equalities
Some relationships between the masses of the Primary and Secondary and their related orbital separations are constant:
$$
\begin{align}
&\frac{S_\circ}{P_\circ} = \frac{M_P}{M_S} \qquad
&&\frac{P_\circ}{S_\circ} = \frac{M_S}{M_P} \\[1em]
&\frac{P_\circ}{T_\circ} = \frac{M_S}{M_P + M_S}   \qquad
&&\frac{S_\circ}{T_\circ} = \frac{M_P}{M_P + M_S} \\[1em]
&\frac{T_\circ}{P_\circ} = \frac{M_P}{M_S} + 1   \qquad
&&\frac{T_\circ}{S_\circ} = \frac{M_S}{M_P} + 1 \\[3em]
&\frac{Min_\bullet}{Max_\bullet} = \frac{1 - e}{1 + e} \qquad
&&\frac{Max_\bullet}{Min_\bullet} = \frac{1 + e}{1 - e}
\end{align}
$$

Again, if the mass of the Secondary ($M_S$) is expressed in terms of the mass of the Primary ($M_P$), the equations become:
$$
\begin{align}
&M_0 = \frac{M_S}{M_P} \\[1em]
&\frac{S_\circ}{P_\circ} = \frac{1}{M_0} \qquad
&&\frac{P_\circ}{S_\circ} = M_0 \\[1em]
&\frac{P_\circ}{T_\circ} = \frac{M_0}{M_0 + 1}   \qquad
&&\frac{S_\circ}{T_\circ} = \frac{1}{M_0 + 1} \\[1em]
&\frac{T_\circ}{P_\circ} = \frac{1}{M_0} + 1   \qquad
&&\frac{T_\circ}{S_\circ} = M_0 + 1 \\[3em]
&\frac{Min_\bullet}{Max_\bullet} = \frac{1 - e}{1 + e} \qquad
&&\frac{Max_\bullet}{Min_\bullet} = \frac{1 + e}{1 - e}
\end{align}
$$

## Mass Pairings
Solar analog stars are more often than not found in binary or multiple systems than not, with over half exhibiting multiplicity.

- **Duquennoy & Mayor (1991)** originally found that approximately **57%** of solar-type stars (spectral types F6-K3 — more-or-less what WCB calls **Solar Cognates**) in the solar neighborhood are part of binary or higher-order systems.
- **Raghavan et al. (2010)** updated this with modern data for the same spectral class range, reporting:    
    - **~44%** as binaries        
    - **~11%** as triples or higher        
    - → Yielding a total multiplicity fraction of **~55%** for solar-type stars.       

This tendency toward multiplicity defines a pattern that profoundly influences system architecture, orbital stability zones, and the landscape of potential habitability.
### Companion Mass Trends by Primary Type

From the combined statistical analyses of **Duquennoy & Mayor (1991)**, **Raghavan et al. (2010)**, **Moe & Di Stefano (2017)**, and **Li et al. (2022, LAMOST)**, a clear pattern of Primary-to-Secondary spectral type pairings emerges: the **spectral class of the primary star** strongly constrains the **range of companion masses** likely to occur. In other words, binary pairing is _not_ random across the mass spectrum.

- **Early-type primaries (A–F)** tend to draw secondaries from a **narrow, high-mass corridor**, favoring near-equal companions—what observers call the _twin excess_.    
- **Solar-type primaries (G-class)** exhibit a **broader, moderately declining distribution**, allowing both near-equal companions and somewhat smaller partners (typically late G or K types).    
- **Cooler primaries (K–M)** show a **progressively wider, low-mass-biased spread**, where secondaries are often much smaller—late K, M, or even substellar companions.    

This trend can be summarized as:

> Earlier, hotter stars → **narrow, high-q pairing range** (favoring twins).  
> Later, cooler stars → **broad, low-q range** (favoring lighter companions).

Calculating a Secondary star's mass ($M_2$) based on the mass of the Primary ($M_1$):
$$
M_2 = M_1 \times ⟨⟨a ∧ b⟩⟩^{k}
$$
Where:
- $M_1$ — primary mass  
- $M_2$ — secondary mass (assigned)  
- $⟨⟨a ∧ b⟩⟩$ — random draw between *a* and *b* (inclusive range)  
- $k$ — ***optional* weighting exponent**, biasing toward the lower or upper bound  
	- $k = 1$: uniform distribution  
	-  $0 < k < 1$: bias toward lower-mass companions  
	- $k > 1$: bias toward higher-mass (twin-like) companions  

| **Primary** | <center>**Range<br>(⟨⟨a ∧ b⟩⟩)</center><br>** | <center>**Lower-<br>bias<br>(favor<br>smaller<br>M₂)</center><br><br><br><br>** | <center>**Upper-<br>bias<br>(favor twin<br>M₂)</center><br><br><br>** | <center>**Typical<br>“neutral”<br>bias<br>value</center><br><br><br>** | <center>**Physical rationale**</center>                                                    |
| :---------: | --------------------------------------------: | ------------------------------------------------------------------------------: | --------------------------------------------------------------------: | ---------------------------------------------------------------------: | :----------------------------------------------------------------------------------------- |
| **A**       |                                   ⟨0.9 ∧ 1.0⟩ |                                                                     ⟨0.8 ∧ 0.9⟩ |                                                           ⟨1.2 ∧ 1.5⟩ |                                                                  ≈ 1.2 | High twin fraction; modest upward skew reproduces near-equal masses.                       |
| **F**       |                                   ⟨0.7 ∧ 0.9⟩ |                                                                     ⟨0.6 ∧ 0.8⟩ |                                                           ⟨1.1 ∧ 1.3⟩ |                                                                  ≈ 1.0 | Slight bias toward smaller companions, but twins still possible.                           |
| **G**       |                                   ⟨0.6 ∧ 0.8⟩ |                                                                     ⟨0.5 ∧ 0.8⟩ |                                                           ⟨1.0 ∧ 1.2⟩ |                                                                  ≈ 0.8 | Distribution roughly flat; mild downward bias reproduces the DM91 “flat or falling” trend. |
| **K**       |                                   ⟨0.4 ∧ 0.7⟩ |                                                                     ⟨0.5 ∧ 0.8⟩ |                                                           ⟨1.0 ∧ 1.1⟩ |                                                                  ≈ 0.7 | Clearly skewed toward smaller secondaries; use *p* ≈ 0.6∧0.8 to get that fall-off.         |
| **M**       |                                   ⟨0.2 ∧ 0.5⟩ |                                                                     ⟨0.5 ∧ 0.7⟩ |                                                            ⟨1.0 ∧ 1.1 |                                                                  ≈ 0.6 | Strongly bottom-heavy distribution; small-q companions common.                             |

**How to read this table**
- The “lower-bias” column gives a reasonable p range if you want your generator to prefer small companions.
- The “upper-bias” column gives values that push draws upward (more “twin-like” systems).
- The “typical neutral value” is the mid-case consistent with observed distributions.
#### Limiting Eccentricity ($\bar{e}$)
For close-binaries, the two stars should never approach closer than $T_{min} = 0.10$ AU (ideally $0.15$ AU).  The eccentricity of the system which forces this limit can be calculated by:
$$
\begin{align}
\bar{e} = \dfrac{T_{max} - 0.100}{T_{max} + 0.100}
\end{align}
$$
- $ē$ (e-bar) is the largest system eccentricity that can be used with a given $T_{max}$ , while ensuring that $T_{min} ≥ 0.100$.

If you know what eccentricity you want the system to have and need to figure out the minimum maximum separation $T_{max}$ that will maintain $T_{min} ≥ 0.100$ AU, you can calculate it by:
$$
\begin{align}
T_{max} \geq 0.100\left(\dfrac{1 + \bar{e}}{1 - \bar{e}}\right)
\end{align}
$$
### The Period–Eccentricity Relation

#### 1. **Observed Pattern**

Empirically, binary systems trace a clear trend:

| Regime           | Typical Period P | Typical Eccentricity e         | Behavior                    |
| ---------------- | ---------------- | ------------------------------ | --------------------------- |
| **Short-period** | P ≲ 10 days      | e ≈ 0                          | Nearly circular             |
| **Intermediate** | 10 – 10³ days    | e rises from 0 → 0.6           | Mixed circular / elliptical |
| **Wide**         | P ≳ 10³          | Broad scatter, e often 0.6–0.9 | Dynamically “hot”           |
This relation has been confirmed repeatedly—from **Duquennoy & Mayor (1991)** and **Raghavan et al. (2010)** to **Moe & Di Stefano (2017)** and modern **Gaia DR3** samples.

---

#### 2. **Physical Cause — Tidal Circularization**

Close binaries experience **tidal friction**: each star raises bulges on its companion.  
Friction within those bulges converts orbital energy into heat, draining the system’s eccentricity.

Circularization timescale roughly scales as
$$
t_{circ} \propto \left(\frac{\mathcal{a}}{R}\right)^8 \propto P^{\frac{16}{3}}
$$

so even a modest change in separation produces a huge difference in damping time.  
Systems that are young and close become circular long before wide pairs even notice tides.

---

#### 3. **Residual Eccentricities and Anomalies**
- **“Twin” binaries** (nearly equal-mass, short-period) are most circularized.    
- **Eccentric short-period outliers** often show evidence of a **third companion** pumping eee through Kozai–Lidov cycles.    
- **Post-mass-transfer pairs** can re-acquire modest eccentricity as mass loss changes the potential.    

---

#### 4. **Approximate Empirical Envelope**

For solar-type primaries, the upper bound of observed eccentricities can be sketched as
$$
e_{max} \simeq 1 - \left(\frac{P_{circ}}{P}\right)^\frac{2}{3}
$$
with $P_{circ} \sim 10$ days days for main-sequence systems in the solar neighborhood.  
Beyond $P \approx 1000$ days, the envelope flattens near $e_{max} \approx 0.9$.

---

### 🧭 Summary Insight

> **Short orbits → tidal geometry dominates → circular.**  
> **Long orbits → gravitational memory dominates → eccentric.**
> 
> The period–eccentricity curve is the fossilized record of each system’s early interactions and subsequent tidal sculpting.