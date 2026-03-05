#!/usr/bin/python3
import math
from decimal import getcontext, Decimal
getcontext().prec = 50

count = int(input("Wieviel Versuche? "))
x = 0

for k in range(count):
    x += Decimal(math.factorial(4*k) * (1103 + 26390 * k)) / Decimal((math.factorial(k) ** 4 * 396 ** (4 * k)))
    print(f"{k+1:4d}: {9801 / (2 * Decimal(2).sqrt() * x)}")
print(f"  PI: {math.pi}")
