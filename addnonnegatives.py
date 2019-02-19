entry = 0
sum = 0

print("Enter numbers to sum, negative ends list:")

while entry >=0:
    entry = eval(input())
    if entry >= 0:
        sum += entry
print("Sum =", sum)
