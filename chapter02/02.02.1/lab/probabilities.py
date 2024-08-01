'''
This file contains the functions that are used to calculate the probabilities of the different events that can happen in the game.

Details:
    - a function 'fact' that calculates the factorial of a number
    - a function 'comb' that calculates the number of combinations of n elements taken k at a time
    - a function 'perm' that calculates the number of permutations of n elements taken k at a time

'''

import math
import os



'''
Optimize Prompt:

The selected code is correct hoewever it is not optimized, is there a way to use external Memoization to optimize the code?
'''

def memoize(func):
    cache = {}
    
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized_func

'''
Create a function 'fact' that calculates the factorial of a value 'n' where 'n' is a non-negative value using recursion.

details:
n! = n * (n - 1) * ... * 1

steps:
if n is negative return 0
if n == 0 or n == 1 return 1
return n * fact(n - 1)
'''

@memoize
def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)





'''
Create a function 'perm' that calculates the number of permutations of n elements taken k at a time.

details:
nPk = n! / (n - k)!

steps:
return fact(n) / fact(n - k)
'''

def perm(n, k):
    return fact(n) / fact(n - k)
