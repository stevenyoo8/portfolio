# turtles are python objects (part of Turtle class)
# moves along coordinates

### attributes of turtle class
# Position: current x and y coordinates (units are pixels)
# Heading: direction turte is heading; angle in degrees
# color: color of pen
# width: width of line
# down: boolean indiciating whether turtle's tail is down. Tail down: draw. Tail up: don't draw

import turtle
def drawSquare(ttl, x, y, length):
    ttl.penup() # raise pen
    ttl.goto(x, y) # move to position
    ttl.setheading(0) # point turtle east
    ttl.pendown() # lower pwn (start draw)
    for count in range(4):
        ttl.forward(length) # move forward length
        ttl.right(90) # turn right 90 degrees
    ttl.penup() # raise pen (stop draw)

# def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
#     ttl.penup()
#     ttl.goto(x1, y1)
#     ttl.pendown()
#     ttl.goto(x2, y2)
#     ttl.goto(x3, y3)
#     ttl.goto(x1, y1)
#     ttl.penup()

# Tom = turtle.Turtle()
# Tom.speed(10)
# Tom.pensize(3)
# Tom.pencolor(1, 0, 0) # pen.color(R, G, B). Set color to red
# drawTriangle(Tom, 0, 0, 50, 100, 100, 0)
# Tom.pencolor(0, 1, 0) # set pen to green
# drawTriangle(Tom, 0, 0, 50, -100, 100, 0)
# Tom.hideturtle()

# turtle.done()

# ----------------------------------------------------------------------------------------------------

### defining colors using RGB
# each value can be a value between 0 and 255

### circles
# t.circle(r, ext, step) : radius r, ext (arc), step (number of segments)
# t.dot(d, color) : draw filled circle with diameter r and color color

# def centeredCircle(ttl, r, x, y):
#     ttl.up()
#     angle = ttl.heading()
#     ttl.setheading(0)
#     ttl.goto(x, y - r)
#     ttl.down()
#     ttl.circle(r)
#     ttl.up()
#     ttl.setheading(angle)
    
# t = turtle.Turtle()
# t.speed(10)
# t.pensize(3)
# t.screen.colormode(255)
# t.pencolor(255, 125, 25)
# centeredCircle(t, 50, 0, 0)
# turtle.done()

# def drawSomeCircles(ttl):
#     ttl.speed(10)
#     ttl.pensize(3) # line is 3 pixels
#     ttl.up()
#     ttl.home() # go to (0 , 0)
#     ttl.down()
#     ttl.pencolor("Green")
#     ttl.circle(25) # rad . 25 pixels
#     ttl.up()
#     ttl.goto(0, 0)
#     ttl.pencolor("Red")
#     ttl.down()
#     ttl.circle(50 ,180) # arc 180 deg .
#     ttl.up()
#     ttl.goto(0, 0)
#     ttl.pencolor("Blue")
#     ttl.down()
#     ttl.circle(75, 360, 8) # octogon
#     ttl.up()

# t = turtle.Turtle()
# drawSomeCircles(t)
# turtle.done()

# def tangentCircles(ttl):
#     """ Print 10 tangent circles . """
#     r = 10 # initial radius
#     n = 10 # count of circles
#     for i in range (1 , n + 1, 1):
#         ttl.circle(r * i)

# def concentricCircles(ttl):
#     """ Print 10 concentric circles . """
#     r = 10 # initial radius
#     for i in range(10):
#         ttl.circle(r * i)
#         ttl.up()
#         ttl.sety((r * i) *(-1))
#         ttl.down()

# Ben = turtle.Turtle()
# Ben.up(); Ben.goto(0, 150)
# Ben.down(); Ben.pencolor("Blue")
# tangentCircles(Ben)
# Ben.up(); Ben.goto(0, -150)
# Ben.down(); Ben.pencolor("Red")
# concentricCircles(Ben)

# turtle.done()

def maybeFillSquare(ttl, x, y, lngth, fill, color):
    """ Boolean parameter fill says whether to fill . """
    if fill:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawSquare(ttl, x, y, lngth)
        ttl.end_fill()
    else:
        drawSquare(ttl, x, y, lngth)

def drawChessboard(ttl, x, y, squaresize):
    """ Draw a teal and white chessboard . """
    fill = True
    for j in range(8):
        for i in range(8):
            x1 = x + i * squaresize
            y1 = y - j * squaresize
            maybeFillSquare(ttl, x1, y1 , squaresize, fill, "teal")
            fill = not fill
        fill = not fill

Matt = turtle.Turtle()
drawChessboard(Matt, 0, 0, 20)

Matt.speed(10)
turtle.done()