"""
project euler 012: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

from math import sqrt
from datetime import datetime
starttime = datetime.now()

# find the factors of a number and build into a list
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


# define some starting parameters
start = 1
end = 9999
amicableNoList = []


# generate 'number' sequentially, find the sum of its factors 'sumDivisors',
# find the sum of the factors of the sum of the factors 'sumSumDivFL',
# if 'sumSumDivFL' = 'number' then the numbers are amicable
for number in range(start,end):

    factorList = []
    sumDivisors = buildFactorList(number,factorList)

    factorList = []
    sumSumDivFL = buildFactorList(sumDivisors,factorList)

    if sumSumDivFL == number and sumDivisors != sumSumDivFL:
#        print("Number",number,"has sum of factors = ",sumDivisors, "; and",sumDivisors,"has sum of factors:",sumSumDivFL)

        if number not in amicableNoList:
            amicableNoList.append(number)
        if sumDivisors not in amicableNoList:
            amicableNoList.append(sumDivisors)


sumAmicableNos = sum(amicableNoList)


print("------")
print("List of amicable numbers between",start,"and",end,"is:")
print("   ",amicableNoList)
print("with a total sum =",sumAmicableNos)
print("------")
print("Execution time:", datetime.now() - starttime)
