#Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

#If there is no solution possible, return -1.

a = [3, 5, 4, 2]
#a = [1,10]
# (3,0), (5,1), (4,2) (2,3)  store value and store index
# (2,3), (3,0), (4,2), (5,1)  sort based on value

def maximumGap(A):
    array = list(range(len(A)))
    array.sort(key=lambda i: A[i])
    print(array)
    maxDistance = 0
    minSofar = array[0]
    for i in array:
        if i <= minSofar:
            minSofar = i
        else:
            maxDistance = max(maxDistance, i - minSofar)
    return maxDistance

print(maximumGap(a))
'''
b = []
for i in range (len(a)):
    b.append([a[i],i])
b.sort()
print(b)

mini = b[0][1]
max_val = 0
for i in range(len(b)-1):
        mini = min(mini, b[i][1])
        max_val = max(max_val, b[i][1] - mini)

print(max_val)
'''
#brute force
'''
max_diff = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if(a[i]) <= a[j]:
            max_diff = max(max_diff, j-i)

print(max_diff)
'''
