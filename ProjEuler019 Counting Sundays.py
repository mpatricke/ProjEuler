"""
project euler 018: Sundays on 1st of Month

You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import datetime
starttime = datetime.now()

d01011900 = 1
week = 7
sumSunOneCount = 0
jan1 = 2


for year in range(1901,2001):
    sunOneCount = 0
    leapYearInd = False
    monFeb = 28

    if (year%4 == 0 and not year%100 == 0) or (year%400 == 0):
        leapYearInd = True
        monFeb = 29

    feb1 = (jan1 + 31)%7
    mar1 = (feb1 + monFeb)%7
    apr1 = (mar1 + 31)%7
    may1 = (apr1 + 30)%7
    jun1 = (may1 + 31)%7
    jul1 = (jun1 + 30)%7
    aug1 = (jul1 + 31)%7
    sep1 = (aug1 + 31)%7
    oct1 = (sep1 + 30)%7
    nov1 = (oct1 + 31)%7
    dec1 = (nov1 + 30)%7

    yearList = (str(jan1) + str(feb1) + str(mar1) + str(apr1) + str(may1) + str(jun1) + str(jul1) + str(aug1) + str(sep1) + str(oct1) + str(nov1) + str(dec1))

    sunOneCount = yearList.count('0')
    sumSunOneCount += sunOneCount

    print("For year",year,"the months started:",yearList,", with",sunOneCount,"Sundays on the 1st; running total:",sumSunOneCount)

    jan1 = (dec1 + 31)%7


print("=== the end ===")
print("Execution time:", datetime.now() - starttime)
