x = 12
y = True
while y:
    predict = (int(input("Make a numerical guess: ")))

    if predict == x:
        print("You made a right guess")

    elif predict < x:
        print("Less than than the number")

    else:
        print("Greater than than the number")

else:
    print("Game over")

print("Done!")
    
