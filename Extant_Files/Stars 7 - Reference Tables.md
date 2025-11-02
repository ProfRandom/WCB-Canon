---
title: *Stars 6 — Reference Tables*
---

## 1 Spectral Class Temperature Ranges

| Spectral Class | Low K | High K | Thermal Interval Constant (þ K) |
|:--:|:--:|:--:|:--:|
| O | 25 000 | 55 000 | 3 000 |
| B | 10 000 | 25 000 | 1 500 |
| A | 7 500 | 10 000 | 250 |
| F | 6 000 | 7 500 | 150 |
| G | 5 000 | 6 000 | 100 |
| K | 3 500 | 5 000 | 150 |
| M | 2 400 | 3 500 | 110 |
| L | 1 300 | 2 400 | 110 |
| T | 600 | 1 300 | 70 |
| Y | 300 | 600 | 30 |

## 2 Solar-Relative Parameters by Spectral Class

| SC | K (mean) | T⊙ | R⊙ | L⊙ | M⊙ | Q⊙ (lifetime vs Sun) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| O | 40 000 | 6.90 | 12.4 | 3.5 × 10⁵ | 13.7 | 6.7 × 10⁻⁴ |
| B | 17 500 | 3.02 | 5.43 | 2.4 × 10³ | 5.97 | 6.6 × 10⁻² |
| A | 8 750 | 1.51 | 2.72 | 38.2 | 2.99 | 0.28 |
| F | 6 750 | 1.16 | 2.09 | 8.05 | 2.30 | 0.84 |
| G | 5 500 | 0.95 | 1.71 | 2.36 | 1.88 | 2.10 |
| K | 4 250 | 0.73 | 1.32 | 0.50 | 1.45 | 12.5 |
| M | 2 950 | 0.51 | 0.92 | 0.056 | 1.01 | 82.4 |

> *All quantities are rounded to two significant figures; the spread between “high” and “low” subclass values is typically ±15–25 %.*

## 3 Quick-Reference Equations

| From | To | Formula (approximate) |
|:--:|:--:|:--|
| Temperature (T) | Luminosity (L) | $L = T^{7.6}$ |
| Temperature (T) | Mass (M) | $M = T^{2.0}$ |
| Temperature (T) | Radius (R) | $R = T^{1.8}$ |
| Temperature (T) | Lifetime (Q) | $Q = T^{-5}$ |
| Luminosity (L) | Temperature (T) | $T = L^{1/7.6}$ |
| Luminosity (L) | Mass (M) | $M = L^{1/3.8}$ |
| Mass (M) | Radius (R) | $R = M^{0.9}$ |
| Mass (M) | Lifetime (Q) | $Q = M^{-2.5}$ |
| Kelvin (K) ↔ Solar (T) | $T = K / 5800$ and $K = 5800 T$ |

## 4 Thermozone Boundaries (normalized to N = 1.0)

| Label | Orbit Multiple (×N) | Animozone | Common Name |
| :---: | :-----------------: | :---------------------------- | :------------------- |
| H₀ |        0.500        | Inner Xenotic | Igniozone |
| H₁ |        0.750        | Inner Parahabitable | Calorozone |
| H₂ |        0.950        | Inner Habitable | Heliozone |
| H₃ |        1.385        | Hospitable | Solarazone |
| H₄ |        1.770        | Outer Habitable | Hiberozone |
| H₅ |        4.850        | Outer Parahabitable / Xenotic | Brumazone → Cryozone |

## 5 Symbol Index (Stars Modules 1–5)

| Symbol | Meaning | Units / Scale                |
|:--:|:--|:--|
|   K    | Surface temperature | Kelvin (K)                   |
|   T    | Relative temperature | Solar units (⊙ = 1.0)        |
|   M    | Mass | Solar masses (⊙)             |
|   R    | Radius | Solar radii (⊙)              |
|   L    | Luminosity | Solar luminosities (⊙)       |
|   Q    | Lifetime | Solar lifetimes (⊙)          |
|   þ    | Thermal Interval Constant | Kelvin per spectral subclass |
|   κ    | Upper temperature bound of class | K                            |
|   𝓢   | Spectral type number | 0–9 (continuous)             |
|   N    | Nucleal orbit | AU                           |
|   P   | Perannual orbit | AU                           |
| H₀–H₅  | Thermozone limits | AU (N�)                      |
|  OHI   | Orbital Habitability Index | 0–1 scalar                   |

## 6 Usage Notes
This reference file is designed for direct consultation during world-modeling. All tables and exponents reflect the **WCB linearized stellar framework** used across the *Stars 1–5* modules. Values may differ slightly from canonical astrophysical data; they are optimized for internal consistency and symbolic clarity within the WCB cosmology.
