fhand = open('mat.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
