#!/usr/bin/env python3
"""
Project Euler
Problems 016
Solution 1 
created on 08.02.2021
by medulka
"""

#What is the sum of the digits of the number 2^1000?
import time

def sum_of_digits(n):
    "in: a natural number (int), out: the sum of the digits (int)"
    lst = list(str(2**n))
    lst = [int(i) for i in lst]
    return sum(lst)


def main():
    n = 1000
    t1 = time.time()
    print(f"the sum of digits: {sum_of_digits(n)}")
    print(f"time: {(time.time() - t1):.5f}s")


if __name__ == '__main__':
    main()
