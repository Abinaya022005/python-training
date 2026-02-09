#one class can acquire the properties and methods of another class
#single inheritance
class animal():         #parent class
    def eat(self):
        print("animal is eating")

class dog(animal):      #child class
    def bark(self):
        print("dog is barking")

a=dog()

a.eat()
a.bark()

#multiple inheritance
class camera():
    def photo(self):
        print("taking photos")
class internet():
    def browse(self):
        print("browsing information")
class phone(camera,internet):
    def call(self):
        print("hello")

a=phone()   #object

a.photo()
a.browse()
a.call()

#multilevel inheritance
# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting")
# Inherits from Vehicle
class Car(Vehicle):
    def fuel(self):
        print("Car uses petrol/diesel")
# Inherits from Car
class ElectricCar(Car):
    def battery(self):
        print("Electric Car uses battery")
a = ElectricCar()

a.start()   
a.fuel()    
a.battery() 
#hierarchical inheritance (one parent multi children)
# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
class Bus(Vehicle):
    def wheels(self):
        print("Bus has 6 wheels")

c = Car()
b = Bike()
bus = Bus()

c.start()   
c.wheels()

b.start()   
b.wheels()  

bus.start()  
bus.wheels() 
