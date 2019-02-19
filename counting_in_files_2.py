fname = input("Enter the file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

fhand = open('mat.txt')
index = 0
lst = []
for i in fhand:
    words = i.split()
    
    for sole in words:
        lst.append(sole)
        index +=1
print("The total number of words in the file is %d" %index)
        
