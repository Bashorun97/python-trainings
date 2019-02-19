'''Abstraction
    with dictionaries
'''

'''
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magnus Lie Hetland'
my_sister = 'Anne Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)
storage['first']['Anne']

print(storage['first']['Anne'])
print(storage)

girls = ['alice', 'bernice', 'clarice', 'claron']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:5
    letterGirls.setdefault(girl[0], []).append(girl)
print(b+'+'+g for b in boys for g in letterGirls[b[0]])
'''
'''
def flexible(init, *flex):
    print(init)
    print(flex)
flexible(init = 'New flex')

'''
