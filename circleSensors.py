from phonoSensors2D import phonoSensors2D
import math

class circleSensors(phonoSensors2D):
    def __init__(self, radius, sensors, center = None):
        phonoSensors2D.__init__(self)

        if center == None:
            center = self.space.Point(0, 0)

        angleStep = math.pi*2/sensors
        for i in range(0, sensors):
            angle = angleStep * i
            x = center.x + math.sin(angle)*radius
            y = center.y + math.cos(angle)*radius
            self.add( self.space.Point(x, y) )
