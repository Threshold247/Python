# Write a Python program to find out the number of CPUs using.

import multiprocessing


def pcores():
    logical = multiprocessing.cpu_count()
    corecount = int(logical/2)
    print(corecount)


pcores()
