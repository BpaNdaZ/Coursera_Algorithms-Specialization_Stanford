# Week1_Karatsuba Algorithm

## Problem:
> How to make n-digit number multiplications faster when n is large?
> That is n-digit number multiple n-digit number.

Karatsuba algorithm recursively uses 3 multiplications other than 4 multiplications in the classic multiplication algorithm, another multiplication can be derived from those 3 multiplications.

In this way, Karatsuba algorithm reduces the classic n^2 single-digit number multiplications to n^(log2(3)) single-digit number multiplications.

- divide and conquer, solve the original problem by recursively solving the sub-problems.
- when multiple two numbers with different length, ***make sure the right part of the two splited numbers must have the same length!!! otherwise the logic of the computation would be wrong.***
- be careful about the ***negative numbers*** when implementing the algorithm, if there are any.
	- HOW negative numbers behave under % operator? (you don't need to consider this question if you use another way to split the numbers)
	- in my implementation, negative numbers will always satisfy the base case
	- automatically floored under // operator
	
Since there are so many problems can be arised when the input has negative numbers, i decide to abs() the input and then return the right result based on the sign of the original input.
