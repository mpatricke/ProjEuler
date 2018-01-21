"""
https://projecteuler.net/problem=18 - solution = 1074
https://projecteuler.net/problem=67 - solution = 7273

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is
3 + 7 + 4 + 9 = 23:

3
7 4
2 4 6
8 5 9 3

core solution based on http://code.jasonbhill.com/python/project-euler-problem-18/
"""

from datetime import datetime
import operator

starttime = datetime.now()

# =========================================================
# recursive function to create partial sums by row:
# for each element on a row in rowData find the greatest sum of itself
# and the two elements in the row immediately below.
#
# By starting on the second last row and working upwards the sums build
# so that the result on the *top* row becomes the maximum possible path
# sum of all paths through the data.
#
def recSumAtRow(rowData, rowNum):                      

    # each element on a given row becomes the sum of itself and the
    # greater of the two elements in the row below
    for i in range(len(rowData[rowNum])):
        rowData[rowNum][i] += max([rowData[rowNum + 1][i], rowData[rowNum + 1][i + 1]])

    # if we're on the top row return the result
    if len(rowData[rowNum]) == 1:
        return rowData[rowNum][0]

    # else go up one row and do the same calculation
    else:
        return recSumAtRow(rowData, rowNum - 1)

# =========================================================
# initialise variables
#
rowData = []
rowSums = []
rowCount = maxSumNext = idxMaxNext = 0

# =========================================================
# write the data to two lists which will become:
#  1. rowData: the raw data
#  2. rowSums: the data summed from the bottom row upwards
#
#with open('067LargeSumDat') as dataFile:
with open('018LargeSumDat') as dataFile:
    for line in dataFile:
        rowCount += 1
        rowSums.append([int(i) for i in line.rstrip('\n').split(" ")])
        rowData.append([int(i) for i in line.rstrip('\n').split(" ")])

# =========================================================
# let's print the raw data so we can look at it 
#
padding = ''
for i in range(len(rowData)-1):
    padding += "  "

print("====> RowData ====>")
for i in range(len(rowData)):
    print(padding,rowData[i])
    padding = padding[:-2]

# =========================================================
# call the function to find the maximum path sum through the data
# starting at second to last row
#
maxPathSum = recSumAtRow(rowSums, len(rowSums) - 2)

# =========================================================
# now let's print the data summed from the bottom row
#
#print("====> RowSums ====>")
#for i in range(len(rowSums)):
#    print(rowSums[i])

# =========================================================
# table header to display results
#
print("")
print("====> Path ====>")
print("")
print("    Current Line:")
print("    Line  Pos   Sum  Elmt")
print("    ====  ===   ===  ====")
##print("Current Line:         | Next Line:")
##print("Line  Pos   Sum  Elmt | Line  Pos   Sum  Elmt")
##print("====  ===   ===  ==== | ====  ===   ===  ====")

# =========================================================
# now trace back *from the top* through the data for the path
#
for i in range(0,rowCount):
    idxMax = idxMaxNext

    if i < rowCount - 1:
        # until the second last line determine the running
        # max sum on the current line
        if i == 0:
            sumMaxVal = maxPathSum
        else:
            sumMaxVal = maxSumNext

        # find the max of the two sums below ...
        maxSumNext = max(rowSums[i + 1][idxMax],rowSums[i + 1][idxMax+1])
        
        # ... and thus the index of the max sum below
        if maxSumNext == rowSums[i + 1][idxMax]:
            idxMaxNext = idxMax
        else:
            idxMaxNext = idxMax + 1

        # read the *next* line of raw data ...
        # ... and required data is at the same index
        maxValLineNext = rowData[i+1]
        maxValNext = maxValLineNext[idxMaxNext]

        print('    {:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, sumMaxVal, rowData[i][idxMax]))

    else:
        print('    {:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, maxSumNext, rowData[i][idxMax]))

##        print ('{:>4} {:>4} {:>5} {:>5} {:>1} {:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, sumMaxVal, rowData[i][idxMax], "|", i + 1, idxMaxNext, maxSumNext, maxValNext))
##
##    else:
##        print('{:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, maxSumNext, rowData[i][idxMax]), "|   --- end of data ---")

print("")
print("Maximum path sum =", maxPathSum, "; found in:", datetime.now() - starttime, "secs.")
