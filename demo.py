# Exempelkod som visar några egenskaper hos Pythons bibliotek Turtle
# Fullständig referens till biblioteket finns på
# https://docs.python.org/3/library/turtle.html


import turtle as t
import random as r
aTurtle = t.Turtle()    # Initierar en sköldpadda
bTurtle = t.Turtle()    # Initierar en till sköldpadda

# Funktion som sätter slumpad färg


def randomColor(turtle_to_colorize):
    R = r.random()  # Röd färggrad
    G = r.random()  # Grön färggrad
    B = r.random()  # Blå färggrad
    # Färgerna sätts med tre tal mellan 0 och 1
    turtle_to_colorize.color(R, G, B)


aTurtle.shape('turtle')  # Ge den formen av en sköldpadda
aTurtle.color('blue')   # Sätter en startfärg
aTurtle.width(10)       # Sätter en linjebredd
aTurtle.speed(5)        # Sätter en hastighet

aTurtle.forward(200)  # Flyttar sköldpaddan 200 steg framåt
aTurtle.left(90)     # Vrider sköldpaddan 90 grader
aTurtle.forward(100)  # Flyttar sköldpaddan framåt igen

# sköldpaddan kan även flyttas i ett mönster i en loop.
for i in range(15):
    randomColor(aTurtle)  # Här slumpas färgen fram
    aTurtle.forward(50)
    aTurtle.left(30)

# # Här tas den andra sköldpaddan i bruk
bTurtle.shape("turtle")
bTurtle.color("red")
bTurtle.penup()  # Nu kan sköldpaddan flyttas utan att en linje ritas
bTurtle.goto(-100, -50)  # Flytta sköldpaddan
bTurtle.pendown()  # Nu ritas linje igen vid förflyttning

bTurtle.fillcolor('red')  # Slutna figurer kan fyllas
bTurtle.width(5)
bTurtle.begin_fill()
for i in range(4):
    bTurtle.forward(100)  # Går framåt...
    bTurtle.right(90)    # ...och svänger höger fyra gånger
bTurtle.end_fill()

t.mainloop()  # Låt fönstret vara öppet tills användaren stänger det.

# Uppgifter att göra i separarata filer
# 1. Arbeta dig igenom projektet Turtle Race som finns på
#    https://projects.raspberrypi.org/en/projects/turtle-race

# 2. Skapa figurerna:
#   a. Rektangel
#   b. En liksidig triangel
#   c. En likbent triangel med en vinkel på 120 grader (fyll med valfri färg)
#   d. En valfri femhörning
#   e. En sexhörning där alla sidor är lika långa
#   f. En cirkel
#   g. En spiral
#   h. En stor rektangel som innehåller flera mindre rektanglar med olika färger

# 3. Go crazy, skapa roliga mönster.
