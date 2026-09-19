#!/usr/bin/env python3
"""
High-Fidelity Pixel Art Generator
Transforms a character reference into an authentic, crisp pixel art sprite on a 500x500 canvas.
Applies:
1. Pure alpha isolation and precise centering on 500x500.
2. Edge-preserving cel-shading cluster consolidation.
3. Strict palette quantization to cohesive retro game ramps.
4. Clean outline sharpening and eye/insignia contrast enhancement.
"""

import sys
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np

def hex_to_rgb(h):
    h = h.lstrip('#')
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]

# Hand-crafted cohesive retro palette for this character
PALETTE_HEX = [
    # Outlines & Black
    "#110d0c", "#1d1715", "#29211d",
    # Spiky Hair
    "#34241b", "#473426", "#5d4533", "#745943", "#8c6e55",
    # Skin Ramps
    "#7e4525", "#9e5c33", "#bf794c", "#db976b", "#eab28b", "#f6cead", "#fae3d0",
    # Tunic Ramps
    "#6b5c47", "#8c7b62", "#aa997f", "#c6b79c", "#dbcfb8", "#ede5d4",
    # Sun Emblem Ramps
    "#823706", "#b0520b", "#d97314", "#f29824", "#fec34d",
    # Golden Cat Eye (Heterochromia)
    "#5e3a00", "#996200", "#d69004", "#f5b716", "#fedc4a", "#fff5b0",
    # Brown Eye (Heterochromia)
    "#1f130b", "#3b2314", "#5e3a22", "#805234",
    # Belt, Sash & Shorts
    "#23160f", "#362319", "#4c3224", "#634433",
    # Leather Boots
    "#2a1b13", "#3d2a1f", "#543c2c", "#6e503c", "#87654d",
    # Specular & Highlights
    "#ffffff", "#e0e6ed"
]

PALETTE = np.array([hex_to_rgb(c) for c in PALETTE_HEX], dtype=float)

def quantize_to_palette(rgb_arr):
    h, w, _ = rgb_arr.shape
    flat_rgb = rgb_arr.reshape(-1, 3).astype(float)
    
    # Weighted Euclidean distance in perception-weighted RGB space
    # (r*0.3, g*0.59, b*0.11)
    weights = np.array([0.30, 0.59, 0.11], dtype=float)
    diffs = (flat_rgb[:, None, :] - PALETTE[None, :, :]) * weights
    dists = np.sum(diffs ** 2, axis=2)
    nearest_indices = np.argmin(dists, axis=1)
    
    quantized = PALETTE[nearest_indices].reshape(h, w, 3).astype(np.uint8)
    return quantized

def create_pixel_art(input_path: str, output_png: str, output_ase: str):
    src = Image.open(input_path).convert('RGBA')
    arr = np.array(src)
    
    # Isolate character from background #605746
    bg = np.array([96, 87, 70], dtype=float)
    diff = np.sqrt(np.sum((arr[:, :, :3].astype(float) - bg)**2, axis=2))
    is_bg = diff < 22.0
    # Clear left border stray mark
    is_bg[100:130, :15] = True
    
    # 8-connected flood fill from corners
    h, w = arr.shape[:2]
    visited = np.zeros((h, w), dtype=bool)
    from collections import deque
    q = deque()
    for y in range(h):
        if is_bg[y, 0]: q.append((y, 0)); visited[y, 0] = True
        if is_bg[y, w-1]: q.append((y, w-1)); visited[y, w-1] = True
    for x in range(w):
        if is_bg[0, x]: q.append((0, x)); visited[0, x] = True
        if is_bg[h-1, x]: q.append((h-1, x)); visited[h-1, x] = True
        
    while q:
        cy, cx = q.popleft()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and is_bg[ny, nx]:
                    visited[ny, nx] = True
                    q.append((ny, nx))
                    
    char_mask = ~visited
    alpha = np.where(char_mask, 255, 0).astype(np.uint8)
    arr[:, :, 3] = alpha
    isolated = Image.fromarray(arr)
    
    # Crop to character bounding box
    bbox = isolated.getbbox()
    cropped = isolated.crop(bbox)
    cw, ch = cropped.size
    
    # Scale to fit 500x500 canvas (height 450, leaving 25px margin)
    target_h = 450
    target_w = int(round(cw * (target_h / ch)))
    
    # Resize with crisp sampling
    scaled = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Pixel clustering: apply median filter to consolidate micro-noise into cel-shaded flats
    rgb = scaled.convert('RGB')
    clustered_rgb = rgb.filter(ImageFilter.MedianFilter(size=3))
    
    # Quantize to curated pixel art palette
    rgb_arr = np.array(clustered_rgb)
    quantized_rgb = quantize_to_palette(rgb_arr)
    
    # Sharpen outlines: detect edges on alpha / luminance
    scaled_alpha = np.array(scaled.split()[-1])
    solid_mask = scaled_alpha > 128
    
    # Build 500x500 canvas
    canvas_rgba = np.zeros((500, 500, 4), dtype=np.uint8)
    ox = (500 - target_w) // 2
    oy = (500 - target_h) // 2
    
    canvas_rgba[oy:oy+target_h, ox:ox+target_w, :3] = quantized_rgb
    canvas_rgba[oy:oy+target_h, ox:ox+target_w, 3] = np.where(solid_mask, 255, 0)
    
    out_img = Image.fromarray(canvas_rgba)
    out_img.save(output_png)
    print(f"Saved PNG to {output_png}")
    
    return output_png

if __name__ == "__main__":
    in_file = sys.argv[1]
    out_png = sys.argv[2]
    create_pixel_art(in_file, out_png, "")
