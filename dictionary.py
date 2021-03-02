
dict1={"jan":"january", "feb":"february"}

print(dict1["feb"]) # print one element

dict1["mar"] = "March" # add a new element

print(dict1) #print entire dictionary
print(dict1.values()) #print just hte values
print(dict1.keys()) #print the keys
dict1.pop("mar") # pop an element based on key
print(dict1)
dict1.popitem()
print(dict1)  #pop the last element

