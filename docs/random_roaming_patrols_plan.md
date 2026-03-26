# Synthèse des patrouilles random/roaming ajoutées (version thématique)

## Périmètre et méthode
- Source de trajectoires: `routes_expansion.json`.
- Fenêtre de jeu demandée: `x=2000..11000` et `z=5000..8000`.
- 30 patrouilles conservées, avec **5 waypoints** chacune.
- Réaffectation par **zone** + **faction** + **loadout** + **table de loot** dédiée.

## Mini-histoire (lore de répartition)
- **Ouest**: zones plus "habitées" et routes secondaires -> guides/civils, patrouilles police locales, contrebande opportuniste.
- **Centre**: corridors logistiques disputés -> raiders, bandits et détachements paramilitaires (Gorka/TTSKO/East).
- **Est**: secteurs techniques et sensibles -> stalkers mercenaires, détachements West, équipes NBC et escortes médicales.

## Répartition par zone
- Ouest (x < 5000): **5** patrouilles
- Centre (5000 ≤ x < 8000): **15** patrouilles
- Est (x ≥ 8000): **10** patrouilles

## Répartition des loadouts utilisés
- `BanditLoadout`: **3**
- `DeerIsleGuideLoadout`: **2**
- `DeerIsleMedicLoadout`: **2**
- `DeerIsleRaiderLoadout`: **3**
- `DeerIsleSmugglerLoadout`: **1**
- `DeerIsleStalkerLoadout`: **3**
- `EastLoadout`: **3**
- `GorkaLoadout`: **3**
- `NBCLoadout`: **2**
- `PoliceLoadout`: **1**
- `SurvivorLoadout`: **1**
- `TTSKOLoadout`: **3**
- `WestLoadout`: **3**


## Cache centralisé "Basic Needs"
- Nouveau fichier: `profiles/ExpansionMod/AI/LootDrops/BasicNeedsCache.json`.
- Tous les PNJ AI (patrouilles de `AIPatrolSettings.json`) utilisent maintenant `LootDropOnDeath: BasicNeedsCache.json`.
- Les items de besoins de base (nourriture/eau) ont été retirés des autres caches pour éviter les doublons.

## Tables de loot disponibles
- `BasicNeedsCache.json` (centralisé pour tous les AI)
- `BanditWarCache.json`
- `CivilianGuideCache.json`
- `EastConvoyCache.json`
- `ExpeditionWestCache.json`
- `NBCResponseCache.json`
- `PoliceMedicCache.json`

## Détail des 30 patrouilles

