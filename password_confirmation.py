pass1 = input("Enter the password:")
pass2 = input("Enter the same password:")
if pass1 == pass2:
    print("password Matched!")
elif pass1.casefold() == pass2.casefold():
    print("Please check the cases")
else:
    print("please enter the same password")