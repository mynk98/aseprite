#!/usr/bin/env python3
"""
Master Pixel Art Background Art for 256x256 Canvas:
"The Cursed Elder Grove: Moonlight over the Haunted Tree"
A true 2D game background asset with deep parallax atmosphere across 8 discrete layers:
1. Sky, Moon & Distant Clouds (Midnight gradient, luminous full moon, drifting lunar mist)
2. Far Background Treeline & Spires (Distant silhouettes of dead pines and gothic ruins)
3. Midground Rolling Fog Bank (Volumetric atmosphere creating deep environmental depth)
4. Ancient Gnarled Tree Trunk & Buttresses (Slender, gnarled ancient trunk with deep bark texture)
5. Dense Sprawling Branch Canopy & Twigs (Intricate gothic silhouette network framing the moon)
6. Weeping Spanish Moss & Lichen (Organic wispy drapes of swamp lichen framing branches)
7. Graveyard Earth, Headstones & Iron Fence (Weathered gothic graves, broken iron fence, mossy rocks)
8. Foreground Fog, Soul Lantern & Embers (Low rolling ground fog, glowing lantern, drifting motes)
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np
import math

def draw_haunted_tree_background():
    w, h = 256, 256

    # 8 Discrete Layers
    l_sky        = Image.new('RGBA', (w, h), (0,0,0,0))
    l_far_bg     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_mid_fog    = Image.new('RGBA', (w, h), (0,0,0,0))
    l_trunk      = Image.new('RGBA', (w, h), (0,0,0,0))
    l_canopy     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_moss       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_ground     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_fore_fog   = Image.new('RGBA', (w, h), (0,0,0,0))

    d_sky        = ImageDraw.Draw(l_sky)
    d_far_bg     = ImageDraw.Draw(l_far_bg)
    d_mid_fog    = ImageDraw.Draw(l_mid_fog)
    d_trunk      = ImageDraw.Draw(l_trunk)
    d_canopy     = ImageDraw.Draw(l_canopy)
    d_moss       = ImageDraw.Draw(l_moss)
    d_ground     = ImageDraw.Draw(l_ground)
    d_fore_fog   = ImageDraw.Draw(l_fore_fog)

    # --- PROFESSIONAL GOTHIC ENVIRONMENT PALETTE ---
    # Midnight Sky Ramp
    SKY_TOP      = (8, 10, 24, 255)
    SKY_MID      = (16, 24, 46, 255)
    SKY_LOW      = (26, 38, 62, 255)

    # Luminous Full Moon
    MOON_SURFACE   = (195, 212, 230, 255)
    MOON_BRIGHT    = (238, 246, 255, 255)
    MOON_SHADOW    = (142, 160, 184, 255)
    MOON_CRATER    = (118, 134, 158, 255)

    # Far Parallax Background
    FAR_BG_DEEP    = (18, 24, 42, 255)

    # Gnarled Tree & Bark (Gothic cold charcoal / weathered ash)
    INK_VOID       = (6, 5, 10, 255)
    BARK_DARK      = (18, 16, 24, 255)
    BARK_MID       = (34, 30, 42, 255)
    BARK_LIGHT     = (56, 50, 68, 255)
    BARK_HIGHLIGHT = (82, 74, 98, 255)

    # Moonlight Rim Light on Branches (Silver-Cyan Edge Glow)
    MOON_RIM       = (108, 132, 162, 255)
    MOON_RIM_BRIGHT= (172, 198, 226, 255)
    MOON_SPEC      = (230, 244, 255, 255)

    # Swamp Moss & Lichen
    MOSS_DARK      = (16, 26, 22, 255)
    MOSS_MID       = (30, 48, 38, 255)
    MOSS_LIGHT     = (52, 78, 60, 255)
    MOSS_PALE      = (94, 130, 106, 255)

    # Graveyard Stones & Iron
    STONE_DARK     = (24, 22, 32, 255)
    STONE_MID      = (48, 44, 58, 255)
    STONE_LIGHT    = (78, 74, 92, 255)
    STONE_BRIGHT   = (120, 114, 138, 255)
    IRON_RUST      = (82, 44, 34, 255)
    IRON_DARK      = (22, 18, 20, 255)

    # Lantern & Embers
    LANTERN_AMBER  = (255, 165, 45, 255)
    LANTERN_GOLD   = (255, 220, 95, 255)
    SOUL_CYAN      = (55, 215, 235, 255)
    SOUL_WHITE     = (230, 255, 252, 255)

    # =========================================================================
    # LAYER 1: SKY, MOON & DISTANT CLOUDS
    # =========================================================================
    for y in range(h):
        ratio = y / h
        if ratio < 0.5:
            t = ratio / 0.5
            r = int(SKY_TOP[0] * (1 - t) + SKY_MID[0] * t)
            g = int(SKY_TOP[1] * (1 - t) + SKY_MID[1] * t)
            b = int(SKY_TOP[2] * (1 - t) + SKY_MID[2] * t)
        else:
            t = (ratio - 0.5) / 0.5
            r = int(SKY_MID[0] * (1 - t) + SKY_LOW[0] * t)
            g = int(SKY_MID[1] * (1 - t) + SKY_LOW[1] * t)
            b = int(SKY_MID[2] * (1 - t) + SKY_LOW[2] * t)
        d_sky.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Grand Luminous Moon (X: 160, Y: 80, Radius: 46)
    moon_x, moon_y, moon_r = 160, 80, 46

    # Lunar halo glow
    for gr in range(moon_r + 40, moon_r, -4):
        alpha = int(22 * (1.0 - (gr - moon_r) / 40))
        d_sky.ellipse([moon_x - gr, moon_y - gr, moon_x + gr, moon_y + gr], fill=(45, 70, 105, alpha))

    # Moon disc
    d_sky.ellipse([moon_x - moon_r, moon_y - moon_r, moon_x + moon_r, moon_y + moon_r], fill=MOON_SURFACE)
    d_sky.ellipse([moon_x - moon_r + 2, moon_y - moon_r + 2, moon_x + moon_r - 2, moon_y + moon_r - 2], fill=MOON_BRIGHT)

    # Detailed Lunar Maria
    craters = [
        (moon_x - 16, moon_y - 14, 18, 12),
        (moon_x + 10, moon_y - 20, 14, 10),
        (moon_x - 20, moon_y + 10, 16, 14),
        (moon_x + 14, moon_y + 12, 20, 14),
        (moon_x - 2, moon_y + 22, 14, 10),
        (moon_x + 2, moon_y - 4, 10, 8),
        (moon_x - 26, moon_y - 2, 8, 8),
        (moon_x + 24, moon_y - 8, 10, 8)
    ]
    for cx, cy, cw, ch in craters:
        d_sky.ellipse([cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2], fill=MOON_CRATER)
        d_sky.ellipse([cx - cw//2 + 1, cy - ch//2 + 1, cx + cw//2 - 1, cy + ch//2 - 1], fill=MOON_SHADOW)

    # Distant drifting gothic cloud bands
    clouds = [
        [(10, 50), (60, 44), (120, 48), (190, 42), (250, 46)],
        [(30, 84), (90, 80), (160, 86), (220, 82), (256, 86)],
        [(0, 116), (50, 110), (130, 118), (190, 112), (256, 120)]
    ]
    for c_pts in clouds:
        for i in range(len(c_pts) - 1):
            p1, p2 = c_pts[i], c_pts[i+1]
            d_sky.line([p1, p2], fill=(20, 30, 50, 130), width=4)
            d_sky.line([(p1[0], p1[1] + 1), (p2[0], p2[1] + 1)], fill=(16, 24, 38, 150), width=2)

    # =========================================================================
    # LAYER 2: FAR BACKGROUND SILHOUETTES (TREELINE & SPIRES)
    # =========================================================================
    bg_ridge = [
        (0, 192), (25, 186), (55, 180), (85, 184), (115, 176), (145, 180),
        (175, 172), (205, 178), (230, 170), (256, 176), (256, 220), (0, 220)
    ]
    d_far_bg.polygon(bg_ridge, fill=FAR_BG_DEEP)

    pines = [10, 24, 42, 60, 80, 185, 205, 225, 245]
    for px in pines:
        py = 180
        h_pine = 18 + (px % 7) * 2
        d_far_bg.line([(px, py), (px, py - h_pine)], fill=FAR_BG_DEEP, width=2)
        for b_off in range(4, h_pine, 3):
            bw = int((h_pine - b_off) * 0.4)
            d_far_bg.line([(px - bw, py - b_off), (px + bw, py - b_off)], fill=FAR_BG_DEEP, width=1)

    d_far_bg.polygon([(34, 180), (34, 158), (37, 146), (40, 158), (40, 180)], fill=FAR_BG_DEEP)
    d_far_bg.line([(37, 146), (37, 140)], fill=FAR_BG_DEEP, width=1)

    # =========================================================================
    # LAYER 3: MIDGROUND ROLLING FOG BANK
    # =========================================================================
    for fy in range(165, 210, 3):
        alpha = int(50 + math.sin(fy * 0.25) * 25)
        d_mid_fog.ellipse([-30, fy, 150, fy + 16], fill=(38, 54, 76, alpha))
        d_mid_fog.ellipse([90, fy - 2, 280, fy + 18], fill=(34, 48, 70, alpha))

    # =========================================================================
    # HELPER: TAPERED GNARLED WOOD LIMB WITH MOON BACKLIGHTING
    # =========================================================================
    def draw_wood_limb(draw, draw_rim, pts, start_r, end_r):
        n_steps = len(pts) - 1
        for i in range(n_steps):
            p1, p2 = pts[i], pts[i+1]
            t1 = i / max(1, n_steps)
            t2 = (i + 1) / max(1, n_steps)
            r1 = start_r * (1.0 - t1) + end_r * t1
            r2 = start_r * (1.0 - t2) + end_r * t2

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dist = max(1e-4, math.hypot(dx, dy))
            nx = -dy / dist
            ny = dx / dist

            poly_out = [
                (p1[0] + nx * (r1 + 1), p1[1] + ny * (r1 + 1)),
                (p2[0] + nx * (r2 + 1), p2[1] + ny * (r2 + 1)),
                (p2[0] - nx * (r2 + 1), p2[1] - ny * (r2 + 1)),
                (p1[0] - nx * (r1 + 1), p1[1] - ny * (r1 + 1))
            ]
            draw.polygon(poly_out, fill=INK_VOID)

            poly_core = [
                (p1[0] + nx * r1, p1[1] + ny * r1),
                (p2[0] + nx * r2, p2[1] + ny * r2),
                (p2[0] - nx * r2, p2[1] - ny * r2),
                (p1[0] - nx * r1, p1[1] - ny * r1)
            ]
            draw.polygon(poly_core, fill=BARK_DARK)

            # Moon direction vector
            mid_x = (p1[0] + p2[0]) * 0.5
            mid_y = (p1[1] + p2[1]) * 0.5
            to_moon_x = moon_x - mid_x
            to_moon_y = moon_y - mid_y
            moon_dist = max(1e-4, math.hypot(to_moon_x, to_moon_y))
            mx_norm = to_moon_x / moon_dist
            my_norm = to_moon_y / moon_dist

            dot = nx * mx_norm + ny * my_norm
            rim_side = 1 if dot > 0 else -1

            if abs(dot) > 0.15:
                draw_rim.line([
                    (p1[0] + nx * r1 * rim_side, p1[1] + ny * r1 * rim_side),
                    (p2[0] + nx * r2 * rim_side, p2[1] + ny * r2 * rim_side)
                ], fill=MOON_RIM, width=max(1, int(r1 * 0.35)))

                if r1 > 2 and abs(dot) > 0.4:
                    draw_rim.line([
                        (p1[0] + nx * r1 * rim_side, p1[1] + ny * r1 * rim_side),
                        (p2[0] + nx * r2 * rim_side, p2[1] + ny * r2 * rim_side)
                    ], fill=MOON_RIM_BRIGHT, width=1)

    # =========================================================================
    # LAYER 5: DENSE BRANCH CANOPY & INTRICATE TWIGS
    # =========================================================================
    # 1. LEFT MAIN BOUGH
    draw_wood_limb(d_canopy, d_canopy, [(105, 115), (85, 105), (66, 100), (48, 108), (32, 122), (18, 136)], 10, 2)
    draw_wood_limb(d_canopy, d_canopy, [(48, 108), (38, 96), (26, 90), (14, 84), (6, 80)], 5, 1)
    draw_wood_limb(d_canopy, d_canopy, [(32, 122), (26, 134), (16, 146), (8, 154)], 4, 1)
    draw_wood_limb(d_canopy, d_canopy, [(26, 90), (24, 76), (16, 64), (8, 56)], 3, 1)

    # 2. MID-LEFT REACHING BOUGH
    draw_wood_limb(d_canopy, d_canopy, [(110, 95), (96, 82), (80, 72), (64, 62), (48, 52), (32, 40), (18, 28)], 8, 1)
    draw_wood_limb(d_canopy, d_canopy, [(80, 72), (74, 58), (62, 44), (50, 34)], 4, 1)
    draw_wood_limb(d_canopy, d_canopy, [(64, 62), (60, 74), (50, 84), (38, 92)], 3, 1)
    draw_wood_limb(d_canopy, d_canopy, [(74, 58), (80, 44), (78, 30), (72, 20)], 3, 1)

    # 3. HIGH-LEFT CROWN ANTLER
    draw_wood_limb(d_canopy, d_canopy, [(118, 80), (112, 62), (102, 48), (92, 34), (80, 22), (70, 12)], 7, 1)
    draw_wood_limb(d_canopy, d_canopy, [(102, 48), (106, 34), (104, 20), (98, 10)], 3, 1)
    draw_wood_limb(d_canopy, d_canopy, [(92, 34), (88, 22), (90, 12)], 2, 1)

    # 4. CENTRAL CROWN FORK
    draw_wood_limb(d_canopy, d_canopy, [(124, 75), (122, 56), (120, 38), (116, 22), (112, 10)], 7, 1)
    draw_wood_limb(d_canopy, d_canopy, [(120, 38), (126, 26), (124, 14)], 3, 1)

    draw_wood_limb(d_canopy, d_canopy, [(134, 75), (136, 56), (142, 38), (148, 22), (152, 10)], 7, 1)
    draw_wood_limb(d_canopy, d_canopy, [(142, 38), (136, 26), (138, 14)], 3, 1)

    # 5. HIGH-RIGHT CROWN FORK
    draw_wood_limb(d_canopy, d_canopy, [(142, 80), (154, 64), (166, 50), (178, 36), (190, 24), (198, 14)], 8, 1)
    draw_wood_limb(d_canopy, d_canopy, [(154, 64), (150, 48), (152, 32), (156, 18)], 4, 1)
    draw_wood_limb(d_canopy, d_canopy, [(166, 50), (172, 36), (170, 22)], 3, 1)

    # 6. MID-RIGHT REACHING BOUGH
    draw_wood_limb(d_canopy, d_canopy, [(148, 95), (166, 86), (184, 78), (202, 68), (220, 56), (234, 44), (246, 32)], 9, 2)
    draw_wood_limb(d_canopy, d_canopy, [(184, 78), (192, 64), (204, 50), (216, 38), (224, 28)], 5, 1)
    draw_wood_limb(d_canopy, d_canopy, [(202, 68), (204, 80), (214, 90), (224, 96)], 4, 1)
    draw_wood_limb(d_canopy, d_canopy, [(192, 64), (188, 48), (190, 32)], 3, 1)

    # 7. RIGHT MAIN BOUGH
    draw_wood_limb(d_canopy, d_canopy, [(145, 115), (165, 105), (185, 102), (204, 106), (222, 114), (238, 124), (250, 134)], 10, 2)
    draw_wood_limb(d_canopy, d_canopy, [(204, 106), (212, 94), (224, 88), (236, 82)], 5, 1)
    draw_wood_limb(d_canopy, d_canopy, [(222, 114), (226, 126), (234, 138), (244, 146)], 4, 1)
    draw_wood_limb(d_canopy, d_canopy, [(185, 102), (188, 116), (192, 128)], 4, 2)

    # 8. LOW-RIGHT DROOPING BOUGH
    draw_wood_limb(d_canopy, d_canopy, [(140, 135), (158, 142), (176, 150), (194, 162), (210, 174), (224, 184)], 7, 2)
    draw_wood_limb(d_canopy, d_canopy, [(176, 150), (184, 138), (196, 132), (206, 128)], 3, 1)
    draw_wood_limb(d_canopy, d_canopy, [(194, 162), (200, 176), (210, 186)], 2, 1)

    # Fine twigs crossing moon face
    moon_twigs = [
        [(134, 68), (140, 60), (146, 54), (152, 48)],
        [(144, 72), (150, 64), (158, 60), (164, 54)],
        [(160, 58), (168, 50), (174, 46)],
        [(148, 40), (154, 32), (160, 28)],
        [(172, 78), (180, 72), (188, 66)],
        [(194, 90), (202, 86), (210, 80)]
    ]
    for tw in moon_twigs:
        for i in range(len(tw) - 1):
            d_canopy.line([tw[i], tw[i+1]], fill=INK_VOID, width=1)
            d_canopy.point([tw[i+1]], fill=MOON_RIM)

    # =========================================================================
    # LAYER 4: ANCIENT GNARLED TRUNK & BUTTRESSES
    # =========================================================================
    trunk_poly = [
        (38, 240), (52, 234), (70, 226), (84, 216), (94, 202), (98, 188),
        (96, 170), (94, 152), (96, 134), (102, 118), (105, 102),
        (112, 88), (120, 76), (128, 82), (136, 76), (144, 88),
        (148, 102), (150, 118), (148, 134), (146, 152), (148, 170),
        (152, 188), (160, 202), (174, 216), (192, 226), (212, 234), (228, 240),
        (216, 242), (190, 236), (168, 228), (148, 230), (136, 238), (126, 244), (116, 238), (104, 230), (84, 236), (56, 242)
    ]
    d_trunk.polygon(trunk_poly, fill=BARK_DARK, outline=INK_VOID, width=2)

    # Left shaded muscular ridges
    d_trunk.polygon([
        (38, 240), (52, 234), (70, 226), (84, 216), (94, 202), (98, 188),
        (96, 170), (94, 152), (96, 134), (102, 118), (105, 102),
        (110, 104), (106, 120), (102, 136), (100, 154), (102, 172),
        (104, 190), (98, 206), (86, 218), (72, 228), (54, 236)
    ], fill=BARK_MID)

    # Right moon-backlit ridges
    d_trunk.polygon([
        (148, 102), (150, 118), (148, 134), (146, 152), (148, 170),
        (152, 188), (160, 202), (174, 216), (192, 226), (212, 234), (228, 240),
        (216, 236), (200, 230), (184, 220), (170, 208), (162, 192),
        (158, 172), (156, 154), (156, 136), (158, 120), (154, 104)
    ], fill=BARK_LIGHT)

    d_trunk.line([
        (148, 102), (150, 118), (148, 134), (146, 152), (148, 170),
        (152, 188), (160, 202), (174, 216), (192, 226), (212, 234), (228, 240)
    ], fill=MOON_RIM_BRIGHT, width=2)

    d_trunk.line([
        (149, 119), (147, 135), (145, 153), (147, 171), (151, 189)
    ], fill=MOON_SPEC, width=1)

    # Vertical wood grain fissures
    for y in range(106, 220, 3):
        gx_l = int(106 + math.sin(y * 0.12) * 5)
        d_trunk.line([(gx_l, y), (gx_l + 3, y + 2)], fill=BARK_MID, width=1)

        gx_c = int(124 + math.sin(y * 0.14 + 1.0) * 4)
        d_trunk.line([(gx_c, y), (gx_c + 2, y + 2)], fill=BARK_LIGHT, width=1)

        gx_r = int(140 + math.sin(y * 0.16 + 2.0) * 4)
        d_trunk.line([(gx_r, y), (gx_r + 2, y + 2)], fill=BARK_HIGHLIGHT, width=1)

    # Weathered Knot Hollow at Y: 138
    d_trunk.ellipse([120, 132, 132, 146], fill=INK_VOID)
    d_trunk.ellipse([122, 134, 130, 144], fill=(12, 10, 16, 255))
    d_trunk.line([(120, 138), (124, 133), (128, 133), (132, 138)], fill=MOON_RIM, width=1)

    # Deep Base Cavity between Roots (Deep atmospheric heartwood void)
    base_hollow = [(116, 186), (126, 182), (134, 186), (138, 202), (134, 218), (124, 224), (116, 218), (112, 202)]
    d_trunk.polygon(base_hollow, fill=INK_VOID)
    d_trunk.line([(116, 186), (126, 182), (134, 186)], fill=BARK_LIGHT, width=1)
    d_trunk.line([(112, 202), (116, 218), (124, 224)], fill=MOON_RIM, width=1)

    # Atmospheric curling mist escaping naturally from base cavity
    mist_curls = [(124, 214, 12), (122, 206, 10), (126, 198, 8), (128, 190, 6)]
    for mx, my, mr in mist_curls:
        d_trunk.ellipse([mx - mr, my - mr//2, mx + mr, my + mr//2], fill=(45, 145, 165, 45))

    # =========================================================================
    # LAYER 6: WEEPING SPANISH MOSS & LICHEN (WISPY GOTHIC CURTAINS)
    # =========================================================================
    def draw_wispy_moss(draw, x, y, length, max_w):
        for dy in range(length):
            w_cur = max(0, int(max_w * (1.0 - dy / length) + math.sin(dy * 0.4 + x) * 1.2))
            cx = x + int(math.sin(dy * 0.2 + x * 0.3) * 2)
            for ox in range(-w_cur, w_cur + 1):
                col = MOSS_DARK if abs(ox) == w_cur else (MOSS_MID if abs(ox) > 0 else MOSS_LIGHT)
                draw.point([(cx + ox, y + dy)], fill=col)
        draw.point([(x + int(math.sin(length * 0.2 + x * 0.3) * 2), y + length)], fill=MOSS_PALE)

    moss_anchors = [
        # Left bough drapes
        (28, 110, 22, 3), (18, 124, 16, 3), (44, 108, 26, 4), (22, 78, 18, 3),
        (48, 70, 20, 3), (72, 64, 16, 3), (88, 48, 16, 3),
        # Center drapes (framed against moon)
        (116, 50, 20, 3), (142, 52, 22, 4), (160, 56, 18, 3),
        # Right bough drapes
        (184, 68, 22, 4), (210, 78, 24, 4), (228, 94, 20, 3), (238, 124, 20, 3),
        (194, 148, 18, 3), (214, 160, 20, 3)
    ]
    for mx, my, mlen, mw in moss_anchors:
        draw_wispy_moss(d_moss, mx, my, mlen, mw)

    # Patchy moss & lichen on tree trunk buttresses (not a diagonal stripe)
    buttress_moss = [
        (88, 196), (92, 192), (90, 188), (96, 184),
        (82, 212), (86, 208), (78, 220), (74, 224),
        (162, 196), (166, 192), (170, 204), (178, 212)
    ]
    for bx, by in buttress_moss:
        d_moss.ellipse([bx - 2, by - 2, bx + 2, by + 2], fill=MOSS_DARK)
        d_moss.point([(bx, by)], fill=MOSS_MID)
        d_moss.point([(bx, by - 1)], fill=MOSS_LIGHT)

    # =========================================================================
    # LAYER 7: GRAVEYARD EARTH, HEADSTONES & IRON FENCE
    # =========================================================================
    ground_poly = [
        (0, 256), (0, 240), (20, 234), (54, 228), (92, 224), (126, 223),
        (160, 224), (198, 228), (234, 234), (256, 240), (256, 256)
    ]
    d_ground.polygon(ground_poly, fill=BARK_DARK)
    d_ground.polygon([(x, y - 1) for x, y in ground_poly[1:-1]], fill=STONE_DARK)

    # Ancient Gothic Headstones with crisp high-contrast stone relief
    # Tombstone 1: Left Celtic Cross headstone (X: 24 to 38, Y: 210 to 238)
    d_ground.rounded_rectangle([24, 210, 38, 236], radius=3, fill=STONE_MID, outline=INK_VOID, width=1)
    d_ground.line([(31, 214), (31, 230)], fill=STONE_LIGHT, width=1)
    d_ground.line([(27, 218), (35, 218)], fill=STONE_LIGHT, width=1)
    d_ground.line([(25, 211), (37, 211)], fill=MOON_RIM_BRIGHT, width=1)
    d_ground.line([(33, 222), (31, 226), (34, 230)], fill=INK_VOID, width=1) # Crack

    # Tombstone 2: Tilted sunken headstone near left root (X: 68 to 80, Y: 220 to 240)
    d_ground.polygon([(68, 224), (78, 221), (82, 241), (71, 243)], fill=STONE_MID, outline=INK_VOID, width=1)
    d_ground.line([(69, 225), (77, 222)], fill=MOON_RIM_BRIGHT, width=1)
    d_ground.line([(73, 227), (74, 236)], fill=STONE_LIGHT, width=1)

    # Tombstone 3: Right ornate arched crypt marker (X: 216 to 232, Y: 212 to 240)
    d_ground.rounded_rectangle([216, 212, 232, 238], radius=4, fill=STONE_MID, outline=INK_VOID, width=1)
    d_ground.ellipse([220, 216, 228, 224], fill=STONE_DARK)
    d_ground.line([(217, 213), (231, 213)], fill=MOON_RIM_BRIGHT, width=1)
    d_ground.line([(224, 226), (224, 235)], fill=STONE_LIGHT, width=1)

    # Wrought iron graveyard fence with ornate spear tops
    for fx in [6, 12, 18, 238, 244, 250]:
        d_ground.line([(fx, 238), (fx, 216)], fill=IRON_DARK, width=1)
        d_ground.polygon([(fx - 1, 216), (fx, 212), (fx + 1, 216)], fill=IRON_RUST)
        d_ground.point([(fx, 213)], fill=MOON_RIM)
    d_ground.line([(4, 224), (20, 224)], fill=IRON_DARK, width=1)
    d_ground.line([(236, 224), (252, 224)], fill=IRON_DARK, width=1)

    # Mossy rocks & roots gripping stone
    d_ground.ellipse([88, 232, 104, 242], fill=STONE_MID, outline=INK_VOID)
    d_ground.line([(90, 233), (100, 233)], fill=MOON_RIM)
    d_ground.line([(86, 235), (94, 234), (104, 237)], fill=BARK_DARK, width=2)
    d_ground.line([(86, 235), (94, 234), (104, 237)], fill=BARK_LIGHT, width=1)

    # Glowing toxic swamp fungi
    shrooms = [(44, 230, 4), (50, 232, 3), (192, 230, 4), (200, 229, 3), (208, 231, 4)]
    for sx, sy, sr in shrooms:
        d_ground.line([(sx, sy), (sx, sy - sr*2)], fill=STONE_LIGHT, width=1)
        d_ground.ellipse([sx - sr, sy - sr*2 - 1, sx + sr, sy - sr*2 + 2], fill=(125, 40, 160, 255), outline=INK_VOID)
        d_ground.point([(sx, sy - sr*2)], fill=(215, 105, 255, 255))

    # =========================================================================
    # LAYER 8: FOREGROUND GROUND MIST, LANTERN & NIGHT PARTICLES
    # =========================================================================
    # 1. Rusted Iron Hanging Lantern on right bough (X: 192, Y: 116 to 150)
    for cy in range(116, 126, 2):
        d_fore_fog.line([(192, cy), (192, cy + 1)], fill=IRON_RUST, width=1)
        d_fore_fog.point([(193, cy)], fill=MOON_RIM)

    # Lantern roof cap
    d_fore_fog.polygon([(184, 126), (192, 121), (200, 126)], fill=IRON_DARK, outline=INK_VOID)
    d_fore_fog.line([(185, 126), (192, 122)], fill=MOON_RIM_BRIGHT, width=1)

    # Lantern iron cage
    d_fore_fog.rectangle([184, 126, 200, 142], outline=IRON_DARK, width=1)
    d_fore_fog.line([(188, 126), (188, 142)], fill=IRON_DARK, width=1)
    d_fore_fog.line([(196, 126), (196, 142)], fill=IRON_DARK, width=1)

    # Warm amber glowing flame
    d_fore_fog.rectangle([185, 127, 199, 141], fill=(55, 35, 18, 200))
    d_fore_fog.ellipse([174, 118, 210, 150], fill=(255, 165, 45, 35))
    d_fore_fog.ellipse([180, 124, 204, 144], fill=(255, 185, 60, 75))
    d_fore_fog.ellipse([187, 129, 197, 139], fill=LANTERN_AMBER)
    d_fore_fog.ellipse([189, 131, 195, 137], fill=LANTERN_GOLD)
    d_fore_fog.point([(192, 134)], fill=(255, 255, 240, 255))

    # Bottom spike
    d_fore_fog.polygon([(187, 142), (192, 147), (197, 142)], fill=IRON_DARK, outline=INK_VOID)

    # 2. Sinister Black Raven perched on high-left branch overlooking graveyard (X: 48, Y: 66)
    raven_body = [(42, 68), (50, 70), (58, 66), (62, 58), (58, 50), (50, 48), (44, 52), (38, 60)]
    d_fore_fog.polygon(raven_body, fill=INK_VOID, outline=INK_VOID)
    d_fore_fog.polygon([(44, 66), (50, 68), (56, 64), (56, 58), (50, 52), (44, 54)], fill=BARK_DARK)
    d_fore_fog.line([(44, 58), (50, 64), (54, 66)], fill=MOON_RIM_BRIGHT, width=1)
    # Tail feathers
    d_fore_fog.polygon([(38, 60), (44, 64), (34, 74), (32, 72)], fill=INK_VOID)
    # Head & beak
    d_fore_fog.ellipse([54, 44, 62, 52], fill=INK_VOID)
    d_fore_fog.polygon([(61, 47), (68, 49), (61, 51)], fill=IRON_DARK)
    d_fore_fog.point([(58, 47)], fill=(255, 80, 40, 255))
    # Claws
    d_fore_fog.line([(47, 68), (47, 71)], fill=IRON_RUST, width=1)
    d_fore_fog.line([(52, 67), (52, 70)], fill=IRON_RUST, width=1)

    # 3. Dense Rolling Ground Fog across foreground (Y: 226 to 256)
    for gy in range(226, 256, 3):
        alpha = int(40 + (gy - 226) * 3.5)
        d_fore_fog.ellipse([-30, gy, 150, gy + 10], fill=(45, 65, 90, alpha))
        d_fore_fog.ellipse([105, gy - 2, 285, gy + 12], fill=(40, 60, 85, alpha))

    # 4. Floating Will-o'-the-Wisp Soul Particles
    wisps = [
        (36, 122, 4),   # Left graves
        (74, 94, 5),    # Left canopy
        (130, 146, 4),  # Above hollow
        (164, 132, 4),  # Near lantern
        (224, 98, 5),   # Right canopy
        (84, 214, 4),   # Ground mist
        (170, 212, 4)   # Ground mist
    ]
    for wx, wy, wr in wisps:
        d_fore_fog.ellipse([wx - wr*2, wy - wr*2, wx + wr*2, wy + wr*2], fill=(45, 175, 200, 28))
        d_fore_fog.ellipse([wx - int(wr*1.2), wy - int(wr*1.2), wx + int(wr*1.2), wy + int(wr*1.2)], fill=(55, 195, 220, 70))
        d_fore_fog.ellipse([wx - int(wr*0.6), wy - int(wr*0.6), wx + int(wr*0.6), wy + int(wr*0.6)], fill=SOUL_CYAN)
        d_fore_fog.point([(wx, wy)], fill=SOUL_WHITE)

    # Ambient moonlit night spores
    spores = [
        (26, 44), (62, 26), (90, 16), (140, 32), (166, 22), (216, 16),
        (240, 58), (12, 176), (238, 192), (100, 166)
    ]
    for sx, sy in spores:
        d_fore_fog.point([(sx, sy)], fill=MOON_RIM_BRIGHT)
        d_fore_fog.point([(sx, sy - 1)], fill=MOON_SPEC)

    layers = [
        ("Sky & Luminous Moon", l_sky),
        ("Far Background Treeline", l_far_bg),
        ("Midground Fog Bank", l_mid_fog),
        ("Gnarled Tree Trunk", l_trunk),
        ("Branch Canopy & Twigs", l_canopy),
        ("Spanish Moss & Lichen", l_moss),
        ("Graveyard Earth & Stones", l_ground),
        ("Foreground Fog & Lantern", l_fore_fog)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_haunted_tree_background()
    out_path = Path("/tmp/haunted_tree_bg_256.png")
    composite.save(out_path)
    print(f"Haunted Tree Background Art rendered successfully to {out_path}")
