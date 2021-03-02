from bisect import bisect_right as upper_bound

#arr = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
arr = [[1],[3],[3]]
r = len(arr)
c = len(arr[0])

lg = r*c // 2

mini = arr[0][0]
maxi = 0
for i in range(r):
    if arr[i][0] < mini:
        mini = arr[i][0]
    if arr[i][c-1] > maxi:
        maxi = arr[i][c-1]
print(mini,maxi)
while mini < maxi:
    mid = mini + (maxi - mini) // 2

    j = 0
    for i in range(r):
        j += upper_bound(arr[i],mid)

    if j > lg:
        maxi = mid
    else:
        mini = mid + 1

print(f"Median is {mini}")