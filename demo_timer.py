from codetimer import *
import math
import numpy as np

# Timer.default_unit = 's'

num = 500  # calculate factorial of
rep = 1000  # number of times to repeat calculation
print('Calculating factorial of', num, '\nCalculating', rep, 'times using each method')
# 1. Calculate factorial using while loops
t = Timer()  # start a timer
for _ in range(rep):
    f, i = 1, 1
    while i <= num:
        f *= i
        i += 1
print('factorial = ', f)
t.stop()  # stop the timer
print('\nTime using while loops =', t)

# 2. Calculate factorial using for loops
t = Timer()
for _ in range(rep):
    f = 1
    for i in range(1, num+1):
        f *= i
t.stop()
print('Time using for loops =', t)

# 3. Using math.factorial() function
t = Timer()
for _ in range(rep):
    f = math.factorial(num)
t.stop()
print('Time using math.factorial() =', t, '\t\t\t# best yet')

# 4. Using numpy's factorial function
t = Timer()
for _ in range(rep):
    f = np.math.factorial(num)
t.stop()
print('Time using numpy function =', t)


# 5. Using a recursive function
def fact(num):
    if num > 1:
        return num * fact(num-1)
    else:
        return 1

t = Timer()
for _ in range(rep):
    f = fact(num)
t.stop()
print('Time using recursion =', t, '\t\t\t# worse than while')


# Showing how to count passes and measure total time in loops or functions
@FunctionTimer
def facto(num):
    f = 1
    for i in range(1, num):
        f *= i
    return f

t2 = Timer()
for _ in range(rep):
    f = facto(num)  # passing timer to the function to measure internal times and counts
t2.stop()
t1 = facto.timer
print('\nTotal time =', t1, 'in', t1.count, 'iterations.')
print('Time per loop =', t1.total/t1.count, 's')
print('Time taken outside the main loop = ', t2, '\t\t# some time is lost in func calls and returns.')
