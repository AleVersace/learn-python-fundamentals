class Point:

    def __init__(self, name, x, y):
        self.name = name    # Public        Access from everywhere.
        self._x = x         # _ Protected     Access from inside or from sub-classes or proprial methods.
        self.__y = y        # __ Private       Access just with proprial methods.

    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self._x = x
        self.__y = y
    
    def printXY(self):
        print('x = {}, y = {}'.format(self._x, self.__y))

p1 = Point("uno", 1, 1)
print(p1.name)
# print(p1.x) WRONG We have to use implement proper method!
# print(p1.y) WRONG Same here
p1.printXY()

    