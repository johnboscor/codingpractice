#https://www.interviewbit.com/problems/compare-version-numbers/
a = "013.12"
b = "13.1"
def compareVersion(A, B):
    A = A.split('.')
    B = B.split('.')
    if len(B) > len(A):
        A += ["0" for i in range(len(B) - len(A))]
    else:
        B += ["0" for i in range(len(A) - len(B))]

    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            return 1
        elif int(A[i]) < int(B[i]):
            return -1

    return 0

print(compareVersion(a,b))