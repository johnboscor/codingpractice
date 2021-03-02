from math import sqrt


def primesum(n):
    pnum = [1] * (n + 1)
    pnum[0] = 0
    pnum[1] = 0
    for i in range(2, int(sqrt(n)) + 1):
        if pnum[i] == 1:
            for j in range(2, n):
                if i * j > n:
                    break
                pnum[i * j] = 0

    arr = [i for i, j in enumerate(pnum) if j]

    temp = []
    ans = []
    for i in arr:
        if (n - i) in temp:
            ans = [n-i, i]
            break
        elif i * i == n:
            ans = [i, i]
            break
        else:
            temp.append(i)

    return ans

print(primesum(10))

