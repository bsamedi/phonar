from phonoSensors import phonoSensors
from space3D import Space3D

class phonoSensors3D(phonoSensors):
    def __init__(self):
        phonoSensors.__init__(self, Space3D())
