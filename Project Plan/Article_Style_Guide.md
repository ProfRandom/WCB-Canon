---
title: Meta 0 — Article Structure and Editing (Architect’s Appendix)
summary: Defines the standard order, length, and editorial practices for WCB articles, including table editing, KaTeX handling, and version control procedures.  Serves as the operational reference for maintaining the Architect’s Appendix.
domain: meta
category: structure
tags: [articles, formatting, editing, structure, appendix]
vocabulary: [article, section, table, KaTeX, revision, appendix]
updated: 2025-11-01
status: canonical
version: 1.1
related: [Foundations — World Crafting Basics, Architect’s Appendix]
contributors: [M. Conrad]
source: ""
---

# WCB Article Structure and Editing  
*(Architect’s Appendix Reference)*


# WCB Article Style Guide
## Purpose of this Style Guide

The WCB Style Guide defines the editorial, mathematical, and structural conventions used across all documents in the World-Crafting Basics canon.  Its purpose is not to impose rigidity but to ensure clarity, coherence, and interoperability among articles, editors, and publication formats.

This guide exists to make every piece of the Canon — from a one-page note to a full chapter — consistent, readable, and easy to maintain.  It also serves as a reference for automated formatting and Markdown generation, allowing future contributors and tools to work within a shared framework.

### Goals

1. 	Consistency — Ensure uniform layout, notation, and tone across all WCB articles.
2. 	Clarity — Make every file self-contained and legible in plain text as well as rendered form.
3. 	Compatibility — Maintain stable output across Markdown editors (Zettlr, Obsidian, VS Code), document engines (Quarto, Pandoc), and online wikis (GitLab, Gitea).
4. 	Accessibility — Simplify syntax and math presentation so content remains readable for both human editors and technical renderers.
5. 	Extensibility — Support new article types and scientific models without breaking the underlying style rules.

### Principles
 
The Style Guide follows the same meta-logic as WCB itself:
	•	Science-Adjacent, No Calculus — clear, approachable, and rigorous without excess complexity.
	•	Straightforward, Appropriate, Notationally Clear — every symbol and format should serve readability.
	•	Sufficient and Necessary Constructs — no extra syntax when simpler form will do.
	•	Self-Adjusting, Non-Coercive — these rules guide rather than restrict; use judgment where clarity demands adaptation.

## Scope and Applicability

The **WCB Style Guide** applies to all Markdown (`.md`) documents that form part of the *World-Crafting Basics* (WCB) Canon and its supporting materials.  It defines the conventions used for formatting, structure, mathematical notation, and file organization across all modules.

This includes but is not limited to:  
- Canonical documents in the `Meta`, `Stars`, `Duramons`, `Peramons`, and related directories  
- Technical appendices, data references, and mathematical summaries  
- Wiki articles, abstracts, or publications derived from the Canon  
- Internal drafts intended for future integration into the main repository  

### What It Covers

1. **Document Structure** — header hierarchy, section order, and article templates  
2. **Formatting Rules** — Markdown syntax, KaTeX equations, tables, and typographic conventions  
3. **File and Directory Standards** — naming conventions, numbering, and folder organization  
4. **Editorial Tone** — consistent use of capitalization, punctuation, and in-universe terminology  
5. **Crosslinking and Referencing** — canonical link formats and related-article notation  

### What It Does *Not* Cover

- External media such as images, diagrams, or raw data tables (though filenames should follow the same conventions)  
- Software scripts, configuration files, or automation metadata  
- Informal notes, whiteboard sketches, or out-of-canon material unless incorporated into a canonical document  

### Intended Audience

The guide is designed for:  
- **Primary authors and editors** maintaining the Canon  
- **Contributors** preparing new or revised WCB articles  
- **Automated processes** generating or validating Markdown output (e.g., Quarto, Pandoc, or future WCB toolchains)

In short: if a file lives within the WCB repository and contributes to its published body of work, this Style Guide applies.

## General Markdown and File Rules

The WCB Canon uses **Git-compatible Markdown** (`.md`) as its master document format.  
All content should remain fully legible as plain text while also rendering cleanly in Zettlr, Quarto, Pandoc, and GitLab Wiki environments.

These rules ensure consistent formatting, safe rendering, and future-proof editing behavior.

