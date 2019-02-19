count = 0
while count < 100:
    count = count + 1

    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    if count % 3 == 0:
        print('Fizz')
    if count % 5 == 0:
        print('Buzz')
    else:
        print(count)
