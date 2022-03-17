# Superclass

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def info(self):
        print("Information: \nName: " + self.name + "\nType: " + self.type)


# Subclass 

class Cat(Animal):
    pass

# automatically uses the superclass constructor
cat = Cat('Rambo', "Ferral")
print(cat.info())