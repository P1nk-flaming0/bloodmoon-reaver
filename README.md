# Bloodmoon Reaver

[![Version](https://img.shields.io/badge/version-v1.0.4-blue.svg)](https://github.com/P1nk-flaming0/bloodmoon-reaver)
[![Engine](https://img.shields.io/badge/engine-BG2EE%20%7C%20EET-informational.svg)](#compatibility--prerequisites)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license--legal)

A **Fighter** kit for _Baldur's Gate II: Enhanced Edition_ and _Enhanced Edition Trilogy_ that masters lycanthropy through sheer discipline — shifting between wolf and werewolf forms, hunting with predatory senses, and risking the <span class="werewolf-accent">Beast Within</span>.

**Author:** [P1nk-flaming0](https://github.com/P1nk-flaming0)
**Download:** [_latest release_](https://github.com/P1nk-flaming0/bloodmoon-reaver/releases) · **Forum Thread:** _To be updated..._ · **Source:** [GitHub](https://github.com/P1nk-flaming0/bloodmoon-reaver)  
**Contact:** [p1nk-flaming0@fakemail.com](mailto:p1nk-flaming0@fakemail.com)

---

## Table of Contents

1. [Overview](#overview)
2. [Kit Statistics & Progression](#kit-statistics--progression)
   - [Kit Description](#kit-description)
   - [Shapeshifting Form Breakdown](#shapeshifting-form-breakdown)
   - [Level Progression Matrix](#level-progression-matrix)
   - [High-Level Abilities (HLAs)](#high-level-abilities-hlas)
3. [Compatibility & Prerequisites](#compatibility--prerequisites)
4. [Localization](#localization)
5. [Installation Instructions](#installation-instructions)
6. [Credits & Tools](#credits--tools)
7. [License & Legal](#license--legal)

---

## Overview

**Bloodmoon Reaver** introduces a specialized fighter kit centered on controlled lycanthropy. Stripped of heavy plate, the Reaver relies instead on heightened instincts, overwhelming physical prowess, and unyielding focus — fighting as a tactical warrior who channels predatory fury into precise martial strength.

<blockquote class="werewolf-accent--warn">
"What the weak call a curse, the disciplined call an edge..."
</blockquote>


### Mod Components

<div class="table-wrapper" markdown="1">

| Name                                        | Description                                               |
| :------------------------------------------ | :-------------------------------------------------------- |
| **Bloodmoon Reaver Kit** _(Core)_           | Core kit, class tables, abilities, and spells.            |
| **Dynamic Werewolf Portraits** _(Optional)_ | Swaps character portraits dynamically upon shapeshifting. |

</div>

---

<h2 class="werewolf-title" id="kit-statistics--progression">Kit Statistics & Progression</h2>

### Kit Description

<div class="pffw-stat-card" markdown="1">
**BLOODMOON REAVER:** Born with the "gift" or scarred by a fated encounter, this warrior has been afflicted with lycanthropy. Through discipline and rigorous training, they progressively learn how to master their curse, blending the tactical mind of a soldier with the raw power of the beast.

**ADVANTAGES:**

**PREDATORY SENSES:** The werewolf’s heightened instincts grant infravision and an increasing chance to detect invisible creatures. These senses sharpen as experience is gained, eventually conferring immunity to magical blindness.

– **Wolf Form:** May shapeshift into a wolf form once per day per 2 levels (begins with 1 use at 1st level). While in wolf form, the warrior may use <span class="werewolf-accent">Howl</span> at will.

> **HOWL:** Usable only in wolf form. When sounded in natural surroundings, the howl may summon nearby wolves to fight alongside the caller for 3 turns.
> <span class="pffw-gif-container"> 
![Howl](assets\gif\BaldursGateII-EnhancedEdition-v2.6.6.02026-08-0701-16-46-ezgif.com-video-to-gif-converter-howl-4w.gif)
> </span>

– **Werewolf Form:** May shapeshift into a werewolf form once per day per 2 levels (first use gained at 4th level). While in werewolf form, the warrior may use <span class="werewolf-accent">Growl</span> at will.

> **GROWL:** Usable only in werewolf form. Enemies within 30 feet must save vs. Spell at +3 or flee in panic. At higher levels, the saving throw bonus is removed. Growl also has an increasing chance to trigger automatically on a critical hit. <span class="pffw-gif-container">![Growl](assets\gif\BaldursGateII-EnhancedEdition-v2.6.6.02026-08-0702-33-06-ezgif.com-video-to-gif-converter-growl.gif)</span>

– At 14th level, Werewolf Form upgrades to **Greater Werewolf Form**.  
– At 18th level, gains **Shapeshift at Will** (unlimited alternation between natural, wolf, and werewolf forms).

>  <span class="werewolf-accent">**BEAST WITHIN:**</span> While mastering control over the curse, the warrior risks losing their humanity during intense combat. Under high stress, there is a chance of going berserk and transforming into an uncontrollable beast, attacking friend or foe alike.  
> – The risk diminishes as level increases, until full mastery is achieved at 18th level.  
> – When the frenzy ends, the physical toll forces the warrior back into human form, leaving them briefly unconscious, fatigued, and with reduced morale. <span class="pffw-gif-container">![Berserk](assets/gif/BaldursGateII-EnhancedEdition-v2.6.6.02026-08-0701-32-21-ezgif.com-video-to-gif-converter-berserk.gif)</span>

**DISADVANTAGES:**  
– Cannot wear any physical armor.

**Class & Race Restrictions:** Fighter kit. Available to Humans, Dwarves, Elves, Half-Elves, Gnomes, Halflings, and Half-Orcs. CANNOT be of GOOD alignment

</div>

---

<h2 class="werewolf-title" id="shapeshifting-form-breakdown">Shapeshifting Form Breakdown</h2>

<div class="table-wrapper" markdown="1">

| Attribute / Perk           |                 Wolf Form                 |               Werewolf Form                |                Greater Werewolf Form                |
| :------------------------- | :---------------------------------------: | :----------------------------------------: | :-------------------------------------------------: |
| **Unlocked At**            |                  Level 1                  |                  Level 4                   |                Level 14 _(Upgrade)_                 |
| **Strength**               |                    18                     |                     19                     |                         21                          |
| **Dexterity**              |                     —                     |                     16                     |                         20                          |
| **Constitution**           |                     —                     |                     18                     |                         25                          |
| **Base AC**                |                     5                     |                     1                      |                         −6                          |
| **Attacks / Round** (base) |                     2                     |                     2                      |                          3                          |
| **Base Damage**            |             1d8+1 (Piercing)              |              2d4+4 (Slashing)              |                  2d6+6 (Slashing)                   |
| **Weapon Enchantment**     |                    +1                     |                     +2                     |                         +4                          |
| **Magic Resistance**       |                     —                     |                    20%                     |                         40%                         |
| **Elemental / Special**    |  Cold 100%, Elec 50%<br>+Movement Speed   |                     —                      | Fire/Cold/Elec/Acid 50%<br>Regenerates 1 HP / 2 sec |
| **Unique Ability**         | <span class="werewolf-accent">Howl</span> | <span class="werewolf-accent">Growl</span> |     <span class="werewolf-accent">Growl</span>      |

</div>

_Note: At Level 18, all daily usage limits on shapeshifting are removed (Shapeshift at Will)._

---

### Level Progression Matrix

<div class="table-wrapper" markdown="1">

|  Level  | Ability / Perk Granted                                       |
| :-----: | :----------------------------------------------------------- |
|  **1**  | Gain **Shapeshift: Wolf** (1 use/day), **Predatory Senses**, and <span class="werewolf-accent">Beast Within</span> passive traits |
|  **3**  | +1 Wolf use/day                                              |
|  **4**  | Gain **Shapeshift: Werewolf** (1 use/day)                    |
|  **5**  | +1 Wolf use/day                                              |
|  **6**  | +1 Werewolf use/day                                          |
|  **7**  | +1 Wolf use/day                                              |
|  **8**  | +1 Werewolf use/day                                          |
|  **9**  | +1 Wolf use/day                                              |
| **10**  | +1 Werewolf use/day                                          |
| **12**  | +1 Werewolf use/day                                          |
| **14**  | **Greater Werewolf Form** upgrade                            |
| **18**  | **Shapeshift at Will** (unlimited uses) & <span class="werewolf-accent">Beast Within</span> Mastery (berserk risk removed) |
| **20+** | High-Level Abilities (HLAs) unlocked                         |

</div>

---

<h2 class="werewolf-title" id="high-level-abilities-hlas">High-Level Abilities (HLAs)</h2>

In addition to standard martial HLAs (_Hardiness_, _Critical Strike_, _Power Attack_), the Bloodmoon Reaver gains access to unique options:

<div class="table-wrapper" markdown="1">

| Ability              | Max Picks | Effect                                                                                    |
| :------------------- | :-------: | :---------------------------------------------------------------------------------------- |
| **Blood Frenzy**     |     1     | On kill: temporary surge in speed, attack power, and strength (~3 round duration).        |
| **Feral Rage**       |     5     | Grant +2 Strength, +6 claw enchantment, and total immunity to hard crowd control effects. |
| **Call of the Hunt** |     1     | Summons two spirit-werewolves (**Nightfang Stalkers**) to fight for 3 turns.              |
| **Thick-Skinned**    |     2     | Passively grants +5% resistance to all physical damage types per selection.               |

</div>

---

## Compatibility & Prerequisites

### Supported Game Engines

<div class="table-wrapper" markdown="1">

| Engine / Target                                            |  Compatibility  |
| :--------------------------------------------------------- | :-------------: |
| **Baldur's Gate II: Enhanced Edition** (SoA / ToB)         | Direct Support  |
| **Enhanced Edition Trilogy (EET)**                         | Fully Supported |
| **Baldur's Gate: Enhanced Edition / Siege of Dragonspear** | Fully Supported |
| **Icewind Dale: Enhanced Edition**                         |    Untested     |

</div>

> **Siege of Dragonspear / EET Note:** If installing on an install with Siege of Dragonspear, make sure to run **[DLC Merger](https://github.com/Argent77/A7-DlcMerger)** prior to installing WeiDU mods.

### Mod Load Order Guidelines

- Install **after** general overhaul mods that alter base game engine tables (`SPLPROT.2DA`, `STATDESC.2DA`).
- Install alongside or after other kitpacks.
- Safe to install before tactical AI mods like _Sword Coast Stratagems (SCS)_.

---

## Localization

- **English** — Primary / Native

_If you would like to submit a translation, feel free to open a Pull Request or contact the author._

---

## Installation Instructions

### Standard WeiDU Install

1. Extract the mod archive directly into your main game installation folder (where `BGMain.exe` resides).
2. Run the executable corresponding to your operating system:
   - **Windows:** Double-click `SETUP-PF#werefighter.exe`
   - **macOS:** Run `SETUP-PF#werefighter.command`
   - **Linux:** Run `./setup-pf#werefighter` in your terminal
3. Select your language and follow the on-screen prompts to install desired components.

### Project Infinity

1. Place the extracted mod directory in your Project Infinity downloads/mods folder.
2. Launch **Project Infinity** and refresh your mod list.
3. Select **Bloodmoon Reaver Kit** in your install sequence (placed after DLC Merger/EET core, among other kit additions).
4. Run the install sequence.

---

## Credits & Tools

- **WeiDU** — Wes Weimer, The Bigg, and Wisp
- **Near Infinity** — Jon Olav Hauglid, Astardo, and contributors
- **Project Infinity** — AL\|EN
- **Gibberlings Three Community** — Tutorials, documentation, and `fl#add_kit_ee` helpers
- **Beamdog** — For maintaining and expanding the Infinity Engine

---

## License & Legal

This mod is released under the **MIT License**.

_Disclaimer: Bloodmoon Reaver is an unofficial, fan-made mod for Baldur's Gate II: Enhanced Edition. It is not affiliated with or endorsed by Beamdog, Wizards of the Coast, or BioWare._
