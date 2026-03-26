# AI Loot Standardization Report

## Current state
- Thematic caches are active again (not only BasicNeeds).
- Elite patrols (highest AccuracyMax) rotate between multiple elite caches.
- Drop model: chaque patrouille utilise un cache thématique qui inclut aussi un bloc de besoins de base (effet "2 caches": thématique + général).
- Les 30 patrouilles ajoutées `CentralRoutes_*` sont maintenant uniquement hostiles (plus de faction Civilian).

## Lore narratif (intégré à Deer Isle + DayZ)

Dans la chronologie DayZ (univers ArmA/"Armaverse"), l’effondrement social suit l’apparition d’un pathogène hautement contagieux ayant transformé la majeure partie de la population en infectés violents. Les survivants immunisés — rares, méfiants, et souvent organisés en milices locales — composent l’essentiel des forces encore actives.

Sur Deer Isle, l’archipel devient une zone-refuge paradoxale: suffisamment isolée pour attirer les convois, suffisamment riche en infrastructures pour déclencher des guerres de contrôle. Les anciens pôles logistiques (ports, routes côtières, axes intérieurs) se fragmentent alors en micro-fronts:

- **Camp Eagle** et les secteurs techniques proches servent de points d’appui à des groupes mieux équipés (mercenaires/recon) qui cherchent l’accès aux stocks militaires et au renseignement.
- **Area 42** et les zones de sécurité renforcée deviennent des objectifs de haute valeur, d’où la présence d’unités élites et de caches plus spécialisées.
- **KMUC / axes centraux** concentrent les flux d’armes, munitions, batteries et pièces de maintenance; les patrouilles hostiles y tournent en permanence pour couper les routes.
- **Littoral et petites localités** restent des poches de survie opportuniste (contrebandiers, groupes de récupération), où l’on échange encore nourriture, eau, et médicaments de base.

Le modèle de loot retenu reflète cette histoire: chaque faction garde sa signature (thématique), mais tous les combattants transportent aussi un socle de survie (nourriture/eau/soins), cohérent avec une guerre d’attrition longue où même les unités d’élite restent dépendantes de ressources simples.

*Sources externes utilisées pour cadrage lore:* synthèses DayZ Lore/Survivors/Infected (timeline Armaverse + survivants immunisés), et ressources communauté Deer Isle (zones/POI, progression de map).

## Suggestions d’évolutions futures

1. **Hostilité par anneaux de zone**
   - Forcer Raiders/Mercenaries sur les axes Tier haut, et réserver Guards uniquement à des escortes d’événements.
2. **Escalade dynamique des caches élite**
   - Passer de 2 à 4 variantes élite (recon, assaut, marksman, support) selon `AccuracyMax` + secteur.
3. **Narrative events**
   - Déclencher des mini-événements (convoi, crash, purge NBC) qui basculent temporairement les caches de certaines patrouilles.
4. **Équilibrage anti-snowball**
   - Diminuer légèrement les chances d’optiques/suppresseurs sur les élites si le taux de kill joueur dépasse un seuil serveur.
5. **Journal in-game / mission hooks**
   - Ajouter une petite chaîne de "fragments radio" reliant Camp Eagle, Area 42 et KMUC pour donner un fil narratif aux rotations de patrouilles.

## Lore étendu (Deer Isle x univers DayZ)

Quand l’infection se propage en Chernarus, l’ordre civil s’effondre en quelques semaines. Les survivants immunisés — minoritaires — deviennent des nomades armés, des convoyeurs, ou des chefs de micro-factions. Ce qui reste des institutions (forces locales, milices, ex-unités régulières) se transforme en réseaux opportunistes où la logistique vaut plus que l’idéologie.

Sur Deer Isle, l’archipel joue le rôle d’une plaque tournante périphérique: assez isolée pour retarder les vagues d’infectés massives, assez connectée pour attirer les convois de récupération. Les routes centrales et côtières deviennent alors des lignes de front permanentes. Chaque groupe y impose sa doctrine:

- les **Raiders** contrôlent les goulots et vivent de l’attrition (munitions, pillage, sabotage des axes),
- les **Mercenaries / Stalkers** opèrent autour des zones à haute valeur (renseignement, stocks techniques, surveillance),
- les **Smugglers** exploitent les liaisons secondaires (côtes, points de passage discrets),
- les unités **élite** maintiennent des poches de supériorité locale avec du matériel plus rare.

