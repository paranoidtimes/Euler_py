#!/usr/bin/env python3

a = 999
#b = 990
largest = 111111

def reverseNumber(number):
    reverse = 0
    while number > 0:
        reverse = int(reverse * 10 + number % 10)
        number = int(number / 10)
    #print(reverse)
    return(reverse)


while a >= 100:
    b = 990
    while b >= 100:
        prod = a * b
        if prod == reverseNumber(prod):
            if prod > largest:
                largest = prod
                a -= 1
                continue
        b -= 11
    a -= 1
    

print(largest)

