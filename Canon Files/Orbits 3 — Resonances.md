---
title: ""
---

## Abstract  
**Major Topics:**  
- Definition of **mean motion resonance**: two (or more) bodies orbiting a common primary with orbital periods in an integer ratio (*a:b*).  
- **Notation:** ratio expressed as longer period : shorter period.  
- **Resonance order:**  
  - First-order (difference = 1) → e.g., 2:1, 6:5, 13:12.  
  - Second-order (difference = 2) → e.g., 3:1, 5:3.  
  - Higher orders increasingly unstable.  
- Multi-body case: Io–Europa–Ganymede in 4:2:1 resonance.  
- Limitation: while *N*-conjunctions are mathematically possible, stable mean motion resonances with >3 orbiters are essentially impossible.

**Key Terms & Symbols:**  
- **Mean Motion Resonance (MMR):** orbital commensurability condition.  
- **Order of Resonance:** difference between integer ratio components (1 = strongest).  

**Cross-Check Notes:**  
- Complements **Orbits 1 — Dynamics** (which develops tresonance/gresonance classification).  
- Introduces resonance “order” concept, not formalized in canon elsewhere.  
- No collisions with existing definitions.  
- To be grouped into **Orbits 3 — Resonances** (with Synodion, Synodial Epoch).  

___
___

# Mean Motion Resonance

When two bodies orbit a third body in common, there will be resonances in their orbits. If one body’s orbit is an exact integer value different from the other’s, the two are said to be in *mean motion resonance*, and the ratio of their orbits is **a : b**, denoted as the longer orbital period followed by the shorter orbital period, separated by a colon (∶).

![[MeanMotionResonance2-1.jpg]]

For example, in the figure above, Body 1 orbits twice for every one orbit of Body 2.  This is a _first order resonance_, because the difference between the two values is only 1 unit:
$$
2 - 1 = 1
$$
Other examples of first-order resonances[^1] would be 6 : 5, 13 : 12, etc.

Examples of a _second-order resonance_ would be those in which the orbital periods were separated by a difference of 2; e.g. 3 : 1 or 5 : 3.  The higher the order of the resonance, the less stable the orbits will be over time.

Mean motion resonances can arise between three or more bodies.  Jupiter's moons Io, Europa, and Ganymede experience a 4 : 2 : 1 mean motion resonance between them, such that for every orbit Ganymede makes, Europa completes two, and Io completes four.  This also means that Io orbits twice per each orbit of Europa.

However, an interesting phenomenon also occurs, such that Ganymede, Europa, and Io _never line up_ on the same side of Jupiter.  Any two of them may line up at various points in their orbital dance, but all three never do.

> While N-conjunctions are _technically_ possible in N-orbiton systems, they are reliant on very specific conditions of orbital eccentricity and coplanarity; mean motion resonances between more than three objects should be treated for all intents and purposes as _impossible_.


## Abstract  
**Major Topics:**  
- Defines the **synodion (Σ):** the synodic period between two orbitons whose orbital periods are not in integer ratio.  
- Related concepts:  
  - **Synodos:** moment of alignment (closest approach).  
  - **Synodial fraction (FΣ):** fraction of orbits completed by each body during one synodion.  
  - **Synodial lag angle (ΔΘ):** angular displacement by which successive synodoi shift backward.  
- Demonstrates calculation with example:  
  - $P_\alpha = 24.36$ d, $P_\beta = 11.72$ d.  
  - $\Sigma = 22.587$ d, $F_\alpha = 0.9272$, $F_\beta = 1.9272$.  
  - ΔΘ = 26.203°, so alignments drift backward each synodion.  
- Provides full set of equivalent formulas for Σ, including reciprocal and ratio forms.  
- Emphasizes that synodia recur but not at the original base angle $B^\theta$, unless by coincidence after many cycles.  

