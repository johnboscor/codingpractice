#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

A = [1,1,2,4,5,6,6,6,8]
A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]

i=0
while i < len(A)-1:
    if A[i] == A[i+1]:
        A.pop(i)
        i -=1
    i += 1

print(A)
print(len(A))