from phonoSensors import phonoSensors
from space3D import space3D

class phonoSensors3D(phonoSensors):
    def __init__(self):
        phonoSensors.__init__(self, space3D())
