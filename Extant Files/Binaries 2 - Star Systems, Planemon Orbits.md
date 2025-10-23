---
title: ""
---


## Abstract  
**Major Topics:**  
- Defines the **Chaos Zone** — the dynamically unstable region between circumstellar (S-type) and circumbinary (P-type) orbital regimes in binary systems.  
- Establishes the empirical stability range:  
  $$0.3\,\mathcal{A} \lesssim \alpha \lesssim 3.0\,\mathcal{A}$$  
  within which long-term planetary orbits are generally impossible.  
- Distinguishes between:  
  - **S-type orbits** — planets bound to one star of a wide binary.  
  - **P-type orbits** — planets orbiting both stars of a close binary.  
- Explains that orbital stability depends primarily on the **ratio of the planetary semi-major axis** ($\alpha$) to the **average stellar separation** ($\mathcal{A}$).  
- Summarizes **Holman & Wiegert (1999)** numerical results for circumbinary (P-type) stability, introducing the full empirical relation:  
  $$\frac{a_{crit}}{\mathcal{A}} = 1.60 + 5.10e - 2.22e^2 + 4.12\mu - 4.27e\mu - 5.09\mu^2 + 4.61e^2\mu^2$$  
  and the simplified canonical form:  
  $$\alpha \ge \mathcal{F}(e)\,\mathcal{A}, \qquad \mathcal{F}(e) = 4.1e^2 + 2.0e + 3.5$$  
- Provides tabulated $\mathcal{F}(e)$ values for typical binary eccentricities, showing that stability boundaries rise roughly quadratically with $e$.  
- Notes a simplified linear approximation ($\alpha >rsim \mathcal{A}(3.5 + 4.0e)$) for rapid estimation.  
- Incorporates **Quarles et al. (2018, 2020)** results defining the **S-type stability limit** for wide binaries:  

$$
\mathcal{Q}_{L} = 0.08 \qquad \mathcal{A} = 0.08 \left(\frac{T_{min}}{1 - e}\right)
$$

  —  linking circumstellar orbital stability directly to the stars’ *closest approach* ($T_{\min}$).  
- Introduces the **Quarles Eccentricity Limit** ($\mathcal{Q}_e = 0.92$), the maximum binary eccentricity at which *any* stable circumstellar orbit can exist.  
- Emphasizes that the **inner and outer stability boundaries** (Holman–Wiegert vs. Quarles) form the **complete architecture of binary orbital habitability**.

**Key Terms & Symbols:**  
- **$\mathcal{A}$** — average stellar separation (AU).  
- **$\alpha$** — planetary orbital semi-major axis (AU).  
- **$a_{crit}$** — critical semi-major axis for P-type stability.  
- **$T_{\min}$** — minimum stellar separation at periastron.  
- **$e$** — binary eccentricity.  
- **$\mu$** — binary mass ratio ($M_2 / (M_1 + M_2)$).  
- **$\mathcal{F}(e)$** — stability function for circumbinary (P-type) orbits.  
- **$\mathcal{Q}_L$** — Quarles Stability Limit (outer boundary for S-type).  
- **$\mathcal{Q}_e$** — Quarles Eccentricity Limit (max $e$ for circumstellar stability).  

**Cross-Check Notes:**  
- Complements **Binaries 2 — Star Systems, General** by extending from stellar–stellar dynamics to **planetary–binary interactions**.  
- Provides quantitative criteria for **stable orbital zones** around and within binary systems.  
- Serves as the foundation for later sections on **Roche geometry**, **Hill spheres**, and **habitable zone modeling** in multi-star environments.  

## Chaos Zone
$$
0.3\,\mathcal{A} \lesssim \alpha \lesssim 3.0\,\mathcal{A}
$$
Where:
- $\alpha$ = semi-major axis of the planemon’s orbit (AU)
- $\mathcal{A}$ = average separation between the two stars (AU)

For clarity:
- If the ratio $\alpha/\mathcal{A}$ for a **close-binary** is less than 0.3, a circumstellar (S-type) orbit cannot remain stable.
- If the ratio $\alpha/\mathcal{A}$ for a **wide-binary** is greater than 3.0, a circumbinary (P-type) orbit cannot remain stable.

## P-type Orbit (around both stars in a close-binary)
$$
\alpha >r\sim 3.0\,\mathcal{A}
$$
### Deep Dive: The Empirical Stability Relation
Numerical simulations (Holman & Wiegert 1999, *AJ* 117:621) yield a widely used fit for **circumbinary (P-type)** stability:

$$
\frac{a_{\text{crit}}}{\mathcal{A}}
  = 1.60 + 5.10e - 2.22e^2
    + 4.12\mu - 4.27e\mu
    - 5.09\mu^2 + 4.61e^2\mu^2
$$
Where:
- $a_{\text{crit}}$ = inner edge of stable circumbinary orbits  
- $\mathcal{A}$ = binary semi-major axis  
- $e$ = binary orbital eccentricity  
- $\mu = M_2/(M_1 + M_2)$ = binary mass ratio

This (mercifully) can be simplified to:

$$
\alpha \ge \mathcal{F}(e)\,\mathcal{A},
\qquad
\mathcal{F}(e) = 4.1e^2 + 2.0e + 3.5
$$
$$
\begin{array}{c|c|c}
e & \mathcal{F}(e) & a/\mathcal{A} \\[0.25em]
\hline
0.0 & 3.5 & 3.5\times\\
0.5 & 4.7 & 4\text{–}5\times\\
0.7 & 6.2 & 6\times
\end{array}
$$
> **Rule of thumb:** circumbinary (P-type) planets remain stable when  $\displaystyle\alpha >rsim \mathcal{F}(e)\;\mathcal{A}$ , rising roughly quadratically with binary eccentricity.

A quicker (but less precise) linear form is:

$$
\alpha >r\sim \mathcal{A}\,(3.5 + 4.0e)
$$
## S-type Orbit (around one star in a wide binary)
$$
\alpha \lesssim 0.3\,\mathcal{A}
$$

#### Quarles Stability Limit ($\mathcal{Q}_L$)
$$
\mathcal{Q}_L = 0.08\,\mathcal{A}
             = 0.08\!\left(\frac{T_{\min}}{1 - e}\right)
$$
Where:
- $\mathcal{Q}_{L}$ = maximum stable circumstellar orbital radius (S-type)
- $\mathcal{A}$ = average binary separation (defined from periastron)
- $T_{\min}$ = minimum stellar separation at periastron  
- $e$ = binary eccentricity  

> This expression emphasizes that stability depends primarily on the *closest approach* between the stars, which defines the maximum perturbation on circumstellar orbits.

If $T_{\min}$ and $\mathcal{Q}_L$ are known, the system eccentricity follows from:

$$
e = 1 - 0.08\!\left(\frac{T_{\min}}{\mathcal{Q}_L}\right)
$$

#### Quarles Eccentricity Limit ($\mathcal{Q}_e$)
$$
e \le \mathcal{Q}_e = 0.92
$$
- $\mathcal{Q}_e$ is the maximum binary eccentricity that still allows any stable circumstellar orbit, such that $T_{\min} ≥ \mathcal{Q}_L$.
