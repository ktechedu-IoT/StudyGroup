import random

A = random.randrange(1,101)

i = 0

while True:

    a = int(input(">>>"))

    if A > a:
        i += 1
        print("upupup")
    elif A < a:
        i += 1
        print("down~~~~")
    elif A == a:
        i += 1
        print("You Win!!!")
        print(i)
        break
