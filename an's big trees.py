import simple_animation as sa

def draw_pine(x, y, height):
    """Draws a pine/spruce tree. x, y is the base center of the trunk."""
    trunk_w = max(4, height // 10)
    # Trunk
    sa.set_fill_color("#5c3d1e")
    sa.set_outline_color("#5c3d1e")
    sa.fill_rectangle(x - trunk_w // 2, y - height // 5, trunk_w, height // 5)
    # Three layered triangles
    sa.set_fill_color("#2d5a27")
    sa.set_outline_color("#2d5a27")
    for i in range(3):
        frac = i / 3
        layer_y  = y - int(height * (0.20 + frac * 0.55))
        layer_w  = int(height * (0.45 - frac * 0.12))
        overlap  = int(height * 0.10)
        tip_y    = layer_y - int(height * 0.28)
        sa.fill_triangle(x - layer_w, layer_y + overlap,
                         x + layer_w, layer_y + overlap,
                         x, tip_y)

def draw_round_tree(x, y, height):
    """Draws a round/deciduous tree. x, y is the base center of the trunk."""
    trunk_w  = max(6, height // 8)
    trunk_h  = height // 3
    canopy_r = height // 2
    # Trunk
    sa.set_fill_color("#6b4423")
    sa.set_outline_color("#6b4423")
    sa.fill_rectangle(x - trunk_w // 2, y - trunk_h, trunk_w, trunk_h)
    # Round canopy — three overlapping circles for a natural look
    canopy_cx = x
    canopy_cy = y - trunk_h - int(canopy_r * 0.7)
    sa.set_fill_color("#3a7d35")
    sa.set_outline_color("#3a7d35")
    sa.fill_circle(canopy_cx - int(canopy_r * 0.35), canopy_cy + int(canopy_r * 0.15), int(canopy_r * 0.75))
    sa.fill_circle(canopy_cx + int(canopy_r * 0.35), canopy_cy + int(canopy_r * 0.15), int(canopy_r * 0.75))
    sa.fill_circle(canopy_cx, canopy_cy - int(canopy_r * 0.10), int(canopy_r * 0.85))
    # Highlight circle for depth
    sa.set_fill_color("#4e9e47")
    sa.set_outline_color("#4e9e47")
    sa.fill_circle(canopy_cx - int(canopy_r * 0.15), canopy_cy - int(canopy_r * 0.20), int(canopy_r * 0.45))
    
def draw_frame(frame, elapsed, width, height):
    sa.fill_background("#87ceeb")
    sa.set_fill_color("#4a7c3f")
    sa.set_outline_color("#4a7c3f")
    sa.fill_rectangle(0, height - 80, width, 80)

    draw_pine(200, height - 80, 180)
    draw_pine(350, height - 80, 130)
    draw_round_tree(520, height - 80, 160)
    draw_round_tree(670, height - 80, 120)

sa.start(draw_frame, width=800, height=500)
#Attribution: This code was made by Gemini
