"""
project euler 029: distinct powers

Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2^2=  4  2^3=   8  2^4=  16  2^5=   32
    3^2=  9  3^3=  27  3^4=  81  3^5=  243
    4^2= 16  4^3=  64  4^4= 256  4^5= 1024
    5^2= 25  5^3= 125  5^4= 625  5^5= 3125

If they are then placed in numerical order, with any repeats removed, we get
the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for
    2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

"""

from datetime import datetime
starttime = datetime.now()

noList = []
maxA = 100
maxB = 100

for a in range(2, maxA+1):
    for b in range(2,maxB+1):
        result = a**b
        if result not in noList:
            noList.append(result)

lenNoList = len(noList)

print("There are", lenNoList, "distinct terms in the sequence generated by a^b")
print("for 2 ≤ a ≤",maxA,"and 2 ≤ b ≤",maxB)
print("-----")
print("Total elapsed time:",datetime.now() - starttime)
