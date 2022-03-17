class Person():
    # constructor 
    def __init__(self):
        # self refers to itself(the object)
        self.age = 21
        self.hairColor = "black"
    # pass keyword is used when when a stement is required syntaically
    # , but you do not want tha code to execute
    pass

 # creating an instance of the person class
person = Person()
# calling person attributes and printing them
print(person.age)
print(person.hairColor)








