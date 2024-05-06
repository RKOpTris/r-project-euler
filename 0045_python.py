#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Hn = n * ((2 * n) - 1)          1, 6, 15, 28, 45...
Pn = n * ((3 * n) - 1) / 2      1, 5 , 12, 22, 35...
Tn = n * (n + 1) / 2            1, 3, 6, 10, 15...

It can be verified that T285 = P165 = H143.

Find the next triangle number that is also pentagonal and hexagonal.
"""

def genHexagonal(n):
    n = global_n
    return(n * ((2 * n) - 1))
    
# This function will search for pentagonal numbers from n of H (which in the
# example was 143, until the the value of Pn exceeds hexagonal number) as 
# n of P must always be larger than n of H
def findPentagonal(n): 
    n = global_n
    num = 0
    outPent = []
    while num <= hexNum:
        n += 1
        num = int(n * ((3 * n) - 1) / 2)
        outPent.append(num)
    return(outPent)

# All hexagonal numbers are also triangle numbers which can be seen in the
# instructions above and follows the rule Tn = (Hn * 2) - 1 so it is not 
# necessary to find a triangle number, only the pentagonal number that matches
# the hexagonal number

init_n = 143 + 1 # setting n of H to the next possible value
global_n = init_n

problemSolved = False

while problemSolved == False:
    
    hexNum = genHexagonal(global_n)
    pentNums = findPentagonal(global_n)
    
    if hexNum in pentNums:
        #print(global_n)
        #print(pentNums.index(hexNum) + global_n + 1)
        #triNum = (global_n * 2) - 1
        #print(triNum)
        print(hexNum)        
        problemSolved = True        
    else:
        global_n += 1

    