Les lieux stratégiques déjà présents dans la configuration (Camp Eagle, Area 42, corridors KMUC et routes centrales) sont interprétés comme des nœuds de contrôle: qui tient ces nœuds tient la circulation des batteries, des pièces détachées, des moyens d’observation et des médicaments.

Le modèle de drop actuel reflète ce récit: **cache thématique + socle de survie**. En pratique, chaque faction garde sa signature (type de munitions/outils/spécialités) tout en transportant de quoi survivre à court terme (eau, conserves, pansements), ce qui correspond à une guerre longue d’usure et de raids.

### Références web utilisées (cadrage lore)
- DayZ Wiki — Infected: https://dayz.fandom.com/wiki/Infected
- DayZ Wiki — Survivors: https://dayz.fandom.com/wiki/Survivors
- DayZ Wiki — Republic of Chernarus: https://dayz.fandom.com/wiki/Republic_of_Chernarus
- Deer Isle map (POI / repérage communauté): https://dayz.ginfo.gg/deerIsle/

## Suggestions de modifications futures

1. **Escalade territoriale par horaire serveur**
   - Faire varier la densité/qualité des patrouilles par tranche horaire (prime-time = plus d’élites sur axes centraux).
2. **Caches élite par spécialité**
   - Séparer les élites en sous-profils: recon (optiques), assaut (suppressors/5.56), marksman (308), support (médical + maintenance).
3. **Événements narratifs temporaires**
   - Déclencher des cycles (convoi, lockdown NBC, purge de secteur) qui changent temporairement les caches de 3–5 patrouilles.
4. **Hostilité contextuelle**
   - Garder quelques groupes “neutres armés” hors routes centrales, qui deviennent hostiles seulement selon déclencheur (tir, zone interdite, vol d’item clé).
5. **Progression joueur anti-snowball**
   - Diminuer légèrement les chances des objets très premium si le ratio kill/loot du serveur dépasse un seuil.

## Cache usage by patrol count
- `BanditWarCache.json`: **10** patrols
- `CivilianGuideCache.json`: **2** patrols
- `EastConvoyCache.json`: **3** patrols
- `EliteBlackOpsCache.json`: **2** patrols
- `EliteReconCache.json`: **2** patrols
- `FrontierHunterCache.json`: **6** patrols
- `NBCResponseCache.json`: **2** patrols
- `PoliceMedicCache.json`: **4** patrols
- `SmugglerCache.json`: **5** patrols
- `StalkerCache.json`: **5** patrols

## What each cache can drop
### `BanditWarCache.json`
- Ammo_762x39
- Ammo_545x39
- Ammo_556x45
- ImprovisedSuppressor
- WeaponCleaningKit
- TetracyclineAntibiotics
- Lockpick
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `BasicNeedsCache.json`
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `CivilianGuideCache.json`
- Compass
- Map
- BandageDressing
- HuntingKnife
- Battery9V
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen

### `EastConvoyCache.json`
- Ammo_545x39
- Ammo_762x39
- Compass
- ImprovisedSuppressor
- Battery9V
- Rag
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `EliteBlackOpsCache.json`
- Ammo_556x45
- Ammo_308Win
- Battery9V
- NVGoggles
- Rangefinder
- GPSReceiver
- M4_Suppressor
- ElectronicRepairKit
- Morphine
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `EliteReconCache.json`
- Ammo_308Win
- Ammo_556x45
- Rangefinder
- GPSReceiver
- NVGoggles
- PistolSuppressor
- Battery9V
- Epinephrine
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `Example.json`
- Ammo_545x39
- Ammo_545x39Tracer
- Ammo_762x39
- Ammo_762x39Tracer
- Ammo_556x45
- Ammo_556x45Tracer
- Ammo_762x54
- Ammo_762x54Tracer
- Ammo_308Win
- Ammo_308WinTracer
- FirstAidKit

### `ExpeditionWestCache.json`
- Ammo_556x45
- Ammo_308Win
- Rangefinder
- GPSReceiver
- M4_Suppressor
- ElectronicRepairKit
- Battery9V
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `FrontierHunterCache.json`
- Ammo_308Win
- Ammo_12gaSlug
- HuntingKnife
- Canteen
- Compass
- BandageDressing
- TacticalBaconCan
- SardinesCan
- PeachesCan
- WaterBottle

### `NBCResponseCache.json`
- CharcoalTablets
- TetracyclineAntibiotics
- MaskaNGasFilter
- AntiChemInjector
- BandageDressing
- Epinephrine
- Ammo_556x45
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen

