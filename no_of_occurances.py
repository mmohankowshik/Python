L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']
res =[]
for i in L1:
    if i not in res:
        res.append(i)
        count = L1.count(i)
        res.append(count)

print(res)