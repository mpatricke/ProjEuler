"""
project euler 012: The sequence of triangle numbers is generated by adding the
natural numbers.

So the 7th triangle number would be: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors. What
is the value of the first triangle number to have over five hundred divisors?
"""

from math import sqrt
from datetime import datetime
starttime = datetime.now()

def factorCount(test,factorList,factorsTried):
    countFactor = 0

    if test == 0:
        return countFactor

    for i in range(1,len(primNumbersList)):

        if primNumbersList[i] > test/2 + 1:                             # no point testing a factor greater than test / 2
            break

        else:
            if test%primNumbersList[i] == 0:                            # if test is evenly divisible by this prime...

                for j in range(i,len(primNumbersList)):                 # ... test every prime multiple of this prime
                    nextTestFactor = int(primNumbersList[i]*primNumbersList[j])

#                for j in range(1,primNumbersList[i]):                 # ... test every  multiple of this prime
#                    nextTestFactor = int(primNumbersList[i]*j)

                    if nextTestFactor > test/2 + 1:                     # no point testing a factor  greater than test / 2
                        break

                    else:
                        thisResult = test/(nextTestFactor)
                        thisResultRem = test%(nextTestFactor)

                        if thisResultRem == 0:                          # if test is evenly divisible by nextTestFactor...
 
                            print(" -> ",int(test),"---------            factors:", factorList)
                            print("      ",int(test), "/ (",primNumbersList[i],"*",primNumbersList[j],")",nextTestFactor,"=",int(thisResult),"; tried:",factorsTried)

                                                                        # need to factor thisResult if it is
                                                                        # not prime itself and if it has not
                                                                        # been tested already
                            if thisResult not in primNumbersList and thisResult < test and thisResult not in factorsTried:
                                countFactor += factorCount(thisResult,factorList,factorsTried)

                            if nextTestFactor not in factorList:        # since the number we've just tested is a factor it
                                factorList.append(nextTestFactor)       # can be added to the list of known factors, ...

                            if thisResult not in factorList:            # ... as can the result of dividing test by this number
                                factorList.append(int(thisResult))

                            if nextTestFactor not in factorsTried:          # we can also keep a record of numbers tried 
                                factorsTried.append(nextTestFactor)         # even if they weren't found to be factors

                            if thisResult not in factorsTried:    
                                factorsTried.append(int(thisResult))

    if int(test) not in factorList:
        factorList.append(int(test))

    countFactor = len(factorList)

    return countFactor


#=============
#generate big table of primes

maxPrime = 500000
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

#=============
#generate and test triangular numbers

target = 70000
test = 0
countMax = 0
testMax = 0
factorMax = 7



for i in range(target+1):
    test += i
    factorList = []
    factorsTried = []

    testCount = factorCount(test,factorList,factorsTried)

#    print("")
#    print("    ",factorList)
#    print("")
#    print("tri no:  ",test, "; factors:",testCount, "; time:",datetime.now() - starttime)

    if i%100 == 0 and i != 0:
        print("    no:  ",test, "; factors:",testCount, "; time:",datetime.now() - starttime)

    if testCount > countMax:
        countMax = testCount
        testMax = test
        print("tri no:  ",test, "; factors:",testCount, "; time:",datetime.now() - starttime)
        if countMax >= factorMax:
            break

    print("-------------------------------------------------------------------------")
#    print("=========================================================================")


print("=== the end ===")
print("First triangular number with",factorMax,"factors or more is",testMax)
print("Execution time:", datetime.now() - starttime)