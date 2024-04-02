s=["flower","flow","flight"]
l =s[0]
for string in s[1:]:
	i=0
	while i<len(l) and i<len(string)and l[i]==string[i]:
		i+=1
		l=l[:i]
	print('longest common prefix:',l)