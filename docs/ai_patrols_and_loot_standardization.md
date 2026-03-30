# AI Loot Tables par Faction / Loadout

## Règles actuelles
- `CanBeLooted` actif sur les IA patrol.
- `LootDropOnDeath` laissé vide (pas de cache au sol).
- Loot géré dans `InventoryCargo` des loadouts.

## Format copy/paste pour demander une mise à jour
```yaml
loadout: WestLoadout
patrouilles:
  - CentralRoutes_Elite_BlackOps_01
style: elite_player_like
inventory_cargo:
  - class: Ammo_556x45
    chance: 0.70
    qty_min: 0.60
    qty_max: 1.00
  - class: BandageDressing
    chance: 0.65
    qty_min: 0.00
    qty_max: 0.00
```

## BanditLoadout
Patrouilles: CentralRoutes_Random_Raiders_07, CentralRoutes_Random_Raiders_13, CentralRoutes_Random_Raiders_22

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_762x39` | 0.72 | 0.55 | 1.00 |
| Munitions | `Ammo_762x39` | 0.48 | 0.35 | 0.85 |
| Munitions | `Ammo_545x39` | 0.45 | 0.40 | 0.90 |
| Médical | `BandageDressing` | 0.62 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.42 | 0.00 | 0.00 |
| Médical | `TetracyclineAntibiotics` | 0.18 | 0.00 | 0.00 |
| Attachments | `ImprovisedSuppressor` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.33 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.38 | 0.00 | 0.00 |
| Utilitaire | `Lockpick` | 0.28 | 0.00 | 0.00 |
| Utilitaire | `Compass` | 0.16 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.28 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.26 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.18 | 0.00 | 0.00 |

## DeerIsleGuideLoadout
Patrouilles: Georgestown_IslandGuides, NorthShore_RandomGuides

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Utilitaire | `Compass` | 0.65 | 0.00 | 0.00 |
| Utilitaire | `Map` | 0.60 | 0.00 | 0.00 |
| Utilitaire | `HuntingKnife` | 0.45 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.40 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.58 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.35 | 0.00 | 0.00 |
| Médical | `TetracyclineAntibiotics` | 0.15 | 0.00 | 0.00 |
| Utilitaire | `Lockpick` | 0.08 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.36 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.42 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.30 | 0.00 | 0.00 |

## DeerIsleMedicLoadout
Patrouilles: Bayville_CoastMedics, CentralRoutes_Random_Smugglers_12, CentralRoutes_Random_Stalkers_26

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_9x19` | 0.55 | 0.50 | 1.00 |
| Munitions | `Ammo_12gaRubberSlug` | 0.26 | 0.30 | 0.80 |
| Médical | `BandageDressing` | 0.72 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.55 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.46 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.28 | 0.00 | 0.00 |
| Médical | `Epinephrine` | 0.36 | 0.00 | 0.00 |
| Médical | `SalineBagIV` | 0.24 | 0.00 | 0.00 |
| Médical | `TetracyclineAntibiotics` | 0.24 | 0.00 | 0.00 |
| Médical | `CharcoalTablets` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `HandcuffKeys` | 0.20 | 0.00 | 0.00 |
| Attachments | `PistolSuppressor` | 0.12 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.26 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.22 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.22 | 0.00 | 0.00 |

## DeerIsleRaiderLoadout
Patrouilles: Airfield_Raiders, KMUC_Hunters, CentralForest_RandomRaiders, CentralRoutes_Random_Raiders_01, CentralRoutes_Random_Stalkers_11, CentralRoutes_Random_Raiders_19, CentralRoutes_Random_Smugglers_21

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_762x39` | 0.70 | 0.55 | 1.00 |
| Munitions | `Ammo_762x39` | 0.46 | 0.35 | 0.85 |
| Munitions | `Ammo_556x45` | 0.38 | 0.30 | 0.80 |
| Médical | `BandageDressing` | 0.64 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.40 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.32 | 0.00 | 0.00 |
| Attachments | `ImprovisedSuppressor` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `Lockpick` | 0.30 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.42 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.18 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.32 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.20 | 0.00 | 0.00 |

## DeerIsleSmugglerLoadout
Patrouilles: EastHarbor_Smugglers, SouthCoast_RandomSmugglers, CentralRoutes_Random_Stalkers_02, CentralRoutes_Random_Stalkers_17, CentralRoutes_Random_Stalkers_29

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_9x19` | 0.58 | 0.50 | 1.00 |
| Munitions | `Ammo_12gaSlug` | 0.36 | 0.30 | 0.80 |
| Médical | `BandageDressing` | 0.58 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.34 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `PortableGasStove` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.28 | 0.00 | 0.00 |
| Utilitaire | `Lockpick` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `Compass` | 0.32 | 0.00 | 0.00 |
| Utilitaire | `Map` | 0.20 | 0.00 | 0.00 |
| Attachments | `PistolSuppressor` | 0.14 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.16 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.36 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.24 | 0.00 | 0.00 |

