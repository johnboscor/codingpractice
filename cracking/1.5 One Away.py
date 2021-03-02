#One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false

str1 = 'pale'
str2 = 'bale'

def replaceFunction(str1,str2,ln):
    noMatchFound = False
    for i in range(ln):
        if str1[i] != str2[i]:
            if noMatchFound:
                return False
            noMatchFound = True
    return True

def insertFunction(str1, str2,ln):
    for i in range(ln):
        if i == ln -1:
            return True
        if str1[i] != str2[i]:
            if str1[i+1:] != str2[i:]:
                return False
            else:
                return True
def findOneEdits(str1,str2):
    if str1 == str2:
        return True
    l1 = len(str1)
    l2 = len(str2)
    if abs(l1-l2) > 1:
        return False
    if l1 == l2:
        return replaceFunction(str1,str2,l1)
    elif l1 > l2:
        return insertFunction(str1,str2,l1)
    else:
        return insertFunction(str2,str1,l2)

print(findOneEdits(str1,str2))