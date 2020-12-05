# Object Orientated Programming in Python

x = 1 
# set x is equal to the 'object' which is a type integer with the value 1
print(type(x))
print(type("hello"))
# this string that we typed is actually an object of the class string
# data type str, int are actually a part of a class

def hello():
    print("hello")

print(type(hello))
# pretty much everything in Python, is actually an object of some kind of class
# Class defines the way in which that object can interact with other things in our program

string = "hello"
print(string.upper())
# .upper() : a method, acting on a specific object

# create my own object #
class Dog:
    def __init__(self, name, age): 
        self.name = name
        self.age  = age 
        # attribute of class dog, which is 'name'
        # attribute : it's stored permanently for each specific object
        # self : 'which object?', so we can access attributes that are specific to each dog
        # we can store different names inside of instance

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age     
    # we can access attribute from methods inside our class
    # which allows us to access data that is stored within a specific object

    def add_one(self, x):
        return x + 1 

    def meow(self):
        return "meow"

    def bark(self): 
        print("bark")

# Method is essentially just a function that goes in side of a class
# all of method are gonna start with a parameter called 'self'

d = Dog("Tom", 7)
print(d.name)
print(d.get_name())
print(d.get_age())
d.set_age(82)
print(d.get_age())
# assign 'd' to a instance of the class Dog
# 'd' gonna be an object that is type Dog

print(type(d)) 
# # __main__ : what module this class was defined
 
# d.bark() # .bark is method inside of class Dog
print(d.meow())
print(d.add_one(4))

A = 1
# A.upper() #AttributeError: 'int' object has no attribute 'upper'
print(type(A))
print(type(1))
print(type(int))