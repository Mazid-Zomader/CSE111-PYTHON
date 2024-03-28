class Laptop :
  laptopCount = 0
  def __init__(self , name , num) :
    self.name = name
    self.count = num
    Laptop.laptopCount += num
  @classmethod
  def advantage(cls) :
    print ("Laptops are portable")
  @staticmethod
  def resetCount() :
    Laptop.laptopCount = 0
#Driver Code
lenovo = Laptop("Lenovo", 5)
dell = Laptop("Dell", 7)
print(lenovo.name , lenovo.count)
print(dell.name , dell.count)
print("Total number of Laptop", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptop", Laptop.laptopCount)
