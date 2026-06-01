import simple_animation as sa

def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""

    sa.fill_background("white")


    sa.draw_gradient_sky(800, 600)

    sa.draw_snowy_mountain(-200, 200, 300, 250, "#5a6b7c")
    sa.draw_snowy_mountain(0, 200, 300, 250, "#5a6b7c")
    sa.draw_snowy_mountain(200, 200, 300, 250, "#5a6b7c")
    sa.draw_snowy_mountain(400, 200, 300, 250, "#5a6b7c")
    sa.draw_snowy_mountain(600, 200, 300, 250, "#5a6b7c")

    sa.draw_grass_field(800, 600)


    sa.draw_pine(80, height - 80, 180)
    sa.draw_pine(180, height - 80, 140)


    sa.draw_round_tree(320, height - 80, 160)
    sa.draw_round_tree(420, height - 80, 120)


    sa.draw_house(600, int(height * 0.80), 1)


sa.start(draw_frame)
    