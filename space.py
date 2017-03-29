# X-dimensional tuple-based mathematics space mathematics
class Point:
    def distance(self, other):
        raise NotImplementedError()
    
    def addTime(self, time):
        raise NotImplementedError()
    
    def coordinate(self, index):
        if index < len(self):
            return self[index]
        else:
            raise IndexError()

class PointTime:
    def distance(self, other):
        raise NotImplementedError()
    
    def point(self):
        raise NotImplementedError()

    def coordinate(self, index):
        if index < len(self)-1:
            return self[index]
        else:
            raise IndexError()

class Space:
    def dimensions(self):
        return len(self.zero())

    def zero(self):
        raise NotImplementedError()
