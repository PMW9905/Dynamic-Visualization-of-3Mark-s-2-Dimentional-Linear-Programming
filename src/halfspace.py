from manim import *
class Constraint:
    def __init__(self,c1,c2,b):
        self.c1 = c1
        self.c2 = c2
        self.b = b

    def getIntersection(self, vec2):
        if (self.c1*vec2.c2 - self.c2*vec2.c1) == 0:
            print("Error: The following constraints never intersect:")
            self.printVector()
            vec2.printVector()
            print("Stopping program.")
            quit()
        return ((self.c2*(-vec2.b) - vec2.c2*(-self.b)) / (self.c1*vec2.c2 - self.c2*vec2.c1),
                (self.c1*(-vec2.b) - vec2.c1*(-self.b)) / (self.c2*vec2.c1 - self.c1*vec2.c2))

    def isInHalfspace(self, point):
        return self.c1 * point[0] + self.c2 * point[1] <= self.b

    def printVector(self):
        print(str(self.c1) + "*x + " + str(self.c2) + "*y <= "+str(self.b))

    def getX(self,y):
        return (self.b - self.c2*y) / self.c1

    def getY(self,x):
        return (self.b - self.c1*x) / self.c2

    def isFacingLeft(self):
        return self.c1>0

    def isBoundToLeft(self, L):
        x = self.getIntersection(L)[0] + 10
        y = L.getY(x)
        return self.isInHalfspace((x,y))

class Objective:
    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
    def evaluatePoint(self,point):
        return self.c1*point[0] + self.c2*point[1]
    def printVector(self):
        print(str(self.c1) + "*x + " + str(self.c2) + "*y")