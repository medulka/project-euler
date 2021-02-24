#!/usr/bin/env python3

"""
inspired by:
    Project Euler
    Problems 016
    Solution 2
    https://projecteuler.net/problem=16
created on 08.02.2021
by medulka
"""

# What is 2^1000?
# without computing with large numbers


from ProjectEuler import problem013_2
import time

def power_of_two(n):
    "in: a natural number (int), out: the n-th power of two (int)"
    a = [1]
    for i in range(0, n):
        a = problem013_2.sum_of_two_numbers(a, a)
    a = ''.join([str(i) for i in reversed(a)])
    return int(a)


def main():
    t1 = time.time()
    n = 1000
    result = power_of_two(n)
    print(f"power of two: {result}")
    print(f"time: {(time.time() - t1):.5f}s")


if __name__ == '__main__':
    main()
