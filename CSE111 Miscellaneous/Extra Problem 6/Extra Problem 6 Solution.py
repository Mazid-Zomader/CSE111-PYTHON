class treeHouse :
    number = 0
    total_weight = 0
    def __init__ (self , height  , weight = 1500 ) :
        print("You have a tree house now!")
        treeHouse.number += 1
        self.name = "T"+ str(treeHouse.number)
        self.height = height
        self.weight = weight
        self.tree_position = treeHouse.number
        treeHouse.total_weight += weight
    def details (self) :
        print(f"Tree house at position: {self.tree_position}")
        print(f"Name: {self.name}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
    @classmethod
    def build_and_show(cls , ratio) :
        ratio = ratio.split(":")
        obj = cls(int(ratio[0]), int(ratio[1]))
        obj.details()
        return obj
    @classmethod
    def houses(cls) :
        print(f"Total Tree houses: {cls.number}")     
        print(f"Current Total Weight: {cls.total_weight}")  
    def position (self) :
        return self.tree_position

#Driver Code
t1 = treeHouse(10, 200)
print("-----------------------")
t1.details()
print("-----------------------")
t2 = treeHouse.build_and_show("13:300")
print("-----------------------")
treeHouse.houses()
print("-----------------------")
t3 = treeHouse(30)
t3.details()
print("-----------------------")
print(t2.position()) # Mistake in question !!
print("-----------------------")
t2.details()