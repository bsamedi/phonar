# X-dimensional tuple-based mathematics space mathematics
class space:
    def dimensions(self):
        raise NotImplementedError()

    def distance(self, p1, p2):
        raise NotImplementedError()

    def zero(self):
        raise NotImplementedError()

    def extractPoint(self, pointTime):
        raise NotImplementedError()

    def extractTime(self, pointTime):
        raise NotImplementedError()

    def pointTime(self, point, time):
        raise NotImplementedError()
