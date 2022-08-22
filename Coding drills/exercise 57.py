# Write a Python program to get execution time (in seconds) for a Python method.

import timeit
# timeit.timeit(setup, stmt, number)
# stmt must be a string
mycode = '''sum(range(1, 10))'''

print(timeit.timeit(mycode, number=1))