## DeerIsleStalkerLoadout
Patrouilles: CampEagle_BlackOps, Area42_Stalkers, EastHills_RandomStalkers, CentralRoutes_Random_Smugglers_03, CentralRoutes_Random_Raiders_16, CentralRoutes_Random_Raiders_28

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_556x45` | 0.70 | 0.60 | 1.00 |
| Munitions | `Ammo_556x45` | 0.52 | 0.35 | 0.85 |
| Munitions | `Ammo_308Win` | 0.50 | 0.40 | 0.90 |
| Munitions | `Ammo_9x19` | 0.42 | 0.30 | 0.75 |
| Médical | `BandageDressing` | 0.65 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.50 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.40 | 0.00 | 0.00 |
| Médical | `Epinephrine` | 0.32 | 0.00 | 0.00 |
| Utilitaire | `NVGoggles` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.75 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.52 | 0.00 | 0.00 |
| Utilitaire | `Rangefinder` | 0.25 | 0.00 | 0.00 |
| Utilitaire | `GPSReceiver` | 0.30 | 0.00 | 0.00 |
| Attachments | `M4_Suppressor` | 0.22 | 0.00 | 0.00 |
| Attachments | `PistolSuppressor` | 0.18 | 0.00 | 0.00 |
| Attachments | `ACOGOptic` | 0.20 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.35 | 0.00 | 0.00 |
| Nourriture/Hydratation | `TacticalBaconCan` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.26 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.26 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.25 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.38 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.40 | 0.00 | 0.00 |

## EastLoadout
Patrouilles: CentralRoutes_Random_Raiders_10, CentralRoutes_Random_Stalkers_20, CentralRoutes_Random_Smugglers_27

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_545x39` | 0.68 | 0.55 | 1.00 |
| Munitions | `Ammo_545x39` | 0.42 | 0.35 | 0.80 |
| Munitions | `Ammo_762x39` | 0.46 | 0.30 | 0.80 |
| Médical | `BandageDressing` | 0.60 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.38 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.45 | 0.00 | 0.00 |
| Utilitaire | `Compass` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `Rag` | 0.50 | 0.00 | 0.00 |
| Attachments | `ImprovisedSuppressor` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.25 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.18 | 0.00 | 0.00 |
| Utilitaire | `Map` | 0.14 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.32 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.28 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.20 | 0.00 | 0.00 |

## GorkaLoadout
Patrouilles: CentralRoutes_Random_Stalkers_08, CentralRoutes_Random_Stalkers_14, CentralRoutes_Random_Stalkers_23

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_308Win` | 0.48 | 0.35 | 0.85 |
| Munitions | `Ammo_12gaSlug` | 0.34 | 0.30 | 0.75 |
| Médical | `BandageDressing` | 0.62 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.40 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `HuntingKnife` | 0.45 | 0.00 | 0.00 |
| Utilitaire | `Compass` | 0.28 | 0.00 | 0.00 |
| Utilitaire | `Map` | 0.14 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.28 | 0.00 | 0.00 |
| Utilitaire | `SewingKit` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.22 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.24 | 0.00 | 0.00 |

## NBCLoadout
Patrouilles: CentralRoutes_Random_Stalkers_05, CentralRoutes_Random_Raiders_25

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_556x45` | 0.42 | 0.35 | 0.85 |
| Médical | `BandageDressing` | 0.62 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.42 | 0.00 | 0.00 |
| Médical | `Epinephrine` | 0.34 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.22 | 0.00 | 0.00 |
| Médical | `TetracyclineAntibiotics` | 0.34 | 0.00 | 0.00 |
| Médical | `CharcoalTablets` | 0.30 | 0.00 | 0.00 |
| Médical | `AntiChemInjector` | 0.22 | 0.00 | 0.00 |
| Divers | `MaskaNGasFilter` | 0.36 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.50 | 0.00 | 0.00 |
| Utilitaire | `GPSReceiver` | 0.20 | 0.00 | 0.00 |
| Attachments | `M4_Suppressor` | 0.16 | 0.00 | 0.00 |
| Attachments | `ACOGOptic` | 0.16 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.22 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.22 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.24 | 0.00 | 0.00 |

