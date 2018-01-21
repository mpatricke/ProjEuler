"""
project euler 028: number spiral diagonal sum

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101, i.e.:
1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 = 101

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""

from datetime import datetime
starttime = datetime.now()

maxSideLen = 1002
sumDiag = 1
lastSide = 1

for sideLen in range(3,maxSideLen,2):

    incr = sideLen - 1

    for side in range(1,5):
        lastSide += incr
        sumDiag += lastSide

    print("For side",sideLen,"; incr =",incr,"; sum = ",sumDiag)

print("Total elapsed time:",datetime.now() - starttime)

