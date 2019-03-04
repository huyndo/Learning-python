import turtle

window = turtle.Screen()
bob = turtle.Turtle()

side = int(input("How many sides do you want? "))
length = int(input("How long will each side be? "))
outline_clr = input("What is the colour of the polygon? ")
fill_clr = input("What is the fill color of the polygon? ")

bob.color(fill_clr)
bob.pensize(2)

for move in range(length):
    for fill in range(side):
        bob.forward(move)
        bob.left(360 / side)
    bob.right(90)
    bob.forward(1)
    bob.left(90)

bob.color(outline_clr)

for fill in range(side):
    bob.forward(move)
    bob.left(360 / side)

window.exitonclick()
