"""
Project Euler 63: Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from datetime import datetime
starttime = datetime.now()

count = 0

for integer in range(1,100):
    for power in range(1,100):
        result = integer**power
        lenResult = len(str(result))

        if lenResult == power:
            count += 1
            print(integer, power, result)


print("------")
print("There are",count," n-digit positive integers exist which are also an nth power.")
print("Completion time", datetime.now() - starttime)
