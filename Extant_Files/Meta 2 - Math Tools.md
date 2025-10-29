---
title: ""
---

## Abstract  
**Major Topics:**  
- Consolidates all mathematical and procedural conventions used across the Worldmaking Canon (WCB), forming a unified reference for equations, units, and symbolic notation.  
- Defines **core numerical systems**:  
  - Canonical units (⨁, ⊙, ⟂, 𝒫) for mass, luminosity, gravity, and orbital period.  
  - Scaling conventions for micro- to gigaterran magnitudes.  
- Introduces and standardizes **notation for proportionality, equivalence, and relational operators** (≈, ∝, ≡, ≤, ≥), establishing consistency across scientific and narrative texts.  
- Formalizes **range constraints** and **random assignment protocols** (`Rnd{x::y}`), formerly in *Monons 2*, for probabilistic or stochastic modeling of planetary and stellar parameters.  
- Defines canonical forms for **dimensional analysis**, **conversion constants**, and **rounding precision** in calculations involving luminosity, mass, and orbital ratios.  
- Outlines **hierarchies of mathematical context**:  
  - *Descriptive* (empirical correlations and symbolic shorthand).  
  - *Prescriptive* (model equations governing worldmaking mechanics).  
  - *Procedural* (algorithms or random generation rules for simulation).  
- Establishes the **cross-disciplinary role** of math tools in binding the physical, morphological, and systemic frameworks of WCB.

**Key Terms & Symbols:**  
- **Rnd{x::y}** — random assignment operator (uniform probability).  
- **⨁, ⊙, 𝒫, 𝒩** — canonical Earth, Sun, and orbital constants.  
- **≈, ∝, ≡, ≤, ≥** — standardized relational and equivalence operators.  
- **Ω** — limiting boundary value for a given system parameter.  
- **σ, μ, I** — statistical variance, mean, and interval metrics used in orbital analysis.  

**Cross-Check Notes:**  
- Complements *Meta 1 — Principles* by grounding symbolic consistency across Canon files.  
- Supersedes mathematical content previously embedded in *Monons 2 — Properties and Parameters*.  
- Provides the foundational grammar for all quantitative derivations used in *Orbits*, *Binaries*, and *Stars* modules.  
- No new glossary terms required; consolidates and harmonizes prior notation.

# 🧭 Ellipse Geometry Solver — WCB Reference

This reference provides a complete algebraic toolkit for solving any ellipse — geometric or orbital — from any two independent parameters. All terms match the diagram above.  

## 📘 Glossary of Ellipse Parameters
  All variables match the labeled diagram above.

### 🔹 Core Axes & Foci
- **a** — semi-major axis  
- **b** — semi-minor axis  
- **c** — linear eccentricity (center to focus)  
- **e** — eccentricity (dimensionless) = $\dfrac{c}{a}$  
	  - Describes how "stretched" the ellipse is.  
		  - $e = 0$ → perfect circle  
		  - $0 < e < 1$ → ellipse  
		  - $e = 1$ → parabola (degenerate case)  
		  - $e > 1$ → hyperbola (not an ellipse)  
	- Eccentricity is **unitless** and invariant under scale.  
	-  It also defines the ellipse as a conic:

$$
e =  \dfrac{\text{distance to focus}}{\text{distance to directrix}}
$$
- **f** — flattening $b = 1 - \dfrac{b}{a}$  
- **i** — major axis $=2a$  
- **j** — minor axis $=2b$  
- **P, A** — primary vertices
- **X, Y** — co-vertices (±b along minor axis)  
- **C** — center of ellipse  
- **f₁, f₂** — the two foci  

### 🔹 Derived Lengths  
- **d** — focus-maximus = vertex to opposite focus $= a + c$  
- **g** — focus-minimus = focus to nearest vertex  $= a - c$ (e.g. $f_1P$)  
- **h** — focal span $=2c$  
- **ℓ** — semi-latus rectum $=\dfrac{1}{2} q$  
- **q** — latus rectum $= 2ℓ$

### 🔹 Directrix System  
- **m** — center-to-directrix $=\dfrac{a}{e}$  
- **n** — focus-to-directrix $=m - c$
- **s** — vertex-to-directrix $=m - a = \dfrac{c}{e} - a$  

## 🧮 Canonical Equations

### 🔹 Geometric
- $c = ae$  
- $b = a\sqrt{1 - e^2}$
- $a = \sqrt{b^2 + c^2}$

### 🔹 Orbital Geometry
- $f = a(1 - e^2) = \dfrac{b^2}{a}$  
- $r(\theta) = \dfrac{a(1 - e^2)}{1 + e \cos \theta}$  
- $r_p = a(1 - e)$ 

