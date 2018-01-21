"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

exp1k = 2**1000
len2x1k = len(str(exp1k))
sum = 0

for i in range(len2x1k):
    sum += int(str(exp1k)[i])

print(sum)
