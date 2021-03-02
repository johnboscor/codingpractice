from math import sqrt,pow
from math import log, sqrt


#easy method, log(num) to base of a number will give the power value. If it is a whole number then we have find a power.
#A=30
#print((log(32,2)))

def findPower(A):
    if A == 1:
        return 1
    for i in range(2, int(sqrt(A)) + 1 ):
        x = round(log(A,i),5)
        if x % 1 == 0:
            return 1
    return 0

print(findPower(16))
'''
i=2
while c > 0:
    if(pow(2,c)) == num:
        print(True)
        break
    c -= 1
    i += 1
'''


