# Number Range Notation

WCB uses extended symbolic notation to express range relationships, logical connectives, and modal constraints.  The following sections define these conventions for both rendered and plaintext forms.

## Range Connectives

**Inclusive Interior**  
* $\langle a \wedge b \rangle$
* Value must lie between *a* and *b*, including both *a* and *b*.

**Exclusive Interior**  
* $\langle > a\; \wedge <b \rangle$
* Value must lie between *a* and *b*, excluding both *a* and *b*.

**Inclusive Exterior**  
* $\langle a \vee b \rangle$
* Value must lie outside the range between *a* and *b*, including both *a* and *b*.

**Exclusive Exterior**  
* $\langle <a\; \vee >b\rangle$
* Value must lie outside the range between *a* and *b*, excluding both *a* and *b*.

**Left-Exclusive Interior**  
* $\langle >a \wedge b \rangle$
* Value must lie between *a* and *b*, **excluding** *a* and **including** *b*.

**Right-Exclusive Interior**  
* $\langle a\; \wedge <b \rangle$
* Value must lie between *a* and *b*, **including** *a* and **excluding** *b*.

**Left-Exclusive Exterior**  
* $\langle <a \vee b \rangle$
* Value must lie **outside** the range between *a* and *b*, **excluding** *a* and **including** *b*.

**Right-Exclusive Exterior**  
* $\langle a\; \vee >b \rangle$
* Value must lie **outside** the range between *a* and *b*, **including** *a* and **excluding** *b*.

## Modifiers
### Negation

- $\not{\;}$ overstruck on the operator — **negation**  

Examples:
```
	$\not=,\, \not\in,\, \not\approx,\, \not\le$  
```
yields: $\not=,\, \not\in,\, \not\approx,\, \not\le$
 
- **Plaintext alternative:** precede the operator with ! → !=, !∈, !≈, !≤

### Mandation

- $\wedge$ beneath the operator — **mandative** (“must”)  

Examples:
```
	$\underset{\wedge}{\le}, \,  \underset{\wedge}{\in}, \, \underset{\wedge}{=}$  
```
yields: $\underset{\wedge}{\le}, \,  \underset{\wedge}{\in}, \, \underset{\wedge}{=}$  

- **Plaintext alternative:** precede the operator with ∧ → ∧≤, ∧∈, ∧=

### Prescription

- $\vee$ above the operator — **prescriptive** (“should”)  

Examples:
```
$\overset{\vee}{\le},\, \overset{\vee}{\in}, \, \overset{\vee}{=}$  
```
yields: $\overset{\vee}{\le},\, \overset{\vee}{\in}, \, \overset{\vee}{=}$  

- **Plaintext alternative:** succeed the operator with ∨ → ≤∨, ∈∨, =∨

> *These symbols allow concise, unambiguous expression of conditional ranges and requirements in WCB equations.*
