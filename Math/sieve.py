#https://www.interviewbit.com/problems/prime-numbers/

from math import sqrt

def primeNumber(n):
    a = [1]*(n+1)
    print(a)
    a[0] = 0
    a[1] = 0
    for i in range(2, int(sqrt(n))+1):
        if a[i] == 1:
            for j in range(2,n):
                if i*j > n:
                    break
                a[i*j] = 0
    print(a)

    return [i for i,j in enumerate(a) if j]

print(primeNumber(13))