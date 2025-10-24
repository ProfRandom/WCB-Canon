# Range Constraints & Modifiers

WCB uses extended symbolic notation to express range relationships, logical connectives, and modal constraints.  The following sections define these conventions for both rendered and plaintext forms.

## Range Connectives

**Inclusive Interior**  
* ⟨a ∧ b⟩  
* Value must lie between *a* and *b*, including both *a* and *b*.

**Exclusive Interior**  
* ⟨>a ∧ <b⟩  
* Value must lie between *a* and *b*, excluding both *a* and *b*.

**Inclusive Exterior**  
* ⟨a ∨ b⟩  
* Value must lie outside the range between *a* and *b*, including both *a* and *b*.

**Exclusive Exterior**  
* ⟨<a ∨ >b⟩  
* Value must lie outside the range between *a* and *b*, excluding both *a* and *b*.

**Left-Exclusive Interior**  
* ⟨>a ∧ b⟩  
* Value must lie between *a* and *b*, **excluding** *a* and **including** *b*.

**Right-Exclusive Interior**  
* ⟨a ∧ <b⟩  
* Value must lie between *a* and *b*, **including** *a* and **excluding** *b*.

**Left-Exclusive Exterior**  
* ⟨<a ∨ b⟩  
* Value must lie **outside** the range between *a* and *b*, **excluding** *a* and **including** *b*.

**Right-Exclusive Exterior**  
* ⟨a ∨ >b⟩  
* Value must lie **outside** the range between *a* and *b*, **including** *a* and **excluding** *b*.

## Modifiers

- $\not{\;}$ overstruck on the operator — **negation**  
  Examples: $\not=,\ \not\in,\ \not\approx,\ \not\le$  
  - **Plaintext alternative:** precede the operator with ! → !=, !∈, !≈, !≤

- $\wedge$ beneath the operator — **mandative** (“must”)  
  Examples: $\underset{\wedge}{\le},\ \underset{\wedge}{\in}$  
  - **Plaintext alternative:** precede the operator with ∧ → ∧≤, ∧∈

- $\vee$ above the operator — **prescriptive** (“should”)  
  Examples: $\overset{\vee}{\le},\ \overset{\vee}{\in}$  
  - **Plaintext alternative:** succeed the operator with ∨ → ≤∨, ∈∨

> *These symbols allow concise, unambiguous expression of conditional ranges and requirements in WCB equations.*
