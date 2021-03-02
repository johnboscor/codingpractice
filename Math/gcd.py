from math import sqrt

def get_factors(A):
    B = []
    for i in range(1,int(sqrt(A))+1):
         if A % i == 0:
            B.append(i)
            if(i != sqrt(A)):
                B.append(int(A//i))

    return list(sorted(B, reverse=True))


def find_gcd(B, num):
    for i in B:
        if num % i == 0:
            return i
    return 0

num1 = 11
num2 = -22

gcd = 0
B = []
if num1 > num2:
    B = get_factors(num1)
    gcd = find_gcd(B,num2)
elif num2 > num1:
    B = get_factors(num2)
    gcd = find_gcd(B,num1)
else:
    gcd = num1

if gcd == 0:
    print(num1*num2)
else:
    print(gcd)


#Faster easier method
def gcd(A, B):
        if B > A:
            A, B = B, A
        while B != 0:
            temp = B
            B = A % B
            A = temp
        return A
print(gcd(6,18))