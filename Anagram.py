s1 = input("Enter 1st string:")
s2 = input("enter 2nd string:")
if len(s1)!=len(s2):
    print("not a anagram!")
else:
    for x in s1:
        if x  not in s2:
            print("not anagram")
            break
        else:
            print("anagram")
            break