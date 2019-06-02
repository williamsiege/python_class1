x = 101
for num in range(x):
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZ BUZZ")
        continue

    elif num % 3 == 0:
        print("FIZZ")
        continue

    elif num % 5 == 0:
        print("BUZZ")
        continue
    else:
        print(num)


# for x in range(101):
#     if x % 3 == 0 and x % 5 == 0:
#         print('fizz buzz')
#     elif x % 3 == 0:
#         print('fizz')
#     elif x % 5 == 0:
#         print("buzz")
#
#     else:
#          print (num)




















