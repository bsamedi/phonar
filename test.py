import unittest

from phonoSensors import phonoSensors
class TestPhonoSensors(unittest.TestCase):

    def test_nosensors(self):
        s = phonoSensors()
        self.assertEqual(len(s.sensors), 0)

    def test_onesensor(self):
        s = phonoSensors()
        s.add(5, 5)
        self.assertEqual(len(s.sensors), 1)

    def test_oneIdealReading(self):
        s = phonoSensors()
        s.add(10, 0)
        readings = s.idealReadings(0, 0, 0)
        self.assertAlmostEqual(readings[0]['t'], 10/0.34029, 2)

    def test_oneIdealReading(self):
        s = phonoSensors()
        s.add(3, 4)
        readings = s.idealReadings(-30, -40, 4)
        self.assertAlmostEqual(readings[0]['t'], 4 + 55/0.34029, 2)

from phonoSensors import circleSensors
import math
class TestCircleSensors(unittest.TestCase):
    def test_eightSensors(self):
        s = circleSensors( radius=15, center={'x':5, 'y':4}, sensors = 8)
        self.assertEqual(len(s.sensors), 8)

    def test_twoSensors(self):
        s = circleSensors( radius=15, center={'x':5, 'y':4}, sensors = 2)
        self.assertEqual(len(s.sensors), 2)
        s0 = s.sensors[0]
        s1 = s.sensors[1]
        self.assertAlmostEquals(math.sqrt((s0['x']-s1['x'])*2 + (s0['y']-s1['y'])**2), 15*2, 5)
        self.assertAlmostEquals(math.sqrt((s0['x']-5)*2 + (s0['y']-4)**2), 15, 5)
        self.assertAlmostEquals(math.sqrt((s1['x']-5)*2 + (s1['y']-4)**2), 15, 5)

if __name__ == '__main__':
    unittest.main()

