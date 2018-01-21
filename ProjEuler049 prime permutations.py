"""
project euler 049: prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
   (i) each of the three terms are prime, and,
  (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import itertools
from datetime import datetime
from math import sqrt

starttime = datetime.now()

#=============
#generate table of primes between 1000 and 9999

maxPrime = 9999
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

for i in range(1000,len(primNumbersInd)):
    if primNumbersInd[i] == 1:
        primNumbersList.append(i)

# cycle through all primes to identify which are permutations
# and build a list
primPerms = []

for i in range(len(primNumbersList)):
    primPermsTemp = [primNumbersList[i]]
    for j in range(i+1,len(primNumbersList)):
        if sorted(str(primNumbersList[i])) == sorted(str(primNumbersList[j])):
            primPermsTemp.append(primNumbersList[j])

    if len(primPermsTemp) >= 4:
        primPerms.append(primPermsTemp)   

# cycle through all elements in list of permutations to calculate
# the gap between each element
lenPP = len(primPerms)
ansStr = '; and the answer is:'
for i in range(lenPP):

    count = 0
    primPermi = primPerms[i]
    lenPPi = len(primPermi)

    for j in range(lenPPi):
        for k in range(j+1,lenPPi):
            diff = primPermi[k] - primPermi[j]
            nextPrim = primPermi[k] + diff 

            if nextPrim in primPermi:
                primStr = str(primPermi[j]) + str(primPermi[k]) + str(nextPrim)
                primStrNo = int(primStr)
                primPerms[i].append(ansStr)
                primPerms[i].append(primStrNo)


# let's see what we've got so far
for i in range(len(primPerms)):
    primPermi = primPerms[i]
    if ansStr in primPermi:
        print(primPermi)

print("------")
print("Completion time", datetime.now() - starttime)