| Patrouille | Zone | Faction | Loadout | LootDrop | #WP | Centre (x,z) |
|---|---|---|---|---|---:|---:|
| CentralRoutes_Random_Raiders_01 | Centre (5000 ≤ x < 8000) | Raiders | DeerIsleRaiderLoadout | BasicNeedsCache.json | 5 | 6697.6, 6250.0 |
| CentralRoutes_Random_Raiders_04 | Est (x ≥ 8000) | West | WestLoadout | BasicNeedsCache.json | 5 | 8726.8, 5142.0 |
| CentralRoutes_Random_Raiders_07 | Centre (5000 ≤ x < 8000) | Raiders | BanditLoadout | BasicNeedsCache.json | 5 | 7208.8, 5025.6 |
| CentralRoutes_Random_Raiders_10 | Centre (5000 ≤ x < 8000) | Raiders | EastLoadout | BasicNeedsCache.json | 5 | 7059.6, 5450.8 |
| CentralRoutes_Random_Raiders_13 | Centre (5000 ≤ x < 8000) | Raiders | BanditLoadout | BasicNeedsCache.json | 5 | 7501.2, 5020.0 |
| CentralRoutes_Random_Raiders_16 | Est (x ≥ 8000) | Mercenaries | DeerIsleStalkerLoadout | BasicNeedsCache.json | 5 | 8719.2, 7975.2 |
| CentralRoutes_Random_Raiders_19 | Ouest (x < 5000) | Civilian | SurvivorLoadout | BasicNeedsCache.json | 5 | 4988.0, 6515.6 |
| CentralRoutes_Random_Raiders_22 | Centre (5000 ≤ x < 8000) | Raiders | BanditLoadout | BasicNeedsCache.json | 5 | 7186.8, 6140.8 |
| CentralRoutes_Random_Raiders_25 | Est (x ≥ 8000) | Mercenaries | NBCLoadout | BasicNeedsCache.json | 5 | 10499.2, 7978.4 |
| CentralRoutes_Random_Raiders_28 | Est (x ≥ 8000) | Mercenaries | DeerIsleStalkerLoadout | BasicNeedsCache.json | 5 | 10374.8, 7979.2 |
| CentralRoutes_Random_Smugglers_03 | Est (x ≥ 8000) | Mercenaries | DeerIsleStalkerLoadout | BasicNeedsCache.json | 5 | 10586.0, 7978.0 |
| CentralRoutes_Random_Smugglers_06 | Ouest (x < 5000) | Guards | PoliceLoadout | BasicNeedsCache.json | 5 | 4960.0, 6373.2 |
| CentralRoutes_Random_Smugglers_09 | Centre (5000 ≤ x < 8000) | West | TTSKOLoadout | BasicNeedsCache.json | 5 | 5915.2, 6408.8 |
| CentralRoutes_Random_Smugglers_12 | Est (x ≥ 8000) | Guards | DeerIsleMedicLoadout | BasicNeedsCache.json | 5 | 10276.8, 7959.2 |
| CentralRoutes_Random_Smugglers_15 | Centre (5000 ≤ x < 8000) | West | TTSKOLoadout | BasicNeedsCache.json | 5 | 5180.4, 6346.0 |
| CentralRoutes_Random_Smugglers_18 | Est (x ≥ 8000) | West | WestLoadout | BasicNeedsCache.json | 5 | 10430.4, 7984.0 |
| CentralRoutes_Random_Smugglers_21 | Centre (5000 ≤ x < 8000) | Raiders | DeerIsleRaiderLoadout | BasicNeedsCache.json | 5 | 5080.0, 6340.0 |
| CentralRoutes_Random_Smugglers_24 | Centre (5000 ≤ x < 8000) | West | TTSKOLoadout | BasicNeedsCache.json | 5 | 5019.2, 6420.0 |
| CentralRoutes_Random_Smugglers_27 | Centre (5000 ≤ x < 8000) | Raiders | EastLoadout | BasicNeedsCache.json | 5 | 7030.8, 6133.6 |
| CentralRoutes_Random_Smugglers_30 | Est (x ≥ 8000) | West | WestLoadout | BasicNeedsCache.json | 5 | 8681.6, 5137.2 |
| CentralRoutes_Random_Stalkers_02 | Ouest (x < 5000) | Civilian | DeerIsleGuideLoadout | BasicNeedsCache.json | 5 | 2703.2, 7993.2 |
| CentralRoutes_Random_Stalkers_05 | Est (x ≥ 8000) | Mercenaries | NBCLoadout | BasicNeedsCache.json | 5 | 8548.0, 7979.6 |
| CentralRoutes_Random_Stalkers_08 | Centre (5000 ≤ x < 8000) | West | GorkaLoadout | BasicNeedsCache.json | 5 | 7489.2, 5904.4 |
| CentralRoutes_Random_Stalkers_11 | Centre (5000 ≤ x < 8000) | Raiders | DeerIsleRaiderLoadout | BasicNeedsCache.json | 5 | 7095.6, 6137.2 |
| CentralRoutes_Random_Stalkers_14 | Centre (5000 ≤ x < 8000) | West | GorkaLoadout | BasicNeedsCache.json | 5 | 7348.8, 6148.0 |
| CentralRoutes_Random_Stalkers_17 | Ouest (x < 5000) | Raiders | DeerIsleSmugglerLoadout | BasicNeedsCache.json | 5 | 2871.6, 7985.6 |
| CentralRoutes_Random_Stalkers_20 | Centre (5000 ≤ x < 8000) | Raiders | EastLoadout | BasicNeedsCache.json | 5 | 7386.8, 5893.2 |
| CentralRoutes_Random_Stalkers_23 | Centre (5000 ≤ x < 8000) | West | GorkaLoadout | BasicNeedsCache.json | 5 | 7268.0, 6142.4 |
| CentralRoutes_Random_Stalkers_26 | Est (x ≥ 8000) | Guards | DeerIsleMedicLoadout | BasicNeedsCache.json | 5 | 8667.6, 5110.0 |
| CentralRoutes_Random_Stalkers_29 | Ouest (x < 5000) | Civilian | DeerIsleGuideLoadout | BasicNeedsCache.json | 5 | 4982.4, 6471.2 |
