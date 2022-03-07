#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#
def getPrefixList(lis, mod):
    prefix = []
    for i in range(len(lis)):
        if len(prefix)>0:
            prefix.append((lis[i]+prefix[i-1])%mod)
            # print(prefix,'\n')
        else :
            prefix.append(lis[i]%mod)
            # print(prefix)
    return prefix

def getNumber(lis, num):
    result = [x for x in lis if x>num]
    if len(result)>0:
        return min(result)
    else:
        return 0

def maximumSum(a, m):
    # Write your code here
    # implement kadane algorithm
    # source : https://www.youtube.com/watch?v=u_ft5jCDZXk&t=609s
    prefix = getPrefixList(a, m)
    print(a)
    print(prefix)
    max_mod = 0
    for i in range(1,len(prefix)):
        temp = prefix[:i]
        num = getNumber(temp, prefix[i])
        print(temp, prefix[i])
        if num>0:
            x = (prefix[i]-num+m)%m
            print(prefix[i],num,'=',x)
            if x>max_mod:
                max_mod = x
        else:
            x = prefix[i]
            if x>max_mod:
                max_mod = x                
    return max_mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
