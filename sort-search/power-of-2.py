#https://www.interviewbit.com/problems/power-of-2/
from math import pow,sqrt
num = 2

while num > 1:
    num = int(A)
    if num == 0 or num == 1:
        print(0)
    while num > 1:
        if num % 2 != 0:
            print(0)
        num = num // 2


#Another solution
    def power(self, A):
        n = int(A)
        # print(n)
        if n == 1:
            return 0
        if n & (n - 1) == 0:
            # print(time.clock())
            return 1
        else:
            # print(time.clock())
            return 0


