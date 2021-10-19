import turtle

screen = turtle.getscreen()

t1 = turtle.Turtle()
t1.speed(10)
# t1.shape("turtle")

t1.circle(100)
t1.penup()  # no drawing while moving.
t1.goto(0, 200)
t1.pendown()  # activate drawing again.
t1.circle(60)
t1.penup()
t1.goto(0, 320)
t1.pendown()
t1.circle(30)

turtle.mainloop()
