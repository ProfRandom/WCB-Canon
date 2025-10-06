## Abstract  
**Major Topics:**  
- Defines the **barycentric framework** for all two-body systems, introducing a consistent geometric test for distinguishing **binary** and **satellite** configurations.  
- Establishes that the barycenter’s **locus** relative to the Primary’s radius \(R_P\) is the governing criterion for classification:  
  - \(r_B > R_P\) → **Binary Planemon System** (barycenter outside the Primary).  
  - \(r_B < R_P\) → **Planemon–Moon Pair** (barycenter within the Primary).  
- Introduces **barycentric motility**, the degree to which the barycenter’s position oscillates *into or out of* the Primary’s physical volume, producing four formal categories:  
  1. **Interior-Consistent (S₁)** — barycenter always within.  
  2. **Interior-Migratory (H₂)** — barycenter within on average, but emerges periodically.  
  3. **Exterior-Migratory (H₁)** — barycenter outside on average, but enters periodically.  
  4. **Exterior-Consistent (B₁)** — barycenter always outside.  
- Demonstrates that all two-body systems (planemon–moon, double-planemon, star–planet, stellar binaries) can be classified within this unified barycentric-locus geometry.  
- Validates Asimov’s “double-planet” intuition for the **Earth–Moon system** through geometric criteria, not the variable Tug-of-War Ratio.  
- Defines context-independent mass-ratio thresholds (≈ 80 : 1 and ≈ 4000 : 1) as scale-invariant barycentric boundaries for satellite → binary transitions.  
- Confirms that barycentric quantities share equivalent periodicity: \(B_\circ = P_\circ = S_\circ\).  

**Key Terms & Symbols:**  
- **Barycenter (B)** — system center of mass.  
- **Motility (𝐵̃)** — barycenter’s migration relative to Primary volume.  
- **Locus (𝐵̌)** — positional magnitude of the barycenter.  
- **Hybrid Type 1 / Type 2 (H₁ / H₂)** — transitional barycentric regimes.  
- **Barycentric Locus Test** — classification by \(r_B / R_P\).  
- **Barycentric Morphology Principle** — all paired bodies share a single period, distinct radii, and proportional velocities.  

**Cross-Check Notes:**  
- Fully consistent with **Meta 1 — Principles.md** (system architecture) and **Monons 2 — Properties and Parameters.md** (mass relationships).  
- Extends the formalism to include **hybrid regimes** without redefining planemon or monon classes.  
- Provides the canonical geometric replacement for Asimov’s Tug-of-War method.  
- No contradictions or naming collisions with existing canon.  
- **Status:** [FORMALIZED] — establishes barycentric classification standard across all mononic and stellar scales.  
---
---


This section focuses on binary systems in general. While higher-multiplicity arrangements are common and fascinating, they introduce significant mathematical and physical complexity beyond the current scope of this guide.
# The Basics
Binary systems consist of two bodies bound in a mutual gravitational relationship, each tracing an orbital path around a shared center of mass known as the **barycenter** (_ḅ_). This point, >shown as a black X in the figure<, _always_ lies along the line connecting the centers of the two bodies and is not a massive object itself, but a calculated position determined by the masses and separation of the components.

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


