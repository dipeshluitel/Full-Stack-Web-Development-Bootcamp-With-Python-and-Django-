class Circle():
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return self.radius*self.radius*Circle.pi
myc = Circle(5)
print(myc.radius)
print(myc.area())