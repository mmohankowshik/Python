a = int(input("enter the first number:"))
d = int(input("enter the common difference:"))
n = int(input("enter the number of terms:"))
for i in range(a,(a+(n)*d),d):
    print(i)