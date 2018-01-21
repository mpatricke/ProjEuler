"""
utility function:

Generate a list of all primes less than primeMaxLimit

"""

from datetime import datetime
starttime = datetime.now()
from math import sqrt

primeMaxLimit = 1000000
maxPrime = primeMaxLimit
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

lenPNL = len(primNumbersList)

print("There are",lenPNL,"prime numbers less than",primeMaxLimit)
print("------")
print("Completion time", datetime.now() - starttime)
