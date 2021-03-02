#https://www.interviewbit.com/problems/number-of-1-bits/

A = 122334
#Easy but slow solution
binary = '{:032b}'.format(A)
print(binary.count('1'))

#Faster solution. A & (A-1) resets the last set bit
count = 0
while A > 0:
    A = A & (A-1)
    count += 1

print(count)