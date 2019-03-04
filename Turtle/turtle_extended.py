import turtle

window = turtle.Screen()
bob = turtle.Turtle()

background = input("What background colour do you like? ")
pen_clr = input("What color do you want to turtle to be? ")
width = int(input("How wide will the line drawn be? "))

window.bgcolor(background)
bob.color(pen_clr)
bob.pensize(width)

bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(50)
bob.right(180)
bob.forward(100)

window.exitonclick()