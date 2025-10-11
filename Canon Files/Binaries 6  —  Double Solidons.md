---
title: Binaries 6
---
## Abstract  
**Major Topics:**  
- Defines **double-solidonic systems**—pairs of sub-stellar monons bound in mutual orbit—and classifies them according to both **mass ratio** and **barycentric geometry**.  
- Distinguishes two principal mass-ratio regimes:  
  - **Sobrinic solidons:** mass ratio $\varrho = \dfrac{M_2}{M_1} \le 100:1$; co-dominant or near-binary systems.  
  - **Parensic solidons:** mass ratio $\varrho = \dfrac{M_2}{M_1} > 100:1$; hierarchical or satellite-like systems.  
- Introduces **primeron** and **secondron** as the canonical terms for the dominant and subordinate members of a binary monon pair, maintaining continuity with barycentric notation from *Binaries 1 — Principles and Properties*.  
- Establishes barycentric parameters $B_{min}$, $B_{avg}$, and $B_{max}$ expressed in units of the primeron’s radius ($R_P$), allowing direct comparison between barycenter position and the physical extent of the primeron.  
- Defines two complementary descriptors:  
  - **Barycenter locus** — whether $B_{avg}$ lies inside (interior) or outside (exterior) the primeron’s radius.  
  - **Barycenter motility** — the extent to which the barycenter’s orbit is confined, ambulatory, or free relative to the primeron’s surface.  
- Combines these to yield **four canonical barycentric configurations**—interior-confined, interior-ambulatory, exterior-ambulatory, and exterior-free—and demonstrates how their intersection with the sobrinic/parensic ratio regime produces the **eightfold solidonic-pair taxonomy**.  
- Provides algebraic relations for barycentric distances  
  $$
  B_{avg} = \mu\,\mathcal{a}, \quad  
  B_{min} = B_{avg}(1-e), \quad  
  B_{max} = B_{avg}(1+e),
  $$
  with $\mathcal{a}$ expressed in primeron radii, supporting direct scaling across planemonic and sub-stellar systems.

**Key Terms & Symbols:**  
- **Primeron (P):** dominant body of the pair ($M_1, ν$).  
- **Secondron (S):** subordinate body ($M_2, μ$).  
- **ϱ:** secondron simple mass ratio ($M_2/M_1$).  
- **𝛗:** primeron simple mass ratio ($M_1/M_2$). 
- **μ, ν:** barycentric mass fractions.  
- **Bₘᵢₙ, Bₐᵥg, Bₘₐₓ:** barycentric distances relative to the primeron.  
- **R_P:** primeron radius used as the scaling unit.  
- **Locus:** interior vs. exterior position of the barycenter.  
- **Motility:** confined, ambulatory, or free orbital motion.  

**Cross-Check Notes:**  
- Extends the barycentric framework of *Binaries 1* to sub-stellar mass domains defined in *Meta 1 — Principles* and *Planemons 3 — Parameter Boundaries*.  
- Establishes the formal geometric basis for subsequent modules on **Barycentric Regimes** and **solidonic Dynamics**.  
- Integrates terminology consistent with the **Primaron–Secondron convention** for mass-pair systems.
# Double solidons
Paired solidons may be of two types
- Sobrinic: mass-ratio $\varrho = \dfrac{M_2}{M_1} \le 100:1$
- Parensic: mass-ratio $\varrho = \dfrac{M_2}{M_1} > 100:1$

Each of these types may be one of two sub-types, based on the relationship of their barycenter to the center of mass of the primeron.
## Barycenter Parameters
In binary monon systems (of all mass classes), where $M_2 ≈ M_1$, it is often convenient to imagine the two monons as being stationary and their _barycenter (ḅ)_ as tracing an orbit between them.

The barycenter's orbit describes an ellipse with its center denoted by $B_{avg}$, the vertex closest to the primaron's center-of-mass being denoted as $B_{min}$ and the vertex farthest from the primaron's center-of-mass being denoted as $B_{max}$.

In this frame translation, the equations of the barycenter's orbit are similar to those of the primaron's orbit in the barycenter-static frame, except that the average distance between the two monons ($\mathcal{a}$) is expressed in terms of the radius of the primaron body.  For clarity, we use a _B_ for these distances, rather than a _P_:

$$
\begin{array}{ll}
B_{avg} = \mu\,\mathcal{a} \qquad &\text{Barycenter average separation}\\[0.5em]
B_{min} = B_{avg}(1 - e) \qquad &\text{Barycenter minimum separation} \\[0.5em]
B_{max} = B_{avg}(1 + e) \qquad &\text{Barycenter maximum separation} 
\end{array}
$$

Where:
- $\mu = \dfrac{M_2}{M_1 + M_2}$, the secondron mass-fraction
- $\mathcal{a}$ = the average separation between the two bodies (in primeron radii)
- $e$ = the eccentricity of the system orbits