### `PoliceMedicCache.json`
- Ammo_9x19
- Ammo_12gaRubberSlug
- HandcuffKeys
- Morphine
- Epinephrine
- BandageDressing
- PistolSuppressor
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen

### `RaidersCache.json`
- Ammo_762x39
- Ammo_556x45
- BandageDressing
- Lockpick
- PlateCarrierPouches_Green
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen

### `SmugglerCache.json`
- Ammo_9x19
- Ammo_12gaSlug
- Compass
- PortableGasStove
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

### `StalkerCache.json`
- Ammo_556x45
- Ammo_308Win
- Battery9V
- NVGoggles
- Morphine
- Rangefinder
- SardinesCan
- TacticalBaconCan
- PeachesCan
- WaterBottle
- Canteen
- BandageDressing

## Patrol positions (ALL patrols, existing + new)

| Patrol | Faction | Loadout | AccuracyMax | LootCache | #Waypoints | First waypoint (x,z) | Center (x,z) |
|---|---|---|---:|---|---:|---:|---:|
| Airfield_Raiders | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 6 | 5508.0, 3555.0 | 5540.2, 3518.8 |
| CampEagle_BlackOps | Mercenaries | DeerIsleStalkerLoadout | 0.88 | EliteBlackOpsCache.json | 5 | 8778.0, 3733.0 | 8756.6, 3783.6 |
| Area42_Stalkers | Mercenaries | DeerIsleStalkerLoadout | 0.84 | StalkerCache.json | 5 | 13379.0, 9849.6 | 13343.4, 9891.7 |
| EastHarbor_Smugglers | Raiders | DeerIsleSmugglerLoadout | 0.68 | SmugglerCache.json | 5 | 11363.6, 10103.4 | 11331.5, 10123.3 |
| KMUC_Hunters | West | DeerIsleRaiderLoadout | 0.76 | BanditWarCache.json | 5 | 7226.1, 11625.6 | 7263.8, 11636.9 |
| Georgestown_IslandGuides | Civilian | DeerIsleGuideLoadout | 0.51 | CivilianGuideCache.json | 4 | 4716.6, 4469.7 | 4720.4, 4541.9 |
| Bayville_CoastMedics | Guards | DeerIsleMedicLoadout | 0.48 | PoliceMedicCache.json | 4 | 10178.4, 12011.8 | 10148.6, 12060.0 |
| SouthCoast_RandomSmugglers | Raiders | DeerIsleSmugglerLoadout | 0.68 | SmugglerCache.json | 3 | 4716.6, 4469.7 | 5522.1, 3256.9 |
| CentralForest_RandomRaiders | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 3 | 7226.1, 11625.6 | 7566.8, 9836.9 |
| EastHills_RandomStalkers | Mercenaries | DeerIsleStalkerLoadout | 0.84 | StalkerCache.json | 3 | 10417.4, 7852.0 | 10586.4, 8260.4 |
| NorthShore_RandomGuides | Guards | DeerIsleGuideLoadout | 0.51 | CivilianGuideCache.json | 3 | 10178.4, 12011.8 | 5328.7, 13389.1 |
| CentralRoutes_Random_Raiders_01 | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 5 | 6636.0, 6320.0 | 6697.6, 6250.0 |
| CentralRoutes_Random_Stalkers_02 | Raiders | DeerIsleSmugglerLoadout | 0.68 | SmugglerCache.json | 5 | 2596.0, 7982.0 | 2703.2, 7993.2 |
| CentralRoutes_Random_Smugglers_03 | Mercenaries | DeerIsleStalkerLoadout | 0.84 | StalkerCache.json | 5 | 10670.0, 7978.0 | 10586.0, 7978.0 |
| CentralRoutes_Random_Raiders_04 | West | WestLoadout | 0.86 | EliteReconCache.json | 5 | 8814.0, 5136.0 | 8726.8, 5142.0 |
| CentralRoutes_Random_Stalkers_05 | Mercenaries | NBCLoadout | 0.82 | NBCResponseCache.json | 5 | 8444.0, 7972.0 | 8548.0, 7979.6 |
| CentralRoutes_Random_Smugglers_06 | Guards | PoliceLoadout | 0.62 | PoliceMedicCache.json | 5 | 4994.0, 6540.0 | 4960.0, 6373.2 |
| CentralRoutes_Random_Raiders_07 | Raiders | BanditLoadout | 0.76 | BanditWarCache.json | 5 | 7784.0, 5000.0 | 7208.8, 5025.6 |
| CentralRoutes_Random_Stalkers_08 | West | GorkaLoadout | 0.78 | FrontierHunterCache.json | 5 | 7572.0, 5902.0 | 7489.2, 5904.4 |
| CentralRoutes_Random_Smugglers_09 | West | TTSKOLoadout | 0.80 | FrontierHunterCache.json | 5 | 5816.0, 6408.0 | 5915.2, 6408.8 |
| CentralRoutes_Random_Raiders_10 | Raiders | EastLoadout | 0.74 | EastConvoyCache.json | 5 | 7086.0, 5488.0 | 7059.6, 5450.8 |
| CentralRoutes_Random_Stalkers_11 | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 5 | 6972.0, 6124.0 | 7095.6, 6137.2 |
| CentralRoutes_Random_Smugglers_12 | Guards | DeerIsleMedicLoadout | 0.56 | PoliceMedicCache.json | 5 | 10422.0, 7984.0 | 10276.8, 7959.2 |
| CentralRoutes_Random_Raiders_13 | Raiders | BanditLoadout | 0.76 | BanditWarCache.json | 5 | 7066.0, 5036.0 | 7501.2, 5020.0 |
| CentralRoutes_Random_Stalkers_14 | West | GorkaLoadout | 0.78 | FrontierHunterCache.json | 5 | 7432.0, 6170.0 | 7348.8, 6148.0 |
| CentralRoutes_Random_Smugglers_15 | West | TTSKOLoadout | 0.80 | FrontierHunterCache.json | 5 | 5278.0, 6350.0 | 5180.4, 6346.0 |
| CentralRoutes_Random_Raiders_16 | Mercenaries | DeerIsleStalkerLoadout | 0.84 | StalkerCache.json | 5 | 8480.0, 7980.0 | 8719.2, 7975.2 |
| CentralRoutes_Random_Stalkers_17 | Raiders | DeerIsleSmugglerLoadout | 0.68 | SmugglerCache.json | 5 | 3036.0, 7956.0 | 2871.6, 7985.6 |
| CentralRoutes_Random_Smugglers_18 | West | WestLoadout | 0.86 | EliteBlackOpsCache.json | 5 | 10310.0, 7992.0 | 10430.4, 7984.0 |
| CentralRoutes_Random_Raiders_19 | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 5 | 4998.0, 6338.0 | 4988.0, 6515.6 |
| CentralRoutes_Random_Stalkers_20 | Raiders | EastLoadout | 0.74 | EastConvoyCache.json | 5 | 7286.0, 5844.0 | 7386.8, 5893.2 |
| CentralRoutes_Random_Smugglers_21 | Raiders | DeerIsleRaiderLoadout | 0.74 | BanditWarCache.json | 5 | 4982.0, 6336.0 | 5080.0, 6340.0 |
| CentralRoutes_Random_Raiders_22 | Raiders | BanditLoadout | 0.76 | BanditWarCache.json | 5 | 7404.0, 6140.0 | 7186.8, 6140.8 |
| CentralRoutes_Random_Stalkers_23 | West | GorkaLoadout | 0.78 | FrontierHunterCache.json | 5 | 7036.0, 6144.0 | 7268.0, 6142.4 |
| CentralRoutes_Random_Smugglers_24 | West | TTSKOLoadout | 0.80 | FrontierHunterCache.json | 5 | 5080.0, 6342.0 | 5019.2, 6420.0 |
| CentralRoutes_Random_Raiders_25 | Mercenaries | NBCLoadout | 0.82 | NBCResponseCache.json | 5 | 10612.0, 7978.0 | 10499.2, 7978.4 |
| CentralRoutes_Random_Stalkers_26 | Guards | DeerIsleMedicLoadout | 0.56 | PoliceMedicCache.json | 5 | 8572.0, 5144.0 | 8667.6, 5110.0 |
| CentralRoutes_Random_Smugglers_27 | Raiders | EastLoadout | 0.74 | EastConvoyCache.json | 5 | 7170.0, 6140.0 | 7030.8, 6133.6 |
| CentralRoutes_Random_Raiders_28 | Mercenaries | DeerIsleStalkerLoadout | 0.84 | StalkerCache.json | 5 | 10474.0, 7976.0 | 10374.8, 7979.2 |
| CentralRoutes_Random_Stalkers_29 | Raiders | DeerIsleSmugglerLoadout | 0.68 | SmugglerCache.json | 5 | 4978.0, 6580.0 | 4982.4, 6471.2 |
| CentralRoutes_Random_Smugglers_30 | West | WestLoadout | 0.86 | EliteReconCache.json | 5 | 8758.0, 5144.0 | 8681.6, 5137.2 |
