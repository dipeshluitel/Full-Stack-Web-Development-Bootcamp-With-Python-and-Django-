class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog("Japanese Spitz","Saanu")
aayush_dog = Dog("German Shephard","Loki")
print(f"{mydog.breed}, name is {mydog.name}")
print(f"{aayush_dog.breed}, name is {aayush_dog.name}")