import turtle

window = turtle.Screen()
bob = turtle.Turtle()

bob.shape("turtle")
window.bgcolor("green")
bob.color("blue")

for i in range(12):
    bob.up()
    bob.forward(100)
    bob.down()
    bob.forward(10)
    bob.up()
    bob.forward(10)
    bob.stamp()
    bob.backward(120)
    bob.right(360 / 12)

window.exitonclick()