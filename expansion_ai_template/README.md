# Expansion AI (current-compatible note)

The older `init_eAI.c` / `PatrolSettings.json` community template was removed because it uses an outdated API (`eAIDynamicPatrol.Create`) and causes compile errors with current Expansion AI builds.

## Current Expansion AI paths
- Profile AI settings: `ServerProfile/ExpansionMod/Settings/AISettings.json`
- Mission patrol settings: `dayzOffline.deerisle/expansion/settings/AIPatrolSettings.json`

## Important
- Do **not** add `#include "$profile:ExpansionMod/AI/Patrols/init_eAI.c"` in `init.c` with current Expansion AI.
- Do **not** call `InitDynamicPatrols();` from `init.c`.
- Current Expansion AI initializes patrol logic from the mod itself and reads patrol config from the mission `expansion/settings` folder.

## Recommended usage
1. Copy `ServerProfile/ExpansionMod/Settings/AISettings.json` into your real server profile folder.
2. Start the server once with Expansion AI loaded so it can generate default mission AI settings if needed.
3. Edit `dayzOffline.deerisle/expansion/settings/AIPatrolSettings.json` after it has been generated, or replace it with your own valid file.
