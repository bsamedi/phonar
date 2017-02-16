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


if __name__ == '__main__':
    unittest.main()

