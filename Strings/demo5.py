# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = " Hello, World "
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])


print(a[2:5])

print(a)

print(a.strip())   # returns "hello, world" without spacing.

print(len(a))      #counts the length of the string.

print(a.lower())   #returns all values to lower case

print(a.upper())    # returns all values to uppercase

print(a.replace("Hello", "Good"))  # replaces a value with another value

print(a.split())  # returns ['Hello', ' World!']