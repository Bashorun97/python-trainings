//Naive FizzBuzz
for items in range(1, 21):
    if items % 5 ==  0  and items % 3 == 0:
        print('FizzBuzz')
    elif items % 3 == 0:
        print('Fizz')
        
    elif items % 5 == 0:
        print('Buzz')

    print(items)
