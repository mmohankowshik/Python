import random
n = random.randint(1,10)
while n > 0:
    m = int(input("enter number to guess:"))
    if m > n:
        print("number is less than this")
    elif m < n:
        print("number is greater than this")
    else:
        print("number found!")
        break