### 🔹 Directrix Relationships
- $m = \dfrac{a}{e}$  
- $s = m - a = \dfrac{c}{e} - a$  
- $n = m - c = \dfrac{a}{e} - c$

## 📐 What Is the Directrix?
For an ellipse, the **directrix** is:

> A fixed vertical line such that, for any point PPP on the ellipse,  
> the ratio of the distance from PPP to a **focus** and the distance from PPP to the **directrix** is equal to the **eccentricity** eee.

Formally:
$$\dfrac{\text{distance to focus}}{\text{distance to directrix}} = e$$
*This defines the ellipse!*
## 📏 Where Is the Directrix?

There are **two directrices**, one on each side of the center, at a distance:
$$m = \dfrac{a}{e}$$
… from the center, where:
- *a* is the semi-major axis
- *e* is the eccentricity    

So:
- Right-side directrix: $x = \dfrac{a}{e}$
- Left-side directrix: $x = -\dfrac{a}{e}$​
    If *e* → 0, the directrix moves off to infinity — which makes sense, because a circle (eccentricity 0) has no directrix-like behavior.

## 🎯 How the Directrix Relates to the Ellipse
You can think of the ellipse as a **set of points** where:
$$\dfrac{PF}{PD} = e$$
Where:
- PF is the distance from a point P on the ellipse to a **focus**
- PD is the distance from that same point P to the **directrix**   

This definition is symmetric and constructive: it's how conics are *defined* in classic geometry.

## 💡 So What Does It *Do*?
The directrix is mostly a **definitional and constructional tool** — not something we see in physical orbits, but:
- It gives us a clean formula for an ellipse in Cartesian coordinates:
$$r(\theta) = \dfrac{p}{1 + e \cos \theta} \quad \text{where } p = \dfrac{b^2}{a}$$
- It shows up in **ray-tracing**, **parabolic reflectors**, **classical mechanics**, and **procedural shape generation**.

## 🔍 Quick Facts
- Directrix location: $x= \pm \dfrac{a}{e}$
- Distance center to directrix: $m = \dfrac{a}{e}$
- Distance vertex to directrix: $s = m - a = \dfrac{c}{e}-a$
- Distance focus to directrix: $n = m - c = \dfrac{a}{e} - c$
- Eccentricity via directrix: $e = \dfrac{PF}{PD}$​

A reference sheet of exponent and logarithm rules useful in constructing systems of thermal, gravitational, orbital, and energetic relationships in scientifically-grounded worldbuilding.

## 🔢 Rules of Exponents

### ➕ Product & Quotient Rules
$$
x^m \cdot x^n = x^{m+n}, \qquad \frac{x^m}{x^n} = x^{m-n}
$$
### 📏 Index Rule
$$
\sqrt[n]{x} = x^{\frac{1}{n}}, \qquad \sqrt[-n]{x} = \frac{1}{\sqrt[n]{x}} = x^{-\frac{1}{n}}
\sqrt[m]{\frac{x^n}{x^p}} = x^{\frac{n - p}{m}}, \qquad \sqrt[m]{x^n x^p} = x^{\frac{n + p}{m}}
$$
### 🔁 Power Rule
$$
(x^m)^n = x^{mn}, \qquad (x^{-m})^n = x^{-mn}
\sqrt[n]{\sqrt[m]{x}} = \sqrt[nm]{x}, \qquad \sqrt[n]{x^{\frac{1}{m}}} = x^{\frac{1}{nm}}
$$
### 🧮 Power of a Fraction
$$
\left(\frac{x}{y}\right)^n = \frac{x^n}{y^n}
$$
### 🎯 Fractional Exponents
$$
\sqrt[m]{x^n} = x^{\frac{n}{m}}, \qquad \sqrt[n]{x^m} = x^{\frac{m}{n}}, \qquad (\sqrt[m]{x})^n = x^{\frac{n}{m}}
$$
### 🚫 Negative Exponent Rule
$$
x^{-n} = \frac{1}{x^n}
$$
### 🕳️ Zero Exponent Rule
$$
x^0 = 1 \quad \text{(for } x \ne 0\text{)}
$$
### ♾️ Infinity Exponent Rule
$$
x^\infty = \infty, \qquad x^{-\infty} = 0
$$
## 🧠 Additional Useful Identities

