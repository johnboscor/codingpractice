#Another solution:
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
A = [0, 0, 0, 1]
sum_a = sum(A)
B = set(A)
print(B)
sum_b = sum(B)
dup = (3*sum_b - sum_a) // 2
print(dup)

def singleNumber(A):
    x = 0
    for n in A:
        x = x ^ n
    return x

print(singleNumber(A))

A.in