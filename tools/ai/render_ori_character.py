#!/usr/bin/env python3
"""
Masterpiece Ori-Inspired Spirit Character Pixel Art (500x500 Canvas)
Organic, smooth, ethereal spirit guardian perched on an ancient mossy branch.
Uses Bezier splines and rounded geometry to achieve Moon Studios' signature fluid aesthetic.
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np

def cubic_bezier(p0, p1, p2, p3, n=30):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3*u**2 * t * p1[0] + 3*u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3*u**2 * t * p1[1] + 3*u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((int(round(x)), int(round(y))))
    return pts

def draw_ori():
    w, h = 500, 500

    # 8 Discrete Layers
    l_aura       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_wisps      = Image.new('RGBA', (w, h), (0,0,0,0))
    l_branch     = Image.new('RGBA', (w, h), (0,0,0,0))
    l_tail       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_body       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_head       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_eyes       = Image.new('RGBA', (w, h), (0,0,0,0))
    l_highlights = Image.new('RGBA', (w, h), (0,0,0,0))

    d_aura       = ImageDraw.Draw(l_aura)
    d_wisps      = ImageDraw.Draw(l_wisps)
    d_branch     = ImageDraw.Draw(l_branch)
    d_tail       = ImageDraw.Draw(l_tail)
    d_body       = ImageDraw.Draw(l_body)
    d_head       = ImageDraw.Draw(l_head)
    d_eyes       = ImageDraw.Draw(l_eyes)
    d_highlights = ImageDraw.Draw(l_highlights)

    # Palette
    C_WHITE_PURE   = (255, 255, 255, 255)
    C_CYAN_HOT     = (225, 252, 255, 255)
    C_CYAN_MINT    = (175, 245, 245, 255)
    C_CYAN_MID     = (95, 210, 235, 255)
    C_CYAN_DEEP    = (45, 160, 215, 255)
    C_TWILIGHT_BLUE= (28, 85, 160, 255)
    C_TWILIGHT_DARK= (16, 42, 90, 255)
    C_SHADOW_NAVY  = (10, 18, 45, 255)

    C_WOOD_DARK    = (14, 18, 30, 255)
    C_WOOD_MID     = (26, 34, 52, 255)
    C_WOOD_LIGHT   = (42, 54, 80, 255)
    C_MOSS_DEEP    = (12, 60, 70, 255)
    C_MOSS_TEAL    = (20, 135, 140, 255)
    C_MOSS_GLOW    = (45, 220, 200, 255)
    C_MOSS_BRIGHT  = (140, 255, 225, 255)

    def draw_star(draw, x, y, r, fill):
        pts = [(x, y - r), (x + r*0.22, y - r*0.22), (x + r, y), (x + r*0.22, y + r*0.22),
               (x, y + r), (x - r*0.22, y + r*0.22), (x - r, y), (x - r*0.22, y - r*0.22)]
        draw.polygon(pts, fill=fill)

    # ==========================================
    # LAYER 1: AMBIENT CELESTIAL SPIRIT AURA
    # ==========================================
    ox, oy = 250, 235
    for rad, col in [
        (190, (25, 20, 80, 25)),
        (155, (25, 90, 160, 40)),
        (120, (35, 155, 210, 55)),
        (85,  (75, 210, 235, 75)),
        (55,  (135, 240, 245, 95)),
        (30,  (195, 255, 255, 125))
    ]:
        d_aura.ellipse([ox - rad, oy - rad, ox + rad, oy + rad], fill=col)

    d_aura.ellipse([100, 360, 400, 460], fill=(18, 135, 155, 35))

    # ==========================================
    # LAYER 2: SPIRIT WISPS & STARDUST
    # ==========================================
    motes = [
        (115, 130, 6, C_CYAN_MINT),
        (135, 190, 4, C_CYAN_HOT),
        (85,  270, 7, C_CYAN_MID),
        (125, 335, 5, C_WHITE_PURE),
        (385, 110, 6, C_CYAN_MINT),
        (360, 175, 4, C_WHITE_PURE),
        (425, 230, 8, C_CYAN_MID),
        (395, 300, 5, C_CYAN_HOT),
        (345, 380, 6, C_MOSS_BRIGHT),
        (215, 95,  5, C_WHITE_PURE),
        (295, 70,  7, C_CYAN_MINT),
        (180, 410, 4, C_MOSS_BRIGHT),
        (300, 420, 5, C_MOSS_GLOW)
    ]
    for mx, my, mr, mc in motes:
        d_wisps.ellipse([mx - mr*1.8, my - mr*1.8, mx + mr*1.8, my + mr*1.8], fill=(mc[0], mc[1], mc[2], 40))
        d_wisps.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=mc)
        d_wisps.ellipse([mx - mr*0.4, my - mr*0.4, mx + mr*0.4, my + mr*0.4], fill=C_WHITE_PURE)

    sparkles = [(115, 115, 7), (405, 135, 8), (365, 265, 6), (75, 235, 8), (250, 50, 8)]
    for sx, sy, sr in sparkles:
        draw_star(d_wisps, sx, sy, sr, C_CYAN_MINT)
        draw_star(d_wisps, sx, sy, sr*0.4, C_WHITE_PURE)

    # ==========================================
    # LAYER 3: ANCIENT MOSSY BRANCH & FLORA
    # ==========================================
    # Smooth gnarled branch outline using Bezier curves
    b_top = cubic_bezier((20, 460), (140, 390), (280, 370), (480, 445), n=50)
    b_bot = cubic_bezier((480, 490), (320, 455), (180, 465), (20, 500), n=50)
    branch_poly = b_top + b_bot
    d_branch.polygon(branch_poly, fill=C_WOOD_DARK, outline=C_SHADOW_NAVY, width=2)

    # Bark rings
    for bx in range(90, 430, 20):
        by = int(380 + ((bx - 260)**2)*0.0012)
        d_branch.line([(bx, by + 12), (bx + 14, by + 45)], fill=C_WOOD_MID, width=2)

    # Smooth lush moss cap
    m_top = cubic_bezier((80, 425), (180, 375), (300, 370), (430, 430), n=40)
    m_bot = cubic_bezier((420, 442), (300, 388), (180, 392), (85, 438), n=40)
    moss_poly = m_top + m_bot
    d_branch.polygon(moss_poly, fill=C_MOSS_DEEP)
    d_branch.polygon([(x, y - 2) for x, y in moss_poly], fill=C_MOSS_TEAL)

    # Glowing moss line
    for p in m_top:
        d_branch.point([(p[0], p[1] - 1)], fill=C_MOSS_GLOW)
        if p[0] % 6 == 0:
            d_branch.point([(p[0], p[1] - 2)], fill=C_MOSS_BRIGHT)

    # Hanging moss vines
    vines = [(135, 420, 28), (175, 428, 38), (285, 418, 32), (335, 415, 22), (370, 430, 30)]
    for vx, vy, vl in vines:
        for seg in range(vl):
            px = int(vx + math.sin(seg*0.22)*5)
            py = vy + seg
            col = C_MOSS_GLOW if seg % 4 == 0 else C_MOSS_TEAL
            d_branch.point([(px, py)], fill=col)
        d_branch.ellipse([px - 2, py - 2, px + 2, py + 2], fill=C_MOSS_BRIGHT)

    # Glowing mushrooms
    mushrooms = [
        (125, 410, 5, 10), (145, 420, 4, 8), (165, 400, 6, 12),
        (350, 395, 5, 9),  (375, 408, 6, 13), (395, 422, 4, 8)
    ]
    for msx, msy, mr, mh in mushrooms:
        d_branch.line([(msx, msy), (msx, msy - mh)], fill=C_CYAN_MINT, width=2)
        d_branch.ellipse([msx - mr, msy - mh - mr*0.8, msx + mr, msy - mh + mr*0.3], fill=C_CYAN_DEEP, outline=C_CYAN_MINT)
        d_branch.point([(msx, msy - mh - int(mr*0.2))], fill=C_WHITE_PURE)

    # ==========================================
    # LAYER 4: FLOWING SPIRIT TAIL & LEFT EAR
    # ==========================================
    # Distant Left Ear (curves back-left with smooth Bezier contour)
    ear_l_outer = cubic_bezier((208, 175), (170, 135), (130, 100), (95, 70), n=25)
    ear_l_inner = cubic_bezier((95, 70), (125, 108), (160, 150), (195, 185), n=25)
    ear_l_poly = ear_l_outer + ear_l_inner
    d_tail.polygon(ear_l_poly, fill=C_TWILIGHT_BLUE, outline=C_TWILIGHT_DARK, width=2)
    d_tail.polygon([(x + 2, y + 2) for x, y in ear_l_poly], fill=C_CYAN_DEEP)
    d_tail.polygon([(x + 4, y + 3) for x, y in ear_l_poly[:30]], fill=C_CYAN_MID)

    # Sinuous Flowing Spirit Tail
    # Tail loops gracefully from rump (275, 315) back, down, and curls up to (385, 215)
    tail_top = cubic_bezier((270, 312), (310, 335), (360, 330), (390, 260), n=30)
    tail_tip = cubic_bezier((390, 260), (395, 235), (392, 215), (385, 210), n=15)
    tail_bot = cubic_bezier((385, 210), (370, 245), (340, 295), (285, 305), n=30)
    tail_poly = tail_top + tail_tip + tail_bot
    d_tail.polygon(tail_poly, fill=C_CYAN_DEEP, outline=C_TWILIGHT_BLUE, width=2)
    d_tail.polygon([(x - 2, y - 2) for x, y in tail_poly], fill=C_CYAN_MID)
    d_tail.polygon([(x - 4, y - 4) for x, y in tail_top], fill=C_CYAN_MINT)
    # Luminous plume flame at tail tip
    d_tail.ellipse([378, 205, 396, 225], fill=C_CYAN_MINT)
    d_tail.ellipse([382, 208, 392, 221], fill=C_WHITE_PURE)
    d_tail.point([(395, 198), (402, 206), (398, 192), (406, 215)], fill=C_WHITE_PURE)

    # ==========================================
    # LAYER 5: LUMINOUS SPIRIT BODY & PAWS
    # ==========================================
    # Smooth curved spirit torso (chest, arched back, flank)
    c_chest = cubic_bezier((215, 215), (192, 245), (190, 285), (200, 325), n=20)
    c_arm_l = cubic_bezier((200, 325), (204, 348), (208, 362), (216, 368), n=15)
    c_paw_l = [(222, 368), (224, 350)]
    c_belly = cubic_bezier((224, 350), (235, 325), (250, 320), (262, 320), n=15)
    c_paw_r = [(265, 345), (272, 358), (280, 358), (282, 340)]
    c_rump  = cubic_bezier((282, 340), (292, 315), (285, 275), (268, 245), n=20)
    c_back  = cubic_bezier((268, 245), (255, 230), (242, 222), (228, 215), n=15)
    body_poly = c_chest + c_arm_l + c_paw_l + c_belly + c_paw_r + c_rump + c_back
    d_body.polygon(body_poly, fill=C_TWILIGHT_BLUE, outline=C_TWILIGHT_DARK, width=2)
    d_body.polygon([(x, y - 2) for x, y in body_poly], fill=C_CYAN_DEEP)

    # Inner bright mint body core
    i_chest = cubic_bezier((218, 222), (198, 250), (198, 285), (208, 325), n=15)
    i_belly = cubic_bezier((208, 325), (230, 315), (255, 305), (272, 275), n=15)
    i_back  = cubic_bezier((272, 275), (260, 240), (245, 228), (228, 222), n=15)
    inner_pts = i_chest + i_belly + i_back
    d_body.polygon(inner_pts, fill=C_CYAN_MID)
    d_body.polygon([(x, y - 2) for x, y in inner_pts], fill=C_CYAN_MINT)

    # Glowing Spirit Core / Heart on chest (Sein's Light)
    d_body.ellipse([206, 250, 234, 282], fill=C_CYAN_HOT)
    d_body.ellipse([211, 255, 229, 277], fill=C_WHITE_PURE)

    # Poised, muscular, crouched hind leg
    hind_leg_outer = cubic_bezier((275, 295), (298, 315), (302, 345), (294, 365), n=20)
    hind_leg_inner = cubic_bezier((294, 365), (282, 366), (278, 345), (270, 320), n=15)
    hind_poly = hind_leg_outer + hind_leg_inner
    d_body.polygon(hind_poly, fill=C_CYAN_DEEP, outline=C_TWILIGHT_DARK, width=1)
    d_body.polygon([(x - 2, y - 1) for x, y in hind_poly], fill=C_CYAN_MID)
    d_body.polygon([(x - 3, y - 2) for x, y in hind_leg_outer[:12]], fill=C_CYAN_MINT)

    # Rounded front paws
    d_body.ellipse([204, 360, 222, 370], fill=C_CYAN_MINT, outline=C_TWILIGHT_DARK, width=1)
    d_body.ellipse([207, 362, 219, 367], fill=C_WHITE_PURE)
    d_body.ellipse([264, 352, 282, 362], fill=C_CYAN_MINT, outline=C_TWILIGHT_DARK, width=1)
    d_body.ellipse([267, 354, 279, 359], fill=C_WHITE_PURE)

    # ==========================================
    # LAYER 6: HEAD, MUZZLE & PRIMARY (RIGHT) EAR
    # ==========================================
    # Soft, organic, feline/bunny rounded spirit head
    h_jaw   = cubic_bezier((225, 222), (205, 212), (195, 195), (194, 185), n=15) # cute muzzle
    h_brow  = cubic_bezier((194, 185), (196, 168), (210, 150), (235, 148), n=15) # forehead
    h_crown = cubic_bezier((235, 148), (255, 152), (268, 170), (264, 198), n=15) # crown
    h_neck  = cubic_bezier((264, 198), (258, 212), (242, 222), (225, 222), n=10) # throat
    head_poly = h_jaw + h_brow + h_crown + h_neck
    d_head.polygon(head_poly, fill=C_CYAN_DEEP, outline=C_TWILIGHT_DARK, width=2)
    d_head.polygon([(x, y - 1) for x, y in head_poly], fill=C_CYAN_MID)
    d_head.polygon([(x, y - 3) for x, y in head_poly], fill=C_CYAN_MINT)
    # Forehead pure glow
    d_head.ellipse([205, 155, 238, 184], fill=C_WHITE_PURE)

    # Soft glowing spirit antenna curl
    crest_pts = cubic_bezier((220, 150), (216, 135), (210, 128), (204, 125), n=15)
    for i in range(len(crest_pts)-1):
        d_head.line([crest_pts[i], crest_pts[i+1]], fill=C_CYAN_MINT, width=2)
    d_head.point([crest_pts[-1]], fill=C_WHITE_PURE)

    # Primary Swept Fore Ear (Right side: long, fluid, feather-like curve)
    ear_r_outer = cubic_bezier((238, 155), (265, 130), (295, 95), (322, 55), n=30)
    ear_r_inner = cubic_bezier((322, 55), (305, 88), (278, 130), (252, 168), n=30)
    ear_r_poly = ear_r_outer + ear_r_inner
    d_head.polygon(ear_r_poly, fill=C_CYAN_DEEP, outline=C_TWILIGHT_DARK, width=2)
    d_head.polygon([(x - 2, y) for x, y in ear_r_poly], fill=C_CYAN_MID)
    d_head.polygon([(x - 4, y - 1) for x, y in ear_r_poly], fill=C_CYAN_MINT)
    # Luminous white inner light beam
    for i in range(len(ear_r_outer)-1):
        d_head.line([(ear_r_outer[i][0] - 2, ear_r_outer[i][1] + 1),
                     (ear_r_outer[i+1][0] - 2, ear_r_outer[i+1][1] + 1)], fill=C_WHITE_PURE, width=2)

    # Cute nose dot
    d_head.point([(195, 188)], fill=C_TWILIGHT_DARK)

    # ==========================================
    # LAYER 7: SOULFUL CELESTIAL EYES
    # ==========================================
    # Large, soulful, almond-shaped eye
    eye_top = cubic_bezier((206, 188), (214, 176), (225, 178), (234, 186), n=15)
    eye_bot = cubic_bezier((234, 186), (228, 198), (216, 199), (206, 188), n=15)
    eye_poly = eye_top + eye_bot
    d_eyes.polygon(eye_poly, fill=C_SHADOW_NAVY, outline=C_TWILIGHT_DARK, width=2)
    d_eyes.ellipse([210, 180, 230, 198], fill=(12, 28, 65, 255))
    d_eyes.ellipse([213, 189, 227, 198], fill=C_CYAN_DEEP)
    d_eyes.ellipse([216, 191, 224, 197], fill=C_CYAN_MID)

    # Signature celestial star sparkles inside the eye!
    d_eyes.ellipse([211, 180, 218, 187], fill=C_WHITE_PURE)  # Big primary sparkle
    d_eyes.point([(224, 187)], fill=C_WHITE_PURE)            # Small companion sparkle

    # Far eye (brow curve on silhouette)
    d_eyes.line([(198, 181), (202, 179), (204, 183)], fill=C_SHADOW_NAVY, width=2)
    d_eyes.point([(200, 180)], fill=C_WHITE_PURE)

    # ==========================================
    # LAYER 8: RIM LIGHTING & SPECULAR GLINTS
    # ==========================================
    # Pure living white edge-lighting along curves
    for i in range(len(h_brow)-1):
        d_highlights.line([h_brow[i], h_brow[i+1]], fill=C_WHITE_PURE, width=2)
    for i in range(len(ear_r_outer)-1):
        d_highlights.line([ear_r_outer[i], ear_r_outer[i+1]], fill=C_WHITE_PURE, width=2)
    for i in range(len(c_back)-1):
        d_highlights.line([c_back[i], c_back[i+1]], fill=C_WHITE_PURE, width=2)
    for i in range(len(tail_top)-1):
        d_highlights.line([tail_top[i], tail_top[i+1]], fill=C_WHITE_PURE, width=2)
    for i in range(len(c_chest)-1):
        d_highlights.line([c_chest[i], c_chest[i+1]], fill=C_WHITE_PURE, width=2)

    # Stardust glints
    draw_star(d_highlights, 322, 55, 9, C_WHITE_PURE)
    draw_star(d_highlights, 95, 70, 7, C_WHITE_PURE)
    draw_star(d_highlights, 220, 266, 10, C_WHITE_PURE)
    draw_star(d_highlights, 220, 266, 4, C_CYAN_MINT)

    layers = [
        ("Forest Spirit Aura", l_aura),
        ("Floating Light Wisps", l_wisps),
        ("Mossy Spirit Branch", l_branch),
        ("Spirit Tail & Left Ear", l_tail),
        ("Luminous Spirit Body", l_body),
        ("Head & Swept Right Ear", l_head),
        ("Soulful Eyes & Face", l_eyes),
        ("Pure Light Highlights", l_highlights)
    ]

    composite = Image.new('RGBA', (w, h), (0,0,0,0))
    for _, lay in layers:
        composite = Image.alpha_composite(composite, lay)

    return layers, composite

if __name__ == "__main__":
    layers, composite = draw_ori()
    composite.save('/tmp/ori_spirit_masterpiece.png')
    print("Masterpiece Ori Character successfully rendered to /tmp/ori_spirit_masterpiece.png")