### Blank Line Conventions

- Always include **one blank line before and after** each equation block (`$$…$$`).  
- Include **one blank line before and after each header** for readability and rendering stability.  
  - If an equation block is followed by a header, the same blank line serves for both.  
- Leave **one blank line before and after lists, tables, and block quotes**.  
- Avoid double-blank spacing between paragraphs except for visual separation in drafts.

### Headers

- Use Markdown header levels (`#`, `##`, `###`, etc.) to organize sections.  
- Reserve `#` for document titles; `##` for primary sections; `###` and below for subsections.  
- Do not use horizontal rules (`---`) as section dividers — only YAML headers may use triple-dash lines.  
- **If a horizontal rule is absolutely necessary, use `___` or `***` instead of `---`** to prevent the line from being mistaken for a YAML delimiter.  
- Maintain consistent capitalization and hierarchy throughout the file.

## Mathematics Formatting Conventions

Mathematical expressions are a central part of WCB’s analytical framework.  
They must be **clear, readable, and visually consistent** across all Canon articles.  
This section defines how equations should be formatted, styled, and embedded within WCB Markdown documents.

### General Principles

- Every equation should **illustrate or clarify** the text, never obscure it.  
- Present equations in **KaTeX-compatible** syntax only.  
- Keep notation consistent across the Canon.  
- Define all symbols and variables on first use within a section.  
- Use GEWE (*Good Enough for Worldmaking Efforts*) precision — express values with no more digits than the context demands.

### Equations and KaTeX Blocks

- Use `$$…$$` for block equations and `$…$` for inline equations.  
- Place block equations on their own lines, surrounded by single blank lines.  
- Use `{array}` or `{aligned}` for multi-line layouts; avoid `eqnarray`, `split`, or unsupported KaTeX environments.  
- Keep syntax KaTeX-safe:
  - Avoid `@{}`, `\hspace`, or other LaTeX spacing tricks outside `\text{}`.  
  - Escape special characters where needed (`_`, `%`, `&`, `#`).  
- Define each variable or symbol the first time it appears in a section.

#### Inline and Block Math

- Use `$…$` for **inline equations** within running text.  
  - Example: `The escape velocity is given by $v_e = \sqrt{2GM/R}$.`
- Use `$$…$$` for **block equations** on their own lines.  
  - Example:
    ```latex
    $$
    v_e = \sqrt{\frac{2GM}{R}}
    $$
    ```
- Always include **one blank line** above and below each block equation.  
- If a block equation is immediately followed by a header, the same blank line serves both.

#### Multi-Line Equations and Alignment

- Use `{aligned}` or `{array}` environments for multi-line relationships.  
- Align on the primary operator (`=`, `≈`, `≤`, etc.) for readability.

```latex
$$
\begin{aligned}
a &= F / m \\
v &= v_0 + at
\end{aligned}
$$
```
#### Radical Notation In Denominators

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

#### Fractional Exponent Representation

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

This can be made more readable by pairing the fraction with a text sizing command, e.g.:
```
$m^{{\footnotesize\frac{2}{3}}}

or

$m^{{\small\frac{2}{3}}}
```
These are a passable workarounds,: as can be seen from this text block example using the full fraction results in renderings such as $m^{{\footnotesize\frac{2}{3}}}$ or $m^{{\small\frac{2}{3}}}$ (compare to $m^{\frac{2}{3}}$).  This *can* cause a slight discontinuity in the line spacing of the text block, which can be problematic if there is a line of text above the sentence in which the exponent appears, but it is not terribly jarring in most cases.

A variation:
```
$m^{{}^2/{}_3}$
```
 — can be employed.  This renders somewhat more readably than the above, but again, in inline usages, an expression of the form $m^{{}^2/{}_3}$ can cause irregular line spacing (though to a lesser degree) if a line of text appears above the line bearing the expression.  This is perhaps less noticeable than the full fractional expression even when rendered `\small` or `\footnotesize`, however. This format is generally cross-renderer compliant, but should be tested before relied upon extensively.

#### Math Block Text Sizing Commands
These can be used in math blocks or as inline math sequences within text blocks to control the rendered size of text.

