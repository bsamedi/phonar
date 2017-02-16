class phonoSensors:
    def __init__(self):
        self.sensors = []
        
    def add(self, x, y):
        self.sensors.append( {x:x, y:y} )
    
    def idealReadings(self, soundX, soundY, soundT):
        readings = []
        for sensor in self.sensors:
            sensorTime = distance( (sensor.x, sensor.y), (soundX, soundY) ) / phonoSensors.SPEED_OF_SOUND
            readings.append({x:sensor.x, y:sensor.y, t:sensorTime})
        return readings
    
    SPEED_OF_SOUND=0.34029 # km per second