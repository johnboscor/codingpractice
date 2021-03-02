n = 4

a = [ [n] * (2*n-1) for i in range((n*2)-1)]
lg = n*2 -1

start_i=1
start_j=1
start_num = n-1
while True:

    for i in range(start_i, lg-start_i):
        a[start_i][i] = start_num

    for i in range(lg - start_j -1, start_j,-1):
        a[i][lg-start_j-1] = start_num

    for i in range(lg - start_i-1, start_i-1,-1):
        a[lg-start_i-1][i] = start_num

    for i in range(lg - start_j-1, start_j-1,-1):
        a[i][start_j] = start_num

    start_i += 1
    start_j += 1
    start_num -= 1
    if start_num <= 0:
        break


for i in a:
    print(i)