We compare the values of $B_{min}, B_{avg}, \text{ and } B_{max}$ to the radius of the primaron ($R_P$) to determine the barycenter's _locus_ and _motility_.
### Barycenter _locus_
This is a measure of where $B_{avg}$ falls relative to the center of mass of the primaron:
- $B_{avg} \le R_P$: the barycenter locus is _interior_.
- $B_{avg} > R_P$: the barycenter locus is _exterior_.
### Barycenter _motility_
This is a measure of the values of $B_{min}$ and $B_{max}$ to the primaron's center-of-mass, and there are _three_ possible configurations:
1. $B_{max} \le R_P$: the barycenter's motility is _confined_; no part of the barycenter's orbit extends beyond the physical volume of the primaron; because $B_{min} \;\cdot\!\!< B_{max}$, there's no need to specify its relationship to the primaron's center of mass in this case.
2. $B_{min} \le R_P$ and $B_{max} \ge R_P$: the barycenter's motility is _ambulatory_; part of the barycenter's orbit extends beyond the physical volume of the primaron.
3. $B_{min} > R_P$: the barycenter's motility is _free_; no part of the barycenter's orbit extends into the physical volume of the primaron; because $B_{max} \;\cdot\!\!> B_{min}$, there's no need to specify its relationship to the primaron's center of mass in this case.
#### Combining _locus_ and _motility_
The combination of locus and motility result in _four_ possible configurations:
- If $B_{max} < R_P$, then by definition $B_{avg} < R_P$, and the barycenter configuration is
   _interior confined_.
- If $B_{min} > R_P$, then by definition $B_{avg} > R_P$, and the barycenter configuration is _exterior free_.
- If $B_{avg} \le R_P$ (by definition $B_{min} < R_P$) and $B_{max} > R_P$, then the barycenter configuration is _interior ambulatory_.
- If $B_{avg} > R_P$ (by definition $B_{max} > R_P$), and $B_{min} \le R_P$, then the barycenter configuration is _exterior ambulatory_.

| **Locus** | **Motility** | **Configuration** | **Barycenter Position** |
|:--|:--|:--|:--|
| Interior | Confined | **Interior-Confined** | Entire barycenter orbit lies within the physical volume of the primaron. |
| Interior | Ambulatory | **Interior-Ambulatory** | Barycenter orbit crosses the primaron’s surface; part of its path is interior. |
| Exterior | Ambulatory | **Exterior-Ambulatory** | Barycenter orbit grazes or passes tangent to the primaron’s surface. |
| Exterior | Free | **Exterior-Free** | Entire barycenter orbit lies outside the primaron’s physical volume. |

| ↓ Motility ↓ |     Locus is Interior<br>$B_{avg} \le R_P$     |      Locus is Exterior<br>$B_{avg} > R_P$      |
| ------------ | :--------------------------------------------: | :--------------------------------------------: |
| Confined     | $B_{min} < B_{avg} < B_{max} \le \mathbf{R_P}$ |                       —                        |
| Ambulatory   | $B_{min} < B_{avg} \le \mathbf{R_P} < B_{max}$ | $B_{min} \le \mathbf{R_P} < B_{avg} < B_{max}$ |
| Free         |                       —                        | $\mathbf{R_P} \le B_{min} < B_{avg} < B_{max}$ |

This schema yields eight possible **solidonic pairings**, grouped by mass ratio:
- **Sobrinon** ($\varrho \le 100:1$)
  1. Interior-Confined  
  2. Interior-Ambulatory  
  3. Exterior-Ambulatory  
  4. Exterior-Free
- **Parenson** ($\varrho > 100:1$)
  1. Interior-Confined  
  2. Interior-Ambulatory  
  3. Exterior-Ambulatory  
  4. Exterior-Free

# What is a "moon"?
In WCB, the term **moon** is *synergological*; that is to say, it describes a **relationship** rather than a condition or status.

Accordingly, WCB defines *moon* as:

> “A natural mononic satellite of another monon that is one hundred or more times more massive than itself.”

The technical term for such a relationship is **parensate** — a monon gravitationally bound to another that overwhelmingly dominates the barycenter.

Thus, Titan is a *moon* of Saturn; and if Earth were in orbit around Jupiter, it too would be classed as a *moon*.

By contrast, if **Uranus** were in orbit around **Jupiter**, it would *not* be a moon (parensate) but a **sobrinate**, because the primeron mass ratio between the two is less than 100 : 1:

$$
\varphi = \frac{M_{Jupiter}}{M_{Uranus}} = \frac{317.8}{14.536} ≈ 21.9
$$

The singular term for a sobrinic pair is a **sobrinon**; for a parensic pair, a **parenson**.  
We might therefore speak of the *Jupiter–Uranus sobrinon* or the *Saturn–Titan parenson*.

# Historical Context
## Etymology of "moon"
Most dictionaries are somewhat specific in defining the word “moon”: something along the lines of “a moon is a natural satellite of a planet”. However, modern exploration has shown this definition to be limiting: even asteroids have "moons" (Hebe 6 and $415$ others are known as of this writing). So, for our purposes, we need to be a bit more general.  WCB defines "moon" as  “a natural satellite of a monon more than 100 or more times more massive than itself.”

## "The" Moon
In English, the generic noun turned into a proper noun, “the Moon”, as a name for Earth’s only natural satellite. Other English names for the Moon, less commonly seen or used, include Luna, Selene, and Cynthia (the first is Latin, the others Greek). The most common adjectival form used to refer to the Moon is "lunar", though you might also sometimes see “selenic" and “cynthion" (with a hard ‘c’).

As a proper noun, the name “Moon” comes from Old English *mōna*, stemming from Proto-Germanic \**mēnōn*, itself from Proto-Indo-European (PIE) \**mēnsis*, which meant "month" (and still exists in English as “menses”), ultimately derived from PIE \**mēnōt* "to measure", because the Moon's phases were used to measure that unit of time.

In WCB, we will most often refer to Earth's Moon by the Roman name Luna, along with its related terms "lunar", "lunation", — 

> **Keppy:** And "lunacy"!

> **Hippy:** You'd know, Keplarius; you'd know.

For convenience, we'll often just use "moon" generically and more specific terms when distinction is called-for.