n = int(input("enter a number to check if it is palindrome or not:"))
m = n
rev = 0
while n>0:
    r = n %10
    n = n//10
    rev = rev *10 +r
if rev == m:
    print("palindrome")
else:
    print("not a palindrome")