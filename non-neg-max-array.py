A = [-5, -1, 2, 4, 5, -6, 3, 4, 5,-8,3,1,7]


#A = [ 1, 2, 5, -7, 2, 5 ]
#A = [2, 5, -7, 2, 5 ]
#A = [10, -1, 2, 3, -4, 100]
B = []

max_val = []
sum_val = 0
start = 0
for i in range(len(A)):
    if A[i] < 0:
        if max_val or sum_val > sum(max_val):
            max_val = A[start:i]
        start = i+1
        sum_val = 0
    else:
        sum_val += A[i]

    max_val  = A[start:i+1] if sum_val > sum(max_val) else max_val
print(max_val)


'''
start = 0
found = False
for i in range(len(A)):
    if A[i] < 0:
        if found:
            #print(f"appending from {start} to {i}")
            B.append(A[start:i])
            start=i+1
            found = False
    else:
        #print(f"{i}, {found} ")
        if not found:
            start = i
            found = True
if found:
    B.append(A[start:i+1])

print(B)
max=0
for i in range(len(B)):
    if sum(B[i]) > max:
        max=i

print(B[max])
'''