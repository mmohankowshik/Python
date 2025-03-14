n = input("Enter the string:")
upper = ''
lower = ''
for x in n:
    if x.isupper():
        upper += x
    else :
        lower += x
print("The string is:",lower+upper)