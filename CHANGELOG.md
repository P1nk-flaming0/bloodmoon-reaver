# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [1.0.4] - 2026-08-09

### Changed

- **Updated** `README.md` and changed Howl ability description.

---

## [1.0.3] - 2026-08-07

### Fixed

- **HOWL (`PF#FWPX-#.BAF`):** Increased the time lapse between a successful summoning call and the creature’s appearance by introducing an execution pause in the summoner’s script.

---

## [1.0.2] - 2026-08-06

### Changed

- **Updated** `README.md`, `pf#werefighter.ini` and `SETUP-PF#werefighter.tp2` with author and mod details & information. `README.md` is displayed upon WeiDU start-up.

---

## [1.0.1] - 2026-08-05

### Fixed

- **Beast Within Balance (`PF#FWPAY.SPL`):** Fixed an issue where berserk attacks per round were scaling too high; reduced character Attacks Per Round (APR) by 1 while under the berserk condition.

---

## [1.0.0] - 2026-08-03

### Added

- **Bloodmoon Reaver** fighter kit for BG2EE and EET (`pf#werefighter-core`), focused on controlled lycanthropy.
- Shapeshifting progression: **Wolf Form** (level 1), **Werewolf Form** (level 4), **Greater Werewolf Form** (level 14), and **Shapeshift at Will** (level 18).
- Form abilities **Howl** (wolf) and **Growl** (werewolf / greater werewolf), plus **Predatory Senses** and the **Beast Within** risk/mastery system.
- Unique high-level abilities: **Blood Frenzy**, **Feral Rage**, **Call of the Hunt**, and **Thick-Skinned**, alongside standard martial HLAs.
- Optional **Dynamic Werewolf Portraits** component (`pf#werefighter-portraits`) that swaps character portraits on shapeshift.

### Changed

- N/A — initial public release.

### Fixed

- N/A — initial public release.

[unreleased]: https://github.com/USER/REPO/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/USER/REPO/releases/tag/v1.0.0
