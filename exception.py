from __future__ import print_function

while True:
    try:
        x = float(input("enter a value for x: "))
        y = float(input("enetr a value for y: "))

        if x==0 or y==0:
            break

        z = (x/2) / (x-y)
        print(z)
    except NameError as e:
        print("Name error")
        print("Error message: ", str(e))
    except Exception as e:
        print("Exception error")
        print("Error message: ",str(e))
