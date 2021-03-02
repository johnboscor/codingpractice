A = [1, 3, 2, 4, 5, 6, 8, 9, 7]

# incomplete
B = sorted(A)
print(A)
print (B)
C = []
i = 0
#print(len(A))
while i < len(A):
    print(i)
    while A[i] != B[i]:
        C.append(A[i])
        i += 1
    i += 1


print(C)