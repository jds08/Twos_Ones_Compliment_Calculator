class Car():

    def __init__ (self, speed, color, year ):
        self.speed = speed
        self.color = color
        self.year = year

    def increaseSpeed(self):
        self.speed + 2
        print("Speed increase \n New Speed: " + str(self.speed))

    def getSpeed(self):
        return self.speed


    def setSpeed(self, speed):
        # check if speed is valid 
        if speed >= 0:
            self.speed = speed
        else:
            self.speed = 45
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year

     

# Testing my Car class
car1 = Car(45,"Red", 1992)
car2 = Car(90,"Green", 2003)

print("Car1 information: \n" + "Speed: " + str(car1.getSpeed()))
print("Color: " + car1.getColor() + "\nYear: " + str(car1.getYear()) + "\n")

print("Car2 information: \n" + "Speed: " + str(car2.getSpeed()))
print("Color: " + car2.getColor() + "\nYear: " + str(car2.getYear()))


# further notes 
# Magic Methods: 
# examples: 
    # __add__ , denotes +
    # __sub__ , denotes -
    # __mul__ , denotes *
    # __and__ , denotes ^