$$
\begin{array}{lcl}
 \setminus\text{tiny} &\longrightarrow & \tiny \text{Example} \\
 \setminus\text{scriptsize} &\longrightarrow & \scriptsize \text{Example} \\
 \setminus\text{footnotesize} &\longrightarrow & \footnotesize \text{Example} \\
 \setminus\text{small} &\longrightarrow & \small \text{Example} \\
 \setminus\text{normalsize} &\longrightarrow & \normalsize \text{Example} \\
 \setminus\text{large} &\longrightarrow & \large \text{Example} \\
 \setminus\text{Large} &\longrightarrow & \Large \text{Example} \\
 \setminus\text{LARGE} &\longrightarrow & \LARGE \text{Example} \\
 \setminus\text{huge} &\longrightarrow & \huge \text{Example} \\
 \setminus\text{Huge} &\longrightarrow & \Huge \text{Example} \\
\end{array}
$$
##### Examples
```
$\small\text{This text is smaller than the text surrounding it.}$
```
This is normal sized text. $\small\text{This text is smaller than the text surrounding it.}$ It is also rendered in a different font face.

```
$$
\varphi = \frac{\sqrt{5} + 1}{2} = \LARGE \boxed{1.61803399}
$$
```
Renders as:

$$
\varphi = \frac{\sqrt{5} + 1}{2} = \LARGE \boxed{1.61803399}
$$
***You probably don't want to actually use that particular size, it's just presented for illustration purposes.***

### Lists and Tables

Tables are **strongly discouraged** in WCB articles.

While Markdown tables may render correctly in some editors, they are unstable across platforms and **notoriously unreliable in Zettlr**.  
Zettlr’s renderer automatically resizes columns, wraps header text, and may even restore deleted rows when editing via its table interface.  
For this reason, authors should treat tables as a last resort.

#### Why Tables Are Problematic

- Markdown tables cannot define or lock column widths.  
- Zettlr compresses the leftmost column when any cell wraps, often destroying alignment.  
- KaTeX `{array}` blocks used for mixed text will overflow past the right margin instead of wrapping.  
- The built-in table editor may silently discard changes when the table structure is edited in rendered mode.  

In short: if a table might wrap, **don’t use a table**.

#### Preferred Alternatives

##### 1. KaTeX `{array}` Blocks — For Numeric or Symbolic Data

When alignment matters and the content will not wrap, use KaTeX `{array}` environments.  
They provide full control over column alignment and spacing.

```latex
$$
\begin{array}{l c r}
\text{Name} & \text{Symbol} & \text{Value} \\
\hline
\text{Speed of light} & c & 2.998\times10^{8}\ \text{m/s} \\
\text{Gravitational constant} & G & 6.674\times10^{-11}\ \text{N·m²/kg²} \\
\end{array}
$$
```

✅ **Use this method when:**
- All entries are short and uniform in width.
- You require mathematical alignment (`l`, `c`, `r` columns).
- The table will not contain multi-line or prose cells.

⚠️ **Avoid** if text is likely to wrap, as KaTeX will not handle long lines—it will overflow beyond the page margin.

##### 2. Formatted (Key–Value) Lists — For Textual or Mixed Data

When descriptive text is needed, replace tables with formatted lists.  
These read clearly in both raw Markdown and rendered form.
```markdown
**Parameter:** `mass`  
**Meaning:** Total system mass of the body in Earth units.  
**Example:** `5.97 × 10²⁴ kg`

**Parameter:** `radius`  
**Meaning:** Mean equatorial radius in kilometers.  
**Example:** `6371 km`
```

✅ **Use this method when:**
- Data include sentences, long phrases, or explanatory text.  
- Readability and editability are more important than strict alignment.  
- You want to preserve formatting consistency across editors.

#### Summary Rule

- Use **KaTeX `{array}`** for short, fixed-width numeric data.  
- Use **Key–Value formatted lists** for descriptive or textual data.  
- **Avoid Markdown tables entirely** except for the simplest, single-line entries.  
- If a table is visually essential, prepare it externally (e.g., Word, Pages, or a spreadsheet) and import it as a static graphic.

> **In short:** if you find yourself fighting the table, the table has already won.

### Inline Text and Emphasis

