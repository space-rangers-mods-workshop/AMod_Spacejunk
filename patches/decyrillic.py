# Byte-level patch of Lang_spacejunk.txt (cp1251), ASCII-only edits.
# Makes the on-screen panel language-neutral so one source serves both Rus/Eng:
# replaces Cyrillic words with colored Latin-letter markers (no brackets, like the
# existing RaceColors / TLColors scheme) and ASCII units.
#
# Reproducibility: apply this AFTER patches/strip_sft_comments.py to a FRESH copy of
# denballakh's original Lang_spacejunk.txt (src/). On the already-fixed committed src/
# the count asserts fail (patterns already replaced), which is expected — this is a
# historical record of the exact old->new substitutions (same contract as patch_readback.py).
# The marker palette is documented in AMod_Spacejunk.yaml.
# Decodes/encodes cp1251 losslessly so the remaining Cyrillic comments are preserved.

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # repo root (patches/ -> root)
path = BASE / "src" / "Lang_spacejunk.txt"

with open(path, "rb") as f:
    raw = f.read()
text = raw.decode("cp1251")

NL = "\r\n" if "\r\n" in text else "\n"

# (old, new, expected_count)
repls = [
    # --- Items.Display: tons unit -> ASCII ---
    ("0=size = ''+ItemSize(object)+' т';", "0=size = ''+ItemSize(object)+' t';", 1),
    # --- table words -> colored Latin markers (language-neutral; 10 distinct RGB) ---
    ("TypeDescription=предметы", "TypeDescription=<color=180,255,220>itm</color>", 1),
    ("TypeDescription=кор", "TypeDescription=<color=180,150,255>shp</color>", 1),
    ("Description=цена" + NL, "Description=<color=255,255,255>cst</color>" + NL, 1),
    ("Description=тип", "Description=<color=170,170,170>typ</color>", 2),  # Items + Ships
    ("Description=ТУ", "Description=<color=0,255,255>lvl</color>", 1),
    ("Description=цена/<br>вес", "Description=<color=255,160,50>c/w</color>", 1),
    ("Description=вес", "Description=<color=130,180,255>wgt</color>", 1),
    ("Description=акрин", "Description=<color=220,175,90>acr</color>", 1),
    ("Description=ХП", "Description=<color=0,220,0>hp</color>", 1),
    ("Description=расстояние", "Description=<color=110,130,150>dst</color>", 1),
]

ok = True
for old, new, exp in repls:
    c = text.count(old)
    status = "OK" if c == exp else "FAIL"
    if c != exp:
        ok = False
    print(f"[{status}] count={c} (expected {exp})  {old[:70]!r}")

if not ok:
    print("\nAborting: pattern counts not as expected, file NOT modified.")
    sys.exit(1)

for old, new, _ in repls:
    text = text.replace(old, new)

with open(path, "wb") as f:
    f.write(text.encode("cp1251"))

print(f"\nApplied {len(repls)} replacements (newline={NL!r}). Wrote {len(text.encode('cp1251'))} bytes.")
