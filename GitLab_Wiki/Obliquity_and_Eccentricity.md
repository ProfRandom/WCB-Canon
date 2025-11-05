---
title: 
---

# Obliquity — Planetary Orientation

*Throughout WCB, derived obliquity parameters are denoted by Greek subscripts: η (envelope), δ (scope), σ (cycle), τ (tempo), μ (magnitude).*


## Orientation of the Orbital Normal

**Orbital Normal ( N )**
The vector perpendicular to the orbital plane, defined by the **right-hand rule**: when the fingers of the right hand curl in the direction of **orbital motion**, the extended thumb points toward **orbital north**. Formally:

$$
\mathbf{N} = \frac{\mathbf{r} \,\boldsymbol{\times}\, \mathbf{v}}{|\mathbf{r} \,\boldsymbol{\times}\, \mathbf{v}|}
$$

This establishes a concrete mathematical object, such that:

$$
\begin{array}{l c l}
	+ x &= &\text{barycenter} \rightarrow \text{periapsis} \\[0.25em]
 + y &= &\text{direction of motion \textit{at} periapsis} \\[0.25em]
	+ z &= &\mathbf{N}
\end{array}
$$

### Why the Right-hand Rule is Necessary

In an isotropic universe there’s no intrinsic “up,” “north,” or “clockwise.” Every plane in space has *two* equally valid perpendiculars, and they point in opposite directions. Without an external asymmetry (a magnetic field, angular momentum, etc.), you can’t say which one is “positive.”

The right-hand rule supplies that missing **orientation convention**:
* If you curl the fingers of your right hand in the direction of orbital motion,
* Your thumb points along the **positive normal** — the **orbital north**.

This convention doesn’t imply that the cosmos *prefers* that direction; it merely provides a shared geometric rule so we can speak consistently about “north,” “tilt,” and “anticlockwise.”

## Defining Obliquity

Once $\mathbf{N}$ is defined, **obliquity** ($\varepsilon$) becomes an immediate vector relationship:

$$
\begin{gathered}
\\cos \varepsilon = \mathbf{s} \!\cdot\! \mathbf{N}, \\[1em]
\mathbf{s} =
\bigl(
\sin|\varepsilon| \cos\phi,\,
\sin|\varepsilon| \sin\phi,\,
\operatorname{sgn}(\varepsilon)\cos|\varepsilon|
\bigr)
\end{gathered}
$$

Where:
- $\phi$ = the **solstitial angle**, the angular offset of the spin-axis projection from the +x-axis (the barycenter–periapsis line) within the orbital plane.

This ties tilt, azimuth, and the coordinate frame together cleanly.

### Special Cases and Degeneracies
$$
\begin{array}{l l l}
	\textbf{Case} & \textbf{Meaning} & \textbf{Effect on N} \\
 \hline\\[-0.5em]
 e > 0 & \text{Elliptical orbit} & \textbf{N}\text{ well defined by motion vector.} \\
 e = 0 & \text{Circular orbit} & \textbf{N}\text{ still defined; orientation unaffected by lack of apsides.} \\
 \varepsilon = 0 & \text{No tilt} & \textbf{s = N}\text{; obliquity angle zero.} \\
 e = \varepsilon = 0 & \text{Isoseasonal system} & \textbf{N}\text{ defined; but spin and orbital normals coincide, no seasonal variation or preferred longitude.}
\end{array}
$$
When both e and ε vanish, the system becomes fully symmetric. The orbital normal $\textbf{N}$ remains defined, but there is no intrinsic direction within the orbital plane; any 0° longitude must be chosen arbitrarily or inherited from a higher-order reference frame.

This is directly related to the **Solstitial Angle** ($\Psi_n$).

## Solstitial Angle ($\Psi$)  

The **solstitial angle** describes the angular alignment of a monon’s *precessional orientation* relative to its orbit’s **periaptic axis**.  
It is defined as the angle between **periapsis** (the line of apsides) and the direction in the orbital plane where the planet’s projected **north pole is tilted directly away** from its star — the ***prime solstice***.  

- $\Psi = 0$ — *(periaptic zero)*: the northern solstice occurs at periastron.  
- $\Psi = 90$ — the solstitial alignment has precessed 90° forward along the orbit.  
- $\Psi = 180$ — the northern solstice occurs at apastron.  
- $\Psi = 270$ — the solstitial alignment has precessed 270° forward along the orbit.

For notational convenience, the solstitial angle is sometimes indicated by appending the angular measure as a subscript to the symbol, e.g. $\Psi_{90}$ is the same as $\Psi = 90^\circ$.

As axial precession proceeds, $\Psi$ increases anticlockwise with respect to the orbit, so solstices and equinoxes **precess relative to periastron and apastron**.

The **solstitial angle** thus tracks the *slow rotation of the solstitial alignment* around the orbital normal.

The **calendar seasons** remain fixed relative to the planet’s equinoxes and solstices, but their **orbital context** shifts steadily over the precessional cycle.  

This precession occurs for all planets with nonzero obliquity ($\varepsilon \neq 0$) and is independent of tilt magnitude — even an $\varepsilon = 90^\circ$ planet experiences the same drift, with its solstices alternating between periapsis and apastron alignment.  

