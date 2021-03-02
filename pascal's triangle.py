# return k=th row of pascal's triangle:

#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#[1]
#[1, 1]
#[1, 2, 1]
#[1, 3, 3, 1]
#[1, 4, 6, 4, 1]

k = 4

#first lets generate a pascal's triangle:

a = []

for i in range(k+1):
    b = []
    for j in range(i+1):
        if j == 0 or j == i:
            b.append(1)
        else:
            b.append(a[i-1][j] + a[i-1][j-1])
    a.append(b)

for i in a:
    print(i)
