#https://www.interviewbit.com/problems/atoi/

A = "98 adfs"
B = ""
for i in range(len(A)):
    if A[i].isdigit():
        B += A[i]
    else:
        break
print(int(B)%(2**32))
