stg="ADOBECODEBABCD"
sub = "ABC"

table = {}
for c in sub:
    try:
	    table[c] +=1
    except KeyError:
        table[c] = 1

counter = len(table)
stg_len = len(stg)
begin = end = 0
min_len = float('inf')
result = []
while end < stg_len:
    curr_char = stg[end]
    if curr_char in table:
        table[curr_char] -= 1
        if table[curr_char] == 0:
            counter -= 1
    end += 1
    print(begin,end,counter,table)
    while counter == 0:
        if (end - begin) < min_len:
            min_len = end - begin
            result = stg[begin:min_len]

        start_char = stg[begin]
        if start_char in table:
            table[start_char] += 1
            if table[start_char] > 0:
                counter += 1
        begin += 1
        print('inside',begin,end,counter,table)
print(begin,end)
print(result)