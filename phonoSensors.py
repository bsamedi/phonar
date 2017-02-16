import math
def distance(point1, point2):
    return math.sqrt( float(point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

class phonoSensors:
    def __init__(self):
        self.sensors = []
        
    def add(self, x, y):
        self.sensors.append( {'x':x, 'y':y} )
    
    def idealReadings(self, soundX, soundY, soundT):
        readings = []
        for sensor in self.sensors:
            sensorDistance = distance( (sensor['x'], sensor['y']), (soundX, soundY) )
            sensorTime = sensorDistance / phonoSensors.SPEED_OF_SOUND
            readings.append({'x':sensor['x'], 'y':sensor['y'], 't':sensorTime+soundT})
        return readings
    
    SPEED_OF_SOUND=0.34029 # km per second