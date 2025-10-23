## 📏 Number Relationships

### Symbol Reference

$$
\begin{array}{ll}
l & \text{lower bound} \\[0.3em]
u & \text{upper bound} \\[0.3em]
s & \text{sum of bounds: } s = l + u \\[0.3em]
d & \text{difference (range): } d = u - l \\[0.3em]
h & \text{half-range (semi-span): } h = \tfrac{d}{2} = \tfrac{u - l}{2} \\[0.3em]
m & \text{mean (midpoint): } m = \tfrac{l + u}{2} = \tfrac{s}{2} \\[0.3em]
r & \text{ratio (lower→upper): } r = \tfrac{l}{u} \\[0.3em]
q & \text{quotient (upper→lower): } q = \tfrac{u}{l} = \tfrac{1}{r}
\end{array}
$$

Any two of these parameters determine all the rest:

$$
\{\,l,\,u,\,s,\,d,\,h,\,m,\,r,\,q\,\}
$$


### 1. Canonical Transformations

$$
\begin{aligned}
s &= l + u = 2m, &
d &= u - l = 2h, \\[0.4em]
r &= \frac{l}{u} = \frac{m - h}{m + h}, &
q &= \frac{u}{l} = \frac{1}{r}.
\end{aligned}
$$

These four equations form a closed relational system linking the lower and upper bounds,
their mean and half-range, and their ratio and quotient.


### 2. Core Definitions

$$
\begin{array}{ll}
l = \text{lower bound} & u = \text{upper bound} \\[0.3em]
s = \text{sum} = l + u & d = \text{difference (range)} = u - l \\[0.3em]
h = \text{half-range} = \dfrac{d}{2} = \dfrac{u - l}{2} \\[0.3em]
m = \text{mean (midpoint)} = \dfrac{l + u}{2} = \dfrac{s}{2} \\[0.3em]
r = \text{ratio} = \dfrac{l}{u} & q = \text{quotient} = \dfrac{u}{l} = \dfrac{1}{r}
\end{array}
$$


### 3. Transformations Between Bounds

$$
l = m - h, \qquad
u = m + h.
$$

Equivalently:

$$
m = \frac{u + l}{2}, \qquad
h = \frac{u - l}{2}.
$$


### 4. Alternate Forms by Ratio

$$
\begin{aligned}
l &= \frac{r s}{1 + r} = s\!\left(\frac{r}{1 + r}\right), \\[0.4em]
u &= \frac{s}{1 + r} = s\!\left(\frac{1}{1 + r}\right), \\[0.4em]
h &= m\!\left(\frac{1 - r}{1 + r}\right).
\end{aligned}
$$


### 5. Derived Sum & Difference Forms

$$
\begin{aligned}
s &= d\!\left(1 + \frac{1}{r}\right) = 2h\!\left(1 + \frac{1}{r}\right), \\[0.4em]
d &= s\!\left(\frac{1 - r}{1 + r}\right) = 2h.
\end{aligned}
$$


### 6. Product Relationship

$$
l\,u = (m - h)(m + h) = m^2 - h^2.
$$


### 7. Inequality Conditions

Illustrating special cases and symmetry:

$$
\begin{aligned}
m &> \tfrac{1}{2}u &&\text{if } (u > 0,\, l < 0), \\[0.3em]
m &= \tfrac{1}{2}u &&\text{if } l = 0, \\[0.3em]
m &= u = l &&\text{if } u = l.
\end{aligned}
$$


### 8. Closure Check

For any consistent pair of inputs, the following identity must hold:

$$
(m + h)(m - h) = l\,u.
$$

This verifies the self-consistency of the entire system.
