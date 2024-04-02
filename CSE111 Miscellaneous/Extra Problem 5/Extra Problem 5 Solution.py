class Square :
    def __init__(self , length ) :
        self.__length = length
        self.__area = length**2
    def getLength (self) :
        return self.__length
    def getArea(self) :
        return self.__area
    def setLength(self , new_length) :
        self.__length = new_length
    @classmethod
    def add_area (cls , *args) :
        total_area = 0
        for index in range(len(args)) :
            total_area += args[index].getArea()
        print(f"Summation of areas: {total_area}")

sq1 = Square(10)
print("First Square Length:" , sq1.getLength())
print("First Square Area:" , sq1.getArea())
sq1.setLength(12)
print("1==============================")
sq2 = Square(10)
print("First Square Length:" , sq1.getLength())
print("First Square Area:" , sq1.getArea())
print("2==============================")
Square.add_area(sq1,sq2)