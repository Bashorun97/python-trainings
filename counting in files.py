fname = input("Enter the file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

index = 0
total = 0
for i in fhand:
    words = i.split()
    
    for sole in words:
        index += 1
total = total + index
print("The total number of words in the file is %d" %total)
