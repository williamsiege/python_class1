import os

dictionaries = open("text.txt", "r")
print(dictionaries.read())

diction_list = dictionaries.readline()

#  print(type(diction_list))
# print(diction_list[1])

f = open("text.txt", "r")
print(f.read(5))

for x in f:
    print(x)


# os.remove("text.html")

if os.path.exists("text.txt"):
    print("FILE EXISTS")
else:
    print("FILE DOES NOT EXIST")

f = open("myfile.txt", "x")