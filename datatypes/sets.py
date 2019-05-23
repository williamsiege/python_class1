#A set is a collection which is unordered and un indexed. In Python sets are written with curly brackets.

cars = {'BMW', 'AUDI', 'PORSCHE'}
print(cars)

# Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for each_car in cars:
    print(each_car)

# Add an item to a set, using the add() method:
# set_name.add('Item added')

cars.add('AZURE')

print(cars)

#Add multiple items to a set, using the update() method:
#set_name.update(['item 1 added','item 2 added'])

cars.update(['TOYOTA', 'FORD'])

print(cars)

#To determine how many items a set has, use the len() method.

print(len(cars))

# To remove an item in a set, use the remove(), or the discard() method.
# if the item to remove does not exist remove() function will raise an error
# if the item to remove does not exist discard() function will not raise an error

print(cars.remove('AUDI'))

print(cars.discard('BMW'))

# It is also possible to use the set() constructor to make a set.
# this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(this_set)

cars = (('BMW', 'AUDI', 'PORSCHE'))

print(cars)








