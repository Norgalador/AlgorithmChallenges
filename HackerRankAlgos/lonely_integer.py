# Given an array of integers, where all elements but one occur twice, find the unique element.

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    for i in range(len(a)):
        occuredTwice = False
        for j in range(len(a)):
            if(a([j] == a[i]) and (i!=j)):
                occuredTwice = True


lonelyinteger([1,2,3,4,3,2,1])