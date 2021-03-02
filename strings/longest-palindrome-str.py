#https://www.interviewbit.com/problems/longest-palindromic-substring/
a = "abacdfgdcaba"
#a = "a"
#a = "aaaabaaa"

#print((a[1:])[::-1])
#print(a[0:1])
res = [0,1] # start index, len
for i in range(len(a)):
    for j in range(i + res[1], len(a)):
        #print(f"i={i},j={j},k={k}")
        #print(a[i:j+1],(a[i:j+1])[::-1],len(a[i:j+1]))
        if a[i:j+1] == (a[i:j+1])[::-1] and len(a[i:j+1]) > res[1]:
            res = [i, len(a[i:j+1])]
#print(res)
print(a[res[0]:res[1]+res[0]])


#Alternative method to expand from middle

def findPalindrome(a,start,end):
    global max_len
    global start_p
    while start >= 0 and end < len(a) and a[start] == a[end]:
        start -= 1
        end += 1
    curr_len = end - start - 1
    if max_len < curr_len:
        max_len = curr_len
        start_p = start + 1

a = "ghsdfgaabaacdfgdcaba"
if len(a) < 2:
    print(a)
start_p = 0
max_len = 0
for i in range(len(a)):
    findPalindrome(a,i,i)
    findPalindrome(a,i,i+1)

print(a[start_p:start_p+max_len])


