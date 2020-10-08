import random


def MaximumDiscount(n=int, price=list):
    price.sort(reverse=True)
    print(price)
    sum_of_discount = 0
    for i in range(1, n//3 + 1):
        sum_of_discount += price[i * 3 - 1]
    return sum_of_discount


k = random.randint(4,11)
a = [random.randint(100, 1000) for i in range(0,k)]
print(k, a)
discount = MaximumDiscount(k, a)
print(discount)
