from pathlib import Path

# Look in the current folder (where the script lives & runs)
folder = Path(".")

# Output files
abstracts_out = folder / "Canon_Abstracts.md"
missing_out = folder / "Abstracts_Missing.md"
covered_out = folder / "Abstracts_Covered.md"

abstracts = []
abstract_files = []
missing = []

for md_file in folder.glob("*.md"):
    text = md_file.read_text(encoding="utf-8")

    if "## Abstract" in text:
        start = text.find("## Abstract")
        end = text.find("---\n\n---", start)
        if end == -1:  # fallback if no ending marker found
            end = len(text)
        abstract_block = text[start:end].strip()
        abstracts.append(f"# {md_file.name}\n\n{abstract_block}\n")
        abstract_files.append(md_file.name)
    else:
        missing.append(f"- {md_file.name}")

# Sort lists
abstract_files.sort()
missing.sort()

# Write collected abstracts into one file
with open(abstracts_out, "w", encoding="utf-8") as f:
    f.write("# Canon Abstracts Compendium\n\n")
    f.write("\n\n---\n\n".join(abstracts))

# Write missing list
with open(missing_out, "w", encoding="utf-8") as f:
    f.write("# Files Missing Abstracts\n\n")
    f.write("\n".join(missing))

# Write covered list
with open(covered_out, "w", encoding="utf-8") as f:
    f.write("# Files With Abstracts (Alphabetical)\n\n")
    f.write("\n".join(f"- {name}" for name in abstract_files))

print(f"Done. Compiled {len(abstracts)} abstracts, {len(missing)} files missing, {len(abstract_files)} files covered.")
