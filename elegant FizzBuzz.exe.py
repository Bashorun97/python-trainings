for i in range(1, 345100):
    msg = ''
    if i % 3 == 0:
        msg += 'Fizz'
    if i % 5 == 0:
        msg += 'Buzz'
    print(msg)
