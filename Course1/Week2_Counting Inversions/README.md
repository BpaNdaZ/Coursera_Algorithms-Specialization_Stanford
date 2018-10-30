**Week2_Counting Inversions**

Use the merge sort paradim to solve this problem
- divide and conquer, solve the original problem by recursively merge sort the sub-sequences and counting the inversions @ the same time
- detailes are shown in the Week2_CountingInversions.py
- there is also a Week2_1_CountingInversions.py which is faster than Week2_CountingInversions.py, however I dunno why...(hope someone could show me how)


The logic for counting inversions:
1. assume we have 2 sorted lists
2. we merge these 2 sorted lists into 1 sorted list (need 2 pointers to the index of these 2 sorted lists)
3. during the merging, we keep tracking of the # of inversions
