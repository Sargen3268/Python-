class Animal: # Parent class (superclass)
    
    location = "Earth"  # Class attribute shared by all instances of Animal
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now ....")


class Dog(Animal):
    def speak(self):
        super().speak() # Calling the speak method of the parent class
        print("Woof!")

# a=Animal("Dog")
# a.speak()

d=Dog("Brook")
d.speak()
#print(d.location)  # Accessing the class attribute from the parent class