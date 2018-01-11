#!/usr/bin/env python3

limit = int(100)
summ = int(limit * (limit + 1)/2)
sum_sq = int((2 * limit + 1)*(limit + 1)*limit/6)
out = int(summ ** 2 - sum_sq)
print(out)
