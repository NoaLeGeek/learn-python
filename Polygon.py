import turtle


# Draws a square depending on length and pen's size
def draw_square(length: int = 50, speed: int = 1, pensize: int = 1):
    print("e")
    draw_polygon(length, 4, speed, pensize)


# Draws a rectangle depending on length, width and pen's size
def draw_rectangle(length: int = 50, width: int = 75, speed: int = 1, pensize: int = 1):
    turtle.speed(speed)
    turtle.pensize(pensize)
    for x in range(0, 2):
        turtle.right(90)
        turtle.back(length)
        turtle.right(90)
        turtle.back(width)
    turtle.done()


# Draws a polygon depending on the length, the sides and pen's size
def draw_polygon(length: int = 50, sides: int = 8, speed: int = 1, pensize: int = 1):
    turtle.speed(speed)
    turtle.pensize(pensize)
    for x in range(sides):
        turtle.right(360 / sides)
        turtle.back(length)
