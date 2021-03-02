#https://www.interviewbit.com/problems/rotate-matrix/

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]
#A = [[1,2], [3,4]]
for i in A:
    print(i)

# using extra dictionary
'''
length = len(A)
B = []
for i in range(length):
    j = length - 1
    C = []
    while j >= 0:
        C.append(A[j][i])
        j -= 1
    B.append(C)

for i in B:
    print(i)
'''
#in place replacement
i = 0
j = len(A) -1
N = len(A) - 1
for i in range(len(A)):

    A[0][i], A[i][N], A[N][j], A[j][0] = A[j][0], A[0][i], A[i][N], A[N][j]
    '''
    same as:
    first = A[0][i]
    second = A[i][N]
    third = A[N][j]
    fourth = A[j][0]

    A[0][i] = fourth
    A[i][N] = first
    A[N][j] = second
    A[j][0] = third
    '''
    j -= 1

    if j <= 0:
        break

print("After Rotation")
for i in A:
    print(i)



