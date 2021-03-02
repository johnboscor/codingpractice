n = 5
a = [ [0] * n for i in range(n)]

start_i=0
start_j=0
start_num = 1
while True:

    for i in range(start_i, n-start_i):
        a[start_i][i] = start_num
        start_num += 1

    for i in range(start_i+1,n - start_j):
        a[i][n-start_j-1] = start_num
        start_num += 1

    for i in range(n - start_i -1, start_i, -1):
        a[n - start_i -1][i-1] = start_num
        start_num += 1

    for i in range(n - start_j - 1, start_j + 1, -1):
        a[i-1][start_j] = start_num
        start_num += 1

    start_i += 1
    start_j += 1
    if start_num > n * n:
        break


for i in a:
    print(i)
