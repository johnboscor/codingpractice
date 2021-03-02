#https://www.interviewbit.com/problems/minimize-the-absolute-difference/

A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]
A = [ -1 ]
B = [ -2 ]
C = [ -3 ]
i = j = k = 0
result = 2**31
while True:
    max_val = max(A[i],B[j],C[k])
    min_val = min(A[i],B[j],C[k])
    res = abs(max_val - min_val)
    result = min(result,res)
    if result == 0:
        break

    if A[i] < max_val and i < len(A)-1:
        i += 1
    if B[j] < max_val and j < len(B)-1:
        j += 1
    if C[k] < max_val and k < len(C)-1:
        k += 1

    if i == len(A) -1 or j == len(B) -1 or k == len(C) -1:
        max_val = max(A[i], B[j], C[k])
        min_val = min(A[i], B[j], C[k])
        res = abs(max_val - min_val)
        result = min(result, res)
        break
print(result)


