#Is Unique: Implement an algorithm to determine if a string has all unique characters.

str = 'abcedefgh'

dct = {}
for i in str:
    try:
        if dct[i] == True:
            print('Found duplicate')
            break
    except KeyError:
        dct[i] = True
# O(n) -- time complexity
# O(n) -- space complexity
