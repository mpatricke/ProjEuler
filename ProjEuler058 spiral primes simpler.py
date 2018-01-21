"""
project euler 058: spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with
side length 7 is formed:

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but
what is more interesting is that 8 out of the 13 numbers lying along both diagonals are
prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side
length 9 will be formed. If this process is continued, what is the side length of the
square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

from datetime import datetime
from math import sqrt
starttime = datetime.now()


#=============
# build a list of the numbers on the diagonal
#
# maxSideLen  prime on the diagonals
#     2901        13.42%     0'16"    0'18"
#     3901        12.88%     0'32"    0'27"
#     4901        12.58%     0'45"    0'44"
#     5901        12.21%     1'14"
#     6901        %    
#     7901        %
#     8901        %
#     9901        
#
diagPrimPercent = 100
maxSideLen = 3

startDiagNo = 1
startPrimNo = 2
diagList = [1]
diagPrimList = []
diagLast = 1
diagPrimTarget = 10.0

while diagPrimPercent >= diagPrimTarget:
    finishNo = maxSideLen**2

    #=============
    # generate list of numbers on the diagonal for square of maxSideLen
    diagNextFour = []
    for i in range(startDiagNo,maxSideLen,2):
        i = i + 1
        for corner in range(4):
            diagLast += i
            diagNextFour.append(diagLast)
            corner += 1

    for i in range(len(diagNextFour)):
        diagList.append(diagNextFour[i])

    lenDL = len(diagList)
    startDiagNo = maxSideLen

    #=============
    # check which of the additional diagonal nos are prime

    for i in range(len(diagNextFour)):
        notPrime = 0
        if diagNextFour[i]%2 == 0:
            break

        if int(sqrt(diagNextFour[i])) == diagNextFour[i]:
            break

        # this is the expensive part - how to simplify?
        for j in range(3,int(sqrt(diagNextFour[i]))+1,2):
            if diagNextFour[i]%j == 0:
                notPrime = 1
                break

        if notPrime == 0:
            diagPrimList.append(diagNextFour[i])

    #=============
    # how many diagonal numbers are prime?
    diagPrimCount = len(diagPrimList)
    diagPrimPercent = int((diagPrimCount / lenDL) * 100)

    if maxSideLen < 21 or (maxSideLen+1)%500 == 0 or diagPrimPercent < diagPrimTarget:
        print("------")
        print("A spiral square of side",maxSideLen,"has",finishNo,"elements, of which",lenDL,"are on the diagonal.")
        print(diagPrimCount,"of the diagonal elements are prime, or",diagPrimPercent,"%. Try side length =",maxSideLen+2)
        print("Total elapsed time:",datetime.now() - starttime)

    primIndIncr = (maxSideLen*2) + ((maxSideLen + 2) * 2)
    maxSideLen += 2


#print("------")
#print("A spiral square of side",maxSideLen,"has",finishNo,"elements, of which",lenDL,"are on the diagonal.")
#print(diagPrimCount,"of the diagonal elements are prime, or",diagPrimPercent,"%. Try side length =",maxSideLen+2)
#print("Total elapsed time:",datetime.now() - starttime)

