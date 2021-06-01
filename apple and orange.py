#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples.extend([])
    length_of_apple=[]
    num_a=0
    for i in apples: 
       length_of_apple.append(i+a)
    for i in range(len(length_of_apple)):
        if length_of_apple[i] in range(s,t+1):
            num_a+=1
    #print(num_a)      
    oranges.extend([])
    length_of_orange=[]
    num_m=0
    for i in oranges:
       length_of_orange.append(i+b)
    for i in range(len(length_of_orange)):
        if length_of_orange[i] in range(s,t+1):
            num_m+=1
    #print(num_m) 
    print(num_a)
    print(num_m)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
