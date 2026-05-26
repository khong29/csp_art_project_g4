import simple_animation as sa

def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    
    sa.fill_background("white") # Clear the background for this frame
   
     # Example Animation: A moving circle
    x_ball = sa.loop_motion(0, width, 5.0, frame_number) # x coordinate
    
    sa.set_fill_color("red")
    
    sa.fill_circle(x_ball, height / 2, 40)
    
    # Example Animation: A moving fish (a little more complicated) with changing colors
    
    repeat_fish = 300 # number of frames to repeat
    color_hue = (frame_number % repeat_fish) / repeat_fish
    fish_color = sa.hls_to_rgb_hex(color_hue, 0.5, 1.0)
    
    x_fish = sa.oscillate_frames(0, width-50, repeat_fish, frame_number)
    y_fish = sa.oscillate_motion(height//2, height//2 +100, 0.15, frame_number)
    
    if (frame_number % repeat_fish)  < (repeat_fish // 2):
        sa.draw_fish(x_fish, y_fish, 50, fish_color, "right")
    else:
        sa.draw_fish(x_fish, y_fish, 50, fish_color, "left")
    

    
    
    # Draw the information text
    sa.set_fill_color("black")
    sa.draw_text(40, 50, f"Frame number: {frame_number}")
    sa.draw_text(40, 80, f"Elapsed Time: {elapsed_seconds:.1f} seconds")
    sa.draw_text(40, 110, f"Mouse x: {sa.get_mouse_x()}")
    sa.draw_text(40, 140, f"Mouse y: {sa.get_mouse_y()}")

if __name__ == "__main__":
    # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)
    

