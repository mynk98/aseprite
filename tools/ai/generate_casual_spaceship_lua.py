#!/usr/bin/env python3
"""
Converts the casual mobile spaceship into a native Aseprite Lua script
that programmatically constructs all 8 layers and paints each cel.
"""

from pathlib import Path
from PIL import Image
import numpy as np
from render_casual_spaceship import draw_casual_spaceship

def generate_lua():
    layers, composite = draw_casual_spaceship()
    output_lua = Path("/Users/mynk/Projects/aseprite/tools/ai/scripts/draw_casual_spaceship.lua")
    user_scripts_lua = Path.home() / "Library/Application Support/Aseprite/scripts/draw_casual_spaceship.lua"

    with open(output_lua, "w") as f:
        f.write("""-- Lyra Casual Mobile Game Spaceship Painter
-- Programmatically draws a juicy, vibrant casual starfighter across 8 organized layers.

local spr = app.activeSprite
if not spr or spr.width ~= 500 or spr.height ~= 500 then
  spr = Sprite(500, 500)
end

app.transaction("Draw Casual Starfighter by Lyra", function()
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

        for layer_name, layer_img in layers:
            arr = np.array(layer_img)
            h, w, _ = arr.shape
            mask = arr[:, :, 3] > 0

            f.write(f'  -- Layer: {layer_name}\n')
            f.write(f'  local layer = spr:newLayer()\n')
            f.write(f'  layer.name = "{layer_name}"\n')
            f.write(f'  local cel = spr:newCel(layer, 1)\n')
            f.write(f'  local img = cel.image\n')
            f.write(f'  local spans = {{\n')

            for y in range(h):
                row_mask = mask[y]
                if not np.any(row_mask):
                    continue

                x = 0
                while x < w:
                    if row_mask[x]:
                        x_start = x
                        cur_col = arr[y, x]
                        while x < w and row_mask[x] and np.array_equal(arr[y, x], cur_col):
                            x += 1
                        x_end = x - 1
                        f.write(f'    {{{y}, {x_start}, {x_end}, {cur_col[0]}, {cur_col[1]}, {cur_col[2]}, {cur_col[3]}}},\n')
                    else:
                        x += 1

            f.write(f'  }}\n')
            f.write(f'  drawSpans(img, spans)\n\n')

        f.write("""  app.refresh()
end)

if not app.isUIAvailable then
  spr:saveAs("/Users/mynk/Desktop/drawn_casual_spaceship.aseprite")
end

print("Lyra: Casual Mobile Spaceship drawn across 8 layers on 500x500 canvas successfully!")
""")

    user_scripts_lua.write_text(output_lua.read_text())
    print(f"Generated Lua script at {output_lua} and copied to {user_scripts_lua}")

if __name__ == "__main__":
    generate_lua()
