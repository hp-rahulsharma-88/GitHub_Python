#file = open('test.txt')

#print(file.read()) # read the whole content of a file
#print(file.read(7)) # read characters of a file

#print(file.readline()) # read file line by line
#print(file.readline()) # read file line by line

# write a code which prints each line of a method

# line= file.readline() # read first line of a file
# while line!='':
#     print(line)
#     line = file.readline() # read next line of a file

# for line in file.readlines(): # while using readlines method, it creates a list
#     print(line)
#
# file.close()

with open('test.txt', 'r') as reader: # with this need not to mention close file statement
    content = reader.readlines() # a list will be created [afaf, erere, tytyty, yuyuyughghgh]
    reversed(content) # reversed the list [yuyuyughghgh, tytyty, erere, afaf]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)