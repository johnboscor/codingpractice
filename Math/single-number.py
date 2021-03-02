#https://www.interviewbit.com/problems/single-number/

#longer solution using extra memory
A = [1, 2, 2, 3, 1]
B = []
for i in A:
    if i in B:
        B.remove(i)
    else:
        B.append(i)
print(B[0])

#Another solution:
sum_a = sum(A)
B = set(A)
sum_b = sum(B)
dup = 2*sum_b - sum_a
print(dup)

#Using bitwise
def singleNumber(A):
    x = 0
    for n in A:
        x = x ^ n

    return x
print(singleNumber(A))

a