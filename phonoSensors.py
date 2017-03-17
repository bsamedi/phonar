import random

class phonoSensors:
    SPEED_OF_SOUND=0.34029 # km per second

    def __init__(self, space = None):
        self.sensors = []
        self.space = space
        
    def add(self, sensorPoint):
        self.sensors.append( sensorPoint )
    
    def idealReadings(self, soundPointTime):
        space = self.space
        soundPoint = space.extractPoint( soundPointTime )
        soundTime = space.extractTime( soundPointTime )
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
