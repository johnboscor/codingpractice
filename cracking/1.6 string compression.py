#String Compression: Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).

st = "abcccccaaa"
ln = len(st)
new_st = ""
curr = st[0]
count = 1
for i in range(1,ln):
    if st[i] != st[i-1]:
        new_st += curr + str(count)
        count = 1
        curr = st[i]
    else:
        count += 1
new_st += curr + str(count)

print(new_st)

