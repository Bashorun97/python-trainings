def multiply (x, y):
    prod = 0
    while x > 0:
        if x%2 != 0:
            prod = prod + y
            print(prod)
        x = x/2
        y = y + y
    return prod

print(multiply(2, 2))
