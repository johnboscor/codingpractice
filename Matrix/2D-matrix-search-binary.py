#https://www.youtube.com/watch?v=FOa55B9Ikfg

'''
 1 2 3
 4 5 6
 7 8 9
'''

A = [[1,2,3],[4,5,6],[7,8,9]]

row = len(A)
col = len(A[0])
ln = row*col

# number to search
k = 4

start = 0
end = ln - 1

found = False
while start <= end:
    mid = start + (end - start) // 2
    r = mid // col
    c = mid % col
    if A[r][c] == k:
        found = True
        break
    elif A[r][c] < k:
        start = mid + 1
    else:
         end = mid - 1

print(f"Item found = {found}")
