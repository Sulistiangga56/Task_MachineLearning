import math

class Dog:
    counter = 0
    def __init__(self, name): # constructor
        self.name = name
        Dog.counter += 1
    def bark(self):
        return self.name +'(' + str(Dog.counter)+') wouaf'
    
dog1 = Dog('Lassie')
dog2 = Dog('Rex')
print(dog1.bark()) #Lassie(2)wouaf
print(dog2.bark(), '\n') #Rex(2)wouaf
    
class Vehicle:
    def __init__(self, initial_covered_distance):
        self.covered_distance = initial_covered_distance
    def add_distance(self, new_covered_distance):
        self.covered_distance += new_covered_distance
            
class Plane(Vehicle): # inheritance from Vehicle
    def __init__(self,number_of_engines, initial_covered_distance):
        Vehicle.__init__(self,initial_covered_distance) # constructor of the parent has to be called
        self.number_of_engines = number_of_engines
    def __str__(self): # called by default by print 
        return "Plane with %i engines. Covered distance is %d" % (self.number_of_engines, self.covered_distance)

print(Plane(4,150000)) # Plane with 4 engines. Covered distance is 150000

class Surface:
    def get_surface(self):
        raise NotImplementedError()
    def get_perimeter(self):
        raise NotImplementedError()
    def __str__(self):
        return 'Surface is: %f and perimeter: %f' % (self.get_surface(), self.get_perimeter())
    
class Color:
    def __init__(self, color: int = 0):
        self.color = color
    def set(self, color: int):
        self.color = color
    def get(self):
        return self.color

class Rectangle(Surface, Color): # multiple inheritance
    def __init__(self, width: float, height: float, color: int = 0):
        Color.__init__(self, color) # all the parent constructors should be called
        Surface.__init__(self) # all the parent constructors should be called
        self.width = width
        self.height = height
    def get_surface(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
class Square(Rectangle):
    def __init__(self,length: float, color: int = 0):
        Rectangle.__init__(self, length, length, color)

class Disk(Surface,Color):
    def __init__(self, radius: float,color: int = 0):
        Color.__init__(self, color)
        Surface.__init__(self)
        self.radius = radius
    def get_surface(self):
     return math.pi * self.radius ** 2
    def get_perimeter(self):
     return 2 * math.pi * self.radius

print(Square(4, 5)) #Surface is: 13.500000 and perimeter: 15.000000
print(Disk(3, 2), '\n') #Surface is: 32.169909 and perimeter: 20.106193

def some_function():
    try:
        10/0 # Division by zero raises an exception
    except ZeroDivisionError:
        print("Oops, invalid. ")
    else: #Exception didn't occur, we're good.
        pass
    finally:
        #   This is executed after the code block is run and all exceptions have been handled, even if a new exception is
        #   raised while handling.
        print("We're done with that.")

some_function()

def perkalian(x,y):
    hasil = x * y
    print(hasil)

perkalian(5, 4)
#Oops, invalid.
#We're done with that.