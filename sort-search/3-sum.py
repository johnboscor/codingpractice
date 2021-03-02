A = [-1, 2, 1, -4]
target = 1

A.sort()
print(A)

i = 0
sum_i = abs(target - sum(A[i:3]))
print(sum_i)
for i in range(1,len(A)):
    #print(i+3)
    if i + 3 > len(A):
        break
    sum_i = min(sum_i,abs(target-sum(A[i:i+3])))

print(sum_i)
# incomplete
