import turtle

window = turtle.Screen()
bob = turtle.Turtle()

for side in range(8):
    bob.forward(20)
    bob.left(45)

window.exitonclick()