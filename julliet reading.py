#get name of file from the user
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
    exit()

#picks each line in the opened file
#split each line into words

for line in fhand:
    words = line.split()

    index = 0
    for counts in fhand:
        index += 1
        print(index, counts5)
