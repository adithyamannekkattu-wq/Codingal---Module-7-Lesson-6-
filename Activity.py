import turtle

wn=turtle.Screen()
wn.bgcolor("black")

pen=turtle.Turtle()
pen.hideturtle
turtle.speed(0)

colors=["red", "green", "violet", "orange", "yellow"]
for i in range(80):
    turtle.pendown()
    turtle.color(colors[i%len(colors)])
    turtle.forward(i*2)
    turtle.right(90)


turtle.penup()
turtle.goto(100, 150)
turtle.pendown()

for i in range(3):
    turtle.color("red")
    turtle.forward(120)
    turtle.left(120)

for i in range(3):
    turtle.color("red")
    turtle.forward(120)
    turtle.right(120)




'''
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

for i in range(4):
    turtle.color("red")
    turtle.forward(80)
    turtle.right(90)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

for i in range(4):
    turtle.color("green")
    turtle.circle(100)'''


turtle.done()

