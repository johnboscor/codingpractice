a = [1, 2, 3, 4]

def wave_func(a):
    a.sort()
    leng=len(a);
    i = 0
    while True:
        if i >= len(a)-1:
            break
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
        i +=2
    return a

print(wave_func(a))



