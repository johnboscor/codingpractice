A = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
C = [ list(i) for i in zip(*A)]
print(C)

from math import log

print(log(8,2))


A = [1, 2, 3, 4, 5]


A = "cat"
B = {"A":1, "B":2}
print(''.join(sorted(A)))
print(B["A"])
A=15
binary = bin(256)[2:].zfill(32)
print(binary)

A = [1, 2, 3, 4, 5]

A = A[4:] + A[:3]
print(A)

file1 = open("test-file",'w')
file1.write("hello123\n")
file1.close()
file1 = open("test-file",'r')
for line in file1.readlines():
    print(line)

#num1 = 6, num2 = 3
def findGcd(num1, num2):
    if num1 < num2:
        num2, num1 = num1, num2

    while num2 != 0:
        temp = num2
        num2 = num1%num2
        num1 = temp
    return num1

num1 = 10
num2 = 2
print(f'gcd of {num1} and {num2} is {findGcd(num1,num2)}')

