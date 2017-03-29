from space import Space, Point, PointTime
from math import sqrt
from collections import namedtuple

class Point3D( namedtuple('Point3D', ['x','y','z']), Point ):
    def distance(self, p):
        return sqrt((self.x-p.x)**2 + (self.y-p.y)**2 + (self.z-p.z)**2)

    def addTime(self, t):
        return PointTime3D(self.x, self.y, self.z, t)

class PointTime3D( namedtuple('PointTime3D', ['x','y','z','t']), PointTime ):
    def point(self):
        return Point3D(self.x, self.y, self.z)

class Space3D(Space):
    Point = Point3D
    PointTime = PointTime3D
    
    def zero(self):
        return self.Point(0.0, 0.0, 0.0)
