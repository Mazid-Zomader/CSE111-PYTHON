class Assasin:
  Num = 0
  def __init__(self , name , success) :
    self.name = name
    self.success_rate = success
    Assasin.Num += 1
  @classmethod
  def failureRate(cls , name , fail) :
    obj = cls(name , 100-fail)
    return obj
  def printDetails(self) :
    print(f"Name: {self.name}")
    print(f"Success Rate: {self.success_rate}%")
    print(f"Total number of Assasin: {Assasin.Num}")
  @classmethod
  def failurePercentage(cls, name , fail_per) :
     obj = cls(name , 100-int(fail_per[0:len(fail_per)-1]))
     return obj
  
#Driver Code
john_wick = Assasin('John Wick', 100)
john_wick.printDetails()
print("========================")
nagisa = Assasin.failureRate('Nagisa', 20)
nagisa.printDetails()
print("========================")
akabane = Assasin.failurePercentage('Akabane', "10%")
akabane.printDetails()
