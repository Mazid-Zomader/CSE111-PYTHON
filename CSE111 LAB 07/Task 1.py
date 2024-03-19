class Circle :
    def __init__(self, radius) :
        self.__radius = radius
    def getRadius(self) :
        return self.__radius
    def setRadius(self, new_radius) :
        self.__radius = new_radius
    def area(self) :
        area = 3.1416 * (self.__radius ** 2)
        return area
#Driver Code
c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())
c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())