print("Enter a name(s) to store names party invitees and 'Done' to print out invitees")
guests = ['zzzz']
name = ' '
space = ''

while name != 'Done':
    name = input('Enter guest name: ')
    guests.append(name)

guests.remove('Done')
guests.sort()
guests[-1] = 'are changing the world'

for guest in guests:
    print(guest, space, end='')
