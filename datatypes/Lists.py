# List is a collection which is ordered and changeable. Allows duplicate members.it allows duplicate members.

# this list =['item1','item2','item3']

fruits = ['apple', 'mango', 'pineapple', 'banana', 'melon']

print(type(fruits))

print(fruits)

# indexing / accessing items in a list

print(fruits[0])

# changing item value in a list

fruits[0] = 'grapes'

print(fruits)

fruits[2] = 'straw berry'

print(fruits)

# looping through a list
# syntax for a loop
# for fruit in fruits :
#     print(fruit)

for each_fruit in fruits:
    print(each_fruit)

# checking if an item exists in a list

if 'pineapple' in fruits:
    print('pineapple present')
else:
    print('pineapple absent')

# adding an item at the end of a list
# list_name.append("item to be added")

fruits.append('Avocado')
print(fruits)

# adding a item in specific index of a list
# list_name.insert('position','item to be added')

fruits.insert(2, 'kiwi')
print(fruits)

# popping / removing items in a list
# list_name.pop()

fruits.pop()
print(fruits)

# removing a specific item in a list
# list_name.remove('item to be removed')

fruits.remove('banana')
print(fruits)


# using for loop pop items in the fruits list

for fruit in fruits:
    fruits.pop()
print(fruits)


# methods of creating a list
# list_name = []
# 1. fruits = ['apple', 'mango', 'pineapple', 'banana', 'melon']
# 2. list_name = list() # an empty list
# 3. list_name = [] # an empty list

# assigment copying a list

# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

fruits = ['apple', 'mango', 'pineapple', 'banana', 'melon']

fruits_lists = fruits.copy()

print(fruits_lists)









