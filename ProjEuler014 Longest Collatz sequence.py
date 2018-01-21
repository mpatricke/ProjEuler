#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon 21 August 2017

@author: magnus

Project Euler 014: The following iterative sequence is defined for the set 
of positive integers:
	n → n/2 (n is even)
	n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1. Which starting number, under one 
million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

nCollatz = 1
maxNCollatz = 1
nNext = 0
chainCount = 0
maxChainCount = 0

def collatzChain(nCollatz):
    chainCount = 1

    while nCollatz > 0:

        if nCollatz == 1:
#            print("break: nCollatz:", int(nCollatz), "chainCount:", chainCount)
            return chainCount
        else:
            chainCount += 1
#            print("else:  nCollatz:", int(nCollatz), "chainCount:", chainCount)

            if nCollatz % 2 == 0:
                nCollatz /= 2

            else:
                nCollatz = nCollatz * 3 + 1


while nCollatz < 1000000:


#    print("===========")

    chainCount = collatzChain(nCollatz)

#    print("next:  nCollatz:", int(nCollatz), "chainCount:", chainCount)

    if chainCount > maxChainCount:
        maxChainCount = chainCount
        maxNCollatz = nCollatz

    nCollatz += 1

print("Max Chain Count =",maxChainCount," for Collatz number =",maxNCollatz)
