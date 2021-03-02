#https://www.interviewbit.com/problems/median-of-array/

A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]

C = A + B
C.sort()
print(C)
lg = len(C)
if lg % 2 == 0:
    print((C[(lg-1)//2] + C[lg//2]) / 2.0)
else:
    print(C[lg//2])
