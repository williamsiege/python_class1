# syntax for  a loop
# : for item_name in sequence (list,tuple, dictionary , string ,set ):

# code to be run

name = "developer"
for letter in name:
    print(letter)

fruits = ['banana', 'Guava', 'pineapple', 'avocado']
for fruit in fruits:
    print(fruit)

# break statement

for fruit in fruits:
    if fruit == 'pineapple':
        break
    print(fruit)

# continue Statement

for fruit in fruits:
    if fruit == "pineapple":
        continue
    print(fruit)

# Range() function
# the range function takes 3 arguments
# range (<starting point>,<end point>,<increment value>)

for num in range(2, 10, 3):
    print(num)

# break

for num in range(2, 10):
    if num == 5:
        break
    print(num)

for num in range(10):
    print(num)
else:
    print('python is awesome')


names = ['Antony', 'William', 'Way_hive', 'Victor']
fruits = ['banana', 'Guava', 'pineapple', 'avocado']

for name in names:
    for fruit in fruits:
        print(name, fruit)

for name in names:
    for fruit in fruits:
        if name == 'Antony':
            if fruit == 'banana':
                print(name, fruit)
                break
        elif name == 'William':
            if fruit == 'Guava':
                print(name, fruit)
                break
        elif name == 'Way_hive':
            if fruit == 'pineapple':
                print(name, fruit)
                break
        elif name == 'Victor':
            if fruit == 'avocado':
                print(name, fruit)
                break

# Using Indexing in a for loop

for name in names:
    for fruit in fruits:
        if name == names[0]:
            if fruit == 'banana':
                print(name, fruit)
                break
        elif name == names[1]:
            if fruit == 'Guava':
                print(name, fruit)
                break
        elif name == names[2]:
            if fruit == 'pineapple':
                print(name, fruit)
                break
        elif name == names[3]:
            if fruit == 'avocado':
                print(name, fruit)
                break

















