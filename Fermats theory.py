import math
print("This is a program to test for the validity of fermats theory")
print("Input values for the variables below")

num1 = int(input("a:"))
num2 = int(input("b:"))
num3 = int(input("c:"))
exponent = int(input("exp:"))

def check_fermat ():
    a = math.pow(num1, exponent)
    b = math.pow(num2, exponent)
    c = math.pow(num3, exponent)
    total = a + b

    if (exponent>2):
        if (total == c):
            print("Holy Smokes! Fermat was wrong")
            return False
        else:
            print('Fermat was correct!!')
            return True

    elif(exponent<2):
        print("Error!!! Exponent must be greater than 2")
        
check_fermat()
