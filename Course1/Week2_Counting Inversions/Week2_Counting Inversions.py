# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:30:06 2018

@author: BNZ
"""



'''

when solving this problem, I used merge sort paradim, which is just another
divide and conquer algorithm

the runnning time analysis of merge&sort algorithm is not complex, which
is O(nlogn)

'''





def split(listed_num):
    """
    divide the input into 2 parts, return the left and right part
    it's alright if the 2 parts are not balanced, which situation
    can be handled in mergeandCount() function
    """

    split_point = len(listed_num) // 2
    left = listed_num[:split_point]
    right = listed_num[split_point:]
    
    return left, right



def mergeandCount(ll, rl, count):
    """
    ll and rl are sorted lists
    count holds the # of total inversions inherited from the 2 sorted
    input lists
    we merge these 2 sorted list into 1 sorted list and count the inversions
    between them @ the same time
    return the merged sorted list and the counting of inversions
    """
    
    sorted_num = []
    # using for holding the new sorted numbers
    i, j = 0, 0
    # i tracks the indec in ll
    # j tracks the index in rl
    
    '''
    while i < len(ll) and j < len(rl):
        sorted_num.append(min(ll[i], rl[j]))
        if rl[j] < ll[i]:
            count += len(ll) - i
            j += 1
        else:
            i += 1
    
    # when we jump out the while loop, 1 of the list is fully scaned
    # add the remainder sorted elements to sorted_num list
    # sorted_num += ll[i:] + rl[j:] takes longer time than append()
    # it's ok if the slice index is larger than the length of the list...which will be []
    
    if i < len(ll):
        while i < len(ll):
            sorted_num.append(ll[i])
            i += 1
        
    if j < len(rl):
        while j < len(rl):
            sorted_num.append(rl[j])
            j += 1
    
    
    %timeit countInversions(num_list)
    841 ms ± 2.32 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    
    '''
    
    for k in range(len(ll) + len(rl)):
        if i < len(ll) and j < len(rl) and ll[i] > rl[j]:
            count += len(ll) - i
            sorted_num.append(rl[j])
            j += 1
        elif i < len(ll):
            sorted_num.append(ll[i])
            i += 1
        elif j < len(rl):
            sorted_num.append(rl[j])
            j += 1
            
    '''
    %timeit countInversions(num_list)
    643 ms ± 2.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    
    '''
            
    return sorted_num, count




def countInversions(listed_num):
    """
    list contains the numbers (can be negative) that we are working on
    return the sorted list and countings of the inversions
    """
    
    # here is the base case
    if len(listed_num) == 1:
        return listed_num, 0
    
    else:
        # for the cases other than the base case
        left, right = split(listed_num)
        # recursively sovle the original problem by sovling the sub-problems
        ll, lc = countInversions(left)
        rl, rc = countInversions(right)
        # next we will combine the sub-results to get the full solution
        count = lc + rc
        sorted_num, count = mergeandCount(ll, rl, count)
    
    return sorted_num, count



f = open('Week2IntegerArray.txt')
num_list = []
for line in f:
    x = line.strip()
    num_list.append(int(x))


'''
count = 0

for num in num_list:
    sorted_num, single_count = countInversions(list(str(num)))
    count += single_count

print(count)
''' 


sorted_num, count = countInversions(num_list)
print(count) # 2407905288


'''
%timeit countInversions(num_list)
681 ms ± 19.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
'''



