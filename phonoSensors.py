import math
import random

class phonoSensors:
    def __init__(self, space = None):
        self.sensors = []
        self.space = space
        
    def add(self, sensorPoint):
        self.sensors.append( sensorPoint )
    
    def idealReadings(self, soundSpaceTimePoint):
        space = self.space
        soundPoint = space.extractPoint( soundSpaceTimePoint )
        soundTime = space.extractTime( soundSpaceTimePoint )
        readings = []
        for sensor in self.sensors:
            sensorDistance = space.distance(sensor, soundPoint)
            timeToSensor = sensorDistance / phonoSensors.SPEED_OF_SOUND
            readings.append( space.pointTime(sensor, soundTime + timeToSensor))
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
