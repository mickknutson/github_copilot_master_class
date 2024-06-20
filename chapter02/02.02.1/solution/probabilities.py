import math
import os

'''
Create a function 'fact' that calculates the factorial of a value 'n' where 'n' is a non-negative value using recursion.
details:
n! = n * (n - 1) * ... * 1
steps:
if n is negative return 0
if n == 0 or n == 1 return 1
return n * fact(n - 1)
'''

def fact(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

'''
Create a function 'perm' that calculates the number of permutations of n elements taken k at a time.
details:
nPk = n! / (n - k)!
steps:
return fact(n) / fact(n - k)
'''


'''
the selected code is correct hoewever it is not optimized, is there a way to use Memoization to optimize the code?
'''
def perm(n, k):
    return fact(n) / fact(n - k)

