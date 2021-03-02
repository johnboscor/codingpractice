
contents = open('test-file','r')
print(contents.readable()) # check if file is readable

#print(contents.readline()) # reads one line at a time and moves the pointer to next line

#print(contents.readlines()) # reads entire file into a array

for line in contents.readlines():   #read each line at a time and print it.
    print(line)

contents.close() # always remember to close the file
contents = open('test-file','a') # append to a file

contents.write("\nnew data - 1234") # writes to a file at the end. Make sure to add \n to write in new line
contents.writelines("new data - 12345")
contents.close()