food =['pizza','nuggets','hotdog','noodles','pasta','burger']
n = input('enter the letter:')
for i in food:
    if i.startswith(n):
        print(i)
        