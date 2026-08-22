"""Build AMod_Spacejunk mod/ from readable sources (.scr route).

Run from workshop/AMod_Spacejunk:
    ..\\..\\.venv\\Scripts\\python.exe build_spacejunk.py

Prerequisite (one-time, via SRHD-XenoModKit): compile the stub scenario script
from the RSON project into mod/Data/Script/mod_spacejunk.scr:
    ..\\SRHD-XenoModKit\\srhd.cmd script build src\\Spacejunk.rson ^
        --scr mod\\Data\\Script\\mod_spacejunk.scr ^
        --lang tmp\\spacejunk_lang.txt --tools-root ..\\..\\workshop --overwrite
(No dialogs in Spacejunk.rson, so the lang fragment is empty; the mod's real
Lang.dat comes from src/Lang_spacejunk.txt, not from the RSON compile.)

The .scr stub carries the 3 engine code points (Top/Global, Init, Turn), each
delegating to the readable Script.AMod_Spacejunk block in Lang.dat via
ExecuteCodeFromString(GenerateCodeStringFromBlock(...)). Without the registered
Data/Script + CacheData + compiled .scr, InitCode (which sets sjMainPanel
Active=True) never runs and the panel stays invisible.

Layout produced (conventions taken from installed game reference mods):
  mod/ModuleInfo.txt            UTF-16 LE BOM, Dependence=LEOGraphicsMod
  mod/CFG/Main.dat              from src/Main_spacejunk.txt  fmt=HDMain  unsigned
  mod/CFG/CacheData.dat         from src/CacheData_spacejunk.txt fmt=HDCache  unsigned
  mod/CFG/Rus/Lang.dat          from src/Lang_spacejunk.txt  fmt=HDMain  signed
  mod/CFG/Eng/Lang.dat          same content as Rus (Script block is language-independent)
  mod/Data/Script/mod_spacejunk.scr   compiled stub (from Spacejunk.rson)

Source corrections (see AMod_Spacejunk.yaml acquire note):
  - src/Lang_spacejunk.txt has an appended closing `}` for the top-level
    `Script ~{` block (denballakh's file shipped one brace short).
  - src/Main_spacejunk.txt has the `Data ^{ Script ^{ mod_spacejunk=1,
    Script.mod_spacejunk } }` header restored (was stripped in Model A; the
    script registration is required, not dead).
"""
import sys
from pathlib import Path

import rangers.dat as d

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
MOD = ROOT / "mod"
CFG = MOD / "CFG"
RUS = CFG / "Rus"
ENG = CFG / "Eng"
SCRIPT = MOD / "Data" / "Script" / "mod_spacejunk.scr"

MODULEINFO = """Name=AMod_Spacejunk
Author=LEOPARD, Huk, denballakh, ringill
Conflict=
Dependence=LEOGraphicsMod
Priority=1
Section=Разное
SectionEng=Miscellaneous
Languages=Rus,Eng
SmallDescription=На форме космоса добавляется панелька-смотрелка, показывающая какой предмет и где лежит в системе
SmallDescriptionEng=Spacejunk viewer panel
FullDescription=На форме космоса добавляется панелька-смотрелка, показывающая какой предмет и где лежит в системе
FullDescriptionEng=A viewing panel is added to the space form, showing which item is located and where in the system
"""


def write_module_info():
    CFG.mkdir(parents=True, exist_ok=True)
    RUS.mkdir(parents=True, exist_ok=True)
    ENG.mkdir(parents=True, exist_ok=True)
    # UTF-16 LE with BOM
    (MOD / "ModuleInfo.txt").write_bytes(
        b"\xff\xfe" + MODULEINFO.encode("utf-16-le")
    )
    print("wrote mod/ModuleInfo.txt (UTF-16 LE BOM,", len(MODULEINFO), "chars)")


def read_source_text(src):
    """Decode a readable BlockPar source. denballakh's sources are win-1251
    (SRHD legacy codepage); rangers.DAT.from_txt only tries utf8/utf16."""
    data = src.read_bytes()
    if data[:2] == b"\xff\xfe":
        return data.decode("utf-16-le")
    if data[:2] == b"\xfe\xff":
        return data.decode("utf-16-be")
    try:
        return data.decode("utf8")
    except UnicodeDecodeError:
        return data.decode("cp1251")


def encode(src_rel, out_rel, fmt, sign):
    src = SRC / src_rel
    out = MOD / out_rel
    text = read_source_text(src)
    dat = d.DAT.from_str(text)
    dat.to_dat(out, fmt=fmt, sign=sign)
    b = out.read_bytes()
    ok = d.check_signed(b) == sign
    back = d.DAT.from_dat(out)
    print(f"encoded {out_rel}: fmt={dat.fmt} sign={sign} len={len(b)} reparse_fmt={back.fmt} sig_match={ok}")
    return out


def check_scr():
    if not SCRIPT.exists():
        print(
            "ERROR: missing compiled stub mod/Data/Script/mod_spacejunk.scr\n"
            "  compile it first via SRHD-XenoModKit (see module docstring).",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"scr present: {SCRIPT} ({SCRIPT.stat().st_size} bytes)")


def main():
    # sanity: sources exist
    for name in ["Main_spacejunk.txt", "Lang_spacejunk.txt", "CacheData_spacejunk.txt"]:
        if not (SRC / name).exists():
            print(f"ERROR: missing source {name}", file=sys.stderr)
            sys.exit(1)

    check_scr()
    write_module_info()
    encode("Main_spacejunk.txt", "CFG/Main.dat", "HDMain", False)
    encode("CacheData_spacejunk.txt", "CFG/CacheData.dat", "HDCache", False)
    encode("Lang_spacejunk.txt", "CFG/Rus/Lang.dat", "HDMain", True)
    # Script.AMod_Spacejunk is the engine code (language-independent) and lives
    # in Lang.dat, which SRHD loads per language. Emit Eng too so the script is
    # found regardless of the active game language (ModuleInfo declares Rus,Eng).
    encode("Lang_spacejunk.txt", "CFG/Eng/Lang.dat", "HDMain", True)
    print("build complete (.scr route: Data/Script + CacheData + restored Data.Script header)")


if __name__ == "__main__":
    main()
