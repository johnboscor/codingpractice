a="101"


def countOnes(A):
    empty = []
    a = list(A)

    if a.count("1") == len(a):
        return empty

    b = []
    max_nums = a.count("1")
    location = [1, 1]
    for i in range(len(a)):
        for j in range(i, len(a)):
            b = a.copy()
            if i == j:
                b[i] = str(1 - int(b[i]))
            else:
                for k in range(i, j + 1):
                    b[k] = str(1 - int(b[k]))
            # b[j] = 1 - (b[j])

            if b.count("1") > max_nums:
                location = [i + 1, j + 1]
                max_nums = b.count("1")
            # print(b,location,b.count("1"),max_nums)
        # print(f"({i},{j}) array-{b}, bcount-{b.count(1)}, max-val-{max_nums}, {location}")

    return location

def countOnes_kadane(A):

    a = [1 if i == '0' else -1 for i in A]
    curr_sum=0
    max_sum=0
    res = []
    start=0
    for i in range(len(A)):
        curr_sum += a[i]
        if curr_sum > max_sum and curr_sum >=0:
            max_sum=curr_sum
            res = [start+1, i+1]
        else:
            start +=1
            curr_sum=0
    return res


#print(countOnes(a))
print(countOnes_kadane(a))






