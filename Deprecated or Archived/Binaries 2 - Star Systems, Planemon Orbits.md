---
title: ""
---


## Chaos Zone
$$
0.3\,A \lesssim \alpha \lesssim 3.0\,A
$$
Where:
- $\alpha$ = semi-major axis of the planemon’s orbit (AU)
- $A$ = average separation between the two stars (AU)

For clarity:
- If the ratio $\alpha/A$ for a **close-binary** is less than 0.3, a circumstellar (S-type) orbit cannot remain stable.
- If the ratio $\alpha/A$ for a **wide-binary** is greater than 3.0, a circumbinary (P-type) orbit cannot remain stable.

## P-type Orbit (around both stars in a close-binary)
$$
\alpha >r\sim 3.0\,A
$$
### Deep Dive: The Empirical Stability Relation
Numerical simulations (Holman & Wiegert 1999, *AJ* 117:621) yield a widely used fit for **circumbinary (P-type)** stability:

$$
\frac{a_{\text{crit}}}{A}
  = 1.60 + 5.10e - 2.22e^2
    + 4.12\mu - 4.27e\mu
    - 5.09\mu^2 + 4.61e^2\mu^2
$$
Where:
- $a_{\text{crit}}$ = inner edge of stable circumbinary orbits  
- $A$ = binary semi-major axis  
- $e$ = binary orbital eccentricity  
- $\mu = M_2/(M_1 + M_2)$ = binary mass ratio

This (mercifully) can be simplified to:

$$
\alpha \ge F(e)\,A,
\qquad
F(e) = 4.1e^2 + 2.0e + 3.5
$$
$$
\begin{array}{c|c|c}
e & F(e) & a/A \\[0.25em]
\hline
0.0 & 3.5 & 3.5\times\\
0.5 & 4.7 & 4\text{–}5\times\\
0.7 & 6.2 & 6\times
\end{array}
$$
> **Rule of thumb:** circumbinary (P-type) planets remain stable when  $\displaystyle\alpha >rsim F(e)\;A$ , rising roughly quadratically with binary eccentricity.

A quicker (but less precise) linear form is:

$$
\alpha >r\sim A\,(3.5 + 4.0e)
$$
## S-type Orbit (around one star in a wide binary)
$$
\alpha \lesssim 0.3\,A
$$

#### Quarles Stability Limit ($Q_L$)
$$
Q_L = 0.08\,A
             = 0.08\!\left(\frac{T_{\min}}{1 - e}\right)
$$
Where:
- $Q_{L}$ = maximum stable circumstellar orbital radius (S-type)
- $A$ = average binary separation (defined from periastron)
- $T_{\min}$ = minimum stellar separation at periastron  
- $e$ = binary eccentricity  

> This expression emphasizes that stability depends primarily on the *closest approach* between the stars, which defines the maximum perturbation on circumstellar orbits.

If $T_{\min}$ and $Q_L$ are known, the system eccentricity follows from:

$$
e = 1 - 0.08\!\left(\frac{T_{\min}}{Q_L}\right)
$$

#### Quarles Eccentricity Limit ($Q_e$)
$$
e \le Q_e = 0.92
$$
- $Q_e$ is the maximum binary eccentricity that still allows any stable circumstellar orbit, such that $T_{\min} ≥ Q_L$.
