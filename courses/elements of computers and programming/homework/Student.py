# File: Student.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: Feb 27, 2023
# Description of Program: Create a program to output the exam grades for a given student

class Student:
    def __init__(self, name, exam1 = None, exam2 = None):
        self.name = name
        self.exam1 = exam1
        self.exam2 = exam2

    def getName(self):
        return self.name
    
    def getExam1Grade(self):
        if (self.exam1 != None):
            return self.exam1
    
    def setExam1Grade(self, exam1):
        self.exam1 = exam1

    def getExam2Grade(self):
        if (self.exam2 != None):
            return self.exam2 
    
    def setExam2Grade(self, exam2):
        self.exam2 = exam2
    
    def getAverage(self):
        if (self.exam1 != None) and (self.exam2 != None):
            average = (self.exam1 + self.exam2) / 2
            return average
        else:
            return "Some exam grades not available."

    def __str__(self):
        if (self.exam1 != None) and (self.exam2 != None):
            return "Student: " +  self.name + "\n  Exam1: " + str(self.exam1) + "\n  Exam2: " + str(self.exam2)
        elif (self.exam1 == None) and (self.exam2 != None):
            return "Student: " +  self.name + "\n  Exam1: " + "None" + "\n  Exam2: " + str(self.exam2)
        elif (self.exam1 != None) and (self.exam2 == None):
            return "Student: " +  self.name + "\n  Exam1: " + str(self.exam1) + "\n  Exam2: " + "None"
        elif (self.exam1 == None) and (self.exam2 == None):
            return "Student: " +  self.name + "\n  Exam1: " + "None" + "\n  Exam2: " + "None"