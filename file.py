fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'

file = open(fileName, mode = WRITE)
file.write('This is the first line\n')
file.write('This is the second line')
file.close()

print('File written sucessfully')


