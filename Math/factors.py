from math import sqrt
def allFactors_method1(A):
    B = []
    for i in range(1,A+1):
        if A % i == 0:
            B.append(i)

    return B

def allFactors_method2(A):
    B = []
    for i in range(1,A//2 + 1):
        if A % i == 0:
            B.append(i)
    B.append(A)
    return B

def allFactors_method3(A):
    B = []
    for i in range(1,int(sqrt(A)) + 1):
        if A % i == 0:
            B.append(i)
            if(i != sqrt(A)):
                B.append(int(A//i))
    return sorted(B)

print(allFactors_method1(36))
print(allFactors_method2(36))
print(allFactors_method3(21))