**Key Terms & Symbols:**  
- **Synodion (Σ) [NEW].**  
- **Synodos [NEW].**  
- **Synodial fraction (FΣ) [NEW].**  
- **Synodial lag angle (ΔΘ) [NEW].**  

**Cross-Check Notes:**  
- Canon has no prior abstract of synodic periods.  
- Complements Orbits 1 (Dynamics), but distinct: this covers non-integer commensurabilities.  
- **Status:** [NEW] — establishes synodion framework as part of orbital resonance canon.  
---
---


## The Synodian: Non-Integer Resonances
When two bodies orbit a central body, but their orbital periods are:
1. not integer multiples of the system's base time unit *T*; and,
2. not directly commensurate[^2] with one another,
… a more sophisticated approach is required to calculate periodic alignments of the system.

The _base time unit_ ($T$), may be years, months, days, even hours or minutes.

The interval between such instances of alignment is called the _synodic period_; here, we'll refer to it as a _synodion_ $\Sigma$ (pl: _synodia_), for reasons which will become clear presently.  The moment of alignment, when the two orbitons are closest to one another, we call a _synodos_ (pl: _synodoi_).

Thus, the synodion represents the time it takes for the two orbitons to return to the same relative configuration, such as having their centers fall on a line that includes the center of the central body.  While synodia are still predictable, their periodicity is less intuitive that in mean motion resonance systems, requiring more precise calculations.

The best way to grasp these concepts is by working through an example.  By appling the rules of synodic periods to a specific pair of orbiting bodies, we can illustrate how to calculate a synodion, and explore the patterns it reveals.

### A Worked Example
Let's imagine a system of three bodies, the central body (_centron_ $\dot{C}$) and two less massive bodies orbiting it (the _orbitons_ $M_\alpha$ and $M_\beta$).  $M_\alpha$ has the longer orbital period ($P_\alpha$; the time it takes $M_\alpha$ to orbit the centron) and $M_\beta$ has the shorter orbital period ($P_\beta$; the time it takes $M_\beta$ to orbit the centron).

> While the masses of the bodies have no bearing on the following equations, they _do_ matter from a nomenclature perspective.  The more massive body is always the _primary_, the second-most massive body is the _secondary_; the third most is the _tertiary_, etc.  Their _radii_ are not a factor in determining their hierarchy.
> For instance, Mercury is more massive than Ganymede, but Ganymede has a larger radius.  If the two of them were to form a two-body system, *Ganymede would orbit Mercury*, even though it is larger in radius and volume than Mercury.

For this example, we will define:
$$
\begin{align}
P_\alpha = 24.36\; \text{days} \\
P_\beta = 11.72\; \text{days}
\end{align}
$$
![[synodion01.jpg|300]]
The above figure illustrates the starting configuration of our system ($T_0$).  The starting angle at which all three bodies are lined up we call the _base angle_, denoted by $B^\theta$.

We can already make some determinations about our system:
$$
\begin{align}
P_\delta = P_\alpha - P_\beta = 24.36 - 11.72 = 12.64\; \text{days} \\
P_Q = \dfrac{P_\beta}{P_\alpha} = \dfrac{11.72}{24.36} = 0.481\; \text{days}
\end{align}
$$
The ratio of their orbits ($P_Q$) is not an integer, so these orbitons are not in a mean motion resonance; for every orbit of $M_\beta$, $M_\alpha$ only completes $0.481$ of its orbit, because $M_\alpha$ takes $12.64$ days longer to orbit the centron than does $M_\beta$.

Since a full orbit for _either_ orbiton is $360^\circ$, we can figure out how many degrees of their orbit each orbiton completes within the system base time unit, which in this case would be $1$ day.
$$
\begin{align}
\theta_\alpha &= \dfrac{360^\circ}{24.36} = 14.778^\circ \qquad \text{The \emph{minor unit angle}}\\
\theta_\beta &= \dfrac{360^\circ}{11.72} = 30.717^\circ  \qquad \text{The \emph{major unit angle}}\\
\end{align}
$$

