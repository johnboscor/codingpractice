A = [2, 4, 6]

def binary_count(n):
    if n ==0:
        return 0
    count = 0
    while n>0:
        if n % 2:
            count += 1
        n = n // 2
    return count
print(sum(binary_count(A[i] ^ A[j]) for i in range(len(A)) for j in range(len(A))))

##*******************FASTER 0(n) solution**********************
#A = [2, 4, 6] = [010, 100, 110]
#At bit position 0 (LSB): x = 3, y = 0
#At bit position 1: x = 1, y = 2
#At bit position 2(MSB): x = 1, y = 2

#Total sum = number of pairs having different bit at each bit-position = (2 * 3 * 0) + (2 * 1 * 2) + (2 * 1 * 2) = 8
l = []
for i in A:
    l.append('{:032b}'.format(i))  # converts to 32bit binary
l= list(zip(*l))  # create a list with each bit for every element
val = 0
for i in l:
    a = i.count('1')
    b = i.count('0')
    val += 2*a*b
print(val)
