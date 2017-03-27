from phonoSensors import phonoSensors
from space2D import Space2D

class phonoSensors2D(phonoSensors):
    def __init__(self):
        phonoSensors.__init__(self, Space2D())
