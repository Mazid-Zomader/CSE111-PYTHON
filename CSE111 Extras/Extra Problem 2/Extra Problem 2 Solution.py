class Course :
    def __init__ (self , name , credit) :
        self.__name = name
        self.__credit = credit
    def setCredit(self , new_credit) :
        self.__credit = new_credit
        print("Credit successfully updated")
    def getName(self) :
        return self.__name
    def getCredit(self) :
        return self.__credit
class Student :
    def __init__ (self , name) :
        self.name = name
        self.credit = []
        self.grade = []
        self.total_credit = 0
    def addGP (self , location , grade) :
        self.grade.append(grade)
        print(f"Hello {self.name}, your grade for the {location.getName()} course is added")
        self.credit.append(location.getCredit())
        self.total_credit += location.getCredit()
    def gpa (self ) :
        calculating_grade = 0
        for index in range(len(self.grade)) :
            calculating_grade += self.grade[index] * self.credit[index]
        calculating_grade /= self.total_credit
        return round(calculating_grade , 2 )


#Driver Code
c1 = Course("CSE110", 3)
c2 = Course("CSE111", 3)
c3 = Course("CSE400", 3)
c4 = Course("CSE421", 3)
print("1*************************************")
c3.setCredit(4)
s1 = Student("Alif")
s2 = Student("Sehrin")
print("2*************************************")
s1.addGP(c1, 4.0)
s1.addGP(c2, 3.7)
s1.addGP(c3, 4.0)
print("3*************************************")
print(f"{s1.name}'s GPA for this semester is {s1.gpa()}")
print("4*************************************")
s2.addGP(c4, 4.0)
s2.addGP(c2, 3.3)
s2.addGP(c3, 3.7)
print("5*************************************")
print(f"{s2.name}'s GPA for this semester is {s2.gpa()}")
print("6*************************************")
