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

# class TestDetectSource(unittest.TestCase):
    # def test_fourSensors(self):
        # s = phonoSensors()
        # s.add(0, 1)
        # s.add(1, 0)
        # s.add(0, -1)
        # s.add(-1, 0)
        # soundOriginal = (0, 0, 0)
        # readings = s.idealReadings(*soundOriginal)
        # soundDetected = s.detectSource(readings, 1)
        # print('soundDetected {}'.format(soundDetected))

if __name__ == '__main__':
    unittest.main()

