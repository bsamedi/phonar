from point.py import point

class point2D(point):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def zero():
        return point2D(0.0, 0.0)
    
    def squareDistanceTo(self, p):
        return (self.x - p.x) ** 2 + (self.y - p.y) ** 2
    
    def distanceTo(self, p):
        return math.sqrt( float( self.squareDistanceTo(p) ) )

    def tuple(self):
        return (self.x, self.y)
        