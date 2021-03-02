#https://www.interviewbit.com/problems/implement-power-function/

def pow(A, B,C):
    if B == 0:
        return 1%C
    if A % 2:
        B = B // 2
    return (A * pow(A,B // 2,C) % C)


print(pow(71045970,41535484,20805472))

