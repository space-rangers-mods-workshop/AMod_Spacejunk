"""Remove dead //SFT debug lines from Lang_spacejunk.txt (cp1251-preserving).

Only lines matching `0=//SFT(` are removed. Useful doc comments (lines like
`0=object - объект; result - ...` inside the _ObjType doc template) are kept.
Byte-level cp1251 decode/encode because the edit tool assumes UTF-8.

Reproducibility: apply this to a FRESH copy of denballakh's original
Lang_spacejunk.txt (src/), i.e. run it BEFORE the read-back patch below.
On the already-fixed committed src/ it is a no-op (no matching lines).
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # repo root (patches/ -> root)
SRC = BASE / "src" / "Lang_spacejunk.txt"

data = SRC.read_bytes()
text = data.decode("cp1251")
if "\r\n" in text:
    newline = "\r\n"
elif "\r" in text:
    newline = "\r"
else:
    newline = "\n"

lines = text.split(newline)
pattern = re.compile(r"^\s*0=//SFT\(")
kept = [ln for ln in lines if not pattern.match(ln)]
removed = len(lines) - len(kept)

assert removed >= 2, f"expected at least the 2 SJ debug lines removed, got {removed}"
out = newline.join(kept)
SRC.write_bytes(out.encode("cp1251"))
print(f"removed {removed} //SFT lines from {SRC.name}")