### Canonical Cases for $\Psi$​  
$$
\begin{array}{l l l}
\textbf{Orbital / Axial State} & \textbf{Meaning} & \textbf{Effect on }\Psi_{(x)} \\[0.5em]
\hline\\[-0.5em]
e \neq 0,\, \varepsilon = 0 &
\text{Elliptical orbit without axial tilt.} &
\text{The orbit has a defined periapsis, but no solstices or equinoxes exist.}\\
&& \Psi_0 \text{ may be defined conventionally as the periapsis direction,}\\
&& \text{though it carries no physical seasonal meaning.}\\[0.75em]
e \neq 0,\, \varepsilon \neq 0 &
\text{Elliptical orbit with axial tilt.} &
\Psi \text{ measures the orbital longitude where the north pole is tilted away}\\
&& \text{from the star. } \Psi_0 \text{ corresponds to the periaptic solstice.}\\[0.75em]
e = 0,\, \varepsilon \neq 0 &
\text{Circular orbit with tilt.} &
\text{No physical periapsis exists; a } 0^\circ \text{ reference must be defined arbitrarily.}\\
&& \Psi \text{ is then measured relative to that direction.}\\[0.75em]
e = 0,\, \varepsilon = 0 &
\text{Circular orbit, no tilt.} &
\text{No solstices, equinoxes, or apsidal points exist. } \Psi \text{ is undefined,}\\
&& \text{unless an arbitrary 0° longitude is adopted for bookkeeping.}
\end{array}
$$
#### Relating $\Psi$ and $\nu$

$$
	\Psi_{prime} = \nu_{prime} \mod 360^\circ
$$

## Solstitial Angle Precession Period ($\chi$)  

The **solstitial precession period** ($\chi$) is the time required for the solstitial angle ($\Psi$) to complete one full $360^\circ$ precession around the orbit.  

- Defined such that $\Psi_{0}$ occurs when the planet’s north pole is tilted **away from the star** at periastron.  
- At $\Psi_{180}$, the north pole is tilted **toward the star** at periastron.  
- For Earth, $\chi \approx 27{,}000$ years.  

Thus, after about **13,000 years**, Earth’s northern summer will occur near December–February if the Gregorian calendar framework remains unchanged.  

> **Note:** $χ$ is undefined for $\varepsilon = 0$, since there is no obliquity to precess. Some analytical frameworks assign $χ = 0$ for bookkeeping, but this has no physical meaning.  

### Conceptual Summary  

> The **solstitial angle ($\Psi$)** specifies *where the prime solstice points* in space — its precessional alignment relative to the periaptic axis —  
> while the **obliquity orientation ($\zeta$)** specifies *where that solstice occurs* in the orbit.  
>  
> Together, they define both the **spatial** and **temporal** components of a planet’s seasonal geometry.  

## Obliquity Progression

Since obliquity is the **instantaneous angle** between a monon’s rotational axis and the perpendicular to its orbital plane, it is necessary to indicate how the current state of the obliquity is varying. An up arrow $\uparrow$ or down arrow $\downarrow$ may be appended after the angular measure to indicate whether the obliquity is increasing or decreasing. 

For Earth: 

$$
\varepsilon = 23.5^\circ\downarrow
$$
## Obliquity Envelope ($\varepsilon_\eta$) 

$$
\varepsilon_\eta =
\begin{bmatrix}
\varepsilon_{min} \\
\varepsilon_{mean} \\
\varepsilon_{max}
\end{bmatrix}
$$

Where: 
- $\varepsilon_x$ = current tilt angle 
- $\varepsilon_{min}$ = minimum obliquity 
- $\varepsilon_{mean}$ = mean obliquity 
- $\varepsilon_{max}$ = maximum obliquity 

Example (Earth): 

$$
\varepsilon_\eta = 
\begin{bmatrix}
22.1^\circ \\
23.3^\circ \\
24.5^\circ
\end{bmatrix}
$$

## Obliquity Scope ($\varepsilon_\delta$)

Simply the difference between the maximum and minimum obliquity extents:

$$
\varepsilon_\delta = \varepsilon_{max} - \varepsilon_{min}
$$

For Earth:

$$
\varepsilon_\delta = 24.5^\circ - 22.1^\circ = 2.4^\circ
$$

## Obliquity Cycle ($\varepsilon_\sigma$) 

The time interval between two maxima (or minima) of obliquity. 

For Earth: 

$$
\varepsilon_\sigma \approx 41{,}000 \text{ years}
$$

## Obliquity Tempo ($\varepsilon_\tau$) 

Rate of obliquity change per year (chronum): 

$$
\varepsilon_\tau = \dfrac{\varepsilon_{max} - \varepsilon_{min}}{\varepsilon_\sigma}
$$

For Earth: 

$$
\varepsilon_\tau = \frac{24.5 - 22.1}{41000} ≈ 0.0000585^\circ/\text{yr} \;=\; 0.00585^\circ/\text{kyr}
$$
## Obliquity Magnitude ($\varepsilon_\mu$) 

The ratio of the current obliquity to its maximum value, expressed as a percentage, with an arrow showing whether the trend is increasing $\uparrow$ or decreasing $\downarrow$:

$$
\varepsilon_\mu = \dfrac{\varepsilon}{\varepsilon_{max}}\times 100 \; (\uparrow,\downarrow)
$$

For Earth: 

$$
\varepsilon_\mu = \dfrac{23.5}{24.5}\times 100 \approx 95.9\text{\%}\;\downarrow
$$

