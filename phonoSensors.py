import math
import random

def distance(point1, point2):
    return math.sqrt( float(point1['x']-point2['x'])**2 + (point1['y']-point2['y'])**2 )

class phonoSensors:
    def __init__(self):
        self.sensors = []
        
    def add(self, x, y):
        self.sensors.append( {'x':x, 'y':y} )
    
    def idealReadings(self, soundX, soundY, soundT):
        readings = []
        for sensor in self.sensors:
            sensorDistance = distance( {'x':sensor['x'], 'y':sensor['y']}, {'x':soundX, 'y':soundY} )
            sensorTime = sensorDistance / phonoSensors.SPEED_OF_SOUND
            readings.append({'x':sensor['x'], 'y':sensor['y'], 't':sensorTime+soundT})
        return readings
    
    # def detectSource(self, readings, numSounds):
        # minT = min(map(lambda s: s['t'], readings))
        # maxT = max(map(lambda s: s['t'], readings))
        # minX = min(map(lambda s: s['x'], readings))
        # maxX = max(map(lambda s: s['x'], readings))
        # minY = min(map(lambda s: s['y'], readings))
        # maxY = max(map(lambda s: s['y'], readings))
        # sounds = []
        # for i in range(numSounds):
            # randomX = minX + (maxX-minX)*random.random()
            # randomY = minY + (maxY-minY)*random.random()
            # randomT = minT - (maxT-minT)*random.random()
            # sounds.append((randomX, randomY, randomT))
        
        # for i in range(10):
            
        
        # return sounds
    
    SPEED_OF_SOUND=0.34029 # km per second

class circleSensors(phonoSensors):
    def __init__(self, radius, sensors, center={'x':0,'y':0}):
        phonoSensors.__init__(self)
        angleStep = math.pi*2/sensors
        for i in range(0, sensors):
            angle = angleStep * i
            x = center['x'] + math.sin(angle)*radius
            y = center['y'] + math.cos(angle)*radius
            self.add(x=x, y=y)
