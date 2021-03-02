#https://www.interviewbit.com/problems/anagrams/

#Input : cat dog god tca
#Output : [[1, 4], [2, 3]]

A = ['cat','dog','god','tca']

hash_map = {}
for i, val in enumerate(A):
    val = ''.join(sorted(val))
    if val in hash_map:
        hash_map[val] += [i+1]
    else:
        hash_map[val] = [i + 1]

print(list(hash_map.values()))