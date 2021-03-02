
'''
#normal iterative non efficient method
def hasdup(ints):
    for i in range(len(ints)):
        for j in range(i+1,len(ints)):
            print("iterating")
            if ints[i] == ints[j]:
                return True

    return False
'''

'''
#a little better method since sort will order elements
def hasdup(ints):
    ints.sort()
    for i in range(len(ints)):
        for j in range(i+1,len(ints)):
            print("iterating")
            if ints[i] == ints[j]:
                return True

    return False
'''

#a little faster method
def hasdup(ints):
    seen = []
    for i in ints:
        print("iterating")
        if i in seen:
            return True
        seen.append(i)

    return False

ints= [34,54,23,52,23,32]
print(hasdup(ints))

