## 📖 Description

**AMod_Spacejunk** adds an object viewer panel to the space map (star map), showing every item and ship in the current system at a glance.

The panel has two modes — **Items** and **Ships** — switched with toggle buttons:

- **Items:** name, race, tech level (TL), price, weight and distance; sortable by price, type, tech level, price/weight, weight, and the special *acrin* property.
- **Ships:** name, race, distance and HP/hull size; sortable by HP, type and distance (the player's own ship is excluded).

Race is shown as a colored marker, including Kling subraces, pirate clans and custom factions. Long lists are paged (up to 200 objects), and a button centers the map on the selected object.

## 📦 Installation instructions

### 🤖 Automatic — Mod Organizer 2

The easiest way is to install the mod through **Mod Organizer 2** using the plugin for Space Rangers HD: A War Apart:

- [Mod Organizer 2 plugin for Space Rangers HD](https://www.nexusmods.com/spacerangersawarapart/mods/57)

Download the mod with MO2 mod manager and deploy it — the plugin places the mod in the correct `Mods\` folder for you.

### ✋ Manual

1. Make sure the game loads mods from its `Mods\` folder (this requires the patched `Rangers.exe` — see the game's modding guide).
2. Download the latest release archive from the
   [GitHub releases page](https://github.com/space-rangers-mods-workshop/AMod_Spacejunk/releases/latest)
   (or the [Nexus Mods page](https://www.nexusmods.com/spacerangersawarapart/mods/59)).
3. Unpack the archive into the game's `Mods\` folder so that the mod folder ends up at:
   ```
   <game root>\Mods\Miscellaneous\AMod_Spacejunk
   ```
   (The folder must contain `ModuleInfo.txt` at its root — do not nest it an extra level down.)
4. Launch the game. The panel appears on the space map once you enter a system.

To remove the mod, delete the `AMod_Spacejunk` folder.

## ✨ Main features

- Item viewer: name, race, tech level, price, weight, distance.
- Ship viewer: name, race, distance, HP/hull size (player's ship excluded).
- Sorting in both modes (price, type, TL, price/weight, weight, acrin for items; HP, type, distance for ships).
- Colored race markers, incl. Kling subraces, pirate clans and custom factions.
- Paged list — up to 200 objects.
- Button to center the map on the selected object.

## 🎮 How to use

- Make sure the mod is loaded:
  [mod_loaded](./mod_loaded.png)
- When you **take off from a planet** (after loading a save or starting a new game), a vertical panel appears on the left:
  [collaped_panel](./collaped_panel.png)
- Click the **gray** part of the panel (not the blue one!). The panel expands and shows all the items ejected into space:
  [panel_junk](./panel_junk.png)
- The **+/-** buttons inside the panel let you switch between object viewing and sorting modes. Example with ship viewing:
  [panel_ship](./panel_ship.png)

## ✅ Requirements

No other mods required

## 🙏 Shout outs

- **LEOPARD** — drew the panel images.
- **Huk** — author of the original AMod_Spacejunk, made it possible to quickly find items ejected into space.
- **denballakh** — added the ability to find ships in addition to items, and published the readable sources.
- **ringill** — added English support and removed the LEOGraphicsMod dependency.

## 🔗 Source

- [https://github.com/space-rangers-mods-workshop/AMod_Spacejunk](https://github.com/space-rangers-mods-workshop/AMod_Spacejunk)

## ⚖️ Licence

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).**
