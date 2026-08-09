"""Compose fixed site background from upscaled side portraits."""
from __future__ import annotations

import os

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

IMG = os.path.dirname(os.path.abspath(__file__))
STONE = (0x12, 0x11, 0x10)  # --pffw-stone


def fit_height(im: Image.Image, target_h: int, max_w: int | None = None) -> Image.Image:
    w, h = im.size
    scale = target_h / h
    nw, nh = int(w * scale), int(h * scale)
    if max_w and nw > max_w:
        scale = max_w / w
        nw, nh = int(w * scale), int(h * scale)
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def smoothstep(t: np.ndarray) -> np.ndarray:
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def horizontal_fade_mask(
    size: tuple[int, int],
    fade_from_left: bool,
    solid_ratio: float = 0.38,
    fade_ratio: float = 0.55,
) -> Image.Image:
    """Opaque on the outer edge, soft falloff toward the page center."""
    w, h = size
    x = np.arange(w, dtype=np.float32)
    src = x if fade_from_left else (w - 1 - x)
    solid_end = w * solid_ratio
    fade_end = w * (solid_ratio + fade_ratio)
    t = (src - solid_end) / max(1.0, fade_end - solid_end)
    alpha = np.where(src <= solid_end, 1.0, np.where(src >= fade_end, 0.0, 1.0 - smoothstep(t)))
    col = (alpha * 255.0).astype(np.uint8)
    mask = np.repeat(col[np.newaxis, :], h, axis=0)
    return Image.fromarray(mask, mode="L").filter(ImageFilter.GaussianBlur(radius=28))


def vertical_edge_fade(mask: Image.Image, top_fade: float = 0.06, bottom_fade: float = 0.12) -> Image.Image:
    arr = np.asarray(mask).astype(np.float32)
    h, w = arr.shape
    y = np.arange(h, dtype=np.float32)
    top_n = max(1.0, h * top_fade)
    bot_n = max(1.0, h * bottom_fade)
    mul = np.ones(h, dtype=np.float32)
    top_idx = y < top_n
    bot_idx = y > (h - 1 - bot_n)
    mul[top_idx] = smoothstep(y[top_idx] / top_n)
    mul[bot_idx] = smoothstep((h - 1 - y[bot_idx]) / bot_n)
    arr *= mul[:, np.newaxis]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), mode="L")


def place_portrait(
    base: Image.Image,
    portrait: Image.Image,
    xy: tuple[int, int],
    fade_from_left: bool,
) -> None:
    mask = horizontal_fade_mask(portrait.size, fade_from_left=fade_from_left)
    mask = vertical_edge_fade(mask)
    darkened = ImageEnhance.Brightness(portrait).enhance(0.88)
    darkened = ImageEnhance.Color(darkened).enhance(0.92)
    r, g, b, _a = darkened.split()
    layered = Image.merge("RGBA", (r, g, b, mask))
    base.alpha_composite(layered, xy)


def export_faded_panel(portrait: Image.Image, fade_from_left: bool, name: str) -> None:
    panel = Image.new("RGBA", portrait.size, (0, 0, 0, 0))
    place_portrait(panel, portrait, (0, 0), fade_from_left)
    solid = Image.new("RGBA", portrait.size, STONE + (255,))
    solid = Image.alpha_composite(solid, panel)
    solid.convert("RGB").save(os.path.join(IMG, name), "PNG", optimize=True)


def center_vignette(w: int, h: int, center_clear: int, fade: int = 180, strength: int = 95) -> Image.Image:
    x = np.arange(w, dtype=np.float32)
    cx0 = w / 2 - center_clear / 2
    cx1 = w / 2 + center_clear / 2
    alpha = np.zeros(w, dtype=np.float32)
    inside = (x >= cx0) & (x <= cx1)
    left = x < cx0
    right = x > cx1
    alpha[inside] = strength
    left_dist = cx0 - x[left]
    left_t = 1.0 - left_dist / fade
    alpha[left] = np.where(left_dist >= fade, 0.0, strength * smoothstep(left_t))
    right_dist = x[right] - cx1
    right_t = 1.0 - right_dist / fade
    alpha[right] = np.where(right_dist >= fade, 0.0, strength * smoothstep(right_t))
    a = np.repeat(alpha[np.newaxis, :], h, axis=0).astype(np.uint8)
    rgb = np.zeros((h, w, 4), dtype=np.uint8)
    rgb[..., 0] = 0x0C
    rgb[..., 1] = 0x0B
    rgb[..., 2] = 0x0A
    rgb[..., 3] = a
    return Image.fromarray(rgb, mode="RGBA")


def atmosphere_overlay(w: int, h: int) -> Image.Image:
    y = np.arange(h, dtype=np.float32)
    top_band = h * 0.18
    bot_band = h * 0.22
    alpha = np.zeros(h, dtype=np.float32)
    top = y < top_band
    bot = y > (h - bot_band)
    alpha[top] = 70.0 * ((1.0 - y[top] / top_band) ** 2)
    alpha[bot] = 90.0 * (((y[bot] - (h - bot_band)) / bot_band) ** 2)
    a = np.repeat(alpha[:, np.newaxis], w, axis=1).astype(np.uint8)
    rgb = np.zeros((h, w, 4), dtype=np.uint8)
    rgb[..., 3] = a
    return Image.fromarray(rgb, mode="RGBA")


def main() -> None:
    were = Image.open(os.path.join(IMG, "werewolf-left-upscaled.png")).convert("RGBA")
    wolf = Image.open(os.path.join(IMG, "wolf-right-upscaled.png")).convert("RGBA")

    # Covers common desktop viewports with background-size: cover
    W, H = 2560, 1600
    canvas = Image.new("RGBA", (W, H), STONE + (255,))

    portrait_h = int(H * 0.98)
    were_s = fit_height(were, portrait_h, max_w=int(W * 0.42))
    wolf_s = fit_height(wolf, portrait_h, max_w=int(W * 0.42))

    # Keep ~980px center corridor mostly clear for the 52rem main frame
    center_clear = 980

    were_pos = (0, (H - were_s.size[1]) // 2 + 20)
    wolf_pos = (W - wolf_s.size[0], (H - wolf_s.size[1]) // 2 + 20)

    place_portrait(canvas, were_s, were_pos, fade_from_left=True)
    place_portrait(canvas, wolf_s, wolf_pos, fade_from_left=False)

    canvas = Image.alpha_composite(canvas, center_vignette(W, H, center_clear))
    canvas = Image.alpha_composite(canvas, atmosphere_overlay(W, H))

    final = canvas.convert("RGB")
    full_path = os.path.join(IMG, "site-background.png")
    left_path = os.path.join(IMG, "site-background-left.png")
    right_path = os.path.join(IMG, "site-background-right.png")

    final.save(full_path, "PNG", optimize=True)
    final.crop((0, 0, W // 2, H)).save(left_path, "PNG", optimize=True)
    final.crop((W // 2, 0, W, H)).save(right_path, "PNG", optimize=True)

    export_faded_panel(were_s, True, "werewolf-left-blended.png")
    export_faded_panel(wolf_s, False, "wolf-right-blended.png")

    for name in (
        "site-background.png",
        "site-background-left.png",
        "site-background-right.png",
        "werewolf-left-blended.png",
        "wolf-right-blended.png",
    ):
        path = os.path.join(IMG, name)
        im = Image.open(path)
        print(f"{name}: {im.size}  {os.path.getsize(path) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
