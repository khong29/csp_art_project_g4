import simple_animation as sa
import math


def draw_frame(frame, elapsed, width, height):
    # ── Sky ──────────────────────────────────────────────────────────────────
    # Gradient sky: draw horizontal bands from deep blue at top to light blue
    sky_bands = 30
    for i in range(sky_bands):
        t = i / sky_bands
        # Interpolate from deep sky blue (top) to pale cyan-white (horizon)
        hue = 0.58 - t * 0.03          # slight hue shift toward cyan
        light = 0.45 + t * 0.30        # get lighter near horizon
        sat = 0.70 - t * 0.25
        sa.set_fill_color(sa.hls_to_rgb_hex(hue, light, sat))
        sa.set_outline_color(sa.hls_to_rgb_hex(hue, light, sat))
        band_h = height * 0.55 / sky_bands
        sa.fill_rectangle(0, i * band_h, width, band_h + 1)

    # ── Animated Clouds ──────────────────────────────────────────────────────
    cloud_color = "#f0f4ff"
    cloud_positions = [
        (sa.loop_motion(-120, width + 50, 0.3, frame), 0.05 * height, 1.0),
        (sa.loop_motion(-200, width + 80, 0.18, frame + 200), 0.09 * height, 0.7),
        (sa.loop_motion(-80, width + 60, 0.22, frame + 400), 0.04 * height, 0.85),
        (sa.loop_motion(-150, width + 100, 0.14, frame + 100), 0.13 * height, 0.6),
    ]

    def draw_cloud(cx, cy, scale):
        sa.set_fill_color(cloud_color)
        sa.set_outline_color(cloud_color)
        sa.fill_circle(cx, cy, int(28 * scale))
        sa.fill_circle(cx + int(30 * scale), cy - int(8 * scale), int(22 * scale))
        sa.fill_circle(cx + int(60 * scale), cy, int(26 * scale))
        sa.fill_circle(cx + int(25 * scale), cy + int(14 * scale), int(20 * scale))
        sa.fill_circle(cx + int(45 * scale), cy + int(12 * scale), int(22 * scale))

    for cx, cy, scale in cloud_positions:
        draw_cloud(cx, cy, scale)

    # ── Far background mountains (snow-capped, blue-grey) ────────────────────
    horizon_y = height * 0.38

    def draw_mountain(peaks, color_top, color_body):
        # Fill body
        sa.set_fill_color(color_body)
        sa.set_outline_color(color_body)
        for i in range(len(peaks) - 1):
            x1, y1 = peaks[i]
            x2, y2 = peaks[i + 1]
            base_y = horizon_y + 60
            sa.fill_triangle(x1, y1, x2, y2, x1, base_y)
            sa.fill_triangle(x2, y2, x2, base_y, x1, base_y)

        # Snow caps on the highest peaks
        sa.set_fill_color(color_top)
        sa.set_outline_color(color_top)
        for i in range(1, len(peaks) - 1):
            x, y = peaks[i]
            snow_height = (horizon_y - y) * 0.30
            if snow_height > 8:
                sa.fill_triangle(
                    x - snow_height * 0.7, y + snow_height,
                    x + snow_height * 0.7, y + snow_height,
                    x, y
                )

    # Background mountain range
    bg_peaks = [
        (-20,  horizon_y + 10),
        (80,   horizon_y - 95),
        (180,  horizon_y - 60),
        (280,  horizon_y - 130),   # tallest center-left
        (380,  horizon_y - 145),   # tallest center
        (440,  horizon_y - 120),
        (530,  horizon_y - 90),
        (630,  horizon_y - 70),
        (720,  horizon_y - 55),
        (820,  horizon_y + 5),
    ]
    draw_mountain(bg_peaks, "#e8ecf0", "#8fa8c0")

    # ── Mid mountains (darker green-grey) ────────────────────────────────────
    mid_horizon = horizon_y + 40
    mid_peaks = [
        (-30,  mid_horizon + 20),
        (60,   mid_horizon - 40),
        (160,  mid_horizon - 80),
        (240,  mid_horizon - 110),
        (320,  mid_horizon - 60),
        (420,  mid_horizon - 30),
        (500,  mid_horizon - 75),
        (600,  mid_horizon - 55),
        (700,  mid_horizon - 90),
        (790,  mid_horizon - 45),
        (840,  mid_horizon + 10),
    ]
    draw_mountain(mid_peaks, "#cdd5d0", "#4a6650")

    # ── Forest-covered valley sides ──────────────────────────────────────────
    # Left forest slope
    left_slope_points = [
        (0, height),
        (0, height * 0.42),
        (80, height * 0.38),
        (160, height * 0.44),
        (220, height * 0.50),
        (260, height * 0.58),
        (230, height * 0.75),
        (180, height * 0.88),
        (100, height),
    ]
    sa.set_fill_color("#2d5a27")
    sa.set_outline_color("#2d5a27")
    flat_l = []
    for p in left_slope_points:
        flat_l += list(p)
    sa._canvas.create_polygon(flat_l, fill="#2d5a27", outline="#2d5a27")

    # Right forest slope
    right_slope_points = [
        (width, height),
        (width, height * 0.40),
        (720, height * 0.38),
        (640, height * 0.44),
        (560, height * 0.52),
        (520, height * 0.62),
        (540, height * 0.78),
        (600, height * 0.90),
        (width, height),
    ]
    flat_r = []
    for p in right_slope_points:
        flat_r += list(p)
    sa._canvas.create_polygon(flat_r, fill="#2d5a27", outline="#2d5a27")

    # ── Valley floor (green meadow) ──────────────────────────────────────────
    # Gradient meadow bands from mid-green at top to bright green at bottom
    meadow_top = int(height * 0.62)
    meadow_bands = 20
    for i in range(meadow_bands):
        t = i / meadow_bands
        hue = 0.30 + t * 0.03
        light = 0.30 + t * 0.12
        sat = 0.55 + t * 0.15
        sa.set_fill_color(sa.hls_to_rgb_hex(hue, light, sat))
        sa.set_outline_color(sa.hls_to_rgb_hex(hue, light, sat))
        y_band = meadow_top + int(i * (height - meadow_top) / meadow_bands)
        band_h2 = int((height - meadow_top) / meadow_bands) + 1
        # Narrow valley at top, wider at bottom
        taper = 1 - (1 - t) * 0.5
        band_w = int(width * taper)
        x_off = (width - band_w) // 2
        sa.fill_rectangle(x_off, y_band, band_w, band_h2)

    # ── Trees (pine/spruce silhouettes in foreground) ────────────────────────
    def draw_pine(tx, ty, tree_h, color="#1a4020"):
        trunk_w = max(3, tree_h // 10)
        # Trunk
        sa.set_fill_color("#5c3d1e")
        sa.set_outline_color("#5c3d1e")
        sa.fill_rectangle(tx - trunk_w // 2, ty, trunk_w, tree_h // 4)
        # Three layered triangles
        sa.set_fill_color(color)
        sa.set_outline_color(color)
        layers = 3
        for li in range(layers):
            frac = li / layers
            layer_y = ty - int(tree_h * (0.25 + frac * 0.6))
            layer_w = int(tree_h * (0.55 - frac * 0.15))
            overlap = int(tree_h * 0.12)
            sa.fill_triangle(
                tx - layer_w, layer_y + overlap,
                tx + layer_w, layer_y + overlap,
                tx, layer_y - int(tree_h * 0.28)
            )

    # Midground trees (left side of valley opening)
    mid_trees_left = [
        (260, int(height * 0.64), 80, "#244d1f"),
        (295, int(height * 0.67), 65, "#1e4019"),
        (230, int(height * 0.66), 55, "#2a5523"),
        (320, int(height * 0.70), 50, "#1e4019"),
    ]
    for tx, ty, th, tc in mid_trees_left:
        draw_pine(tx, ty, th, tc)

    # Midground trees (right side)
    mid_trees_right = [
        (520, int(height * 0.63), 85, "#244d1f"),
        (555, int(height * 0.66), 70, "#1e4019"),
        (490, int(height * 0.67), 60, "#2a5523"),
        (580, int(height * 0.68), 55, "#1e4019"),
    ]
    for tx, ty, th, tc in mid_trees_right:
        draw_pine(tx, ty, th, tc)

    # Foreground trees (large, bottom area)
    fg_trees = [
        (60,  int(height * 0.72), 140, "#163512"),
        (130, int(height * 0.78), 120, "#1a3d16"),
        (195, int(height * 0.80), 100, "#163512"),
        (680, int(height * 0.73), 135, "#163512"),
        (740, int(height * 0.77), 115, "#1a3d16"),
        (790, int(height * 0.82), 95,  "#163512"),
        (355, int(height * 0.76), 90,  "#1e4019"),
        (430, int(height * 0.74), 105, "#163512"),
    ]
    for tx, ty, th, tc in fg_trees:
        draw_pine(tx, ty, th, tc)

    # ── Winding road ─────────────────────────────────────────────────────────
    # Road color (gravel/dirt - light grey-tan)
    road_color = "#c8c0b0"
    road_edge = "#a8a098"

    # Road as a set of trapezoid segments following a winding S-curve
    # Path: comes from bottom-left, curves right then straightens toward horizon
    road_segments = [
        # (x_left, x_right, y)  — road cross-section at each y level
        (260, 330, height),
        (270, 335, int(height * 0.95)),
        (275, 335, int(height * 0.90)),
        (280, 338, int(height * 0.85)),
        (290, 345, int(height * 0.80)),
        (310, 360, int(height * 0.76)),
        (330, 376, int(height * 0.73)),
        (345, 388, int(height * 0.70)),
        (355, 393, int(height * 0.68)),
        (363, 396, int(height * 0.66)),
        (368, 396, int(height * 0.64)),
        (370, 394, int(height * 0.62)),
        (370, 390, int(height * 0.60)),
        (368, 385, int(height * 0.58)),
        (365, 380, int(height * 0.56)),
        (362, 376, int(height * 0.54)),
        (360, 372, int(height * 0.52)),
        (358, 368, int(height * 0.50)),
        (357, 365, int(height * 0.48)),
        (356, 362, int(height * 0.46)),
    ]

    for i in range(len(road_segments) - 1):
        xl1, xr1, y1 = road_segments[i]
        xl2, xr2, y2 = road_segments[i + 1]
        sa.set_fill_color(road_color)
        sa.set_outline_color(road_color)
        sa._canvas.create_polygon(
            [xl1, y1, xr1, y1, xr2, y2, xl2, y2],
            fill=road_color, outline=road_edge, width=1
        )

    # ── Wooden fence (left side of road) ─────────────────────────────────────
    def draw_fence_post(fx, fy, post_h=18, post_w=4):
        sa.set_fill_color("#7a5c3a")
        sa.set_outline_color("#5a3c1a")
        sa.set_line_thickness(1)
        sa.fill_rectangle(fx - post_w // 2, fy - post_h, post_w, post_h)

    fence_posts_left = [
        (248, int(height * 0.80)),
        (240, int(height * 0.76)),
        (232, int(height * 0.73)),
        (224, int(height * 0.70)),
        (218, int(height * 0.68)),
        (215, int(height * 0.66)),
    ]
    fence_posts_right = [
        (348, int(height * 0.80)),
        (365, int(height * 0.76)),
        (380, int(height * 0.73)),
        (392, int(height * 0.70)),
        (398, int(height * 0.68)),
        (400, int(height * 0.66)),
    ]
    for fx, fy in fence_posts_left:
        draw_fence_post(fx, fy)
    for fx, fy in fence_posts_right:
        draw_fence_post(fx, fy)

    # Rails connecting posts
    sa.set_outline_color("#8a6c4a")
    sa.set_line_thickness(2)
    for i in range(len(fence_posts_left) - 1):
        x1, y1 = fence_posts_left[i]
        x2, y2 = fence_posts_left[i + 1]
        sa.draw_line(x1, y1 - 12, x2, y2 - 12)
        sa.draw_line(x1, y1 - 6, x2, y2 - 6)
    for i in range(len(fence_posts_right) - 1):
        x1, y1 = fence_posts_right[i]
        x2, y2 = fence_posts_right[i + 1]
        sa.draw_line(x1, y1 - 12, x2, y2 - 12)
        sa.draw_line(x1, y1 - 6, x2, y2 - 6)
    sa.set_line_thickness(1)

    # ── Sunlight shimmer on meadow ────────────────────────────────────────────
    shimmer_x = sa.oscillate_frames(350, 460, 240, frame)
    shimmer_y = int(height * 0.72)
    sa.set_fill_color("#ffffcc")
    sa.set_outline_color("#ffffcc")
    # Soft glow ellipse (multiple semi-transparent layers approximated by layering)
    for r in range(30, 5, -8):
        alpha_color = sa.hls_to_rgb_hex(0.16, 0.93, 0.80)
        sa.set_fill_color(alpha_color)
        sa.set_outline_color(alpha_color)
        sa.fill_circle(int(shimmer_x), shimmer_y, r)


sa.start(draw_frame, width=800, height=600)
