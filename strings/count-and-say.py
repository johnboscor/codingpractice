#https://www.interviewbit.com/problems/count-and-say/
#1, 11, 21, 1211, 111221, ...

n = 5

if n == 1:
    print('1')
elif n == 2:
    print('11')
else:

    s = '11'
    for i in range(3, n+1):
        temp = ""
        cnt = 1
        s += '$'
        for j in range(1,len(s)):
            if s[j] != s[j-1]:
                temp += str(cnt)
                temp += s[j-1]
                cnt = 1
            else:
                cnt += 1

        s = temp

    print(s)