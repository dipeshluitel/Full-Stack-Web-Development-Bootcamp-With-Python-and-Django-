class game():

    def __init__(self,name,size,req):
        self.name = name
        self.size = size
        self.requirements = req

    def __str__(self):
        return "The Game name is {}, It's size is {} and requires {} of RAM".format(self.name,self.size,self.requirements)
g=game("valorant","44GB","8GB")
print(g)