#!/usr/bin/env python3
"""
Master Human-Quality Pixel Art Background:
"The Cursed Elder Grove - Moonlight over the Gnarled Tree"
Engineered with seamless, organic branching (ZERO stuck-on lines, ZERO disjointed seams).
Built as a unified, monolithic wood anatomy with authentic human pixel art techniques:
- Continuous single-silhouette tree structure with smooth branching crotches
- Exterior-only dark inking (no internal seam cuts)
- Directional lunar backlight with soft edge bleed
- Natural tree growth hierarchy (Trunk -> 2 Major Boughs -> Secondary Limbs -> Delicate Twigs)
- Soft ragged Spanish moss curtains
- Weathered gothic graveyard & warm focal soul lantern
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import math

def draw_haunted_tree_background():
    w, h = 256, 256

    # 8 Discrete Game Background Layers
    l_sky        = Image.new('RGBA', (w, h), (0,0,0,0))
    l_far_bg     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_mid_fog    = Image.new('RGBA', (w, h), (0,0,0,0))
    l_tree_base  = Image.new('RGBA', (w, h), (0,0,0,0)) # Unified trunk & branch wood
    l_tree_shade = Image.new('RGBA', (w, h), (0,0,0,0)) # Bark grain, crotch AO & moon rim
    l_moss       = Image.new('RGBA', (w, h), (0,0,0,0)) # Organic weeping Spanish moss
    l_graveyard  = Image.new('RGBA', (w, h), (0,0,0,0)) # Ground, rocks, headstones, fence
    l_foreground = Image.new('RGBA', (w, h), (0,0,0,0)) # Rolling ground fog, lantern, raven

    d_sky        = ImageDraw.Draw(l_sky)
    d_far_bg     = ImageDraw.Draw(l_far_bg)
    d_mid_fog    = ImageDraw.Draw(l_mid_fog)
    d_moss       = ImageDraw.Draw(l_moss)
    d_graveyard  = ImageDraw.Draw(l_graveyard)
    d_foreground = ImageDraw.Draw(l_foreground)

    # --- PROFESSIONAL GOTHIC ENVIRONMENT PALETTE ---
    # Midnight Sky
    SKY_TOP      = (8, 10, 24, 255)
    SKY_MID      = (16, 24, 46, 255)
    SKY_LOW      = (26, 38, 62, 255)

    # Luminous Full Moon
    MOON_SURFACE   = (192, 210, 228, 255)
    MOON_BRIGHT    = (238, 246, 255, 255)
    MOON_SHADOW    = (140, 158, 182, 255)
    MOON_CRATER    = (116, 132, 156, 255)

    # Far Parallax Background
    FAR_BG_DEEP    = (18, 24, 42, 255)

    # Gnarled Tree & Bark
    INK_VOID       = (6, 5, 10, 255)
    BARK_DEEP      = (14, 12, 18, 255)
    BARK_DARK      = (22, 18, 28, 255)
    BARK_MID       = (36, 30, 44, 255)
    BARK_LIGHT     = (58, 50, 70, 255)
    BARK_HIGHLIGHT = (84, 76, 100, 255)

    # Moonlight Rim Backlight
    MOON_RIM_DARK  = (70, 92, 120, 255)
    MOON_RIM_MID   = (118, 146, 178, 255)
    MOON_RIM_LIGHT = (176, 204, 232, 255)
    MOON_SPEC      = (234, 246, 255, 255)

    # Swamp Spanish Moss (Wispy Lichen)
    MOSS_SHADOW    = (14, 22, 18, 255)
    MOSS_DARK      = (24, 38, 30, 255)
    MOSS_MID       = (42, 64, 50, 255)
    MOSS_LIGHT     = (68, 98, 78, 255)
    MOSS_PALE      = (108, 144, 120, 255)

    # Graveyard Stones & Iron
    STONE_DARK     = (22, 20, 28, 255)
    STONE_MID      = (42, 38, 52, 255)
    STONE_LIGHT    = (70, 66, 82, 255)
    STONE_RIM      = (112, 128, 152, 255)
    IRON_DARK      = (20, 16, 18, 255)
    IRON_RUST      = (80, 42, 32, 255)

    # Lantern & Fireflies
    LANTERN_AMBER  = (255, 160, 40, 255)
    LANTERN_GOLD   = (255, 215, 90, 255)
    SOUL_CYAN      = (55, 215, 235, 255)
    SOUL_WHITE     = (230, 255, 252, 255)

    # =========================================================================
    # LAYER 1: SKY, MOON & CLOUDS
    # =========================================================================
    for y in range(h):
        ratio = y / h
        if ratio < 0.55:
            t = ratio / 0.55
            r = int(SKY_TOP[0] * (1 - t) + SKY_MID[0] * t)
            g = int(SKY_TOP[1] * (1 - t) + SKY_MID[1] * t)
            b = int(SKY_TOP[2] * (1 - t) + SKY_MID[2] * t)
        else:
            t = (ratio - 0.55) / 0.45
            r = int(SKY_MID[0] * (1 - t) + SKY_LOW[0] * t)
            g = int(SKY_MID[1] * (1 - t) + SKY_LOW[1] * t)
            b = int(SKY_MID[2] * (1 - t) + SKY_LOW[2] * t)
        d_sky.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Large Silver Full Moon (X: 155, Y: 82, Radius: 48)
    moon_x, moon_y, moon_r = 155, 82, 48

    for gr in range(moon_r + 36, moon_r, -3):
        alpha = int(24 * (1.0 - (gr - moon_r) / 36))
        d_sky.ellipse([moon_x - gr, moon_y - gr, moon_x + gr, moon_y + gr], fill=(45, 72, 108, alpha))

    d_sky.ellipse([moon_x - moon_r, moon_y - moon_r, moon_x + moon_r, moon_y + moon_r], fill=MOON_SURFACE)
    d_sky.ellipse([moon_x - moon_r + 2, moon_y - moon_r + 2, moon_x + moon_r - 2, moon_y + moon_r - 2], fill=MOON_BRIGHT)

    # Lunar Maria Craters
    craters = [
        (moon_x - 16, moon_y - 16, 20, 14),
        (moon_x + 12, moon_y - 22, 16, 12),
        (moon_x - 22, moon_y + 10, 18, 14),
        (moon_x + 16, moon_y + 14, 22, 16),
        (moon_x - 2, moon_y + 24, 16, 10),
        (moon_x + 4, moon_y - 4, 12, 10),
        (moon_x - 28, moon_y - 2, 10, 8),
        (moon_x + 26, moon_y - 8, 12, 8)
    ]
    for cx, cy, cw, ch in craters:
        d_sky.ellipse([cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2], fill=MOON_CRATER)
        d_sky.ellipse([cx - cw//2 + 1, cy - ch//2 + 1, cx + cw//2 - 1, cy + ch//2 - 1], fill=MOON_SHADOW)

    clouds = [
        [(10, 48), (60, 42), (120, 46), (190, 40), (250, 44)],
        [(30, 82), (90, 78), (160, 84), (220, 80), (256, 84)],
        [(0, 118), (50, 112), (130, 120), (190, 114), (256, 122)]
    ]
    for c_pts in clouds:
        for i in range(len(c_pts) - 1):
            p1, p2 = c_pts[i], c_pts[i+1]
            d_sky.line([p1, p2], fill=(20, 30, 50, 125), width=4)
            d_sky.line([(p1[0], p1[1] + 1), (p2[0], p2[1] + 1)], fill=(16, 24, 38, 145), width=2)

    # =========================================================================
    # LAYER 2: FAR BACKGROUND (DISTANT PINES & CATHEDRAL RUINS)
    # =========================================================================
    bg_ridge = [
        (0, 192), (25, 186), (55, 180), (85, 184), (115, 176), (145, 180),
        (175, 172), (205, 178), (230, 170), (256, 176), (256, 225), (0, 225)
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
    for fy in range(165, 212, 3):
        alpha = int(45 + math.sin(fy * 0.25) * 25)
        d_mid_fog.ellipse([-30, fy, 150, fy + 16], fill=(36, 52, 74, alpha))
        d_mid_fog.ellipse([90, fy - 2, 285, fy + 18], fill=(32, 46, 68, alpha))

    # =========================================================================
    # LAYERS 4 & 5: UNIFIED MONOLITHIC TREE (ZERO STUCK-ON SEAMS!)
    # =========================================================================
    tree_canvas = Image.new('1', (w, h), 0)
    d_tc = ImageDraw.Draw(tree_canvas)

    def draw_smooth_branch(pts, radii):
        for i in range(len(pts) - 1):
            p1, p2 = pts[i], pts[i+1]
            r1, r2 = radii[i], radii[i+1]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dist = max(1e-4, math.hypot(dx, dy))
            steps = max(2, int(dist * 2))

            for s in range(steps + 1):
                t = s / steps
                cx = p1[0] + dx * t
                cy = p1[1] + dy * t
                cr = r1 * (1.0 - t) + r2 * t
                d_tc.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=1)

    # 1. ROOT BUTTRESSES & MAIN TRUNK FOUNDATION
    buttresses = [
        ([(120, 205), (105, 215), (85, 226), (60, 235), (38, 242), (24, 246)], [16, 14, 11, 8, 5, 2]),
        ([(122, 210), (110, 222), (95, 234), (78, 242), (66, 246)], [14, 11, 8, 5, 2]),
        ([(128, 215), (126, 228), (122, 240), (120, 248)], [15, 12, 8, 4]),
        ([(136, 210), (148, 222), (164, 234), (180, 242), (192, 246)], [14, 11, 8, 5, 2]),
        ([(138, 205), (155, 215), (178, 226), (204, 235), (226, 242), (242, 246)], [16, 14, 11, 8, 5, 2]),
        ([(128, 215), (127, 195), (125, 175), (124, 155), (126, 135), (128, 118)], [20, 19, 18, 18, 19, 21])
    ]
    for pts, rads in buttresses:
        draw_smooth_branch(pts, rads)

    # 2. TWO GIANT PRIMARY BOUGHS
    primary_boughs = [
        ([(126, 118), (112, 108), (96, 102), (80, 102), (65, 108), (52, 118), (38, 130), (26, 142), (16, 150)],
         [18, 15, 13, 11, 9, 7, 5, 4, 2]),

        ([(130, 118), (145, 108), (162, 100), (180, 98), (198, 102), (216, 112), (230, 124), (242, 136)],
         [18, 15, 13, 11, 9, 7, 5, 3]),

        ([(128, 118), (128, 100), (129, 84), (130, 68), (132, 52), (134, 38), (136, 24), (138, 12)],
         [15, 12, 10, 8, 6, 5, 3, 2])
    ]
    for pts, rads in primary_boughs:
        draw_smooth_branch(pts, rads)

    # 3. SECONDARY LIMBS
    secondary_limbs = [
        ([(96, 102), (88, 88), (78, 74), (66, 62), (52, 52), (38, 42), (24, 32), (14, 24)],
         [10, 8, 7, 6, 5, 4, 3, 1]),

        ([(65, 108), (56, 96), (44, 88), (32, 82), (20, 80), (10, 78)],
         [7, 6, 5, 4, 3, 1]),

        ([(38, 130), (32, 120), (22, 112), (12, 106)],
         [4, 3, 2, 1]),

        ([(129, 84), (122, 70), (116, 54), (110, 38), (106, 24), (102, 12)],
         [7, 6, 5, 4, 3, 1]),

        ([(130, 68), (138, 56), (144, 42), (150, 28), (154, 16)],
         [6, 5, 4, 3, 1]),

        ([(162, 100), (168, 84), (176, 68), (186, 52), (198, 38), (210, 26), (220, 16)],
         [10, 8, 7, 6, 5, 4, 2, 1]),

        ([(180, 98), (192, 86), (206, 76), (220, 68), (234, 58), (246, 48)],
         [9, 7, 6, 5, 4, 2]),

        ([(180, 98), (184, 110), (188, 122), (190, 130)],
         [7, 5, 4, 3]),

        ([(216, 112), (222, 124), (228, 138), (234, 150)],
         [6, 4, 3, 1])
    ]
    for pts, rads in secondary_limbs:
        draw_smooth_branch(pts, rads)

    # 4. TERTIARY SPINDLY TWIGS
    twigs = [
        ([(78, 74), (72, 60), (64, 48), (56, 38)], [4, 3, 2, 1]),
        ([(52, 52), (48, 64), (40, 72)], [3, 2, 1]),
        ([(66, 62), (72, 48), (70, 34)], [3, 2, 1]),
        ([(116, 54), (122, 42), (120, 28)], [3, 2, 1]),
        ([(144, 42), (138, 30), (140, 18)], [3, 2, 1]),
        ([(176, 68), (172, 54), (174, 38)], [4, 3, 2]),
        ([(186, 52), (194, 40), (192, 26)], [3, 2, 1]),
        ([(206, 76), (212, 62), (218, 50)], [4, 3, 2]),
        ([(220, 68), (224, 80), (232, 90)], [3, 2, 1])
    ]
    for pts, rads in twigs:
        draw_smooth_branch(pts, rads)

    tree_mask = np.array(tree_canvas)

    # Natural Heartwood Hollows
    hollow_knot = Image.new('1', (w, h), 0)
    d_hk = ImageDraw.Draw(hollow_knot)
    d_hk.ellipse([121, 130, 131, 142], fill=1)
    knot_mask = np.array(hollow_knot)

    base_cavity = Image.new('1', (w, h), 0)
    d_bc = ImageDraw.Draw(base_cavity)
    d_bc.polygon([(118, 192), (128, 186), (138, 192), (142, 208), (136, 224), (128, 228), (120, 224), (114, 208)], fill=1)
    base_mask = np.array(base_cavity)

    # Exterior-only outline
    dilated_img = tree_canvas.filter(ImageFilter.MaxFilter(3))
    dilated_mask = np.array(dilated_img)
    edge_mask = dilated_mask & ~tree_mask

    eroded1_img = tree_canvas.filter(ImageFilter.MinFilter(3))
    eroded1_mask = np.array(eroded1_img)
    eroded2_img = eroded1_img.filter(ImageFilter.MinFilter(3))
    eroded2_mask = np.array(eroded2_img)

    tree_base_arr = np.zeros((h, w, 4), dtype=np.uint8)
    tree_shade_arr = np.zeros((h, w, 4), dtype=np.uint8)

    # Fill continuous exterior outline
    tree_base_arr[edge_mask] = INK_VOID

    # Fill base wood core
    tree_base_arr[tree_mask] = BARK_DARK

    # Ambient Occlusion in deep wood core
    tree_shade_arr[eroded2_mask] = BARK_MID

    # Continuous vertical wood grain
    for y in range(115, 230):
        gx1 = int(116 + math.sin(y * 0.12) * 4)
        if 0 <= gx1 < w and tree_mask[y, gx1]:
            tree_shade_arr[y, gx1:gx1+2] = BARK_LIGHT

        gx2 = int(136 + math.sin(y * 0.15 + 1.2) * 4)
        if 0 <= gx2 < w and tree_mask[y, gx2]:
            tree_shade_arr[y, gx2:gx2+2] = BARK_HIGHLIGHT

    # Hollow cutouts
    tree_base_arr[knot_mask] = [0, 0, 0, 0]
    tree_shade_arr[knot_mask] = [0, 0, 0, 0]
    tree_base_arr[base_mask] = [0, 0, 0, 0]
    tree_shade_arr[base_mask] = [0, 0, 0, 0]

    d_tb = ImageDraw.Draw(l_tree_base)
    d_tb.ellipse([121, 130, 131, 142], fill=INK_VOID)
    d_tb.polygon([(118, 192), (128, 186), (138, 192), (142, 208), (136, 224), (128, 228), (120, 224), (114, 208)], fill=INK_VOID)

    # Soft diffuse blue mist inside base cavity
    for my in range(196, 226):
        alpha = int(25 + (my - 196) * 1.8)
        d_tb.ellipse([120, my, 136, my + 4], fill=(45, 145, 165, alpha))

    # Moon Back-Rim Lighting on outer branch boundary
    rim_zone = tree_mask & ~eroded1_mask
    y_rim, x_rim = np.where(rim_zone)
    for py, px in zip(y_rim, x_rim):
        dx = moon_x - px
        dy = moon_y - py
        dist = math.hypot(dx, dy)
        if dist < 125:
            n_out_x = 0
            n_out_y = 0
            for oy in [-1, 0, 1]:
                for ox in [-1, 0, 1]:
                    if not tree_mask[min(h-1, max(0, py+oy)), min(w-1, max(0, px+ox))]:
                        n_out_x += ox
                        n_out_y += oy
            norm_len = math.hypot(n_out_x, n_out_y)
            if norm_len > 0:
                dot = (n_out_x * dx + n_out_y * dy) / (norm_len * dist)
                if dot > 0.15:
                    tree_shade_arr[py, px] = MOON_SPEC if dot > 0.65 else MOON_RIM_LIGHT
                elif dot > 0.0:
                    tree_shade_arr[py, px] = MOON_RIM_MID

    l_tree_base.paste(Image.fromarray(tree_base_arr, 'RGBA'), (0, 0), Image.fromarray(tree_base_arr[:,:,3], 'L'))
    l_tree_shade.paste(Image.fromarray(tree_shade_arr, 'RGBA'), (0, 0), Image.fromarray(tree_shade_arr[:,:,3], 'L'))

    # =========================================================================
    # LAYER 6: WEEPING SPANISH MOSS & LICHEN (SOFT WISPS DRAPING FROM BOUGHS)
    # =========================================================================
    def draw_ragged_moss(draw, x, y, length, max_w):
        for dy in range(length):
            w_cur = max(0, int(max_w * (1.0 - dy / length) + math.sin(dy * 0.4 + x) * 1.2))
            cx = x + int(math.sin(dy * 0.2 + x * 0.3) * 2)
            for ox in range(-w_cur, w_cur + 1):
                col = MOSS_DARK if abs(ox) == w_cur else (MOSS_MID if abs(ox) > 0 else MOSS_LIGHT)
                draw.point([(cx + ox, y + dy)], fill=col)
        draw.point([(x + int(math.sin(length * 0.2 + x * 0.3) * 2), y + length)], fill=MOSS_PALE)

    moss_anchors = [
        (26, 112, 22, 3), (16, 126, 16, 3), (42, 110, 26, 4), (20, 80, 18, 3),
        (46, 72, 20, 3), (70, 66, 16, 3), (86, 50, 16, 3),
        (114, 52, 20, 3), (140, 54, 22, 4), (158, 58, 18, 3),
        (182, 70, 22, 4), (208, 80, 24, 4), (226, 96, 20, 3), (236, 126, 20, 3),
        (192, 150, 18, 3), (212, 162, 20, 3)
    ]
    for mx, my, mlen, mw in moss_anchors:
        draw_ragged_moss(d_moss, mx, my, mlen, mw)

    buttress_moss = [
        (86, 200), (90, 194), (88, 190), (94, 186),
        (80, 214), (84, 210), (76, 222), (72, 226),
        (160, 200), (164, 194), (168, 206), (176, 214)
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
    d_graveyard.polygon(ground_poly, fill=BARK_DARK)
    d_graveyard.polygon([(x, y - 1) for x, y in ground_poly[1:-1]], fill=STONE_DARK)

    # Tombstone 1: Celtic Cross
    d_graveyard.rounded_rectangle([24, 210, 38, 236], radius=3, fill=STONE_MID, outline=INK_VOID, width=1)
    d_graveyard.line([(31, 214), (31, 230)], fill=STONE_LIGHT, width=1)
    d_graveyard.line([(27, 218), (35, 218)], fill=STONE_LIGHT, width=1)
    d_graveyard.line([(25, 211), (37, 211)], fill=STONE_RIM, width=1)
    d_graveyard.line([(33, 222), (31, 226), (34, 230)], fill=INK_VOID, width=1)

    # Tombstone 2: Sunken tilted headstone
    d_graveyard.polygon([(68, 224), (78, 221), (82, 241), (71, 243)], fill=STONE_MID, outline=INK_VOID, width=1)
    d_graveyard.line([(69, 225), (77, 222)], fill=STONE_RIM, width=1)
    d_graveyard.line([(73, 227), (74, 236)], fill=STONE_LIGHT, width=1)

    # Tombstone 3: Ornate crypt headstone
    d_graveyard.rounded_rectangle([216, 212, 232, 238], radius=4, fill=STONE_MID, outline=INK_VOID, width=1)
    d_graveyard.ellipse([220, 216, 228, 224], fill=STONE_DARK)
    d_graveyard.line([(217, 213), (231, 213)], fill=STONE_RIM, width=1)
    d_graveyard.line([(224, 226), (224, 235)], fill=STONE_LIGHT, width=1)

    # Wrought iron fence
    for fx in [6, 12, 18, 238, 244, 250]:
        d_graveyard.line([(fx, 238), (fx, 216)], fill=IRON_DARK, width=1)
        d_graveyard.polygon([(fx - 1, 216), (fx, 212), (fx + 1, 216)], fill=IRON_RUST)
        d_graveyard.point([(fx, 213)], fill=MOON_RIM_DARK)
    d_graveyard.line([(4, 224), (20, 224)], fill=IRON_DARK, width=1)
    d_graveyard.line([(236, 224), (252, 224)], fill=IRON_DARK, width=1)

    # Mossy rock
    d_graveyard.ellipse([88, 232, 104, 242], fill=STONE_MID, outline=INK_VOID)
    d_graveyard.line([(90, 233), (100, 233)], fill=STONE_RIM)
    d_graveyard.line([(86, 235), (94, 234), (104, 237)], fill=BARK_DARK, width=2)
    d_graveyard.line([(86, 235), (94, 234), (104, 237)], fill=BARK_LIGHT, width=1)

    # Toxic swamp mushrooms
    shrooms = [(44, 230, 4), (50, 232, 3), (192, 230, 4), (200, 229, 3), (208, 231, 4)]
    for sx, sy, sr in shrooms:
        d_graveyard.line([(sx, sy), (sx, sy - sr*2)], fill=STONE_LIGHT, width=1)
        d_graveyard.ellipse([sx - sr, sy - sr*2 - 1, sx + sr, sy - sr*2 + 2], fill=(125, 40, 160, 255), outline=INK_VOID)
        d_graveyard.point([(sx, sy - sr*2)], fill=(215, 105, 255, 255))

    # =========================================================================
    # LAYER 8: FOREGROUND GROUND FOG, LANTERN & PERCHED RAVEN
    # =========================================================================
    # 1. Rusted Iron Hanging Lantern
    for cy in range(130, 138, 2):
        d_foreground.line([(190, cy), (190, cy + 1)], fill=IRON_RUST, width=1)
        d_foreground.point([(191, cy)], fill=MOON_RIM_LIGHT)

    d_foreground.polygon([(182, 138), (190, 133), (198, 138)], fill=IRON_DARK, outline=INK_VOID)
    d_foreground.line([(183, 138), (190, 134)], fill=MOON_RIM_LIGHT, width=1)

    d_foreground.rectangle([182, 138, 198, 152], outline=IRON_DARK, width=1)
    d_foreground.line([(186, 138), (186, 152)], fill=IRON_DARK, width=1)
    d_foreground.line([(194, 138), (194, 152)], fill=IRON_DARK, width=1)

    d_foreground.rectangle([183, 139, 197, 151], fill=(55, 35, 18, 200))
    d_foreground.ellipse([172, 130, 208, 160], fill=(255, 160, 40, 32))
    d_foreground.ellipse([178, 134, 202, 154], fill=(255, 185, 60, 75))
    d_foreground.ellipse([185, 140, 195, 150], fill=LANTERN_AMBER)
    d_foreground.ellipse([187, 142, 193, 148], fill=LANTERN_GOLD)
    d_foreground.point([(190, 145)], fill=(255, 255, 240, 255))
    d_foreground.polygon([(185, 152), (190, 157), (195, 152)], fill=IRON_DARK, outline=INK_VOID)

    # 2. Sinister Black Raven perched on high-left branch
    raven_body = [(40, 74), (48, 76), (56, 72), (60, 64), (56, 56), (48, 54), (42, 58), (36, 66)]
    d_foreground.polygon(raven_body, fill=INK_VOID, outline=INK_VOID)
    d_foreground.polygon([(42, 72), (48, 74), (54, 70), (54, 64), (48, 58), (42, 60)], fill=BARK_DARK)
    d_foreground.line([(42, 64), (48, 70), (52, 72)], fill=MOON_RIM_MID, width=1)
    d_foreground.polygon([(36, 66), (42, 70), (32, 80), (30, 78)], fill=INK_VOID)
    d_foreground.ellipse([52, 50, 60, 58], fill=INK_VOID)
    d_foreground.polygon([(59, 53), (66, 55), (59, 57)], fill=IRON_DARK)
    d_foreground.point([(56, 53)], fill=(255, 80, 40, 255))
    d_foreground.line([(45, 74), (45, 77)], fill=IRON_RUST, width=1)
    d_foreground.line([(50, 73), (50, 76)], fill=IRON_RUST, width=1)

    # 3. Dense Rolling Ground Fog
    for gy in range(226, 256, 3):
        alpha = int(40 + (gy - 226) * 3.5)
        d_foreground.ellipse([-30, gy, 150, gy + 10], fill=(45, 65, 90, alpha))
        d_foreground.ellipse([105, gy - 2, 285, gy + 12], fill=(40, 60, 85, alpha))

    # 4. Floating Soul Particles
    wisps = [
        (36, 122, 4), (74, 94, 5), (130, 146, 4), (164, 132, 4),
        (224, 98, 5), (84, 214, 4), (170, 212, 4)
    ]
    for wx, wy, wr in wisps:
        d_foreground.ellipse([wx - wr*2, wy - wr*2, wx + wr*2, wy + wr*2], fill=(45, 175, 200, 28))
        d_foreground.ellipse([wx - int(wr*1.2), wy - int(wr*1.2), wx + int(wr*1.2), wy + int(wr*1.2)], fill=(55, 195, 220, 70))
        d_foreground.ellipse([wx - int(wr*0.6), wy - int(wr*0.6), wx + int(wr*0.6), wy + int(wr*0.6)], fill=SOUL_CYAN)
        d_foreground.point([(wx, wy)], fill=SOUL_WHITE)

    spores = [
        (26, 44), (62, 26), (90, 16), (140, 32), (166, 22), (216, 16),
        (240, 58), (12, 176), (238, 192), (100, 166)
    ]
    for sx, sy in spores:
        d_foreground.point([(sx, sy)], fill=MOON_RIM_LIGHT)
        d_foreground.point([(sx, sy - 1)], fill=MOON_SPEC)

    layers = [
        ("Sky & Luminous Moon", l_sky),
        ("Far Background Treeline", l_far_bg),
        ("Midground Fog Bank", l_mid_fog),
        ("Gnarled Tree Wood", l_tree_base),
        ("Tree Shading & Rimlight", l_tree_shade),
        ("Spanish Moss & Lichen", l_moss),
        ("Graveyard Earth & Stones", l_graveyard),
        ("Foreground Fog & Lantern", l_foreground)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_haunted_tree_background()
    out_path = Path("/tmp/haunted_tree_bg_256.png")
    composite.save(out_path)
    print(f"Master Haunted Tree Background Art rendered successfully to {out_path}")
