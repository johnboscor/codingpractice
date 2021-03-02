from functools import cmp_to_key

a = [3, 30, 34, 5, 9]

def brute_sort(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            num1 = int(b[i] + b[j])
            num2 = int(b[j] + b[i])
            if num1 < num2:
                temp = b[j]
                b[j] = b[i]
                b[i] = temp


def largestNumber(a):
    b = []
    for i in a:
        b.append(str(i))

    brute_sort(b)

    return int(''.join(b))


def largestNumber_fastest(A):
    ''' When comparing numbers we must pick the one leading
        to the best concatenated result:
        787978 > 787879  so 7879 is 'bigger' than 78
                    but     7879 is 'less' than 788
    '''

    # Convert to string once, for proper comparison a+b vs b+a
    A = map(str, A)

    key = cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1)
    res = ''.join(sorted(A, key=key, reverse=True))
    # Must left trim 0, apparently
    res = res.lstrip('0')
    return res if res else '0'

#print(largestNumber(a))
print(largestNumber_fastest(a))
