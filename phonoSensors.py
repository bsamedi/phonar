import random
import numpy as np

class phonoSensors:
    SPEED_OF_SOUND = 340.29 # meters per second

    def __init__(self, space):
        self.sensors = []
        self.space = space

    def add(self, sensorPoint):
        self.sensors.append( sensorPoint )

    def idealReadings(self, soundPointTime):
        readings = []
        for sensorPoint in self.sensors:
            source2sensorTime = sensorPoint.distance(soundPointTime.point()) / phonoSensors.SPEED_OF_SOUND
            readings.append( sensorPoint.addTime(soundPointTime.t + source2sensorTime))
        return readings

    def detectSource(self, readings, numSounds):
        dims = self.space.dimensions()
        variablesCoefMatrix = []
        dependentVarValues = []
        r1 = readings[0]
        for rn in readings[1:]:
            coeffs = []
            # space-related coefficients, according to space dimensionality, 2*(xn-x1)
            for i in range(dims):
                coeffs.append( 2 * (rn.coordinate(i) - r1.coordinate(i) ) )
            # time-related coefficient, - S**2 * 2*(tn-t1)
            coeffs.append( - self.SPEED_OF_SOUND**2 * 2 * (rn.t - r1.t) )

            variablesCoefMatrix.append(coeffs)

            # constant coefficient, S**2 * (t1**2 - t2**2) - x1**2 + x2**2 - y1**2 + y2**2 - z1**2 + z2**2
            constCoef = self.SPEED_OF_SOUND**2 * (r1.t**2 - rn.t**2)
            for i in range(dims):
                constCoef += - r1.coordinate(i)**2 + rn.coordinate(i)**2
            dependentVarValues.append( constCoef )
        # solve the equation system
        soundSource = np.linalg.solve(variablesCoefMatrix, dependentVarValues)

        return soundSource
