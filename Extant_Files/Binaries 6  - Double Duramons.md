---
title: Binaries 6
---

# Double Duramons
Paired duramons may be of two types
- Sobrinic: mass-ratio $\varrho = \frac{M_2}{M_1} \le 100:1$
- Parensic: mass-ratio $\varrho = \frac{M_2}{M_1} > 100:1$

Each of these types may be one of two sub-types, based on the relationship of their barycenter to the center of mass of the primaron.

## Barycenter Parameters
In binary monon systems (of all mass classes), where $M_2 ≈ M_1$, it is often convenient to imagine the two monons as being stationary and their *barycenter (ḅ)* as tracing an orbit between them.

The barycenter's orbit describes an ellipse with its center denoted by $B_{avg}$, the vertex closest to the primaron's center-of-mass being denoted as $B_{min}$ and the vertex farthest from the primaron's center-of-mass being denoted as $B_{max}$.

In this frame translation, the equations of the barycenter's orbit are similar to those of the primaron's orbit in the barycenter-static frame, except that the average distance between the two monons ($A$) is expressed in terms of the radius of the primaron body.  For clarity, we use a *B* for these distances, rather than a *P*:

$$
\begin{array}{ll}
B_{avg} = \mu\,A \qquad &\text{Barycenter average separation}\\[0.5em]
B_{min} = B_{avg}(1 - e) \qquad &\text{Barycenter minimum separation} \\[0.5em]
B_{max} = B_{avg}(1 + e) \qquad &\text{Barycenter maximum separation} 
\end{array}
$$

Where:
- $\mu = \dfrac{M_2}{M_1 + M_2}$, the secondron mass-fraction
- $A$ = the average separation between the two bodies (in primaron radii)
- $e$ = the eccentricity of the system orbits

We compare the values of $B_{min}, B_{avg}, \text{ and } B_{max}$ to the radius of the primaron ($R_P$) to determine the barycenter's *locus* and *motility*.

### Barycenter *locus*
This is a measure of where $B_{avg}$ falls relative to the center of mass of the primaron:
- $B_{avg} \le R_P$: the barycenter locus is *interior*.
- $B_{avg} > R_P$: the barycenter locus is *exterior*.

### Barycenter *motility*
This is a measure of the values of $B_{min}$ and $B_{max}$ to the primaron's center-of-mass, and there are *three* possible configurations:
1. $B_{max} \le R_P$: the barycenter's motility is *confined*; no part of the barycenter's orbit extends beyond the physical volume of the primaron; because $B_{min} \;\cdot\!\!< B_{max}$, there's no need to specify its relationship to the primaron's center of mass in this case.
2. $B_{min} \le R_P$ and $B_{max} \ge R_P$: the barycenter's motility is *ambulatory*; part of the barycenter's orbit extends beyond the physical volume of the primaron.
3. $B_{min} > R_P$: the barycenter's motility is *free*; no part of the barycenter's orbit extends into the physical volume of the primaron; because $B_{max} \;\cdot\!\!> B_{min}$, there's no need to specify its relationship to the primaron's center of mass in this case.

#### Combining *locus* and *motility*
The combination of locus and motility result in *four* possible configurations:
- If $B_{max} < R_P$, then by definition $B_{avg} < R_P$, and the barycenter configuration is
   *interior confined*.
- If $B_{min} > R_P$, then by definition $B_{avg} > R_P$, and the barycenter configuration is *exterior free*.
- If $B_{avg} \le R_P$ (by definition $B_{min} < R_P$) and $B_{max} > R_P$, then the barycenter configuration is *interior ambulatory*.
- If $B_{avg} > R_P$ (by definition $B_{max} > R_P$), and $B_{min} \le R_P$, then the barycenter configuration is *exterior ambulatory*.

$$
\begin{array}{l|l|l|l}
\textbf{Locus} & \textbf{Motility} & \textbf{Configuration} & \textbf{Barycenter Position} \\[0.1em]
\hline\\[-1em]
\text{Interior} & \text{Confined} & \textbf{Interior–Confined} & 
\text{Within the primaron.} \\[0.3em]
\text{Interior} & \text{Ambulatory} & \textbf{Interior–Ambulatory} & 
\text{Orbit crosses primaron’s surface.} \\[0.3em]
\text{Exterior} & \text{Ambulatory} & \textbf{Exterior–Ambulatory} &
\text{Orbit crosses primaron’s surface.} \\[0.3em]
\text{Exterior} & \text{Free} & \textbf{Exterior–Free} &
\text{Outside the primaron.}
\end{array}
$$
$$
\begin{array}{c|c|c}
\textbf{Motility} &
\text{Locus Interior }(B_{avg} \le R_P) &
\text{Locus Exterior }(B_{avg} > R_P)\\[0.5em]
\hline\\[-2pt]
\text{Confined} & B_{min} < B_{avg} < B_{max} \le \mathbf{R_P} & --\\[0.5em]
\text{Ambulatory} &
B_{min} < B_{avg} \le \mathbf{R_P} < B_{max} &
B_{min} \le \mathbf{R_P} < B_{avg} < B_{max}\\[0.5em]
\text{Free} & -- & \mathbf{R_P} \le B_{min} < B_{avg} < B_{max}
\end{array}
$$

This schema yields eight possible **duramonic pairings**, grouped by mass ratio:
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

By contrast, if **Uranus** were in orbit around **Jupiter**, it would *not* be a moon (parensate) but a **sobrinate**, because the primaron mass ratio between the two is less than 100 : 1:

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