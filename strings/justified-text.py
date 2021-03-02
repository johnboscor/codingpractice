#https://www.interviewbit.com/problems/justified-text/
words = ["This", "is", "a", "example", "of", "text", "justification", "of", "a", "kind."]
words = [ "What", "must", "be", "shall", "be." ]
#words = ["This", "is", "total", "bullshit"]
L = 12


def create_text(text,L,wl,wc):
    temp = ""
    space_a = L - wl
    s_wc = wc - 1
    inter = []
    print(space_a,L,wl,wc)
    if wc == 1:
        temp += text[0].ljust(len(text[0]) + space_a, " ")
    else:
        for i in range(s_wc,0,-1):
            if i == 0:
                inter.reverse(space_a)
                break
            iv = space_a // i
            inter.append(iv)
            space_a = space_a - iv
        inter.reverse()
        print(inter)
        k = 0
        for k in range(len(text)-1):
            temp += text[k].ljust(len(text[k]) + inter[k], " ")
        temp += text[k+1]
    return temp

res = []
text = []
wl = 0
wc = 0
print(words)

for i in words:
    if wl + wc + len(i) > L:
        res.append(create_text(text, L, wl, wc))
        text = []
        text.append(i)
        wl = len(i)
        wc = 1
    else:
        text.append(i)
        wl += len(i)
        wc += 1
if text:
    #res.append(create_text(text, L, wl, wc))
    res.append(' '.join(map(str,text)).ljust(L," "))
print(res)
