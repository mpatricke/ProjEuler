"""
project euler 013: Large sum:

Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
"""

from datetime import datetime
starttime = datetime.now()

numberSum = 0

with open('ProjEuler_013_data.txt', 'r') as numberFile:
    for line in numberFile:
        numberSum += int(line)

strNumSum = str(numberSum)

firstStrNS = strNumSum[0:10]
#firstStrNS = strNumSum


print(numberSum)
print(strNumSum)
print(firstStrNS)

