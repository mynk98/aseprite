#!/usr/bin/env python3
"""
Master Sci-Fi Interceptor Pixel Art Generator (500x500 Canvas)
Renders a military-grade interstellar fighter across 8 distinct layers:
1. Engine Plasma & Ion Shock Diamonds
2. Engine Thrusters & Reactor Nozzles
3. Chassis & Undercarriage Silhouette
4. Modular Heavy Armor Plating (Fuselage & Wings)
5. Kinetic Railguns, Missiles & Particle Lances
6. Cockpit Canopy & Holographic Tactical HUD
7. Cyber Orange Hazard Stripes & Radiator Grilles
8. Edge Highlights & Armor Panel Seams
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

def draw_spaceship():
    w, h = 500, 500
    cx = 250

    # 8 Discrete Layers
    l_plasma   = Image.new('RGBA', (w, h), (0,0,0,0))
    l_thruster = Image.new('RGBA', (w, h), (0,0,0,0))
    l_chassis  = Image.new('RGBA', (w, h), (0,0,0,0))
    l_armor    = Image.new('RGBA', (w, h), (0,0,0,0))
    l_weapons  = Image.new('RGBA', (w, h), (0,0,0,0))
    l_cockpit  = Image.new('RGBA', (w, h), (0,0,0,0))
    l_decals   = Image.new('RGBA', (w, h), (0,0,0,0))
    l_outlines = Image.new('RGBA', (w, h), (0,0,0,0))

    d_plasma   = ImageDraw.Draw(l_plasma)
    d_thruster = ImageDraw.Draw(l_thruster)
    d_chassis  = ImageDraw.Draw(l_chassis)
    d_armor    = ImageDraw.Draw(l_armor)
    d_weapons  = ImageDraw.Draw(l_weapons)
    d_cockpit  = ImageDraw.Draw(l_cockpit)
    d_decals   = ImageDraw.Draw(l_decals)
    d_outlines = ImageDraw.Draw(l_outlines)

    # Palette
    C_BLACK      = (10, 14, 20, 255)
    C_OUTLINE    = (16, 20, 28, 255)
    C_VOID_DARK  = (22, 28, 38, 255)
    C_STEEL_DARK = (34, 42, 56, 255)
    C_STEEL_MID  = (50, 62, 80, 255)
    C_ARMOR_DARK = (68, 82, 104, 255)
    C_ARMOR_MID  = (92, 108, 134, 255)
    C_ARMOR_LIGHT= (130, 148, 178, 255)
    C_TITANIUM   = (180, 196, 220, 255)
    C_SPECULAR   = (240, 248, 255, 255)

    C_HAZARD_DARK  = (160, 40, 10, 255)
    C_HAZARD_MID   = (225, 75, 15, 255)
    C_HAZARD_LIGHT = (255, 135, 30, 255)

    C_CYAN_CORE = (255, 255, 255, 255)
    C_CYAN_HOT  = (170, 245, 255, 255)
    C_CYAN_MID  = (20, 190, 250, 255)
    C_CYAN_DEEP = (0, 110, 200, 255)
    C_VIOLET    = (120, 50, 230, 200)

    # Helpers
    def sym_poly(draw, pts, fill, outline=None, width=1):
        full = list(pts)
        for x, y in reversed(pts):
            rx = cx - (x - cx)
            if rx != x:
                full.append((rx, y))
        draw.polygon(full, fill=fill, outline=outline, width=width)

    def draw_pair(draw_fn):
        draw_fn(1)
        draw_fn(-1)

    def sym_line(draw, p1, p2, fill, width=1):
        draw.line([p1, p2], fill=fill, width=width)
        rx1 = cx - (p1[0] - cx)
        rx2 = cx - (p2[0] - cx)
        draw.line([(rx1, p1[1]), (rx2, p2[1])], fill=fill, width=width)

    # ==========================================
    # LAYER 1: ENGINE PLASMA & SHOCK DIAMONDS
    # ==========================================
    thrusters = [
        (cx, 400, 36, 95),       # Center Main
        (cx - 72, 385, 22, 75),  # Port
        (cx + 72, 385, 22, 75)   # Starboard
    ]
    for ex, ey, ew, el in thrusters:
        d_plasma.polygon([(ex - ew*1.2, ey), (ex + ew*1.2, ey), (ex, ey + el*1.15)], fill=(70, 30, 180, 120))
        d_plasma.polygon([(ex - ew, ey), (ex + ew, ey), (ex, ey + el)], fill=C_VIOLET)
        d_plasma.polygon([(ex - ew*0.65, ey), (ex + ew*0.65, ey), (ex, ey + el*0.8)], fill=C_CYAN_DEEP)
        d_plasma.polygon([(ex - ew*0.4, ey), (ex + ew*0.4, ey), (ex, ey + el*0.55)], fill=C_CYAN_MID)
        d_plasma.polygon([(ex - ew*0.2, ey), (ex + ew*0.2, ey), (ex, ey + el*0.35)], fill=C_CYAN_HOT)
        d_plasma.line([(ex, ey), (ex, ey + el*0.3)], fill=C_CYAN_CORE, width=3)
        # Shock diamonds
        for ratio in [0.25, 0.5, 0.75]:
            sy = ey + int(el * ratio)
            sw = max(2, int(ew * (1.0 - ratio * 0.9) * 0.45))
            d_plasma.polygon([(ex, sy - sw), (ex + sw, sy), (ex, sy + sw), (ex - sw, sy)], fill=C_CYAN_HOT)
            d_plasma.point([(ex, sy)], fill=C_CYAN_CORE)

    # ==========================================
    # LAYER 2: THRUSTER NOZZLES & HEAT COILS
    # ==========================================
    for ex, ey, ew, _ in thrusters:
        d_thruster.rectangle([ex - ew - 4, ey - 22, ex + ew + 4, ey], fill=C_STEEL_DARK, outline=C_OUTLINE, width=2)
        d_thruster.ellipse([ex - ew - 1, ey - 7, ex + ew + 1, ey + 3], fill=C_CYAN_DEEP, outline=C_CYAN_MID, width=1)
        d_thruster.ellipse([ex - ew*0.6, ey - 5, ex + ew*0.6, ey + 1], fill=C_CYAN_HOT)
        d_thruster.line([(ex - ew*0.4, ey - 2), (ex + ew*0.4, ey - 2)], fill=C_CYAN_CORE, width=2)
        for fx in range(int(ex - ew), int(ex + ew + 1), 6):
            d_thruster.line([(fx, ey - 22), (fx, ey - 5)], fill=C_STEEL_MID, width=1)
            d_thruster.point([(fx, ey - 5)], fill=C_TITANIUM)

    # ==========================================
    # LAYER 3: CHASSIS & UNDERCARRIAGE SILHOUETTE
    # ==========================================
    wing_under = [
        (cx, 110),
        (cx + 40, 150),
        (cx + 95, 210),
        (cx + 215, 305), # Outermost wingtip
        (cx + 220, 320), # Wingtip bevel
        (cx + 180, 350), # Forward sweep notch
        (cx + 175, 375), # Secondary fin
        (cx + 130, 375), # Aft engine cove
        (cx + 105, 395),
        (cx + 50, 400),  # Center engine bay
        (cx, 404)
    ]
    sym_poly(d_chassis, wing_under, fill=C_VOID_DARK, outline=C_OUTLINE, width=2)

    # Mechanical under-wing recesses
    for side in (-1, 1):
        wx = cx + side * 145
        d_chassis.rectangle([wx - 25, 290, wx + 25, 345], fill=C_BLACK, outline=C_STEEL_DARK, width=1)
        for gy in range(295, 345, 6):
            d_chassis.line([(wx - 22, gy), (wx + 22, gy)], fill=C_STEEL_DARK, width=2)
            d_chassis.point([(wx, gy)], fill=C_STEEL_MID)

    # ==========================================
    # LAYER 4: MODULAR ARMOR PLATING
    # ==========================================
    # 1. Main Fuselage Center Wedge (Smooth aerodynamic contours)
    fuse_pts = [
        (cx, 38),        # Forward spear-point nose
        (cx + 16, 75),   # Forward beak
        (cx + 28, 130),  # Canard junction
        (cx + 42, 185),  # Shoulder
        (cx + 54, 250),  # Mid hull flank
        (cx + 48, 335),  # Aft flank
        (cx + 30, 385),  # Engine shroud
        (cx, 392)
    ]
    sym_poly(d_armor, fuse_pts, fill=C_ARMOR_MID, outline=C_OUTLINE, width=1)

    # 2. Elevated Titanium Center Spine
    spine_pts = [
        (cx, 48),
        (cx + 9, 85),
        (cx + 14, 145),
        (cx + 16, 250),
        (cx + 11, 335),
        (cx, 365)
    ]
    sym_poly(d_armor, spine_pts, fill=C_TITANIUM, outline=C_STEEL_DARK, width=1)

    # 3. Swept Forward Canards (Fore-wings)
    canard_pts = [
        (cx + 26, 135),
        (cx + 85, 180),  # Canard tip
        (cx + 88, 192),
        (cx + 46, 192),
        (cx + 28, 168)
    ]
    sym_poly(d_armor, canard_pts, fill=C_ARMOR_LIGHT, outline=C_OUTLINE, width=1)

    # 4. Swept Main Primary Wings (Layered armor bevels)
    main_wing_outer = [
        (cx + 52, 210),
        (cx + 210, 300), # Leading edge tip
        (cx + 215, 312),
        (cx + 175, 340), # Trailing edge
        (cx + 125, 330),
        (cx + 60, 255)
    ]
    sym_poly(d_armor, main_wing_outer, fill=C_ARMOR_MID, outline=C_OUTLINE, width=1)

    # Secondary mid-wing armored flap
    mid_wing_slab = [
        (cx + 50, 245),
        (cx + 125, 290),
        (cx + 140, 360),
        (cx + 55, 368)
    ]
    sym_poly(d_armor, mid_wing_slab, fill=C_ARMOR_LIGHT, outline=C_STEEL_DARK, width=1)

    # Trailing edge control flaps
    flap_pts = [
        (cx + 65, 370),
        (cx + 135, 362),
        (cx + 130, 376),
        (cx + 63, 382)
    ]
    sym_poly(d_armor, flap_pts, fill=C_STEEL_MID, outline=C_OUTLINE, width=1)

    # Independent Side Air Intakes (Left & Right independently, NOT spanning center)
    for s in (-1, 1):
        # Intake cowl
        d_armor.polygon([(cx + s*42, 195), (cx + s*56, 195), (cx + s*52, 245), (cx + s*40, 245)], fill=C_ARMOR_DARK, outline=C_OUTLINE)
        # Inner intake intake scoop
        d_armor.polygon([(cx + s*44, 198), (cx + s*54, 198), (cx + s*50, 238), (cx + s*42, 238)], fill=C_BLACK)
        # Glowing cyan turbine fan blade inside scoop
        d_armor.line([(cx + s*45, 215), (cx + s*51, 215)], fill=C_CYAN_DEEP, width=2)
        d_armor.line([(cx + s*46, 222), (cx + s*49, 222)], fill=C_CYAN_MID, width=2)

    # ==========================================
    # LAYER 5: KINETIC RAILGUNS & HARDPOINTS
    # ==========================================
    for side in (-1, 1):
        # Heavy Dorsal Railgun at X: cx +/- 32
        rx = cx + side * 32
        d_weapons.rectangle([rx - 5, 95, rx + 5, 175], fill=C_STEEL_DARK, outline=C_OUTLINE, width=1)
        d_weapons.rectangle([rx - 4, 45, rx - 1, 95], fill=C_TITANIUM, outline=C_OUTLINE, width=1)
        d_weapons.rectangle([rx + 1, 45, rx + 4, 95], fill=C_TITANIUM, outline=C_OUTLINE, width=1)
        for cy in range(52, 92, 7):
            d_weapons.line([(rx - 4, cy), (rx + 4, cy)], fill=C_CYAN_MID, width=2)
            d_weapons.point([(rx, cy)], fill=C_CYAN_CORE)
        d_weapons.point([(rx, 43), (rx, 44)], fill=C_CYAN_CORE)

        # Micro-Missile Pod Batteries on mid-wings (X: cx +/- 140)
        mx = cx + side * 140
        d_weapons.rectangle([mx - 11, 275, mx + 11, 320], fill=C_STEEL_DARK, outline=C_OUTLINE, width=1)
        for col in (-5, 5):
            for row in (282, 292, 302, 312):
                d_weapons.ellipse([mx + col - 3, row - 3, mx + col + 3, row + 3], fill=C_HAZARD_DARK, outline=C_BLACK)
                d_weapons.point([(mx + col, row)], fill=C_HAZARD_LIGHT)

        # Wingtip Heavy Particle Beams (X: cx +/- 212)
        lx = cx + side * 212
        d_weapons.rectangle([lx - 3, 270, lx + 3, 310], fill=C_STEEL_MID, outline=C_OUTLINE, width=1)
        d_weapons.line([(lx, 255), (lx, 270)], fill=C_TITANIUM, width=2)
        d_weapons.ellipse([lx - 2, 252, lx + 2, 256], fill=(255, 60, 60, 255), outline=C_SPECULAR)

    # ==========================================
    # LAYER 6: COCKPIT CANOPY & SENSOR ARRAYS
    # ==========================================
    canopy_shell = [
        (cx, 98),        # Front apex
        (cx + 12, 118),  # Upper facet
        (cx + 13, 148),  # Mid facet
        (cx + 8, 170),   # Aft taper
        (cx, 176)
    ]
    sym_poly(d_cockpit, canopy_shell, fill=(4, 32, 40, 255), outline=C_BLACK, width=2)

    inner_canopy = [
        (cx, 105),
        (cx + 9, 122),
        (cx + 10, 144),
        (cx + 6, 164),
        (cx, 168)
    ]
    sym_poly(d_cockpit, inner_canopy, fill=(12, 115, 130, 255))

    # Tactical HUD Lattice Grid
    sym_poly(d_cockpit, [(cx, 114), (cx + 6, 126), (cx + 6, 142), (cx + 3, 158), (cx, 162)], fill=C_CYAN_HOT)
    d_cockpit.point([(cx, 138)], fill=C_CYAN_CORE)
    d_cockpit.line([(cx - 3, 138), (cx + 3, 138)], fill=C_CYAN_CORE, width=1)
    d_cockpit.line([(cx, 135), (cx, 141)], fill=C_CYAN_CORE, width=1)

    # Specular white reflection streak
    d_cockpit.line([(cx - 7, 116), (cx - 4, 152)], fill=C_SPECULAR, width=2)
    d_cockpit.line([(cx - 9, 124), (cx - 7, 145)], fill=C_CYAN_CORE, width=1)

    # Dorsal Antimatter Reactor Core (Y: 215 to 265)
    d_cockpit.ellipse([cx - 11, 215, cx + 11, 265], fill=C_STEEL_DARK, outline=C_OUTLINE, width=2)
    d_cockpit.ellipse([cx - 8, 218, cx + 8, 262], fill=C_CYAN_DEEP, outline=C_CYAN_MID, width=1)
    d_cockpit.ellipse([cx - 5, 224, cx + 5, 256], fill=C_CYAN_HOT)
    d_cockpit.ellipse([cx - 2, 232, cx + 2, 248], fill=C_CYAN_CORE)
    for cy in (228, 240, 252):
        d_cockpit.line([(cx - 11, cy), (cx - 6, cy)], fill=C_TITANIUM, width=2)
        d_cockpit.line([(cx + 6, cy), (cx + 11, cy)], fill=C_TITANIUM, width=2)

    # ==========================================
    # LAYER 7: HAZARD DECALS, GREEBLES & VENTS
    # ==========================================
    for side in (-1, 1):
        # Canard leading edge stripe
        sym_poly(d_decals, [(cx + 42, 162), (cx + 72, 178), (cx + 68, 184), (cx + 38, 168)], fill=C_HAZARD_MID)
        sym_poly(d_decals, [(cx + 45, 164), (cx + 70, 177), (cx + 67, 181), (cx + 42, 168)], fill=C_HAZARD_LIGHT)

        # Main wing diagonal warning chevrons
        sym_poly(d_decals, [(cx + 115, 250), (cx + 160, 275), (cx + 152, 283), (cx + 107, 258)], fill=C_HAZARD_MID)
        sym_poly(d_decals, [(cx + 120, 253), (cx + 155, 274), (cx + 149, 279), (cx + 114, 258)], fill=C_HAZARD_LIGHT)

    # Radiator cooling fins on fuselage aft (Y: 285 to 345)
    for side in (-1, 1):
        gx = cx + side * 24
        for gy in range(285, 345, 7):
            d_decals.line([(gx - 6, gy), (gx + 6, gy)], fill=C_BLACK, width=2)
            d_decals.point([(gx + 6, gy)], fill=C_STEEL_MID)

    # Glowing Energy Shield Conduits on Wing Slabs (Neon Cyan Circuit Lines)
    for side in (-1, 1):
        d_decals.line([(cx + side*75, 260), (cx + side*135, 305)], fill=C_CYAN_DEEP, width=1)
        d_decals.line([(cx + side*135, 305), (cx + side*170, 315)], fill=C_CYAN_MID, width=1)
        d_decals.point([(cx + side*75, 260), (cx + side*135, 305), (cx + side*170, 315)], fill=C_CYAN_CORE)

    # Navigation lights
    d_decals.ellipse([cx - 218, 305, cx - 210, 313], fill=(255, 25, 25, 255), outline=C_SPECULAR, width=1) # Red Port
    d_decals.ellipse([cx + 210, 305, cx + 218, 313], fill=(25, 255, 80, 255), outline=C_SPECULAR, width=1) # Green Starboard
    d_decals.point([(cx - 86, 182), (cx + 86, 182)], fill=C_CYAN_CORE)
    d_decals.ellipse([cx - 2, 388, cx + 2, 392], fill=C_CYAN_CORE)

    # ==========================================
    # LAYER 8: OUTLINES & SPECULAR HIGHLIGHTS
    # ==========================================
    d_outlines.line([(cx, 38), (cx, 95)], fill=C_SPECULAR, width=1)
    sym_line(d_outlines, (cx + 1, 39), (cx + 16, 75), fill=C_SPECULAR, width=1)
    sym_line(d_outlines, (cx + 26, 135), (cx + 84, 180), fill=C_SPECULAR, width=1)
    sym_line(d_outlines, (cx + 52, 210), (cx + 209, 300), fill=C_SPECULAR, width=1)

    # Armor plate seams
    sym_line(d_outlines, (cx + 16, 130), (cx + 26, 135), fill=C_OUTLINE, width=1)
    sym_line(d_outlines, (cx + 18, 250), (cx + 54, 250), fill=C_OUTLINE, width=1)
    sym_line(d_outlines, (cx + 14, 310), (cx + 48, 310), fill=C_OUTLINE, width=1)
    sym_line(d_outlines, (cx + 85, 230), (cx + 115, 270), fill=C_OUTLINE, width=1)
    sym_line(d_outlines, (cx + 125, 255), (cx + 165, 300), fill=C_OUTLINE, width=1)

    layers = [
        ("Engine Plasma & Wakes", l_plasma),
        ("Thrusters & Nozzles", l_thruster),
        ("Chassis & Undercarriage", l_chassis),
        ("Modular Armor Plating", l_armor),
        ("Kinetic Railguns & Missiles", l_weapons),
        ("Cockpit & Reactor Core", l_cockpit),
        ("Hazard Decals & Greebles", l_decals),
        ("Highlights & Outlines", l_outlines)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_spaceship()
    composite.save('/tmp/scifi_spaceship.png')
    print("Sci-Fi Spaceship successfully rendered to /tmp/scifi_spaceship.png")