This tells us how many degrees $M_\alpha$ "lags behind" $M_\beta$ per day:
$$
\theta_\Delta = \theta_\beta - \theta_\alpha = 30.717^\circ - 14.778^\circ = 15.939^\circ \qquad \text{The \emph{orbiton difference angle}}
$$
So, every day $M_\beta$ moves almost $16^\circ$ farther in its orbit than $M_\alpha$ does in its orbit.

We can also calculate ho many degrees of its orbit $M_\alpha$ completes (subtends) per each full orbit of $M_\beta$:
$$
\alpha^\circ = P_Q \times 360 = 0.481 \times 360 = 173.202^\circ 
$$
So, after _two_ of $M_\beta$'s orbits:
![[synodion03.jpg|300]]
$$
2 a^\circ = (2)(173.202) = 346.404^\circ
$$
… $M_\alpha$ still hasn't completed one of its orbits, it has only completed
$$
\dfrac{346.404}{360} = 0.962
$$
orbits of the centron.

Conversely, by the time $M_\alpha$ completes one full orbit of the centron, $M_\beta$ will have completed
$$
P_R = \dfrac{24.36}{11.72} = 2.078
$$
orbits of the centron.

![[synodion04.jpg|300]]
It is a curious feature of circular motion that if you get far enough ahead of the other body, you eventually come up behind it.  Think of a 5000-meter Olympic footrace.  All of the competitors start out on the same line and travel in the same direction.  Let's say there are two runners, Number 11 and Number 24.

Number 11 quickly pulls out ahead of Number 24 and for a time it is quite obvious that she is "way out ahead".  But if she maintains her higher running speed, eventually she will be _so far ahead_ of Number 24 that _she will appear to be running behind them_.  Anyone looking in on the race at just that moment could be forgiven for thinking that Number 11 is losing, perhaps badly.

However, eventually Number 11 will catch up to Number 24 and pass them again; but for a moment they will be side-by-side, just as they were at the start of the race _but not back on the starting line_; their meeting point will be some angular distance around the track from where they began.  Where and when this moment occurs is entirely a matter of how fast each runner is running.

Returning to our orbitons, it becomes obvious that at some point while they are orbiting, they will "meet up" at their closest approach to one another, just as our runners did in the Olympic race — they will have achieved synodos.  The first synodos to occur after $T_0$ we label $T_1$; the second we label $T_2$, and so on.

Here's the really cool thing: we can calculate exactly _where_ and _when_ $T_1, T_2$, etc. take place!
#### The When
The synodic period (mentioned above) is the period of time that transpires between any two synodoi:
$$
\begin{equation}
\begin{split}
\Sigma &= \dfrac{P_\alpha \times P_\beta}{|P_\alpha - P_\beta|} \\
&= \dfrac{24.36 \times 11.72}{|24.26 - 11.72|} \\
&= \dfrac{285.499}{12.64} \\
\Sigma &= 22.587\; \text{days ✓}
\end{split}
\end{equation}
$$
So, each synodos occurs just over $22\frac{1}{2}$ days after the preceding one.

> Note that if we divide $360^\circ$ by the difference angle $\theta_\Delta$
> $$
 \Sigma = \dfrac{360}{\theta_\Delta} = \dfrac{360}{15.939}= 22.587\; \text{days}
 $$
 … we also get the synodic period.

Notice that the synodion, $22.587$ days is more than two orbits of $M_\beta$ and less than one orbit of $M_\alpha$.  If we divide the lengths of each orbiton's period by the length of the synodion:
$$
\begin{align}
F_\alpha &= \dfrac{P_\alpha}{\Sigma} = \dfrac{24.36}{22.587} = 0.9272\; \text{orbit}\\
F_\beta &= \dfrac{P_\beta}{\Sigma} = \dfrac{11.72}{22.587} = 1.9272\; \text{orbits}
\end{align}
$$
Do you see it?  The decimal fraction of both of these quotients is the same: $0.9272$.  We designate this as the _synodial fraction_, and denote it as $F_\Sigma$, and it helps us to answer the question of "where" the synodoi take place.

