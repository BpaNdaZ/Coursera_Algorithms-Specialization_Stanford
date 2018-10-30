#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The file contains 1 million integers, both positive and negative (there might be some repetitions!).
This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that
there are distinct numbers x,y in the input file that satisfy x+y=t.
(NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)


The intension of this task is getting familiar with hash table, however, I used
another logic to solve this problem, which is based on sorting and binary search.


"""



import bisect
from time import time


def two_sum(array):
    """Returns the numbers from [-WIDTH, WIDTH] that can be obtained by
    summing up any two elements in 'array'.
    array is a sorted list
    """

    WIDTH = 10000
    out = set() # keep distince elements
    for i in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        # calculate the index of the minimum element within the range
        upper = bisect.bisect_right(array, WIDTH - i)
        # calculate the index of the maximum element within the range
        out |= set([i + j for j in array[lower:upper]])
        # constract a set with all the distince summations in the given range
    return out


def main():
    array = []
    with open('2_SUM.txt') as file_in:
        for line in file_in:
            num = int(line.strip())
            array.append(num)
    array.sort()
    return len(two_sum(array))


if __name__ == '__main__':
    start = time()
    print(main())
    print(time() - start)












