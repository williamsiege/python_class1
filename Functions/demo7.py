# Syntax :
# def  name of the function():
# the code to be run

def print_name():
    print("My name is William")


print_name()


# calling a function

def print_country(country_name):
    print("My country is " + country_name)


print_country("Kenya")

developer = "William and Sey"


def get_dev(a_string):
    for x in a_string:
        print(x)


get_dev(developer)

fruits = ['apple', 'mango', 'pineapple', 'banana', 'melon']


def get_dev(a_list):
    for fruit in a_list:
        print(fruit)


get_dev(fruits)


def say_name(name="Developer"):
    return "My name is "+name


say_name("William")

get_tosh = say_name("William")
print(get_tosh)
