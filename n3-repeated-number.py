

A = [1, 2, 3, 2, 1]
A = [ 1000441, 1000441, 1000994 ]

range = len(A) // 3

'''
def repeatedNumber(A):
    range = len(A) // 3
    B=sorted(A)
    print(B)
    for i in A:
        if A.count(i) > range:
            return(i)

    return(-1)
print(repeatedNumber(A))    
'''

def repeatedNumber_dict(A):
    range = len(A)//3
    dict1 = {}
    for i in A:
        dict1[i] = 0

    for i in A:
        dict1[i] += 1

    sorted(dict1.items(), key=lambda a: a[1])
    if list(dict1.values())[0] > range:
        return list(dict1.keys())[0]
    return -1

print(repeatedNumber_dict(A))


