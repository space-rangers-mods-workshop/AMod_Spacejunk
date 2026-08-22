# Byte-level patch of Lang_spacejunk.txt (cp1251), ASCII-only edits.
# Applies the documented ExecuteCodeFromString read-back rule from
# script-functions/Script_functions_list.txt:4183:
#   - a NEW return var must be declared with a concrete type (int/str) IN the block;
#   - a return var that is ALSO passed as an input needs no declaration.
# Adds SFT() log messages at the UpdateObjects read-back to confirm on the
# 2025 build. Decodes/encodes cp1251 losslessly so all Cyrillic is preserved.
#
# Reproducibility: apply this AFTER patches/strip_sft_comments.py to a FRESH
# copy of denballakh's original Lang_spacejunk.txt (src/). On the already-fixed
# committed src/ the count asserts fail (patterns already replaced), which is
# expected — this is a historical record of the exact old->new substitutions.

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
    # --- UpdateObjects: fix read-back (pass itemArray as input+return) + SFT diagnostics ---
    (
        "0=itemArray = ExecuteCodeFromString(GenerateCodeStringFromBlock(path+'Functions.'+objtype+'.Update'), 'itemArray');",
        (
            "0=SFT('SJ UpdateObjects: calling '+objtype+' Update');"
            + NL
            + "0=itemArray = ExecuteCodeFromString(GenerateCodeStringFromBlock(path+'Functions.'+objtype+'.Update'), 'itemArray', newarray(1), 'itemArray');"
            + NL
            + "0=SFT('SJ UpdateObjects: '+objtype+' read-back OK, dim='+ArrayDim(itemArray));"
        ),
        1,
    ),
    # --- Items SortKey.Code: result is int ---
    ("0=result = -ItemCost(object);", "0=int result = -ItemCost(object);", 1),
    ("0=result = -ItemType(object);", "0=int result = -ItemType(object);", 1),
    ("0=result = -ItemLevel(object);", "0=int result = -ItemLevel(object);", 1),
    ("0=result = -(1000 * ItemCost(object)) / (ItemSize(object) + 1);", "0=int result = -(1000 * ItemCost(object)) / (ItemSize(object) + 1);", 1),
    ("0=result = -ItemSize(object);", "0=int result = -ItemSize(object);", 1),
    ("0=result = EqSpecial(object);", "0=int result = EqSpecial(object);", 1),
    # --- Ships SortKey.Code: result is int ---
    ("0=result = -HullHP(ShipItems(object,0));", "0=int result = -HullHP(ShipItems(object,0));", 1),
    ("0=result = -ShipType(object);", "0=int result = -ShipType(object);", 1),
    ("0=result = Dist(object, Player());", "0=int result = Dist(object, Player());", 1),
    # --- Utils string results (4 blocks share the init line) ---
    ("0=result = '';", "0=str result = '';", 4),
    # --- Utils.Replace final result ---
    ("0=result = s;", "0=str result = s;", 1),
    # --- Utils.GetPageText ---
    (
        "0=result = DeleteTags(Format(CT('Script.AMod_Spacejunk.Text.PageText'), '<L>', GSJ_current_page + 1, '<R>', GSJ_total_pages + 1));",
        "0=str result = DeleteTags(Format(CT('Script.AMod_Spacejunk.Text.PageText'), '<L>', GSJ_current_page + 1, '<R>', GSJ_total_pages + 1));",
        1,
    ),
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
