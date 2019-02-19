def recurse(n):
    if n == 0:
        print('Blastoff!')
    else:
        print (n)
        recurse(n-1)

recurse(6)
