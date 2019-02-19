''' import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
'''

''' def collatz(number):
    if number % 2 == 0:
        num = number // 2
        return num
    else:
        return 3 * number + 1
coll=collatz(5)
print(coll)
'''


def sum_divisible_by_k(k, start, limit):
    stop = int((limit-1)/float(k))
    return k*(stop+start)*(stop-start+1)/2

def divisible_by_3_or_5(divisors=[3, 5], start=0, stop=10):
    total = 0
    for divisor in divisors:
        total += sum_divisible_by_k(divisor, start, stop)
        
    product =  divisors[0]*divisors[1]

    return total - sum_divisible_by_k(product, start, stop)

print(divisible_by_3_or_5(divisors=[3, 5], start=0, stop=10))
'''

def divisible(limit = 1000):
    count = 0
    for num in range(1, limit):
        if num%3 or num%5 == 0:
            count += num
    return count

print(divisible(limit = 1000))

'''
    


    
    

