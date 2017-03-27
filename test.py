import unittest

from space2D import Space2D, Point2D, PointTime2D

class testSpace2D(unittest.TestCase):
    def testZero(self):
        s = Space2D()
        self.assertEqual(s.zero(), Point2D(0.0, 0.0))

    def testDistanceZeroToZero(self):
        s = Space2D()
        zero1 = s.zero()
        zero2 = s.zero()
        self.assertEqual( zero1.distance(zero2), 0)

    def testDistance34ToZero(self):
        s = Space2D()
        zero = Point2D(0,0)
        p = Point2D(3, 4)
        self.assertEqual( zero.distance(p), 5)

    def testDistanceNeg34ToZero(self):
        zero = Point2D(0,0)
        p = Point2D(3, -4)
        self.assertEqual( p.distance(zero), 5)

    def testDistanceNeg34To34(self):
        s = Space2D()
        p1 = Point2D(3, -4)
        p2 = Point2D(-3, 4)
        self.assertEqual( p1.distance(p2), 10)

    def testExtractPoint(self):
        self.assertEqual( PointTime2D(1, 2, 7).point(), Point2D(1, 2))

from phonoSensors2D import phonoSensors2D
class TestPhonoSensors(unittest.TestCase):

    def test_nosensors(self):
        s = phonoSensors2D()
        self.assertEqual(len(s.sensors), 0)

    def test_onesensor(self):
        s = phonoSensors2D()
        s.add( (5, 5) )
        self.assertEqual(len(s.sensors), 1)

    def test_oneIdealReading(self):
        s = phonoSensors2D()
        s.add( Point2D(10, 0) )
        readings = s.idealReadings( PointTime2D(0, 0, 0) )
        self.assertAlmostEqual(readings[0].t, 10/340.29, 2)

    def test_oneIdealReading2(self):
        s = phonoSensors2D()
        s.add( Point2D(3, 4) )
        readings = s.idealReadings( PointTime2D(-30, -40, 4) )
        self.assertAlmostEqual( readings[0].t, 4 + 55/340.29, 2)

from circleSensors import circleSensors
from math import sqrt
class TestCircleSensors(unittest.TestCase):
    def test_eightSensors(self):
        s = circleSensors(radius=15, center=Point2D(5, 4), sensors = 8)
        self.assertEqual(len(s.sensors), 8)

    def test_twoSensors(self):
        center = Point2D(5, 4)
        s = circleSensors( radius=15, center=center, sensors = 2)
        self.assertEqual(len(s.sensors), 2)
        s0 = s.sensors[0]
        s1 = s.sensors[1]
        self.assertAlmostEquals( s0.distance(s1), 15*2, 5)
        self.assertAlmostEquals( s0.distance(center), 15, 5)
        self.assertAlmostEquals( s0.distance(center), 15, 5)

import random

def numberWithin(num, min, max):
    if num<min:
        return min
    if num>max:
        return max
    return num

class TestDetectSource(unittest.TestCase):
    def test_fourSensors(self):
        s = phonoSensors2D()
        s.add( Point2D(0, 0) )
        s.add( Point2D(1, 1) )
        s.add( Point2D(0, -1) )
        s.add( Point2D(-1, 0) )
        soundOriginal = PointTime2D(0, 0, 0)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_fourSensors2(self):
        s = phonoSensors2D()
        s.add( Point2D(0, 0) )
        s.add( Point2D(1, 1) )
        s.add( Point2D(0, -1) )
        s.add( Point2D(-1, 0) )
        soundOriginal = PointTime2D(5, 7, 14)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_fourSensorsFuzzied0_1Pct(self):
        s = phonoSensors2D()
        s.add( Point2D(0, 0) )
        s.add( Point2D(1000, 1000) )
        s.add( Point2D(0, -1000) )
        s.add( Point2D(-1000, 0) )
        soundOriginal = PointTime2D(200, 200, 50)
        readings = s.idealReadings( soundOriginal )
        readingsFozzy = [ PointTime2D( *[ v * numberWithin(random.normalvariate(1, 0.0001), 0.9999, 1.001) for v in r ]) for r in readings]
        soundDetected = s.detectSource(readingsFozzy, 1)
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], -1)

    def test_fourSensorsFuzzied1Pct(self):
        s = phonoSensors2D()
        s.add( Point2D(0, 0) )
        s.add( Point2D(1000, 1000) )
        s.add( Point2D(0, -1000) )
        s.add( Point2D(-1000, 0) )
        soundOriginal = PointTime2D(400, 100, 70)
        readings = s.idealReadings( soundOriginal )
        readingsFozzy = [ PointTime2D( *[ v * numberWithin(random.normalvariate(1, 0.001), 0.999, 1.01) for v in r ]) for r in readings]
        soundDetected = s.detectSource(readingsFozzy, 1)
        #print('\nsoundDetected\n{}\n'.format(soundDetected))
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], -2)

from phonoSensors3D import phonoSensors3D
from space3D import Space3D, Point3D, PointTime3D
import time

class TestDetectSource3D(unittest.TestCase):
    def test_NearlyPlanarExact(self):
        s = phonoSensors3D()
        s.add( Point3D(0, 0, 0) )
        s.add( Point3D(1000, 1000, 0) )
        s.add( Point3D(0, -1000, 20) )
        s.add( Point3D(-1000, 0, 0) )
        s.add( Point3D(-1000, -1000, 0) )
        soundOriginal = PointTime3D(400, 100, 0, 70)
        readings = s.idealReadings( soundOriginal )
        soundDetected = s.detectSource(readings, 1)
        for i in range(len(soundOriginal)-1):
            self.assertAlmostEqual(soundDetected[i], soundOriginal[i], 2)

    def test_speed(self):
        start = time.time()
        numIterations = 100
        for i in range(numIterations):
            self.test_NearlyPlanarExact()
        end = time.time()
        self.assertLess(end-start, numIterations*0.0005)
        #print('\ntime per detection, microseconds = {}\n'.format( round(1e6*(end-start)/numIterations, 1)))

if __name__ == '__main__':
    unittest.main()

