#!/usr/bin/env python3
"""
Master Pixel Art Character for 128x128 Canvas:
"Pip the Red Panda Knight" - Professional game character with 8 discrete layers.
Deliberate, pristine pixel art with perfect clustering, grounding, and iconic red panda silhouette.
"""

from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

def draw_pip():
    w, h = 128, 128

    # 8 Discrete Layers
    l_shadow     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_tail       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_cloak      = Image.new('RGBA', (w, h), (0,0,0,0))
    l_head       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_face       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_gear       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_gold       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_outlines   = Image.new('RGBA', (w, h), (0,0,0,0))

    d_shadow     = ImageDraw.Draw(l_shadow)
    d_tail       = ImageDraw.Draw(l_tail)
    d_cloak      = ImageDraw.Draw(l_cloak)
    d_head       = ImageDraw.Draw(l_head)
    d_face       = ImageDraw.Draw(l_face)
    d_gear       = ImageDraw.Draw(l_gear)
    d_gold       = ImageDraw.Draw(l_gold)
    d_outlines   = ImageDraw.Draw(l_outlines)

    # --- PALETTE DEFINITION ---
    # Ink & Linework
    INK_DARK       = (28, 18, 22, 255)
    INK_MID        = (46, 30, 34, 255)

    # Fur: Russet Red Panda
    FUR_DARK       = (140, 44, 24, 255)
    FUR_MID        = (206, 76, 32, 255)
    FUR_BRIGHT     = (242, 112, 46, 255)
    FUR_LIGHT      = (255, 156, 88, 255)

    # Cream Fur / Muzzle / Cheek Tufts
    CREAM_DARK     = (182, 172, 164, 255)
    CREAM_MID      = (232, 224, 214, 255)
    CREAM_LIGHT    = (254, 250, 244, 255)
    WHITE_PURE     = (255, 255, 255, 255)

    # Dark Chocolate Paws & Ear Rims
    CHOC_DARK      = (34, 22, 22, 255)
    CHOC_MID       = (60, 42, 40, 255)
    CHOC_LIGHT     = (88, 64, 60, 255)

    # Forest Cloak
    CAPE_DARK      = (18, 44, 32, 255)
    CAPE_MID       = (32, 80, 54, 255)
    CAPE_BRIGHT    = (50, 130, 84, 255)
    CAPE_LIGHT     = (88, 174, 114, 255)

    # Gold & Brass
    GOLD_DARK      = (155, 90, 18, 255)
    GOLD_MID       = (220, 158, 28, 255)
    GOLD_BRIGHT    = (255, 210, 52, 255)

    # Magic Star Gem (Cyan / Aquamarine)
    GEM_GLOW       = (78, 235, 255, 55)
    GEM_DARK       = (14, 86, 112, 255)
    GEM_MID        = (28, 172, 214, 255)
    GEM_BRIGHT     = (78, 235, 255, 255)

    # Acorn Shell & Wood
    WOOD_DARK      = (58, 34, 22, 255)
    WOOD_MID       = (110, 68, 42, 255)
    WOOD_LIGHT     = (158, 102, 64, 255)

    # Blush
    BLUSH          = (248, 116, 120, 190)

    def draw_star(draw, x, y, r, fill):
        pts = [(x, y - r), (x + r*0.3, y - r*0.3), (x + r, y), (x + r*0.3, y + r*0.3),
               (x, y + r), (x - r*0.3, y + r*0.3), (x - r, y), (x - r*0.3, y - r*0.3)]
        draw.polygon(pts, fill=fill)

    # ==========================================
    # LAYER 1: SHADOW & GROUND BASE
    # ==========================================
    # Ground contact shadow directly beneath boots
    d_shadow.ellipse([38, 101, 90, 113], fill=(22, 16, 26, 95))
    d_shadow.ellipse([44, 103, 84, 111], fill=(16, 10, 20, 160))
    d_shadow.ellipse([47, 104, 81, 109], fill=(10, 6, 14, 220))

    # Cute clustered grass blades & moss pebbles
    # Left grass clump
    d_shadow.polygon([(35, 106), (33, 99), (36, 102)], fill=CAPE_BRIGHT)
    d_shadow.polygon([(37, 107), (38, 98), (40, 102)], fill=CAPE_LIGHT)
    d_shadow.point([(36, 100)], fill=WHITE_PURE)

    # Right grass clump & tiny flower
    d_shadow.polygon([(88, 106), (90, 99), (92, 103)], fill=CAPE_LIGHT)
    d_shadow.polygon([(92, 107), (95, 100), (96, 104)], fill=CAPE_BRIGHT)
    # Tiny white daisy
    d_shadow.point([(94, 98)], fill=WHITE_PURE)
    d_shadow.point([(94, 99)], fill=GOLD_BRIGHT)

    # ==========================================
    # LAYER 2: FLUFFY RINGED TAIL
    # ==========================================
    tail_hull = [
        (76, 90),
        (84, 98),
        (98, 100),
        (108, 92),
        (112, 78),
        (108, 64),
        (98, 54),   # Tip
        (86, 56),
        (80, 66),
        (86, 76),
        (92, 82),
        (86, 88),
        (76, 86)
    ]
    d_tail.polygon(tail_hull, fill=FUR_DARK, outline=INK_DARK, width=1)
    d_tail.polygon([(x - 1, y - 1) for x, y in tail_hull], fill=FUR_MID)
    d_tail.polygon([(x - 2, y - 2) for x, y in tail_hull[:7]], fill=FUR_BRIGHT)

    # Tail rings (alternating dark chocolate and russet)
    # Ring 1
    d_tail.polygon([(84, 84), (94, 81), (99, 89), (88, 92)], fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_tail.polygon([(86, 85), (93, 83), (97, 88), (89, 90)], fill=CHOC_MID)
    # Ring 2
    d_tail.polygon([(88, 70), (99, 68), (104, 76), (93, 78)], fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_tail.polygon([(90, 71), (98, 70), (102, 75), (94, 77)], fill=CHOC_MID)
    # Fluffy cream tail tip
    d_tail.polygon([(98, 54), (108, 64), (102, 70), (92, 62), (86, 56)], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_tail.polygon([(97, 56), (105, 63), (100, 67), (91, 61), (88, 57)], fill=CREAM_MID)
    d_tail.polygon([(98, 56), (102, 60), (96, 62), (90, 58)], fill=CREAM_LIGHT)

    # ==========================================
    # LAYER 3: FOREST CLOAK & BODY
    # ==========================================
    # Chubby dark chocolate boots firmly planted on shadow
    # Left foot
    d_cloak.rounded_rectangle([47, 98, 59, 107], radius=3, fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_cloak.rounded_rectangle([49, 99, 57, 104], radius=2, fill=CHOC_MID)
    d_cloak.point([(51, 100), (52, 100)], fill=CHOC_LIGHT)
    # Right foot
    d_cloak.rounded_rectangle([69, 98, 81, 107], radius=3, fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_cloak.rounded_rectangle([71, 99, 79, 104], radius=2, fill=CHOC_MID)
    d_cloak.point([(73, 100), (74, 100)], fill=CHOC_LIGHT)

    # Forest Green Traveler's Cloak with natural drapery
    cape_pts = [
        (54, 68),   # Collar L
        (42, 80),   # Shoulder L
        (39, 95),   # Lower flare L
        (45, 99),
        (54, 97),   # Hem scallop
        (64, 100),  # Hem center
        (74, 97),   # Hem scallop
        (83, 99),
        (89, 95),   # Lower flare R
        (86, 80),   # Shoulder R
        (74, 68)    # Collar R
    ]
    d_cloak.polygon(cape_pts, fill=CAPE_DARK, outline=INK_DARK, width=2)
    d_cloak.polygon([(x, y - 1) for x, y in cape_pts], fill=CAPE_MID)

    # Cloak highlights on shoulder folds
    d_cloak.polygon([(54, 70), (45, 82), (43, 93), (49, 95), (51, 80), (58, 72)], fill=CAPE_BRIGHT)
    d_cloak.polygon([(46, 83), (45, 91), (48, 93), (50, 83)], fill=CAPE_LIGHT)

    d_cloak.polygon([(74, 70), (83, 82), (85, 93), (79, 95), (77, 80), (70, 72)], fill=CAPE_BRIGHT)
    d_cloak.polygon([(82, 83), (83, 91), (80, 93), (78, 83)], fill=CAPE_LIGHT)

    # Tunic center opening with leather tunic & golden belt
    d_cloak.rectangle([58, 75, 70, 95], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_cloak.rectangle([59, 76, 69, 94], fill=CREAM_MID)
    # Sturdy leather belt across waist
    d_cloak.rectangle([57, 85, 71, 89], fill=WOOD_DARK, outline=INK_DARK, width=1)
    d_cloak.rectangle([58, 86, 70, 88], fill=WOOD_MID)
    # Golden belt buckle
    d_cloak.rectangle([61, 84, 67, 90], fill=GOLD_DARK, outline=INK_DARK, width=1)
    d_cloak.rectangle([62, 85, 66, 89], fill=GOLD_BRIGHT)
    d_cloak.point([(64, 87)], fill=INK_DARK) # Belt prong

    # ==========================================
    # LAYER 4: HEAD, FLUFFY EARS & FUR
    # ==========================================
    # Oversized rounded ears with chocolate rims & fluffy cream tufts
    # Left Ear
    d_head.rounded_rectangle([29, 19, 51, 41], radius=8, fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_head.rounded_rectangle([31, 21, 49, 39], radius=7, fill=FUR_DARK)
    d_head.ellipse([33, 24, 47, 37], fill=CREAM_DARK)
    d_head.ellipse([35, 26, 45, 35], fill=CREAM_MID)
    d_head.ellipse([37, 28, 43, 33], fill=CREAM_LIGHT)

    # Right Ear
    d_head.rounded_rectangle([77, 19, 99, 41], radius=8, fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_head.rounded_rectangle([79, 21, 97, 39], radius=7, fill=FUR_DARK)
    d_head.ellipse([81, 24, 95, 37], fill=CREAM_DARK)
    d_head.ellipse([83, 26, 93, 35], fill=CREAM_MID)
    d_head.ellipse([85, 28, 91, 33], fill=CREAM_LIGHT)

    # Chubby adorable head shape
    head_hull = [
        (48, 25),
        (64, 23),
        (80, 25),
        (88, 34),
        (93, 47),
        (95, 59),
        (88, 68),
        (76, 73),
        (64, 74),
        (52, 73),
        (40, 68),
        (33, 59),
        (35, 47),
        (40, 34)
    ]
    d_head.polygon(head_hull, fill=FUR_DARK, outline=INK_DARK, width=2)
    d_head.polygon([(x, y - 1) for x, y in head_hull], fill=FUR_MID)
    d_head.polygon([(x, y - 2) for x, y in head_hull[:5]], fill=FUR_BRIGHT)
    d_head.ellipse([52, 26, 76, 40], fill=FUR_LIGHT)

    # Characteristic Red Panda White Markings with fluffy cheek tufts!
    # Left cheek patch
    d_head.ellipse([34, 49, 50, 67], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_head.ellipse([36, 51, 48, 65], fill=CREAM_MID)
    d_head.ellipse([38, 53, 46, 62], fill=CREAM_LIGHT)
    # Fluffy cheek tuft sticking out left
    d_head.polygon([(34, 58), (30, 60), (33, 63)], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_head.polygon([(34, 59), (31, 60), (33, 62)], fill=CREAM_LIGHT)

    # Right cheek patch
    d_head.ellipse([78, 49, 94, 67], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_head.ellipse([80, 51, 92, 65], fill=CREAM_MID)
    d_head.ellipse([82, 53, 90, 62], fill=CREAM_LIGHT)
    # Fluffy cheek tuft sticking out right
    d_head.polygon([(94, 58), (98, 60), (95, 63)], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_head.polygon([(94, 59), (97, 60), (95, 62)], fill=CREAM_LIGHT)

    # Snout / Muzzle oval
    d_head.ellipse([53, 51, 75, 71], fill=CREAM_DARK, outline=INK_DARK, width=1)
    d_head.ellipse([55, 53, 73, 69], fill=CREAM_MID)
    d_head.ellipse([57, 55, 71, 66], fill=CREAM_LIGHT)

    # Eyebrow tear-drop marks
    d_head.ellipse([46, 35, 54, 41], fill=CREAM_MID, outline=INK_DARK, width=1)
    d_head.ellipse([47, 36, 53, 40], fill=CREAM_LIGHT)
    d_head.ellipse([74, 35, 82, 41], fill=CREAM_MID, outline=INK_DARK, width=1)
    d_head.ellipse([75, 36, 81, 40], fill=CREAM_LIGHT)

    # ==========================================
    # LAYER 5: EXPRESSIVE SOULFUL EYES & FACE
    # ==========================================
    # Rosy blush
    d_face.ellipse([38, 57, 47, 64], fill=BLUSH)
    d_face.ellipse([81, 57, 90, 64], fill=BLUSH)

    # Left eye: Big sparkling anime iris
    d_face.rounded_rectangle([47, 43, 57, 55], radius=4, fill=INK_DARK, outline=INK_DARK, width=1)
    d_face.ellipse([48, 47, 56, 54], fill=FUR_DARK)
    d_face.ellipse([50, 49, 54, 53], fill=FUR_BRIGHT)
    d_face.ellipse([49, 44, 53, 48], fill=WHITE_PURE) # Main glint
    d_face.point([(54, 51)], fill=WHITE_PURE)        # Sub glint

    # Right eye
    d_face.rounded_rectangle([71, 43, 81, 55], radius=4, fill=INK_DARK, outline=INK_DARK, width=1)
    d_face.ellipse([72, 47, 80, 54], fill=FUR_DARK)
    d_face.ellipse([74, 49, 78, 53], fill=FUR_BRIGHT)
    d_face.ellipse([73, 44, 77, 48], fill=WHITE_PURE) # Main glint
    d_face.point([(78, 51)], fill=WHITE_PURE)        # Sub glint

    # Cute shiny nose
    d_face.polygon([(62, 57), (66, 57), (64, 60)], fill=INK_DARK)
    d_face.point([(63, 57)], fill=WHITE_PURE)

    # Smiling mouth :3
    d_face.line([(64, 60), (64, 63)], fill=INK_DARK, width=1)
    d_face.line([(64, 63), (61, 65), (59, 64)], fill=INK_DARK, width=1)
    d_face.line([(64, 63), (67, 65), (69, 64)], fill=INK_DARK, width=1)

    # ==========================================
    # LAYER 6: HERO EQUIPMENT (WAND & SHIELD)
    # ==========================================
    # 1. STAR WAND (Viewer's Left, X: 24 to 42, Y: 55 to 92)
    # Wand staff angled cleanly
    wand_pts = [(25, 92), (38, 66)]
    d_gear.line(wand_pts, fill=WOOD_DARK, width=3)
    d_gear.line([(26, 91), (39, 65)], fill=WOOD_MID, width=2)
    d_gear.line([(27, 90), (40, 64)], fill=WOOD_LIGHT, width=1)

    # Soft radial glow aura behind star gem
    d_gear.ellipse([30, 52, 48, 70], fill=GEM_GLOW)

    # Golden socket prongs holding the crystal
    d_gear.ellipse([34, 60, 44, 70], fill=GOLD_DARK, outline=INK_DARK, width=1)
    d_gear.ellipse([36, 62, 42, 68], fill=GOLD_MID)

    # Glowing Cyan Star Crystal
    d_gear.ellipse([33, 55, 45, 67], fill=GEM_DARK, outline=INK_DARK, width=1)
    d_gear.ellipse([35, 57, 43, 65], fill=GEM_MID)
    draw_star(d_gear, 39, 61, 5, GEM_BRIGHT)
    draw_star(d_gear, 39, 61, 2, WHITE_PURE)

    # Chubby chocolate paw gripping the staff
    d_gear.ellipse([32, 74, 42, 83], fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_gear.ellipse([34, 75, 40, 81], fill=CHOC_MID)
    d_gear.point([(35, 77), (37, 76), (39, 77)], fill=CHOC_LIGHT) # 3 cute little paw fingers!

    # 2. ACORN KNIGHT SHIELD (Viewer's Right, X: 84 to 104, Y: 68 to 96)
    # Acorn body
    acorn_pts = [
        (86, 76),
        (96, 76),
        (102, 82),
        (102, 88),
        (94, 96),  # Bottom tip
        (86, 88),
        (84, 82)
    ]
    d_gear.polygon(acorn_pts, fill=WOOD_DARK, outline=INK_DARK, width=1)
    d_gear.polygon([(x, y - 1) for x, y in acorn_pts], fill=WOOD_MID)
    d_gear.polygon([(88, 78), (96, 78), (100, 82), (94, 92), (88, 84)], fill=WOOD_LIGHT)

    # Golden Oak Leaf emblem on shield
    d_gear.polygon([(91, 84), (94, 81), (97, 84), (94, 90)], fill=GOLD_BRIGHT, outline=GOLD_DARK, width=1)
    d_gear.point([(94, 85)], fill=WHITE_PURE)

    # Acorn textured cap with cross-hatch texture
    d_gear.rounded_rectangle([83, 70, 105, 78], radius=3, fill=GOLD_DARK, outline=INK_DARK, width=1)
    d_gear.rounded_rectangle([85, 71, 103, 76], radius=2, fill=GOLD_MID)
    # Acorn stem
    d_gear.line([(94, 70), (94, 66)], fill=WOOD_DARK, width=2)
    d_gear.point([(94, 66)], fill=WOOD_LIGHT)

    # Cap cross-hatch dots
    for dot_x in [87, 91, 95, 99, 101]:
        d_gear.point([(dot_x, 73)], fill=GOLD_BRIGHT)
        d_gear.point([(dot_x + 2, 75)], fill=GOLD_DARK)

    # Chubby chocolate paw gripping shield side
    d_gear.ellipse([80, 78, 88, 86], fill=CHOC_DARK, outline=INK_DARK, width=1)
    d_gear.ellipse([81, 79, 87, 85], fill=CHOC_MID)
    d_gear.point([(85, 80), (86, 82), (86, 84)], fill=CHOC_LIGHT) # 3 paw digits gripping rim

    # ==========================================
    # LAYER 7: GOLDEN BROOCH & SATCHEL STRAP
    # ==========================================
    # Satchel leather strap running diagonal from shoulder under cloak collar
    d_gold.line([(46, 72), (58, 85)], fill=WOOD_DARK, width=3)
    d_gold.line([(47, 72), (59, 85)], fill=WOOD_MID, width=2)
    d_gold.line([(48, 72), (60, 85)], fill=WOOD_LIGHT, width=1)

    # Golden Leaf Cloak Brooch clasp at neck center (X: 64, Y: 68)
    d_gold.ellipse([60, 65, 68, 73], fill=GOLD_DARK, outline=INK_DARK, width=1)
    d_gold.ellipse([61, 66, 67, 72], fill=GOLD_MID)
    d_gold.ellipse([62, 67, 66, 71], fill=GOLD_BRIGHT)
    d_gold.point([(63, 68)], fill=WHITE_PURE) # Brooch gleam!

    # ==========================================
    # LAYER 8: CRISP OUTLINES & SPECULAR LIGHT
    # ==========================================
    # Specular rim lights
    # Crown shine
    d_outlines.line([(58, 24), (70, 24)], fill=FUR_LIGHT, width=1)
    d_outlines.point([(64, 23)], fill=WHITE_PURE)
    # Ear tips
    d_outlines.line([(36, 20), (44, 20)], fill=CHOC_LIGHT, width=1)
    d_outlines.line([(84, 20), (92, 20)], fill=CHOC_LIGHT, width=1)
    # Cloak edge highlights
    d_outlines.line([(42, 85), (40, 94)], fill=CAPE_LIGHT, width=1)
    d_outlines.line([(86, 85), (88, 94)], fill=CAPE_LIGHT, width=1)

    # Floating magical sparkle motes near the star wand
    draw_star(d_outlines, 27, 53, 3, GEM_BRIGHT)
    draw_star(d_outlines, 27, 53, 1, WHITE_PURE)

    draw_star(d_outlines, 49, 53, 2, GEM_BRIGHT)
    d_outlines.point([(49, 53)], fill=WHITE_PURE)

    d_outlines.point([(23, 63), (31, 47), (43, 45)], fill=WHITE_PURE)

    layers = [
        ("Ground Shadow", l_shadow),
        ("Fluffy Ringed Tail", l_tail),
        ("Forest Cloak & Boots", l_cloak),
        ("Head & Fluffy Ears", l_head),
        ("Expressive Eyes & Face", l_face),
        ("Wand & Acorn Shield", l_gear),
        ("Golden Brooch & Satchel", l_gold),
        ("Outlines & Magic Sparkles", l_outlines)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_pip()
    out_path = Path("/tmp/pip_red_panda_128.png")
    composite.save(out_path)
    print(f"Pip the Red Panda successfully rendered to {out_path}")
