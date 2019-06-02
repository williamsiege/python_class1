#A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# syntax: # dict_name = {"key 1":"value 1","key 2":"value2","key3":"Value3"}

persons = {
    "name": "John Doe",
    "Age": 34,
    "Country": "Jamaican"

}

print(type(persons))

print(persons)

# Accessing items  by referring to its key

name = persons["name"]

print(name)

age = persons["Age"]

print(age)

# get() method

country = persons.get("Country")

print(country)

# changing a value in dictionary

persons['Age'] = 44


print(persons)


# looping in dictionary

# looping through keys in dictionary

for x in persons:
    print(x)

for x in persons.keys():
    print("the keys are : "+x)

#looping through  values in a dictionary

for x in persons:
    print(persons[x])

for x in persons.values():
    print(x)

# looping both keys and values by using the items function

for key, value in persons.items():
    print("The Key: "+key+" and the value :"+str(value))

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:

persons = {
    "name": "John Doe",
    "Age": 34,
    "Country": "Jamaican"
}

if "name" in persons:
    print("YES , 'Name' is one of the keys in the dictionary")
else:
    print("NOT A KEY IN THE DICTIONARY PLEASE CORRECT")


# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.

print(len(persons))

























