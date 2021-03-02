#https://www.interviewbit.com/problems/excel-column-title/
from math import log
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']

##return number from title
sum = 0
A = "AAA"
for i in range(len(A)):
    sum = sum*26 + int(l.index(A[i]) + 1)
print(sum)

num=980089
##return title from given number:
title = ""
while num > 0:
    val = num % 26
    title = l[val - 1] + title
    num = num // 26

print(title)

