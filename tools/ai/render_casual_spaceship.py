#!/usr/bin/env python3
"""
Casual Mobile Game Spaceship Pixel Art Generator (500x500 Canvas)
Renders a juicy, vibrant, mobile-game styled starfighter:
- Smooth, chunky aerodynamic curves with excellent readability
- Glossy candy-lacquer finish (Pearl White, Electric Royal Azure, Polished Gold)
- Jewel-like bubble cockpit with bright cartoon specular reflections
- Chunky dual rounded energy blasters with glowing orb tips
- Cute stylized plasma flames with floating star sparkles
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

def draw_casual_spaceship():
    w, h = 500, 500
    cx = 250

    # 8 Discrete Layers
    l_plasma   = Image.new('RGBA', (w, h), (0,0,0,0))
    l_thruster = Image.new('RGBA', (w, h), (0,0,0,0))
    l_wings    = Image.new('RGBA', (w, h), (0,0,0,0))
    l_armor    = Image.new('RGBA', (w, h), (0,0,0,0))
    l_gold     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_canopy   = Image.new('RGBA', (w, h), (0,0,0,0))
    l_weapons  = Image.new('RGBA', (w, h), (0,0,0,0))
    l_highlights = Image.new('RGBA', (w, h), (0,0,0,0))

    d_plasma   = ImageDraw.Draw(l_plasma)
    d_thruster = ImageDraw.Draw(l_thruster)
    d_wings    = ImageDraw.Draw(l_wings)
    d_armor    = ImageDraw.Draw(l_armor)
    d_gold     = ImageDraw.Draw(l_gold)
    d_canopy   = ImageDraw.Draw(l_canopy)
    d_weapons  = ImageDraw.Draw(l_weapons)
    d_highlights = ImageDraw.Draw(l_highlights)

    # --- CASUAL MOBILE COLOR PALETTE ---
    # Outlines: Rich deep navy-violet (softer and juicier than harsh black)
    C_OUTLINE      = (20, 24, 48, 255)
    C_OUTLINE_SOFT = (38, 44, 76, 255)

    # Primary Body: Glossy Electric Azure / Cobalt
    C_BLUE_DARK    = (28, 54, 120, 255)
    C_BLUE_MID     = (42, 94, 210, 255)
    C_BLUE_BRIGHT  = (64, 138, 248, 255)
    C_BLUE_LIGHT   = (112, 178, 255, 255)

    # Secondary Body: Clean Glossy Pearl White
    C_WHITE_SHADOW = (168, 185, 215, 255)
    C_WHITE_MID    = (212, 226, 245, 255)
    C_WHITE_BRIGHT = (245, 250, 255, 255)
    C_SPECULAR     = (255, 255, 255, 255)

    # Metallic Gold / Honey Trims
    C_GOLD_DEEP    = (160, 95, 10, 255)
    C_GOLD_MID     = (225, 155, 20, 255)
    C_GOLD_BRIGHT  = (255, 205, 45, 255)
    C_GOLD_LIGHT   = (255, 238, 130, 255)

    # Cockpit Glass: Luminous Gem Turquoise / Mint
    C_CYAN_DEEP    = (10, 75, 95, 255)
    C_CYAN_MID     = (18, 150, 175, 255)
    C_CYAN_BRIGHT  = (40, 215, 235, 255)
    C_CYAN_GLOW    = (140, 250, 255, 255)

    # Cartoon Exhaust Plasma & Sparkles (Pink-Magenta to Electric Yellow/Cyan)
    C_FIRE_MAGENTA = (235, 45, 125, 240)
    C_FIRE_ORANGE  = (255, 130, 30, 255)
    C_FIRE_YELLOW  = (255, 225, 50, 255)
    C_FIRE_WHITE   = (255, 255, 255, 255)

    def sym_poly(draw, pts, fill, outline=None, width=1):
        full = list(pts)
        for x, y in reversed(pts):
            rx = cx - (x - cx)
            if rx != x:
                full.append((rx, y))
        draw.polygon(full, fill=fill, outline=outline, width=width)

    def sym_ellipse(draw, bbox, fill, outline=None, width=1):
        x1, y1, x2, y2 = bbox
        draw.ellipse([x1, y1, x2, y2], fill=fill, outline=outline, width=width)
        rx1 = cx - (x2 - cx)
        rx2 = cx - (x1 - cx)
        if rx1 != x1:
            draw.ellipse([rx1, y1, rx2, y2], fill=fill, outline=outline, width=width)

    def draw_star(draw, x, y, r, fill):
        # 4-point cartoon sparkle
        pts = [(x, y - r), (x + r*0.25, y - r*0.25), (x + r, y), (x + r*0.25, y + r*0.25),
               (x, y + r), (x - r*0.25, y + r*0.25), (x - r, y), (x - r*0.25, y - r*0.25)]
        draw.polygon(pts, fill=fill)

    # ==========================================
    # LAYER 1: CARTOON PLASMA PLUME & SPARKLES
    # ==========================================
    # Twin big rounded cartoon exhaust flames
    engines_x = [cx - 50, cx + 50]
    for ex in engines_x:
        ey = 370
        # Outer magenta puff
        d_plasma.ellipse([ex - 28, ey, ex + 28, ey + 75], fill=C_FIRE_MAGENTA)
        # Mid orange flame
        d_plasma.ellipse([ex - 20, ey, ex + 20, ey + 60], fill=C_FIRE_ORANGE)
        # Inner yellow core
        d_plasma.ellipse([ex - 12, ey, ex + 12, ey + 42], fill=C_FIRE_YELLOW)
        # Center white hot spot
        d_plasma.ellipse([ex - 6, ey, ex + 6, ey + 22], fill=C_FIRE_WHITE)
        # Floating bubbly exhaust drops
        d_plasma.ellipse([ex - 10, ey + 78, ex + 10, ey + 98], fill=C_FIRE_MAGENTA)
        d_plasma.ellipse([ex - 6, ey + 82, ex + 6, ey + 94], fill=C_FIRE_ORANGE)
        d_plasma.ellipse([ex - 5, ey + 104, ex + 5, ey + 114], fill=C_FIRE_YELLOW)

    # Cute floating star sparkles
    sparkles = [(cx - 75, 450, 7), (cx + 75, 450, 7), (cx, 440, 9), (cx - 110, 420, 5), (cx + 110, 420, 5), (cx, 475, 6)]
    for sx, sy, sr in sparkles:
        draw_star(d_plasma, sx, sy, sr, C_GOLD_BRIGHT)
        draw_star(d_plasma, sx, sy, sr*0.5, C_SPECULAR)

    # ==========================================
    # LAYER 2: CHUNKY ENGINE NOZZLES
    # ==========================================
    for ex in engines_x:
        # Outer nozzle rim
        d_thruster.rounded_rectangle([ex - 30, 350, ex + 30, 375], radius=8, fill=C_GOLD_DEEP, outline=C_OUTLINE, width=2)
        d_thruster.rounded_rectangle([ex - 28, 352, ex + 28, 370], radius=6, fill=C_GOLD_MID)
        # Nozzle interior opening
        d_thruster.ellipse([ex - 22, 362, ex + 22, 374], fill=C_FIRE_MAGENTA, outline=C_OUTLINE, width=2)
        d_thruster.ellipse([ex - 16, 364, ex + 16, 372], fill=C_FIRE_YELLOW)
        # Metallic cylinder upper body
        d_thruster.rounded_rectangle([ex - 24, 325, ex + 24, 355], radius=6, fill=C_WHITE_SHADOW, outline=C_OUTLINE, width=2)
        d_thruster.rounded_rectangle([ex - 21, 327, ex + 7, 353], radius=4, fill=C_WHITE_BRIGHT)

    # ==========================================
    # LAYER 3: WINGS & AERO SURFACES
    # ==========================================
    # Bold, rounded swept delta wings
    main_wings = [
        (cx, 160),
        (cx + 45, 195),
        (cx + 115, 230),
        (cx + 195, 280), # Wingtip leading edge
        (cx + 205, 305), # Rounded wingtip apex
        (cx + 185, 335), # Wingtip trailing edge
        (cx + 135, 340), # Flap junction
        (cx + 95, 355),  # Engine bay corner
        (cx + 40, 360),
        (cx, 365)
    ]
    # Drop shadow under wings
    sym_poly(d_wings, main_wings, fill=C_BLUE_DARK, outline=C_OUTLINE, width=3)
    # Wing midtone base
    sym_poly(d_wings, [(x, y - 4) for x, y in main_wings], fill=C_BLUE_MID)
    # Wing top highlight area
    sym_poly(d_wings, [
        (cx + 45, 198),
        (cx + 110, 232),
        (cx + 180, 282),
        (cx + 182, 305),
        (cx + 120, 315),
        (cx + 50, 280)
    ], fill=C_BLUE_BRIGHT)

    # Wingtip Cute Energy Orb Pods
    for s in (-1, 1):
        ox = cx + s * 195
        oy = 300
        # Golden mounting bracket
        d_wings.rounded_rectangle([ox - 14, oy - 18, ox + 14, oy + 18], radius=6, fill=C_GOLD_MID, outline=C_OUTLINE, width=2)
        # Glowing Orb
        d_wings.ellipse([ox - 10, oy - 10, ox + 10, oy + 10], fill=C_CYAN_MID, outline=C_OUTLINE, width=2)
        d_wings.ellipse([ox - 7, oy - 7, ox + 7, oy + 7], fill=C_CYAN_BRIGHT)
        d_wings.ellipse([ox - 4, oy - 5, ox + 1, oy], fill=C_SPECULAR)

    # ==========================================
    # LAYER 4: GLOSSY CHASSIS & PEARL HULL
    # ==========================================
    # Sleek, rounded central fuselage (Aerodynamic, chunky, friendly teardrop)
    fuse_body = [
        (cx, 48),        # Rounded nose tip
        (cx + 20, 75),   # Nose flare
        (cx + 38, 125),  # Forward cheek
        (cx + 56, 200),  # Mid cabin
        (cx + 62, 285),  # Flank
        (cx + 50, 350),  # Taper to engines
        (cx + 28, 368),
        (cx, 372)
    ]
    # Outer dark outline / shadow
    sym_poly(d_armor, fuse_body, fill=C_WHITE_SHADOW, outline=C_OUTLINE, width=3)
    # Glossy pearl white main body
    sym_poly(d_armor, [(x, y - 3) for x, y in fuse_body], fill=C_WHITE_MID)
    # Pearl white top surface
    fuse_top = [
        (cx, 55),
        (cx + 14, 80),
        (cx + 28, 130),
        (cx + 42, 205),
        (cx + 45, 285),
        (cx + 34, 340),
        (cx, 355)
    ]
    sym_poly(d_armor, fuse_top, fill=C_WHITE_BRIGHT)

    # Front Nose Cone Cap: Glossy Electric Blue
    nose_cap = [
        (cx, 52),
        (cx + 12, 70),
        (cx + 18, 95),
        (cx + 12, 105),
        (cx, 108)
    ]
    sym_poly(d_armor, nose_cap, fill=C_BLUE_MID, outline=C_OUTLINE, width=2)
    sym_poly(d_armor, [(cx, 56), (cx + 9, 72), (cx + 12, 92), (cx, 98)], fill=C_BLUE_BRIGHT)
    # Cute white nose reflection spot
    d_armor.ellipse([cx - 4, 60, cx + 4, 75], fill=C_SPECULAR)

    # ==========================================
    # LAYER 5: GOLDEN TRIMS & RACING CHEVRONS
    # ==========================================
    # Golden Trim border along the nose-to-wing flank
    gold_border = [
        (cx + 22, 110),
        (cx + 35, 145),
        (cx + 48, 195),
        (cx + 42, 200),
        (cx + 30, 150),
        (cx + 18, 115)
    ]
    sym_poly(d_gold, gold_border, fill=C_GOLD_MID, outline=C_OUTLINE, width=1)
    sym_poly(d_gold, [(x, y - 2) for x, y in gold_border], fill=C_GOLD_BRIGHT)

    # Bold Gold Racing Chevrons on wings
    for s in (-1, 1):
        # Wing chevron band
        ch_pts = [
            (cx + s*85, 235),
            (cx + s*130, 265),
            (cx + s*122, 276),
            (cx + s*77, 246)
        ]
        d_gold.polygon(ch_pts, fill=C_GOLD_MID, outline=C_OUTLINE, width=2)
        d_gold.polygon([(x, y - 2) for x, y in ch_pts], fill=C_GOLD_BRIGHT)
        # Second thinner accent stripe
        ch2_pts = [
            (cx + s*92, 222),
            (cx + s*132, 248),
            (cx + s*127, 254),
            (cx + s*87, 228)
        ]
        d_gold.polygon(ch2_pts, fill=C_GOLD_LIGHT)

    # Faction Emblem on Rear Deck: Golden Winged Star (Y: 310 to 335)
    draw_star(d_gold, cx, 320, 14, C_GOLD_BRIGHT)
    draw_star(d_gold, cx, 320, 8, C_GOLD_LIGHT)
    draw_star(d_gold, cx, 320, 4, C_SPECULAR)

    # ==========================================
    # LAYER 6: GEM BUBBLE COCKPIT CANOPY
    # ==========================================
    # Big, friendly, expressive gemstone bubble canopy (Y: 120 to 220)
    # Outer dark bezel
    d_canopy.ellipse([cx - 36, 120, cx + 36, 225], fill=C_BLUE_DARK, outline=C_OUTLINE, width=3)
    # Deep jewel cyan base
    d_canopy.ellipse([cx - 32, 124, cx + 32, 220], fill=C_CYAN_DEEP)
    # Glowing turquoise midtone
    d_canopy.ellipse([cx - 28, 128, cx + 28, 214], fill=C_CYAN_MID)
    # Bright luminous bottom glow
    d_canopy.ellipse([cx - 22, 155, cx + 22, 210], fill=C_CYAN_BRIGHT)
    d_canopy.ellipse([cx - 15, 175, cx + 15, 206], fill=C_CYAN_GLOW)

    # Curved Glass Specular Highlight (The signature "mobile game glossy gem" look)
    # Big primary shine arc on top-left of visor
    d_canopy.ellipse([cx - 24, 130, cx - 4, 175], fill=C_SPECULAR)
    # Little secondary bounce light dot on bottom-right
    d_canopy.ellipse([cx + 12, 185, cx + 18, 195], fill=C_CYAN_GLOW)

    # ==========================================
    # LAYER 7: CUTE ROUNDED ENERGY BLASTERS
    # ==========================================
    # Twin chunky energy blasters mounted under wing roots (X: cx +/- 65)
    for s in (-1, 1):
        bx = cx + s * 65
        by = 190
        # Rounded blaster housing
        d_weapons.rounded_rectangle([bx - 12, by, bx + 12, by + 65], radius=6, fill=C_BLUE_MID, outline=C_OUTLINE, width=2)
        d_weapons.rounded_rectangle([bx - 9, by + 2, bx + 9, by + 62], radius=4, fill=C_BLUE_BRIGHT)
        # Gold collar ring
        d_weapons.rounded_rectangle([bx - 14, by + 18, bx + 14, by + 28], radius=3, fill=C_GOLD_MID, outline=C_OUTLINE, width=1)
        d_weapons.rounded_rectangle([bx - 12, by + 20, bx + 12, by + 26], radius=2, fill=C_GOLD_BRIGHT)
        # Blaster barrel muzzle extending forward
        d_weapons.rounded_rectangle([bx - 7, by - 22, bx + 7, by + 2], radius=4, fill=C_WHITE_MID, outline=C_OUTLINE, width=2)
        d_weapons.rounded_rectangle([bx - 5, by - 20, bx + 2, by], radius=3, fill=C_WHITE_BRIGHT)
        # Glowing cyan energy charge lens
        d_weapons.ellipse([bx - 5, by - 26, bx + 5, by - 16], fill=C_CYAN_BRIGHT, outline=C_OUTLINE, width=1)
        d_weapons.ellipse([bx - 3, by - 24, bx + 3, by - 18], fill=C_CYAN_GLOW)
        d_weapons.point([(bx, by - 21)], fill=C_SPECULAR)

    # ==========================================
    # LAYER 8: CRISP OUTLINES & GLOSS HIGHLIGHTS
    # ==========================================
    # Glossy light streak along left edge of pearl fuselage
    d_highlights.line([(cx - 15, 85), (cx - 28, 135)], fill=C_SPECULAR, width=2)
    d_highlights.line([(cx - 32, 145), (cx - 44, 215)], fill=C_SPECULAR, width=2)
    d_highlights.line([(cx - 46, 230), (cx - 48, 290)], fill=C_SPECULAR, width=2)

    # Wing leading edge glossy highlight
    for s in (-1, 1):
        d_highlights.line([(cx + s*50, 195), (cx + s*120, 235)], fill=C_SPECULAR, width=2)
        d_highlights.line([(cx + s*125, 238), (cx + s*190, 280)], fill=C_BLUE_LIGHT, width=2)

    # Extra sparkle on nose tip
    draw_star(d_highlights, cx - 2, 54, 6, C_SPECULAR)
    draw_star(d_highlights, cx + 120, 240, 5, C_SPECULAR)

    layers = [
        ("Plasma Flames & Sparkles", l_plasma),
        ("Chunky Engine Nozzles", l_thruster),
        ("Wings & Orb Pods", l_wings),
        ("Pearl White & Azure Body", l_armor),
        ("Golden Trims & Chevrons", l_gold),
        ("Gemstone Bubble Cockpit", l_canopy),
        ("Energy Blasters", l_weapons),
        ("Gloss Highlights & Outlines", l_highlights)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_casual_spaceship()
    composite.save('/tmp/casual_spaceship.png')
    print("Casual Mobile Spaceship successfully rendered to /tmp/casual_spaceship.png")
