import turtle
import random


turtle.colormode(255)  # So we can use RGB color for the turtle.
screen = turtle.getscreen()
screen.bgcolor(0, 0, 0)  # Sets black background.

t1 = turtle.Turtle()
t1.speed(0)


def set_random_color(t: turtle.Turtle):
    '''Sets a random, bright, color of a turtle.'''
    t.color(random.randint(128, 200),
            random.randint(128, 200),
            random.randint(128, 200))


# declaring two constants to use in the code below.
# constants are named using ALL_CAPS.
TURN = 7
CIRCLE_SIZE = 150

# We create a loop that draws a circle and turns the turtle a little bit.
i = 0
while i < 360:
    set_random_color(t1)  # set random color
    t1.circle(CIRCLE_SIZE)  # draw a circle
    t1.right(TURN)  # turn the turtle before the next iteration of the loop
    i += 1


turtle.mainloop()  # This leaves the window open until the user closes it.
