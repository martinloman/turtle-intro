import turtle

screen = turtle.getscreen()

t1 = turtle.Turtle()
t1.speed(10)


def move(x, y):
    # t1.penup()
    t1.goto(x, y)
    # t1.pendown()


screen.onclick(move)

turtle.mainloop()
