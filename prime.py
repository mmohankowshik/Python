n = int(input("enter number to find prime or not:"))
for i in range(2,n):
    if n%i ==0:
        print("not a prime")
        break
    else:
        print("its a prime")
        break