list= [10,14,19,25,27,31,34,43,45,52]
n = int(input('enter your key value:'))
for n in list:
    if n  in list:
        print('success! element found')
        break
    else:
        print('failure! element not found')