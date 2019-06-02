fruits = ['banana', 'apple', 'lemon', 'melon', 'pineapple']

try:
    print(fruits)
except:
    pass

y = "lesson learned"

try:
    print(y)
except NameError:
    print("variable y is not defined")
except SyntaxError:
    print("invalid syntax")
except:
    print("something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("finished")