import turtle

turtle.pensize(5)
turtle.color("red")
turtle.pendown()

for j in range(50,200,10):
    angle = 180 * (j - 2) / j

    for i in range(j):
        turtle.forward(10)
        turtle.left(180 - angle)
    turtle.right(90)
    turtle.forward(10)
turtle.done()
