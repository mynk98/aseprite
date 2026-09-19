#!/usr/bin/env python3
from __future__ import annotations
"""
Lyra AI Pixel Art Tool & Pipeline Controller
Automates Aseprite batch commands, procedural Lua generation, and spritesheet compilation.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from typing import Optional

ASEPRITE_BIN = os.environ.get("ASEPRITE_BIN", "aseprite")


def run_aseprite(args: list[str]) -> subprocess.CompletedProcess:
    cmd = [ASEPRITE_BIN, "-b"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running Aseprite: {result.stderr}", file=sys.stderr)
        sys.exit(result.returncode)
    return result


def export_sheet(input_file: str, sheet_file: str, data_file: Optional[str] = None, format: str = "json-array"):
    """Export an Aseprite file to a spritesheet with optional JSON metadata."""
    args = [input_file, "--sheet", sheet_file]
    if data_file:
        args += ["--data", data_file, "--format", format]
    result = run_aseprite(args)
    print(f"Exported sheet: {sheet_file}")
    if data_file:
        print(f"Exported atlas metadata: {data_file}")
    if result.stdout:
        print(result.stdout.strip())


def run_lua(script_path: str, script_params: dict[str, str] | None = None):
    """Execute a headless Lua script inside Aseprite."""
    args = []
    if script_params:
        for k, v in script_params.items():
            args += ["--script-param", f"{k}={v}"]
    args += ["-script", script_path]
    result = run_aseprite(args)
    if result.stdout:
        print(result.stdout.strip())


def generate_sprite(shape: str, width: int, height: int, output_ase: str, output_png: str):
    script = Path(__file__).parent / "scripts" / "generate_sprite.lua"
    params = {
        "shape": shape,
        "width": str(width),
        "height": str(height),
        "output_ase": output_ase,
        "output_png": output_png,
    }
    run_lua(str(script), params)


def main():
    parser = argparse.ArgumentParser(description="Lyra Aseprite AI Pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # export-sheet
    sub_export = subparsers.add_parser("export-sheet", help="Export .aseprite to spritesheet")
    sub_export.add_argument("--input", required=True, help="Input .aseprite file")
    sub_export.add_argument("--sheet", required=True, help="Output spritesheet PNG")
    sub_export.add_argument("--data", help="Output JSON atlas file")
    sub_export.add_argument("--format", default="json-array", choices=["json-array", "json-hash"])

    # run-lua
    sub_lua = subparsers.add_parser("run-lua", help="Run Lua script headlessly")
    sub_lua.add_argument("--script", required=True, help="Path to Lua script")
    sub_lua.add_argument("--param", action="append", help="Script parameter in key=val format")

    # generate
    sub_gen = subparsers.add_parser("generate", help="Procedurally generate a sprite")
    sub_gen.add_argument("--shape", default="gem", choices=["gem"], help="Shape type")
    sub_gen.add_argument("--size", type=int, default=16, help="Width and height in pixels")
    sub_gen.add_argument("--output", default="sprite.aseprite", help="Output .aseprite filename")
    sub_gen.add_argument("--png", default="sprite.png", help="Output .png filename")

    args = parser.parse_args()

    if args.command == "export-sheet":
        export_sheet(args.input, args.sheet, args.data, args.format)
    elif args.command == "run-lua":
        params = {}
        if args.param:
            for p in args.param:
                if "=" in p:
                    k, v = p.split("=", 1)
                    params[k] = v
        run_lua(args.script, params)
    elif args.command == "generate":
        generate_sprite(args.shape, args.size, args.size, args.output, args.png)


if __name__ == "__main__":
    main()
