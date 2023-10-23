# File: Project2.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: March 18, 2023
# Description of Program: Create a program to simulate driving a simple toy car around a grid using class attributes/methods and functions outside the class

# Set constants
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class ToyCar:
    def __init__(self, x = 0, y = 0, d = EAST):
        self.__x = x
        self.__y = y
        self.__d = d
        if self.__d % 90 != 0 or self.__d > 270:
            print("ERROR: Illegal direction entered.")

    def __str__(self):
        if self.__d == 0:
            direction = "East"
        elif self.__d == 90:
            direction = "North"
        elif self.__d == 180:
            direction = "West"
        elif self.__d == 270:
            direction = "South"
        return "Your car is at location (" + str(self.__x) + ", " + str(self.__y) + "), " + "heading " + direction
    
    def setDir(self, n):
        if n % 90 != 0 or n > 270:
            print("ERROR: Illegal direction entered.")
            return
        
        self.__d = n
        if self.__d == 0:
            direction = "East"
        elif self.__d == 90:
            direction = "North"
        elif self.__d == 180:
            direction = "West"
        elif self.__d == 270:
            direction = "South"

        print("DEBUG: setting direction " + direction)

    def getDir(self):
        return int(self.__d)

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def turnLeft(self):
        if self.__d == 270:
            self.__d = 0
        else:
            self.__d += 90
        self.debugTurning()

    def turnRight(self):
        if self.__d == 0:
            self.__d = 270
        else:
            self.__d -= 90
        self.debugTurning()

    def debugTurning(self):
        if self.__d == 0:
            direction = "East"
        elif self.__d == 90:
            direction = "North"
        elif self.__d == 180:
            direction = "West"
        elif self.__d == 270:
            direction = "South"
        print("DEBUG: turning " + direction)

    def forward(self, n):
        if n < 0:
            print("Error: Illegal distance entered.")
        else:
            if self.__d == 0:
                self.__x += n
                print("DEBUG: moving forward " + str(n))
            elif self.__d == 90:
                self.__y += n
                print("DEBUG: moving forward " + str(n))
            elif self.__d == 180:
                self.__x -= n
                print("DEBUG: moving forward " + str(n))
            elif self.__d == 270:
                self.__y -= n
                print("DEBUG: moving forward " + str(n))

def randomDrive(car, n):
    import random
    count = 0
    if n < 0:
        print("ERROR: Illegal value entered.")
        return
    
    while n > count:
        randomDir = random.randint(1, 3)
        randomNum = random.randint(1, 100)
        if randomDir == 1:
            car.turnLeft()
        elif randomDir == 2:
            car.turnRight()
        elif randomDir == 3:
            print("DEBUG: remaining in current direction")
        car.forward(randomNum)
        count += 1

def goto(car, x, y):
    if car.getX() != x:
        distanceX = abs(x - car.getX())
        if x > 0 and car.getX() < 0:
            if car.getDir() != 0:
                car.setDir(0)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x > 0 and (abs(x) > abs(car.getX())):
            if car.getDir() != 0:
                car.setDir(0)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x > 0 and (abs(x) < abs(car.getX())):
            if car.getDir() != 180:
                car.setDir(180)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x < 0 and car.getX() > 0:
            if car.getDir != 180:
                car.setDir(180)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x < 0 and (abs(x) > abs(car.getX())):
            if car.getDir() != 180:
                car.setDir(180)
                car.forward(distanceX)
            else: 
                car.forward(distanceX)
        elif x < 0 and (abs(x) < abs(car.getX())):
            if car.getDir() != 0:
                car.setDir(0)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x == 0 and car.getX() < 0:
            if car.getDir != 0:
                car.setDir(0)
                car.forward(distanceX)
            else:
                car.forward(distanceX)
        elif x == 0 and car.getX() > 0:
            if car.getDir != 180:
                car.setDir(180)
                car.forward(distanceX)
            else:
                car.forward(distanceX)        
    if car.getY() != y:
        distanceY = abs(y - car.getY())
        if y > 0 and car.getY() < 0:
            if car.getDir() != 90:
                car.setDir(90)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y > 0 and (abs(y) > abs(car.getY())):
            if car.getDir() != 90:
                car.setDir(90)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y > 0 and (abs(y) < abs(car.getY())):
            if car.getDir() != 270:
                car.setDir(270)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y < 0 and car.getY() > 0:
            if car.getDir() != 270:
                car.setDir(270)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y < 0 and (abs(y) > abs(car.getY())):
            if car.getDir() != 270:
                car.setDir(270)
                car.forward(distanceY)
            else: 
                car.forward(distanceY)
        elif y < 0 and (abs(y) < abs(car.getY())):
            if car.getDir() != 90:
                car.setDir(90)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y == 0 and car.getY() < 0:
            if car.getDir != 90:
                car.setDir(90)
                car.forward(distanceY)
            else:
                car.forward(distanceY)
        elif y == 0 and car.getY() > 0:
            if car.getDir != 270:
                car.setDir(270)
                car.forward(distanceY)
            else:
                car.forward(distanceY)       
    
def gasStation():
    import random
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    print("Located gas station at (" + str(x) + ", " + str(y) + ")")
    return x, y

def gasUp(car):
    x, y = gasStation()
    goto(car, x, y)