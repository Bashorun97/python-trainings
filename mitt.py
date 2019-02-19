'''
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of' , x, 'is', ans)
'''

'''
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jone', '9843']
]

username = str(input('User name: '))
pin = input('PIN code: ')

if [username, pin] in database: print ('Access granted')
'''
'''
# Print a fromatted price list with a given width

width = input('Please enter width: ')
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print('=' * width)

print(header_format % (item_width, 'Item', price_width, 'Price')
      
print('-' * width)

print(format % (item_width, 'Apples', price_width, 0.4)
print(format % (item_width, 'Pears', price_width, 0.5)
print(format % (item_width, 'Cantaloupes', price_width, 1.92)
print(format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8)
print(format & (item_width, 'Pruces (4 lbs.)', price_width, 12)

print('=' * width)       
'''

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
        },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }

}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = str(input('Name: '))
request = str(input('Phone nember (p) or address (a)?'))

if request == 'p': key = 'phone'
if request == 'a': key ='addr'

if name in people :
    print ("%s's %s is %s." % (name, labels[key], people[name][key]))
