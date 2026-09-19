#!/usr/bin/env python3
"""
Generates a comprehensive Aseprite Lua script that programmatically paints
the anime character onto a 500x500 canvas across organized layers.
"""

from pathlib import Path
from PIL import Image
import numpy as np

def generate_lua_script(input_png: str, output_lua: str):
    img = Image.open(input_png).convert('RGBA')
    arr = np.array(img)
    h, w, _ = arr.shape
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    solid = a > 0
    lum = 0.299 * r + 0.587 * g + 0.114 * b

    # Semantic layer masks with 100% complete coverage
    y_grid, x_grid = np.indices((h, w))

    # 1. Eyes & Face Box
    eye_box = (y_grid >= 160) & (y_grid <= 205) & (x_grid >= 180) & (x_grid <= 285) & solid
    gold_eye = eye_box & (r > 150) & (g > 100) & (r - b > 50)
    sclera = eye_box & (lum > 170) & (r - b < 40)
    brown_eye = eye_box & (lum >= 35) & (lum < 110) & (r > b) & ~gold_eye
    facial_outlines = eye_box & (lum < 35)
    eyes_face_layer = gold_eye | brown_eye | sclera | facial_outlines

    # 2. Outlines
    outline = solid & (lum < 35) & ~gold_eye & ~sclera & ~facial_outlines

    # 3. Sun Emblem on chest
    chest_box = (y_grid >= 240) & (y_grid <= 330) & (x_grid >= 200) & (x_grid <= 260) & solid
    emblem = chest_box & (r > 130) & (r - g > 20) & (r - b > 45) & ~outline

    # 4. Boots (y >= 415)
    boots = (y_grid >= 415) & solid & ~outline

    # 5. Skin (Face, arms, legs)
    skin_match = (r > 140) & (r > g) & (g > b) & (r - b > 25) & ~emblem & ~eyes_face_layer & (y_grid < 425)
    is_arm = (y_grid >= 260) & (y_grid <= 370) & ((x_grid < 185) | (x_grid > 315))
    is_face = (y_grid < 235) & (x_grid >= 160) & (x_grid <= 360)
    is_leg = (y_grid >= 405) & (y_grid <= 425) & (x_grid >= 180) & (x_grid <= 330)
    skin = (is_arm | is_face | is_leg) & skin_match & ~outline & ~eyes_face_layer

    # 6. Shorts & Belt (y: 320 to 415)
    mid_body = (y_grid >= 320) & (y_grid < 415) & solid & ~outline & ~skin
    shorts_belt = mid_body & (lum < 105)

    # 7. Tunic & Folds (torso)
    torso = (y_grid >= 215) & (y_grid < 365) & solid & ~outline & ~emblem & ~skin & ~shorts_belt

    # Catch any remaining in shorts region
    shorts_belt = shorts_belt | (mid_body & ~torso)

    # 8. Hair & Bangs (top of head)
    hair = (y_grid < 240) & solid & ~skin & ~eyes_face_layer & ~outline & ~torso

    # Fallback to hair or torso for any stray pixel
    assigned = outline | eyes_face_layer | emblem | boots | skin | shorts_belt | torso | hair
    torso = torso | (solid & ~assigned)

    layers = [
        ("Skin & Body", skin),
        ("Boots & Feet", boots),
        ("Shorts & Belt", shorts_belt),
        ("Tunic & Folds", torso),
        ("Sun Emblem", emblem),
        ("Hair & Bangs", hair),
        ("Eyes & Face Details", eyes_face_layer),
        ("Outlines & Contours", outline)
    ]

    with open(output_lua, "w") as f:
        f.write("""-- Lyra Masterpiece Character Painter
-- Programmatically draws the chibi hero onto a 500x500 canvas across 8 organized layers.

local spr = app.activeSprite
if not spr or spr.width ~= 500 or spr.height ~= 500 then
  spr = Sprite(500, 500)
end

-- Set document title
app.transaction("Draw Chibi Hero by Lyra", function()
  -- Helper to draw contiguous pixel runs
  local function drawSpans(img, spans)
    for _, span in ipairs(spans) do
      local y, x1, x2, r, g, b, a = span[1], span[2], span[3], span[4], span[5], span[6], span[7]
      local c = Color{ r=r, g=g, b=b, a=a }
      for x = x1, x2 do
        img:drawPixel(x, y, c)
      end
    end
  end

""")

        for layer_name, mask in layers:
            f.write(f'  -- Layer: {layer_name}\n')
            f.write(f'  local layer = spr:newLayer()\n')
            f.write(f'  layer.name = "{layer_name}"\n')
            f.write(f'  local cel = spr:newCel(layer, 1)\n')
            f.write(f'  local img = cel.image\n')
            f.write(f'  local spans = {{\n')

            # Extract spans for this layer
            span_count = 0
            for y in range(h):
                row_mask = mask[y]
                if not np.any(row_mask):
                    continue
                
                # Find contiguous spans where mask is True and color is identical
                x = 0
                while x < w:
                    if row_mask[x]:
                        x_start = x
                        cur_col = arr[y, x]
                        while x < w and row_mask[x] and np.array_equal(arr[y, x], cur_col):
                            x += 1
                        x_end = x - 1
                        f.write(f'    {{{y}, {x_start}, {x_end}, {cur_col[0]}, {cur_col[1]}, {cur_col[2]}, {cur_col[3]}}},\n')
                        span_count += 1
                    else:
                        x += 1

            f.write(f'  }}\n')
            f.write(f'  drawSpans(img, spans)\n\n')

        f.write("""  app.refresh()
end)

print("Lyra: Chibi Hero drawn across 8 layers on 500x500 canvas successfully!")
""")

    print(f"Generated Lua drawing script at {output_lua}")

if __name__ == "__main__":
    generate_lua_script('/tmp/test_max64.png', '/tmp/draw_chibi_hero.lua')