## PoliceLoadout
Patrouilles: CentralRoutes_Random_Smugglers_06

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_9x19` | 0.62 | 0.55 | 1.00 |
| Munitions | `Ammo_9x19` | 0.40 | 0.30 | 0.75 |
| Munitions | `Ammo_12gaRubberSlug` | 0.30 | 0.30 | 0.80 |
| Médical | `BandageDressing` | 0.66 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.48 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.30 | 0.00 | 0.00 |
| Médical | `Epinephrine` | 0.24 | 0.00 | 0.00 |
| Médical | `SalineBagIV` | 0.14 | 0.00 | 0.00 |
| Utilitaire | `HandcuffKeys` | 0.45 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.36 | 0.00 | 0.00 |
| Utilitaire | `Map` | 0.20 | 0.00 | 0.00 |
| Attachments | `PistolSuppressor` | 0.12 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.18 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.34 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.22 | 0.00 | 0.00 |

## TTSKOLoadout
Patrouilles: CentralRoutes_Random_Smugglers_09, CentralRoutes_Random_Smugglers_15, CentralRoutes_Random_Smugglers_24

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_545x39` | 0.65 | 0.55 | 1.00 |
| Munitions | `Ammo_308Win` | 0.35 | 0.30 | 0.75 |
| Munitions | `Ammo_12gaSlug` | 0.28 | 0.30 | 0.70 |
| Médical | `BandageDressing` | 0.60 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.38 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `Compass` | 0.22 | 0.00 | 0.00 |
| Utilitaire | `HuntingKnife` | 0.34 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.30 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.36 | 0.00 | 0.00 |
| Attachments | `ACOGOptic` | 0.14 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.18 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.32 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.24 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.22 | 0.00 | 0.00 |

## WestLoadout
Patrouilles: CentralRoutes_Random_Raiders_04, CentralRoutes_Random_Smugglers_18, CentralRoutes_Random_Smugglers_30

| Catégorie | Classe | Chance | Qty min | Qty max |
|---|---|---:|---:|---:|
| Munitions | `Ammo_556x45` | 0.72 | 0.60 | 1.00 |
| Munitions | `Ammo_556x45` | 0.55 | 0.40 | 0.90 |
| Munitions | `Ammo_308Win` | 0.45 | 0.40 | 0.90 |
| Munitions | `Ammo_9x19` | 0.50 | 0.40 | 0.90 |
| Médical | `BandageDressing` | 0.65 | 0.00 | 0.00 |
| Médical | `BandageDressing` | 0.52 | 0.00 | 0.00 |
| Médical | `Morphine` | 0.40 | 0.00 | 0.00 |
| Médical | `Epinephrine` | 0.30 | 0.00 | 0.00 |
| Médical | `SalineBagIV` | 0.18 | 0.00 | 0.00 |
| Utilitaire | `NVGoggles` | 0.20 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.75 | 0.00 | 0.00 |
| Utilitaire | `Battery9V` | 0.55 | 0.00 | 0.00 |
| Utilitaire | `Rangefinder` | 0.25 | 0.00 | 0.00 |
| Utilitaire | `GPSReceiver` | 0.30 | 0.00 | 0.00 |
| Attachments | `M4_Suppressor` | 0.22 | 0.00 | 0.00 |
| Attachments | `PistolSuppressor` | 0.18 | 0.00 | 0.00 |
| Attachments | `ACOGOptic` | 0.20 | 0.00 | 0.00 |
| Attachments | `ReflexOptic` | 0.35 | 0.00 | 0.00 |
| Nourriture/Hydratation | `TacticalBaconCan` | 0.28 | 0.00 | 0.00 |
| Nourriture/Hydratation | `PeachesCan` | 0.30 | 0.00 | 0.00 |
| Nourriture/Hydratation | `SardinesCan` | 0.32 | 0.00 | 0.00 |
| Nourriture/Hydratation | `WaterBottle` | 0.35 | 0.00 | 0.00 |
| Nourriture/Hydratation | `Canteen` | 0.25 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.40 | 0.00 | 0.00 |
| Utilitaire | `WeaponCleaningKit` | 0.25 | 0.00 | 0.00 |
| Utilitaire | `SewingKit` | 0.24 | 0.00 | 0.00 |
| Utilitaire | `DuctTape` | 0.45 | 0.00 | 0.00 |

