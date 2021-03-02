#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
str1 = 'john'
str2 = 'nohj'

def findPermutation(str1,str2):
    dct = {}
    if len(str1) != len(str2):
        print('Not equal')
        return False
    for i in str1:
        try:
            if dct[i]:
                dct[i] += 1
        except KeyError:
            dct[i] = 1
    for i in str2:
        try:
            if dct[i] <= 0:
                print('Not equal')
                return False
            else:
                dct [i] -= 1
        except KeyError:
            print('Not equal')
            return False
    return True

findPermutation(str1,str2)
