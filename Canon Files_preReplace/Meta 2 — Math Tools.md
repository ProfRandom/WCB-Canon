---
title: ""
---


## Abstract
**Major Topics:**  
- Comprehensive algebraic toolkit for ellipse geometry and orbital mechanics.  
- Full glossary of ellipse parameters: semi-major axis (a), semi-minor axis (b), linear eccentricity (c), eccentricity (e), flattening (f), axes (i, j), vertices, co-vertices, foci.  
- Derived lengths: focus-maximus (d), focus-minimus (g), focal span (h), semi-latus rectum (ℓ), latus rectum (q).  
- Directrix system: center-to-directrix (m), focus-to-directrix (n), vertex-to-directrix (s).  
- Canonical equations for geometric relations, orbital radii, and directrix properties.  
- “Given Any Two, Solve the Rest” matrix for deriving all ellipse properties from any two independent parameters.  

**Key Terms & Symbols:**  
- a = semi-major axis.  
- b = semi-minor axis.  
- c = linear eccentricity.  
- e = eccentricity (unitless).  
- f = flattening.  
- i, j = major/minor axes (2a, 2b).  
- d, g, h = focus-maximus, focus-minimus, focal span.  
- ℓ, q = semi-latus rectum, latus rectum.  
- m, n, s = directrix distances.  
- r(θ) = orbital radius equation.  
- rₚ, rₐ = periapsis, apoapsis distances.  

**Cross-Check Notes:**  
- Eccentricity (e) canonically unitless and invariant under scale.  
- Flattening (f) defined here as $f = 1 - \dfrac{b}{a}$ — ensure consistency with other usage.  
- Directrix is definitional: appears in geometry but not physical orbits (noted explicitly).  
- “Solve the Rest” matrix designed for symbolic algebra; reinforces WCB’s **SANC** approach.  
- Overlaps with **Orbital Eccentricity and Seasonal Effects.md** (use of rₚ, rₐ).  



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
	-  It also defines the ellipse as a conic:   $$
  \dfrac{\text{distance to focus}}{\text{distance to directrix}} = e
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

This definition is symmetric and constructive: it's how conics are _defined_ in classic geometry.
## 💡 So What Does It _Do_?
The directrix is mostly a **definitional and constructional tool** — not something we see in physical orbits, but:
- It gives us a clean formula for an ellipse in Cartesian coordinates:
$$r(\theta) = \dfrac{p}{1 + e \cos \theta} \quad \text{where } p = \dfrac{b^2}{a}$$
- It shows up in **ray-tracing**, **parabolic reflectors**, **classical mechanics**, and **procedural shape generation**.
## 🔍 Quick Facts

| Concept                      | Value / Equation               |
| ---------------------------- | :------------------------------: |
| Directrix location           | $x= \pm \dfrac{a}{e}$​         |
| Distance center to directrix | $m = \dfrac{a}{e}$​            |
| Distance vertex to directrix | $s = m - a = \dfrac{c}{e}-a$   |
| Distance focus to directrix  | $n = m - c = \dfrac{a}{e} - c$ |
| Eccentricity via directrix   | $e = \dfrac{PF}{PD}$​          |
## 🧩 “Given Any Two, Solve the Rest” Matrix
Each row lists two known parameters and what you can solve from them using canonical identities.

|     Known Pair     | Solve For          |                                    Method / Equation(s)                                    |
| :----------------: | :----------------: | :----------------------------------------------------------------------------------------: |
|        a, e        | b, c, f, m, s, n   | $b = a\sqrt{1 - e^2},\ c = ae,\ f = a(1 - e^2),\ m = \dfrac{a}{e},\ s = m - a,\ n = m - c$ |
| a, b               | c, e, f            |       $c = \sqrt{a^2 - b^2},\ e = \sqrt{1 - \dfrac{b^2}{a^2}},\ f = \dfrac{b^2}{a}$        |
| a, c               | b, e, m, s, n      |    $e = \dfrac{c}{a},\ b = \sqrt{a^2 - c^2},\ m = \dfrac{a}{e},\ s = m - a,\ n = m - c$    |
| b, c               | a, e               |                         $a = \sqrt{b^2 + c^2},\ e = \dfrac{c}{a}$                          |
| e, b               | a, c               |                          $a = \dfrac{b}{\sqrt{1 - e^2}},\ c = ae$                          |
| rₚ, rₐ             | a, c, e, b         | $a = \dfrac{rₚ + rₐ}{2},\ c = \dfrac{rₐ - rₚ}{2},\ e = \dfrac{c}{a},\ b = a\sqrt{1 - e^2}$ |
| a, f               | b, e               |                     $b = \sqrt{af},\ e = \sqrt{1 - \dfrac{b^2}{a^2}}$                      |
| a, m               | e, c               |                                $e = \dfrac{a}{m},\ c = ae$                                 |
| c, e               | a, b, m            |                $a = \dfrac{c}{e},\ b = a\sqrt{1 - e^2},\ m = \dfrac{a}{e}$                 |
| a, s               | m, e, c, b         |               $m = a + s,\ e = \dfrac{a}{m},\ c = ae,\ b = a\sqrt{1 - e^2}$                |
| a, n               | m, c, e, b         |              $m = n + c,\ c = m - n,\ e = \dfrac{a}{m},\ b = a\sqrt{1 - e^2}$              |
> 🔍 *Note: This matrix is designed for symbolic manipulation. Some results require substitution into multiple chained equations.*## Abstract
**Major Topics:**  
- Reference sheet of exponent and logarithm rules for worldbuilding math.  
- General-use algebraic identities and transformations.  
- Ratio, sum/difference, mean, product/quotient relationships between bounds.  
- Percentage calculations and range transformations.  
- Integer sequences, summations, odd/even sequences.  
- Special transforms (involutive, reciprocal percentages).  
- Generalized metallic mean formula.  
- Point–slope and slope–intercept line equations.  
- Temperature scale conversions (Fahrenheit, Celsius, Kelvin).  

