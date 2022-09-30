import turtle

t1 = turtle.Turtle()  # Creates a turtle we can control.
t1.speed(10)  # Sets speed 1-10 but 0 is fastest...
t1.shape("turtle")

t1.forward(100)  # moves the turtle forward
t1.right(90)  # turns the turtle forward
t1.forward(100)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(100)

turtle.mainloop()  # Waits for the user to close the window.
