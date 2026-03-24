# DeerIsle Expansion Quests setup notes

The quest pack in `profiles/ExpansionMod/Quests` was synced from:
- `Andrew-InTheBox/Dayz-Expansion-DeerIsle`

## Required mods/modules
For this quest set, the server must have:
- `@CF`
- `@DabsFramework`
- `@DayZ-Expansion-Bundle`
- `@DayZ-Expansion-Licensed`
- `@DayZ-Expansion-Animations`
- `@DeerIsle`

These quests use Expansion AI objective types and NPC classes (`eAI_*`, `ExpansionQuestNPCAI*`) provided by DayZ Expansion.

## Compatibility tweak done in this repo
This repository's `start.bat` does not include RedFalcon (`RFFS`) or SNAFU weapon mods.
To avoid missing-item errors, reward items that depended on those mods were replaced with vanilla/Expansion-safe rewards in:
- `profiles/ExpansionMod/Quests/Quests/300-Patrol-Bandits.json`
- `profiles/ExpansionMod/Quests/Quests/200-AICamp-Ashville.json`
- `profiles/ExpansionMod/Quests/Quests/220-AICamp-Mountainville.json`
- `profiles/ExpansionMod/Quests/Quests/390-Chain-PowerPlant.json`

## NPCs added
Quest NPC definitions included by this pack are:
- `QuestNPC_Peter_1.json`
- `QuestNPC_Steve_2.json`
- `QuestNPC_Board_3.json`
- `QuestNPC_Paul_Spire_4.json`
- `QuestNPC_Board_Spire_5.json`

Legacy placeholder NPC files (`QuestNPC_1/2/3.json`) were removed to avoid duplicate ID conflicts.

## Quest ID collision handling
The imported pack originally reused legacy IDs (`4, 5, 7-22`) already present in local `Quest_*.json` files.
To keep both sets side-by-side without collisions, imported quest IDs were remapped to:
- `4 -> 1004`, `5 -> 1005`
- `7..22 -> 1007..1022`

All `PreQuestIDs` and `FollowUpQuest` references in imported quest files were updated accordingly.


## Test coordinates (NPCs and quest boards)
Use these world coordinates for quick in-game testing of quest NPC/board interactions:

| ID | File | NPC Name | Position (X, Y, Z) |
|---:|---|---|---|
| 1 | `QuestNPC_Peter_1.json` | Peter | `7524.80, 87.68, 4618.89` |
| 2 | `QuestNPC_Steve_2.json` | Steve | `7504.69, 22.14, 4151.96` |
| 3 | `QuestNPC_Board_3.json` | Quest Board | `7519.64, 88.68, 4631.27` |
| 4 | `QuestNPC_Paul_Spire_4.json` | Paul | `5122.99, 59.22, 7974.46` |
| 5 | `QuestNPC_Board_Spire_5.json` | Quest Board | `5118.46, 60.50, 7977.06` |

### Quick test order
1. Go to ID `3` (board near Peter) and accept an available quest.
2. Talk to ID `1` (Peter) and ID `2` (Steve) to validate giver/turn-in interactions.
3. Move to ID `5` and ID `4` (Spire area) to validate second quest hub.

> Tip: If a quest is not visible, check `QuestSettings.json` (`EnableQuests = 1`) and restart the server after edits.


## AIPatrol customization (Faction/Loadout)
AIPatrol objectives are imported and enabled with the following defaults:
- `Objective_AIP_1.json`: `Faction = Raiders`, `Loadout = DeerIsleRaiderLoadout`
- `Objective_AIP_2.json`: `Faction = Mercenaries`, `Loadout = DeerIsleStalkerLoadout`
- `Objective_AIP_3.json`: `Faction = Mercenaries`, `Loadout = DeerIsleSmugglerLoadout`

To use your own custom setup, edit these fields in each file:
- `AISpawn.Faction`
- `AISpawn.Loadout`
- optional: `AISpawn.NumberOfAI`, `AccuracyMin`, `AccuracyMax`, `Waypoints`

