# File: LiberiaFlag.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: April 11, 2023
# Description of Program: Draw the flag of Liberia using turtle graphics
import turtle

# color values
myBlue = (0, 32, 91)
myRed = (191, 13, 62)
myWhite = (255, 255, 255)

# setup turtle
leo = turtle.Turtle() # name turtle
leo.speed(10) # set speed
leo.screen.colormode(255) # color mode

def main():
# initialize position and direction
    leo.penup()
    leo.goto(-110, -209)
    leo.pendown()
    leo.setheading(90)

    bottomStripes()

# bottom red and white stripes
def bottomStripes():
    countFull = 1
    while countFull < 7:
        if countFull % 2 == 0:
            leo.fillcolor(myWhite) # white color
        else:
            leo.fillcolor(myRed) # red color

        leo.begin_fill()
        leo.forward(20)
        leo.setheading(0) 
        leo.forward(418) 
        leo.setheading(270)
        leo.forward(20)
        leo.setheading(180)
        leo.forward(418)
        leo.setheading(90)
        leo.forward(20)
        leo.end_fill()

        countFull += 1

    topStripes()

def topStripes():
    # top red and white stripes
    leo.goto(-10, -89)
    leo.setheading(90)
    countPart = 1
    while countPart < 6:
        if countPart % 2 == 0:
            leo.fillcolor(myWhite)
        else:
            leo.fillcolor(myRed)
        
        leo.begin_fill()
        leo.forward(20)
        leo.setheading(0)
        leo.forward(318)
        leo.setheading(270)
        leo.forward(20)
        leo.setheading(180)
        leo.forward(318)
        leo.setheading(90)
        leo.forward(20)
        leo.end_fill()
        
        countPart += 1
        
    leo.penup()

    blueBox()

def blueBox():
    # create blue box
    leo.fillcolor(myBlue)
    leo.begin_fill()
    leo.goto(-110, -89)
    leo.setheading(90)
    for count in range(4):
            leo.forward(100) # move forward length
            leo.right(90)
    leo.end_fill()

    drawStar()

def drawStar():
    # create star in blue box
    leo.goto(-69, -30)
    leo.fillcolor(myWhite)
    leo.begin_fill()
    leo.setheading(72)
    leo.forward(30)
    leo.setheading(288)
    leo.forward(30)
    leo.setheading(0)
    leo.forward(30)
    leo.setheading(216)
    leo.forward(30)
    leo.setheading(288)
    leo.forward(30)
    leo.setheading(144)
    leo.forward(30)
    leo.setheading(216)
    leo.forward(30)
    leo.setheading(72)
    leo.forward(30)
    leo.setheading(144)
    leo.forward(30)
    leo.setheading(0)
    leo.forward(30)
    leo.end_fill()
    leo.hideturtle()

    turtle.done()

main()