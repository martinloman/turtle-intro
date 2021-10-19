import turtle

t1 = turtle.Turtle()
t1.speed(10)
# t1.shape("turtle")

# Prints three circles as the body of the snowman.
t1.circle(100)
t1.penup()  # no drawing while moving.
t1.goto(0, 200)
t1.pendown()  # activate drawing again.
t1.circle(60)
t1.penup()
t1.goto(0, 320)
t1.pendown()
t1.circle(30)

# Print eyes
t1.penup()
pos = t1.pos()  # The position at the bottom of the top circle
# a position up to the left from current position
rightEyePos = pos + (-10, 40)
t1.goto(rightEyePos)  # move to the position
t1.dot(5)  # draw an eye
leftEyePos = pos + (10, 40)
t1.goto(leftEyePos)
t1.dot(5)

turtle.mainloop()
