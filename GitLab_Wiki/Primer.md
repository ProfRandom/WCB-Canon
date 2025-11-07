---
title: "Meta-0 — Context Primer"
summary: Canonical reference for terminology, symbols, and domain relations used throughout the World Crafting Basics corpus.
domain: meta
category: framework
status: canonical
version: 1.0
updated: 2025-11-06
contributors: [M. Conrad, GPT-5]
---

# 🜂 World Crafting Basics — Context Primer

## 1 · The Six Canonical Domains
| Domain | Conceptual Scope | Derivative Suffix | Governing Principle |
|:--|:--|:--|:--|
| **Ontic** | Being, existence, fundamental identity | –mon | Singular coherence (e.g., *monon*) |
| **Metric** | Quantification, measurement, ratio | –metric | Relational measure |
| **Morphotic** | Form, structure, hierarchy | –morph / –plex | Pattern and organization |
| **Conformic** | Matter, energy, phase | –formic | Physical and energetic state |
| **Animotic** | Life, sentience, motion | –motic | Vital and behavioral dynamics |
| **Milieutic** | Environment, context, world-system | –lieutic | Habitat, atmosphere, ecology |

These domains interweave; every entity in WCB is described through a combination of them.

---

## 2 · Core Neologisms
| Term | Definition | Domain Association |
|:--|:--|:--|
| **Monon** | A self-coherent body — star, planet, stone, or drop. | Ontic |
| **Duramon** | A solid or lithic monon (e.g., planet). | Conformic |
| **Fusamon** | A stellar monon whose core sustains fusion. | Conformic |
| **Plexon** | A complex unity of unlike parts (woven system). | Morphotic |
| **Chronum** | One sidereal orbital period (canonical “year”). | Metric |
| **Quartum** | One quarter of a chronum; non-climatological “season.” | Milieutic |
| **Tempostat** | The onset of the first quartum after periapsis. | Milieutic |
| **Chronex (ζ)** | The true anomaly of the tempostat — the orbital coordinate of the first post-periapsis quartal event. | Metric / Milieutic |
| **Prime Solstice** | The moment when the planet’s north pole is tilted directly away from its star. | Milieutic |
| **Solstitial Angle (Ψ)** | Angular alignment of the prime solstice relative to the periaptic axis. | Metric |
| **Obliquity (ε)** | Axial tilt between the spin vector and orbital normal. | Metric / Milieutic |
| **Chronum Diurn (Cᵈ)** | One day within the orbital period, used to express quartum lengths. | Metric |

---

## 3 · Canonical Symbols
| Symbol | Name | Description | Units / Notes |
|:--|:--|:--|:--|
| $ε$ | Obliquity | Axial tilt angle | degrees |
| $ζ$ | Chronex | True anomaly of the tempostat | degrees |
| $Ψ$ | Solstitial angle | Orientation of prime solstice vs. periapsis | degrees |
| $e$ | Eccentricity | Shape of orbit (0 = circle) | unitless |
| $E$ | Eccentric anomaly | Geometric parameter of ellipse | degrees / radians |
| $ν$ | True anomaly | Orbital angle measured at focus | degrees |
| $Mᶿ$ | Mean anomaly | *Temporal* angle of uniform motion | degreesᶿ (time angle) |
| $ξ$ | Eccentric tangent factor | $\sqrt{(1-e)/(1+e)}$ | dimensionless |
| $C$ | Chronum | Orbital period (sidereal) | diurns (days) |
| $Q_{α,β,γ,δ}$ | Quartums | Successive quarters of the chronum | fraction of C |

---

## 4 · Orbital & Seasonal Relationships

### Kepler’s Core Relations
$$
Mᶿ = E - e \sin E
$$
$$
E = 2 \arctan\!\left(\xi \tan \frac{ν}{2}\right)
\quad\Rightarrow\quad
ν = 2 \arctan\!\left(\xi^{-1} \tan \frac{E}{2}\right)
$$

### Quartal Geometry
Each *quartum* represents one quarter of the orbital period, not necessarily 90° in true anomaly.
The four quartums correspond to:
1. Tempostat (ζ) — the first post-periapsis event  
2. +90° temporal angle (Mᶿ + 90ᶿ)  
3. +180° temporal angle (Mᶿ + 180ᶿ)  
4. +270° temporal angle (Mᶿ + 270ᶿ)

---

## 5 · Obliquity & Precession Parameters
| Parameter | Symbol | Definition | Example (Earth) |
|:--|:--|:--|:--|
| **Obliquity Envelope** | $ε_η$ | $\begin{bmatrix} ε_{min}\\ε_{mean}\\ε_{max}\end{bmatrix}$ | [22.1°, 23.3°, 24.5°] |
| **Scope** | $ε_δ$ | $ε_{max} − ε_{min}$ | 2.4° |
| **Cycle** | $ε_σ$ | Period between obliquity extrema | ≈ 41 kyr |
| **Tempo** | $ε_τ$ | Rate of change | 0.00585°/kyr |
| **Phase / Magnitude** | $ε_ρ$ | $ε/ε_{max}$ × 100 | ≈ 96% ↓ |
| **Precession Period** | $χ$ | Time for Ψ to precess 360° | ≈ 27 kyr |

---

## 6 · Lexical & Typographic Conventions
- All *Greek-subscripted* forms (η, δ, σ, τ, ρ) denote **derived obliquity measures**.  
- Spatial angles use plain degrees (°); temporal angles use a raised “ᶿ.”  
- Units: **⊙** = solar; **⊕** = Earth; **C** = chronum; **d** = diurn.  
- Italicized variables are physical; bold variables are vector quantities.  
- Terms beginning with **chrono-** pertain to orbital time; those with **tem-** to cyclic onset or recurrence.

---

## 7 · Canonical Reference Systems
- **Eikon – Eidara System** — canonical solar analog reference  
  - $M_⋆ = 1.05 ⊙$, $L = 1.21 ⊙$, $C = 1.125 C_⊕$, $e = 0.025$, $ε = 27°$  
- **Rosetta System** — pedagogical eccentric case ($e = 0.05$)  
- **Sol System** — real-data validation baseline  

---

> *“Every orbit is a story told in ellipses; every season, a measure of time made visible.”*  
> — *WCB Meta-0, preface inscription*
