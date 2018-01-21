"""
Project Euler 097: Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered
in 1999, and is a Mersenne prime of the form 2^6972593 − 1; it contains
exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form
2^p − 1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433 × 2^7830457 + 1.

Find the last ten digits of this prime number.

"""

from datetime import datetime
starttime = datetime.now()

power = 7830457
nDigit = 12
answer = 1

for integer in range(1,power+1):
    answer *= 2
    strAnswer = str(answer)
    lastNDigits = strAnswer[-nDigit:]
    answer = int(lastNDigits)


print("------")
print("2 ^",integer, "last",nDigit,"digits =",lastNDigits)

answer = (answer * 28433) + 1
strAnswer = str(answer)
lastNDigits = strAnswer[-10:]

print("------")
print("the last 10 digits digits of (28433 × 2^",power,") + 1 are ",lastNDigits)
print("------")
print("Completion time", datetime.now() - starttime)
