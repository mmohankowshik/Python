tuple= (1,2,3,4,5)
print('elements of tuple:')
for element in tuple:
    print(element)
print("sliced tuple:")
print(tuple[1:4])
tuple1 = (1,2,3)
tuple2 = (4,5,6)
conc_tuple = tuple1+tuple2
print('concatenated tuple:',conc_tuple)
print('repeated tuple:',tuple1*3)
print('length of tuple:',len(tuple))