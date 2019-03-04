import turtle

window = turtle.Screen()
bob = turtle.Turtle()

bob.left(40)

for i in range(5):
    bob.forward(100)
    bob.left(144)

window.exitonclick()