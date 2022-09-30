import turtle

screen = turtle.getscreen()
t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(10)

# Declares constants to use in the code below.
STEP = 1
ROTATIONAL_STEP = 5


def forward():
    """Moves the turtle forward."""
    t1.forward(STEP)


def back():
    """Moves the turtle backwards"""
    t1.backward(STEP)


def rotate_right():
    """Rotates the turtle right"""
    t1.right(ROTATIONAL_STEP)


def rotate_left():
    """Rotates the turtle left"""
    t1.left(ROTATIONAL_STEP)


# This code connects a key pressed to a function in the code.
# as soon as the key is pressed, the function is called.

# pressing the "w" key triggers a call to the forward() function.
screen.onkeypress(forward, "w")
screen.onkeypress(rotate_right, "d")
screen.onkeypress(rotate_left, "a")
screen.onkeypress(back, "s")

# This tells the turtle screen to listen for events from the user.
screen.listen()

turtle.mainloop()