### 🧩 Distributive Rule for Exponents over Multiplication
$$
(xy)^n = x^n y^n, \qquad \left(\frac{x}{y}\right)^n = \frac{x^n}{y^n}
$$
### 🔄 Logarithmic Inverses
$$
\log_b(b^x) = x, \qquad b^{\log_b(x)} = x
$$
### 🪜 Logarithmic Expansion Rules
$$
\log(xy) = \log x + \log y, \qquad \log\left(\frac{x}{y}\right) = \log x - \log y, \qquad \log(x^n) = n \log x
$$
### 🌀 Reciprocal Roots
$$
\sqrt[n]{\frac{1}{x}} = \frac{1}{\sqrt[n]{x}} = x^{-\frac{1}{n}}
$$
### 📈 Arbitrary Exponentials in Terms of *e*
$$
a^x = e^{x \ln a}
$$
## 📊 Powers and Logs
$$
x^y = z \quad \Rightarrow \quad y = \frac{\log z}{\log x} = \log_x z
x = z^{\frac{1}{y}} = \sqrt[y]{z}
$$
# 🧮 General-Use Equations

### 📘 Variable Definitions
- **u** = upper bound  
- **l** = lower bound  
- **s** = sum of bounds (total)  
- **d** = difference between bounds (span)  
- **r** = ratio of lower to upper bound  
- **m** = mean (average)  
- **p** = product of bounds  
- **q** = quotient of bounds  

## 📏 Number Relationships

### ➗ Ratio
$$
\text{ratio} = \frac{l}{u} = \frac{\text{sum} - \text{difference}}{\text{sum} + \text{difference}}
$$
### ➕ Sum & Difference Identities
$$
\text{sum} = u + l = d\left(1 + \frac{1}{r}\right), \qquad
\text{difference} = u - l = s\left(\frac{1 - r}{1 + r}\right)
$$
### 🔀 Transformations Between Bounds
$$
l = \frac{s - d}{2}, \qquad
u = \frac{s + d}{2}, \qquad
s = l + u, \qquad
d = u - l
$$
### 🔁 Alternate Forms with Ratio
$$
l = \frac{s}{1 + r}, \qquad
u = \frac{rs}{1 + r}
l = s \cdot \left(\frac{1}{1 + r}\right), \qquad
u = s \cdot \left(\frac{r}{1 + r}\right)
l = \frac{s - d}{2}, \qquad
u = \frac{s + d}{2}, \qquad
l = \frac{(s - d) \cdot r}{1 + r}, \qquad
u = \frac{s \cdot r + d}{1 + r}
$$
### 📊 Mean
$$
m = \frac{u + l}{2}, \qquad
m = \frac{s}{2}, \qquad
m = u - \frac{d}{2}, \qquad
m = l + \frac{d}{2}
$$
### 🧮 Inequality Notes
$$
m \gg \frac{1}{2} u \quad \text{(if } u < 0 \text{ and } l > 0\text{)}
m = \frac{1}{2} u \quad \text{(if } l = 0\text{)}
m = u = l \quad \text{(if } u = l\text{)}
$$
### ✖️ Product & Quotient
$$
\text{Product } = xy = \frac{s^2 - d^2}{4}
\text{Quotient } = \frac{x + d}{x - d} = \frac{(x + y) + (x - y)}{(x + y) - (x - y)}
\frac{s}{d} = \frac{x + y}{x - y}, \qquad \frac{d}{s} = \frac{x - y}{x + y}
$$
## 📉 Percentage from Portion

### 🔢 Percentage (p) from portion (x) of total  (n)

$$
p = \frac{x}{n}, \qquad x = pn, \qquad n = \frac{p}{x}
$$
### 📘 Definitions
- **p** = percentage  
- **x** = portion (part)  
- **n** = base number (whole)

## 🎯 Percentages in Ranges

### 📐 Percentage (p) Represented by a Value (v) in Range (l … u)
$$
p = \frac{v - l}{u - l}, \qquad v = p(u - l) + l, \qquad u = \frac{v - l}{p} + l, \qquad l = \frac{v - pu}{1 - p}
$$
#### 🔤 Variable Definitions
- **v** = value within the range  
- **l** = lower bound  
- **u** = upper bound  
- **p** = percentage of the \([l, u]\) range represented by \(v\)

### 🔁 Transfer a Percentage Between Two Ranges
#### 🧮 General Equations
Let:
- $R_1 = [\text{min}, \text{num}, \text{max}]$
- $R_2 = [z, x, y]$, where $x < z < y$

Then:

$$
\text{pct} = \frac{\text{num} - \text{min}}{\text{max} - \text{min}}, \qquad
z = \text{pct} \cdot (y - x) + x
$$
#### ✅ Example
Given:
- $R_1 = [0, 6, 10]$
- $R_2 = [4, z, 6]$

Then:

