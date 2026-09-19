-- Lyra Procedural Pixel Art Generator
-- Generates a 16x16 or 32x32 retro asset with custom palettes

local width = tonumber(app.params["width"] or 16)
local height = tonumber(app.params["height"] or 16)
local shape = app.params["shape"] or "gem"
local output_ase = app.params["output_ase"] or "output.aseprite"
local output_png = app.params["output_png"] or "output.png"

local sprite = Sprite(width, height)
local image = sprite.cels[1].image

-- Color Palette
local c_outline = Color{ r=20, g=20, b=30, a=255 }
local c_primary = Color{ r=80, g=180, b=250, a=255 }
local c_highlight = Color{ r=200, g=240, b=255, a=255 }
local c_shadow = Color{ r=40, g=90, b=160, a=255 }

if shape == "gem" then
  local cx, cy = math.floor(width / 2), math.floor(height / 2)
  local r = math.floor(math.min(width, height) * 0.4)
  for y = -r, r do
    for x = -r, r do
      local dist = math.abs(x) + math.abs(y)
      if dist <= r then
        local px = cx + x
        local py = cy + y
        if dist == r then
          image:drawPixel(px, py, c_outline)
        elseif x <= 0 and y <= 0 then
          image:drawPixel(px, py, c_highlight)
        elseif x > 0 and y > 0 then
          image:drawPixel(px, py, c_shadow)
        else
          image:drawPixel(px, py, c_primary)
        end
      end
    end
  end
end

sprite:saveCopyAs(output_png)
sprite:saveAs(output_ase)
print(string.format("Successfully generated %s (%dx%d) -> %s & %s", shape, width, height, output_ase, output_png))
