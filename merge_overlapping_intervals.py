
a=[]
b = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]


for i in b:
    a.append(list(i))
print(a)

i = 0
while i < len(a)-1:
    if a[i][1] > a[i+1][0]:
        if a[i][1] < a[i + 1][1]:
            a[i][1] = a[i+1][1]
        a.pop(i+1)
    else:
        i += 1

c = []
for i in a:
    c.append(tuple(i))
print(c)
