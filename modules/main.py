# consider a module to be the same as a code library
# a file containing a set of functions you want to  include in your application

import demo9.py
import pythonawesome.py as demo10
import platform

print(demo9.sentence)

print(demo9.fruits)

for x in demo9.fruits:
	print(x)


print(demo9.person)

print(demo9.person['name'])
print(demo9.person['age'])


country1 = demo9.person['country']

print(country1)

demo10.get_name("William")

x = platform.system()

print(x)


get_details = dir(demo10)

print(get_details)

for x in get_details:
	print(x)

for x in dir(platform):
	print(x)
