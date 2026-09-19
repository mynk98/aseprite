# Lyra AI Pixel Art Toolkit & Workflow

This directory contains autonomous tooling, procedural generators, and pipeline scripts connecting **Lyra (AI Agent)** with **Aseprite**.

## Architecture & Capabilities

1. **Headless Execution (`aseprite -b`)**:
   All scripts can run in batch mode without opening the GUI, allowing Lyra to procedurally paint, animate, and export game assets directly from terminal/code invocations.

2. **Lua Scripting Engine**:
   Aseprite provides a full embedded Lua environment (`Sprite`, `Image`, `Color`, `Cel`, `Layer`, `Tag`). Scripts inside `scripts/` utilize this API.

3. **Game Engine Pipeline**:
   - Unity: Auto-converts `.aseprite` or outputs packed texture atlases with JSON metadata for `SpriteRenderer` / `SpriteAtlas`.
   - Godot / Web: Direct PNG + JSON atlas export.

## CLI Usage (`lyra_aseprite.py`)

Run scripts headlessly via the wrapper:

```bash
# Run a custom Lua script
python3 tools/ai/lyra_aseprite.py run-lua --script tools/ai/scripts/generate_sprite.lua

# Export an .aseprite file to a packed spritesheet + JSON atlas
python3 tools/ai/lyra_aseprite.py export-sheet --input character.aseprite --sheet character_sheet.png --data character_sheet.json

# Procedurally generate a sprite
python3 tools/ai/lyra_aseprite.py generate --type heart --size 16 --output heart.aseprite
```

## Adding New Tools

1. Add your Lua script to `scripts/`.
2. Add corresponding CLI commands in `lyra_aseprite.py`.
3. Commit and push directly to `mynk98/aseprite` on GitHub!
