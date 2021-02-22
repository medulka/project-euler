#!/usr/bin/env python3
"""
Project Euler
Problems 014
created on 04.02. 2021
"""

"The Collatz sequence. Which starting number, under one million, produces the longest chain?"


"pro sude n - n/2"
"pro liche n - 3n +1"
"x1 - prvni celn rady"
"xn - n-ty clen rady"  
"pc - pocetclenu rady  -> co nejvice"
"x1 - mensi nez milion"
"a - pocet cyklu"

def Collatz_sequence(upper_range):
    lst = []
    for xn in range(2,upper_range):
        a = 1
        x1 = xn
        while xn > 1:
            if xn % 2 == 0:
                xn = xn //2
                a += 1
            else: 
                xn = 3*xn + 1
                a += 1   
        lst.append((a, x1))
    return (lst)


sorted(Collatz_sequence(100),reverse = True)[0]

sorted(Collatz_sequence(1000000),reverse = True)[0]