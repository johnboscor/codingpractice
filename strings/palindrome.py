#https://www.interviewbit.com/problems/palindrome-string/
#consider only alpha-numeric chars
A = "A man, a plan, a canal: Panama"

A = A.lower()
C = []
for i in A:
    if i.isalnum():
        C += i
C=''.join(C)
print(C)
print(C[::-1])
if C == C[::-1]:
    print("Palindrome")
else:
    print("Not a palidrome")