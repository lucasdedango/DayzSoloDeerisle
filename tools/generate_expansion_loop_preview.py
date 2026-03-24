#!/usr/bin/env python3
"""Generate multiple preview Expansion AI loop patrols from routes_expansion.json.

Outputs:
- AIPatrolSettings.preview.generated.json (multiple LOOP patrol entries)
- loop_preview_report.json (metrics for each generated loop)
- loop_preview_map.svg (visual map preview)
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

Point = Tuple[float, float, float]

ROUTES_FILE = Path("routes_expansion.json")
OUTPUT_SETTINGS = Path("mpmissions/dayzOffline.deerisle/expansion/settings/AIPatrolSettings.preview.generated.json")
OUTPUT_REPORT = Path("profiles/ExpansionMod/AI/Generated/loop_preview_report.json")
OUTPUT_SVG = Path("profiles/ExpansionMod/AI/Generated/loop_preview_map.svg")


@dataclass
class Candidate:
    route_index: int
    raw_points: List[Point]
    simplified_points: List[Point]
    sampled_points: List[Point]
    closed_distance: float
    perimeter: float
    max_segment: float
    center: Tuple[float, float, float]


def dist(a: Point, b: Point) -> float:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dz = b[2] - a[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def polyline_length(points: Sequence[Point]) -> float:
    return sum(dist(a, b) for a, b in zip(points, points[1:]))


def polygon_area_2d(points: Sequence[Point]) -> float:
    if len(points) < 4:
        return 0.0

    ring = points[:-1] if points[0] == points[-1] else points
    if len(ring) < 3:
        return 0.0

    acc = 0.0
    for i in range(len(ring)):
        x1, z1 = ring[i][0], ring[i][2]
        x2, z2 = ring[(i + 1) % len(ring)][0], ring[(i + 1) % len(ring)][2]
        acc += (x1 * z2) - (x2 * z1)
    return abs(acc) * 0.5


def dedupe(points: Sequence[Point], min_dist: float = 1.0) -> List[Point]:
    if not points:
        return []
    out = [points[0]]
    for p in points[1:]:
        if dist(out[-1], p) >= min_dist:
            out.append(p)
    return out


def perpendicular_distance_2d(point: Point, start: Point, end: Point) -> float:
    x, z = point[0], point[2]
    x1, z1 = start[0], start[2]
    x2, z2 = end[0], end[2]
    if x1 == x2 and z1 == z2:
        return math.sqrt((x - x1) ** 2 + (z - z1) ** 2)
    num = abs((z2 - z1) * x - (x2 - x1) * z + x2 * z1 - z2 * x1)
    den = math.sqrt((z2 - z1) ** 2 + (x2 - x1) ** 2)
    return num / den


def rdp(points: Sequence[Point], epsilon: float) -> List[Point]:
    if len(points) < 3:
        return list(points)

    start = points[0]
    end = points[-1]
    max_dist = -1.0
    idx = -1

    for i in range(1, len(points) - 1):
        d = perpendicular_distance_2d(points[i], start, end)
        if d > max_dist:
            max_dist = d
            idx = i

    if max_dist > epsilon:
        left = rdp(points[: idx + 1], epsilon)
        right = rdp(points[idx:], epsilon)
        return left[:-1] + right

    return [start, end]


def resample_with_bounds(points: Sequence[Point], min_spacing: float, max_spacing: float) -> List[Point]:
    if len(points) < 2:
        return list(points)

    out = [points[0]]

    for nxt in points[1:]:
        prev = out[-1]
        segment = dist(prev, nxt)

        if segment < min_spacing * 0.55:
            continue

        if segment > max_spacing:
            steps = max(2, math.ceil(segment / max_spacing))
            for s in range(1, steps):
                t = s / steps
                interp = (
                    prev[0] + (nxt[0] - prev[0]) * t,
                    prev[1] + (nxt[1] - prev[1]) * t,
                    prev[2] + (nxt[2] - prev[2]) * t,
                )
                if dist(out[-1], interp) >= min_spacing * 0.7:
                    out.append(interp)
            if dist(out[-1], nxt) >= min_spacing * 0.7:
                out.append(nxt)
            continue

        if dist(out[-1], nxt) >= min_spacing:
            out.append(nxt)

    if dist(out[-1], points[-1]) > 1.0:
        out.append(points[-1])

    return out


def close_loop(points: Sequence[Point], close_threshold: float = 60.0) -> List[Point]:
    if len(points) < 3:
        return list(points)
    out = list(points)
    if dist(out[0], out[-1]) <= close_threshold:
        out[-1] = out[0]
    return out


def to_waypoints(points: Iterable[Point]) -> List[List[float]]:
    return [[round(p[0], 1), round(p[1], 1), round(p[2], 1)] for p in points]


def candidate_score(perimeter: float, point_count: int) -> float:
    return abs(perimeter - 1200.0) + abs(point_count - 48) * 10


def detect_candidates(
    routes: Sequence[Sequence[Point]],
    min_spacing: float,
    max_spacing: float,
    min_perimeter: float,
    max_perimeter: float,
    max_segment_limit: float,
    max_compactness: float,
    min_area: float,
) -> List[Candidate]:
    all_candidates: List[Candidate] = []

    for idx, route in enumerate(routes):
        if len(route) < 14:
            continue

        raw = dedupe(route, min_dist=1.0)
        if len(raw) < 14:
            continue

        closed_d = dist(raw[0], raw[-1])
        if closed_d > 70.0:
            continue

        simplified = rdp(raw, epsilon=8.0)
        simplified = dedupe(simplified, min_dist=4.0)
        simplified = close_loop(simplified, close_threshold=70.0)

        sampled = resample_with_bounds(simplified, min_spacing=min_spacing, max_spacing=max_spacing)
        sampled = close_loop(sampled, close_threshold=80.0)

        if len(sampled) < 16 or len(sampled) > 110:
            continue

        perimeter = polyline_length(sampled)
        if perimeter < min_perimeter or perimeter > max_perimeter:
            continue

        area = polygon_area_2d(sampled)
        if area < min_area:
            continue
        compactness = (perimeter * perimeter) / (4.0 * math.pi * area)
        if compactness > max_compactness:
            continue

        segments = [dist(a, b) for a, b in zip(sampled, sampled[1:])]
        if not segments:
            continue
        max_seg = max(segments)
        if max_seg > max_segment_limit:
            continue
        if dist(sampled[0], sampled[-1]) > 5.0:
            continue

        cx = sum(p[0] for p in sampled) / len(sampled)
        cy = sum(p[1] for p in sampled) / len(sampled)
        cz = sum(p[2] for p in sampled) / len(sampled)

        all_candidates.append(
            Candidate(
                route_index=idx,
                raw_points=list(raw),
                simplified_points=simplified,
                sampled_points=sampled,
                closed_distance=closed_d,
                perimeter=perimeter,
                max_segment=max_seg,
                center=(cx, cy, cz),
            )
        )

    return sorted(all_candidates, key=lambda c: candidate_score(c.perimeter, len(c.sampled_points)))


def select_distinct_loops(candidates: Sequence[Candidate], loop_count: int, min_center_gap: float) -> List[Candidate]:
    selected: List[Candidate] = []

    for cand in candidates:
        is_far_enough = True
        for s in selected:
            if dist(cand.center, s.center) < min_center_gap:
                is_far_enough = False
                break
        if not is_far_enough:
            continue

        selected.append(cand)
        if len(selected) >= loop_count:
            break

    return selected


def build_patrol(name: str, waypoints: List[List[float]]) -> dict:
    return {
        "Name": name,
        "Persist": 0,
        "Faction": "Raiders",
        "Formation": "Column",
        "FormationScale": 1.0,
        "FormationLooseness": 0.2,
        "Units": [
            "eAI_SurvivorM_Rolf",
            "eAI_SurvivorM_Seth",
            "eAI_SurvivorF_Irena",
        ],
        "NumberOfAI": 4,
        "NumberOfAIMax": 0,
        "Behaviour": "LOOP",
        "LootingBehaviour": "",
        "Speed": "JOG",
        "UnderThreatSpeed": "SPRINT",
        "DefaultStance": "STANDING",
        "DefaultLookAngle": 0.0,
        "CanBeLooted": 1,
        "LootDropOnDeath": "RaidersCache.json",
        "UnlimitedReload": 1,
        "SniperProneDistanceThreshold": 250.0,
        "AccuracyMin": 0.32,
        "AccuracyMax": 0.58,
        "ThreatDistanceLimit": 650.0,
        "NoiseInvestigationDistanceLimit": 400.0,
        "MaxFlankingDistance": 180.0,
        "EnableFlankingOutsideCombat": 0,
        "DamageMultiplier": 1.1,
        "DamageReceivedMultiplier": 0.9,
        "HeadshotResistance": 0.0,
        "ShoryukenChance": 0.0,
        "ShoryukenDamageMultiplier": 0.0,
        "CanSpawnInContaminatedArea": 0,
        "CanBeTriggeredByAI": 1,
        "MinDistRadius": 130.0,
        "MaxDistRadius": 500.0,
        "DespawnRadius": 700.0,
        "MinSpreadRadius": 9.0,
        "MaxSpreadRadius": 32.0,
        "Chance": 1.0,
        "DespawnTime": 60.0,
        "RespawnTime": 900.0,
        "LoadBalancingCategory": "Patrol",
        "ObjectClassName": "",
        "WaypointInterpolation": "UniformCubic",
        "UseRandomWaypointAsStartPoint": 1,
        "Waypoints": waypoints,
        "LoadoutFile": "DeerIsleRaiderLoadout",
    }


def write_svg(candidates: Sequence[Candidate], output: Path) -> None:
    width = 1200
    height = 900
    padding = 40
    colors = ["#ff595e", "#1982c4", "#8ac926", "#ffca3a", "#6a4c93", "#ff924c", "#00b4d8", "#2a9d8f"]

    xs = [p[0] for c in candidates for p in c.sampled_points]
    zs = [p[2] for c in candidates for p in c.sampled_points]

    min_x, max_x = min(xs), max(xs)
    min_z, max_z = min(zs), max(zs)

    span_x = max(1.0, max_x - min_x)
    span_z = max(1.0, max_z - min_z)
    scale = min((width - 2 * padding) / span_x, (height - 2 * padding) / span_z)

    def project(p: Point) -> Tuple[float, float]:
        x = padding + (p[0] - min_x) * scale
        y = height - (padding + (p[2] - min_z) * scale)
        return (x, y)

    lines: List[str] = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    lines.append('<rect width="100%" height="100%" fill="#111827"/>')
    lines.append('<text x="20" y="30" fill="#e5e7eb" font-size="18" font-family="monospace">Expansion Loop Preview (generated)</text>')

    for i, cand in enumerate(candidates):
        color = colors[i % len(colors)]
        pts = [project(p) for p in cand.sampled_points]
        points_attr = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        lines.append(f'<polyline points="{points_attr}" fill="none" stroke="{color}" stroke-width="2.5"/>')

        cx, cy = project(cand.center)
        lines.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{color}"/>')
        lines.append(
            f'<text x="{cx + 8:.1f}" y="{cy - 8:.1f}" fill="{color}" font-size="12" font-family="monospace">L{i+1} (r{cand.route_index})</text>'
        )

    legend_y = height - 20 * len(candidates) - 15
    lines.append(f'<rect x="{width - 360}" y="{legend_y - 18}" width="340" height="{20 * len(candidates) + 20}" fill="#1f2937" rx="8"/>')

    for i, cand in enumerate(candidates):
        color = colors[i % len(colors)]
        y = legend_y + i * 20
        lines.append(f'<text x="{width - 340}" y="{y}" fill="{color}" font-size="12" font-family="monospace">L{i+1}: route={cand.route_index}, wp={len(cand.sampled_points)}, perim={cand.perimeter:.0f}m, maxSeg={cand.max_segment:.1f}m</text>')

    lines.append('</svg>')
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--loops", type=int, default=6, help="Number of loops to generate")
    parser.add_argument("--min-spacing", type=float, default=22.0)
    parser.add_argument("--max-spacing", type=float, default=46.0)
    parser.add_argument("--min-perimeter", type=float, default=450.0)
    parser.add_argument("--max-perimeter", type=float, default=2200.0, help="Avoid loops that are too large")
    parser.add_argument("--max-segment", type=float, default=58.0, help="Reject candidates with segment gaps above this")
    parser.add_argument("--min-center-gap", type=float, default=850.0, help="Distance between loop centers to diversify map coverage")
    parser.add_argument("--max-compactness", type=float, default=5.5, help="Lower is more circular/compact (1.0 is perfect circle)")
    parser.add_argument("--min-area", type=float, default=12000.0, help="Reject tiny loops with very small enclosed area")
    args = parser.parse_args()

    routes = json.loads(ROUTES_FILE.read_text(encoding="utf-8"))

    candidates = detect_candidates(
        routes,
        min_spacing=args.min_spacing,
        max_spacing=args.max_spacing,
        min_perimeter=args.min_perimeter,
        max_perimeter=args.max_perimeter,
        max_segment_limit=args.max_segment,
        max_compactness=args.max_compactness,
        min_area=args.min_area,
    )

    if not candidates:
        raise RuntimeError("No suitable loops detected with current constraints.")

    selected = select_distinct_loops(candidates, loop_count=args.loops, min_center_gap=args.min_center_gap)

    if not selected:
        raise RuntimeError("No distinct loops selected.")

    patrols = []
    report_loops = []

    for idx, cand in enumerate(selected, start=1):
        name = f"RoadLoop_Preview_Generated_{idx:02d}"
        waypoints = to_waypoints(cand.sampled_points)
        patrols.append(build_patrol(name, waypoints))
        report_loops.append(
            {
                "loop_name": name,
                "source_route_index": cand.route_index,
                "raw_point_count": len(cand.raw_points),
                "simplified_point_count": len(cand.simplified_points),
                "sampled_point_count": len(cand.sampled_points),
                "start_end_distance_raw": round(cand.closed_distance, 2),
                "loop_perimeter_m": round(cand.perimeter, 2),
                "max_segment_m": round(cand.max_segment, 2),
                "center": [round(cand.center[0], 1), round(cand.center[1], 1), round(cand.center[2], 1)],
            }
        )

    settings_preview = {
        "m_Version": 7,
        "Comment": "Generated preview file with multiple LOOP patrols. Copy Patrols entries into active AIPatrolSettings.json after validation.",
        "Patrols": patrols,
    }

    report = {
        "source": str(ROUTES_FILE),
        "constraints": {
            "loops_requested": args.loops,
            "min_spacing": args.min_spacing,
            "max_spacing": args.max_spacing,
            "min_perimeter": args.min_perimeter,
            "max_perimeter": args.max_perimeter,
            "max_segment": args.max_segment,
            "min_center_gap": args.min_center_gap,
            "max_compactness": args.max_compactness,
            "min_area": args.min_area,
        },
        "detected_candidates": len(candidates),
        "selected_loops": len(selected),
        "loops": report_loops,
        "outputs": {
            "settings": str(OUTPUT_SETTINGS),
            "report": str(OUTPUT_REPORT),
            "svg": str(OUTPUT_SVG),
        },
    }

    OUTPUT_SETTINGS.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_SETTINGS.write_text(json.dumps(settings_preview, indent=4), encoding="utf-8")
    OUTPUT_REPORT.write_text(json.dumps(report, indent=4), encoding="utf-8")
    write_svg(selected, OUTPUT_SVG)

    print(f"Generated settings: {OUTPUT_SETTINGS}")
    print(f"Generated report:   {OUTPUT_REPORT}")
    print(f"Generated SVG:      {OUTPUT_SVG}")
    print(f"Selected {len(selected)} loop(s) out of {len(candidates)} candidate(s).")


if __name__ == "__main__":
    main()
