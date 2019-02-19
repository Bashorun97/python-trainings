hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    pay = hours*1.5*rate
    print('Pay: ', pay)
else:
    pay = hours*rate
    print('Pay: ', pay)
