
def monthabbr():
    
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    n = int(input('Enter any month number (1-12): '))
    pos = (n-1)*3
    abbr = months[pos:pos+3]
    print('The abbreviation is %s' '.' %abbr)

monthabbr()
