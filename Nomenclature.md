### 🧮 Notation Clarification

**WCB acknowledges** that conventional algebraic procedure requires *rationalizing denominators*—that is, removing radical terms from the bottom of a fraction by multiplication with their conjugates.  
 
However, for the sake of **operational clarity** and **mnemonic transparency**, certain expressions are intentionally left in their *unsimplified* form.  

This allows their symbolic structure to directly reflect the relationships among the duramonic parameters they represent.  
 
For example:  

$$
\frac{g}{\sqrt{\rho}}
\quad \text{is formally equivalent to} \quad
\frac{g\,\sqrt{\rho}}{\rho}
$$

 — yet the former is retained in WCB texts for its **immediate interpretive value**—visibly expressing that *escape velocity* increases in proportion to gravity and decreases with the square root of density.  
 
Such departures from formal algebraic convention are **deliberate**, not erroneous, and are applied consistently wherever a simplified expression would obscure the physical relationship it represents.

### ✏️ Exponent Representation

For the same reason, **fractional exponents**, e.g.:

$$
\rho^{1/2} \quad \text{or} \quad m^{2/3}
$$

 — are generally **avoided** in favor of **radical notation**, e.g.:
 
$$
\sqrt{\rho} \quad \text{or} \quad \sqrt[3]{m^2}
$$
 
 Radical form preserves **visual proportionality** and **dimensional intuition**, particularly when multiple roots or parameters appear in the same expression.  Also, the representations, $\sqrt{\rho}$ and $\sqrt[3]{m^2}$ do not break the default line spacing of the rendered text.

 If a fractional exponent **must** be employed, it should be represented as a formal fraction, e.g.:
 ```
$m^{\frac{2}{3}}$
```
This results in a rendering which conforms to the default line spacing in the rest of the paragraph block, appearing as $m^{\frac{2}{3}}$, but the fractional expoenent can become difficult to discern at small font sizes.

This can be made more readable by pairing the fraction with a text sizing command such as `\normalsize`or `\large`, e.g.:
```
$m^{{\normalsize\frac{2}{3}}}

or

m^{{\large\frac{2}{3}}}$
```
These are a passable workarounds, but as can be seen from this text block example using the full fraction results in rendering such as $m^{{\normalsize\frac{2}{3}}}$ or $m^{{\large\frac{2}{3}}}$, which can be problematic if there is a line of text above the sentence in which the exponent appears. This adjustment can still be **difficult to interpret** in complex expressions and should therefore be used **sparingly and with intent**.

A variation:
```
$m^{{}^2/{}_3}$
```
 — can be employed.  This renders somewhat more readably than the above, but again, in inline usages, an expression of the form $m^{{}^2/{}_3}$ can cause irregular line spacing (though to a much lesser degree) if a line of text appears above the line bearing the expression.  This is perhaps less jarring than the full fractional expression, however.  This format is also generally cross-renderer compliant, but should be tested before relied upon extensively.




