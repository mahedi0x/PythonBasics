import turtle
# turtle.forward(100)
# turtle.exitonclick()

turtle.shape("turtle")
"""
turtle.speed(3)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)

turtle.right(90)
turtle.backward(100)
turtle.left(90)
turtle.backward(100)

turtle.exitonclick()
"""



# -----------------draw line ---------
"""
for i in range(10):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.exitonclick()
"""

"""
import turtle

t = turtle.Turtle()

for _ in range(36):
    t.speed(7)
    for _ in range(5):
        t.forward(200)
        t.right(144)
    t.right(10)

turtle.done()
"""

"""
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()
"""

turtle.color("black")
turtle.speed(10)

for i in range(100):
    turtle.forward(10 + i * 5)
    turtle.left(120)
turtle.exitonclick()