What the synodial fraction tells us is that synodos $T_1$ occurs $1.9272$ orbits of $M_\beta$ and $0.9272$
orbits of $M_\alpha$ from their starting time ($T_0$) and place (the base angle $B^\theta$).  Multiplying the synodial fraction by the number of degrees in a circle:
$$
\Theta = F_\Sigma \times 360^\circ = (0.9272)(333.7975^\circ) \qquad \text{The \emph{synodial angle}}
$$
Subtracting the synodial angle from $360^\circ$:
$$
\Delta_\Theta = 360^\circ - \Theta = 360^\circ - 333.7975^\circ = 26.203^\circ \qquad \text{The \emph{synodial lag angle}}
$$
… we now know that each successive synodos occurs $22.587$ days after _when_ and $26.203^\circ$ "short" of where the previous one occurred.  Thus the synodoi "march backward" around the centron.  We can calculate the precise angle relative to $B^\theta$ any given synodos occurs by:
$$
\widehat{\Theta} = 360^\circ - MOD((S \times \Delta_\Theta), 360)
$$
where S is the number of the synodos after $T_0$; e.g. for synodos $T_6, S = 6$.
## Diving Deeper
Above, we learned about the synodic period equation:
$$
\begin{align}
\Sigma &= \dfrac{P_\alpha \times P_\beta}{|P_\alpha - P_\beta|} \\
\end{align}
$$
Here is a comprehensive listing of the related equations:
$$
\begin{aligned}
&&& \text{Given: } P_\alpha > P_\beta \\[1em]
\Sigma &= \dfrac{P_\alpha P_\beta}{|P_\alpha - P_\beta|}
& P_\alpha &= \dfrac{\Sigma P_\beta}{\Sigma - P_\beta}
& P_\beta &= \dfrac{\Sigma P_\alpha}{\Sigma + P_\alpha} \\[1em]
\dfrac{1}{\Sigma} &= \left|\dfrac{1}{P_\alpha}-\dfrac{1}{P_\beta}\right|
& \dfrac{1}{P_\alpha} &= \dfrac{1}{P_\beta}-\dfrac{1}{\Sigma}
& \dfrac{1}{P_\beta} &= \dfrac{1}{P_\alpha}+\dfrac{1}{\Sigma} \\[1em]
\end{aligned}
$$
$$
\begin{array}{rcl}
Q &= \dfrac{P_\beta}{P_\alpha} 
&&&P_\alpha = P_\beta \times R = \dfrac{P_\beta}{Q} 
= \left(\dfrac{\Sigma}{Q} - \Sigma\right) = \Sigma(R - 1) \\[1em]
R &= \dfrac{P_\alpha}{P_\beta} 
&&&P_\beta = P_\alpha \times Q = \dfrac{P_\alpha}{R}
= \left(\Sigma - \dfrac{\Sigma}{R}\right) = \Sigma(1-Q)
\end{array}
$$

Where:
- $\Sigma$ = synodion
- $P_\alpha$ = period of the outer body, $M_\alpha$ (longer)
- $P_\beta$ = period of the inner body, $M_\beta$ (shorter)
- $Q$ = quotient of the outer body period to the inner body period
- $R$ = ratio of the inner body period to the outer body period

> *Note that the second row of equations perform the same calculations as the first row by using the reciprocals of the orbital periods.*

All of this leads us naturally to the question:

> Does any future synodos ever fall precisely at the base angle $B^\theta$ again?  In other words is
> $$
\widehat{\Theta} = 0^\circ
  $$
  … ever true after $T_0$?

The answer is "yes" and we can calculate that, too.



