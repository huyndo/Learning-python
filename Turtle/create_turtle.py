import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
wn.bgcolor("lightgreen")    # set the window background color
alex = turtle.Turtle()      # create a turtle named alex
alex.color("blue")          # make alex blue
alex.pensize(3)             # set the width of her pen
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.exitonclick()            # wait for a user click on the canvas
