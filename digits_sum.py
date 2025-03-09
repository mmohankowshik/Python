n = int(input("enter the number to find its sum:"))
sum = 0
while n>0:
    m = n%10
    n = n // 10
    sum = sum +m

print("the sum of digits is",sum )