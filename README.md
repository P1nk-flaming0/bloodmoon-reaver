# Bloodmoon Reaver

[![Version](https://img.shields.io/badge/version-dev-blue.svg)](PF%23werefighter/SETUP-PF%23werefighter.tp2)
[![Engine](https://img.shields.io/badge/engine-BG2EE%20%7C%20EET-informational.svg)](#compatibility--prerequisites)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license--legal)

A **Fighter** kit for Baldur's Gate II: Enhanced Edition that masters lycanthropy through steel discipline — shifting between wolf and werewolf forms, hunting with predatory senses, and risking the Beast Within.

**Author:** [AUTHOR_NAME]  
**Download:** [DOWNLOAD_URL] · **Forum:** [FORUM_THREAD_URL] · **Source:** [GITHUB_REPO_URL]  
**Contact:** [CONTACT_INFO]

---

## Overview

**Bloodmoon Reaver** is a custom fighter kit for BG2EE (and EET). Where a typical warrior trusts plate and polearm, the Reaver trusts claw, fang, and willpower — a soldier who has learned to leash a lunar curse rather than deny it.

> Born with the “gift,” or scarred by a fated encounter, this warrior has been afflicted with lycanthropy. Through discipline and rigorous training, they progressively learn how to master their curse — honing the predator’s instincts alongside the soldier’s resolve until they become an apex hunter that blends the tactical mind of a man with the raw, terrifying power of the beast.

**Components**

| # | Component | Notes |
|---|-----------|--------|
| 0 | **Bloodmoon Reaver Kit** | Core kit, resources, game-table patches |
| 1 | **Dynamic Werewolf Portrait Switching** *(optional)* | Opcode 107 portrait swaps; requires user-supplied BMPs in the Portraits folder |

---

## Kit Statistics & Progression

### Kit description

Exact class-selection text from `setup.tra` (`@12` / `@13`):

> **BLOODMOON REAVER:** Born with the "gift" or scarred by a fated encounter, this warrior has been afflicted with lycanthropy. Through discipline and rigorous training, \<PRO_HESHE\> progressively learns how to master \<PRO_HISHER\> curse. By honing the predator’s instincts alongside the soldier’s resolve, \<PRO_HESHE\> becomes apex hunter that blends the tactical mind of a man with the raw, terrifying power of the beast.
>
> **Advantages:**  
> **PREDATORY SENSES:** The werewolf’s heightened instincts grant infravision and an increasing chance to detect invisible creatures. These senses sharpen as the warrior gains experience, eventually providing immunity to magical blindness.
>
> – May shapeshift into a wolf form once per day per 2 levels (begins with 1 use at 1st level). While in wolf form, the shapeshifter may use Howl at will.
>
> **HOWL:** A primal call to the wild, usable only in wolf form. When sounded in natural surroundings, the howl may summon 1–5 wolves to fight alongside the caller. These allies remain for 3 turns or until slain.
>
> – May shapeshift into a werewolf form once per day per 2 levels (gains first use at 4th level). While in werewolf form, the shapeshifter may use Growl at will.
>
> **GROWL:** A fearsome roar usable only in werewolf form. Enemies within 30 feet must save vs. Spell at +3 or flee in panic. At higher levels, the saving throw bonus is removed. Growl has a level-based, increasing chance to trigger automatically on a critical hit.
>
> – At 14th level, the werewolf form is upgraded to a greater werewolf form.  
> – At 18th level, the warrior may freely alternate between natural, wolf, and werewolf forms at will.
>
> **BEAST WITHIN:** While learning how to practice control over \<PRO_HISHER\> curse, the warrior runs the risk of losing \<PRO_HISHER\> humanity when faced with particularly stressful combat conditions. Under such circumstances, there is a chance of \<PRO_HESHE\> going berserk and transforming into an uncontrollable beast, blindly attacking friend or foe alike.  
> – As the warrior grows in experience and mental discipline, the likelihood of losing control steadily diminishes until it is mastered entirely at higher levels.  
> – Once the frenzy subsides, the toll on the warrior's body is severe; \<PRO_HESHE\> is forced back into human form, left briefly unconscious, and suffers from profound physical exhaustion and diminished morale.
>
> **Disadvantages:**  
> – Cannot wear any armor.

**Class / races:** Fighter kit (`ADD_KIT`), available to human, dwarf, gnome, elf, half-elf, halfling, and half-orc (`K_F_*` kit table rows).

### Shapeshifting form breakdown

Form stats from innate description strings (`@64`–`@66`):

| | **Wolf** | **Werewolf** | **Greater Werewolf** |
|---|---|---|---|
| **Unlocked** | Level 1 (uses scale with level) | Level 4 (uses scale with level) | Level 14 *(upgrades werewolf)* |
| **Strength** | 18 | 19 | 21 |
| **Dexterity** | — | 16 | 20 |
| **Constitution** | — | 18 | 25 |
| **Base AC** | 5 | 1 | −6 |
| **Attacks / round** | 2 | 2 | 3 |
| **Damage** | 1d8+1 piercing | 2d4+4 slashing | 2d6+6 slashing |
| **Weapon enchantment** | +1 | +2 | +4 |
| **Magic resistance** | — | 20% | 40% |
| **Elemental / other** | Cold 100%, Electricity 50%, Magic cold 100%; increased movement | — | Fire/Cold/Electricity/Acid 50%; regenerates 1 HP / 2 sec |
| **Form ability** | **Howl** (wilderness wolf summons, 3 turns) | **Growl** (30' panic) | Same hybrid toolkit, stronger chassis |
| **Endgame** | At **18**, **Shapeshift at Will** — free alternation between natural, wolf, and werewolf | | |

### Level progression matrix

Translated from `PF#werefighter/2da/pf#clbfw.2da` (`GA_` = gain innate use, `AP_` = apply passive / permanent ability):

| Level | Gained abilities |
|------:|------------------|
| **1** | Shapeshift: **Wolf** (1 use); **Predatory Senses**; Beast Within controller (`PF#FWSCR`); Beast Within risk (`PF#FWBRS`) |
| **2** | — |
| **3** | +1 **Wolf** use |
| **4** | Shapeshift: **Werewolf** (1st use) |
| **5** | +1 **Wolf** use |
| **6** | +1 **Werewolf** use |
| **7** | +1 **Wolf** use |
| **8** | +1 **Werewolf** use |
| **9** | +1 **Wolf** use |
| **10** | +1 **Werewolf** use |
| **11** | — |
| **12** | +1 **Werewolf** use |
| **13** | — |
| **14** | **Greater Werewolf** upgrade (`PF#FWAGW`) |
| **15–17** | — |
| **18** | **Shapeshift at Will** (`PF#FWLSS`); Beast Within **mastery / removal** (`PF#FWRMB`) |
| **19–40** | — *(no further CLAB grants; HLAs from level 20+)* |

### High-level abilities (HLA)

From `LUPF#FW.2DA` plus HLA text in `setup.tra`:

| HLA | Limit | Notes |
|-----|------:|-------|
| Standard fighter HLA tree (`SPCL900`–`SPCL909` subset) | per vanilla rules | Shared martial HLAs |
| **Blood Frenzy** (`PF#FWABF`) | 1 | On kill: short surge of speed, ferocity, and strength (~3 rounds after last kill) |
| **Feral Rage** (`PF#FWAFR`) | 5 | +2 Str, claws as +6, immunities (charm/hold/fear/maze/imprisonment/stun/sleep) |
| **Call of the Hunt** (`PF#FWASU`) | 1 | Summons two **Nightfang Stalkers** (spirit-werewolves) for 3 turns |
| **Thick-Skinned** (`PF#FWATS`) | 2 | +5% slash / pierce / crush / missile resistance per pick |

---

## Compatibility & Prerequisites

### Supported games

| Game | Status |
|------|--------|
| **BG2EE** (SoA + ToB) | Primary target (EE kit helpers via `fl#add_kit_ee`) |
| **EET** | Expected to work when installed on the BG2EE portion of an EET stack |
| **BG:EE / SoD** | Not the design target; do not assume support without testing |
| **IWDEE** | Not verified by the current installer (`GAME_IS` gates are not present) |

> **Siege of Dragonspear (Steam / GOG):** If you use SoD content in a multi-game stack, install **[DLC Merger](https://github.com/Argent77/A7-DlcMerger)** (or equivalent) **before** EET / large WeiDU mods, per community best practice.

### Mod compatibility notes

- Uses standard WeiDU `ADD_KIT` + EE kit extensions; safe to combine with most kit packs if install order is sane.
- Patches shared tables (`SPLPROT.2DA`, `STATDESC.2DA`, `SPLSTATE.IDS`, vanilla `SPCL905.SPL`) with `UNLESS` / duplicate guards — install **after** large overhauls that also touch those files when possible (e.g. SCS, kit meta-mods), or be prepared to reinstall this mod last among kit add-ons.
- Optional portrait component only edits this mod’s shapeshift spells; it does not conflict with NPC portrait packs.

---

## Installation Instructions

### Standard WeiDU install

1. Extract the mod archive so that you have:
   - `SETUP-PF#werefighter.exe` (or platform launcher) in the **game folder**, and  
   - the `PF#werefighter/` directory beside it (containing `SETUP-PF#werefighter.tp2` and resources).
2. **Windows:** double-click `SETUP-PF#werefighter.exe`, or run it from a console in the game directory.
3. **macOS:** run the `.command` WeiDU wrapper from the game directory (or invoke `weidu` / `setup-*.command` per your WeiDU package).
4. **Linux:** run `./setup-pf#werefighter` / `weidu SETUP-PF#werefighter.tp2` from the game directory.
5. Choose language (**English**), then install:
   - **Bloodmoon Reaver Kit** (required)
   - **Install Portrait Switching** (optional — see portraits note below)

To uninstall or reinstall, re-run the same setup binary and follow WeiDU’s prompts.

### Project Infinity

1. Open **Project Infinity** and add / refresh your game install.
2. Place this mod in your PI mods folder (or point PI at the extracted package).
3. Enable **Bloodmoon Reaver** in the install selection; optionally enable the portrait subcomponent.
4. Sort with other kit mods (typically among fighter kits; after DLC Merger / EET core if applicable).
5. Install the selected stack.

### Optional portraits

If you install **Dynamic Werewolf Portrait Switching**, provide custom BMPs named exactly:

- Human / natural: `pffwn0L.bmp`, `pffwn0M.bmp`  
- (Werewolf / wolf portraits ship with the mod as `pffwb0*` / `pffww0*` and are copied to `%USER_DIRECTORY%/portraits`.)

You may install the component first and drop the human portraits in later.

---

## Credits & Tools

- **WeiDU** — Wes Weimer, The Bigg, Wisp, and contributors  
- **Near Infinity** — resource inspection & editing  
- **Project Infinity** / Infinity Auto Packager — AL|EN (ALIEN Quake) and contributors  
- **Gibberlings Three** kit tutorials & community documentation (CamDawg and others)  
- **Beamdog** — Enhanced Edition engine  
- `fl#add_kit_ee` — EE kit table helper used by this installer  

---

## License & Legal

This mod is offered for personal, non-commercial use under the terms indicated by the project license badge (**MIT** unless superseded by an explicit `LICENSE` file in the repository).

**Infinity Engine disclaimer:** This mod is a fan-made, unofficial add-on. It is **not** affiliated with, endorsed by, or connected to Beamdog, BioWare, Black Isle, Interplay, Hasbro, or Wizards of the Coast. *Baldur's Gate*, *Icewind Dale*, and related marks are trademarks of their respective owners. All rights to the original games belong to their copyright holders.

---

*Questions, bugs, or pull requests: [CONTACT_INFO] · [GITHUB_REPO_URL] · [FORUM_THREAD_URL]*
