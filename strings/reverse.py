#https://www.interviewbit.com/problems/reverse-the-string/
A = "the sky is   blue"
B = " ".join(" ".join(A.split()).split(' ')[::-1])
print(B)