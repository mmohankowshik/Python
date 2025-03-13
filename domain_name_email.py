n = input("Enter the email id:")

m = n.find('@')
id = n[:m]
print(id)
domain = n[m+1:]
print(domain)