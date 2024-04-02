n =input('enter your string1:')
m = input('enter your string2:')
list1=list(n)
list2=list(m)
list1.sort()
list2.sort()
if list1 ==list2:
	print('the given strings are anagrams.')
else:
	print('the given strings are not anagrams.')
