from math import sqrt

def primeNumber(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def primeNumber_sqrtmethod(n):
    if n in (1,2,3):
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
#print(primeNumber(11))
print(primeNumber_sqrtmethod(13))