dict = { 'name':'mohan','age':'18','city':'vizag'}
print('dictionary elements:')
for key  in dict:
    print(key,":",value)
    print('accessing :',dict['age'])
    dict['gender'] = 'male'
print('dictionary after gender adding:',dict)
print('remove value:',dict.pop('city'))
print('length of dictionary:',len(dict))
  