$$
\text{pct} = \frac{6 - 0}{10 - 0} = \frac{6}{10} = 0.60
z = 0.60 \cdot (6 - 4) + 4 = 0.60(2) + 4 = 5.2
$$

Check:

$$
\frac{5.2 - 4}{6 - 4} = \frac{1.2}{2} = 0.60
$$
## 🔢 Sums of Number Sequences

### 📘 Variable Definitions
- **Σ** = sum of all integers in the range (l … u)  
- **s** = sum of bounds: $u + l$  
- **d** = difference: $u - l$  
- **l** = lower bound of range  
- **u** = upper bound of range  

### ➕ Consecutive Integers from (l …  u)
$$
s = u + l, \qquad d = u - l
$$
#### 🧮 Summation Formulas
Basic:

$$
\Sigma = \frac{u(u + 1)}{2} - \frac{l(l - 1)}{2}
$$

Symmetric:

$$
\Sigma = \frac{l^2 - 1}{2} + \frac{u^2 + u}{2}, \qquad
\Sigma = \frac{(u + l)(u - l + 1)}{2}
$$

Sum in terms of $d$ and $s$:

$$
\Sigma = \frac{d + 1}{2} s, \qquad
\Sigma = \frac{sd + s}{2}
$$

Expanded forms:

$$
\Sigma = \frac{u^2 + u}{2} - \frac{l^2 - l}{2}
\Sigma = \frac{(u^2 + u) - (l^2 - l)}{2}, \qquad
\Sigma = \frac{u^2 - l^2 + u + l}{2}, \qquad
\Sigma = \frac{u^2 - l^2 + s}{2}
$$
## 🔢 Integer Sequences and Special Transformations

### 🟥 Consecutive Odd Integers (1 … u)
$$
\Sigma_o = \left( \frac{u + 1}{2} \right)^2 = \frac{u^2 + 2u + 1}{4}
$$
### 🟦 Consecutive Even Integers (2 … u)
$$
\Sigma_e = \left( \frac{u}{2} \right) \left( \frac{u}{2} + 1 \right) = \frac{u(u + 2)}{4} = \frac{u^2 + 2u}{4}
$$
### 🧮 Count of Consecutive Integers in Range (1 … u)
$$
\left\lfloor \frac{u - l}{2} \right\rfloor + 1 \quad \text{for odd or even spacing}
$$
 — or for total count of integers:

$$
\left\lfloor \frac{u - l}{2} \right\rfloor \cdot 2 + 1 = 2\left\lfloor \frac{u - l}{2} \right\rfloor + 1
$$
### 📉 Percent Difference

$$
\%\Delta = 100 \cdot \frac{\text{new} - \text{old}}{\text{old}} = 100 \left( \frac{\text{new}}{\text{old}} - 1 \right)
$$
### 🔁 Involutive Transformation
Given:

$$
y = \frac{1 - x}{1 + x}
$$
Then:

$$
x = \frac{1 - y}{1 + y}
$$

This is its own inverse: $f(f(x)) = x$

### 🔄 Percentage Inversion (Reciprocal Percentages)
If $x\% \text{ of } y = y\% \text{ of } x$, then:

$$
\frac{x}{100} \cdot y = \frac{y}{100} \cdot x, \qquad
x \cdot \frac{y}{100} = y \cdot \frac{x}{100}
$$
## 🟨 Generalized Metallic Mean for Any Integer $x$
The traditional formula is:

$$
N_x = \frac{x + \sqrt{x^2 + 4}}{2}
$$

This generalizes the golden ratio (\(x = 1\)), silver ratio (\(x = 2\)), bronze ratio (\(x = 3\)), etc.

Alternative equivalent form:

$$
N_x = \sqrt{1 + \frac{x^2}{4}} + \frac{x}{2}
$$

This version is symmetric and may be more intuitive in nested radical systems.

## 📈 Point–Slope of a Line
Given two points:

$$
\begin{aligned}
P_1 = (x_1, y_1) \\[6pt]
P_2 = (x_2, y_2)
\end{aligned}
$$
### 🧮 Slope Formula
$$
m = \frac{y_1 - y_2}{x_1 - x_2}
$$
### 🧾 Point–Slope Form
$$
y - y_1 = m(x - x_1)
$$
Or rearranged:

