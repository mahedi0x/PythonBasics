import turtle

turtle.color("orange")
for i in range(30):
    turtle.speed(3)
    turtle.forward(10+i*5)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(45)



turtle.exitonclick()