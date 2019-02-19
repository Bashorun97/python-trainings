
char = str(input("Input an argument: "))
msg = ''

def is_palindrome(char):
    if char[0:] == char[::-1]:
         msg = "It's a palindrome"
    else:
        msg = "It's not a palindrome"
    print(msg)
    
is_palindrome(char)
