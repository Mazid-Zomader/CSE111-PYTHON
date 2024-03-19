class Spaceship :
    def __init__(self , name , capacity) :
        self.name = name
        self.capacity = capacity
        self.filled_weight = 0
        self.remained_weight = capacity
        self.cargo_list = []
    def load_cargo(self , item) :
        if self.remained_weight > item.getWeight() :
            self.remained_weight -= item.getWeight()
            self.cargo_list.append(item.getName())
            self.filled_weight += item.getWeight()
        else :
            print(f"Warning: Unable to load {item.getName()} inside")
            print(f"{self.name}. Exceeds capacity by {item.getWeight()-self.remained_weight}.")
    def display_details(self) :
        print(f"Spaceship Name: {self.name}")
        print(f"Capacity: {self.capacity}")
        print(f"Current Cargo Weight: {self.filled_weight}")
        print(f"Cargo: {self.cargo_list}")

class Cargo:
    def __init__(self , c_name , c_weight ):
        self.__c_name = c_name
        self.__c_weight = c_weight
    def getName(self):
        return self.__c_name
    def getWeight(self) :
        return self.__c_weight

#Driver Code
# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold) # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium) # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium) # This should not exceed Enterprise's capacity
enterprise.display_details()