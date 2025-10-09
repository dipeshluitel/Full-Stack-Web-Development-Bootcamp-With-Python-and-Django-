class Animal():
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("ANIMAL")
    
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")


myD = Dog()
# myA = Animal()
# myA.whoAmI()
# myA.eat()
myD.whoAmI()
myD.eat()