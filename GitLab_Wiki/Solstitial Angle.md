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

This is directly related to the **Solstitial Angle** ($\Psi$).

## Solstitial Angle ($\Psi$)  

The **solstitial angle** describes the angular alignment of a monon’s *precessional orientation* relative to its orbit’s **periaptic axis**.  
It is defined as the angle between **periapsis** (the line of apsides) and the direction in the orbital plane where the planet’s projected **north pole is tilted directly away** from its star — the ***prime solstice***.  

$$
\begin{array}{l r l}
\Psi = &0^\circ &\text{periaptic zero: the prime solstice occurs at periastron} \\
\Psi = &90^\circ &\text{the solstitial alignment has precessed $90^\circ$ along the orbit} \\
\Psi = &180^\circ &\text{the prime solstice occurs at apastron} \\
\Psi = &270^\circ &\text{the solstitial alignment has precessed $270^\circ$ forward along the orbit} \\
\end{array}
$$

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

## Solstitial Angle Precession Period (???)  

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