# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:36:43 2018

@author: BNZ
"""



"""

here we implement Karatsuba algorithm for n-digit number multiplication where n is large.

the idea behind Karatsuba algorithm is reducing the traditional n^2 single-digit multiplications
to n^(log2(3)) single-digit multiplications.


key point ==> the right parts of the splited numbers must have the same lengh!
otherwise the algorithm will be wrong in terms of computation logic.


careful about the negative numbers:
    * HOW negative numbers behave under % operator??? (in the split function)
    * negative numbers will always satisfy the base case in my defined Karatsuba function
    * automatic floored using // operator


since there are so many problems that can be arised when the input are negative numbers,
I decide to abs() the input and then return the final result according to the sign of the original input.

"""


def split(absnum1, absnum2):
    """split the n-digit numbers into 2 parts and with the same length of the right parts
    * negative numbers will cause some trouble when using the % operator
    * careful the automatic floor operation of the // operator for negative numbers
    """
    
    l = max(len(str(absnum1)), len(str(absnum2)))
    split_point = l // 2
    # the split point must aim @ the longer number
    
    absnum1_l = absnum1 // (10**split_point)
    absnum1_r = absnum1 % (10**split_point)
    
    absnum2_l = absnum2 // (10**split_point)
    absnum2_r = absnum2 % (10**split_point)
    
   return absnum1_l, absnum1_r, absnum2_l, absnum2_r, split_point




def Karatsuba(num1, num2):
    """recursively multiplicate the splitted numbers"""
    
    absnum1 = abs(num1)
    absnum2 = abs(num2)
    # negative is bad for the base case, change it to positive
    # assign the result to a new variable oterwise there will be problem for the if/else check at the end
    
    if absnum1 <= 10 or absnum2 <= 10:
        # here is the base case
        # return the result directly if one of 2 numbers are less than 10
        return absnum1 * absnum2
    
    # split operation for cases other than base case
    absnum1_l, absnum1_r, absnum2_l, absnum2_r, split_point = split(absnum1, absnum2)
    
    # 3 multiplications recursively using Karatsuba instead of 4 multiplications
    ll = Karatsuba(absnum1_l, absnum2_l)
    rr = Karatsuba(absnum1_r, absnum2_r)
    lrlr = Karatsuba(absnum1_l + absnum1_r, absnum2_l + absnum2_r)
    K = lrlr - ll - rr
    
    # return the result based on the sign of the original input
    if (num1 <= 0 and num2 <= 0) or (num1 >= 0 and num2 >= 0):
        return (ll * 10 ** (2 * split_point) + K * 10  ** split_point + rr)
    else:
        return -(ll * 10 ** (2 * split_point) + K * 10  ** split_point + rr)


print(Karatsuba(0, 360) == 0*360)
print(Karatsuba(2, 360) == 2*360)
print(Karatsuba(200, 3000) == 200*3000)
print(Karatsuba(-12, 3001) == -12*3001)
print(Karatsuba(3678, 5919) == 3678*5919)
print(Karatsuba(-3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == -3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627)


# %timeit Karatsuba(-3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
# 1.83 ms ± 5.09 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

















