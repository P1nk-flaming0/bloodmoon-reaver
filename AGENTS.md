# Agent instructions — Bloodmoon Reaver

This repository is a WeiDU Infinity Engine kit mod. Follow these rules when making changes that ship as a new release.

## When a change is a new release

Treat work as a **new release** when it is (or will be) published to players: install fixes, kit/balance changes, new components, compatibility work, or user-facing docs that ship with the package.

Do **not** bump the version for pure WIP, local experiments, or uncommitted scratch work unless the user explicitly asks to cut a release.

When in doubt, ask the user whether to bump and which SemVer level to use.

## SemVer quick guide (this project)

This project follows [Semantic Versioning](https://semver.org/) and [Keep a Changelog](https://keepachangelog.com/).

| Bump | Use when | Example |
| :--- | :------- | :------ |
| **PATCH** `X.Y.(Z+1)` | Backward-compatible bug / install fixes; no new kit features | Install crash on BG1EE |
| **MINOR** `X.(Y+1).0` | Backward-compatible new capability (new component, notable new support marketed as a feature) | New optional component |
| **MAJOR** `(X+1).0.0` | Breaking change for existing installs / saved games / public kit contract | Removing a kit ability players rely on |

For install-only compatibility fixes that do not change kit behavior on already-supported games, prefer **PATCH**.

## Release checklist (mandatory)

After deciding the new version `vX.Y.Z`, update **all** of the following in the same change set. Do not leave any reference on the previous version.

### 1. `PF#werefighter/SETUP-PF#werefighter.tp2`

Update the WeiDU `VERSION` directive:

```weidu
VERSION ~vX.Y.Z~
```

### 2. `pf#werefighter.ini`

Update Project Infinity metadata (keep the `v` prefix to match git tags / WeiDU):

```ini
Version = vX.Y.Z
```

Also keep `Games = …` aligned with real supported engines when compatibility changes (e.g. `BGEE, BG2EE, EET, IWDEE`).

### 3. `README.md`

Update every inscribed version badge / version string, especially:

```markdown
[![Version](https://img.shields.io/badge/version-vX.Y.Z-blue.svg)](https://github.com/P1nk-flaming0/bloodmoon-reaver)
```

If engine support changed, update the engine badge and the Compatibility table in the same pass.

### 4. `CHANGELOG.md`

1. Move items out of `## [Unreleased]` (if any) into a new section.
2. Add a dated section **above** older releases:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Fixed

- Concise player-facing summary of what was broken and what works now.

### Changed

- Only if behavior, docs, or support matrix changed without being a pure bugfix.

### Added

- Only for new user-facing features / components / resources.
```

3. Use the right Keep a Changelog category:

| Section | Use for |
| :------ | :------ |
| **Fixed** | Bugs, install failures, incorrect behavior |
| **Changed** | Behavior or docs changes that are not fixes; support-matrix wording |
| **Added** | New features, components, or resources |
| **Removed** | Removed features / files |
| **Deprecated** | Still present but discouraged |

4. Prefer short, concrete bullets (resource names / platforms when helpful). Match the tone of existing entries.
5. Do **not** invent footer compare/tag links for every version unless the repo already maintains them consistently; keep the top `## [Unreleased]` section present.

## Suggested workflow for agents

1. Finish the functional change.
2. Confirm with the user (or prior instruction) the SemVer bump and release date.
3. Update `.tp2` → `.ini` → `README.md` → `CHANGELOG.md` together.
4. Grep the repo for the **old** version string (`vX.Y.(Z-1)` or whatever was current) and clear stragglers in those release surfaces.
5. Only create a git commit / tag / GitHub release if the user explicitly asks.

## Out of scope unless asked

- Do not bump version on every small edit in a long WIP session.
- Do not rewrite older changelog sections.
- Do not push tags or create GitHub releases unless requested.
