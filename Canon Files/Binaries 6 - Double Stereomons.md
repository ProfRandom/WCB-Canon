---
title: Binaries 6
---
# Double Stereomons
Paired stereomons may be of two types
- Sobrinic: mass-ratio $\varrho = \tfrac{M_2}{M_1} < 100:1$
- Parensic: mass-ratio $\varrho = \frac{M_2}{M_1} > 100:1$

Each of these types may be one of two sub-types, based on the relationship of their barycenter to the center of mass of the primeron.
## Barycenter Parameters
In binary monon systems (of all mass classes), where $M_2 ≈ M_1$, it is more convenient to think of the two monons as being stationary and their _barycenter (ḅ)_ as orbiting between them.

The barycenter's orbit describes an ellipse with its center denoted by $B_{avg}$, the vertex closest to the primaron's center-of-mass being denoted as $B_{min}$ and the vertex farthes from the primaron's center-of-mass being denoted as $B_{max}$.

In this frame translation, the equations of the barycenter's orbit are similar to those of the primaron's orbit in the barycenter-static frame, except that the average distance between the two monons ($\mathcal{a}$) is expressed in terms of the radius of the primaron body.  For clarity, we use a _B_ for these distances, rather than a _P_:

$$
\begin{array}{ll}
B_{avg} = \mu\,\mathcal{a} \qquad &\text{Barycenter average separation}\\[0.5em]
B_{min} = B_{avg}(1 - e) \qquad &\text{Barycenter minimum separation} \\[0.5em]
B_{max} = B_{avg}(1 + e) \qquad &\text{Barycenter maximum separation} 
\end{array}
$$

Where:
- $\mu = \frac{M_2}{M_1 + M_2}$, the secondron mass-fraction
- $\mathcal{a}$ = the average separation between the two bodies (in primeron radii)
-  $e$ = the eccentricity of the system orbits

We compare the values of $B_{min}, B_{avg}, \text{ and } B_{max}$ to the radius of the primaron ($P_r$) to determine the barycenter's _locus_ and _motility_.
### Barycenter _locus_
This is a measure of where $B_{avg}$ falls relative to the center of mass of the primaron:
- $B_{avg} \le P_r$: the barycenter locus is _interior_.
- $B_{avg} > P_r$: the barycenter locus is _exterior_.

### Barycenter _motility_
This is a measure of the values of $B_{min}$ and $B_{max}$ to the primaron's center-of-mass, and there are _three_ possible configurations:
1. $B_{max} \le P_r$: the barycenter's motility is _confined_; no part of the barycenter's orbit extends beyond the physical volume of the primaron; because $B_{min} \;\cdot\!\!< B_{max}$, there's no need to specify its relationship to the primaron's center of mass in this case.
2. $B_{min} \le P_r$ and $B_{max} \ge P_r$: the barycenter's motility is _ambulatory_; part of the barycenter's orbit extends beyond the physical volume of the primaron.
3. $B_{min} > P_r$: the barycenter's motility is _free_; no part of the barycenter's orbit extends into the physical volume of the primaron; because $B_{max} \;\cdot\!\!> B_{min}$, there's no need to specify its relationship to the primaron's center of mass in this case.

#### Combining _locus_ and _motility_
The combination of locus and motility result in _four_ possible configurations:
- If $B_{max} < P_r$, then by definition $B_{avg} < P_r$, and the barycenter configuration is
   _interior confined_.
- If $B_{min} > P_r$, then by definition $B_{avg} > P_r$, and the barycenter configuration is _exterior free_.
- If $B_{avg} \le P_r$ (by definition $B_{min} < P_r$) and $B_{max} > P_r$, then the barycenter configuration is _interior ambulatory_.
- If $B_{avg} > P_r$ (by definition $B_{max} > P_r$), and $B_{min} \le P_r$, then the barycenter configuration is _exterior ambulatory_.
