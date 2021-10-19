import turtle

screen = turtle.getscreen()

t1 = turtle.Turtle()
t1.speed(10)

STEP = 1
ROTATIONAL_STEP = 5


def forward():
    t1.forward(STEP)


def back():
    t1.backward(STEP)


def rotate_right():
    t1.right(ROTATIONAL_STEP)


def rotate_left():
    t1.left(ROTATIONAL_STEP)


screen.onkeypress(forward, "w")
screen.onkeypress(rotate_right, "d")
screen.onkeypress(rotate_left, "a")
screen.onkeypress(back, "s")

screen.listen()

turtle.mainloop()
