n = int(input("enter number of numbers you want to add:"))
psum = 0
nsum = 0
i = 1
while i <=n:
    m = int(input("enter the number",))
    if m>=0:
        psum = psum+m
    else:
        nsum = nsum + m
    sum = psum + nsum
    i = i+1
print("the postive sum is",psum)
print("the negative sum is",nsum)
print("the sum is",sum)