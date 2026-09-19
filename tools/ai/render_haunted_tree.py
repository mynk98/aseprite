#!/usr/bin/env python3
"""
Master Pixel Art Asset for 256x256 Canvas:
"The Gnarled Haunted Elder Tree"
Authentic, continuous gothic pixel art asset across 8 discrete layers:
1. Ground & Creeping Fog (Cursed earth, sunken tombstones, twisted roots, rolling fog)
2. Hollow Cavity & Soul Fire (Deep dark interior hollow with glowing soul core & spirit eyes)
3. Gnarled Trunk & Muscular Buttresses (Monolithic ancient twisting trunk, seamless root flares)
4. Multi-Tier Sprawling Branches (Unified branching hierarchy, sprawling organic canopy)
5. Bark Fissures & Haunted Face (Deep bark grain grooves, agonized face, moonlit rim light)
6. Weeping Spanish Moss & Cobwebs (Organic dripping lichen clusters, fine gossamer webs)
7. Perched Raven & Iron Soul Lantern (Detailed sinister raven & hanging cage lantern)
8. Will-o'-the-Wisps & Spectral Spores (Luminous floating spirit orbs & night embers)
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np
import math

def draw_haunted_tree():
    w, h = 256, 256

    # 8 Discrete Layers
    l_ground     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_hollow     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_trunk      = Image.new('RGBA', (w, h), (0,0,0,0))
    l_branches   = Image.new('RGBA', (w, h), (0,0,0,0))
    l_bark       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_moss       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_props      = Image.new('RGBA', (w, h), (0,0,0,0))
    l_wisps      = Image.new('RGBA', (w, h), (0,0,0,0))

    d_ground     = ImageDraw.Draw(l_ground)
    d_hollow     = ImageDraw.Draw(l_hollow)
    d_trunk      = ImageDraw.Draw(l_trunk)
    d_branches   = ImageDraw.Draw(l_branches)
    d_bark       = ImageDraw.Draw(l_bark)
    d_moss       = ImageDraw.Draw(l_moss)
    d_props      = ImageDraw.Draw(l_props)
    d_wisps      = ImageDraw.Draw(l_wisps)

    # --- PROFESSIONAL GOTHIC PALETTE ---
    C_VOID         = (10, 6, 14, 255)
    C_INK_DARK     = (22, 16, 26, 255)
    C_INK_MID      = (36, 26, 42, 255)

    # Ancient Weathered Bark (Gothic Cold Slate / Ash)
    C_BARK_SHADOW  = (38, 28, 44, 255)
    C_BARK_BASE    = (58, 44, 66, 255)
    C_BARK_MID     = (82, 64, 90, 255)
    C_BARK_LIGHT   = (118, 96, 126, 255)
    C_MOON_EDGE    = (170, 150, 180, 255)
    C_MOON_SPEC    = (220, 208, 230, 255)

    # Spectral Soul Glow (Cyan/Aquamarine)
    C_SOUL_DEEP    = (10, 48, 60, 255)
    C_SOUL_MID     = (24, 128, 148, 255)
    C_SOUL_BRIGHT  = (64, 215, 230, 255)
    C_SOUL_WHITE   = (230, 255, 252, 255)

    # Sinister Spirit Eyes & Embers (Blood Amber / Crimson)
    C_EMBER_DARK   = (120, 24, 22, 255)
    C_EMBER_MID    = (215, 65, 30, 255)
    C_EMBER_GOLD   = (255, 185, 45, 255)

    # Weeping Spanish Moss (Swamp Sage Green)
    C_MOSS_DARK    = (24, 42, 34, 255)
    C_MOSS_MID     = (44, 76, 58, 255)
    C_MOSS_LIGHT   = (72, 118, 90, 255)
    C_MOSS_PALE    = (118, 168, 134, 255)

    # Toxic Swamp Fungi
    C_FUNGI_STEM   = (185, 175, 190, 255)
    C_FUNGI_DARK   = (110, 32, 138, 255)
    C_FUNGI_LIGHT  = (185, 75, 225, 255)

    # Rusted Iron & Wood
    C_IRON_DARK    = (26, 20, 22, 255)
    C_IRON_RUST    = (90, 44, 30, 255)
    C_IRON_LIGHT   = (142, 80, 54, 255)

    # =========================================================================
    # LAYER 1: GROUND & CREEPING FOG
    # =========================================================================
    mound = [
        (0, 256), (0, 244), (20, 238), (55, 232), (95, 228), (128, 227),
        (160, 228), (200, 232), (235, 238), (256, 244), (256, 256)
    ]
    d_ground.polygon(mound, fill=C_INK_DARK)
    d_ground.polygon([(x, y - 1) for x, y in mound[1:-1]], fill=C_BARK_SHADOW)
    d_ground.polygon([(x, y - 2) for x, y in mound[2:-2]], fill=C_BARK_BASE)

    # Weathered ancient tombstones sinking into soil
    # Left Tombstone (Rounded arch cross)
    d_ground.rounded_rectangle([30, 218, 44, 240], radius=4, fill=C_BARK_BASE, outline=C_INK_DARK, width=1)
    d_ground.line([(37, 222), (37, 234)], fill=C_BARK_LIGHT, width=1)
    d_ground.line([(33, 226), (41, 226)], fill=C_BARK_LIGHT, width=1)
    d_ground.line([(31, 219), (42, 219)], fill=C_MOON_EDGE, width=1)
    d_ground.line([(40, 228), (38, 231), (40, 235)], fill=C_INK_DARK, width=1)

    # Right Tombstone (Crooked slab)
    d_ground.polygon([(214, 222), (226, 218), (230, 240), (217, 242)], fill=C_BARK_SHADOW, outline=C_INK_DARK, width=1)
    d_ground.line([(215, 223), (225, 219)], fill=C_MOON_EDGE, width=1)
    d_ground.line([(220, 224), (221, 234)], fill=C_BARK_LIGHT, width=1)

    # Skull buried near root
    d_ground.ellipse([90, 234, 97, 240], fill=C_BARK_LIGHT, outline=C_INK_DARK, width=1)
    d_ground.point([(92, 237), (95, 237)], fill=C_INK_DARK)

    # Glowing toxic swamp fungi
    mushrooms = [
        (46, 234, 5, 6), (54, 236, 4, 5), (102, 238, 4, 5),
        (194, 235, 5, 7), (202, 234, 4, 5), (226, 240, 3, 4)
    ]
    for mx, my, rw, rh in mushrooms:
        d_ground.line([(mx, my), (mx, my - rh)], fill=C_FUNGI_STEM, width=1)
        d_ground.ellipse([mx - rw, my - rh - 2, mx + rw, my - rh + 2], fill=C_FUNGI_DARK, outline=C_INK_DARK, width=1)
        d_ground.ellipse([mx - rw + 1, my - rh - 1, mx + rw - 1, my - rh + 1], fill=C_FUNGI_LIGHT)
        d_ground.point([(mx, my - rh - 1)], fill=C_SOUL_WHITE)

    # Rolling ground mist
    for fy in range(230, 252, 3):
        alpha = int(35 + (fy - 230) * 4)
        d_ground.ellipse([8, fy, 140, fy + 8], fill=(28, 20, 40, alpha))
        d_ground.ellipse([110, fy + 2, 248, fy + 10], fill=(24, 16, 36, alpha))

    # =========================================================================
    # LAYER 4: MULTI-TIER SPRAWLING BRANCH CANOPY (DRAWN FIRST SO TRUNK WRAPS OVER BASES)
    # =========================================================================
    def draw_continuous_branch(draw, draw_bark, pts, start_r, end_r):
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

            # Outer outline
            poly_out = [
                (p1[0] + nx * (r1 + 1), p1[1] + ny * (r1 + 1)),
                (p2[0] + nx * (r2 + 1), p2[1] + ny * (r2 + 1)),
                (p2[0] - nx * (r2 + 1), p2[1] - ny * (r2 + 1)),
                (p1[0] - nx * (r1 + 1), p1[1] - ny * (r1 + 1))
            ]
            draw.polygon(poly_out, fill=C_INK_DARK)

            # Wood core
            poly_core = [
                (p1[0] + nx * r1, p1[1] + ny * r1),
                (p2[0] + nx * r2, p2[1] + ny * r2),
                (p2[0] - nx * r2, p2[1] - ny * r2),
                (p1[0] - nx * r1, p1[1] - ny * r1)
            ]
            draw.polygon(poly_core, fill=C_BARK_BASE)

            # Directional highlights on top/left
            hl_side = 1 if (nx * (-0.6) + ny * (-0.8)) > 0 else -1
            draw_bark.line([
                (p1[0] + nx * r1 * hl_side * 0.75, p1[1] + ny * r1 * hl_side * 0.75),
                (p2[0] + nx * r2 * hl_side * 0.75, p2[1] + ny * r2 * hl_side * 0.75)
            ], fill=C_BARK_LIGHT, width=max(1, int(r1 * 0.4)))

            if r1 > 2:
                draw_bark.line([
                    (p1[0] + nx * r1 * hl_side * 0.9, p1[1] + ny * r1 * hl_side * 0.9),
                    (p2[0] + nx * r2 * hl_side * 0.9, p2[1] + ny * r2 * hl_side * 0.9)
                ], fill=C_MOON_EDGE, width=1)

            # Shadow on bottom/right
            sh_side = -hl_side
            draw_bark.line([
                (p1[0] + nx * r1 * sh_side * 0.75, p1[1] + ny * r1 * sh_side * 0.75),
                (p2[0] + nx * r2 * sh_side * 0.75, p2[1] + ny * r2 * sh_side * 0.75)
            ], fill=C_BARK_SHADOW, width=max(1, int(r1 * 0.5)))

    # 1. LEFT MAIN BOUGH (Deep root origin at X: 90, Y: 110)
    draw_continuous_branch(d_branches, d_bark, [(90, 110), (70, 96), (54, 98), (40, 106), (28, 116), (18, 126)], 12, 3)
    draw_continuous_branch(d_branches, d_bark, [(40, 106), (32, 98), (22, 92), (12, 88), (6, 84)], 5, 1)
    draw_continuous_branch(d_branches, d_bark, [(28, 116), (24, 128), (16, 142), (10, 148), (4, 152)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(22, 92), (24, 80), (16, 70), (12, 64)], 3, 1)

    # 2. MID-LEFT REACHING BOUGH (Origin deep in trunk at X: 100, Y: 95)
    draw_continuous_branch(d_branches, d_bark, [(100, 95), (84, 84), (70, 76), (56, 70), (42, 62), (28, 56), (16, 48)], 10, 2)
    draw_continuous_branch(d_branches, d_bark, [(56, 70), (50, 56), (42, 44), (32, 36), (24, 30)], 5, 1)
    draw_continuous_branch(d_branches, d_bark, [(42, 62), (40, 74), (32, 84), (22, 90)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(50, 56), (56, 44), (54, 30), (50, 20)], 3, 1)

    # 3. HIGH-LEFT CROWN HORN (Origin in trunk at X: 115, Y: 85)
    draw_continuous_branch(d_branches, d_bark, [(115, 85), (108, 66), (98, 54), (88, 42), (78, 30), (70, 18), (64, 10)], 9, 1)
    draw_continuous_branch(d_branches, d_bark, [(98, 54), (102, 40), (100, 26), (94, 14)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(88, 42), (84, 30), (86, 18)], 3, 1)

    # 4. CENTRAL CROWN SPIRES (Origin deep in trunk at X: 124, Y: 85)
    draw_continuous_branch(d_branches, d_bark, [(122, 85), (118, 62), (116, 48), (112, 34), (108, 20), (104, 10)], 9, 1)
    draw_continuous_branch(d_branches, d_bark, [(112, 34), (118, 24), (116, 12)], 4, 1)

    draw_continuous_branch(d_branches, d_bark, [(132, 85), (128, 62), (132, 48), (138, 34), (144, 20), (148, 10)], 9, 1)
    draw_continuous_branch(d_branches, d_bark, [(138, 34), (132, 24), (134, 12)], 4, 1)

    # 5. HIGH-RIGHT CROWN HORN (Origin in trunk at X: 140, Y: 85)
    draw_continuous_branch(d_branches, d_bark, [(140, 85), (144, 68), (156, 54), (168, 42), (180, 30), (190, 20), (196, 12)], 9, 1)
    draw_continuous_branch(d_branches, d_bark, [(156, 54), (152, 40), (154, 26), (158, 14)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(168, 42), (174, 30), (172, 18)], 3, 1)

    # 6. MID-RIGHT REACHING BOUGH (Origin deep in trunk at X: 155, Y: 95)
    draw_continuous_branch(d_branches, d_bark, [(155, 95), (164, 84), (180, 78), (198, 72), (214, 64), (230, 56), (242, 46)], 10, 2)
    draw_continuous_branch(d_branches, d_bark, [(198, 72), (206, 58), (216, 46), (226, 36), (234, 30)], 5, 1)
    draw_continuous_branch(d_branches, d_bark, [(214, 64), (216, 76), (224, 86), (234, 92)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(206, 58), (200, 44), (202, 30)], 3, 1)

    # 7. RIGHT MAIN BOUGH (Holds lantern! Origin deep in trunk at X: 165, Y: 110)
    draw_continuous_branch(d_branches, d_bark, [(165, 110), (180, 96), (196, 100), (212, 106), (226, 114), (240, 124), (250, 132)], 12, 3)
    draw_continuous_branch(d_branches, d_bark, [(212, 106), (220, 96), (232, 90), (242, 86), (250, 82)], 5, 2)
    draw_continuous_branch(d_branches, d_bark, [(226, 114), (228, 126), (236, 138), (244, 146)], 4, 1)
    draw_continuous_branch(d_branches, d_bark, [(196, 100), (198, 114), (204, 126)], 4, 2) # Hook for lantern!

    # 8. LOW-RIGHT DROOPING ARM (Origin in trunk at X: 165, Y: 130)
    draw_continuous_branch(d_branches, d_bark, [(165, 130), (178, 136), (194, 146), (210, 158), (222, 170), (232, 180)], 8, 2)
    draw_continuous_branch(d_branches, d_bark, [(194, 146), (202, 136), (214, 130), (224, 126)], 3, 1)
    draw_continuous_branch(d_branches, d_bark, [(210, 158), (216, 172), (226, 180)], 2, 1)

    # =========================================================================
    # LAYER 3: GNARLED TRUNK & PRIMARY ROOTS (SEAMLESS ORGANIC BUTTRESSES)
    # =========================================================================
    trunk_mass = [
        # Left root tips & buttresses clawing left
        (14, 246), (28, 242), (48, 234), (74, 224), (88, 214), (96, 200),
        # Left trunk flank rising up
        (92, 180), (88, 160), (84, 140), (76, 120), (66, 106),
        # Left Bough Bridge seamlessly merging with branches
        (58, 98), (72, 92), (86, 88), (98, 80),
        # Crown Bough Bridges
        (108, 70), (116, 62), (124, 70), (132, 62), (140, 70),
        # Right Bough Bridge
        (152, 80), (164, 88), (178, 92), (192, 98),
        # Right trunk flank descending
        (182, 106), (174, 120), (168, 140), (164, 160), (162, 180),
        # Right root buttress clawing right
        (168, 200), (176, 214), (192, 224), (218, 234), (238, 242), (250, 246),
        # Ground root base bottom contour
        (236, 246), (210, 240), (182, 232), (160, 222),
        (138, 224), (128, 234), (122, 246), (116, 234), (108, 222),
        (88, 232), (60, 240), (32, 246)
    ]
    d_trunk.polygon(trunk_mass, fill=C_BARK_BASE, outline=C_INK_DARK, width=2)

    # Shading across the trunk mass:
    # Left moonlit flank
    d_trunk.polygon([
        (14, 246), (28, 242), (48, 234), (74, 224), (88, 214), (96, 200),
        (92, 180), (88, 160), (84, 140), (76, 120), (66, 106), (58, 98),
        (68, 98), (76, 110), (86, 122), (94, 142), (98, 162), (102, 182),
        (104, 202), (96, 216), (82, 226), (56, 236), (36, 244)
    ], fill=C_BARK_LIGHT)

    d_trunk.line([
        (16, 245), (30, 241), (50, 233), (76, 223), (90, 213), (98, 199),
        (94, 179), (90, 159), (86, 139), (78, 119), (68, 105), (60, 98)
    ], fill=C_MOON_EDGE, width=2)

    d_trunk.line([
        (94, 178), (90, 158), (86, 138), (78, 118)
    ], fill=C_MOON_SPEC, width=1)

    # Right deep shadow flank
    d_trunk.polygon([
        (192, 98), (182, 106), (174, 120), (168, 140), (164, 160), (162, 180),
        (168, 200), (176, 214), (192, 224), (218, 234), (238, 242), (250, 246),
        (236, 246), (216, 236), (190, 226), (174, 216), (166, 202),
        (160, 182), (162, 162), (166, 142), (172, 122), (180, 108)
    ], fill=C_BARK_SHADOW)

    # Muscular intermediate root tendons flowing across trunk belly
    d_trunk.polygon([(118, 212), (114, 226), (108, 238), (114, 240), (120, 228), (124, 214)], fill=C_BARK_LIGHT, outline=C_INK_DARK, width=1)
    d_trunk.polygon([(136, 212), (142, 224), (150, 234), (144, 236), (138, 226), (130, 214)], fill=C_BARK_SHADOW, outline=C_INK_DARK, width=1)

    # =========================================================================
    # LAYER 2: HOLLOW CAVITY VOID & SOUL CORE
    # =========================================================================
    mouth_hollow = [
        (114, 158), (122, 154), (134, 154), (142, 158),
        (146, 172), (144, 186), (138, 196), (128, 200), (118, 196), (112, 186), (110, 172)
    ]
    d_hollow.polygon(mouth_hollow, fill=C_VOID, outline=C_INK_DARK, width=2)

    # Wooden fangs
    d_hollow.polygon([(116, 157), (118, 165), (121, 156)], fill=C_BARK_LIGHT)
    d_hollow.polygon([(124, 155), (126, 167), (129, 155)], fill=C_MOON_EDGE)
    d_hollow.polygon([(132, 155), (134, 164), (137, 156)], fill=C_BARK_MID)
    d_hollow.polygon([(118, 195), (120, 187), (123, 197)], fill=C_BARK_MID)
    d_hollow.polygon([(129, 198), (132, 189), (135, 197)], fill=C_BARK_SHADOW)

    # Soul Core inside mouth
    d_hollow.ellipse([118, 172, 138, 192], fill=C_SOUL_DEEP)
    d_hollow.ellipse([121, 175, 135, 189], fill=C_SOUL_MID)
    d_hollow.ellipse([124, 178, 132, 186], fill=C_SOUL_BRIGHT)
    d_hollow.point([(128, 182)], fill=C_SOUL_WHITE)

    # Spirit eyes
    l_eye = [(110, 137), (116, 133), (122, 138), (118, 141), (112, 140)]
    d_hollow.polygon(l_eye, fill=C_VOID, outline=C_INK_DARK, width=1)
    d_hollow.ellipse([113, 135, 119, 139], fill=C_EMBER_DARK)
    d_hollow.ellipse([114, 136, 118, 138], fill=C_EMBER_GOLD)
    d_hollow.point([(116, 137)], fill=C_SOUL_WHITE)

    r_eye = [(134, 138), (140, 133), (146, 137), (144, 140), (138, 141)]
    d_hollow.polygon(r_eye, fill=C_VOID, outline=C_INK_DARK, width=1)
    d_hollow.ellipse([137, 135, 143, 139], fill=C_EMBER_DARK)
    d_hollow.ellipse([138, 136, 142, 138], fill=C_EMBER_GOLD)
    d_hollow.point([(140, 137)], fill=C_SOUL_WHITE)

    # Fissure
    fissure = [(126, 112), (129, 108), (131, 112), (129, 120)]
    d_hollow.polygon(fissure, fill=C_VOID)
    d_hollow.line([(128, 110), (128, 118)], fill=C_SOUL_BRIGHT, width=1)
    d_hollow.point([(128, 113)], fill=C_SOUL_WHITE)

    # Cut out holes from trunk layer so hollow shows cleanly
    d_trunk.polygon(mouth_hollow, fill=(0,0,0,0))
    d_trunk.polygon(l_eye, fill=(0,0,0,0))
    d_trunk.polygon(r_eye, fill=(0,0,0,0))
    d_trunk.polygon(fissure, fill=(0,0,0,0))

    # =========================================================================
    # LAYER 5: BARK FISSURES & HAUNTED FACE DETAIL
    # =========================================================================
    # Brow ridge over eyes
    d_bark.polygon([
        (106, 131), (116, 127), (124, 131), (132, 127), (142, 131),
        (136, 125), (128, 123), (120, 125), (112, 127)
    ], fill=C_BARK_LIGHT, outline=C_INK_DARK, width=1)
    d_bark.line([(116, 127), (128, 123), (136, 125)], fill=C_MOON_EDGE, width=1)

    # Mouth lips
    d_bark.line([(112, 156), (122, 153), (134, 153), (144, 156)], fill=C_MOON_EDGE, width=1)
    d_bark.line([(109, 170), (111, 186), (115, 196), (128, 201)], fill=C_MOON_EDGE, width=1)
    d_bark.line([(145, 170), (143, 186), (139, 196), (128, 201)], fill=C_BARK_SHADOW, width=1)

    # Wood grain strictly within the trunk
    for y in range(112, 210, 4):
        # Left grain strictly inside trunk (X: 98 to 108)
        d_bark.line([(100, y), (106, y + 2)], fill=C_BARK_LIGHT, width=1)
        d_bark.point([(99, y)], fill=C_MOON_EDGE)
        # Right grain strictly inside trunk (X: 148 to 158)
        d_bark.line([(148, y + 2), (154, y)], fill=C_BARK_SHADOW, width=1)

    # Knots on branch forks
    knots = [(52, 88), (176, 92), (102, 60), (148, 58), (188, 74), (36, 118), (160, 142)]
    for kx, ky in knots:
        d_bark.ellipse([kx - 3, ky - 2, kx + 3, ky + 2], fill=C_INK_DARK)
        d_bark.ellipse([kx - 2, ky - 1, kx + 2, ky + 1], fill=C_BARK_SHADOW)
        d_bark.point([(kx, ky)], fill=C_SOUL_DEEP)

    # Ghostly spirit mist seeping upward from the open mouth
    for my, alpha in [(152, 90), (148, 120), (144, 150), (140, 100), (136, 60)]:
        d_bark.ellipse([124, my, 132, my + 4], fill=(64, 215, 230, alpha))
        d_bark.point([(128, my + 1)], fill=C_SOUL_WHITE)

    # =========================================================================
    # LAYER 6: WEEPING SPANISH MOSS & WEBBING (ORGANIC SOFT DRIPS)
    # =========================================================================
    def draw_moss_cluster(draw, x, y, length, max_w):
        for dy in range(length):
            w_cur = max(0, int(max_w * (1.0 - dy / length) + math.sin(dy * 0.7 + x) * 1.2))
            cx = x + int(math.sin(dy * 0.35 + x * 0.5) * 2)
            for ox in range(-w_cur, w_cur + 1):
                col = C_MOSS_DARK if abs(ox) == w_cur else (C_MOSS_MID if abs(ox) > 0 else C_MOSS_LIGHT)
                draw.point([(cx + ox, y + dy)], fill=col)
        # Tip droplet
        draw.point([(x + int(math.sin(length * 0.35 + x * 0.5) * 2), y + length)], fill=C_MOSS_PALE)

    moss_anchors = [
        (36, 108, 20, 3), (24, 118, 14, 3), (48, 108, 24, 4), (38, 74, 16, 3),
        (54, 72, 20, 3), (80, 56, 14, 3), (100, 42, 16, 3), (128, 48, 18, 4),
        (160, 46, 16, 3), (184, 62, 18, 3), (210, 72, 22, 4), (226, 88, 16, 3),
        (238, 116, 18, 3), (196, 142, 14, 3), (214, 154, 18, 3)
    ]
    for mx, my, mlen, mw in moss_anchors:
        draw_moss_cluster(d_moss, mx, my, mlen, mw)

    # Gossamer webs
    webs = [
        [(54, 72), (44, 64), (60, 84)],
        [(170, 64), (186, 54), (176, 76)],
        [(116, 62), (112, 46), (122, 38)],
        [(210, 104), (218, 118), (226, 108)]
    ]
    for w_pts in webs:
        for i in range(len(w_pts)):
            p1 = w_pts[i]
            p2 = w_pts[(i+1)%len(w_pts)]
            d_moss.line([p1, p2], fill=(175, 195, 205, 70), width=1)
        d_moss.line([w_pts[0], w_pts[1]], fill=(205, 225, 235, 80), width=1)

    # =========================================================================
    # LAYER 7: PERCHED RAVEN & RUSTED CAGE LANTERN
    # =========================================================================
    # 1. Sinister Black Raven perched on high-left branch
    raven_poly = [
        (42, 68), (48, 72), (56, 70), (62, 62), (58, 54), (50, 52), (44, 56), (38, 64)
    ]
    d_props.polygon(raven_poly, fill=C_VOID, outline=C_INK_DARK)
    d_props.polygon([(44, 66), (48, 70), (54, 68), (58, 62), (56, 56), (50, 54), (45, 58)], fill=C_BARK_SHADOW)
    # Wing feathers
    d_props.line([(44, 62), (50, 68), (54, 70)], fill=C_BARK_LIGHT, width=1)
    d_props.line([(46, 64), (52, 69)], fill=C_MOON_EDGE, width=1)
    # Tail feathers pointing down-left
    d_props.polygon([(38, 64), (44, 66), (34, 74), (32, 72)], fill=C_VOID)
    d_props.line([(38, 65), (34, 72)], fill=C_BARK_LIGHT, width=1)
    # Head & beak
    d_props.ellipse([54, 48, 62, 56], fill=C_VOID)
    d_props.polygon([(61, 51), (68, 53), (61, 55)], fill=C_IRON_DARK) # Beak
    # Glowing eye
    d_props.point([(58, 51)], fill=C_EMBER_MID)
    d_props.point([(59, 51)], fill=C_EMBER_GOLD)
    # Feet gripping branch
    d_props.line([(48, 71), (48, 74)], fill=C_IRON_RUST, width=1)
    d_props.line([(53, 70), (53, 73)], fill=C_IRON_RUST, width=1)

    # 2. Rusted Iron Hanging Cage Lantern on right bough (X: 202, Y: 112 to 146)
    for cy in range(114, 125, 2):
        d_props.line([(200, cy), (200, cy + 1)], fill=C_IRON_RUST, width=1)
        d_props.point([(201, cy)], fill=C_IRON_LIGHT)

    # Pyramid roof cap
    d_props.polygon([(192, 125), (200, 121), (208, 125)], fill=C_IRON_DARK, outline=C_VOID)
    d_props.line([(193, 125), (200, 122)], fill=C_IRON_LIGHT, width=1)

    # Cage frame
    d_props.rectangle([192, 125, 208, 141], outline=C_IRON_DARK, width=1)
    d_props.line([(196, 125), (196, 141)], fill=C_IRON_DARK, width=1)
    d_props.line([(204, 125), (204, 141)], fill=C_IRON_DARK, width=1)

    # Glass panes & inner soul flame
    d_props.rectangle([193, 126, 207, 140], fill=(12, 38, 48, 190))
    d_props.ellipse([195, 128, 205, 138], fill=C_SOUL_DEEP)
    d_props.ellipse([197, 130, 203, 136], fill=C_SOUL_MID)
    d_props.ellipse([198, 131, 202, 135], fill=C_SOUL_BRIGHT)
    d_props.point([(200, 133)], fill=C_SOUL_WHITE)

    # Bottom spike
    d_props.polygon([(194, 141), (200, 146), (206, 141)], fill=C_IRON_DARK, outline=C_VOID)
    d_props.point([(200, 146)], fill=C_IRON_LIGHT)

    # =========================================================================
    # LAYER 8: WILL-O'-THE-WISPS & SPECTRAL SPORES
    # =========================================================================
    wisps = [
        (38, 110, 5),   # Left lower
        (72, 50, 6),    # Left crown
        (124, 32, 5),   # High center
        (184, 48, 6),   # Right crown
        (232, 90, 5),   # Far right mid
        (98, 130, 4),   # Trunk shoulder
        (158, 144, 5),  # Right hollow flank
        (64, 164, 4)    # Near ground roots
    ]

    for wx, wy, wr in wisps:
        d_wisps.ellipse([wx - wr*2, wy - wr*2, wx + wr*2, wy + wr*2], fill=(24, 145, 170, 38))
        d_wisps.ellipse([wx - int(wr*1.3), wy - int(wr*1.3), wx + int(wr*1.3), wy + int(wr*1.3)], fill=(32, 175, 200, 85))
        d_wisps.ellipse([wx - int(wr*0.7), wy - int(wr*0.7), wx + int(wr*0.7), wy + int(wr*0.7)], fill=C_SOUL_MID)
        d_wisps.ellipse([wx - int(wr*0.4), wy - int(wr*0.4), wx + int(wr*0.4), wy + int(wr*0.4)], fill=C_SOUL_BRIGHT)
        d_wisps.point([(wx, wy)], fill=C_SOUL_WHITE)
        # Trailing soul embers
        d_wisps.point([(wx - 1, wy + wr + 1), (wx, wy + wr + 2), (wx + 1, wy + wr + 3)], fill=C_SOUL_MID)
        d_wisps.point([(wx + 2, wy + wr + 4)], fill=C_SOUL_DEEP)

    # Ambient night spores
    spores = [
        (24, 44), (58, 20), (90, 16), (142, 14), (166, 20), (214, 18),
        (242, 52), (16, 184), (234, 202), (82, 214), (170, 218)
    ]
    for sx, sy in spores:
        d_wisps.point([(sx, sy)], fill=C_SOUL_BRIGHT)
        d_wisps.point([(sx, sy - 1)], fill=C_SOUL_WHITE)

    layers = [
        ("Ground & Creeping Fog", l_ground),
        ("Hollow Void & Soul Core", l_hollow),
        ("Gnarled Trunk & Roots", l_trunk),
        ("Multi-Tier Branches", l_branches),
        ("Bark Grain & Face", l_bark),
        ("Weeping Moss & Webs", l_moss),
        ("Raven & Iron Lantern", l_props),
        ("Will-o-Wisps & Spores", l_wisps)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_haunted_tree()
    out_path = Path("/tmp/haunted_tree_256.png")
    composite.save(out_path)
    print(f"Haunted Tree rendered successfully to {out_path}")