## Abstract  
**Major Topics:**  
- Defines the **synodial epoch (Y):** interval after which two orbitons return to their original alignment angle (base angle $B^\theta$).  
- Related measures:  
  - **Epochal aggregate (Y₀):** total days in a synodial epoch.  
  - **Epochal interval (Ψ):** number of synodoi within one epoch.  
  - **Quarter synodial epoch (Y₀/4):** recurrence at cardinal angles (90°, 180°, 270°).  
  - **Quarter epochal interval (Ψ/4):** synodoi per quarter epoch.  
  - **Epochal complements (Yα, Yβ):** complete orbits of each body per epoch.  
- Requires integer normalization of orbital periods for LCM/GCD computation.  
- Worked example ($P_\alpha = 24.36$ d, $P_\beta = 11.72$ d):  
  - $Y₀ = 7137.48$ d ≈ 19.54 y.  
  - Ψ = 316 synodoi.  
  - Quarter epoch ≈ 1784 d ≈ 4.89 y.  
  - Yα = 293 orbits, Yβ = 609 orbits.  

**Key Terms & Symbols:**  
- **Synodial Epoch (Y) [NEW].**  
- **Epochal Aggregate (Y₀) [NEW].**  
- **Epochal Interval (Ψ) [NEW].**  
- **Quarter Synodial Epoch (Y₀/4) [NEW].**  
- **Quarter Epochal Interval (Ψ/4) [NEW].**  
- **Epochal Complements (Yα, Yβ) [NEW].**  

**Cross-Check Notes:**  
- No prior canon coverage of epochal cycles; this is a new layer building on the **Synodion** framework.  
- Depends on GCD/LCM math tools (already canonized in **The Euclidean Algorithm**).  
- **Status:** [NEW] — introduces full synodial epoch framework as part of resonance canon.  
---
---


## The Synodial Epoch

The _synodial epoch_ ($Y$) is the time interval after which a synodion occurs at the base angle $B^\theta$ agin, completing a full cycle.

The _epochal aggregate_ ($Y_0$) is the total number of synodia that transpire within a synodial epoch.

Whereas we used the synodic formula:
$$
\begin{align}
\Sigma &= \dfrac{P_\alpha \times P_\beta}{|P_\alpha - P_\beta|} \\
\end{align}
$$
to calculate the synodic period, we need to use a different method to calculate the Epochal Aggregate; we employ both the *Least Common Multiple* (LCM) and the *Greatest Common Divisor* (GCD):
$$
LCM(a, b) = \dfrac{a \times b}{GCD(a, b)}
$$
>❗️Important ❗️
>1. Most modern calculators, spreadsheets, and programming languages have built-in functions for calculating both LCM and GCD, but be aware that *both of these can only be correctly calculated for integer inputs*.  If something like LCM(1.5, 3.3) returns a value rather than an error, it will likely be the LCM of 1 and 3, not of 1.5 and 3.3.
>2. The GCD _can_ be calculated by hand using the _Euclidean Algorithm_ (detailed elsewhere), calculators, spreadsheets, or programmed scripts are much faster.

