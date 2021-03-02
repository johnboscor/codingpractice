def find_smaller(str, start, lg1):
    count = 0
    for i in range(start+1, lg1):
        if str[start] > str[i]:
            count += 1
    return count
def find_dup_smaller(start,str):
    from math import factorial as fact
    c = []
    ft = 1
    for i in range(len(str)): # bbbaaa
        if str[start] >= str[i]:
            if str[i] not in c:
                ft = ft * fact(str.count(str[i]))
                c.append(str[i])
    print(ft)
    return ft

def findRank(str):
    from math import factorial as fact
    lg = len(str)
    ft = fact(lg)
    r_ft = 1
    i = 0
    rank = 1
    while i < lg:
        ft = ft // (lg - i)

        r_ft = find_dup_smaller(i,str)
        count = find_smaller(str, i, lg)
        ftt = ((count * ft)//r_ft)%1000003
        rank += ftt

        i += 1
    return rank%1000003

str = "bbbcccaaa"
print(findRank(str))