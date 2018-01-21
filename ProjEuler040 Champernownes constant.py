"""
Project Euler 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789 10 11 12 13 14 15 16 17 18 19 20 21...

=>
    0.123456789101112131415161718192021...
                 ^

It can be seen that the 12th digit of the fractional part is 1. If dn represents
the nth digit of the fractional part, find the value of the following expression:
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from datetime import datetime
starttime = datetime.now()

maxI = 1000000
targetI = 1
decimalString = ''

for i in range(maxI):
    decimalString += str(i)

    if len(decimalString) > maxI:
        break

nthProduct = 1

while targetI < len(decimalString):
    ithChar = int(decimalString[targetI])
    nthProduct *= ithChar
    print(targetI,"th char =", ithChar,"; nth product =",nthProduct)
    targetI *= 10

print("------")
print("Completion time", datetime.now() - starttime)
