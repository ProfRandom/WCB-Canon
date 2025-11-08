---
title: "Orbits–0 — Orbital and Seasonal Primer"
summary: Foundational framework for interpreting orbital divisions, anomalies, and seasonal approximations within WCB.
domain: metric
category: framework
status: canonical
version: 1.0
updated: 2025-11-08
contributors: [M. Conrad, GPT-5]
---

# 🜂 Orbital and Seasonal Primer

## 1 · Quarta and Secta

In WCB, the orbital period (*chronum*, $\chi$) is divided two ways:

| Division | Nature | Symbol | Description |
|:--|:--|:--|:--|
| **Quartum** (pl. *quarta*) | *Temporal* — equal fractions of orbital **time** | Q₀…Q₃ | Represent the four quarters of the *chronum*; may differ in angular extent due to orbital eccentricity. |
| **Sectum** (pl. *secta*) | *Spatial* — equal divisions of orbital **angle** | ς₀…ς₃ | Represent four 90° sectors of **true anomaly**, dividing the ellipse into geometric quarters. |

Thus, **secta** describe *where* the body is, while **quarta** describe *when* during the orbit it occurs.  
At zero eccentricity, quarta and secta coincide; as eccentricity rises, they diverge.

---

## 2 · Canonical Relationships

| Parameter | Symbol | Definition |
|:--|:--|:--|
| **True Anomaly** | \(ν_n = (ζ + 90n) \bmod 360°\) | Defines the angular loci (secta) for quartal boundaries. |
| **Eccentric Tangent Factor** | \(ξ = \sqrt{\frac{1 - e}{1 + e}}\) | Relates true and eccentric anomalies. |
| **Eccentric Anomaly** | \(E = 2 \arctan(ξ\tan\frac{ν}{2})\) | Projects true anomaly onto the auxiliary circle. |
| **Mean Anomaly** | \(M = E - e\sin E\) | Converts geometry to uniform time; basis for quartum fractions. |

---

## 3 · Seasonal Geometry

Each quartum \(Q_n\) spans one-quarter of the chronum, but not necessarily 90° in true anomaly.  
The quartum boundaries are offset by the **chronex (ζ)** — the true anomaly of the *tempostat*, the first cardinal event following periapsis.

\[
\nu_n = (ζ + 90n) \bmod 360
\]

For Earth, \(ζ ≈ 77°\); for the Rosetta model, \(ζ = 180°\).

---

## 4 · Practical Simplifications

### 4.1 Sidereal Quartum Durations
The **Eccentric Anomaly Method** provides reliable sidereal season lengths within 1% accuracy for low-eccentricity orbits.  
Example (Earth):  
| Quartum | Fraction | Duration (sidereal) | |
|:--|:--|--:|:--|
| Q₀ | 0.252 | 92.0 d | Spring |
| Q₁ | 0.253 | 92.5 d | Summer |
| Q₂ | 0.248 | 90.6 d | Autumn |
| Q₃ | 0.247 | 90.1 d | Winter |

---

### 4.2 Tropical Approximation (Calendrical)
Because precession causes the tropical year to drift slightly shorter than the sidereal year, sidereal season lengths can be adjusted by ±1 day to emulate tropical values:

| Quartum | Adjustment | Rationale |
|:--|--:|:--|
| Q₀ (spring) | +1 day | Precessional advance of equinox |
| Q₁ (summer) | +1 day | Forward phase lead |
| Q₂ (autumn) | –1 day | Retrograde lag |
| Q₃ (winter) | –1 day | Retrograde lag |

This heuristic correction yields tropical season durations accurate to within a few hours.

> *For most worldbuilding purposes, the sidereal results alone are sufficient — who’s going to argue?*  
> *Mundus tuum est.*

---

## 5 · Precessional Ratio (Optional Refinement)

When a world’s precession period \(χ\) is known, the tropical–sidereal relationship may be refined:

\[
p = \frac{C}{χ}, \qquad C_{trop} = C_{sid}^{1+p}.
\]

For Earth, \(C = 1\) yr, \(χ ≈ 26{,}000\) yr, giving \(p ≈ 3.85×10^{-5}\).  
The effect is negligible for long-precession systems and becomes meaningful only for rapid axial precession (≲10³ orbits).

---

## 6 · Notes on Notation

- \(Ψ\) remains reserved for the **solstitial angle** (orientation of the solstice axis relative to periapsis).  
- \(χ\) (chi) denotes the **precession period** — formerly “ψ” in draft notes.  
- \(ς\) (final sigma) designates **sectal indices**: \(ς₀, ς₁, ς₂, ς₃\).  
- Quartum indices \(Q₀–Q₃\) remain temporal by definition.  

---

> *“Equal distances in unequal times — the rhythm of a year made visible.”*  
> — *WCB Orbits–0 inscription*
