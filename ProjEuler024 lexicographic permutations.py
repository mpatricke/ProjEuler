"""
project euler 024: lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

import itertools
from datetime import datetime
starttime = datetime.now()

listNos = ['0','1','2','3','4','5','6','7','8','9']
target = 1000000

listNos = sorted(listNos)

listPerms = list(itertools.permutations(listNos))

listPermsTarget = listPerms[target - 1]
listPermsAns = ''

for i in range(len(listPermsTarget)):
    listPermsAns += str(listPermsTarget[i])

print("------")
print(target,"th permuation of",listNos,"is", listPermsAns, "found in", datetime.now() - starttime)

print("------")
listNos = ['0','1','2','3','4','5','6','7','8','9']
print(listNos)
listNosEx = listNos.pop(4)
print(listNos)
