---
title: Meta 3 — Mass Domains
summary: Defines symbolic and numerical mass intervals relative to Earth mass (⨁), including the microterran subscale for small-mass bodies.
domain: meta
category: nomenclature
tags: [mass, terran, units, scales, prefixes]
vocabulary: [terran, microterran, duramon, scale, mass-domain]
updated: 2025-10-25
status: canonical
version: 1.0
related: [Meta 2 — Math Tools, Meta 1 — Units and Measures, Duramons 1 — Classification]
contributors: [M. Conrad]
source: https://gitlab.com/wcbcanon/meta
---

# Introduction

The following conventions establish how **World Crafting Basics (WCB)** names and interprets mass intervals relative to Earth’s mass ($\oplus$).

These ensure that both scientific notation and symbolic terminology remain intuitive across a vast range of scales.

## Contents
1. Mass Domains
3. Mathematical or Structural Section (if applicable)
4. Applications or Examples (if applicable)
5. Terminology/Lexicon Section
6. Crosslinks/Internal References Section
7. Version/Contributor Notes
8. External References Section (if applicable)

## Mass Domains
$$
\begin{array}{l c r r r}
\textbf{Intervals} &
\textbf{Abbr.} &
\textbf{Min. Mass} \ge &
\textbf{Max. Mass} < &
\textbf{Power} \\[3pt]
\hline
\text{deniterran}  & \text{dn} & 0.0000000001 & 0.000000001   & 10^{-10} \\
\text{nanoterran}  & \text{n}  & 0.000000001  & 0.00000001    & 10^{-9}  \\
\text{oktiterran}  & \text{ok} & 0.00000001   & 0.0000001     & 10^{-8}  \\
\text{septiterran} & \text{sp} & 0.0000001    & 0.000001      & 10^{-7}  \\
\text{microterran} & \mu t     & 0.000001     & 0.00001       & 10^{-6}  \\
\text{pentiterran} & \text{pn} & 0.00001      & 0.0001        & 10^{-5}  \\
\text{demiterran}  & \text{dm} & 0.0001       & 0.001         & 10^{-4}  \\
\text{milliterran} & \text{m}  & 0.001        & 0.01          & 10^{-3}  \\
\text{centiterran} & \text{c}  & 0.01         & 0.1           & 10^{-2}  \\
\text{deciterran}  & \text{d}  & 0.1          & 1             & 10^{-1}  \\
\text{terran}      & \text{t}  & 1            & 10            & 10^{0}   \\
\text{dekaterran}  & \text{da} & 10           & 100           & 10^{1}   \\
\text{hectoterran} & \text{h}  & 100          & 1000          & 10^{2}   \\
\text{kiloterran}  & \text{k}  & 1000         & 10000         & 10^{3}   \\
\text{myriaterran} & \text{Mr} & 10000        & 100000        & 10^{4}   \\
\text{hexaterran}  & \text{Hx} & 100000       & 1000000       & 10^{5}   \\
\text{megaterran}  & \text{Mt} & 1000000      & 10000000      & 10^{6}   \\
\text{heptoterran} & \text{Hp} & 10000000     & 100000000     & 10^{7}   \\
\text{octoterran}  & \text{Oc} & 100000000    & 1000000000    & 10^{8}   \\
\text{gigaterran}  & \text{Gt} & 1000000000   & 10000000000   & 10^{9}   \\
\text{denoterran}  & \text{Dd} & 10000000000  & 100000000000  & 10^{10}  \\
\text{ondoterran}  & \text{On} & 100000000000 & 1000000000000 & 10^{11}  \\
\text{teraterran}  & \text{T}  & 1000000000000 & 10000000000000 & 10^{12} \\
\text{triskaterran}& \text{Tr} & 10000000000000 & 100000000000000 & 10^{13} \\
\text{quadraterran}& \text{Qd} & 100000000000000 & 1000000000000000 & 10^{14} \\
\text{petaterran}  & \text{Pt} & 1000000000000000 & 10000000000000000 & 10^{15} \\
\text{sexaterran}  & \text{Sx} & 10000000000000000 & 100000000000000000 & 10^{16} \\
\text{septaterran} & \text{St} & 100000000000000000 & 1000000000000000000 & 10^{17} \\
\text{exaterran}   & \text{Et} & 1000000000000000000 & 10000000000000000000 & 10^{18} \\
\end{array}
$$

1. Where official SI prefixes exist (e.g., *micro-*, *milli-*, etc.), **WCB** uses them directly.  
2. For intermediate powers without SI prefixes, **WCB** adopts consistent **neologisms** based on the exponent’s magnitude:  
   - Exponents **below zero** use an *-i* ending (unless overridden by SI, e.g., *micro-*, not *micri-*).  
   - Exponents **above zero** use an *-a* ending (unless overridden by SI, e.g., *mega-*, not *mego-*).  
3. While SI defines prefixes beyond *tera-* (*peta-*, *exa-*), **WCB** rarely uses them in monon contexts.  
   Even the observable universe spans only ≈ $46.5$ **giga**light-years (Gly) in radius — roughly three orders of magnitude below **teraterran** relevance.  
4. The **negative intervals** are symbolically essential: many moons, asteroids, and micro-monons fall far below $1 \oplus$ in mass.  
   It is often clearer to say  
   - “The body is $1 \text{microterran}\,(\mu\oplus)$”  
     than  
   - “The body is $0.000001 \oplus$.”  
