#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    '''
        jika energy > height => new energy = energy+(energy-height)
        jika energy < height => new energy = energy-(height-energy)
        maka:
        new energy = 2x energy - height
        energy = ceil((new energy + height)/2)
        
        untuk mencari energy minimum maka diasumsikan bahwa 
        new energy pada tahapan terakhir adalah 0,
        untuk menunjukkan bahwa energy yang digunakan 
        tidak kurang dari 0 hingga akhir iterasi
    '''
    # Write your code here
    energy = 0
    
    count = len(arr)-1
    while(count>=0):
        energy = math.ceil((energy+arr[count])/2)
        print(energy)
        count-=1
        
    return energy    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
