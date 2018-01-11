#!/usr/bin/env python3

#for x in range(0, 3):
total = 0
x = 3
while x < 1000:
    total += x
    print ("We're on time %d" % (x))
    x += 3

# now 5
x = 5
while x < 1000:
    total += x
    print ("We're on time %d" % (x))
    x += 5

x = 15
while x < 1000:
    total -= x
    print ("We're on time %d" % (x))
    x += 15

print("The total is %d" % (total))
