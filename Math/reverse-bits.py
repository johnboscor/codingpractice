#https://www.interviewbit.com/problems/reverse-bits/
A = 3
if A==0:
    print(0)
y = str(bin(A)[2:]).zfill(32)
y = y[::-1]
print(int(y,2))
# or simply use:
print(int(str(bin(A)[2:]).zfill(32)[::-1], 2))