$$
y = m(x - x_1) + y_1
$$
### 🎯 Slope–Intercept Form
$$
y = mx + b
$$
### 🔃 Converting from Point–Slope to Slope–Intercept
$$
\begin{aligned}
\text{Start with point–slope:} \quad & y - y_1 = m(x - x_1) \\[6pt]
\text{Distribute the slope:} \quad & y = mx - mx_1 + y_1 \\[6pt]
\text{Group constants:} \quad & y = mx + (y_1 - mx_1) \\[6pt]
\text{Therefore:} \quad & b = y_1 - mx_1
\end{aligned}
$$
> 🧠 **Note:** The subscripts vanish because their values get absorbed into the constant $b$.  
> The slope–intercept form still “remembers” your point — just more subtly.

## 🧪 Example 1
Given:  
- $P_1 = (4.85, 0)$  
- $P_2 = (1, 1)$

### Step 1: Find the slope
$$
m = \frac{0 - 1}{4.85 - 1} = \frac{-1}{3.85}
$$

### Step 2: Use point–slope form
$$
y - 0 = \frac{-1}{3.85}(x - 4.85)
$$

### Step 3: Rearrange to slope–intercept form
$$
y = \frac{-1}{3.85}x + \frac{4.85}{3.85} \approx -0.26x + 1.26
$$
## 🧪 Example 2
Given:  
- $P_1 = (0.5, 0)$  
- $P_2 = (1, 1)$

### Step 1: Find the slope
$$
m = \frac{0 - 1}{0.5 - 1} = \frac{-1}{-0.5} = 2
$$

### Step 2: Use point–slope form
$$
y - 0 = 2(x - 0.5)
$$

### Step 3: Rearrange to slope–intercept form
$$
y = 2x - 1
$$

## 📉 Visualizing Point–Slope Examples

This plot shows the two lines derived in the examples above:

- **Blue Line**:  
  From $P_1 = (4.85, 0)$ and $P_2 = (1, 1)$  
  $y = -0.25974x + 1.25974$

- **Red Line**:  
  From $P_1 = (0.5, 0)$ and $P_2 = (1, 1)$  
  $y = 2x - 1$

They intersect at the point (1, 1), which lies on both lines.

## 🌡️ Temperature Scale Equalities
### 🔁 Fahrenheit ↔ Kelvin
**Core conversion equations:**

$$
C = K - 273.15, \qquad C = \frac{5}{9}(F - 32)
$$

So:

$$
K - 273.15 = \frac{5}{9}(F - 32)
$$

Or rearranged:

$$
K = \frac{5}{9}(F - 32) + 273.15
$$

And:

$$
F = \frac{9}{5}(K - 273.15) + 32
$$
### 🧪 Worked Example (Convert 255.372 K to °F)
Start from:

$$
K = 255.372
$$

Plug into conversion formula:

$$
K - 273.15 = \frac{5}{9}(F - 32)
-17.7778 = \frac{5}{9}(F - 32)
$$

Multiply both sides by 9:

$$
-160 = 5(F - 32)
$$

Divide by 5:

$$
-32 = F - 32
$$

So:

$$
F = 0^\circ\text{F}
$$

Alternatively, in reverse:

$$
F = 0 \Rightarrow K = \frac{5}{9}(0 - 32) + 273.15 = -17.7778 + 273.15 = 255.372 \text{ K}
$$
### 🌡️ Fahrenheit ↔ Celsius
Standard conversion formulas:

$$
F = \frac{9}{5}C + 32, \qquad C = \frac{5}{9}(F - 32)
$$

#### 🔁 Rearrangements:
From:

$$
F = \frac{9}{5}C + 32
$$

Subtract 32:

$$
F - 32 = \frac{9}{5}C
$$

Multiply both sides by 5:

$$
5(F - 32) = 9C
$$

Divide by 9:

$$
C = \frac{5}{9}(F - 32)
$$
### 🧪 Worked Example (Convert -40°F to °C)
$$
C = \frac{5}{9}(-40 - 32) = \frac{5}{9}(-72) = -40
$$

So:

$$
-40^\circ \text{F} = -40^\circ \text{C}
$$
### 🌡️ Kelvin ↔ Celsius
The Kelvin and Celsius scales are offset by a constant:

$$
K = C + 273.15, \qquad C = K - 273.15
$$

> 📎 **Note:** The size of 1 degree is identical in both scales; only the zero point differs.
> Water freezes at 0 °C = 273.15 K and boils at 100 °C = 373.15 K.

> 📎 **Terminology Note:**  
> Temperatures on the Kelvin scale are written simply as **K**, without a degree symbol.  
> For example:  
> - Correct: **273.15 K**  ✓
> - Incorrect: **273.15 °K** – or – **273.15 degrees Kelvin**
# The Euclidean Algorithm

The Euclidean Algorithm provides an elegant and efficient (if somewhat involved) way to compute the greatest common divisor (GCD) of two integers.  This is especially useful for simplifying ratios or finding integer relationships when work with synodic systems

