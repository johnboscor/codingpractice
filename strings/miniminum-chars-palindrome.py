#https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/
A = "AACECABAD"
#A = "AACECAAAA"
#A = "ABC"
lg = len(A)

for i in range(1,lg):
    pal = A[-i:][::-1] + A
    print(pal)
    if pal == pal[::-1]:
        print(i)
        break