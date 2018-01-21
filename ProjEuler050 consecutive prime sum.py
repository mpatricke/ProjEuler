"""
Project Euler 50: Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred. The longest sum of consecutive primes below one-thousand that
adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from datetime import datetime
starttime = datetime.now()
from math import sqrt

primeMaxLimit = 1000000
maxPrime = primeMaxLimit
primNumbersInd = [1] * maxPrime
primNumbersList = []

# generate list of primes less than max prime
#
for i in range(2,int(sqrt(maxPrime + 1)) + 1):
    if primNumbersInd[i] == 1:
        for j in range(0, maxPrime + 1):
            k = i * i + i * j

            if k > maxPrime - 1:
                break
            else:
                primNumbersInd[k] = 0

for i in range(2,len(primNumbersInd)):
    if primNumbersInd[i] == 1:
        primNumbersList.append(i)

lenPNL = len(primNumbersList)

print("There are",lenPNL,"prime numbers less than",primeMaxLimit)
print("------")

# starting at the first prime number in the list, calculate the consecutive
# sum and identify the longest run of terms

maxConsSumPrime = 0
maxConsSumTerms = 0

for indStartPrime in range(lenPNL):
    startPrime = primNumbersList[indStartPrime]
    testCountTerms = 1
    runSum = startPrime

    # no point going any further if...: 
    if maxConsSumTerms * startPrime > primeMaxLimit or indStartPrime + maxConsSumTerms > lenPNL:
        break

    for indNextPrime in range(indStartPrime+1,lenPNL):
        nextPrime = primNumbersList[indNextPrime]
        testCountTerms += 1
        runSum += nextPrime

        if runSum > primeMaxLimit or indStartPrime + indNextPrime > lenPNL:
            continue

        elif runSum in primNumbersList:
            if testCountTerms > maxConsSumTerms:
                print("New max count:",testCountTerms,"; prime:",runSum,"(seq start:",startPrime,")")
                maxConsSumTerms = testCountTerms
                maxConsSumPrime = runSum
        
print("------")
print("The prime less than",primeMaxLimit,"that is the sum of the most consecutive primes is:")
print("    ", maxConsSumPrime,", with",maxConsSumTerms,"terms.")
print("------")
print("Completion time", datetime.now() - starttime)