## The Algorithm
The algorithm itself is deceptively short and simple:
1. Start with two integers $a$ and $b$, such that $a>b$.
2. Divide $a$ by $b$, and note the *remainder*, $r$.
	- $r = a\; MOD\; b$
3. Replace $a$ with $b$ and $b$ with $r$.
4. Repeat steps 2 - 3 until $f = 0$.

The last *non-zero remainder* is the greatest common divisor between $a$ and $b$.

### Example

$$
\begin{aligned}
a = 2436 \qquad b = 1172 \\
r = a\;mod\;b = 92 \\[1em]
a = 1172 \qquad b = 92 \\
r = a\;mod\;b = 68 \\[1em]
a = 92 \qquad b = 68 \\
r = a\;mod\;b = 24 \\[1em]
a = 68 \qquad b = 24 \\
r = a\;mod\;b = 20 \\[1em]
a = 24 \qquad b = 20 \\
r = a\;mod\;b = 4\; ✓ \\[1em]
a = 20 \qquad b = 4 \\
⟶ r = a\;mod\;b = 0 \\
\end{aligned}
$$

If you don't have a tool that directly calculates modulos, $r$ can manually be calculated by:

$$
r = a - \left( b \times \left\lfloor \dfrac{a}{b} \right\rfloor \right)
$$

Here is an admittedly clunky longhand version for clarity

$$
\begin{aligned}
2 &\quad (Quotient)\\[-0.2ex]
1172)\,\overline{2436} &\quad (Dividend)\\[-0.4ex]
\underline{-2344} &\quad (Subtracted: 2\times1172)\\[-0.3ex]
92 &\leftarrow (Remainder)
\end{aligned}
$$

$$
\begin{aligned}
12 &\quad (Quotient)\\[-0.2ex]
92)\,\overline{1172} &\quad (Dividend)\\[-0.4ex]
\underline{-1104} &\quad (Subtracted: 12\times92)\\[-0.3ex]
68 &\leftarrow (Remainder)
\end{aligned}
$$

$$
\begin{aligned}
1 &\quad (Quotient)\\[-0.2ex]
68)\,\overline{92} &\quad (Dividend)\\[-0.4ex]
\underline{-68} &\quad (Subtracted: 1\times68)\\[-0.3ex]
24 &\leftarrow (Remainder)
\end{aligned}
$$

$$
\begin{aligned}
2 &\quad (Quotient)\\[-0.2ex]
24)\,\overline{68} &\quad (Dividend)\\[-0.4ex]
\underline{-48} &\quad (Subtracted: 2\times24)\\[-0.3ex]
20 &\leftarrow (Remainder)
\end{aligned}
$$

$$
\begin{aligned}
1 &\quad (Quotient)\\[-0.2ex]
20)\,\overline{24} &\quad (Dividend)\\[-0.4ex]
\underline{-20} &\quad (Subtracted: 1\times20)\\[-0.3ex]
\mathbf{4} &\;\boldsymbol{\checkmark}\leftarrow (Remainder)
\end{aligned}
$$

$$
\begin{aligned}
5 &\quad (Quotient)\\[-0.2ex]
4)\,\overline{20} &\quad (Dividend)\\[-0.4ex]
\underline{-20} &\quad (Subtracted: 5\times4)\\[-0.3ex]
0 &\leftarrow (Remainder)
\end{aligned}
$$

$$
\text{Since this remainder is } 0, \text{ the previous remainder is the GCD:}\\[0.5ex]
\therefore\;\gcd(2436,1172)=4
$$
# Rational Approximation (Continued Fractions)
```latex
$$
x = a_0 + 1/(a_1 + 1/(a_2 + 1/(a_3 + \dots)))
$$
```

$$
x = a_0 + 1/(a_1 + 1/(a_2 + 1/(a_3 + \dots)))
$$

```latex

$$
x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}
$$
```
$$
x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}
$$
```latex
$$
x = 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2 + \ddots}}}
$$
```
$$x = 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2 + \ddots}}}$$
## Step 1 — Define the goal

Given a real number $x$, find a fraction $\dfrac{p}{q}$ that’s as close as possible while keeping $q$ below some limit, $Q_{max}$.

$$
\text{minimize}\;\left|x-\frac{p}{q}\right|, \quad q \le Q_{max}
$$

## Step 2 — Start the continued-fraction expansion
Begin:

$$
\begin{array}{ll}
x_0 = x, & a_0 = \lfloor x_0 \rfloor
\end{array}
$$

Iterate:

