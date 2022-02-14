import math
class Circle():
    def __init__(self, a,b,r):
        self.a = a
        self.b = b
        self.r = r

    def Area(self):
        return math.pi * (self.r ** 2)

    def Perimeter(self):
        return 2 * math.pi * self.r

    def testBelongs(self,x,y):
        if x == self.a and y == self.b:
            return True

        else:
            return False

circle = Circle(2,3,5)
print('Circle Area: ', circle.Area())
print('Circle Perimeter: ', circle.Perimeter())
print('Is the point belongs to the circle: ', circle.testBelongs(2,3))
