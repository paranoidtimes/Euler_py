#!/usr/bin/env python3

number = 20 # largest number
count = 2 # start at first prime

primes=[2] # seed list with first prime

finaltotal = 1
exp = 0

while 1: # run the first prime seperately, otherwise it would be skipped in the prime check
    testexp = 2 ** exp
    if testexp < number:
        exp += 1
        continue
    else:
        finaltotal = finaltotal * 2 ** (exp - 1)
        count += 1
        break
        
def primecheck(current):
    for val in primes:
        if current % val == 0: # not a prime
            return(1)

while count <= number:
    # test if prime
    if primecheck(count) == 1:
        count += 1
        continue
    exp = 1
    while 1:
        testexp = count ** exp
        if testexp <= number:
            exp += 1
            continue
        else:
            finaltotal = finaltotal * count ** (exp - 1)
            primes.insert(len(primes),count)
            count += 1
            break

print(finaltotal)
