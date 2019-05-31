import multiprocessing
import os

def addone(num):
    return num + 1

numbers = [1, 2, 3, 4]

results = multiprocessing.Pool(4).map(addone, numbers)

print results


