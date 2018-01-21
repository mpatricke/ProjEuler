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
def fillRowColOdd(count):
    global indHV
    global indLR
    global indUD
    global iMax
    global iMin
    global jMax
    global jMin

    if indHV == 'H':          # horizontal
        if indLR == 'R':      # left to right   HLx
            if indUD == 'U':
                j = jMax
            else:
                j = jMin
            for iNext in range(iMin,iMax+1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[j][iNext+1] = count
            iMax += 1
            indHV = 'V'
            indLR = 'L'
            return count

        else:                 # right to left    HRx
            if indUD == 'U':
                j = jMax
            else:
                j = jMin
            for iNext in range(iMax,iMin-1,-1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[j][iNext - 1] = count
            iMin -= 1
            indHV = 'V'
            indLR = 'R'
            return count

    else:                     # vertical
        if indUD == 'D':      # downwards        VDx
            if indLR == 'L':
                i = iMax
            else:
                i = iMin
            for jNext in range(jMin,jMax+1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[jNext + 1][i] = count
            jMax += 1
            indHV = 'H'
            indUD  = 'U'
            return count

        else:                 # upwards          VUx
            if indLR == 'L':
                i = iMax
            else:
                i = iMin
            for jNext in range(jMax,jMin-1,-1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[jNext-1][i] = count
            jMin -= 1
            indHV = 'H'
            indUD = 'D'
            return count

#=============
def fillRowColEven(count):
    global indHV
    global indLR
    global indUD
    global iMax
    global iMin
    global jMax
    global jMin

    if indHV == 'H':          # horizontal
        if indLR == 'R':      # left to right   HLx
            if indUD == 'U':
                j = jMax +1
            else:
                j = jMin
            for iNext in range(iMin-1,iMax):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[j][iNext+1] = count
            iMin -= 1
            indHV = 'V'
            indLR = 'L'
            return count

        else:                # right to left    HRx
            if indUD == 'U':
                j = jMax 
            else:
                j = jMin + 1
            for iNext in range(iMax,iMin-1,-1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[j][iNext -1] = count
            iMax += 1
            indHV = 'V'
            indLR = 'R'
            return count

    else:                    # vertical
        if indUD == 'D':     # downwards        VDx
            if indLR == 'L':
                i = iMax
            else:
                i = iMin - 1
            for jNext in range(jMin+1,jMax+2):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[jNext + 1][i] = count
            jMax += 1
            indHV = 'H'
            indUD  = 'U'
            return count

        else:                # upwards          VUx
            if indLR == 'L':
                i = iMax
            else:
                i = iMin - 1
            for jNext in range(jMax,jMin-1,-1):
                count += 1
                if count > finishNo:
                    return count
                else:
                    spiralArr[jNext][i] = count
            jMin -= 1
            indHV = 'H'
            indUD = 'D'
            return count


#=============
# initialise empty array
#
# maxSideLen  prime on the diagonals
#     2901        13.42%     0'16"
#     3901        12.88%     0'32"
#     4901        12.58%     0'45"
#     5901        12.21%     1'14"
#     6901        %    
#     7901        %
#     8901        %
#     9901        
#
maxSideLen = 31
startNo = 1
finishNo = maxSideLen**2

spiralArr = [[]] * maxSideLen

for i in range(maxSideLen):
    spiralArr[i] = [0] * maxSideLen


#=============
# initialise start value to 1 (note offset for even sided squares)
if maxSideLen%2 == 0:
    x = int(maxSideLen/2)
    y = int(maxSideLen/2) - 1
else:
    x = int(maxSideLen/2)
    y = int(maxSideLen/2)

spiralArr[x][y] = startNo


#=============
# now let's populate the array with numbers
# set up starting parameters 
indHV = 'H'    # 1 = horizontal; -1 = vertical
indLR = 'R'    # 1 = left to right; -1 = right to left
indUD = 'U'    # 1 = downwards; -1 = upwards
i = x
j = y
iMax = x
iMin = x
jMax = y
jMin = y

count = startNo

while count < finishNo:
    if maxSideLen%2 == 0:
        count = fillRowColEven(count)
    else:
        count = fillRowColOdd(count)
            

#=============
# print final array
print(maxSideLen,"sided spiral square:")
print("")
widthCol = len(str(finishNo)) + 1
for i in range(maxSideLen):
    for j in range(maxSideLen):
        if j == 0:
            print("     ",'{num:{fill}{width}}'.format(num=spiralArr[i][j], fill=' ', width=widthCol),end='')
        elif j < maxSideLen - 1:
            print('{num:{fill}{width}}'.format(num=spiralArr[i][j], fill=' ', width=widthCol),end='')
        else:
            print('{num:{fill}{width}}'.format(num=spiralArr[i][j], fill=' ', width=widthCol))

print("")
print("------")

#=============
# generate big table of primes
maxPrime = finishNo
primNumbersInd = [1] * maxPrime
primNumbersList = []

for i in range(2,int(sqrt(maxPrime + 1)) + 1):
    if primNumbersInd[i] == 1:
        for j in range(0, maxPrime + 1):
            k = i * i + i * j

            if k > maxPrime - 1:
                break
            else:
                primNumbersInd[k] = 0

for i in range(len(primNumbersInd)):
    if primNumbersInd[i] == 1:
        primNumbersList.append(i)

lenPPL = len(primNumbersList)
print("There are",lenPPL,"primes up to",finishNo,":")
#print(primNumbersList)
print("")
print("------")

#=============
# build list of array elements on the diagonals
diagList = []
for n in range(maxSideLen):
    if spiralArr[n][maxSideLen - (n + 1)] not in diagList:
        diagList.append(spiralArr[n][maxSideLen - (n + 1)])
    if spiralArr[n][n] not in diagList:
        diagList.append(spiralArr[n][n])

diagList = sorted(diagList)
lenDL = len(diagList)

print("There are",lenDL,"numbers on the diagonals:")
#print(diagList)
print("")
print("------")

#=============
# how many diagonal numbers are prime?

diagPrimList = sorted(set(diagList) - (set(diagList) - set(primNumbersList)))
diagListLen = len(diagList)
diagPrimCount = len(diagPrimList)
diagPrimPercent = int((diagPrimCount / diagListLen) * 10000)/100

#print(diagPrimList)

print("")
print("Of",diagListLen,"numbers on the diagonals",diagPrimCount,"are prime, or",diagPrimPercent,"%")
print("")
print("------")

print("Completion time", datetime.now() - starttime)
