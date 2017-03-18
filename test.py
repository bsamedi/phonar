import unittest

from space2D import space2D

class testSpace2D(unittest.TestCase):
    def testZero(self):
        s = space2D()
        self.assertEqual(s.zero(), (0.0, 0.0))

    def testDistanceZeroToZero(self):
        s = space2D()
        zero1 = s.zero()
        zero2 = s.zero()
        self.assertEqual( s.distance(zero1, zero2), 0)

    def testDistance34ToZero(self):
        s = space2D()
        zero = (0,0)
        p = (3, 4)
        self.assertEqual( s.distance(zero, p), 5)

    def testDistanceNeg34ToZero(self):
        s = space2D()
        zero = (0,0)
        p = (3, -4)
        self.assertEqual( s.distance(p, zero), 5)

    def testDistanceNeg34To34(self):
        s = space2D()
        p1 = (3, -4)
        p2 = (-3, 4)
        self.assertEqual( s.distance(p1, p2), 10)

    def testExtractPoint(self):
        s = space2D()
        self.assertEqual( s.extractPoint((1, 2, 7)), (1, 2))

    def testExtractTime(self):
        s = space2D()
        self.assertEqual( s.extractTime((4, 7, 15)), 15)

from phonoSensors import phonoSensors
class TestPhonoSensors(unittest.TestCase):

    def test_nosensors(self):
        s = phonoSensors(space2D())
        self.assertEqual(len(s.sensors), 0)

    def test_onesensor(self):
        s = phonoSensors(space2D())
        s.add( (5, 5) )
        self.assertEqual(len(s.sensors), 1)

    def test_oneIdealReading(self):
        space = space2D()
        s = phonoSensors(space)
        s.add( (10, 0) )
        readings = s.idealReadings( (0, 0, 0) )
        self.assertAlmostEqual(space.extractTime(readings[0]), 10/0.34029, 2)

    def test_oneIdealReading2(self):
        space = space2D()
        s = phonoSensors(space)
        s.add( (3, 4) )
        readings = s.idealReadings( (-30, -40, 4) )
        self.assertAlmostEqual( space.extractTime(readings[0]), 4 + 55/0.34029, 2)

from circleSensors import circleSensors
from math import sqrt
class TestCircleSensors(unittest.TestCase):
    def test_eightSensors(self):
        space = space2D()
        s = circleSensors(radius=15, center=(5, 4), sensors = 8)
        self.assertEqual(len(s.sensors), 8)

    def test_twoSensors(self):
        center = (5, 4)
        s = circleSensors( radius=15, center=center, sensors = 2)
        self.assertEqual(len(s.sensors), 2)
        s0 = s.sensors[0]
        s1 = s.sensors[1]
        self.assertAlmostEquals( s.space.distance(s0, s1), 15*2, 5)
        self.assertAlmostEquals( s.space.distance(s0, center), 15, 5)
        self.assertAlmostEquals( s.space.distance(s1, center), 15, 5)

import random

def numberWithin(num, min, max):
    if num<min:
        return min
    if num>max:
        return max
    return num

class TestDetectSource(unittest.TestCase):
    def test_fourSensors(self):
        s = phonoSensors(space2D())
        s.add( (0, 0) )
        s.add( (1, 1) )
        s.add( (0, -1) )
        s.add( (-1, 0) )
        soundOriginal = (0, 0, 0)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_fourSensors2(self):
        s = phonoSensors(space2D())
        s.add( (0, 0) )
        s.add( (1, 1) )
        s.add( (0, -1) )
        s.add( (-1, 0) )
        soundOriginal = (5, 7, 14)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_fourSensorsFuzzied0_1Pct(self):
        s = phonoSensors(space2D())
        s.add( (0, 0) )
        s.add( (1000, 1000) )
        s.add( (0, -1000) )
        s.add( (-1000, 0) )
        soundOriginal = (200, 200, 50)
        readings = s.idealReadings( soundOriginal )
        readingsFozzy = [ [ v * numberWithin(random.normalvariate(1, 0.001), 0.999, 1.001) for v in r ] for r in readings]
        soundDetected = s.detectSource(readingsFozzy, 1)
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], -1)

    def test_fourSensorsFuzzied1Pct(self):
        s = phonoSensors(space2D())
        s.add( (0, 0) )
        s.add( (1000, 1000) )
        s.add( (0, -1000) )
        s.add( (-1000, 0) )
        soundOriginal = (400, 100, 70)
        readings = s.idealReadings( soundOriginal )
        readingsFozzy = [ [ v * numberWithin(random.normalvariate(1, 0.01), 0.99, 1.01) for v in r ] for r in readings]
        soundDetected = s.detectSource(readingsFozzy, 1)
        #print('\nsoundDetected\n{}\n'.format(soundDetected))
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], -2)

from space3D import space3D
import time

class TestDetectSource3D(unittest.TestCase):
    def test_NearlyPlanarExact(self):
        s = phonoSensors(space3D())
        s.add( (0, 0, 0) )
        s.add( (1000, 1000, 0) )
        s.add( (0, -1000, 20) )
        s.add( (-1000, 0, 0) )
        s.add( (-1000, -1000, 0) )
        soundOriginal = (400, 100, 0, 70)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_speed(self):
        start = time.time()
        numIterations = 2000
        for i in range(numIterations):
            self.test_NearlyPlanarExact()
        end = time.time()
        self.assertLess(end-start, numIterations*0.0005)
        #print('\ntime per detection, microseconds = {}\n'.format( round(1e6*(end-start)/numIterations, 1)))

if __name__ == '__main__':
    unittest.main()

