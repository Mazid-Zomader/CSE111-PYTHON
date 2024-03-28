from datetime import date
class Employee:
  def __init__(self, name , j_year) :
    self.name = name
    self.workingPeriod = j_year
  @classmethod
  def employeeByJoiningYear(cls , name  , j_year) :
    obj = cls (name , date.today().year - j_year)
    return obj
  @staticmethod
  def experienceCheck(time,  gender) :
    if time < 3 :
      if gender == 'male' :
        return "He is not experienced"
      else :
        return "She is not experienced"
    else :
      if gender == 'male' :
        return "He is experienced"
      else :
        return "She is experienced"
#Driver Code
employee1 = Employee('Dororo' , 3)
employee2 = Employee.employeeByJoiningYear('Harry' , 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2,"male"))
print(Employee.experienceCheck(3,"female"))