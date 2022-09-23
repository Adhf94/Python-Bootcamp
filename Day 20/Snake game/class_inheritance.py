class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exhale")

#The class object instance has inhereted all the attributes of the superclass.
class Fish(Animal):
    def __init__(self):
        super().__init__()

#if we want to define a method that inherits the superclass methods, and then change it :
    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water")

nemo = Fish()

nemo.breathe()
print(nemo.num_eyes)

# This allows us to do is to take an existing class and build on top of it without reinvent the wheel.(doing all from zero again)