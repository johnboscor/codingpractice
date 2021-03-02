

b = []
def decimalToBinary(n):
    while n > 0:
        rem = n%2
        b.append(rem)
        n = int(n/2)
    b.reverse()
    return ''.join(map(str,b))
print(decimalToBinary(15))



def findNoDigs(n):
    dig=0
    while n > 0:
        dig += 1
        n = int(n/10)
    return dig

print(findNoDigs(2032))

def addAllDigits(n):
    sum_val = 0
    while n > 0:
        rem = n // 10
        sum_val += n - (rem*10)
        n = n // 10

    return sum_val

print(addAllDigits(1234))

def binaryToDecimal(n):
    i = 0
    dec = 0
    while n > 0:
        rem = n // 10
        val = n - (rem*10)
        if val:
            dec += pow(2,i)
        i += 1
        n = n // 10
    return(dec)
print(binaryToDecimal(111))