roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
         40: "XL", 50: "L", 90: "XC", 100: "C",
         400: "CD", 500: "D", 900: "CM", 1000: "M"}

num = 9
def get_base(num):
    if num > 1000:
        return 1000
    if num > 500 and num < 900:
        return 500
    if num > 100:
        return 100
    if num > 50 and num < 90:
        return 50
    if num > 10:
        return 10
    if num > 5 and num < 9:
        return 5
    else:
        return 1

i = 0
arr = ""

while num > 0:
    base_val = get_base(num)
    val = num // base_val
    try:
        arr += roman[val*base_val]
    except KeyError:
        for i in range(val):
            arr += roman[base_val]
    num -= val*base_val

print(arr)


def intToRoman(A):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]

    return thousands[(A // 1000)] + hundreds[(A % 1000) // 100] + tens[(A % 100) // 10] + ones[A % 10]

print(intToRoman(3454))