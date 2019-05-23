# Python is an object oriented programming language.
#
# Almost everything in Python is an object, with its properties and methods.
#
# A Class is like an object constructor, or a "blueprint" for creating objects.


class Person:
    hands = 2
    legs = 2
    eyes = 2
    head = 1
    hair = "black"  # this is a property


p1 = Person()  # initializing a class / creating an object.

p2 = Person()

p3 = Person()

# p1, p2 ,p3 are objects / instances of the class person(). an object is a variable assigned to a class.


print(p1.hands)

print(p2.eyes)

print(p3.hair)


# the _ init _ () function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#
# To understand the meaning of classes we have to understand the built-in __init__() function.
#
# All classes have a function called __init__(), which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


class Car:
    wheels = 4
    engine = 1

    def __init__(self, color, brand):
        self.my_color = color
        self.my_brand = brand

    def print_my_car(self):
        print('COLOR : ' + self.my_color + '  BRAND: ' + self.my_brand)

    def print_color(self):
        print("COLOR : " + self.my_color)

    def print_brand(self):
        print("BRAND : " + self.my_brand)


c1 = Car('Blue', 'Ford')

c2 = Car('Yellow', 'Subaru')

c1.print_my_car()
c2.print_my_car()

c1.print_color(), c1.print_brand()

c2.print_color(), c2.print_brand()

# MODIFYING OBJECT PROPERTIES

# print(c1.wheels)
#
# print(c2.wheels)
#
# c1.wheels= 3
# print(c1.wheels)

# deleting object properties , deletes the value of the property

# del c1.wheels
# print(c1.wheels)


del c1   # deletes the object itself.