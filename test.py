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

if __name__ == '__main__':
    unittest.main()

