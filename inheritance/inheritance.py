class Animal:
    def __init__(self, name, country):
        self.the_name = name
        self.the_country = country
        # self.property = arg1

    def print_the_details(self):
        print("The Name: " + self.the_name + "  and the Country: " + self.the_country)

    def print_hello_world(self):
        print("Hello World to " + self.the_name + " of " + self.the_country)


# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
#
# We want to add the __init__() function to the child class (instead of the pass keyword).
#
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Mammal(Animal):
    def __init__(self, name, country, Age, Height):
        Animal.__init__(self, Age, Height)
        self.the_name = name
        self.the_country = country
        self.the_age = Age
        self.the_height = Height

    def print_the_details(self):
        print("The Name: " + self.the_name + "  and the Country: " + self.the_country +
              " Age: " + self.the_age + " Height: " + self.the_height)


cow = Animal("rabo", "Germany")
bull_dog = Animal("Junior", "UK")

cow.print_the_details()

bull_dog.print_hello_world()

calf = Mammal('calpho', 'Kenya', '5 years', '10m')

calf.print_the_details()

# changing python version from version 2 and 3 vise versa
# alias python=python3.7
