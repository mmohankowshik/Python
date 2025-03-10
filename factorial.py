#factorial
n = int(input("enter the number to find factorial:"))
m = 1
for i in range(n,1,-1):
    m= m*i
print("the factorial is ",m)