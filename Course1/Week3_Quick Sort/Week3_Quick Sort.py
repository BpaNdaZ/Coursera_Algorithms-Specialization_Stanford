#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 09:27:53 2018

@author: BNZ
"""


'''

Quick Sort:
    1. there will be a pivot, which is used as a reference value during the comparison
    2. then the next question is how to choose a good pivot? (think about the extrem cases)
    3. after 1-round the pivot number shoule be @ its right rank position
    4. 3.means that the numbers on the left of the pivot are less than the pivot number
    and the numbers on the right are larger than the pivot, but not sorted on both side
    5. in the paradim, there are 2 index pointers, 1 pointing to the first number the algo
    are going to scan (not scan yet) and another 1 pointing to the first number that seperate
    the less and larger ones compare  to the pivot
    6. each round we can partition the (sub-)sequences around the pivot and use the
    divide and conquer paradim. there are 2 advatages about the partition:
        6.1 linear O(n) time, no extra memory
        6.2 reduces problem size
    7. average running time is O(nlog(n)), given the pivot is chosen randomly


'''




'''
def read_data():
    
    input_list = []
    
    with open('quicksort.txt') as file:
        for num in file:
            input_list.append(int(num))
    return input_list


%timeit read_data()
3.24 ms ± 8.09 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

'''


def read_data():

    with open('Week3QuickSort.txt') as file:
        input_list = [int(num) for num in file]

    return input_list

# %timeit read_data()
# 2.81 ms ± 25.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)






# there is something need to be noticed
# if we code partition() and quickSort() like below then we actually resursively 
# work on the new list rather than modify the input_list in-place!!!  which will cause
# problems since there is no combine process

'''
def partition(input_list, pivot_index):
    
    
    input_list[0], input_list[pivot_index] = input_list[pivot_index] , input_list[0]
    # swap the first element & the pivot number
    # it's ok is pivot_index == 0
    
    i, j = 1, 1
    # i is the pointer of seperation
    # j is the ppinter of the first unscaned element
    
    p = input_list[0]
    
    for j in range(1, len(input_list)):
        if input_list[j] <  p:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
    input_list[0], input_list[i-1] = input_list[i-1], input_list[0]
    
    return input_list[:input_list.index(p)], input_list[input_list.index(p):]
            
            

def quickSort(input_list):
    
    if len(input_list) == 1:
        return
    
    else:
        pivot_index = 0 # choosePivot(input_list)
        
    
        left, right = partition(input_list, pivot_index)
    
        quickSort(left)
        quickSort(right)

    
'''



def partition(input_list, head, tail):
    """
    partition the input_list with its head as the pivot
    
    head: the index where partition starts
    
    tail: the index where partition ends
    
    return the pivot index
    
    arguments are setting like this will convinient for the in-place modification
    
    dont forget the final swap between the pivot and the last element in the left half
    
    """
        
    pivot = input_list[head]
    
    i = head + 1
    # i is the pointer of seperation
    # initially points to the element after the head, increases by 1 after each swap
    # always points to the 1st element of the right half
    # so @ last, i - 1 points to the (rank) index of the pivot
   
    # j is the ppinter of the first unscaned element
    for j in range(head + 1, tail + 1):
        if input_list[j] <  pivot: # swap if the element is smaller than the pivot
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1 # increase the pointer by 1 after the swap to point to the 1st larger one
    
    # the final swap
    input_list[head], input_list[i-1] = input_list[i-1], input_list[head]
    
    return i - 1


count = 0
# here we need a global variable that can not be changed during repeated calls for quickSort()


def quickSort(input_list, head, tail):
    """
    sort and modify the input_list in-place recursively
    """

    global count

    if tail -head < 1:
        # there is only 1 element
        # there is no elements: tail <= head
        return 
    
    else:
        pivot_index = partition(input_list, head, tail)
        count += tail - head
        # each partition compare n-1 times, n is the length of the input_list
        
        quickSort(input_list, head, pivot_index-1)
        quickSort(input_list, pivot_index + 1, tail)
    
    return input_list, count



def choose_median(array):
    if len(array) % 2 == 0:
        candidates = [array[0], array[len(array) // 2 - 1], array[-1]]
    else:
        candidates = [array[0], array[len(array) // 2], array[-1]]
    candidates.sort()
    return candidates[1]






import time

start_time = time.time()
input_list= read_data()
pivot = choose_median(input_list)
input_list[0], input_list[input_list.index(pivot)] = input_list[input_list.index(pivot)], input_list[0]
# we swap the above 2 elements in the list since the pivot is fixed as the head in partition()

result, count = quickSort(input_list, 0, len(input_list) - 1)
print(result == list(range(1, 10001)), count)
print(time.time() - start_time)

# True 162085
# 0.0372319221496582





























