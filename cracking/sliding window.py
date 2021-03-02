def segment(x, space):

    result = []
    result.append(min(space[:x])) #  get the first window here into a list
    for i in range(len(space) - x):
        next_element = space[i + x]
        prev_element = space[i]
        if next_element < result[-1]:  #compare element and if lesser add it to the list
            result.append(next_element)
        else:
            if result[-1] == prev_element:
                result.append(min(space[i + 1:i + 1 + x])) # if equal to last element, append the min of next element in
            else:                                          # the current window to the result array
                result.append(result[-1]) # else just append the last element
    return max(result)



space=[2,5,4,6,8]
print(segment(3,space))
from collections import deque

def sliding_deque(x,space):
    res = []
    min_val = min(space[:x])
    min_in = space[:x]
    min_val = min_in.index(min_val)
    dq = deque([min_val])
    for i in range(len(space) - x):
        res.append(dq[0])

        print(dq.)
        for item in dq:
            if item < i+x:
                dq.popleft()

        if space[dq[0]] < space[i+x]:
            while dq and space[dq[0]] < space[i+x]:
                dq.popleft()
            dq.appendleft(i+x)
        else:
            dq.append(i+x)

    return min(res)

print(sliding_deque(3,space))