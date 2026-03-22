# Expansion AI template for Deer Isle

This folder contains a drop-in server profile template for DayZ Expansion AI, sourced from the community setup package by Degrath.

## What is included
- `ServerProfile/ExpansionMod/Settings/AISettings.json`
- `ServerProfile/ExpansionMod/AI/Patrols/init_eAI.c`
- `ServerProfile/ExpansionMod/AI/Patrols/PatrolSettings.json`
- vanilla loadout JSON files

## Recommended use
1. Copy `ServerProfile/ExpansionMod/...` into your real server profile folder.
2. In `dayzOffline.deerisle/init.c`, add:

```c
#include "$profile:ExpansionMod/AI/Patrols/init_eAI.c"
```

3. Then call this in `main()` before it exits:

```c
InitDynamicPatrols();
```

## Notes
- This template is kept separate on purpose so the mission does not break on servers that do not yet run Expansion AI.
- The included package README states it supports Deer Isle patrol generation.
