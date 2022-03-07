#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def replace(s):
    '''
        Merubah :
        - bc || cb => a
        - ac || ca => b
        - ab || ba => c
    '''
    temp = [x for x in s]
    if temp[0]==temp[1]:
        return s
    
    result = [x for x in 'abc' if x not in temp]
    return result[0]

def stringReduction(s):
    # Write your code here
    status = True
    start = 0
    
    result = s
    count = 0
    while(status):
        if len(list(set([i for i in result]))) == 1:
            status = False

        if start+2<=len(result):
            remove = result[start:start+2]
            print(remove)
            print(replace(remove))
            result = result.replace(remove, replace(remove))
            print(result,'\n')
            if remove == replace(remove):
                start+=1
        else:
            start = -1
    return len(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
