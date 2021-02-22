#!/usr/bin/env python3
"""
Project Euler
Problems 012
created on 26.01.2021

"""
import time
def pocet_delitelu(n):
    "vstup: cislo, vrati: pocet delitelu"
    a = 0
    i = 1
    while i*i <= n: 
        if i*i == n:
            a = a + 1
        elif n % i == 0:
            a = a + 2            
        i += 1
    return a

def vysledek(parameter):
"vstup: pocet delitelu nejakeho cisla , vrati: triangular number "
    n = 2080
    while pocet_delitelu((n*(n+1))//2) <= parameter:
        n += 1    
    return n, (n*(n+1)//2)

t1 = time.time()
parameter = 500
vysledek(parameter)
print(time.time() - t1)
#(12375, 76576500)
#5.4s

