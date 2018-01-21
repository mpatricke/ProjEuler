"""
project euler 023: non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
    1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number (1 + 2 + 3 + 4 + 6 = 16) the smallest
number that can be written as the sum of two abundant numbers is 12 + 12 = 24.

By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

from math import sqrt
from datetime import datetime
starttime = datetime.now()

# find the factors of a number and return the sum
def buildFactorList(test,factorList):

    sumFactors = 0

    for i in range (1,int(sqrt(test))+1):

        if test%i == 0:
            if i not in factorList and i != test:
                factorList.append(i)
                sumFactors += i
            if int(test/i) not in factorList and int(test/i) != test:
                factorList.append(int(test/i))
                sumFactors += int(test/i)

    factorList = factorList.sort()

    return sumFactors


# generate 'number' sequentially, find the sum of its factors 'sumDivisors'
# build list of 'abundant' numbers
start = 1
end = 28123
#end = 8123
abundantNoList = []
numberList = list(range(end+1))

for number in range(start,end):

    factorList = []
    sumDivisors = buildFactorList(number,factorList)

    if sumDivisors > number:
        numberType = 'abundant'
        abundantNoList.append(number)
    elif sumDivisors < number:
        numberType = 'deficient'
    else:
        numberType = 'perfect'


# build a list of all possible sums of two abundant numbers
abundantNoListCount = len(abundantNoList)
abNoSums = []
misc = 0

for i in range(abundantNoListCount):
    for j in range(i,abundantNoListCount):
        sumAbNo = abundantNoList[i] + abundantNoList[j]

        if sumAbNo > end:
            break
        else:
#            try:
#                numberList.remove(sumAbNo)
#            except:
#                misc = 1

            abNoSums.append(sumAbNo)

# build a set which is the difference between numberList and abNoSums
nonSumAbNosList = set(numberList) - set(abNoSums)
sumNonSumAbList = sum(nonSumAbNosList)


print("------")
print("Sum of all numbers between",start,"and",end,"that are not the sum of")
print("two abundant numbers is",sumNonSumAbList,", found in execution time:",datetime.now() - starttime)