$$
\begin{array}{ll}
x_{n + 1} = \dfrac{1}{x_n - a_n}, & a_{n + 1} = \lfloor x_{n + 1} \rfloor
\end{array}
$$
> In each iteration, replace $a_n$ with the value of $a_{n+1}$ from the previous iteration.

Record each $a_n$: the sequence $a_0, a_1, a_2,\ldots$ forms the **continued-fraction coefficients** of $x$.

$$
x = \mathbf{a_0} + \cfrac{1}{\mathbf{a_1} + \cfrac{1}{\mathbf{a_2} + \cfrac{1}{\mathbf{a_3} + \cdots}}}
$$

Thus, the number $x$ can be written as:

$$
x = [a_0; a_1, a_2, a_3, \ldots]
$$
Where:
- $a_0$ = the integer portion of $x$ (if any)
- $a_1, a_2, a_3, \ldots$ = the sequence of $a_n$ recorded above.

## Step 3  — Build convergents
Initialize:

$$
\begin{array}{lll}
p_{n-2} = 0, &p_{n-1} = 1, \\[0.5em]
q_{n-2} = 1, &q_{n-1} = 0 \\[0.5em]
n = 1
\end{array}
$$

Calculate:

$$
\begin{array}{lll}
&p_n = a_n\,p_{n-1} + p_{n-2}, \\[0.5em]
&q_n = a_n\,q_{n-1} + q_{n-2} \\[0.5em]
\text{Test:} &y_n = \dfrac{p_n}{q_n}, \\[0.5em]
\text{If:} &y_n \not\approx x, \\[0.5em]
\text{Increment n:} &n = n + 1 \\[0.5em]
\text{Continue until:} &|x - y_n| \quad\text{is within the desired tolerance}
\end{array}
$$


## 🎲 Random Assignment Syntax

### Basic Rule:
Use `⟨⟨ ⟩⟩` to indicate **random value assignment** from a specified range.

| Expression     | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| x = ⟨⟨a ∧ b⟩⟩  | Assign random value from a to b (inclusive)          |
| x .= ⟨⟨a ⩝ b⟩⟩ | Must assign value outside strict range               |
| x = ⟨⟨a ⩟ b⟩⟩  | Assign value in left-inclusive, right-excluded range |

- = → assignment
- .= → mandated assignment (value must be generated)

## 🎲 Random Assignment Syntax With Weighting

$$
x = a + (b - a)\,⟨⟨0 ∧ 1⟩⟩^{p}
$$

Where:
- $a$ = low end of the random range  
- $b$ = high end of the random range  
- $p$ = weighting exponent  
    - $p > 1$: weights the randomization toward $b$  
    - $0 < p < 1$: weights the randomization toward $a$  
    - $p = 1$: produces a uniform (unbiased) distribution  
    - $p \neq 0$: undefined at zero  

> Because ⟨⟨0 ∧ 1⟩⟩ represents a continuous uniform variable, and because the exponent $p \in (0, \infty)$ continuously reshapes that distribution, the **biasing space** is symmetric about $p = 1$: bias toward *a* for $0 < p < 1$, bias toward *b* for $p > 1$.

## 🔬 Precision Inference Rule

> The **decimal precision of a randomized result** is inferred from the **most precise** range endpoint.

| Syntax            | Result Precision |
| ----------------- | ---------------- |
| ⟨⟨1.4 ∧ 2.2⟩⟩     | 1 decimal place  |
| ⟨⟨1.40 ∧ 2.2⟩⟩    | 2 decimal places |
| ⟨⟨1.400 ∧ 2.200⟩⟩ | 3 decimal places |

This rule applies **even if the endpoints are excluded** from the valid output range.

## ❌ Invalid Forms

| Expression    | Reason                              |
| ------------- | ----------------------------------- |
| x = ⟨⟨1.414⟩⟩ | ❌ Invalid: one-value range          |
| x ∈ !⟨a ∧ b⟩  | ❌ Ambiguous: use `⩜` or `⩝` instead |
| x !.∈ ...     | ❌ Invalid modifier stacking         |

## 📜 Axioms

### WCB Axiom 7.1 — The Symbolcrafter’s Creed  
> *“Better to have it and not need it than need it and not have it.”*

All range connectives, including obscure ones like `⩡`, are retained in W101 to ensure semantic closure and support future or edge-case modeling needs.

## 🌌 Example Use

$K_1\; .\!\in ⟨a ⩜ b⟩$
 Kirkwood Gap 1 must lie strictly between a and b (excluding both endpoints)

$r\; .\!= ⟨⟨a ⩝ b⟩⟩$
 Assign a randomized orbital radius outside a forbidden band

