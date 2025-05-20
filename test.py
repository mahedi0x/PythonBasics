import turtle

"""
turtle.color("green")
for i in range(30):
    turtle.speed(3)
    turtle.forward(20 + i * 5)
    turtle.left(90)
    if i == 29:
        turtle.left(45)
        turtle.color("red")
        turtle.forward(40 + i * 3)

turtle.exitonclick()
"""

t = turtle.Turtle()

for _ in range(36):
    t.speed(7)
    for _ in range(5):
        t.forward(200)
        t.right(144)
        t.color("green")

    t.color("red")
    t.right(10)

turtle.done()
