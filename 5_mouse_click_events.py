import turtle
screen = turtle.getscreen()
t1 = turtle.Turtle()
t1.speed(10)


def move(x, y):
    """Moves a turtle to coordinates x and y."""
    # t1.penup()
    t1.goto(x, y)
    # t1.pendown()


# this tells the screen to trigger the move() function when a mouse
# button is clicked. The x and y coordinates will automatically
# be sent to that function.
screen.onclick(move)

turtle.mainloop()
