#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    machine = m
    worker = w
    
    leftover = 0
    step = 1
    
    while((machine*worker)+leftover <=n):
        print("step = ",step)
        print("current : worker =",worker,", machine =",machine)
        production = machine*worker
        production += leftover
        
        print("produce : ",production)
        print("price = ",p)
        
        buy = production // p
        leftover = production - (buy*p)
        
        # jika terjadi pembelian > 1
        if buy>1:
            temp = buy//2
            worker += temp + buy%2
            machine += temp
        # jika pembelian hanya sekali
        elif buy > 0:
            """
                jika selisih worker dan machine >= 1
                maka machine yang akan ditambah
                untuk mempercepat perulangan 
            """
            if worker-machine>=1:
                machine+=1
            else:
                worker+=1
            
        step += 1
        print("buy = ", buy)
        print("leftover candies = ",leftover)
        print("after : worker ",worker, "machine ",machine,"\n")
    return step

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
