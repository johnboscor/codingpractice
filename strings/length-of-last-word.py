s = "hello dda  "
lg = len(s)

length = 0
char_found = 0

while lg > 0:
    if not char_found:
        if s[lg-1] == ' ':
            lg -=1
            continue
        else:
            length += 1
            char_found = True
    else:
        if s[lg-1] == ' ':
            break
        else:
            length += 1
    lg -= 1
print(length)