We need to calculate the LCM of $P_\alpha = 24.36$ and $P_\beta = 11.72$, but neither of these are integers, so we _normalize_ them by multiplying by the factor of ten which will render the more precise of the two into an integer value.  In this case, both have two decimal places of precision, so multiplying by $10^2 = 100$ will be sufficient:
$$
P'_\alpha = 24.36 \times 100 = 2436 \quad \text{and} \quad P'_\beta = 11.72 \times 100 = 1172
$$
Now we can compute the LCM by:
$$
\begin{equation}
\begin{split}
LCM(a, b) &= \dfrac{a \times b}{GCD(a, b)} \\[0.5em]
&= \dfrac{2436 \times 1172}{GCD(2436, 1172)} \\[0.5em]
&= \dfrac{2854992}{4} \\
&= 713748\; ✓
\end{split}
\end{equation}
$$
Now, _since we normalized our inputs_ by scaling up by a factor of $10^2 = 100$, we need to scale this result _down_ by the same factor:
$$
Y_0 = \dfrac{713748}{100} = 7137.48\; \text{days } ✓
$$
The _epochal interval_ ($\Psi$) is calculated by dividing the Epochal Aggregate ($Y_0$) by the synodic period ($\Sigma$):
$$
\begin{equation}
\begin{split}
\Psi &= \dfrac{Y_0}{\Sigma} \\[0.5em]
&= \dfrac{7137.48}{22.587} \\[0.5em]
&= 316\; \text{synodia}
\end{split}
\end{equation}
$$
This reveals that $T_{316}$ occurs in the same configuration at the base angle $B^\theta$.  We can double-check by supplying $S=316$ to our synodian instance angle ($\widehat{\Theta}$) equation:
$$
\begin{equation}
\begin{split}
\widehat{\Theta} &= 360^\circ - MOD((S \times \Lambda_\Theta), 360^\circ) \\
&= 360^\circ - MOD((316 \times 26.203^\circ), 360^\circ) \\
&= 360^\circ - 360^\circ \\
&= 0\; ✓
\end{split}
\end{equation}
$$
To convert the epochal aggregate $\Psi = 7137.48$ days into something more useful, we can divide by the number of days in a sidereal year ($≈ 365.2564$):
$$
Y_0^y = \dfrac{7137.48}{365.2564} = 19.54\; \text{years }✓
$$
… which is about
$$
19^y\;197^d\;11^h\;16^m\;20.724^s
$$
give-or-take a millisecond.
### Quarter Synodial Epoch
#### The Where
A quarter synodial epoch ($Y_{/4}$) is an important quantity, as well; at these intervals, synodoi occur precisely on a cardinal angle ($90^\circ, 180^\circ, 270^\circ$) in succession.  We call these the _cardinal synodoi_.  They occur, of course every one fourth of the synodion:
$$
Y_{/4} = \dfrac{Y_0}{4}
$$
In our worked example above, the quarter synodial epoch is:
$$
\begin{gather}
Y_{/4} = \dfrac{Y_0}{4} = \dfrac{7137.48}{4} = 1784.37\; \text{days} \\[0.5em]
Y_{/4}^y = \dfrac{Y_{/4}}{365.2564} = \dfrac{1784.37}{365.2564} ≈ 4.89\; \text{years}
\end{gather}
$$
### Quarter Epochal Interval
Similarly, a _quarter epochal interval_ ($\Psi_{/4}$) is the number of _common synodoi_ that occur between cardinal synodoi:
$$
\Psi_{/4} = \dfrac{\Psi_0}{4} = \dfrac{316}{4} = 79\; \text{synodoi}
$$
### The Epochal Complements
There are two of these, the _epochal major complement_ ($Y_\alpha$) and the _epochal minor complement_ ($Y_\beta$), which are the number of complete orbits of orbiton $M_\alpha$ and $M_\beta$, respectively, per each synodial epoch:
$$
\begin{align}
Y_\alpha &= \dfrac{Y_0}{P_\alpha} \\[1em]
Y_\beta &= \dfrac{Y_0}{P_\beta}
\end{align}
$$
In our worked example above:
$$
\begin{align}
Y_\alpha &= \dfrac{Y_0}{P_\alpha} = \dfrac{7137.48}{24.36} = 293\; \text{orbits }✓ \\[1em]
Y_\beta &= \dfrac{Y_0}{P_\beta} = \dfrac{7137.48}{11.72} = 609\; \text{orbits }✓
\end{align}
$$





---

[^1]: While the notation ²/₁ is notationally equivalent to 2 : 1, we use the colon format exclusively.

[^2]: literally, "having a common measure"; the orbit of one can't be expressed by a whole number or rational fraction of the other's.
