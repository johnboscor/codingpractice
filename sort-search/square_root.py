#square root using binary search
#https://www.geeksforgeeks.org/square-root-of-an-integer/


def squart_binary_search(x):
    from math import floor
    if x == 0 or x == 1:
        return x

    start = 1
    end = x
    while start <= end:
        mid = start + (end - start) // 2
        if mid*mid == x:
            return mid

        if mid*mid > x:
            end = mid - 1
        else:
            start = mid + 1
    return floor((start+end)/2)

print(squart_binary_search(49))