# How Big?

## The Small Angle Approximation
When the apparent angular size ($\theta$) of an object (or the distance between two objects) in the sky is small — typically less than 10° — the sine and tangent of $\theta$ are nearly equal to $\theta$ itself when measured in radians:

$$
\theta ≈ \frac{d}{D} \times \frac{180}{\pi} = 57.2958\;\frac{d}{D}
$$
Where:
- $\theta$ = angular diameter (in degrees)
- $d$ = true diameter of the object (or separation between the objects)
- $D$ = distance to the object in the same units as $d$

When working in radians:

$$
\theta^c = \frac{d}{D}
$$
Where:
- $\theta^c$ = angular diameter (in radianss)
- $d$ = true diameter of the object (or separation between the objects)
- $D$ = distance to the object in the same units as $d$

## Measuring Exactly
If one wants to be precise, the appropriate equation is:

$$
\theta^c = 2\;arctan\;\left(\frac{d}{2D}\right)
$$
Where:
- $\theta^c$ = angular diameter (in radianss)
- $d$ = true diameter of the object (or separation between the objects)
- $D$ = distance to the object in the same units as $d$

To get the angle in degrees, convert:

$$
\begin{array}{l}
\theta^\circ = 2\;arctan\;\left(\dfrac{d}{2D}\right) \times \dfrac{180}{\pi} \\
\theta^\circ = 2\;arctan\;\left(\dfrac{d}{2D}\right) \times 57.2958
\end{array}
$$
## Approximating Angular Sizes (or Separations)
But, how does one arrive at an angular measure in the first place?  Well, there's this thing called a sextant....

Actually, there's a much simpler method using an instrument almost everyone has with them at all times — the hand at the end of their arm.  When the arm is fully extended, the hand (and its various parts) form a remarkably consistent angular ruler:

| Gesture                                              | Approximate<br>Angle | Notes                                                |
| ---------------------------------------------------- | -------------------- | ---------------------------------------------------- |
| Width of little finger                               | ≈ 1°                 | about twice the apparent diameter of the Sun or Moon |
| Width of first three fingers                         | ≈ 15°                | a convenient "finder field" in binoculars            |
| Width of closed fist                                 | ≈ 10°                | one _decadal_ unit — useful for quick sky hops       |
| Span from thumb to little finger ("rock on" gesture) | ≈ 20 – 25°           | a coarse measure for constellation spans             |
The most use a worldmaker will find for this trick is when you have calculated the size in degrees of something in your world's sky (or the separation between two objects in the heavens), you can get a sense for how "really" big that would appear by holding out your hand and approximating the appropriate angular measure.

The most use a worldmaker will find for this trick is when you have calculated the size in degrees of something in your world's sky (or the separation between two objects in the heavens), you can get a sense for how "really" big that would appear by holding out your hand and approximating the appropriate angular measure.

For instance; say you've calculated that your world's sun is about $3^\circ$ in the sky... that's about the width of the first two fingers held up at arm's length.

This is essentially the **practical inverse** of the *small-angle approximation* discussed earlier.

#### Universally Applicable
Because hand and arm proportions scale together with age and body size, this method works for nearly everyone — from children to giants — with only slight variations. And since this is an *approximate* method to begin with, those small differences can be safely ignored.

# The Naked-Eye Limit

Even without a telescope, the human eye is a sensitive instrument.  
Under a perfectly dark, moonless sky far from city lights, a person with average eyesight can see stars down to about **magnitude 6.0** — roughly **one-millionth** as bright as the faintest stars that remain visible from a town.

But brightness isn’t everything. A planet, asteroid, or moonlet that *reflects* light rather than producing its own must also be **large enough** and **close enough** for its surface area to gather and scatter enough starlight toward the observer.

In practice:

| Sky Condition     | Naked-Eye Limit | Example                                    |
| :---------------- | :-------------- | :----------------------------------------- |
| City sky          | ≈ mag 3         | Only the brightest dozen stars and planets |
| Suburban sky      | ≈ mag 4.5       | Dozens of stars; Milky Way faintly hinted  |
| Rural dark site   | ≈ mag 6         | Several thousand stars visible             |
| High desert / sea | ≈ mag 6.5 – 7   | Milky Way casts a faint shadow             |

The *naked-eye limit* defines the practical boundary between **visible** and **imagined** objects in a sky.

When worldbuilding, anything dimmer than about **mag 6** should be considered invisible to ordinary people unless aided by magic, technology, or narrative emphasis.

*(For detailed calculations of apparent magnitude and reflectivity, see **Stars 4 — Observation and Measurement**.)*