5. For practical purposes, **WCB** defines the upper bound of each mass interval as **one demiterran** ($0.00001 \oplus$) below the next power of ten.  
   - Thus, the *terran* interval spans $1.0 \oplus ≤ M < 10 \oplus$.  
   - Any value exceeding that threshold — even slightly — **rounds up** to the next symbolic interval.  
     - **Example:** $9.999 990 1 \oplus → 10.0 \oplus$, placing the body in the **dekaterran** interval.  
6. The **deniterran** marks the lower limit of the scale; bodies smaller than this cannot achieve hydrostatic equilibrium.  
7. The **exaterran** marks the upper limit, approximating the realistic mass ceiling for Ultra-massive Black Holes (UMBHs), about $10^{12}\,M_\odot$.

## The Microterran Subscale

Because many **duramons** have masses best expressed as a **millionth of a terran** ($\mu \oplus$), WCB defines an optional *microterran subscale* for intuitive symbolic modeling.

This subscale maps cleanly to the standard symbolic intervals and absolute powers of ten.

$$
\begin{array}{l r r l r r r}
\textbf{$\mu$-Terran Scale} &
\textbf{Min. Mass} &
\textbf{Max. Mass} &
\textbf{Std. Scale} &
\textbf{Power} \\[3pt]
\hline\hline
\text{demimicro (dm$\mu$)}  & 0.0001 & 0.001  & \text{deniterran}  & 10^{-10} \\
\text{millimicro (m$\mu$)}  & 0.001  & 0.01   & \text{nanoterran}  & 10^{-9}  \\
\text{centimicro (c$\mu$)}  & 0.01   & 0.1    & \text{oktiterran}  & 10^{-8}  \\
\text{decimicro (d$\mu$)}   & 0.1    & 1      & \text{septiterran} & 10^{-7}  \\
\text{microterran ($\mu$)}  & 1      & 10     & \text{microterran} & 10^{-6}  \\
\text{dekamicro (da$\mu$)}  & 10     & 100    & \text{pentiterran} & 10^{-5}  \\
\text{hectomicro (h$\mu$)}  & 100    & 1000   & \text{demiterran}  & 10^{-4}  \\
\text{kilomicro (k$\mu$)}   & 1000   & 10000  & \text{milliterran} & 10^{-3}  \\
\text{myriamicro (Mr$\mu$)} & 10000  & 100000 & \text{centiterran} & 10^{-2}  \\
\text{quintamicro (Qn$\mu$)}& 100000 & 1000000& \text{deciterran}  & 10^{-1}  \\
\end{array}
$$

The microterran subscale preserves the same logarithmic spacing as the full terran sequence but simplifies relative comparisons for sub-planetary bodies — e.g., moons, asteroids, or micro-monons — within a single stellar system.

It improves readability and narrative clarity for small-mass bodies such as **Vesta**, **Miranda**, and **Ceres**.

- It is especially useful for monons with masses between $10^{-6}\oplus$ and $10^{-1}\oplus$, where decimal $\oplus$ values become visually dense or cognitively opaque.  
- This symbolic shorthand allows you to say:  
  > “Ceres is about $157$ **microterrans** ($157\,\mu t$)” instead of “Ceres is $0.000157\,\oplus$.”  
- However, even with this scaling, **fractional expressions remain common** at the lowest mass levels:  
  > “Miranda is approximately $0.001\,\mu t$ in mass” is still easier to read and parse than “Miranda is one **demimicroterran ($\text{dm}\mu$}** in mass.”

> **In short:** The $\mu t$ unit supports clarity without sacrificing scalar precision — a vital aid to both symbolic modeling and *thesiastic* storytelling.  While most useful in describing small-mass duramons, these subscale prefixes can be used wherever a scaling prefix is needed.

## Applications and Examples

$$
\begin{array}{lrll}
\textbf{Example Monon} & \textbf{Mass ($\oplus$)} & \textbf{Symbolic} & \text{Interval}\\
\hline\hline
\text{Miranda} & 0.0000076 & 7.60\text{\;dnt} & \text{deniterran}\\
\text{Ceres} & 0.000157 & 1.57 \text{\;dmt} & \text{demiterran}\\
\text{Luna} & 0.0123 & 1.23 \text{\;ct} & \text{centiterran}\\
\text{Proxima b} & 1.27	& 1.27\text{\;t} & \text{terran}\\
\text{Jupiter} & 317.8 & 3.18\text{\;ht} & \text{hectoterran}
\end{array}
$$

These examples illustrate how WCB notation maintains both intuitive scale and quantitative accuracy across ten orders of magnitude.

## Terminology

- **Terran (t):** Base mass unit equal to $1\oplus$ (Earth mass).
- **Duramon:** A solid-bodied natural satellite, moon, or asteroid.
- **Microterran (μt):** One millionth of a terran, or $10^{-6}\oplus$.
- **Interval:** Symbolic category denoting an order-of-magnitude mass range.
- **Subscale:** A scaled re-expression (e.g., microterran scale) that preserves logarithmic ratios within a domain.

## Crosslinks

## Version and Contributor Notes
- Version 1.0 — First canonical release (2025-10-24).  
- Concept, nomenclature, and interval definitions by M. Conrad.  
- Structural edits and SANC compliance verified against Meta 0 — WCB Style Guide.

## External References








