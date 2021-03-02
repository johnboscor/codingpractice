


def find_smaller(str, start, lg1):
    count = 0
    for i in range(start+1, lg1):
        if str[start] > str[i]:
            count += 1
    return count

def findRank(str):
    from math import factorial as fact
    lg = len(str)
    ft = fact(lg)
    i = 0
    rank = 1
    while i < lg:
        ft = ft // (lg - i)
        count = find_smaller(str, i, lg)
        rank = rank + (count * ft)
        i += 1
    return rank%1000003

str = "DTNGJPURFHYEW"
print(findRank(str))