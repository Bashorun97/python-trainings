def divisible(limit):
    count = 0
    for num in range(1, limit):
        if num%3 or num%5 == 0:
            count += num
    return count

print(divisible(41000000000))