- Use **bold** for key terms or headers; *italics* for emphasis or new terminology.  
- Avoid all-caps for emphasis.  
- Use `\text{}` in math blocks for human-readable words.  
- Prefer en-dashes (–) for numeric ranges and em-dashes (—) for narrative breaks.  
- SI symbols (m, s, kg, etc.) remain upright (roman); variables are italicized.

### Code and Snippets

- Use backticks (\`) for inline code or variable names in explanations.  
- Use triple backticks (\`\`\`) for fenced code blocks when needed.  
- Code examples should be language-tagged (````python `,````bash `, etc.) for clarity.

### Crosslinks

- Crosslinks use the format `[[Category — Article Title]]`.  
- Maintain exact capitalization and spacing of the target file’s title line.  
- Avoid relative paths or external URLs inside canonical Markdown files.

### Line Length and Indentation

- Keep paragraphs to **80–100 characters per line** for readability.  
- Use spaces, not tabs.  
- Indent nested lists with two spaces per level; do not mix tabs and spaces.

### Whitespace and Line Breaks

- Avoid unnecessary spaces at the ends of lines of text.  
  - One or two trailing spaces are harmless, but more than two can trigger inconsistent behavior across renderers — or simply give the editor a migraine.  
- Use a **single blank line** to separate paragraphs and major elements (headers, lists, tables, equations).  
- Do not use multiple consecutive blank lines except in drafts or comment blocks.  
- End each file with exactly **one newline** for clean version control and predictable rendering.

### File Naming

- Filenames must use **underscores** (`_`) instead of spaces for portability and command-line safety.  
  - ✅ `Meta_0_WCB_Style_Guide.md`  
  - ❌ `WCB Style Guide.md`
- Use **Title Case** for human readability (capitalize each major word).  
- Use only ASCII letters, digits, and underscores — no hyphens, punctuation, or whitespace.  
- Prefix each file with its **category** and **sequence number**, followed by the title.  
  - Example: `Stars_4_Observation_and_Measurement.md`
- Always end filenames with a lowercase `.md` extension.  
- Avoid unnecessary abbreviations unless the filename would otherwise exceed 80 characters.

### File Encoding

- All files must use **UTF-8 encoding**.  
- Do not include a byte-order mark (BOM).  
- End each file with a single newline.

## YAML Headers

Every canonical WCB Markdown article begins with a **YAML front-matter block** enclosed by triple dashes (`---`).  
This header defines essential metadata used by editors, renderers, and validation tools.  
It is invisible to the reader but indispensable to the author and to the automated systems that maintain the Canon.

### Purpose and Visibility

YAML headers serve as **editorial metadata**, not part of the visible text.  
They are *not displayed* in rendered WCB articles or exported Wiki pages,  
but they enable consistent cataloging, crosslinking, contributor tracking, and machine readability.

> Think of the YAML header as the *control panel* of an article — unseen by the reader, but vital to its structure and integrity.

### Header Completeness Policy

All canonical WCB articles must include the **full set of YAML fields**, in the order listed below, even if some fields are empty or set to `null`.  
This ensures uniform file structure, predictable parsing, and clean version-control diffs.  
Empty fields may use blank strings (`""`), empty arrays (`[]`), or explicit `null` values.

**Required Field Order**

1. `title`  
2. `summary`  
3. `domain`  
4. `category`  
5. `tags`  
6. `vocabulary`  
7. `updated`  
8. `status`  
9. `version`  
10. `related`  
11. `contributors`  
12. `source`

### Field Definitions

**Title**  
Full, human-readable title of the article. Should match the first Markdown header (`# …`).  
*Example:* `Stars 4 — Observation and Measurement`

**Summary**  
One-sentence description of the article’s content. Appears in catalogs or wikis.  
*Example:* `Reference for measurement techniques and notation.`

**Domain**  
Broad grouping of the file within the Canon.  
*Examples:* `meta`, `stars`, `duramons`, `peramons`

**Category**  
Narrower subject classification within a domain.  
*Examples:* `observation`, `structure`, `habitability`

**Tags**  
Keyword list for search and filtering.  
Use lowercase; enclose in brackets `[tag1, tag2]`.

**Vocabulary**  
Lists the five most important concepts or neolexes introduced or discussed in the article.  
Keep concise (≤ 5 entries). Broader term lists belong under a “Terminology” or “Lexicon” section.

**Updated**  
ISO-format date of the last major edit (`YYYY-MM-DD`).  
*Example:* `2025-10-24`

**Status**  
Editorial or publication state.  
Accepted values: `draft`, `review`, `stable`, `canonical`.

**Version**  
Identifies a numbered or tagged revision.  
*Example:* `1.3`

**Related**  
Lists cross-referenced files by title.  
*Example:* `[Stars 5 — System Architecture, Meta 2 — Math Tools]`

**Contributors**  
Credits multiple authors or editors.  
*Example:* `[G. Conrad, A. Reyes]`

**Source**  
Links to primary references or datasets.  
*Example:* `https://github.com/wcbcanon/data-stars`

### Example Minimal Header

```yaml
---
title: Monons 3 — Small Star System Bodies
summary: ""
domain: duramons
category: ""
tags: []
vocabulary: []
updated: 2025-10-24
status: draft
version: null
related: []
contributors: []
source: ""
---
```
### Example Maximal Header

```yaml
---
title: ""
summary: ""
domain: ""
category: ""
function: definitive        # definitive | descriptive | meta
scope: []                   # e.g., [ontic, duramonic]
tags: []
vocabulary: []
updated: 2025-__
reviewed: null              # optional review date
status: draft
version: 0.1
related: []
parent: null
children: []
contributors: [M. Conrad]
editorial_notes: ""
license: "CC BY-SA 4.0"
source: ""
---
```
### Formatting Rules

- YAML headers must appear at the **very top** of the file.  
  No blank lines or comments may precede the opening `---`.  
- Leave **one blank line after the closing `---`** before the first Markdown header (`# …`).  
- Use plain ASCII quotes (`"…"`) only when a field contains punctuation or colons.  
- Lists are bracketed (`[item1, item2]`) or indented using standard YAML list syntax (`- item`).  
- Dates follow **ISO-8601** (`YYYY-MM-DD`).  
- Use lowercase field names exactly as listed.  
- Maintain the specified field order in all files.

> **Reminder:** YAML headers are invisible to end-users but are essential for consistent indexing and cross-referencing within the WCB Canon.

### Header Validation Checklist

Before committing a new or updated article, verify that:

1. The header begins and ends with `---` lines.  
2. No blank lines or comments precede the opening `---`.  
3. Exactly one blank line follows the closing `---`.  
4. All twelve required fields appear in the correct order.  
5. Empty or unused fields contain valid placeholders (`""`, `[]`, or `null`).  
6. The `title` matches the first Markdown header in the file.  
7. Dates follow ISO format (`YYYY-MM-DD`).  
8. Lists use bracketed or properly indented YAML syntax.  
9. The file saves cleanly and passes YAML validation (no unbalanced brackets or colons).  
10. All metadata accurately reflects the article’s content and editorial status.

> **Tip:** Keeping header structure uniform across all articles ensures reliable indexing and makes future automation trivial.

## Article Structure and Content Order

Each WCB article follows a consistent internal structure to ensure clarity, navigability, and compatibility across the Canon.  
This structure applies to all article types — conceptual, mathematical, or referential — with optional sections as noted.

### General Principles

- Articles are **modular**: each file should make sense when read on its own, but connect naturally to related topics.  
- Sections are **hierarchical**: higher-level headings (##, ###) establish conceptual order, while lower-level subsections (####) refine details.  
- Each article should progress from **overview → detail → application → references**.  
- Avoid redundancy between articles; use crosslinks (`[[Category — Article Title]]`) instead of re-explaining shared concepts.

### Standard Section Order

1. **Title and Header Block**
   - Defined in the YAML header and repeated as the first Markdown header (`# …`).
   - The title should match the `title` field in the YAML header exactly.

2. **Abstract or Introduction**
   - A short overview (1–3 paragraphs) summarizing the article’s purpose and scope.  
   - Should answer: *What is this about? Why does it matter?*  
   - Use plain language and avoid equations unless essential for framing.

3. **Contents Box (Optional but Recommended)**
   - A short, bulleted summary of the article’s major sections or key ideas.  
   - Keeps navigation consistent with longer articles.  
   - Example:
```markdown
     **Contents**
     - Overview
     - Core Equations
     - Applications
     - Crosslinks
```
4. **Explanatory Section(s)**
   - The main body of the article, divided into clearly titled subsections.  
   - Explain concepts before presenting formulas or classifications.  
   - Define every variable or symbol upon first use.  
   - Keep each subsection focused and self-contained.

5. **Mathematical or Structural Section (if applicable)**
   - Present equations, derivations, or frameworks that support the article’s main concepts.  
   - Use KaTeX block equations (`$$ … $$`) with clear definitions below or beside them.  
   - Example:
```latex
     $$ a = \frac{F}{m} $$

     where:
     a = acceleration,  
     F = applied force,  
     m = mass.
```
6. **Applications or Examples**
   - Demonstrate how the concept or relationship is used within WCB modeling or worldbuilding contexts.  
   - Keep examples concise, with plain-language explanations following equations.  
   - Example:
```markdown
     **Example:**  
     A terran planet with double lunar mass (2 μt) exhibits tidal patterns consistent with…
```
7. **Terminology / Lexicon Section**
   - Lists and defines key terms, neolexes, and abbreviations introduced in the article.  
   - Format as bolded entries with one-sentence explanations.  
   - Example:
```markdown
     **planemon** — A monon that maintains hydrostatic equilibrium but has no self-sustaining fusion.  
     **duramon** — Any solid-surface monon (e.g., asteroid, moon, or planet).  
```

8. **Crosslinks and Internal References**
   - Provide links to directly related WCB articles or external references.  
   - Use the `[[Category — Title]]` format for internal crosslinks.  
   - Example:
```markdown
     **See also:** [[Stars 5 — System Architecture]], [[Meta 2 — Math Tools]]
```
9. **External References (if applicable)**
    - Provide citations or source material not part of the WCB Canon.  
    - Place all external references at the **end of the article**, following internal crosslinks.  
    - Keep entries concise and consistent — author, title, publication, year, and (if relevant) URL.  
    - Use plain Markdown formatting; avoid BibTeX or embedded LaTeX citation commands.  
    - Example:

```markdown
      **External References**
      - NASA Exoplanet Archive, 2024. [https://exoplanetarchive.ipac.caltech.edu](https://exoplanetarchive.ipac.caltech.edu)  
      - Asimov, I. *The Relativity of Wrong.* 1989.
```

> **Note:** WCB treats external references as *sources of inspiration or verification*, not as dependencies.  
> They supplement worldmaking context but do not define Canonical truths within WCB’s internal logic.

10. **Version and Contributor Notes**
   - Optional final block for tracking edit history or attribution beyond YAML metadata.  
   - Use plain text or a short bullet list.

### Article Length and Depth

- Keep each article focused on a single core concept.  
- If a topic requires more than five major sections, consider dividing it into a numbered series.  
- Avoid duplicating long derivations already explained elsewhere; crosslink instead.  
- Use short summaries and links rather than repeating full explanations from related articles.  

### Editing Tables and KaTeX in Zettlr

> **Known Editor Behavior (Zettlr):**
> 
> - Zettlr’s live preview cannot toggle seamlessly between rendered and raw Markdown views.  
> - To edit tables or complex KaTeX blocks:
>   1. Open **Preferences → Markdown** and enable *Show Markdown Source*.
>   2. **Restart Zettlr** to activate raw mode.
>   3. Edit the table manually in plain text.
>   4. Save the file, then revert the setting and restart again to return to preview mode.
> - Changes made in raw Markdown are always preserved; changes made in rendered view may not persist.
> 
> *Tip:* If frequent table or math editing is required, consider using an external Markdown editor (Typora, Obsidian, or VS Code) and then reopen the file in Zettlr for KaTeX rendering.

### Revision and Version Control

- All official edits to the WCB Canon must be committed to the Git repository with clear, descriptive commit messages.  
- Use branch names that describe the change (e.g., `update-style-guide`, `revise-binaries-structure`).  
- Tag major versions of the Style Guide and Canon with semantic labels (e.g., `v1.0`, `v1.1-draft`).  
- Avoid editing directly on `main` — use feature branches and merge through review.  
- Always ensure YAML headers and section structure remain valid before pushing commits.

> **Goal:** Maintain a transparent, traceable editorial history while ensuring that every file in the Canon remains synchronized and style-compliant.