**Key Terms & Symbols:**  
- Exponents, roots, logs (standard algebra rules).  
- Variables for bounds: u (upper), l (lower), s (sum), d (difference), r (ratio), m (mean), p (product), q (quotient).  
- Percentages: p, x, n, v.  
- Σ = summation over integer ranges.  
- Metallic mean: Nₓ.  
- Line equations: slope (m), intercept (b), points (x₁, y₁), (x₂, y₂).  
- Temperature variables: F (Fahrenheit), C (Celsius), K (Kelvin).  

**Cross-Check Notes:**  
- Functions as a **toolbox reference** rather than a conceptual note.  
- Reinforces WCB’s **SANC** principle: simple, approximate, notationally clear.  
- Purely mathematical — no worldbuilding-specific notation introduced beyond standard algebra.  
- Should remain a **utility reference** to support other canon notes.  


A reference sheet of exponent and logarithm rules useful in constructing systems of thermal, gravitational, orbital, and energetic relationships in scientifically-grounded worldbuilding.


## 🔢 Rules of Exponents

### ➕ Product & Quotient Rules
$$
x^m \cdot x^n = x^{m+n}, \qquad \frac{x^m}{x^n} = x^{m-n}
$$


### 📏 Index Rule
$$
\sqrt[n]{x} = x^{\frac{1}{n}}, \qquad \sqrt[-n]{x} = \frac{1}{\sqrt[n]{x}} = x^{-\frac{1}{n}}
$$

$$
\sqrt[m]{\frac{x^n}{x^p}} = x^{\frac{n - p}{m}}, \qquad \sqrt[m]{x^n x^p} = x^{\frac{n + p}{m}}
$$


### 🔁 Power Rule
$$
(x^m)^n = x^{mn}, \qquad (x^{-m})^n = x^{-mn}
$$

$$
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
$$

$$
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
$$

$$
l = s \cdot \left(\frac{1}{1 + r}\right), \qquad
u = s \cdot \left(\frac{r}{1 + r}\right)
$$

$$
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
$$

$$
m = \frac{1}{2} u \quad \text{(if } l = 0\text{)}
$$

$$
m = u = l \quad \text{(if } u = l\text{)}
$$


### ✖️ Product & Quotient
$$
\text{Product } = xy = \frac{s^2 - d^2}{4}
$$

$$
\text{Quotient } = \frac{x + d}{x - d} = \frac{(x + y) + (x - y)}{(x + y) - (x - y)}
$$

$$
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
- \( R_1 = [\text{min}, \text{num}, \text{max}] \)
- \( R_2 = [z, x, y] \), where \( x < z < y \)

Then:
$$
\text{pct} = \frac{\text{num} - \text{min}}{\text{max} - \text{min}}, \qquad
z = \text{pct} \cdot (y - x) + x
$$


#### ✅ Example
Given:
- \( R_1 = [0, 6, 10] \)
- \( R_2 = [4, z, 6] \)

Then:
$$
\text{pct} = \frac{6 - 0}{10 - 0} = \frac{6}{10} = 0.60
$$

$$
z = 0.60 \cdot (6 - 4) + 4 = 0.60(2) + 4 = 5.2
$$

Check:
$$
\frac{5.2 - 4}{6 - 4} = \frac{1.2}{2} = 0.60
$$


## 🔢 Sums of Number Sequences

### 📘 Variable Definitions
- **Σ** = sum of all integers in the range (l … u)  
- **s** = sum of bounds: \( u + l \)  
- **d** = difference: \( u - l \)  
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

Sum in terms of \( d \) and \( s \):
$$
\Sigma = \frac{d + 1}{2} s, \qquad
\Sigma = \frac{sd + s}{2}
$$

Expanded forms:
$$
\Sigma = \frac{u^2 + u}{2} - \frac{l^2 - l}{2}
$$

$$
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

or for total count of integers:
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

