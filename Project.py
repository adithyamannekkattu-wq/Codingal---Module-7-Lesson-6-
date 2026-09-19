import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")

artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(2)


def petal(size, colour):
    artist.color(colour)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size, 60)
        artist.left(120)

    artist.end_fill()



colours = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

for i in range(36):
    petal(180, colours[i % len(colours)])
    artist.right(10)


artist.penup()
artist.goto(0, -35)
artist.pendown()

artist.color("white")
artist.begin_fill()
artist.circle(50)
artist.end_fill()


turtle.done()