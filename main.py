from phonoSensors import circleSensors

# create sensors located on an ideal circle
sensors = circleSensors( radius=20e3, sensors=10 )

# create sound in the circle centre
sound = {x:0, y:0, t:0}

# calculate ideal sensor output
sensorReadings = sensors.idealReadings( sound )

# sensorReadings.gaussError(x=0.010, y=0.010, t=0.05)
# sensorReadings.missRandomReadings( pct=20 )

# reverse-find sound source
soundFound = sensorReadings.calcSound()

print soundFound
