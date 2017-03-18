from phonoSensors2D import phonoSensors2D
import math

class circleSensors(phonoSensors2D):
    def __init__(self, radius, sensors, center = (0, 0)):
        phonoSensors2D.__init__(self)
        centerX = center[0]
        centerY = center[1]
        angleStep = math.pi*2/sensors
        for i in range(0, sensors):
            angle = angleStep * i
            x = centerX + math.sin(angle)*radius
            y = centerY + math.cos(angle)*radius
            self.add( (x, y) )
