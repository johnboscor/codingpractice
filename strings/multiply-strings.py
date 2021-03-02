#https://www.interviewbit.com/problems/multiply-strings/

a = "1234"
b = "1234"

#Convert str to list and also convert each character to int.
#Also reverse it.
a = list(map(int,reversed(a)))
b = list(map(int,reversed(b)))
print(a,b)

lena, lenb = len(a), len(b)

res = [0]*(lena+lenb)
for i in range(lena):
    for j in range(lenb):
        res[i+j] += a[i] * b[j]
        res[i+j+1] += res[i+j] // 10
        res[i+j] %= 10

res = ''.join(map(str,reversed(res))).lstrip('0')  # join and remove leading zeros
print(res)