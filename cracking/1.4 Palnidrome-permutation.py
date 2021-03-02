#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#A palindrome is a word or phrase that is the same forwards and backwards. A permutation
#is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

#find the count of each characters

st = "Tact Coa"
st = st.lower()
dct = {}
for i in st:
    if i == " ":
        continue
    try:
        if dct[i]:
            dct[i] += 1
    except KeyError:
        dct[i] = 1

numOdds = 0
for i in dct:
    if dct[i] % 2 != 0:
        numOdds += 1
        if numOdds > 1:
            print("Not a permutation")
            break

print(ord('a'))
