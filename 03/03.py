#!/usr/bin/env python3

number = 60085147514323
count = 2

while count <= number:
    if number % count == 0:
        newnum = number / count
        number = newnum
        print(count)
        continue
    count += 1
