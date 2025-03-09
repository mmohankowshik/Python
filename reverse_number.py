n = int(input("enter number to find its reverse:"))
rev = 0
while n>0:
    r = n%10
    n = n//10
    rev = rev*10+r
print("the reverse of anumber is",rev)