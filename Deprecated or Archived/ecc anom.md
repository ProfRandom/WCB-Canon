The **eccentric anomaly**, $E$, is an angular coordinate that describes a body’s position along an **elliptical orbit** in a way that keeps Kepler’s equation simple.

Imagine a circle drawn around the ellipse with the same center and major axis. If you project the planet’s position *up* to that circle by a line drawn perpendicular to the major axis, the angle at the center of the ellipse between that line and the direction of periastron is the **eccentric anomaly**.

In other words:

- The *true anomaly* ($ν$) is the angle measured **from the focus** — subtending the arc from periastron to the planet itself.  
- The *eccentric anomaly* ($E$) is measured **from the center** — subtending the arc from periastron to the projected point on the reference circle.  
- The *mean anomaly* ($\textit{Ⳁ}$) increases uniformly with time and connects to $E$ through Kepler’s Equation:

$$
\textit{Ⳁ} = E - (e\,\sin E)
$$

The eccentric anomaly acts as the mathematical bridge between the **uniform time variable** ($\textit{Ⳁ}$) and the **actual orbital position** ($ν$).  It allows us to calculate how much of the orbital period has elapsed at any given geometric position — even when the orbit is not circular.