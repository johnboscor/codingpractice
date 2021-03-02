#https://www.interviewbit.com/problems/reverse-integer/

num = 12345
if num < 0:
    num = -(num)
rev = 0
while num > 0:
    temp = num % 10
    rev = rev*10 + temp
    num = num // 10

print(rev)


