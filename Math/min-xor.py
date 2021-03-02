def findMinXor(xs):
    xs.sort()
    print(list(zip(xs,xs[1:])))
    print()
    return min(map(lambda p: p[0] ^ p[1], zip(xs, xs[1:])))

A = [0, 2, 5, 7]
print(findMinXor(A))

print(4^0)