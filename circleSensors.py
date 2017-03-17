from space2D import space2D
from phonoSensors import phonoSensors
import math

class circleSensors(phonoSensors):
    def __init__(self, radius, sensors, center = (0, 0)):
        phonoSensors.__init__(self, space2D())
        centerX = center[0]
        centerY = center[1]
        angleStep = math.pi*2/sensors
        for i in range(0, sensors):
            angle = angleStep * i
            x = centerX + math.sin(angle)*radius
            y = centerY + math.cos(angle)*radius
            self.add( (x, y) )
