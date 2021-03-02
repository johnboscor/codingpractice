A=(100, 100, 100, 100, 100 )
a=list(A)
a.sort()



max_gap=0
prev=a[0]
for i in range(len(a)):
    curr_gap = abs(prev - a[i])
    max_gap = max(max_gap, curr_gap)
    prev = a[i]
    #print(curr_gap, max_gap)

print(max_gap)