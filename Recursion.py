def print_n(s, n):
    if n<=0:
        return
    print (s)
    print_n(s, n-1)
