#https://www.interviewbit.com/problems/implement-strstr/

stg = "hello, how are you today?"

sub = "how are"

try:
    print(stg.index(sub))
except:
    print("-1")


# Method without using built in functions
len1 = len(stg)
len2 = len(sub)

for i in range(len1):
    if len2 + i > len1:
        break
    if stg[i:len2+i] == sub:
        break

print(i)
