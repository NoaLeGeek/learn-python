import turtle


# Draws a square depending on length and pen's size
def square(length: int = 50, speed: int = 1, pensize: int = 1):
    rectangle(length, length, speed, pensize)


# Draws a rectangle depending on length, width and pen's size
def rectangle(length: int = 50, width: int = 75, speed: int = 1, pensize: int = 1):
    turtle.speed(speed)
    turtle.pensize(pensize)
    for x in range(0, 2):
        turtle.right(90)
        turtle.back(length)
        turtle.right(90)
        turtle.back(width)
    turtle.done()


# Draws a polygon depending on the length, the sides and pen's size
def polygon(length: int = 50, sides: int = 8, speed: int = 1, pensize: int = 1):
    turtle.speed(speed)
    turtle.pensize(pensize)
    for x in range(sides):
        turtle.right(360 / sides)
        turtle.back(length)
