import turtle
import random


turtle.colormode(255)  # So we can use RGB color for the turtle.
screen = turtle.getscreen()
screen.bgcolor(0, 0, 0)

t1 = turtle.Turtle()
t1.speed(0)


def random_color(t: turtle.Turtle):
    '''Sets a random, bright, color of a turle.'''
    t.color(random.randint(128, 200),
            random.randint(128, 200),
            random.randint(128, 200))


# We create a loop that draws a circle and turns the turtle a little bit.
i = 0
while i < 360:
    random_color(t1)
    t1.circle(150)
    t1.right(7)
    i += 1


turtle.mainloop()  # This leaves the window open until the user closes it.