This is its own inverse: \( f(f(x)) = x \)


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
\begin{gather}
P_1 = (x_1, y_1) \\[6pt]
P_2 = (x_2, y_2)
\end{gather}
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
\begin{align}
\text{Start with point–slope:} \quad & y - y_1 = m(x - x_1) \\[6pt]
\text{Distribute the slope:} \quad & y = mx - mx_1 + y_1 \\[6pt]
\text{Group constants:} \quad & y = mx + (y_1 - mx_1) \\[6pt]
\text{Therefore:} \quad & b = y_1 - mx_1
\end{align}
$$

> 🧠 **Note:** The subscripts vanish because their values get absorbed into the constant \( b \).  
> The slope–intercept form still “remembers” your point — just more subtly.


## 🧪 Example 1
Given:  
- \( P_1 = (4.85, 0) \)  
- \( P_2 = (1, 1) \)

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
- \( P_1 = (0.5, 0) \)  
- \( P_2 = (1, 1) \)

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

![[Line Point-Slope Illustration.png|500]]

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
$$

$$
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

## Abstract  
**Major Topics:**  
- Presents the **Euclidean Algorithm** as a systematic way to compute the **greatest common divisor (GCD)** of two integers.  
- Algorithm steps:  
  1. Start with integers a > b.  
  2. Divide a by b, record remainder r.  
  3. Replace a with b, b with r.  
  4. Repeat until r = 0. The last non-zero remainder is the GCD.  
- Provides both modular notation ($r = a \;mod\; b$) and longhand remainder calculation:  
  $$
  r = a - \left(b \times \left\lfloor \tfrac{a}{b} \right\rfloor \right)
  $$  
- Includes a complete worked example (2436, 1172 → gcd = 4), with step-by-step divisions.  
- Notes applications in worldbuilding, especially for **simplifying ratios** and finding integer relationships in **synodic systems**.  

**Key Terms & Symbols:**  
- **Euclidean Algorithm [NEW].**  
- **Greatest Common Divisor (GCD) [NEW].**  

**Cross-Check Notes:**  
- Neither term appeared in canon previously.  
- This file establishes both as new canonical entries.  
- **Status:** [NEW] — introduces Euclidean Algorithm and GCD into WCB canon with worked examples.  


# The Euclidean Algorithm

The Euclidean Algorithm provides an elegant and efficient (if somewhat involved) way to compute the greatest common divisor (GCD) of two integers.  This is especially useful for simplifying ratios or finding integer relationships when work with synodic systems

## The Algorithm
The algorithm itself is deceptively short and simple:
1. Start with two integers $a$ and $b$, such that $a>b$.
2. Divide $a$ by $b$, and note the _remainder_, $r$.
	- $r = a\; MOD\; b$
3. Replace $a$ with $b$ and $b$ with $r$.
4. Repeat steps 2 - 3 until $f = 0$.

The last _non-zero remainder_ is the greatest common divisor between $a$ and $b$.

### Example
$$
\begin{gather}
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
\end{gather}
$$
If you don't have a tool that directly calculates modulos, $r$ can manually be calculated by:
$$
r = a - \left( b \times \left\lfloor \dfrac{a}{b} \right\rfloor \right)
$$
Here is an admittedly clunky longhand version for clarity
$$
\begin{array}{r@{}l}
   2 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
1172\,)\,\overline{2436}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-2344}  \quad &\text{\scriptsize(Subtracted: $2\times1172$)} \\[-0.3ex]
\phantom{ }\,\,92 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   12 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
92\,)\,\overline{1172}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-1104}  \quad &\text{\scriptsize(Subtracted: $12\times92$)} \\[-0.3ex]
\phantom{}\,\,68 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   1 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
68\,)\,\overline{92}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-68}  \quad &\text{\scriptsize(Subtracted: $1\times68$)} \\[-0.3ex]
\phantom{}\,\,24 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   2 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
24\,)\,\overline{68}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-48}  \quad &\text{\scriptsize(Subtracted: $2\times24$)} \\[-0.3ex]
\phantom{}\,\,20 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   1 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
20\,)\,\overline{24}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-20}  \quad &\text{\scriptsize(Subtracted: $1\times20$)} \\[-0.3ex]
\phantom{}\,\,\mathbf{4} \; \boldsymbol{\checkmark} &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\begin{array}{r@{}l}
   5 \quad &\text{\scriptsize(Quotient)} \\[-0.2ex]
4\,)\,\overline{20}  \quad &\text{\scriptsize(Dividend)} \\[-0.4ex]
\underline{-20}  \quad &\text{\scriptsize(Subtracted: $5\times4$)} \\[-0.3ex]
\phantom{}\,\,0 \quad &\leftarrow \text{\scriptsize(Remainder)}
\end{array}
$$
$$
\text{Since this remainder is } 0 \text{, the previous remainder is the GCD}
$$
$$
\begin{array}{c c c}
\therefore \; \gcd(2436,1172) = 4 
\end{array}
$$

