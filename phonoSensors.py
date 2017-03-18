import random
import numpy as np

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

    def detectSource(self, readings, numSounds):
        dims = self.space.dimensions()
        variablesCoefMatrix = []
        dependentVarValues = []
        r1 = readings[0]
        for n in range(dims+1):
            rn = readings[n+1]
            coeffs = []
            # space-related coefficients, according to space dimensionality, 2*(xn-x1)
            for d in range(dims):
                coeffs.append( 2*(rn[d] - r1[d]) )
            # time-related coefficient, - S**2 * 2*(tn-t1)
            t1 = r1[dims]
            tn = rn[dims]
            coeffs.append( - self.SPEED_OF_SOUND**2 * 2 * (tn - t1) )

            variablesCoefMatrix.append(coeffs)

            # constant coefficient, S**2 * (t1**2 - t2**2) - x1**2 + x2**2 - y1**2 + y2**2 - z1**2 + z2**2
            constCoef = self.SPEED_OF_SOUND**2 * (t1**2 - tn**2)
            for d in range(dims):
                constCoef = constCoef - r1[d]**2 + rn[d]**2
            dependentVarValues.append( constCoef )
        # solve the equation system
        soundSource = np.linalg.solve(variablesCoefMatrix, dependentVarValues)

        return soundSource
