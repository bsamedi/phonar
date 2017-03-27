from space import Space, Point, PointTime
from math import sqrt
from collections import namedtuple

class Point2D( namedtuple('Point2D', ['x','y']), Point ):
    def distance(self, p):
        return sqrt((self.x-p.x)**2 + (self.y-p.y)**2)

    def addTime(self, t):
        return PointTime2D(self.x, self.y, t)

class PointTime2D( namedtuple('PointTime2D', ['x','y','t']), PointTime ):
    def point(self):
        return Point2D(self.x, self.y)

class Space2D(Space):
    Point = Point2D
    PointTime = PointTime2D
    
    def zero(self):
        return self.Point(0.0, 0.0)
