n = int(input("enter number of numbers  to find maximum:"))
max = 0
i = 1
while i <=n:
    m = int(input("enter a number:"))
    if m> max:
        max = m
    else:
        pass
    i = i+1
print("the maximum number of all is",max)
