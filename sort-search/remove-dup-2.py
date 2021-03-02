#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

A = [1,1,1,2,2,3,4,4,4,5,5,6,7,8,9,9,9]
#A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

i=0
while i < len(A)-2:
    if A[i] == A[i+1] and A[i] == A[i+2]:
        A.pop(i)
        i -= 1
    i += 1

print(A)
print(len(A))