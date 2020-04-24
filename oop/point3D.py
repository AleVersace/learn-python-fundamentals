from point import *

class Point3D(Point):   # With multiple inheritance and conflicts, wins the lefter ones.
    _z = 0
    def __init__(self, x, y, z):
        Point.__init__(self, 'Broo', x, y)
        self._z = z
    
    def describe(self):
        return 'Point3d name:{} ({}, {}, {})'.format(self.name, self._x, self.getY(), self._z)
    
p1 = Point3D(1, 2, 3)
print(p1.describe())