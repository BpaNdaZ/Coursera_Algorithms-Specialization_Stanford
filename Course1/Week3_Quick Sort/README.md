In this sorting algorithm, there will be a pivot, which is used as a reference value for comparison.
(there is a reasonable question-->how to choose a pivot? Is there any performance difference for different povit?)

after 1-round comparison, the pivot should be @ its rank position of the given input array
(this means that elements on the left side of the pivot are smaller than the pivot, and elements on the right side of the pivot are larger
than the pivot. But both sides are not in the sorted order)

in this paradim, we need 2 index pointers:
- 1 pointing to the 1st element that haven't been exploided and seperating the exploided and unexploided
- 1 pointing to the 1st element that seperate the smaller and larger ones compare to the pivot

each iteration, we partition the (sub-)sequences around the choosing pivot and using the divide and conquer paradim in this way.
the partition takes O(n) linear time, no extra memory and reduces the problem size

the average running time is O(nlog(n)), **given the pivot is chosen randomly**.
