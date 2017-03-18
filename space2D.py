from space import space
from math import sqrt

class space2D(space):
    def zero(self):
        return (0.0, 0.0)

    def squareDistance(self, p1, p2):
        p1x, p1y = p1[0], p1[1]
        p2x, p2y = p2[0], p2[1]
        return (p1x - p2x) ** 2 + (p1y - p2y) ** 2

    def distance(self, p1, p2):
        return sqrt( self.squareDistance(p1, p2) )

    def extractPoint(self, pointTime):
        return (pointTime[0], pointTime[1])

    def extractTime(self, pointTime):
        return pointTime[2]

    def pointTime(self, point, time):
        return (point[0], point[1], time)
