# 🚀 AMod_Spacejunk

* **Name:** AMod_Spacejunk
* **Author:** LEOPARD, Huk, denballakh, ringill
* **License:** Creative Commons BY-NC-SA 4.0

### Summary

Spacejunk viewer panel

---

## 📖 Description

An object viewer panel on the star map showing all items and ships in the current system. Two modes — items and ships (toggle buttons). Items: name, race, tech level (TL), price, weight, distance; sortable by price, type, TL, price/weight, weight, and special (acrin) property. Ships: name, race, distance, HP/hull size; sortable by HP, type, and distance; the player's ship is excluded. Race is shown as a colored marker (incl. Kling subraces, pirate clans, custom factions). Paged viewing of up to 200 objects. A button centers the map on the selected object.

---

## 🔗 Based on

```yaml
based_on:
  - source: 🏛️ https://github.com/space-rangers-mods-museum/AMod_Spacejunk
    note: AMod_Spacejunk - Huk version
  - source: 🏛️ https://github.com/space-rangers-mods-museum/LEOGraphicsMod
    note: LEOGraphicsMod - resources
  - source: https://github.com/denballakh/Space-Rangers-Mods-Sources/tree/master/AnotherMods/AMod_Spacejunk
    note: AMod_Spacejunk - denballakh version

```

---

## 📁 Mod files

* [nexusmods](https://www.nexusmods.com/games/spacerangersawarapart/mods/59) — the mod page on Nexus Mods
* [latest release (archive)](https://github.com/space-rangers-mods-workshop/AMod_Spacejunk/releases/latest) — the mod packaged for download
* [`mod/`](mod/) — the assembled, ready-to-deploy mod folder (/Mods/Miscellaneous/AMod_Spacejunk)
* [`src/`](src/) — the readable sources

---

## ⚖️ License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).**

You are free to share and adapt it, provided you give credit to the authors, do not use it commercially, and release your derivative under the same license. For a mod derived from museum exhibits, that credit includes the original exhibit authors and a link back to the preserved originals. See [LICENSE](LICENSE) for the full license text.

---

## 🧬 Mod evolution

- LEOPARD drew the images
- Huk made it possible to quickly find items ejected into space
- denballakh added the ability to quickly find ships (in addition to items)
- ringill added support for the English version; removed the dependency on LEOGraphicsMod

---

## 🔍 How the sources were used

An ordered chain of repeatable steps - how the source data was processed, modified and transformed into a usable form: [AMod_Spacejunk.yaml](./AMod_Spacejunk.yaml)