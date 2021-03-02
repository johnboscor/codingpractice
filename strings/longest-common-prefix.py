#https://www.interviewbit.com/problems/longest-common-prefix/

#A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "ab", "abcd"];

def lcp(str1,str2):
    l1 = len(str1) -1
    l2 = len(str2) -1
    i = j = 0
    res = ""
    while i <= l1 and j <= l2:
        if str1[i] != str2[j]:
            break
        res += str1[i]
        i +=1
        j +=1
    return res

lg = len(A)
prefix = A[0]
for i in range(1,lg):
    prefix = lcp(prefix,A[i])

print(prefix)



