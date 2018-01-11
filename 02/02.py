#!/usr/bin/env python3

# get fib sequence

x = 1
y = 1
z = x + y
total = 0

while z < 4000000:
    total += z
    x = y + z
    y = z + x
    z = x + y

print(total)
