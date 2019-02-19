def after_discount(n):
    discount = (n)- n*0.4
    after = discount-0.75
    return after*59 + (discount-3)

def rake(n):
    return after_discount(n)*2

print(rake(34))
