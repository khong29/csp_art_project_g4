import turtle

def draw_pine(t, x, y, height):
    # Trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#5c3d1e")
    t.begin_fill()
    t.goto(x - 5, y)
    t.goto(x - 5, y + height * 0.2)
    t.goto(x + 5, y + height * 0.2)
    t.goto(x + 5, y)
    t.goto(x, y)
    t.end_fill()

    # Three triangle layers
    t.color("#2d5a27")
    for i in range(3):
        frac = i / 3
        base_y = y + height * (0.15 + frac * 0.5)
        tip_y  = y + height * (0.45 + frac * 0.5)
        half_w = height * (0.35 - frac * 0.08)
        t.begin_fill()
        t.penup(); t.goto(x - half_w, base_y)
        t.pendown()
        t.goto(x + half_w, base_y)
        t.goto(x, tip_y)
        t.goto(x - half_w, base_y)
        t.end_fill()

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#87ceeb")

draw_pine(t, -100, -150, 200)
draw_pine(t,    0, -150, 250)
draw_pine(t,  150, -150, 180)

turtle.done()
