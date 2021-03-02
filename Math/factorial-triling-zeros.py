#https://www.interviewbit.com/problems/trailing-zeros-in-factorial/

num=100
i = 5
zeros = 0
while True:
    rem = num // i
    i *= 5
    zeros += rem
    if rem <= 0:
        break

print(zeros)
#method which fails for long numbers but works otherwise.
'''
from math import factorial
n=9938
def fact(n):
    if n > 0:
        return n*fact(n-1)
    else:
        return 1

f = factorial(9247)
rem=1
count = 0
while f > 0:
    rem = f % 10
    if not rem:
        count +=1
    else:
        break
    f = int(f//10)

print(f"Number of trailing zeros: {count}")
'''