
A=[4,3,11,1,2,6,9]

num = 5
left = 0
right = len(A)

while left < right:
    mid = (right - left)//2 + left
    if num == A[mid]:
        print('Number found')
        exit(0)
    if num > A[mid]:
        left = mid + 1
    else:
        right = mid

print('Number not found')